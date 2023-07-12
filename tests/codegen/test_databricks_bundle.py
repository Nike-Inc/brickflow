import os
from pathlib import Path
from typing import Dict, Any
from unittest.mock import patch, Mock

import yaml
from deepdiff import DeepDiff

from brickflow import BrickflowEnvVars
from brickflow.cli import BrickflowDeployMode
from brickflow.codegen.databricks_bundle import DatabricksBundleTagsAndNameMutator
from brickflow.engine.project import Stage, Project
from tests.codegen.sample_workflow import wf

BUNDLE_FILE_NAME = "bundle.yml"


def read_yaml_file(file_name: str):
    with open(file_name, "r", encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)
    return yaml_data


def assert_equal_dicts(actual: Dict[str, Any], expected: Dict[str, Any]):
    diff = DeepDiff(actual, expected)
    # pylint indicates that empty dictionary is falsey
    # diff should be empty dict
    assert not diff, diff


def get_expected_bundle_yaml(file_name):
    return read_yaml_file(str(Path(__file__).parent / f"expected_bundles/{file_name}"))


class TestBundleCodegen:
    @patch.dict(
        os.environ,
        {
            BrickflowEnvVars.BRICKFLOW_MODE.value: Stage.deploy.value,
            BrickflowEnvVars.BRICKFLOW_ENV.value: "local",
            BrickflowEnvVars.BRICKFLOW_DEPLOYMENT_MODE.value: BrickflowDeployMode.BUNDLE.value,
        },
    )
    @patch("subprocess.check_output")
    @patch("brickflow.context.ctx.dbutils_widget_get_or_else")
    @patch(
        "brickflow.codegen.databricks_bundle.DatabricksBundleTagsAndNameMutator._get_current_user_alphanumeric"
    )
    def test_generate_bundle_local(
        self,
        get_user_mock: Mock,
        dbutils: Mock,
        sub_proc_mock: Mock,
    ):
        get_user_mock.return_value = "test_user"
        dbutils.return_value = None
        sub_proc_mock.return_value = b""
        # get caller part breaks here
        with Project(
            "test-project",
            entry_point_path="test_databricks_bundle.py",
            codegen_kwargs={
                "mutators": [DatabricksBundleTagsAndNameMutator()]
            },  # dont test import mutator
        ) as f:
            f.add_workflow(wf)

        with open(BUNDLE_FILE_NAME, "r", encoding="utf-8") as bundle:
            bundle_content = bundle.read()
            assert bundle_content is not None
            assert len(bundle_content) > 0

        actual = read_yaml_file(BUNDLE_FILE_NAME)
        expected = get_expected_bundle_yaml("local_bundle.yml")
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
    @patch("subprocess.check_output")
    @patch("brickflow.context.ctx.dbutils_widget_get_or_else")
    @patch(
        "brickflow.codegen.databricks_bundle.DatabricksBundleTagsAndNameMutator._get_current_user_alphanumeric"
    )
    def test_generate_bundle_dev(
        self,
        get_user_mock: Mock,
        dbutils: Mock,
        sub_proc_mock: Mock,
    ):
        get_user_mock.return_value = "test_user"
        dbutils.return_value = None
        git_ref_b = b"a"
        git_repo = "https://github.com/"
        git_provider = "github"
        sub_proc_mock.return_value = git_ref_b
        # get caller part breaks here
        with Project(
            "test-project",
            entry_point_path="test_databricks_bundle.py",
            git_repo=git_repo,
            provider=git_provider,
            codegen_kwargs={
                "mutators": [DatabricksBundleTagsAndNameMutator()]
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
            BrickflowEnvVars.BRICKFLOW_MONOREPO_PATH_TO_BUNDLE_ROOT.value: "some/path/to/root",
        },
    )
    @patch("subprocess.check_output")
    @patch("brickflow.context.ctx.dbutils_widget_get_or_else")
    @patch(
        "brickflow.codegen.databricks_bundle.DatabricksBundleTagsAndNameMutator._get_current_user_alphanumeric"
    )
    def test_generate_bundle_dev_monorepo(
        self,
        get_user_mock: Mock,
        dbutils: Mock,
        sub_proc_mock: Mock,
    ):
        get_user_mock.return_value = "test_user"
        dbutils.return_value = None
        git_ref_b = b"a"
        git_repo = "https://github.com/"
        git_provider = "github"
        sub_proc_mock.return_value = git_ref_b
        # get caller part breaks here
        with Project(
            "test-project",
            entry_point_path="test_databricks_bundle.py",
            git_repo=git_repo,
            provider=git_provider,
            codegen_kwargs={
                "mutators": [DatabricksBundleTagsAndNameMutator()]
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
