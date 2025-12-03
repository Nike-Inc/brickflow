import importlib
import importlib.util
import inspect
import logging
import os
import sys
import types

from dataclasses import field, dataclass
from enum import Enum
from pathlib import Path
from types import ModuleType
from typing import Dict, Optional, List, Any, Type, Union, Callable, cast

from decouple import config

from brickflow import (
    _ilog,
    BrickflowEnvVars,
    BrickflowProjectDeploymentSettings,
)
from brickflow.cli import BrickflowDeployMode
from brickflow.codegen import CodegenInterface
from brickflow.codegen.databricks_bundle import DatabricksBundleCodegen
from brickflow.context import ctx, BrickflowInternalVariables
from brickflow.engine import get_current_commit, ROOT_NODE
from brickflow.engine.task import (
    TaskLibrary,
    filter_bf_related_libraries,
    get_brickflow_libraries,
    TaskType,
    PypiTaskLibrary,
)
from brickflow.engine.compute import Cluster
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
    provider: str = "github"
    git_reference: Optional[str] = None
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
                # handling adding any module item if it is a workflow, list of workflows, or dict of workflows
                self._add_if_workflow(module_item)

    def _add_if_workflow(self, maybe_workflow: Any) -> None:
        if isinstance(maybe_workflow, Workflow):
            self.add_workflow(maybe_workflow)
        elif isinstance(maybe_workflow, (list, types.GeneratorType)):
            for item in maybe_workflow:
                # Add check for list of workflows
                self._add_if_workflow(item)
        elif isinstance(maybe_workflow, dict):
            for item in maybe_workflow.values():
                # Add check for dict of workflows
                self._add_if_workflow(item)

    def add_workflow(self, workflow: Workflow) -> None:
        if self.workflow_exists(workflow) is True:
            raise WorkflowAlreadyExistsError(
                f"Workflow with name: {workflow.name} already exists!"
            )

        # Inject tasks from YAML config if specified
        self._inject_tasks_from_yaml(workflow)

        self.workflows[workflow.name] = workflow

    def workflow_exists(self, workflow: Workflow) -> bool:
        return workflow.name in self.workflows

    @wraps_keyerror(WorkflowNotFoundError, "Unable to find workflow: ")
    def get_workflow(self, workflow_id: str) -> Optional[Workflow]:
        return self.workflows[workflow_id]

    def _inject_tasks_from_yaml(self, workflow: Workflow) -> None:
        """
        Inject tasks into workflow based on YAML configuration.

        This is called during add_workflow() to inject tasks before the workflow
        is registered in the project.
        """
        # Check if task injection is enabled via environment variable
        inject_config_path = os.environ.get(
            BrickflowEnvVars.BRICKFLOW_INJECT_TASKS_CONFIG.value
        )
        if not inject_config_path:
            return

        try:
            from brickflow.engine.task_injection_config import TaskInjectionConfig
            from brickflow.engine.task_executor import GenericTaskExecutor

            # Load configuration
            config_obj = TaskInjectionConfig.from_yaml(inject_config_path)

            if not config_obj.global_config.enabled:
                _ilog.info("Task injection is globally disabled")
                return

            # Inject each enabled task
            for task_def in config_obj.tasks:
                if not task_def.enabled:
                    _ilog.info("Skipping disabled task: %s", task_def.task_name)
                    continue

                _ilog.info(
                    "Injecting task '%s' into workflow '%s'",
                    task_def.task_name,
                    workflow.name,
                )

                # For "all_tasks" strategy, capture existing root tasks before injection
                existing_root_tasks = []
                if task_def.depends_on_strategy == "all_tasks":
                    existing_root_tasks = self._find_root_tasks(workflow)
                    _ilog.info(
                        "Found %d root tasks to update: %s",
                        len(existing_root_tasks),
                        existing_root_tasks,
                    )

                # Create task function using executor
                executor = GenericTaskExecutor(task_def)
                task_func = executor.create_task_function()

                # Build libraries list
                task_libraries = self._build_task_libraries(
                    task_def.libraries,
                    config_obj.global_config.default_libraries,
                )

                # Determine dependencies based on strategy
                depends_on = self._get_injection_dependencies(
                    workflow, task_def.depends_on_strategy
                )

                # Get cluster configuration
                cluster = None
                if task_def.cluster:
                    cluster = Cluster.from_existing_cluster(task_def.cluster)

                # Inject the task into workflow
                workflow._add_task(
                    f=task_func,
                    task_id=task_def.task_name,
                    depends_on=cast(
                        Optional[Union[Callable, str, List[Union[Callable, str]]]],
                        depends_on,
                    ),
                    task_type=TaskType[task_def.task_type],
                    libraries=task_libraries,
                    cluster=cluster,
                )

                # For "all_tasks" strategy, make all root tasks depend on injected task
                if task_def.depends_on_strategy == "all_tasks":
                    self._update_root_tasks_dependencies(
                        workflow, existing_root_tasks, task_def.task_name
                    )

                _ilog.info("Successfully injected task: %s", task_def.task_name)

        except FileNotFoundError:
            _ilog.warning(
                "Task injection config file not found: %s", inject_config_path
            )
        except Exception as e:
            _ilog.error("Failed to inject tasks from YAML: %s", e, exc_info=True)
            # Don't fail deployment on injection errors

    def _build_task_libraries(
        self,
        task_libraries: List[str],
        global_libraries: List[str],
    ) -> List[TaskLibrary]:
        """
        Build the complete list of libraries for an injected task.

        Combines:
        - Global default libraries
        - Task-specific libraries

        Note: Artifacts are handled separately in GenericTaskExecutor.create_task_function()
        """
        all_libraries: List[TaskLibrary] = []

        # Add global default libraries
        for lib in global_libraries:
            all_libraries.append(PypiTaskLibrary(package=lib))

        # Add task-specific libraries
        for lib in task_libraries:
            all_libraries.append(PypiTaskLibrary(package=lib))

        # Note: If artifact should be installed as library, it's handled
        # via artifact.install_as_library in the task execution phase

        return all_libraries

    def _get_injection_dependencies(
        self, workflow: Workflow, strategy: str
    ) -> Optional[List[str]]:
        """
        Determine task dependencies based on injection strategy.

        Strategies:
        - "leaf_nodes": Inject after all leaf nodes (tasks with no downstream deps)
        - "all_tasks": All tasks depend on this (task runs first)
        - "specific_tasks": Comma-separated list of task names
        """
        if strategy == "all_tasks":
            # This task runs first, so no dependencies
            return None

        elif strategy == "leaf_nodes":
            # Find all leaf nodes (tasks with no downstream dependencies)
            leaf_nodes = self._find_leaf_nodes(workflow)
            return leaf_nodes if leaf_nodes else None

        elif strategy.startswith("specific_tasks:"):
            # Parse specific task names
            task_names = strategy.replace("specific_tasks:", "").split(",")
            return [name.strip() for name in task_names if name.strip()]

        else:
            # Default to leaf_nodes
            _ilog.warning(
                "Unknown injection strategy '%s', defaulting to leaf_nodes", strategy
            )
            return self._find_leaf_nodes(workflow)

    def _find_leaf_nodes(self, workflow: Workflow) -> List[str]:
        """
        Find all leaf nodes in the workflow DAG.

        Leaf nodes are tasks that have no downstream dependencies
        (no other tasks depend on them).
        """
        leaf_nodes = []

        for task_name in workflow.tasks.keys():
            # Check if this task has any successors in the graph
            successors = list(workflow.graph.successors(task_name))
            if not successors:
                leaf_nodes.append(task_name)

        return leaf_nodes

    def _find_root_tasks(self, workflow: Workflow) -> List[str]:
        """
        Find all root tasks in the workflow DAG.

        Root tasks are tasks that have no upstream dependencies
        (they don't depend on other tasks, only on the root node).
        """
        root_tasks = []

        for task_name in workflow.tasks.keys():
            # Get predecessors (dependencies) for this task
            predecessors = list(workflow.graph.predecessors(task_name))
            # Filter out the ROOT_NODE as it's just a marker
            real_predecessors = [p for p in predecessors if p != ROOT_NODE]

            # If no real predecessors, this is a root task
            if not real_predecessors:
                root_tasks.append(task_name)

        return root_tasks

    def _update_root_tasks_dependencies(
        self, workflow: Workflow, root_tasks: List[str], injected_task_name: str
    ) -> None:
        """
        Update root tasks to depend on the injected task.

        This is used for the "all_tasks" strategy to ensure the injected
        task runs first and all other tasks depend on it.
        """
        for root_task in root_tasks:
            # Add edge from injected task to root task
            # This makes root_task depend on injected_task_name
            workflow.graph.add_edge(injected_task_name, root_task)
            _ilog.info(
                "Updated task '%s' to depend on '%s'", root_task, injected_task_name
            )


class Stage(Enum):
    deploy = "deploy"
    execute = "execute"
    unittest = "unittest"


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
    provider: str = "github"
    libraries: Optional[List[TaskLibrary]] = None
    git_reference: Optional[str] = None
    entry_point_path: Optional[str] = None
    mode: Optional[str] = None
    batch: bool = True
    codegen_mechanism: Optional[Type[CodegenInterface]] = None
    codegen_kwargs: Optional[Dict[str, Any]] = None
    bundle_obj_name: Optional[str] = (
        None  # repo name or folder where bundle assets will be saved
    )
    bundle_base_path: Optional[str] = None
    enable_plugins: bool = False
    _project: _Project = field(init=False)

    def __post_init__(self) -> None:
        # during entry of project enable logging
        _ilog.setLevel(logging.INFO)

        self._mode = Stage[
            config(BrickflowEnvVars.BRICKFLOW_MODE.value, default=Stage.execute.value)
        ]
        self.entry_point_path = self.entry_point_path or get_caller_info()
        deploy_settings = BrickflowProjectDeploymentSettings()
        # setup current_project
        env_project_name = deploy_settings.brickflow_project_name

        self.libraries = self.libraries or []
        if deploy_settings.brickflow_auto_add_libraries is True:
            _ilog.info("Auto adding brickflow libraries...")
            self.libraries = filter_bf_related_libraries(self.libraries)
            # here libraries should not be null anymore if this branch is invoked
            self.libraries += get_brickflow_libraries()

        if (
            env_project_name is not None
            and self.name is not None
            and env_project_name != self.name
        ):
            raise ValueError(
                "Project name in config files and entrypoint must be the same"
            )

        ctx.set_current_project(self.name or env_project_name)  # always setup first

        # populate bundle info via env vars
        self.bundle_obj_name = config(
            BrickflowEnvVars.BRICKFLOW_BUNDLE_OBJ_NAME.value,
            default=".brickflow_bundles",
        )
        self.bundle_base_path = config(
            BrickflowEnvVars.BRICKFLOW_BUNDLE_BASE_PATH.value,
            default="/Users/${workspace.current_user.userName}",
        )

        self.git_reference = config(
            BrickflowEnvVars.BRICKFLOW_GIT_REF.value, default=self.get_git_ref()
        )

        if (
            self._mode == Stage.deploy
            and ctx.is_local() is False
            and self.git_reference is None
        ):
            raise ValueError(
                "git_reference must be set when deploying to non-local envs"
            )

        self.provider = config(
            BrickflowEnvVars.BRICKFLOW_GIT_PROVIDER.value, default=self.provider
        )
        self.git_repo = config(
            BrickflowEnvVars.BRICKFLOW_GIT_REPO.value, default=self.git_repo
        )

        deployment_mode = config(
            BrickflowEnvVars.BRICKFLOW_DEPLOYMENT_MODE.value, default="bundle"
        )
        if deployment_mode == BrickflowDeployMode.BUNDLE.value:
            self.codegen_mechanism = DatabricksBundleCodegen
        if self.codegen_kwargs is None:
            self.codegen_kwargs = {}

    def get_git_ref(self) -> Optional[str]:
        if self._mode == Stage.deploy:
            if self.git_reference is not None:
                return self.git_reference
            else:
                try:
                    return f"commit/{get_current_commit()}"
                except Exception:
                    _ilog.warning(
                        "Unable to get current commit; defaulting to empty string"
                    )
                    return "commit/fake-local-stub" if ctx.is_local() else None
        else:
            return self.git_reference if self.git_reference is not None else ""

    def __enter__(self) -> "_Project":
        self._project = _Project(
            self.name,
            self.git_repo,
            self.provider,
            self.git_reference,
            self.entry_point_path,
            libraries=self.libraries,
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

        if self._mode == Stage.unittest:
            # Mode is purely for testing purposes for the _Project internal class
            _ilog.info("Running unit tests...")
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
                **(self.codegen_kwargs or {}),
            )
            codegen.synth()

        if self._mode.value == Stage.execute.value:
            wf_id = ctx.get_parameter(
                BrickflowInternalVariables.workflow_id.value,
                self.debug_execute_workflow,
            )
            t_id = ctx.get_parameter(
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
