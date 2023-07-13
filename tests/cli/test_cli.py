import os
import random
import shutil
import string
import subprocess
import traceback
from pathlib import Path
from unittest.mock import patch, Mock

import click
from click.testing import CliRunner

from brickflow.cli import (
    cli,
    bundle_download_path,
    download_and_unzip_databricks_cli,
    exec_command,
)


def fake_run(*_, **__):
    click.echo("hello world")


def fake_run_with_error(*_, **__):
    raise subprocess.CalledProcessError(
        returncode=127,
        cmd="cdktf help",
        output="cdktf help error",
        stderr="cdktf help std error",
    )


class TestCli:
    @patch("subprocess.check_output")
    @patch("os.path")
    def test_init(self, path_mock: Mock, subproc_mock: Mock, tmp_path):
        test_dir = Path(tmp_path) / "test"
        test_dir.mkdir(exist_ok=True, parents=True)
        os.chdir(str(test_dir))

        test_git_ignore = test_dir / ".gitignore"
        test_git_ignore.write_text("")

        assert test_dir.exists() is True and test_dir.is_dir()
        subproc_mock.return_value = b"https://github.com/someorg/somerepo"
        path_mock.exists.return_value = True
        path_mock.isdir.return_value = True
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "init",
                "-n",
                "test-proj",
                "-g",
                "https://github.com/someorg/somerepo",
                "-wd",
                str(test_dir),
                "-bfv",
                "0.4.0",
                "-sev",
                "0.5.0",
            ],
            "",
        )  # noqa
        assert result.exit_code == 0, traceback.print_exception(*result.exc_info)
        # result.output

    @patch("os.path")
    def test_init_no_gitignore_error(self, path_mock: Mock, tmp_path):
        test_dir = Path(tmp_path) / "test"
        test_dir.mkdir(exist_ok=True, parents=True)
        os.chdir(str(test_dir))
        path_mock.exists.return_value = True
        path_mock.isdir.return_value = True
        path_mock.isfile.return_value = False
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "init",
                "-n",
                "test-proj",
                "-g",
                "https://github.com/someorg/somerepo",
                "-wd",
                str(test_dir),
                "-bfv",
                "0.4.0",
                "-sev",
                "0.5.0",
            ],  # noqa
        )
        assert result.exit_code == 0
        assert (
            Path(test_dir / ".gitignore").exists()
            and Path(test_dir / ".gitignore").is_file()
        ) is True

    @patch("os.path")
    @patch("os.environ.copy", wraps=os.environ.copy)
    @patch("subprocess.run")
    def test_cdktf(self, run_mock: Mock, os_environ_mock: Mock, path_mock: Mock):
        runner = CliRunner()
        run_mock.side_effect = fake_run
        path_mock.exists.return_value = True
        path_mock.isdir.return_value = True
        result = runner.invoke(cli, ["cdktf", "help"])  # noqa
        assert result.exit_code == 0, traceback.print_exception(*result.exc_info)
        assert result.output.strip() == "hello world"
        run_mock.assert_called_once_with(
            ["cdktf", "help"], check=True, env=os.environ.copy()
        )
        os_environ_mock.assert_called()

    @patch("os.path")
    @patch("os.environ.copy", wraps=os.environ.copy)
    @patch("subprocess.run")
    def test_diff(self, run_mock: Mock, os_environ_mock: Mock, path_mock: Mock):
        runner = CliRunner()
        run_mock.side_effect = fake_run
        path_mock.exists.return_value = True
        path_mock.isdir.return_value = True
        result = runner.invoke(cli, ["cdktf", "diff"])  # noqa
        assert result.exit_code == 0, traceback.print_exception(*result.exc_info)
        assert result.output.strip() == "hello world"
        run_mock.assert_called_once_with(
            ["cdktf", "diff"], check=True, env=os.environ.copy()
        )
        os_environ_mock.assert_called()

    @patch("os.path")
    @patch("os.environ.copy", wraps=os.environ.copy)
    @patch("subprocess.run")
    def test_cdktf_error(self, run_mock: Mock, os_environ_mock: Mock, path_mock: Mock):
        runner = CliRunner()
        run_mock.side_effect = fake_run_with_error
        path_mock.exists.return_value = True
        path_mock.isdir.return_value = True
        result = runner.invoke(cli, ["cdktf", "help"])  # noqa
        assert result.exit_code == 1, traceback.print_exception(*result.exc_info)
        assert (
            result.output.strip()
            == "Error: Command 'cdktf help' returned non-zero exit status 127."
        )
        run_mock.assert_called_once_with(
            ["cdktf", "help"], check=True, env=os.environ.copy()
        )
        os_environ_mock.assert_called()

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
            "https://verbose-garbanzo-6b8a1ae2.pages.github.io/", new=2
        )

    @patch("os.path")
    @patch("brickflow.cli.exec_cdktf_command")
    def test_cdktf_deploy(self, exec_cdktf_mock: Mock, path_mock: Mock, tmp_path):
        runner = CliRunner()
        exec_cdktf_mock.side_effect = fake_run
        path_mock.exists.return_value = True
        path_mock.isdir.return_value = True

        # deploy with no auto approve
        working_dir = tmp_path / "".join(random.choices(string.ascii_letters, k=10))
        working_dir.mkdir()
        result = runner.invoke(
            cli, ["deploy", "--workflows-dir", str(working_dir)]
        )  # noqa
        assert result.exit_code == 0, traceback.print_exception(*result.exc_info)
        assert result.output.strip() == "hello world"
        exec_cdktf_mock.assert_called_once_with("deploy", [])

    @patch("os.path")
    @patch("brickflow.cli.exec_cdktf_command")
    def test_cdktf_deploy_auto_approve(
        self, exec_cdktf_mock: Mock, path_mock: Mock, tmp_path
    ):
        runner = CliRunner()
        exec_cdktf_mock.side_effect = fake_run
        path_mock.exists.return_value = True
        path_mock.isdir.return_value = True
        # deploy with auto approve
        working_dir = tmp_path / "".join(random.choices(string.ascii_letters, k=10))
        working_dir.mkdir()
        result = runner.invoke(
            cli, ["deploy", "--auto-approve", "--workflows-dir", str(working_dir)]
        )  # noqa
        assert result.exit_code == 0, traceback.print_exception(*result.exc_info)
        assert result.output.strip() == "hello world"
        exec_cdktf_mock.assert_called_once_with("deploy", ["--auto-approve"])

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
