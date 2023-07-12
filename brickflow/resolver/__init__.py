from __future__ import annotations

import inspect
import os
import sys
from pathlib import Path
from typing import Union, Dict, Any, List, Optional
import pathlib

from brickflow import BrickflowProjectConstants, _ilog, ctx


def add_to_sys_path(directory: Union[str, pathlib.Path]):
    dir_str = str(directory)
    if dir_str not in sys.path and os.path.isdir(dir_str):
        sys.path.append(dir_str)


def get_caller_file_paths() -> List[str]:
    caller_file_paths = []
    frames = inspect.stack()[1:]  # Exclude the current frame

    for frame in frames:
        caller_file_paths.append(frame.filename)

    return list(set(caller_file_paths))


class BrickflowRootNotFound(Exception):
    pass


def go_up_till_brickflow_root(path: str) -> str:
    if path.startswith("<"):
        raise BrickflowRootNotFound("Invalid brickflow root.")

    path = pathlib.Path(path).resolve()

    valid_roots = [
        BrickflowProjectConstants.DEFAULT_MULTI_PROJECT_ROOT_FILE_NAME.value,
        BrickflowProjectConstants.DEFAULT_MULTI_PROJECT_CONFIG_FILE_NAME.value,
    ]

    # recurse to see if there is a brickflow root and return the path
    while not path.is_dir() or not any(
        file.name in valid_roots for file in path.iterdir()
    ):
        path = path.parent

        if path == path.parent:
            raise BrickflowRootNotFound(
                "Brickflow root directory not found in path hierarchy."
            )

    return str(path.resolve())


def get_relative_path_to_brickflow_root() -> None:
    paths = get_caller_file_paths()
    _ilog.info("Brickflow setting up python path resolution...")
    # if inside notebook also get that path
    notebook_path = get_notebook_path(ctx.dbutils)
    if notebook_path is not None:
        paths.append(notebook_path)

    for path in paths:
        try:
            resolved_path = go_up_till_brickflow_root(path)
            _ilog.info("Brickflow root input path - %s", path)
            _ilog.info("Brickflow root found - %s", resolved_path)
            add_to_sys_path(resolved_path)
            _ilog.info("Sys path set to: %s", str(sys.path))
        except BrickflowRootNotFound:
            _ilog.info("Unable to find for path: %s", path)
        # print(path)


def get_notebook_path(dbutils: Optional[Any]) -> Optional[str]:
    if dbutils is not None:
        return (
            dbutils.notebook.entry_point.getDbutils()
            .notebook()
            .getContext()
            .notebookPath()
            .get()
        )
    return None


class RelativePathPackageResolver:
    @staticmethod
    def _get_current_file_path(global_vars: Dict[str, Any]):
        if "dbutils" in global_vars:
            get_notebook_path(global_vars["dbutils"])
        else:
            return global_vars["__file__"]

    @staticmethod
    def add_relative_path(
        global_vars: Dict[str, Any],
        current_file_to_root: str,
        root_to_module: str = ".",
    ) -> None:
        # root to module must always be relative to the root of the project (i.e. must not start with "/")
        if root_to_module.startswith("/"):
            raise ValueError(
                f"root_to_module must be relative to the root of the project. "
                f"It must not start with '/'. root_to_module: {root_to_module}"
            )
        p = (
            Path(RelativePathPackageResolver._get_current_file_path(global_vars)).parent
            / Path(current_file_to_root)
            / root_to_module
        )
        path = p.resolve()
        add_to_sys_path(path)
