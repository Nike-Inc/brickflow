import os
import shutil
import traceback
from unittest.mock import patch, Mock

import click
from click.testing import CliRunner

from brickflow import BrickflowProjectDeploymentSettings
from brickflow.cli import (
    cli,
    exec_command,
)
from brickflow.cli.bundles import (
    bundle_download_path,
    download_and_unzip_databricks_cli,
)
from brickflow.cli.projects import handle_libraries


def fake_run(*_, **__):
    click.echo("hello world")


# TODO: Add more tests to the cli
class TestCli:
    def test_no_command_error(self):
        runner = CliRunner()
        non_existent_command = "non_existent_command"
        result = runner.invoke(cli, ["non_existent_command"])  # noqa
        assert result.exit_code == 2
        assert result.output.strip().endswith(
            f"Error: No such command '{non_existent_command}'."
        )

    @patch("webbrowser.open")
    def test_docs(self, browser: Mock):
        runner = CliRunner()
        browser.return_value = None
        result = runner.invoke(cli, ["docs"])  # noqa
        assert result.exit_code == 0, traceback.print_exception(*result.exc_info)
        assert result.output.strip().startswith("Opening browser for docs...")
        browser.assert_called_once_with(
            "https://engineering.nike.com/brickflow/", new=2
        )

    def test_install_cli(self):
        expected_version = "0.200.0"
        url = bundle_download_path(expected_version)
        file_path = download_and_unzip_databricks_cli(url, expected_version)
        assert url is not None
        version_value = exec_command(file_path, "--version", [], capture_output=True)
        assert (
            version_value.strip() == f"Databricks CLI v{expected_version}"
        ), version_value
        directory_path = ".databricks"
        if os.path.exists(directory_path):
            shutil.rmtree(directory_path)

    def test_projects_handle_libraries(self):
        bpd = BrickflowProjectDeploymentSettings()
        bpd.brickflow_auto_add_libraries = None
        handle_libraries(skip_libraries=True)
        assert bpd.brickflow_auto_add_libraries is False
        handle_libraries(skip_libraries=False)
        assert bpd.brickflow_auto_add_libraries is True
        bpd.brickflow_auto_add_libraries = None
