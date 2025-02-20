import logging
import os
from unittest.mock import patch, Mock
from pytest import LogCaptureFixture

from brickflow import BrickflowEnvVars, _ilog
from brickflow.cli.bundles import bundle_deploy, bundle_destroy


class TestBundles:
    @patch("brickflow.cli.bundles.should_deploy", return_value=True)
    @patch("brickflow.cli.bundles.exec_command")
    @patch.dict(
        os.environ, {BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_VERSION.value: "0.203.0"}
    )
    def test_bundle_deploy_new_cli(self, mock_exec_command: Mock, _: Mock):
        mock_exec_command.side_effect = lambda *args, **kwargs: None
        mock_exec_command.return_value = None
        # workflows_dir needed to make the function work due to bundle sync
        bundle_deploy(force_acquire_lock=True, workflows_dir="somedir", debug=True)
        bundle_cli = os.environ[BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_EXEC.value]
        mock_exec_command.assert_called_with(
            bundle_cli,
            "bundle",
            ["deploy", "-t", "local", "--force-lock", "--debug"],
        )
        bundle_destroy(force_acquire_lock=True, workflows_dir="somedir", debug=True)
        bundle_cli = os.environ[BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_EXEC.value]
        mock_exec_command.assert_called_with(
            bundle_cli,
            "bundle",
            ["destroy", "-t", "local", "--force-lock", "--debug"],
        )

    @patch("brickflow.cli.bundles.should_deploy", return_value=True)
    @patch("brickflow.cli.bundles.exec_command")
    @patch.dict(
        os.environ,
        {
            BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_VERSION.value: "0.201.0",
            BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_EXEC.value: "databricks",
        },
    )
    def test_bundle_deploy_old_cli(self, mock_exec_command: Mock, _: Mock):
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

    @patch("brickflow.cli.bundles.exec_command")
    @patch.dict(
        os.environ, {BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_VERSION.value: "0.203.0"}
    )
    def test_deploy_no_workflows(
        self, mock_exec_command: Mock, caplog: LogCaptureFixture
    ):
        mock_exec_command.side_effect = lambda *args, **kwargs: None
        mock_exec_command.return_value = None

        # Adjusting the log level and propagating it to the root logger to make sure it's captured by caplog
        _ilog.propagate = True
        _ilog.level = logging.WARN

        with caplog.at_level(logging.WARN):
            # running this should not fail but log a warning stating that no bundle has been found
            bundle_deploy(force_acquire_lock=True, workflows_dir="somedir")

        assert "No bundle.yml found, skipping deployment." in [
            rec.message for rec in caplog.records
        ]
