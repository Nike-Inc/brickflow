# pylint: disable=wrong-import-position

from __future__ import annotations

import logging
import os
import sys
from enum import Enum
from typing import List, Callable, Any, Union, Optional

import warnings
import functools

from decouple import config


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
    BRICKFLOW_INTERACTIVE_MODE = "BRICKFLOW_INTERACTIVE_MODE"
    BRICKFLOW_BUNDLE_BASE_PATH = "BRICKFLOW_BUNDLE_BASE_PATH"
    BRICKFLOW_BUNDLE_OBJ_NAME = "BRICKFLOW_BUNDLE_OBJ_NAME"
    BRICKFLOW_BUNDLE_CLI_EXEC = "BRICKFLOW_BUNDLE_CLI_EXEC"
    BRICKFLOW_BUNDLE_NO_DOWNLOAD = "BRICKFLOW_BUNDLE_NO_DOWNLOAD"
    BRICKFLOW_BUNDLE_CLI_VERSION = "BRICKFLOW_BUNDLE_CLI_VERSION"
    BRICKFLOW_MONOREPO_PATH_TO_BUNDLE_ROOT = "BRICKFLOW_MONOREPO_PATH_TO_BUNDLE_ROOT"

    BRICKFLOW_ENABLE_PLUGINS = "BRICKFLOW_ENABLE_PLUGINS"
    BRICKFLOW_PROJECT_RUNTIME_VERSION = "BRICKFLOW_PROJECT_RUNTIME_VERSION"
    BRICKFLOW_PROJECT_NAME = "BRICKFLOW_PROJECT_NAME"
    BRICKFLOW_AUTO_ADD_LIBRARIES = "BRICKFLOW_AUTO_ADD_LIBRARIES"
    BRICKFLOW_USE_PROJECT_NAME = "BRICKFLOW_USE_PROJECT_NAME"  # for projects which injects project name to cli context
    BRICKFLOW_PROJECT_PARAMS = "BRICKFLOW_PROJECT_PARAMS"
    BRICKFLOW_PROJECT_TAGS = "BRICKFLOW_PROJECT_TAGS"


def env_chain(env_var: str, dbx_get_param: str, default: Optional[str] = None) -> str:
    from_env = config(env_var, default=None)
    if from_env is not None and isinstance(from_env, str):
        return from_env
    from_task_param = ctx.get_parameter(
        dbx_get_param,
        None,
    )
    if from_task_param is not None and isinstance(from_task_param, str):
        return from_task_param
    return default


class Empty:
    pass


class BrickflowProjectDeploymentSettings:
    def __init__(self):
        # purely here for type hinting
        self.brickflow_env = Empty()
        self.brickflow_force_deploy = Empty()
        self.brickflow_mode = Empty()
        self.brickflow_deployment_mode = Empty()
        self.brickflow_git_repo = Empty()
        self.brickflow_git_ref = Empty()
        self.brickflow_git_provider = Empty()
        self.brickflow_databricks_config_profile = Empty()
        self.brickflow_deploy_only_workflows = Empty()
        self.brickflow_workflow_prefix = Empty()
        self.brickflow_workflow_suffix = Empty()
        self.brickflow_interactive_mode = Empty()
        self.brickflow_bundle_base_path = Empty()
        self.brickflow_bundle_obj_name = Empty()
        self.brickflow_bundle_cli_exec = Empty()
        self.brickflow_bundle_no_download = Empty()
        self.brickflow_bundle_cli_version = Empty()
        self.brickflow_monorepo_path_to_bundle_root = Empty()
        self.brickflow_enable_plugins = Empty()
        self.brickflow_project_runtime_version = Empty()
        self.brickflow_project_name = Empty()
        self.brickflow_use_project_name = Empty()
        self.brickflow_auto_add_libraries = Empty()

    @staticmethod
    def _possible_string_to_bool(value: Optional[str]) -> Optional[Union[bool, str]]:
        """
        https://github.com/python/cpython/blob/878ead1ac1651965126322c1b3d124faf5484dc6/Lib/distutils/util.py#L308-L321

        Convert a string representation of truth to true (1) or false (0).

        True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
        are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
        'val' is anything else.
        """
        if value is None:
            return value
        val = value.lower()
        if val in ("y", "yes", "t", "true", "on", "1"):
            return True
        elif val in ("n", "no", "f", "false", "off", "0"):
            return False
        else:
            return value

    def __getattr__(self, attr: str) -> Union[str, bool]:
        upper_attr = attr.upper()
        if upper_attr in BrickflowEnvVars.__members__:
            value = config(upper_attr, default=None)
            log.info("Getting attr: %s which has value: %s", upper_attr, value)
            return self._possible_string_to_bool(value)
        else:
            raise AttributeError(
                f"Attribute {upper_attr} is not a valid BrickflowEnvVars"
            )

    def __setattr__(self, attr: str, value: Union[str, bool, Empty]) -> None:
        if isinstance(value, Empty):
            return
        upper_attr = attr.upper()
        if upper_attr in BrickflowEnvVars.__members__:
            log.info("Configuring attr: %s with value: %s", upper_attr, value)
            if value is None:
                os.environ.pop(upper_attr, None)
            elif isinstance(value, bool):
                os.environ[upper_attr] = str(value).lower()
            else:
                os.environ[upper_attr] = value
        else:
            raise AttributeError(
                f"Attribute {upper_attr} is not a valid BrickflowEnvVars"
            )


class BrickflowDefaultEnvs(Enum):
    LOCAL = "local"
    DEV = "dev"
    TEST = "test"
    QA = "qa"
    UAT = "uat"
    NON_PROD = "non_prod"
    PROD = "prod"


def get_entrypoint_python() -> str:
    return str(sys.executable)


def get_brickflow_version(package_name: str = "brickflows") -> str:
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

_ilog.setLevel(logging.ERROR)

log = setup_logger()

from brickflow.context import ctx


# get project env for bundles
def get_bundles_project_env() -> str:
    if (
        ctx.current_project is None
        or config(
            BrickflowEnvVars.BRICKFLOW_USE_PROJECT_NAME.value, default=True, cast=bool
        )
        is False
    ):
        return ctx.env
    return f"{ctx.current_project}-{ctx.env}"


from brickflow.engine.workflow import (
    Workflow,
    WorkflowPermissions,
    User,
    Group,
    ServicePrincipal,
    WorkflowEmailNotifications,
    WorkflowWebhookNotifications,
    WorkflowNotificationSettings,
    Trigger,
)
from brickflow.engine.task import (
    Task,
    TaskType,
    TaskSettings,
    TaskResponse,
    BrickflowTriggerRule,
    TaskRunCondition,
    Operator,
    BrickflowTaskEnvVars,
    StorageBasedTaskLibrary,
    JarTaskLibrary,
    EggTaskLibrary,
    WheelTaskLibrary,
    PypiTaskLibrary,
    MavenTaskLibrary,
    CranTaskLibrary,
    EmailNotifications,
    TaskNotificationSettings,
    DLTPipeline,
    DLTEdition,
    DLTChannels,
    NotebookTask,
    SparkJarTask,
    SparkPythonTask,
    RunJobTask,
    SqlTask,
    IfElseConditionTask,
)
from brickflow.engine.compute import Cluster, Runtimes
from brickflow.engine.project import Project
from brickflow.resolver import (
    get_relative_path_to_brickflow_root,
)

__version__ = get_brickflow_version()

__all__: List[str] = [
    "ctx",
    "get_bundles_project_env",
    "get_entrypoint_python",
    "Workflow",
    "WorkflowPermissions",
    "WorkflowEmailNotifications",
    "WorkflowWebhookNotifications",
    "WorkflowNotificationSettings",
    "TaskNotificationSettings",
    "Trigger",
    "User",
    "Group",
    "ServicePrincipal",
    "Task",
    "TaskType",
    "TaskSettings",
    "TaskResponse",
    "BrickflowTriggerRule",
    "TaskRunCondition",
    "Operator",
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
    "SparkJarTask",
    "SparkPythonTask",
    "RunJobTask",
    "DLTEdition",
    "DLTChannels",
    "Cluster",
    "Runtimes",
    "IfElseConditionTask",
    "Project",
    "SqlTask",
    "_ilog",
    "log",
    "BrickflowEnvVars",
    "BrickflowDefaultEnvs",
    "get_default_log_handler",
    "get_brickflow_version",
    "BrickflowProjectConstants",
    "BrickflowProjectDeploymentSettings",
]

# auto path resolver

get_relative_path_to_brickflow_root()
