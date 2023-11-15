import subprocess

from brickflow.engine import (
    get_current_commit,
)


class TestEngine:
    def test_get_current_commit(self, mocker):
        branch = "some_random_sha"
        mocker.patch("subprocess.check_output")
        subprocess.check_output.return_value = branch.encode("utf-8")
        assert get_current_commit() == branch
        subprocess.check_output.assert_called_once_with(
            ['git log -n 1 --pretty=format:"%H"'], shell=True
        )  # noqa
