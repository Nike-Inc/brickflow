# pylint: disable=wrong-import-position

from __future__ import annotations

import logging
import os
import sys
from enum import Enum
from pathlib import Path
from typing import List, Dict, Any, Union


def _insert_before_path_startswith(
    arr: List[str], value: str, new_element: str
) -> None:
    for index, item in enumerate(arr):
        if item.startswith(value):
            arr.insert(index, new_element)
            return
    arr.append(new_element)


class RelativePathPackageResolver:
    @staticmethod
    def _get_current_file_path(global_vars):
        if "dbutils" in global_vars:
            return (
                global_vars["dbutils"]
                .notebook.entry_point.getDbutils()
                .notebook()
                .getContext()
                .notebookPath()
                .get()
            )
        else:
            return global_vars["__file__"]

    @staticmethod
    def _add_to_sys_path(directory: Union[str, Path]):
        dir_str = str(directory)
        if dir_str not in sys.path and os.path.isdir(dir_str):
            sys.path.append(dir_str)

    @staticmethod
    def add_relative_path(
        global_vars: Dict[str, Any],
        current_file_to_root: str,
        root_to_module: str = ".",
    ):
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
        RelativePathPackageResolver._add_to_sys_path(path)


class BrickflowEnvVars(Enum):
    BRICKFLOW_ENV = "BRICKFLOW_ENV"
    BRICKFLOW_FORCE_DEPLOY = "BRICKFLOW_FORCE_DEPLOY"
    BRICKFLOW_MODE = "BRICKFLOW_MODE"
    BRICKFLOW_DEPLOYMENT_MODE = "BRICKFLOW_DEPLOYMENT_MODE"
    BRICKFLOW_GIT_REPO = "BRICKFLOW_GIT_REPO"
    BRICKFLOW_GIT_REF = "BRICKFLOW_GIT_REF"
    BRICKFLOW_GIT_PROVIDER = "BRICKFLOW_GIT_PROVIDER"
    BRICKFLOW_DATABRICKS_CONFIG_PROFILE = "DATABRICKS_CONFIG_PROFILE"
    BRICKFLOW_DEPLOY_ONLY_WORKFLOWS = "BRICKFLOW_DEPLOY_ONLY_WORKFLOWS"
    BRICKFLOW_WORKFLOW_PREFIX = "BRICKFLOW_WORKFLOW_PREFIX"
    BRICKFLOW_WORKFLOW_SUFFIX = "BRICKFLOW_WORKFLOW_SUFFIX"
    BRICKFLOW_S3_BACKEND_BUCKET = "BRICKFLOW_S3_BACKEND_BUCKET"
    BRICKFLOW_S3_BACKEND_KEY = "BRICKFLOW_S3_BACKEND_KEY"
    BRICKFLOW_S3_BACKEND_REGION = "BRICKFLOW_S3_BACKEND_REGION"
    BRICKFLOW_S3_BACKEND_DYNAMODB_TABLE = "BRICKFLOW_S3_BACKEND_DYNAMODB_TABLE"
    BRICKFLOW_INTERACTIVE_MODE = "BRICKFLOW_INTERACTIVE_MODE"
    BRICKFLOW_BUNDLE_BASE_PATH = "BRICKFLOW_BUNDLE_BASE_PATH"
    BRICKFLOW_BUNDLE_OBJ_NAME = "BRICKFLOW_BUNDLE_OBJ_NAME"
    BRICKFLOW_BUNDLE_CLI_EXEC = "BRICKFLOW_BUNDLE_CLI_EXEC"
    BRICKFLOW_BUNDLE_NO_DOWNLOAD = "BRICKFLOW_BUNDLE_NO_DOWNLOAD"
    BRICKFLOW_BUNDLE_CLI_VERSION = "BRICKFLOW_BUNDLE_CLI_VERSION"
    BRICKFLOW_MONOREPO_PATH_TO_BUNDLE_ROOT = "BRICKFLOW_MONOREPO_PATH_TO_BUNDLE_ROOT"


class BrickflowDefaultEnvs(Enum):
    LOCAL = "local"
    DEV = "dev"
    TEST = "test"
    QA = "qa"
    UAT = "uat"
    NON_PROD = "non_prod"
    PROD = "prod"


def get_brickflow_version(package_name: str = "brickflow") -> str:
    try:
        from importlib import metadata  # type: ignore
    except ImportError:
        # Python < 3.8
        import importlib_metadata as metadata  # type: ignore

    try:
        return metadata.version(package_name)  # type: ignore
    except metadata.PackageNotFoundError:  # type: ignore
        return "unknown"


def get_default_log_handler(pkg_name="brickflow-framework"):
    logger_handler = logging.StreamHandler(stream=sys.stdout)
    version = get_brickflow_version()
    logger_handler.setFormatter(
        logging.Formatter(
            f"[%(asctime)s] [%(levelname)s] [{pkg_name}-{version}] "
            "{%(module)s.py:%(funcName)s:%(lineno)d} - %(message)s"
        )
    )
    return logger_handler


def setup_logger(name=None):
    _log = logging.getLogger(name or __name__)  # Logger
    _log.setLevel(logging.INFO)
    logger_handler = get_default_log_handler()
    _log.propagate = False
    if _log.hasHandlers():
        _log.handlers.clear()
    _log.addHandler(logger_handler)
    return _log


_ilog = setup_logger("brickflow-internal")
"""logger for internal logging please do not use outside of brickflow internal"""
log = setup_logger()

from brickflow.context import ctx
from brickflow.engine.workflow import (
    Workflow,
    WorkflowPermissions,
    User,
    Group,
    ServicePrincipal,
)
from brickflow.engine.task import (
    Task,
    TaskType,
    TaskSettings,
    TaskResponse,
    BrickflowTriggerRule,
    BrickflowTaskEnvVars,
    StorageBasedTaskLibrary,
    JarTaskLibrary,
    EggTaskLibrary,
    WheelTaskLibrary,
    PypiTaskLibrary,
    MavenTaskLibrary,
    CranTaskLibrary,
    EmailNotifications,
    DLTPipeline,
    DLTEdition,
    DLTChannels,
)
from brickflow.engine.compute import Cluster, Runtimes
from brickflow.engine.project import Project

__version__ = get_brickflow_version()

__all__: List[str] = [
    "ctx",
    "Workflow",
    "WorkflowPermissions",
    "User",
    "Group",
    "ServicePrincipal",
    "Task",
    "TaskType",
    "TaskSettings",
    "TaskResponse",
    "BrickflowTriggerRule",
    "BrickflowTaskEnvVars",
    "StorageBasedTaskLibrary",
    "JarTaskLibrary",
    "EggTaskLibrary",
    "WheelTaskLibrary",
    "PypiTaskLibrary",
    "MavenTaskLibrary",
    "CranTaskLibrary",
    "EmailNotifications",
    "DLTPipeline",
    "DLTEdition",
    "DLTChannels",
    "Cluster",
    "Runtimes",
    "Project",
    "_ilog",
    "log",
    "BrickflowEnvVars",
    "BrickflowDefaultEnvs",
    "get_default_log_handler",
    "get_brickflow_version",
    "RelativePathPackageResolver",
]
