import os
from unittest.mock import patch, Mock

from brickflow import BrickflowEnvVars
from brickflow.cli.bundles import bundle_deploy, bundle_destroy


class TestBundles:
    @patch("brickflow.cli.bundles.exec_command")
    @patch.dict(
        os.environ, {BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_VERSION.value: "0.203.0"}
    )
    def test_bundle_deploy_new_cli(self, mock_exec_command: Mock):
        mock_exec_command.side_effect = lambda *args, **kwargs: None
        mock_exec_command.return_value = None
        # workflows_dir needed to make the function work due to bundle sync
        bundle_deploy(force_acquire_lock=True, workflows_dir="somedir")
        bundle_cli = os.environ[BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_EXEC.value]
        mock_exec_command.assert_called_with(
            bundle_cli,
            "bundle",
            ["deploy", "-t", "local", "--force-lock"],
        )
        bundle_destroy(force_acquire_lock=True, workflows_dir="somedir")
        bundle_cli = os.environ[BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_EXEC.value]
        mock_exec_command.assert_called_with(
            bundle_cli,
            "bundle",
            ["destroy", "-t", "local", "--force-lock"],
        )

    @patch("brickflow.cli.bundles.exec_command")
    @patch.dict(
        os.environ,
        {
            BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_VERSION.value: "0.201.0",
            BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_EXEC.value: "databricks",
        },
    )
    def test_bundle_deploy_old_cli(self, mock_exec_command: Mock):
        mock_exec_command.side_effect = lambda *args, **kwargs: None
        mock_exec_command.return_value = None
        # workflows_dir needed to make the function work due to bundle sync
        bundle_deploy(force_acquire_lock=True, workflows_dir="somedir")
        bundle_cli = os.environ[BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_EXEC.value]
        mock_exec_command.assert_called_with(
            bundle_cli,
            "bundle",
            ["deploy", "-t", "local", "--force"],
        )
        bundle_destroy(force_acquire_lock=True, workflows_dir="somedir")
        bundle_cli = os.environ[BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_EXEC.value]
        mock_exec_command.assert_called_with(
            bundle_cli,
            "bundle",
            ["destroy", "-t", "local", "--force"],
        )
