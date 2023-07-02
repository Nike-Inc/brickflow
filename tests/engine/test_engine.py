import subprocess
from unittest.mock import patch, Mock

from brickflow.engine import (
    is_git_dirty,
    get_current_branch,
    get_current_commit,
    get_git_remote_url_https,
)


class TestEngine:
    def test_is_git_dirty(self, mocker):
        mocker.patch("subprocess.check_output")
        assert is_git_dirty() is False
        subprocess.check_output.assert_called_once_with(  # noqa
            ["git diff --stat"], shell=True
        )

    @patch("subprocess.check_output")
    def test_git_remote_url_https(self, subproc_mock: Mock):
        subproc_mock.return_value = b"git@github.com:org/repo.git"
        assert get_git_remote_url_https() == "https://github.com/org/repo"

        subproc_mock.return_value = b"something random"
        assert get_git_remote_url_https() is None

    def test_is_git_dirty_true(self, mocker):
        mocker.patch("subprocess.check_output")
        subprocess.check_output.return_value = b"superlongstringtofakedirtyrepo"
        assert is_git_dirty() is True
        subprocess.check_output.assert_called_once_with(  # noqa
            ["git diff --stat"], shell=True
        )

    def test_get_current_branch(self, mocker):
        branch = "branch"
        mocker.patch("subprocess.check_output")
        subprocess.check_output.return_value = branch.encode("utf-8")
        assert get_current_branch() == branch
        subprocess.check_output.assert_called_once_with(  # noqa
            ["git rev-parse --abbrev-ref HEAD"], shell=True
        )

    def test_get_current_commit(self, mocker):
        branch = "some_random_sha"
        mocker.patch("subprocess.check_output")
        subprocess.check_output.return_value = branch.encode("utf-8")
        assert get_current_commit() == branch
        subprocess.check_output.assert_called_once_with(  # noqa
            ['git log -n 1 --pretty=format:"%H"'], shell=True
        )
