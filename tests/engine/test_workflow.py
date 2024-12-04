from unittest.mock import patch
import pytest

import brickflow_plugins.databricks.run_job
from brickflow.bundles.model import JobsContinuous
from brickflow.engine.compute import Cluster, DuplicateClustersDefinitionError
from brickflow.engine.task import (
    Task,
    TaskType,
    BrickflowTriggerRule,
    TaskAlreadyExistsError,
    AnotherActiveTaskError,
    NoCallableTaskError,
    TaskNotFoundError,
    PypiTaskLibrary,
    WheelTaskLibrary,
    JarTaskLibrary,
)
from brickflow.engine.workflow import (
    User,
    Group,
    ServicePrincipal,
    Workflow,
    NoWorkflowComputeError,
    WorkflowConfigError,
)

# `get_job_id` is being called during workflow init, hence the patch
with patch("brickflow.engine.task.get_job_id", return_value=12345678901234):
    from tests.engine.sample_workflow import wf, task_function, run_job_task


class TestWorkflow:
    def test_add_task(self):
        t = wf.get_task(task_function.__name__)
        assert t.name == task_function.__name__
        assert t.task_func is not None
        assert t.workflow == wf
        # task compute is workflow default compute
        assert t.cluster == wf.default_cluster
        assert t.depends_on == []
        assert t.task_type == TaskType.BRICKFLOW_TASK
        assert t.trigger_rule == BrickflowTriggerRule.ALL_SUCCESS
        assert t.custom_execute_callback is None

    def test_create_workflow_no_compute(self, caplog):
        try:
            # if cluster details are not provided, the job must be treated as serverless
            Workflow("test")
            assert (
                "Default cluster details are not provided, switching to serverless compute."
                in caplog.text
            )
        except NoWorkflowComputeError:
            pytest.fail("NoWorkflowComputeError was raised")

    def test_create_workflow_with_duplicate_compute(self):
        with pytest.raises(DuplicateClustersDefinitionError):
            compute = [
                Cluster("name", "spark", "vm-node"),
                Cluster("name2", "spark1", "vm-node"),
                Cluster("name", "spark", "vm-node"),
                Cluster("name2", "spark", "vm-node"),
                Cluster("name3", "spark", "vm-node"),
            ]
            this_wf = Workflow("test", clusters=compute)
            this_wf.validate_new_clusters_with_unique_names()

    def test_create_workflow_with_unstructured_data(self):
        aws_attributes = {
            "first_on_demand": 1,
            "availability": "SPOT_WITH_FALLBACK",
            "instance_profile_arn": "arn:aws:iam::000000000000:instance-profile/lrole-testing",
            "spot_bid_price_percent": 100,
            "ebs_volume_type": "GENERAL_PURPOSE_SSD",
            "ebs_volume_count": 3,
            "ebs_volume_size": 100,
        }
        init_script = {"dbfs": "something"}
        compute = [
            Cluster(
                "name",
                "spark",
                "vm-node",
                aws_attributes=aws_attributes,
                init_scripts=[init_script],
            ),
            Cluster(
                "name2",
                "spark",
                "vm-node",
                aws_attributes=aws_attributes,
                init_scripts=[init_script],
            ),
            Cluster(
                "name3",
                "spark",
                "vm-node",
                aws_attributes=aws_attributes,
                init_scripts=[init_script],
            ),
        ]
        this_wf = Workflow("test", clusters=compute)
        this_wf.unique_new_clusters_dict()

    def test_create_workflow_with_default_cluster(self):
        cluster = Cluster(
            name="job_cluster",
            spark_version="3.3.0",
            min_workers=1,
            max_workers=3,
            node_type_id="some_node_type",
        )
        this_wf = Workflow("test", default_cluster=cluster)
        list_of_cluster_dicts = this_wf.unique_new_clusters_dict()
        assert len(list_of_cluster_dicts) == 1
        cluster_dict = list_of_cluster_dicts[0]
        assert cluster_dict["job_cluster_key"] == cluster.name
        new_cluster = cluster_dict["new_cluster"]
        for field in ["spark_version", "autoscale", "node_type_id"]:
            assert field in new_cluster

    def test_default_cluster_isnt_empty(self, caplog):
        #  pylint: disable=no-value-for-parameter
        #  pylint: disable=unexpected-keyword-arg
        try:
            compute = [
                Cluster("name", "spark", "vmnode"),
            ]
            this_wf = Workflow("test", clusters=compute)
            this_wf.default_cluster = None
            this_wf._add_task(f=lambda: 123, task_id="taskid")

            assert (
                "Default cluster details are not provided, switching to serverless compute."
                in caplog.text
            )
        except RuntimeError:
            # The error should not be raised because when default cluster is not configure, the job will be treated
            # as serverless conpute job
            pytest.fail("RuntimeError was raised")

    def test_max_tasks_reached_error(self):
        with pytest.raises(ValueError):
            compute = [
                Cluster("name", "spark", "vmnode"),
            ]
            this_wf = Workflow("test", clusters=compute, max_tasks_in_workflow=1)
            for i in range(this_wf.max_tasks_in_workflow + 1):

                @this_wf.task(name=f"task_{i}")  # noqa
                def create_task():
                    return "hello world"

    def test_create_workflow_set_default_cluster(self):
        this_wf = Workflow("test", clusters=[Cluster("name", "spark", "vm-node")])
        assert this_wf.default_cluster == this_wf.clusters[0]

    def test_add_existing_task_name(self):
        with pytest.raises(TaskAlreadyExistsError):

            @wf.task(name=task_function.__name__)
            def _(abc):
                return abc

            wf.pop_task(task_function.__name__)

    def test_another_active_task_error(self):
        task_name = "_some_task"
        with pytest.raises(AnotherActiveTaskError):

            @wf.task(name=task_name)
            def error(*, abc="def"):
                task_function()
                return abc

            error()
        wf.pop_task(task_name)

    def test_deco_no_args(self):
        with pytest.raises(NoCallableTaskError):
            wf.task("hello world")

    def test_get_tasks(self):
        assert len(wf.tasks) == 11

    def test_task_iter(self):
        arr = []
        for t in wf.task_iter():
            assert isinstance(t, Task)
            assert callable(t.task_func)
            arr.append(t)
        assert len(arr) == 11, print([t.name for t in arr])

    def test_permissions(self):
        assert wf.permissions.to_access_controls() == [
            {"permission_level": "IS_OWNER", "user_name": "abc@abc.com"},
            {"permission_level": "CAN_MANAGE", "user_name": "abc@abc.com"},
            {"permission_level": "CAN_MANAGE_RUN", "user_name": "abc@abc.com"},
            {"permission_level": "CAN_VIEW", "user_name": "abc@abc.com"},
        ]

    def test_max_concurrent_runs(self):
        assert wf.max_concurrent_runs == 1

    def test_tags(self):
        assert wf.tags == {"test": "test2"}

    def test_default_task_settings(self):
        assert wf.default_task_settings is not None

    def test_health_settings(self):
        assert wf.health == {
            "rules": [
                {"metric": "RUN_DURATION_SECONDS", "op": "GREATER_THAN", "value": 7200}
            ]
        }

    def test_timeout_seconds(self):
        assert wf.timeout_seconds == 42

    def test_user(self):
        principal = "abc@abc.com"
        u = User(principal)
        assert u.to_access_control() == {"user_name": principal}

    def test_group(self):
        principal = "abc"
        g = Group(principal)
        assert g.to_access_control() == {"group_name": principal}

    def test_service_principal(self):
        principal = "abc-123-456-678"
        sp = ServicePrincipal(principal)
        assert sp.to_access_control() == {"service_principal_name": principal}

    def test_scim_entity(self):
        principal = "abc"
        principal2 = "def"
        user1 = User(principal)
        user2 = User(principal)
        user3 = User(principal2)
        assert user2 == user1
        assert len({user1, user2}) == 1
        assert user1 != user3

    def test_key_error(self):
        with pytest.raises(TaskNotFoundError):
            wf.get_task("some_task_that_doesnt_exist")

    def test_prefix_suffix(self):
        # Test before prefix/suffix
        from tests.engine.sample_workflow_2 import wf as wf1

        assert wf1.name == "test1"

        # Test after prefix/suffix
        wf1.prefix = "prefix_string_"
        wf1.suffix = "_suffix_string"
        assert wf1.name == "prefix_string_" + "test1" + "_suffix_string"

    def test_another_workflow(self):
        from tests.engine.sample_workflow_2 import wf as wf1

        assert len(wf1.graph.nodes) == 2
        assert len(wf.graph.nodes) == 12

    def test_schedule_run_status_workflow(self):
        this_wf = Workflow("test", clusters=[Cluster("name", "spark", "vm-node")])
        assert this_wf.schedule_pause_status == "UNPAUSED"

        this_wf = Workflow(
            "test",
            clusters=[Cluster("name", "spark", "vm-node")],
            schedule_pause_status="PAUSED",
        )
        assert this_wf.schedule_pause_status == "PAUSED"

        this_wf = Workflow(
            "test",
            clusters=[Cluster("name", "spark", "vm-node")],
            schedule_pause_status="paused",
        )
        assert this_wf.schedule_pause_status == "PAUSED"

        with pytest.raises(WorkflowConfigError) as excinfo:
            Workflow(
                "test",
                clusters=[Cluster("name", "spark", "vm-node")],
                schedule_pause_status="invalid",
            )
        assert "schedule_pause_status must be one of ['PAUSED', 'UNPAUSED']" == str(
            excinfo.value
        )

    def test_schedule_continous_workflow(self):
        with pytest.raises(WorkflowConfigError) as excinfo:
            Workflow(
                "test",
                clusters=[Cluster("name", "spark", "vm-node")],
                schedule_continuous=JobsContinuous(pause_status="PAUSED"),
                schedule_quartz_expression="* * * * *",
            )
        assert (
            "Please configure either schedule_quartz_expression or schedule_continuous for workflow"
            == str(excinfo.value)
        )

        with pytest.raises(WorkflowConfigError) as excinfo:
            Workflow(
                "test",
                clusters=[Cluster("name", "spark", "vm-node")],
                schedule_continuous=JobsContinuous(pause_status="PAUSED"),
                trigger={
                    "file_arrival": {"url": "<my_url>"},
                    "pause_status": "UNPAUSED",
                },
            )
        assert (
            "Please configure either trigger or schedule_continuous for workflow"
            == str(excinfo.value)
        )

        with pytest.raises(WorkflowConfigError) as excinfo:
            Workflow(
                "test",
                clusters=[Cluster("name", "spark", "vm-node")],
                schedule_continuous=JobsContinuous(pause_status="INVALID_STATUS"),
            )
        assert (
            "Please configure either PAUSED or UNPAUSED for schedule_continuous.pause_status"
            == str(excinfo.value)
        )

    def test_add_task_for_run_job_task(self, mocker):
        with mocker.patch("brickflow_plugins.databricks.run_job.WorkspaceClient"):
            with mocker.patch.object(
                brickflow_plugins.databricks.run_job.RunJobInRemoteWorkspace,
                "execute",
                return_value="success",
            ):
                t = wf.get_task(run_job_task.__name__)
                assert t.name == run_job_task.__name__
                assert t.task_func.__name__ == "run_job_func"
                assert t.task_func() == "success"

    def test_convert_libraries_to_environments(self):
        wf_serverless = Workflow(
            "test",
            libraries=[
                PypiTaskLibrary(package="foo"),
                # PypiTaskLibrary(package="bar", repo="https://pypi.org/simple"),
                WheelTaskLibrary(whl="dbfs:/mnt/lib/baz.whl"),
                JarTaskLibrary(jar="dbfs:/mnt/lib/qux.jar"),
            ],
        )
        expect = [
            {
                "environment_key": "Default",
                "spec": {
                    "client": "1",
                    "dependencies": ["foo", "dbfs:/mnt/lib/baz.whl"],
                },
            }
        ]
        assert expect == wf_serverless.convert_libraries_to_environments

    def test_convert_libraries_to_environments_with_repo_error(self):
        with pytest.raises(WorkflowConfigError):
            Workflow(
                "test",
                libraries=[
                    PypiTaskLibrary(package="foo"),
                    PypiTaskLibrary(package="bar", repo="https://pypi.org/simple"),
                ],
            )
