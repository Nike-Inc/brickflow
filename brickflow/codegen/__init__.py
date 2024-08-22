import abc
from enum import Enum
from pathlib import Path

from typing import TYPE_CHECKING, Optional, Dict, Any

from decouple import config

from brickflow import get_brickflow_version, BrickflowEnvVars, BrickflowDefaultEnvs

if TYPE_CHECKING:
    from brickflow.engine.project import _Project


class CodegenInterface(abc.ABC):
    def __init__(
        self, project: "_Project", id_: str, env: str, **_: Any
    ) -> None:  # noqa
        self.env: str = env
        self.project: "_Project" = project
        self.id_ = id_

    @abc.abstractmethod
    def synth(self) -> None:
        pass


class DatabricksDefaultClusterTagKeys(Enum):
    ENVIRONMENT = "environment"
    DEPLOYED_BY = "deployed_by"
    DEPLOYED_AT = "deployed_at"
    BRICKFLOW_PROJECT_NAME = "brickflow_project_name"
    BRICKFLOW_DEPLOYMENT_MODE = "brickflow_deployment_mode"
    DATABRICKS_TF_PROVIDER_VERSION = "databricks_tf_provider_version"
    BRICKFLOW_VERSION = "brickflow_version"


BRICKFLOW_BUILTIN_DEPLOY_TAGS = {
    "brickflow_version": get_brickflow_version()
    or "undefined",  # certain scenarios get_brickflow_version maybe None
}


def get_brickflow_tags(
    user_defined_tags: Optional[Dict[str, str]], other_tags: Dict[str, str]
) -> Dict[str, str]:
    return {**(user_defined_tags or {}), **other_tags, **BRICKFLOW_BUILTIN_DEPLOY_TAGS}


def handle_mono_repo_path(project: "_Project", env: str) -> str:
    base_path = config(
        BrickflowEnvVars.BRICKFLOW_MONOREPO_PATH_TO_BUNDLE_ROOT.value, None
    )

    if project.entry_point_path is None:
        raise ValueError("project.entry_point_path is None")

    if base_path is None or env == BrickflowDefaultEnvs.LOCAL.value:
        return project.entry_point_path
    else:
        return str(Path(base_path) / project.entry_point_path)
