import importlib
import importlib.util
import inspect
import os
import sys
from dataclasses import field, dataclass
from enum import Enum
from pathlib import Path
from types import ModuleType
from typing import Dict, Optional, List, Any, Type

from decouple import config

from brickflow import _ilog, BrickflowEnvVars
from brickflow.cli import BrickflowDeployMode
from brickflow.codegen import CodegenInterface
from brickflow.codegen.databricks_bundle import DatabricksBundleCodegen
from brickflow.codegen.hashicorp_cdktf import HashicorpCDKTFGen
from brickflow.context import ctx, BrickflowInternalVariables
from brickflow.engine import get_current_commit
from brickflow.engine.task import TaskLibrary
from brickflow.engine.utils import wraps_keyerror
from brickflow.engine.workflow import Workflow


class WorkflowAlreadyExistsError(Exception):
    pass


class WorkflowNotFoundError(Exception):
    pass


class DeployError(Exception):
    pass


class ExecuteError(Exception):
    pass


# TODO: Logging
@dataclass(frozen=True)
class _Project:
    name: str
    git_repo: Optional[str] = None
    provider: Optional[str] = None
    git_reference: Optional[str] = None
    s3_backend: Optional[Dict[str, str]] = None
    entry_point_path: Optional[str] = None
    workflows: Dict[str, Workflow] = field(default_factory=lambda: {})
    libraries: Optional[List[TaskLibrary]] = None
    batch: bool = True
    bundle_obj_name: Optional[str] = None
    bundle_base_path: Optional[str] = None

    def add_pkg(self, pkg: ModuleType) -> None:
        file_name = pkg.__file__
        if file_name is None:
            raise ImportError(f"Invalid pkg error: {str(pkg)}")
        actual_workflow_dir_files = os.listdir(os.path.dirname(file_name))

        if os.getenv(BrickflowEnvVars.BRICKFLOW_ENV.value) == "local":
            if BrickflowEnvVars.BRICKFLOW_DEPLOY_ONLY_WORKFLOWS.value in os.environ:
                deploy_only_workflow_files = os.getenv(  # type: ignore
                    BrickflowEnvVars.BRICKFLOW_DEPLOY_ONLY_WORKFLOWS.value
                ).split(",")
                files_not_in_actual = [
                    file
                    for file in deploy_only_workflow_files
                    if file not in actual_workflow_dir_files
                ]
                if files_not_in_actual:
                    raise WorkflowNotFoundError(
                        f"The following workflows are not present in the directory: {', '.join(files_not_in_actual)}"
                    )
                actual_workflow_dir_files = deploy_only_workflow_files

        for module in actual_workflow_dir_files:
            # only find python files and ignore __init__.py
            if module == "__init__.py" or module[-3:] != ".py":
                continue

            module_name = module.replace(".py", "")
            # import all the modules into the mod object and not actually import them using __import__
            module_name_with_package = f"{pkg.__name__}.{module_name}"
            module_file_path = str(Path(str(pkg.__file__)).parent / module)
            spec = importlib.util.spec_from_file_location(
                module_name_with_package, module_file_path
            )
            if spec is None:
                raise RuntimeError("Unable to find spec for module")
            mod = importlib.util.module_from_spec(spec)
            sys.modules[module_name_with_package] = mod
            spec.loader.exec_module(mod)  # type: ignore
            for obj in dir(mod):
                module_item = getattr(mod, obj)
                if isinstance(module_item, Workflow):
                    # checked to see if this is a workflow object
                    self.add_workflow(module_item)

    def add_workflow(self, workflow: Workflow) -> None:
        if self.workflow_exists(workflow) is True:
            raise WorkflowAlreadyExistsError(
                f"Workflow with name: {workflow.name} already exists!"
            )
        self.workflows[workflow.name] = workflow

    def workflow_exists(self, workflow: Workflow) -> bool:
        return workflow.name in self.workflows

    @wraps_keyerror(WorkflowNotFoundError, "Unable to find workflow: ")
    def get_workflow(self, workflow_id: str) -> Optional[Workflow]:
        return self.workflows[workflow_id]


class Stage(Enum):
    deploy = "deploy"
    execute = "execute"


def get_caller_info() -> Optional[str]:
    # First get the full filename which isnt project.py (the first area where this caller info is called).
    # This should work most of the time.
    _cwd = str(os.getcwd())
    for i in inspect.stack():
        if i.filename not in [__file__, ""] and os.path.exists(i.filename):
            return os.path.splitext(os.path.relpath(i.filename, _cwd))[0]
    return None


# TODO: See if project can just be a directory path and scan for all "Workflow" instances
@dataclass
class Project:
    name: str
    debug_execute_workflow: Optional[str] = None
    debug_execute_task: Optional[str] = None
    git_repo: Optional[str] = None
    provider: Optional[str] = None
    libraries: Optional[List[TaskLibrary]] = None
    git_reference: Optional[str] = None
    # refer to: https://developer.hashicorp.com/terraform/language/settings/backends/s3
    s3_backend: Optional[Dict[str, str]] = None
    entry_point_path: Optional[str] = None
    mode: Optional[str] = None
    batch: bool = True
    codegen_mechanism: Optional[Type[CodegenInterface]] = None
    codegen_kwargs: Optional[Dict[str, Any]] = None
    bundle_obj_name: Optional[
        str
    ] = None  # repo name or folder where bundle assets will be saved
    bundle_base_path: Optional[str] = None

    _project: _Project = field(init=False)

    def __post_init__(self) -> None:
        self._mode = Stage[
            config(BrickflowEnvVars.BRICKFLOW_MODE.value, default=Stage.execute.value)
        ]
        self.entry_point_path = self.entry_point_path or get_caller_info()

        # populate bundle info via env vars
        self.bundle_obj_name = config(
            BrickflowEnvVars.BRICKFLOW_BUNDLE_OBJ_NAME.value,
            default=".brickflow_bundles",
        )
        self.bundle_base_path = config(
            BrickflowEnvVars.BRICKFLOW_BUNDLE_BASE_PATH.value,
            default="/Users/${workspace.current_user.userName}",
        )

        if self._mode == Stage.deploy:
            git_ref_default = (
                self.git_reference
                if self.git_reference is not None
                else f"commit/{get_current_commit()}"
            )
        else:
            git_ref_default = (
                self.git_reference if self.git_reference is not None else ""
            )
        self.git_reference = config(
            BrickflowEnvVars.BRICKFLOW_GIT_REF.value, default=git_ref_default
        )
        self.provider = config(
            BrickflowEnvVars.BRICKFLOW_GIT_PROVIDER.value, default=self.provider
        )
        self.git_repo = config(
            BrickflowEnvVars.BRICKFLOW_GIT_REPO.value, default=self.git_repo
        )
        if self.s3_backend is None:
            self.s3_backend = {
                "bucket": config("BRICKFLOW_S3_BACKEND_BUCKET", default=None),
                "key": config("BRICKFLOW_S3_BACKEND_KEY", default=None),
                "region": config("BRICKFLOW_S3_BACKEND_REGION", default=None),
                "dynamodb_table": config(
                    "BRICKFLOW_S3_BACKEND_DYNAMODB_TABLE", default=None
                ),
            }
            if all(value is None for value in self.s3_backend.values()):
                self.s3_backend = None

        deployment_mode = config(
            BrickflowEnvVars.BRICKFLOW_DEPLOYMENT_MODE.value, default="cdktf"
        )
        if deployment_mode == BrickflowDeployMode.CDKTF.value:
            self.codegen_mechanism = HashicorpCDKTFGen
        elif deployment_mode == BrickflowDeployMode.BUNDLE.value:
            self.codegen_mechanism = DatabricksBundleCodegen
        if self.codegen_kwargs is None:
            self.codegen_kwargs = {}

    def __enter__(self) -> "_Project":
        self._project = _Project(
            self.name,
            self.git_repo,
            self.provider,
            self.git_reference,
            self.s3_backend,
            self.entry_point_path,
            libraries=self.libraries or [],
            batch=self.batch,
            bundle_obj_name=self.bundle_obj_name,
            bundle_base_path=self.bundle_base_path,
        )
        return self._project

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:  # type: ignore
        if exc_type is not None:
            error_types = {Stage.deploy: DeployError, Stage.execute: ExecuteError}
            raise error_types[self._mode](
                f"Oops... failed during: {self._mode}"
            ) from exc_val

        if len(self._project.workflows) == 0:
            _ilog.info("Doing nothing no workflows...")
            return

        if self._mode.value == Stage.deploy.value:
            _ilog.info("Deploying changes... to %s", ctx.env)
            if self.codegen_mechanism is None:
                raise ValueError(
                    "codegen_mechanism cannot be None; please raise a github issue for this."
                )
            codegen = self.codegen_mechanism(
                project=self._project,
                id_=f"{ctx.env}_{self.name}",
                env=ctx.env,
                **self.codegen_kwargs,
            )
            codegen.synth()

        if self._mode.value == Stage.execute.value:
            wf_id = ctx.dbutils_widget_get_or_else(
                BrickflowInternalVariables.workflow_id.value,
                self.debug_execute_workflow,
            )
            t_id = ctx.dbutils_widget_get_or_else(
                BrickflowInternalVariables.task_id.value, self.debug_execute_task
            )

            if wf_id is None or t_id is None:
                _ilog.info(
                    "No workflow id or task key was able to found; doing nothing..."
                )
                return

            workflow = self._project.get_workflow(wf_id)
            task = workflow.get_task(t_id)
            task.execute()
