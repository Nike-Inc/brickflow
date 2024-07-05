import os
from pathlib import Path
from typing import Dict, Any
from unittest.mock import patch, Mock, MagicMock

import yaml
from deepdiff import DeepDiff

from brickflow import BrickflowEnvVars
from brickflow.bundles.model import (
    Resources,
    Jobs,
    JobsTasks,
    Pipelines,
    PipelinesLibraries,
    PipelinesLibrariesNotebook,
    PipelinesClusters,
    DatabricksAssetBundles,
)
from brickflow.cli import BrickflowDeployMode
from brickflow.codegen import DatabricksDefaultClusterTagKeys
from brickflow.codegen.databricks_bundle import (
    DatabricksBundleTagsAndNameMutator,
    DatabricksBundleImportMutator,
    DatabricksBundleCodegen,
    ImportBlock,
    ImportManager,
)
from brickflow.engine.project import Stage, Project
from brickflow.engine.task import NotebookTask
from tests.codegen.sample_workflows import wf
from tests.codegen.sample_workflows import wf2

# BUNDLE_FILE_NAME = str(Path(__file__).parent / f"bundle.yml")
BUNDLE_FILE_NAME = "bundle.yml"


def read_yaml_file(file_name: str):
    with open(file_name, "r", encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)
    return yaml_data


def normalize_bundle_via_pydantic(d: Dict[str, Any]) -> Dict[str, Any]:
    return DatabricksAssetBundles.parse_obj(d).dict()


def assert_equal_dicts(actual: Dict[str, Any], expected: Dict[str, Any]):
    diff = DeepDiff(
        normalize_bundle_via_pydantic(expected),
        normalize_bundle_via_pydantic(actual),
        ignore_order=True,
    )
    print(diff)
    # pylint indicates that empty dictionary is falsey
    # diff should be empty dict
    assert not diff, diff


def get_expected_bundle_yaml(file_name):
    return read_yaml_file(str(Path(__file__).parent / f"expected_bundles/{file_name}"))


def get_workspace_client_mock() -> MagicMock:
    workspace_client = MagicMock()
    workspace_client.current_user.me.return_value.user_name = "test_user"
    return workspace_client


class TestBundleCodegen:
    @patch.dict(
        os.environ,
        {
            BrickflowEnvVars.BRICKFLOW_MODE.value: Stage.deploy.value,
            BrickflowEnvVars.BRICKFLOW_ENV.value: "local",
            BrickflowEnvVars.BRICKFLOW_DEPLOYMENT_MODE.value: BrickflowDeployMode.BUNDLE.value,
        },
    )
    @patch("brickflow.engine.task.get_job_id", return_value=12345678901234.0)
    @patch("subprocess.check_output")
    @patch("brickflow.context.ctx.get_parameter")
    @patch("importlib.metadata.version")
    def test_generate_bundle_local(
        self,
        bf_version_mock: Mock,
        dbutils: Mock,
        sub_proc_mock: Mock,
        get_job_id_mock: Mock,
    ):
        dbutils.return_value = None
        sub_proc_mock.return_value = b""
        bf_version_mock.return_value = "1.0.0"
        workspace_client = get_workspace_client_mock()
        get_job_id_mock.return_value = 12345678901234.0
        # get caller part breaks here
        with Project(
            "test-project",
            entry_point_path="test_databricks_bundle.py",
            codegen_kwargs={
                "mutators": [
                    DatabricksBundleTagsAndNameMutator(
                        databricks_client=workspace_client
                    )
                ]
            },  # dont test import mutator
        ) as f:
            f.add_workflow(wf)

        with open(BUNDLE_FILE_NAME, "r", encoding="utf-8") as bundle:
            bundle_content = bundle.read()
            assert bundle_content is not None
            assert len(bundle_content) > 0

        actual = read_yaml_file(BUNDLE_FILE_NAME)
        expected = get_expected_bundle_yaml("local_bundle.yml")
        bf_version_mock.assert_called_once()
        assert_equal_dicts(actual, expected)
        if os.path.exists(BUNDLE_FILE_NAME):
            os.remove(BUNDLE_FILE_NAME)

    @patch.dict(
        os.environ,
        {
            BrickflowEnvVars.BRICKFLOW_MODE.value: Stage.deploy.value,
            BrickflowEnvVars.BRICKFLOW_ENV.value: "local",
            BrickflowEnvVars.BRICKFLOW_DEPLOYMENT_MODE.value: BrickflowDeployMode.BUNDLE.value,
            BrickflowEnvVars.BRICKFLOW_WORKFLOW_PREFIX.value: "_prefix",
            BrickflowEnvVars.BRICKFLOW_WORKFLOW_SUFFIX.value: "_suffix",
        },
    )
    @patch("brickflow.engine.task.get_job_id", return_value=12345678901234.0)
    @patch("subprocess.check_output")
    @patch("brickflow.context.ctx.get_parameter")
    @patch("importlib.metadata.version")
    def test_generate_bundle_local_prefix_suffix(
        self,
        bf_version_mock: Mock,
        dbutils: Mock,
        sub_proc_mock: Mock,
        get_job_id_mock: Mock,
    ):
        dbutils.return_value = None
        sub_proc_mock.return_value = b""
        bf_version_mock.return_value = "1.0.0"
        workspace_client = get_workspace_client_mock()
        get_job_id_mock.return_value = 12345678901234.0
        # get caller part breaks here
        with Project(
            "test-project",
            entry_point_path="test_databricks_bundle.py",
            codegen_kwargs={
                "mutators": [
                    DatabricksBundleTagsAndNameMutator(
                        databricks_client=workspace_client
                    )
                ]
            },  # dont test import mutator
        ) as f:
            f.add_workflow(wf)

        with open(BUNDLE_FILE_NAME, "r", encoding="utf-8") as bundle:
            bundle_content = bundle.read()
            assert bundle_content is not None
            assert len(bundle_content) > 0

        actual = read_yaml_file(BUNDLE_FILE_NAME)
        expected = get_expected_bundle_yaml("local_bundle_prefix_suffix.yml")
        bf_version_mock.assert_called_once()
        assert_equal_dicts(actual, expected)
        if os.path.exists(BUNDLE_FILE_NAME):
            os.remove(BUNDLE_FILE_NAME)

    @patch.dict(
        os.environ,
        {
            BrickflowEnvVars.BRICKFLOW_MODE.value: Stage.deploy.value,
            BrickflowEnvVars.BRICKFLOW_ENV.value: "dev",
            BrickflowEnvVars.BRICKFLOW_DEPLOYMENT_MODE.value: BrickflowDeployMode.BUNDLE.value,
        },
    )
    @patch("brickflow.engine.task.get_job_id", return_value=12345678901234.0)
    @patch("subprocess.check_output")
    @patch("brickflow.context.ctx.get_parameter")
    @patch("importlib.metadata.version")
    def test_generate_bundle_dev(
        self,
        bf_version_mock: Mock,
        dbutils: Mock,
        sub_proc_mock: Mock,
        get_job_id_mock: Mock,
    ):
        dbutils.return_value = None
        git_ref_b = b"a"
        git_repo = "https://github.com/"
        git_provider = "github"
        sub_proc_mock.return_value = git_ref_b
        bf_version_mock.return_value = "1.0.0"
        get_job_id_mock.return_value = 12345678901234.0

        workspace_client = get_workspace_client_mock()

        # get caller part breaks here
        with Project(
            "test-project",
            entry_point_path="test_databricks_bundle.py",
            git_repo=git_repo,
            provider=git_provider,
            codegen_kwargs={
                "mutators": [DatabricksBundleTagsAndNameMutator(workspace_client)]
            },  # dont test import mutator
        ) as f:
            f.add_workflow(wf)

        assert f.git_reference == "commit/" + git_ref_b.decode("utf-8")
        assert f.git_repo == git_repo
        assert f.provider == git_provider
        with open(BUNDLE_FILE_NAME, "r", encoding="utf-8") as bundle:
            bundle_content = bundle.read()
            assert bundle_content is not None
            assert len(bundle_content) > 0

        actual = read_yaml_file(BUNDLE_FILE_NAME)
        expected = get_expected_bundle_yaml("dev_bundle_polyrepo.yml")
        assert_equal_dicts(actual, expected)
        if os.path.exists(BUNDLE_FILE_NAME):
            os.remove(BUNDLE_FILE_NAME)

    @patch.dict(
        os.environ,
        {
            BrickflowEnvVars.BRICKFLOW_MODE.value: Stage.deploy.value,
            BrickflowEnvVars.BRICKFLOW_ENV.value: "dev",
            BrickflowEnvVars.BRICKFLOW_DEPLOYMENT_MODE.value: BrickflowDeployMode.BUNDLE.value,
            BrickflowEnvVars.BRICKFLOW_AUTO_ADD_LIBRARIES.value: "true",
            BrickflowEnvVars.BRICKFLOW_PROJECT_RUNTIME_VERSION.value: "0.1.0",
        },
    )
    @patch("brickflow.engine.task.get_job_id", return_value=12345678901234.0)
    @patch("subprocess.check_output")
    @patch("brickflow.context.ctx.get_parameter")
    @patch("importlib.metadata.version")
    def test_generate_bundle_dev_auto_add_libs(
        self,
        bf_version_mock: Mock,
        dbutils: Mock,
        sub_proc_mock: Mock,
        get_job_id_mock: Mock,
    ):
        dbutils.return_value = None
        git_ref_b = b"a"
        git_repo = "https://github.com/"
        git_provider = "github"
        sub_proc_mock.return_value = git_ref_b
        bf_version_mock.return_value = "1.0.0"
        get_job_id_mock.return_value = 12345678901234.0

        workspace_client = get_workspace_client_mock()

        # get caller part breaks here
        with Project(
            "test-project",
            entry_point_path="test_databricks_bundle.py",
            git_repo=git_repo,
            provider=git_provider,
            codegen_kwargs={
                "mutators": [DatabricksBundleTagsAndNameMutator(workspace_client)]
            },  # dont test import mutator
        ) as f:
            f.add_workflow(wf)
            from brickflow import Workflow, Cluster

            fake_workflow = Workflow(
                "some_wf",
                default_cluster=Cluster.from_existing_cluster("some-id"),
                enable_plugins=True,
            )

            @fake_workflow.task
            def some_task():
                pass

            f.add_workflow(fake_workflow)

        assert f.git_reference == "commit/" + git_ref_b.decode("utf-8")
        assert f.git_repo == git_repo
        assert f.provider == git_provider
        with open(BUNDLE_FILE_NAME, "r", encoding="utf-8") as bundle:
            bundle_content = bundle.read()
            assert bundle_content is not None
            assert len(bundle_content) > 0

        actual = read_yaml_file(BUNDLE_FILE_NAME)
        expected = get_expected_bundle_yaml("dev_bundle_polyrepo_with_auto_libs.yml")
        assert_equal_dicts(actual, expected)
        if os.path.exists(BUNDLE_FILE_NAME):
            os.remove(BUNDLE_FILE_NAME)

    @patch.dict(
        os.environ,
        {
            BrickflowEnvVars.BRICKFLOW_MODE.value: Stage.deploy.value,
            BrickflowEnvVars.BRICKFLOW_ENV.value: "dev",
            BrickflowEnvVars.BRICKFLOW_DEPLOYMENT_MODE.value: BrickflowDeployMode.BUNDLE.value,
            BrickflowEnvVars.BRICKFLOW_MONOREPO_PATH_TO_BUNDLE_ROOT.value: "some/path/to/root",
        },
    )
    @patch("brickflow.engine.task.get_job_id", return_value=12345678901234.0)
    @patch("subprocess.check_output")
    @patch("brickflow.context.ctx.get_parameter")
    @patch("importlib.metadata.version")
    def test_generate_bundle_dev_monorepo(
        self,
        bf_version_mock: Mock,
        dbutils: Mock,
        sub_proc_mock: Mock,
        get_job_id_mock: Mock,
    ):
        dbutils.return_value = None
        git_ref_b = b"a"
        git_repo = "https://github.com/"
        git_provider = "github"
        sub_proc_mock.return_value = git_ref_b
        bf_version_mock.return_value = "1.0.0"
        get_job_id_mock.return_value = 12345678901234.0

        workspace_client = get_workspace_client_mock()

        # get caller part breaks here
        with Project(
            "test-project",
            entry_point_path="test_databricks_bundle.py",
            git_repo=git_repo,
            provider=git_provider,
            codegen_kwargs={
                "mutators": [DatabricksBundleTagsAndNameMutator(workspace_client)]
            },  # dont test import mutator
        ) as f:
            f.add_workflow(wf)

        assert f.git_reference == "commit/" + git_ref_b.decode("utf-8")
        assert f.git_repo == git_repo
        assert f.provider == git_provider
        with open(BUNDLE_FILE_NAME, "r", encoding="utf-8") as bundle:
            bundle_content = bundle.read()
            assert bundle_content is not None
            assert len(bundle_content) > 0

        actual = read_yaml_file(BUNDLE_FILE_NAME)
        expected = get_expected_bundle_yaml("dev_bundle_monorepo.yml")
        assert_equal_dicts(actual, expected)
        if os.path.exists(BUNDLE_FILE_NAME):
            os.remove(BUNDLE_FILE_NAME)

    def test_mutators(self):
        job_name = "test-job"
        pipeline_name = "test-pipeline"
        fake_job_id = "some-id"
        fake_pipeline_id = "fake-pipeline-id"
        fake_user_name = "test_user"
        fake_user_email = f"{fake_user_name}@fakedomain.com"
        project_name = "test-project"
        databricks_fake_client = MagicMock()
        fake_job = MagicMock()
        fake_pipeline = MagicMock()
        fake_pipeline_cluster = MagicMock()
        project = MagicMock()

        databricks_fake_client.jobs.list.return_value = [fake_job]
        databricks_fake_client.current_user.me.return_value.user_name = fake_user_email

        fake_job.job_id = fake_job_id
        fake_job.settings.tags = {
            DatabricksDefaultClusterTagKeys.BRICKFLOW_PROJECT_NAME.value: project_name
        }
        fake_pipeline.pipeline_id = fake_pipeline_id
        fake_pipeline.clusters = [fake_pipeline_cluster]
        fake_pipeline_cluster.custom_tags = {
            DatabricksDefaultClusterTagKeys.BRICKFLOW_PROJECT_NAME.value: project_name
        }
        project.name = project_name
        import_mutator = DatabricksBundleImportMutator(databricks_fake_client)
        tag_and_name_mutator = DatabricksBundleTagsAndNameMutator(
            databricks_fake_client
        )

        code_gen = DatabricksBundleCodegen(
            project, "some-id", "local", mutators=[tag_and_name_mutator, import_mutator]
        )
        resource = Resources(
            jobs={
                job_name: Jobs(
                    name=job_name,
                    tasks=[
                        JobsTasks(
                            notebook_task=NotebookTask(notebook_path="test-notebook"),
                            task_key="somekey",
                        ),
                    ],
                )
            },
            pipelines={
                pipeline_name: Pipelines(
                    name=pipeline_name,
                    clusters=[PipelinesClusters(custom_tags={"test": "test"})],
                    libraries=[
                        PipelinesLibraries(
                            notebook=PipelinesLibrariesNotebook(path="test-notebook")
                        )
                    ],
                )
            },
        )

        code_gen.proj_to_bundle()
        import_mutator.mutate_resource(
            resource=resource,
            ci=code_gen,
        )
        tag_and_name_mutator.mutate_resource(
            resource=resource,
            ci=code_gen,
        )

        assert code_gen.imports == [
            ImportBlock(to=f"databricks_job.{job_name}", id_=fake_job_id)
        ]
        databricks_fake_client.jobs.list.assert_called_once_with(name=job_name)
        databricks_fake_client.current_user.me.assert_called_once()
        # pylint: disable=unsubscriptable-object
        jobs: dict = resource.jobs
        assert (
            jobs is not None and jobs[job_name].name == f"{fake_user_name}_{job_name}"
        )

    def test_import_blocks(self):
        # Databricks object ids are either strings or integers
        block1 = ImportBlock(to="test", id_=1)
        block2 = ImportBlock(to="test_2", id_="test")
        blocks = [block1, block2]
        expected_output = """import { 
  to = test 
  id = "1" 
}

import { 
  to = test_2 
  id = "test" 
}"""
        assert (
            ImportManager.create_import_str(blocks).strip() == expected_output.strip()
        ), "Import blocks are not equal"

    @patch.dict(
        os.environ,
        {
            BrickflowEnvVars.BRICKFLOW_MODE.value: Stage.deploy.value,
            BrickflowEnvVars.BRICKFLOW_ENV.value: "local",
            BrickflowEnvVars.BRICKFLOW_DEPLOYMENT_MODE.value: BrickflowDeployMode.BUNDLE.value,
        },
    )
    @patch("brickflow.engine.task.get_job_id", return_value=12345678901234.0)
    @patch("subprocess.check_output")
    @patch("brickflow.context.ctx.get_parameter")
    @patch("importlib.metadata.version")
    def test_schedule_continuous(
        self,
        bf_version_mock: Mock,
        dbutils: Mock,
        sub_proc_mock: Mock,
        get_job_id_mock: Mock,
    ):
        dbutils.return_value = None
        sub_proc_mock.return_value = b""
        bf_version_mock.return_value = "1.0.0"
        workspace_client = get_workspace_client_mock()
        get_job_id_mock.return_value = 12345678901234.0
        # get caller part breaks here
        with Project(
            "test-project",
            entry_point_path="test_databricks_bundle.py",
            codegen_kwargs={
                "mutators": [
                    DatabricksBundleTagsAndNameMutator(
                        databricks_client=workspace_client
                    )
                ]
            },  # dont test import mutator
        ) as f:
            f.add_workflow(wf2)

        with open(BUNDLE_FILE_NAME, "r", encoding="utf-8") as bundle:
            bundle_content = bundle.read()
            assert bundle_content is not None
            assert len(bundle_content) > 0

        actual = read_yaml_file(BUNDLE_FILE_NAME)
        expected = get_expected_bundle_yaml("local_bundle_continuous_schedule.yml")
        bf_version_mock.assert_called_once()
        assert_equal_dicts(actual, expected)
        if os.path.exists(BUNDLE_FILE_NAME):
            os.remove(BUNDLE_FILE_NAME)

    @patch.dict(
        os.environ,
        {
            BrickflowEnvVars.BRICKFLOW_MODE.value: Stage.deploy.value,
            BrickflowEnvVars.BRICKFLOW_ENV.value: "local",
            BrickflowEnvVars.BRICKFLOW_DEPLOYMENT_MODE.value: BrickflowDeployMode.BUNDLE.value,
        },
    )
    @patch("brickflow.engine.task.get_job_id", return_value=12345678901234.0)
    @patch("subprocess.check_output")
    @patch("brickflow.context.ctx.get_parameter")
    @patch("importlib.metadata.version")
    def test_selected_workflows(
        self,
        bf_version_mock: Mock,
        dbutils: Mock,
        sub_proc_mock: Mock,
        get_job_id_mock: Mock,
    ):
        dbutils.return_value = None
        sub_proc_mock.return_value = b""
        bf_version_mock.return_value = "1.0.0"
        workspace_client = get_workspace_client_mock()
        get_job_id_mock.return_value = 12345678901234.0
        # get caller part breaks here
        with Project(
            "test-project",
            entry_point_path="test_databricks_bundle.py",
            codegen_kwargs={
                "mutators": [
                    DatabricksBundleTagsAndNameMutator(
                        databricks_client=workspace_client
                    )
                ]
            },  # dont test import mutator
        ) as f:
            # f.add_workflow(wf)
            f.add_workflow(wf2)

        with open(BUNDLE_FILE_NAME, "r", encoding="utf-8") as bundle:
            bundle_content = bundle.read()
            assert bundle_content is not None
            assert len(bundle_content) > 0

        actual = read_yaml_file(BUNDLE_FILE_NAME)
        expected = get_expected_bundle_yaml("local_bundle_continuous_schedule.yml")
        bf_version_mock.assert_called_once()
        assert_equal_dicts(actual, expected)
        if os.path.exists(BUNDLE_FILE_NAME):
            os.remove(BUNDLE_FILE_NAME)
