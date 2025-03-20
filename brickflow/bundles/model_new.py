"""
This module contains the data classes for the Databricks Asset Bundles.
This is handwritten as opposed to being code generated. It leverages
the dataclasses provided by databricks-bundles and code generated from brickflow.

Right now databricks-bundles supports only Jobs and no other resources yet.

This is to avoid the need to maintain the code generated classes and to keep the
codebase clean and maintainable.
"""

import dataclasses
from dataclasses import dataclass
from typing import Dict, Optional, Union, List, Any

from databricks.bundles.core import Resource
from databricks.bundles.jobs import (
    Job as Jobs,
    JobRunAs as JobsRunAs,
)
from pydantic import BaseModel

from brickflow.bundles.model import (
    Experiments,
    ModelServingEndpoints,
    Models,
    Pipelines,
    QualityMonitors,
    RegisteredModels,
    Schemas,
    Artifacts
)


@dataclass(kw_only=True)
class Resources:
    class Config:
        extra = "forbid"
        protected_namespaces = ()

    experiments: Optional[Dict[str, Experiments]] = None
    jobs: Optional[Dict[str, Jobs]] = None
    model_serving_endpoints: Optional[Dict[str, ModelServingEndpoints]] = None
    models: Optional[Dict[str, Models]] = None
    pipelines: Optional[Dict[str, Pipelines]] = None
    quality_monitors: Optional[Dict[str, QualityMonitors]] = None
    registered_models: Optional[Dict[str, RegisteredModels]] = None
    schemas: Optional[Dict[str, Schemas]] = None


@dataclass(kw_only=True)
class DeploymentLock:
    class Config:
        extra = "forbid"
        protected_namespaces = ()

    enabled: Optional[Union[bool, str]] = None
    force: Optional[Union[bool, str]] = None


@dataclass(kw_only=True)
class Deployment:
    class Config:
        extra = "forbid"
        protected_namespaces = ()

    fail_on_active_runs: Optional[
        Union[
            bool, str,
        ]
    ] = None
    lock: Optional[DeploymentLock] = None


@dataclass(kw_only=True)
class Git:
    class Config:
        extra = "forbid"
        protected_namespaces = ()

    branch: Optional[str] = None
    origin_url: Optional[str] = None


@dataclass(kw_only=True)
class Bundle:
    class Config:
        extra = "forbid"
        protected_namespaces = ()

    name: str
    compute_id: Optional[str] = None
    databricks_cli_version: Optional[str] = None
    deployment: Optional[Deployment] = None
    git: Optional[Git] = None


@dataclass(kw_only=True)
class Permissions:
    class Config:
        extra = "forbid"
        protected_namespaces = ()

    level: str
    group_name: Optional[str] = None
    service_principal_name: Optional[str] = None
    user_name: Optional[str] = None


@dataclass(kw_only=True)
class Presets:
    class Config:
        extra = "forbid"
        protected_namespaces = ()

    jobs_max_concurrent_runs: Optional[
        Union[
            float,
            str,
        ]
    ] = None
    name_prefix: Optional[str] = None
    pipelines_development: Optional[
        Union[
            bool,
            str,
        ]
    ] = None
    tags: Optional[Dict[str, str]] = None
    trigger_pause_status: Optional[str] = None


@dataclass(kw_only=True)
class Sync:
    class Config:
        extra = "forbid"
        protected_namespaces = ()

    exclude: Optional[List[str]] = None
    include: Optional[List[str]] = None
    paths: Optional[List[str]] = None


@dataclass(kw_only=True)
class VariablesLookup:
    class Config:
        extra = "forbid"
        protected_namespaces = ()

    alert: Optional[str] = None
    cluster: Optional[str] = None
    cluster_policy: Optional[str] = None
    dashboard: Optional[str] = None
    instance_pool: Optional[str] = None
    job: Optional[str] = None
    metastore: Optional[str] = None
    pipeline: Optional[str] = None
    query: Optional[str] = None
    service_principal: Optional[str] = None
    warehouse: Optional[str] = None


@dataclass(kw_only=True)
class Variables:
    class Config:
        extra = "forbid"
        protected_namespaces = ()

    default: Optional[Any] = None
    description: Optional[str] = None
    lookup: Optional[VariablesLookup] = None
    type: Optional[str] = None


@dataclass(kw_only=True)
class Workspace:
    class Config:
        extra = "forbid"
        protected_namespaces = ()

    artifact_path: Optional[str] = None
    auth_type: Optional[str] = None
    azure_client_id: Optional[str] = None
    azure_environment: Optional[str] = None
    azure_login_app_id: Optional[str] = None
    azure_tenant_id: Optional[str] = None
    azure_use_msi: Optional[
        Union[
            bool,
            str,
        ]
    ] = None
    azure_workspace_resource_id: Optional[str] = None
    client_id: Optional[str] = None
    file_path: Optional[str] = None
    google_service_account: Optional[str] = None
    host: Optional[str] = None
    profile: Optional[str] = None
    root_path: Optional[str] = None
    state_path: Optional[str] = None


@dataclass(kw_only=True)
class Targets:
    class Config:
        extra = "forbid"
        protected_namespaces = ()

    artifacts: Optional[Dict[str, Artifacts]] = None
    bundle: Optional[Bundle] = None
    compute_id: Optional[str] = None
    default: Optional[
        Union[
            bool,
            str,
        ]
    ] = None
    git: Optional[Git] = None
    mode: Optional[str] = None
    permissions: Optional[List[Permissions]] = None
    presets: Optional[Presets] = None
    resources: Optional[Resources] = None
    # TODO: Need generic run_as even though its same schema
    run_as: Optional[JobsRunAs] = None
    sync: Optional[Sync] = None
    variables: Optional[Dict[str, Variables]] = None
    workspace: Optional[Workspace] = None


@dataclass(kw_only=True)
class ExperimentalPydabs:
    class Config:
        extra = "forbid"
        protected_namespaces = ()

    enabled: Optional[
        Union[
            bool,
            str,
        ]
    ] = None
    # needs custom as_dict
    import_: Optional[List[str]] = None
    venv_path: Optional[str] = None


@dataclass(kw_only=True)
class Experimental:
    class Config:
        extra = "forbid"
        protected_namespaces = ()

    pydabs: Optional[ExperimentalPydabs] = None
    python_wheel_wrapper: Optional[
        Union[
            bool,
            str,
        ]
    ] = None
    scripts: Optional[Dict[str, str]] = None
    use_legacy_run_as: Optional[
        Union[
            bool,
            str,
        ]
    ] = None


def convert_to_dict(obj: Any, exclude_unset: bool = True, exclude_none: bool = True) -> Union[
    Dict[str, Any], List[Any], Any]:
    """Recursively converts a dataclass or Pydantic model to a dictionary, handling dictionaries and lists."""

    if isinstance(obj, list):
        return [convert_to_dict(item, exclude_unset, exclude_none) for item in obj]

    if isinstance(obj, dict):
        return {key: convert_to_dict(value, exclude_unset, exclude_none) for key, value in obj.items()}

    # databricks resource conversion
    if isinstance(obj, Resource):
        if hasattr(obj, "as_dict"):
            return obj.as_dict()

    # generic data class conversion
    if dataclasses.is_dataclass(obj):
        data = {}
        for f in dataclasses.fields(obj):
            value = getattr(obj, f.name)

            if exclude_none and value is None:
                continue
            if exclude_unset and f.default is not None and value == f.default:
                continue

            key = "import" if f.name == "_import" else f.name
            data[key] = convert_to_dict(value, exclude_unset, exclude_none)  # Recursive conversion

        return data


    # generic pydantic model conversion
    if isinstance(obj, BaseModel):
        data = obj.dict(exclude_unset=exclude_unset, exclude_none=exclude_none)
        return {("import" if k == "_import" else k): convert_to_dict(v, exclude_unset, exclude_none) for k, v in
                data.items()}

    return obj  # Return primitive types as-is

@dataclass(kw_only=True)
class DatabricksAssetBundles:
    artifacts: Optional[Dict[str, Artifacts]] = None
    bundle: Optional[Bundle] = None
    experimental: Optional[Experimental] = None
    include: Optional[List[str]] = None
    permissions: Optional[List[Permissions]] = None
    presets: Optional[Presets] = None
    resources: Optional[Resources] = None
    # TODO: Need generic run_as even though its same schema
    run_as: Optional[JobsRunAs] = None
    sync: Optional[Sync] = None
    targets: Optional[Dict[str, Targets]] = None
    variables: Optional[Dict[str, Variables]] = None
    workspace: Optional[Workspace] = None

    def dict(self, exclude_unset: bool =True, exclude_none: bool = True):
        return convert_to_dict(self, exclude_unset=exclude_unset, exclude_none=exclude_none)
