# pylint: disable=wrong-import-position

from __future__ import annotations

import logging
import sys
from enum import Enum
from typing import List, Callable, Any

import warnings
import functools


def deprecated(func: Callable):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""

    @functools.wraps(func)
    def new_func(*args: Any, **kwargs: Any):
        warnings.simplefilter("always", DeprecationWarning)  # turn off filter
        warnings.warn(
            f"Call to deprecated function {func.__name__}.",
            category=DeprecationWarning,
            stacklevel=2,
        )
        warnings.simplefilter("default", DeprecationWarning)  # reset filter
        return func(*args, **kwargs)

    return new_func


def _insert_before_path_startswith(
    arr: List[str], value: str, new_element: str
) -> None:
    for index, item in enumerate(arr):
        if item.startswith(value):
            arr.insert(index, new_element)
            return
    arr.append(new_element)


class BrickflowProjectConstants(Enum):
    DEFAULT_MULTI_PROJECT_ROOT_FILE_NAME = ".brickflow-project-root.yml"
    DEFAULT_MULTI_PROJECT_CONFIG_FILE_NAME = "brickflow-multi-project.yml"


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
    BRICKFLOW_PROJECT_NAME = "BRICKFLOW_PROJECT_NAME"


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


# get project env for bundles
def get_bundles_project_env() -> str:
    if ctx.current_project is None:
        return ctx.env
    return f"{ctx.current_project}-{ctx.env}"


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
    NotebookTask,
)
from brickflow.engine.compute import Cluster, Runtimes
from brickflow.engine.project import Project
from brickflow.resolver import (
    RelativePathPackageResolver,
    get_relative_path_to_brickflow_root,
)

__version__ = get_brickflow_version()

__all__: List[str] = [
    "ctx",
    "get_bundles_project_env",
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
    "NotebookTask",
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
    "BrickflowProjectConstants",
]

# auto path resolver

get_relative_path_to_brickflow_root()
