import os
from pathlib import Path
from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

import yaml
from deepdiff import DeepDiff

from brickflow import BrickflowEnvVars
from brickflow.bundles.model import (
    DatabricksAssetBundles,
)
from brickflow.cli import BrickflowDeployMode
from brickflow.codegen.databricks_bundle import (
    DatabricksBundleTagsAndNameMutator,
)
from brickflow.engine.project import Project, Stage

from tests.codegen.sample_serverless_workflow import wf

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
    # pylint indicates that empty dictionary is false
    # diff should be empty dict
    assert not diff, diff


def get_expected_bundle_yaml(file_name):
    return read_yaml_file(str(Path(__file__).parent / f"expected_bundles/{file_name}"))


def get_workspace_client_mock() -> MagicMock:
    workspace_client = MagicMock()
    workspace_client.current_user.me.return_value.user_name = "test_user"
    return workspace_client


class TestServerlessBundleCodegen(TestCase):
    @patch.dict(
        os.environ,
        {
            BrickflowEnvVars.BRICKFLOW_MODE.value: Stage.deploy.value,
            BrickflowEnvVars.BRICKFLOW_ENV.value: "local",
            BrickflowEnvVars.BRICKFLOW_DEPLOYMENT_MODE.value: BrickflowDeployMode.BUNDLE.value,
        },
    )
    @patch("subprocess.check_output")
    @patch("brickflow.context.ctx.get_parameter")
    @patch("importlib.metadata.version")
    @patch(
        "brickflow.context.ctx.get_current_timestamp",
        MagicMock(return_value=1704067200000),
    )
    def test_generate_bundle_local(
        self,
        bf_version_mock: Mock,
        dbutils: Mock,
        sub_proc_mock: Mock,
    ):
        dbutils.return_value = None
        sub_proc_mock.return_value = b""
        bf_version_mock.return_value = "1.0.0"
        workspace_client = get_workspace_client_mock()
        # get caller part breaks here
        with Project(
            "test-serverless-project",
            entry_point_path="test_databricks_serverless_bundle.py",
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
        expected = get_expected_bundle_yaml("local_serverless_bundle.yml")
        bf_version_mock.assert_called_once()
        assert_equal_dicts(actual, expected)
        if os.path.exists(BUNDLE_FILE_NAME):
            os.remove(BUNDLE_FILE_NAME)
