import datetime
from collections import namedtuple
from unittest.mock import MagicMock, Mock, patch

import pytest
from deepdiff import DeepDiff
from pydantic import SecretStr

from brickflow import (
    BrickflowProjectDeploymentSettings,
    IfElseConditionTask,
    SparkJarTask,
    SparkPythonTask,
)
from brickflow.bundles.model import (
    JobsTasks,
    JobsTasksWebhookNotifications,
)
from brickflow.context import (
    BRANCH_SKIP_EXCEPT,
    RETURN_VALUE_KEY,
    SKIP_EXCEPT_HACK,
    BrickflowInternalVariables,
    ctx,
)
from brickflow.engine.task import (
    CranTaskLibrary,
    EggTaskLibrary,
    EmailNotifications,
    ForEachTask,
    InvalidTaskLibraryError,
    InvalidTaskSignatureDefinition,
    JarTaskLibrary,
    JobsTasksForEachTaskConfigs,
    MavenTaskLibrary,
    PypiTaskLibrary,
    TaskLibrary,
    TaskSettings,
    WheelTaskLibrary,
    get_brickflow_lib_version,
    get_brickflow_libraries,
    get_brickflow_tasks_hook,
    get_plugin_manager,
    TaskType,
)
from brickflow.engine.utils import get_job_id
from tests.engine.sample_workflow import (
    custom_python_task_push,
    task_function,
    task_function_2,
    task_function_3,
    task_function_4,
    task_function_nokwargs,
    task_function_with_error,
    wf,
)


class TestTask:
    builtin_task_params = {
        "brickflow_job_id": "{{job_id}}",
        "brickflow_run_id": "{{run_id}}",
        "brickflow_start_date": "{{start_date}}",
        "brickflow_start_time": "{{start_time}}",
        "brickflow_task_retry_count": "{{task_retry_count}}",
        "brickflow_parent_run_id": "{{parent_run_id}}",
        "brickflow_task_key": "{{task_key}}",
    }

    def test_builtin_notebook_params(self):
        assert (
            wf.get_task(task_function.__name__).builtin_notebook_params
            == self.builtin_task_params
        )

    def test_builtin_default_params(self):
        assert wf.get_task(task_function.__name__).brickflow_default_params == {
            "brickflow_internal_workflow_name": wf.name,
            "brickflow_internal_task_name": "{{task_key}}",
            "brickflow_internal_only_run_tasks": "",
            "brickflow_internal_workflow_prefix": "",
            "brickflow_internal_workflow_suffix": "",
            "brickflow_env": ctx.env,
        }

        wf.prefix = "my_prefix"
        wf.suffix = "my_suffix"
        assert wf.get_task(task_function.__name__).brickflow_default_params == {
            "brickflow_internal_workflow_name": wf.name,
            "brickflow_internal_task_name": "{{task_key}}",
            "brickflow_internal_only_run_tasks": "",
            "brickflow_internal_workflow_prefix": "my_prefix",
            "brickflow_internal_workflow_suffix": "my_suffix",
            "brickflow_env": ctx.env,
        }

    def test_custom_task_params(self):
        assert wf.get_task(task_function.__name__).custom_task_parameters == {
            "all_tasks1": "test",
            "all_tasks3": "123",
            "test": "var",
        }
        assert wf.get_task(task_function_nokwargs.__name__).custom_task_parameters == {
            "all_tasks1": "test",
            "all_tasks3": "123",
        }

        wf.common_task_parameters = {
            "all_tasks1": "test",
            "all_tasks3": "123",
            "test": "to_be_overridden",  # This should be overridden by the task argument passed with same key
        }
        assert wf.get_task(task_function.__name__).custom_task_parameters == {
            "all_tasks1": "test",
            "all_tasks3": "123",
            "test": "var",
        }
        wf.common_task_parameters = {}
        assert wf.get_task(task_function_nokwargs.__name__).custom_task_parameters == {}

    def test_task_settings(self):
        assert wf.get_task(task_function.__name__).task_settings is None

    def test_parents(self):
        assert wf.get_task(task_function_2.__name__).parents == ["task_function"]

    def test_task_type(self):
        assert (
            wf.get_task(task_function_2.__name__).databricks_task_type_str
            == "notebook_task"
        )

    def test_depends_on(self):
        assert wf.get_task(task_function_3.__name__).depends_on == ["task_function_2"]
        assert wf.get_task(task_function_2.__name__).depends_on == [task_function]
        assert wf.get_task(task_function.__name__).depends_on == []

    def test_invalid_task_signature(self):
        with pytest.raises(InvalidTaskSignatureDefinition):
            # missing * and kwargs
            @wf.task
            def _fake_task1(test):  # noqa
                # pylint: disable=unused-argument
                pass

        with pytest.raises(InvalidTaskSignatureDefinition):
            # missing *
            @wf.task
            def _fake_task2(test="test"):  # noqa
                # pylint: disable=unused-argument
                pass

    @pytest.mark.parametrize(
        "test_input",
        [123413, 13231.32, b"test", False, {"test": "test"}, ["hello"], (2, 3)],
    )
    def test_invalid_task_signature_objects(self, test_input):
        with pytest.raises(InvalidTaskSignatureDefinition):
            # doesnt support bytes-like
            @wf.task(name=f"fake_task_{str(test_input)}")
            def _fake_task(*, test=test_input):  # noqa
                # pylint: disable=unused-argument
                pass

    @patch("brickflow.context.ctx._task_coms")
    def test_should_skip_false(self, task_coms_mock: Mock):
        task_coms_mock.get.return_value = task_function_3.__name__
        skip, reason = wf.get_task(task_function_3.__name__).should_skip()
        assert skip is False
        assert reason is None
        task_coms_mock.get.assert_called_once()
        ctx._configure()

        task_coms_mock.get.value = task_function.__name__
        task_coms_mock.get.side_effect = Exception("error")
        skip, reason = wf.get_task(task_function_3.__name__).should_skip()
        assert skip is False
        assert reason is None
        ctx._configure()

        skip, reason = wf.get_task(task_function.__name__).should_skip()
        assert skip is False
        assert reason is None
        ctx._configure()

        skip, reason = wf.get_task(task_function_4.__name__).should_skip()
        assert skip is False
        assert reason is None
        ctx._configure()

    @pytest.mark.parametrize(
        "tasks",
        [
            "somethingelse",  # other task
            f"[{task_function_4.__name__}]",  # invalid JSON list defaults to no skip
        ],
    )
    @patch("brickflow.context.ctx.get_parameter")
    def test_skip_not_selected_task(self, dbutils, tasks):
        dbutils.return_value = tasks
        skip, reason = wf.get_task(
            task_function_4.__name__
        )._skip_because_not_selected()
        dbutils.assert_called_once_with(
            BrickflowInternalVariables.only_run_tasks.value, ""
        )
        assert skip is True
        assert reason.startswith(
            f"This task: {task_function_4.__name__} is not a selected task"
        )
        assert wf.get_task(task_function_4.__name__).execute() is None

    @pytest.mark.parametrize(
        "tasks",
        [
            task_function_4.__name__,  # clean string
            f'["{task_function_4.__name__}"]',  # clean JSON list
            f'["  {task_function_4.__name__}  "]',  # spaced JSON list
            f"  {task_function_4.__name__}  ",  # spaced string
        ],
    )
    @patch("brickflow.context.ctx.get_parameter")
    def test_no_skip_selected_task(self, dbutils, tasks):
        dbutils.return_value = tasks
        skip, reason = wf.get_task(
            task_function_4.__name__
        )._skip_because_not_selected()
        dbutils.assert_called_once_with(
            BrickflowInternalVariables.only_run_tasks.value, ""
        )
        assert skip is False
        assert reason is None
        assert wf.get_task(task_function_4.__name__).execute() == task_function_4()

    @patch("brickflow.engine.task.Task._skip_because_not_selected")
    @patch("brickflow.context.ctx._task_coms")
    def test_should_skip_true(
        self, task_coms_mock: Mock, task_skip_selected_mock: Mock
    ):
        task_skip_selected_mock.return_value = (False, None)
        task_coms_mock.get.value = task_function_2.__name__
        skip, reason = wf.get_task(task_function_3.__name__).should_skip()
        assert skip is True
        assert reason == "All tasks before this were not successful"
        task_coms_mock.get.assert_called_once()
        assert wf.get_task(task_function_3.__name__).execute() is None
        task_coms_mock.put.assert_called_once_with(
            task_function_3.__name__, BRANCH_SKIP_EXCEPT, SKIP_EXCEPT_HACK
        )

    @patch("brickflow.context.ctx.get_parameter")
    @patch("brickflow.context.ctx._task_coms")
    def test_execute(self, task_coms_mock: Mock, dbutils: Mock):
        dbutils.return_value = ""
        resp = wf.get_task(task_function.__name__).execute()
        task_coms_mock.put.assert_called_once_with(
            task_function.__name__, RETURN_VALUE_KEY, task_function()
        )

        assert resp is task_function()

    @patch("brickflow.context.ctx.get_parameter")
    def test_execute_with_error(self, dbutils: Mock):
        dbutils.return_value = ""
        get_plugin_manager.cache_clear()
        get_brickflow_tasks_hook.cache_clear()
        with pytest.raises(
            ValueError,
            match="BRICKFLOW_USER_OR_DBR_ERROR: This is an error thrown in user code.",
        ):
            wf.get_task(task_function_with_error.__name__).execute()

    @patch("brickflow.context.ctx.get_parameter")
    @patch("brickflow.context.ctx._task_coms")
    def test_execute_custom(self, task_coms_mock: Mock, dbutils: Mock):
        dbutils.return_value = ""
        resp = wf.get_task(custom_python_task_push.__name__).execute()
        task_coms_mock.put.assert_called_once_with(
            custom_python_task_push.__name__,
            RETURN_VALUE_KEY,
            custom_python_task_push.__name__,
        )

        assert resp is custom_python_task_push.__name__

    def test_email_notifications(self):
        email_arr = ["abc@abc.com"]
        en = EmailNotifications(
            on_start=email_arr,
            on_failure=email_arr,
            on_success=email_arr,
        )
        assert en.to_tf_dict() == {
            "on_start": email_arr,
            "on_failure": email_arr,
            "on_success": email_arr,
        }

    def test_task_settings_tf_dict(self):
        email_arr = ["abc@abc.com"]
        wn = JobsTasksWebhookNotifications(
            on_duration_warning_threshold_exceeded=[{"id": "123"}],
            on_failure=[{"id": "123"}],
            on_start=[{"id": "123"}],
            on_streaming_backlog_exceeded=[{"id": "123"}],
            on_success=[{"id": "123"}],
        )
        default_int = 10
        default_bool = True
        en = EmailNotifications(
            on_start=email_arr,
            on_failure=email_arr,
            on_success=email_arr,
        )
        ts = TaskSettings(
            email_notifications=en,
            timeout_seconds=default_int,
            max_retries=default_int,
            min_retry_interval_millis=default_int,
            retry_on_timeout=default_bool,
            webhook_notifications=wn,
        )
        assert ts.to_tf_dict() == {
            "email_notifications": en.to_tf_dict(),
            "timeout_seconds": default_int,
            "max_retries": default_int,
            "min_retry_interval_millis": default_int,
            "retry_on_timeout": default_bool,
            "webhook_notifications": wn,
        }

    def test_task_settings_merge(self):
        email_arr = ["abc@abc.com"]
        other_email_arr = ["new@new.com"]
        default_int = 10
        other_default_int = 20
        default_bool = True
        en = EmailNotifications(
            on_start=email_arr,
            on_failure=email_arr,
            on_success=email_arr,
        )
        other_en = EmailNotifications(
            on_start=other_email_arr,
            on_failure=other_email_arr,
        )
        wn = JobsTasksWebhookNotifications(
            on_duration_warning_threshold_exceeded=[{"id": "123"}],
            on_failure=[{"id": "123"}],
            on_start=[{"id": "123"}],
            on_streaming_backlog_exceeded=[{"id": "123"}],
            on_success=[{"id": "123"}],
        )
        other_wn = JobsTasksWebhookNotifications(
            on_duration_warning_threshold_exceeded=[{"id": "124"}],
            on_failure=[{"id": "124"}],
            on_start=[{"id": "124"}],
            on_streaming_backlog_exceeded=[{"id": "124"}],
            on_success=[{"id": "124"}],
        )
        ts = TaskSettings(
            email_notifications=en,
            timeout_seconds=default_int,
            max_retries=default_int,
            min_retry_interval_millis=default_int,
            retry_on_timeout=default_bool,
            webhook_notifications=wn,
        )
        other_ts = TaskSettings(
            email_notifications=other_en,
            timeout_seconds=other_default_int,
            max_retries=other_default_int,
            retry_on_timeout=default_bool,
            webhook_notifications=other_wn,
        )

        final_ts = ts.merge(other_ts)
        assert final_ts.to_tf_dict() == {
            "email_notifications": other_en.to_tf_dict(),
            "timeout_seconds": other_default_int,
            "max_retries": other_default_int,
            "min_retry_interval_millis": default_int,
            "retry_on_timeout": default_bool,
            "webhook_notifications": other_wn,
        }

        final_ts = ts.merge(None)
        assert final_ts.to_tf_dict() == {
            "email_notifications": en.to_tf_dict(),
            "timeout_seconds": default_int,
            "max_retries": default_int,
            "min_retry_interval_millis": default_int,
            "retry_on_timeout": default_bool,
            "webhook_notifications": wn,
        }

    def test_task_settings_small_timeout(self):
        small_to = TaskSettings(
            timeout_seconds=30,
        )
        print(small_to.timeout_seconds)
        assert not wf.log_timeout_warning(small_to)

    def test_task_settings_big_timeout_warning(self):
        big_to = TaskSettings(
            timeout_seconds=datetime.timedelta(hours=0.5).seconds,
        )
        print(big_to.timeout_seconds)
        assert wf.log_timeout_warning(big_to)

    def test_task_settings_no_timeout_warning(self):
        no_to = TaskSettings()
        print(no_to.timeout_seconds)
        assert not wf.log_timeout_warning(no_to)

    def test_task_libraries(self):
        s3_path = "s3://somepath-in-s3"
        repo = "somerepo"
        package = "somepackage"
        coordinates = package
        exclusions = None
        assert JarTaskLibrary(s3_path).dict == {"jar": s3_path}
        assert EggTaskLibrary(s3_path).dict == {"egg": s3_path}
        assert WheelTaskLibrary(s3_path).dict == {"whl": s3_path}
        assert PypiTaskLibrary(package, repo).dict == {
            "pypi": {"package": package, "repo": repo}
        }
        assert MavenTaskLibrary(coordinates, repo, exclusions).dict == {
            "maven": {
                "coordinates": coordinates,
                "repo": repo,
                "exclusions": exclusions,
            }
        }
        assert CranTaskLibrary(package, repo).dict == {
            "cran": {"package": package, "repo": repo}
        }

    def test_invalid_storage_library_path(self):
        with pytest.raises(InvalidTaskLibraryError):
            JarTaskLibrary("somebadpath")

    def test_task_library_unique_list(self):
        s3_path = "s3://somepath-in-s3"
        assert TaskLibrary.unique_libraries(
            [
                JarTaskLibrary(s3_path),
                JarTaskLibrary(s3_path),
            ]
        ) == [JarTaskLibrary(s3_path)]

        assert not TaskLibrary.unique_libraries(None)

    def test_get_brickflow_lib_version(self):
        settings = BrickflowProjectDeploymentSettings()
        InputOutput = namedtuple(
            "MyNamedTuple", ["bf_version", "cli_version", "expected_version"]
        )

        input_outputs = [
            InputOutput("1.0.0", "1.0.0", "1.0.0"),
            InputOutput("1.0.0rc12312", "1.0.0", "v1.0.0rc12312"),
            InputOutput("main", "1.0.0", "main"),
            InputOutput("auto", "0.1.0rcabc12e312", "main"),
            InputOutput("auto", "0.1.0", "0.1.0"),
            InputOutput("auto", "something", "main"),
            InputOutput("v1.0.0", "something", "1.0.0"),
        ]
        for input_output in input_outputs:
            settings.brickflow_project_runtime_version = input_output.bf_version
            assert (
                get_brickflow_lib_version(
                    input_output.bf_version, input_output.cli_version
                )
                == input_output.expected_version
            )
            settings.brickflow_project_runtime_version = None

    # TODO: parameterize these tests
    def test_get_brickflow_libraries(self):
        settings = BrickflowProjectDeploymentSettings()
        settings.brickflow_project_runtime_version = "1.0.0"
        assert len(get_brickflow_libraries(enable_plugins=True)) == 6
        assert len(get_brickflow_libraries(enable_plugins=False)) == 1
        lib = get_brickflow_libraries(enable_plugins=False)[0].dict
        expected = {
            "pypi": {
                "package": "brickflows==1.0.0",
                "repo": None,
            }
        }
        diff = DeepDiff(expected, lib)
        assert not diff, diff

    def test_get_brickflow_libraries_semver_non_numeric(self):
        settings = BrickflowProjectDeploymentSettings()
        tag = "1.0.1rc1234"
        settings.brickflow_project_runtime_version = tag
        assert len(get_brickflow_libraries(enable_plugins=True)) == 6
        assert len(get_brickflow_libraries(enable_plugins=False)) == 1
        lib = get_brickflow_libraries(enable_plugins=False)[0].dict
        expected = {
            "pypi": {
                "package": f"brickflows @ git+https://github.com/Nike-Inc/brickflow.git@v{tag}",
                "repo": None,
            }
        }
        diff = DeepDiff(expected, lib)
        assert not diff, diff

    def test_get_brickflow_libraries_non_semver(self):
        settings = BrickflowProjectDeploymentSettings()
        tag = "somebranch"
        settings.brickflow_project_runtime_version = tag
        assert len(get_brickflow_libraries(enable_plugins=True)) == 6
        assert len(get_brickflow_libraries(enable_plugins=False)) == 1
        lib = get_brickflow_libraries(enable_plugins=False)[0].dict
        expected = {
            "pypi": {
                "package": f"brickflows @ git+https://github.com/Nike-Inc/brickflow.git@{tag}",
                "repo": None,
            }
        }
        diff = DeepDiff(expected, lib)
        assert not diff, diff

    @patch("brickflow.engine.utils.WorkspaceClient")
    def test_get_job_id(self, mock_workspace_client) -> None:
        # Arrange
        mock_workspace_client.return_value.jobs.list.return_value = [
            MagicMock(job_id=123)
        ]
        job_name = "test_job"
        host = "https://databricks-instance"
        token = SecretStr("token")

        # Act
        result = get_job_id(job_name, host, token)

        # Assert
        assert result == 123

    @patch("brickflow.engine.utils.WorkspaceClient")
    def test_get_job_id_no_job_found(self, mock_workspace_client) -> None:
        # Arrange
        mock_workspace_client.return_value.jobs.list.return_value = []
        job_name = "test_job"
        host = "https://databricks-instance"
        token = SecretStr("token")

        # Act and Assert
        try:
            get_job_id(job_name, host, token)
            assert False, "Expected ValueError"
        except ValueError:
            pass

    def test_init_spark_jar(self):
        task = SparkJarTask(
            main_class_name="MainClass",
            jar_uri="test_uri",
            parameters=["param1", "param2"],
        )
        assert task.main_class_name == "MainClass"
        assert task.jar_uri == "test_uri"
        assert task.parameters == ["param1", "param2"]

    def test_without_params_spark_jar(self):
        task = SparkJarTask(main_class_name="MainClass", jar_uri="test_uri")
        assert task.main_class_name == "MainClass"
        assert task.jar_uri == "test_uri"
        assert task.parameters is None

    def test_init_spark_python(self):
        task = SparkPythonTask(
            python_file="./products/test-project/path/to/python/file.py",
            source="GIT",
            parameters=["--param1", "World!"],
        )
        assert task.python_file == "./products/test-project/path/to/python/file.py"
        assert task.source == "GIT"
        assert task.parameters == ["--param1", "World!"]

    def test_without_params_spark_python(self):
        task = SparkPythonTask(
            python_file="./products/test-project/path/to/python/file.py",
        )
        assert task.python_file == "./products/test-project/path/to/python/file.py"
        assert task.source is None
        assert task.parameters is None

    def if_else_condition_task(self):
        # Test the __init__ method
        instance = IfElseConditionTask(left="left_value", right="right_value", op="==")
        assert instance.left == "left_value"
        assert instance.right == "right_value"
        assert instance.op == "=="

    @patch("brickflow.bundles.model.JobsTasksSqlTaskAlert")
    @patch("brickflow.engine.task.SqlTask")
    def test_alert_creation(self, mock_sql_task, mock_alert):
        mock_alert_instance = MagicMock()
        mock_alert_instance.alert_id = "alert1"
        mock_alert_instance.pause_subscriptions = False
        mock_alert_instance.subscriptions = {
            "usernames": ["user1", "user2"],
            "destination_id": ["dest1", "dest2"],
        }
        mock_alert.return_value = mock_alert_instance

        mock_sql_task_instance = MagicMock()
        mock_sql_task_instance.alert = mock_alert_instance
        mock_sql_task.return_value = mock_sql_task_instance

        sql_task = mock_sql_task(
            query_id="query1",
            file_path="path/to/file",  # sample test file
            alert_id="alert1",
            pause_subscriptions=False,
            subscriptions={
                "usernames": ["user1", "user2"],
                "destination_id": ["dest1", "dest2"],
            },
            dashboard_id="dashboard1",
            dashboard_custom_subject="custom subject",
            warehouse_id="warehouse1",
        )
        assert isinstance(sql_task.alert, MagicMock)
        assert sql_task.alert.alert_id == "alert1"
        assert sql_task.alert.pause_subscriptions is False
        assert len(sql_task.alert.subscriptions) == 2

    @patch("brickflow.bundles.model.JobsTasksSqlTaskDashboard")
    @patch("brickflow.engine.task.SqlTask")
    def test_dashboard_creation(self, mock_sql_task, mock_dashboard):
        mock_dashboard_instance = MagicMock()
        mock_dashboard_instance.dashboard_id = "dashboard1"
        mock_dashboard_instance.custom_subject = "custom subject"
        mock_dashboard_instance.pause_subscriptions = False
        mock_dashboard_instance.subscriptions = {
            "usernames": ["user1", "user2"],
            "destination_id": ["dest1", "dest2"],
        }
        mock_dashboard.return_value = mock_dashboard_instance

        mock_sql_task_instance = MagicMock()
        mock_sql_task_instance.dashboard = mock_dashboard_instance
        mock_sql_task.return_value = mock_sql_task_instance

        sql_task = mock_sql_task(
            query_id="query1",
            file_path="path/to/file",
            alert_id="alert1",
            pause_subscriptions=False,
            subscriptions={
                "usernames": ["user1", "user2"],
                "destination_id": ["dest1", "dest2"],
            },
            dashboard_id="dashboard1",
            dashboard_custom_subject="custom subject",
            warehouse_id="warehouse1",
        )
        assert isinstance(sql_task.dashboard, MagicMock)
        assert sql_task.dashboard.dashboard_id == "dashboard1"
        assert sql_task.dashboard.custom_subject == "custom subject"
        assert sql_task.dashboard.pause_subscriptions is False
        assert len(sql_task.dashboard.subscriptions) == 2

    def test_for_each_task_validation(self):
        for_each_task = ForEachTask(
            configs=JobsTasksForEachTaskConfigs(
                inputs=["input1", "input2"], concurrency=2
            ),
            task=JobsTasks(task_key="task_key"),
        )

        assert for_each_task.inputs == '["input1", "input2"]'

    @pytest.mark.parametrize(
        "task_type", [(TaskType.IF_ELSE_CONDITION_TASK,), (TaskType.FOR_EACH_TASK,)]
    )
    def task_settings_filtered_out(self, task_type):
        """timeout settings and retry settings should be filtered out for if/else and for-each tasks"""
        task_settings = TaskSettings(
            timeout_seconds=30,
            max_retries=3,
            min_retry_interval_millis=1000,
            retry_on_timeout=True,
        )

        actual = task_settings.to_tf_dict(task_type)
        assert "timeout_seconds" not in actual
        assert "max_retries" not in actual

    def task_settings_not_filtered(self):
        task_settings = TaskSettings(
            timeout_seconds=30,
            max_retries=3,
            min_retry_interval_millis=1000,
            retry_on_timeout=True,
        )

        actual = task_settings.to_tf_dict()
        assert "timeout_seconds" in actual
        assert "max_retries" in actual

    def test_for_each_task_validation_task_type(self):
        # Valid task type
        for_each_task = ForEachTask(
            configs=JobsTasksForEachTaskConfigs(
                inputs=["input1", "input2"],
                concurrency=2,
                task_type=TaskType.NOTEBOOK_TASK,
            ),
            task=JobsTasks(task_key="task_key"),
        )
        assert for_each_task.configs.task_type == TaskType.NOTEBOOK_TASK

        # Not providing a task type should set task type to None
        for_each_task = ForEachTask(
            configs=JobsTasksForEachTaskConfigs(
                inputs=["input1", "input2"], concurrency=2
            ),
            task=JobsTasks(task_key="task_key"),
        )
        assert for_each_task.configs.task_type is None

        # Setting a task type with a value other than the valid ones should raise a ValueError
        with pytest.raises(ValueError):
            ForEachTask(
                configs=JobsTasksForEachTaskConfigs(
                    inputs=["input1", "input2"],
                    concurrency=2,
                    task_type=TaskType.IF_ELSE_CONDITION_TASK,
                ),
                task=JobsTasks(task_key="task_key"),
            )
