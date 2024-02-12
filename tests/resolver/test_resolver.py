# test_resolver.py
from typing import Type

import pytest

import brickflow
from brickflow.resolver import (
    BrickflowRootNotFound,
)


@pytest.fixture
def default_mocks(mocker):
    # Create mocks for the three methods
    mocker.patch(
        "brickflow.resolver.get_caller_file_paths", return_value=["path1", "path2"]
    )
    mocker.patch(
        "brickflow.resolver.get_notebook_ws_path", return_value="/notebook/ws/path"
    )


def test_resolver_methods(default_mocks, mocker):  # noqa
    error_msg = "This is a test message"

    def make_exception_function(exc: Type[Exception]):
        def raise_exception(*args, **kwargs):
            raise exc(error_msg)

        return raise_exception

    # catch random error
    mocker.patch(
        "brickflow.resolver.go_up_till_brickflow_root",
        side_effect=make_exception_function(ValueError),
    )
    with pytest.raises(ValueError, match=error_msg):
        brickflow.resolver.get_relative_path_to_brickflow_root()

    mocker.patch(
        "brickflow.resolver.go_up_till_brickflow_root",
        side_effect=make_exception_function(BrickflowRootNotFound),
    )

    brickflow.resolver.get_relative_path_to_brickflow_root()

    mocker.patch(
        "brickflow.resolver.go_up_till_brickflow_root",
        side_effect=make_exception_function(PermissionError),
    )

    brickflow.resolver.get_relative_path_to_brickflow_root()
