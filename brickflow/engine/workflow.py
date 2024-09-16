import abc
import functools
import logging
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Iterator, List, Optional, Union

import networkx as nx

from brickflow import BrickflowEnvVars, env_chain
from brickflow.bundles.model import (
    JobsContinuous,
    JobsEmailNotifications,
    JobsHealthRules,
    JobsNotificationSettings,
    JobsParameters,
    JobsTrigger,
    JobsWebhookNotifications,
)
from brickflow.context import BrickflowInternalVariables
from brickflow.engine import ROOT_NODE
from brickflow.engine.compute import Cluster, DuplicateClustersDefinitionError
from brickflow.engine.task import (
    AnotherActiveTaskError,
    BrickflowTriggerRule,
    NoCallableTaskError,
    Task,
    TaskAlreadyExistsError,
    TaskLibrary,
    TaskNotFoundError,
    TaskSettings,
    TaskType,
)
from brickflow.engine.utils import wraps_keyerror


class WorkflowConfigError(Exception):
    pass


class NoWorkflowComputeError(Exception):
    pass


@dataclass(frozen=True)
class ScimEntity(abc.ABC):
    name: str

    @abc.abstractmethod
    def to_access_control(self) -> Dict[str, str]:  # pragma: no cover
        pass


class User(ScimEntity):
    def to_access_control(self) -> Dict[str, str]:
        return {"user_name": self.name}


class Group(ScimEntity):
    def to_access_control(self) -> Dict[str, str]:
        return {"group_name": self.name}


class ServicePrincipal(ScimEntity):
    def to_access_control(self) -> Dict[str, str]:
        return {"service_principal_name": self.name}


@dataclass(frozen=True)
class WorkflowPermissions:
    owner: Optional[User] = None
    can_manage_run: List[ScimEntity] = field(default_factory=lambda: [])
    can_view: List[ScimEntity] = field(default_factory=lambda: [])
    can_manage: List[ScimEntity] = field(default_factory=lambda: [])

    def to_access_controls(self) -> List:
        access_controls = []
        # TODO: Permissions as ENUM
        if self.owner is not None:
            access_controls.append(
                {"permission_level": "IS_OWNER", **self.owner.to_access_control()}
            )
        for principal in list(set(self.can_manage)):
            access_controls.append(
                {"permission_level": "CAN_MANAGE", **principal.to_access_control()}
            )
        for principal in list(set(self.can_manage_run)):
            access_controls.append(
                {"permission_level": "CAN_MANAGE_RUN", **principal.to_access_control()}
            )
        for principal in list(set(self.can_view)):
            access_controls.append(
                {"permission_level": "CAN_VIEW", **principal.to_access_control()}
            )
        return access_controls


class WorkflowEmailNotifications(JobsEmailNotifications):
    pass


class WorkflowWebhookNotifications(JobsWebhookNotifications):
    pass


class WorkflowNotificationSettings(JobsNotificationSettings):
    pass


class Trigger(JobsTrigger):
    pass


# TODO: Re-architect to make this frozen and immutable after being defined.
@dataclass(eq=True)
class Workflow:
    # name should be immutable and not modified after being set
    _name: str
    schedule_quartz_expression: Optional[str] = None
    schedule_continuous: Optional[JobsContinuous] = None
    timezone: str = "UTC"
    schedule_pause_status: str = "UNPAUSED"
    default_cluster: Optional[Cluster] = None
    clusters: List[Cluster] = field(default_factory=lambda: [])
    health: Optional[List[JobsHealthRules]] = None
    timeout_seconds: Optional[int] = None
    default_task_settings: TaskSettings = TaskSettings()
    email_notifications: Optional[WorkflowEmailNotifications] = None
    webhook_notifications: Optional[WorkflowWebhookNotifications] = None
    notification_settings: Optional[WorkflowNotificationSettings] = None
    trigger: Optional[Trigger] = None
    libraries: List[TaskLibrary] = field(default_factory=lambda: [])
    tags: Optional[Dict[str, str]] = None
    max_concurrent_runs: int = 1
    permissions: WorkflowPermissions = WorkflowPermissions()
    active_task: Optional[str] = None
    graph: nx.DiGraph = field(default_factory=nx.DiGraph)
    tasks: Dict[str, Task] = field(default_factory=lambda: {})
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    common_task_parameters: Optional[Dict[str, str]] = None
    run_as_user: Optional[str] = None
    run_as_service_principal: Optional[str] = None
    # this a databricks limit set on workflows, you can override it if you have exception
    max_tasks_in_workflow: int = 100
    enable_plugins: Optional[bool] = None
    parameters: Optional[List[JobsParameters]] = None

    def __post_init__(self) -> None:
        self.graph.add_node(ROOT_NODE)
        if self.default_cluster is None and self.clusters == []:
            raise NoWorkflowComputeError(
                f"Please configure default_cluster or "
                f"clusters field for workflow: {self.name}"
            )
        if self.prefix is None:
            self.prefix = env_chain(
                BrickflowEnvVars.BRICKFLOW_WORKFLOW_PREFIX.value,
                BrickflowInternalVariables.workflow_prefix.value,
                "",
            )
        if self.suffix is None:
            self.suffix = env_chain(
                BrickflowEnvVars.BRICKFLOW_WORKFLOW_SUFFIX.value,
                BrickflowInternalVariables.workflow_suffix.value,
                "",
            )
        if self.default_cluster is None:
            # the default cluster is set to the first cluster if it is not configured
            self.default_cluster = self.clusters[0]

        self.validate_schedule_configs()

    # def __hash__(self) -> int:
    #     import json
    #
    #     # dedupe dicts and lists which are default un hashable. Easiest way to identify dupes.
    #     return hash(json.dumps(self.as_dict()))

    @property
    def name(self) -> str:
        return (self.prefix or "") + (self._name or "") + (self.suffix or "")

    @property
    def unique_new_clusters(self) -> List[Cluster]:
        clusters = (
            [v.cluster for k, v in self.tasks.items()]
            + self.clusters
            + [self.default_cluster]
        )
        return list(
            set([c for c in clusters if c is not None and c.is_new_job_cluster])
        )

    def unique_new_clusters_dict(self) -> List[Dict[str, Any]]:
        self.validate_new_clusters_with_unique_names()
        all_unique_clusters = self.unique_new_clusters
        return [
            # job clusters do not need names
            {
                "job_cluster_key": c.name,
                "new_cluster": c.as_dict(remove_fields=["name"]),
            }
            for c in all_unique_clusters
        ]

    def validate_new_clusters_with_unique_names(self) -> None:
        all_unique_clusters = self.unique_new_clusters
        unique_name_list: Dict[str, Optional[str]] = {}
        duplicates = []
        for cluster in all_unique_clusters:
            if cluster.name not in unique_name_list:
                unique_name_list[cluster.name] = None
            else:
                duplicates.append(cluster.name)

        duplicate_list = list(set(duplicates))
        if len(duplicate_list) > 0:
            raise DuplicateClustersDefinitionError(
                f"Found duplicate cluster definitions in your workflow: {self.name}, "
                f"with names: {duplicate_list}"
            )

    def validate_schedule_configs(self) -> None:
        allowed_scheduled_pause_statuses = ["PAUSED", "UNPAUSED"]
        self.schedule_pause_status = self.schedule_pause_status.upper()
        if self.schedule_pause_status not in allowed_scheduled_pause_statuses:
            raise WorkflowConfigError(
                f"schedule_pause_status must be one of {allowed_scheduled_pause_statuses}"
            )

        if (
            self.schedule_quartz_expression is not None
            and self.schedule_continuous is not None
        ):
            raise WorkflowConfigError(
                "Please configure either schedule_quartz_expression or schedule_continuous for workflow"
            )

        if self.trigger is not None and self.schedule_continuous is not None:
            raise WorkflowConfigError(
                "Please configure either trigger or schedule_continuous for workflow"
            )

        if self.schedule_continuous is not None:
            self.schedule_continuous.pause_status = (
                self.schedule_continuous.pause_status.upper()
            )

            if (
                self.schedule_continuous.pause_status
                not in allowed_scheduled_pause_statuses
            ):
                raise WorkflowConfigError(
                    "Please configure either PAUSED or UNPAUSED for schedule_continuous.pause_status"
                )

    @property
    def bfs_layers(self) -> List[str]:
        return list(nx.bfs_layers(self.graph, ROOT_NODE))[1:]

    def task_iter(self) -> Iterator[Task]:
        for task in self.bfs_task_iter():
            yield task

    def bfs_task_iter(self) -> Iterator[Task]:
        for layer in self.bfs_layers:
            for task_key in layer:
                yield self.get_task(task_key)

    def parents(self, node: str) -> Iterator:
        return self.graph.predecessors(node)

    def check_no_active_task(self) -> None:
        if self.active_task is not None:
            raise AnotherActiveTaskError(
                "You are calling another active task in another task. Please abstract the code more."
            )

    @wraps_keyerror(TaskNotFoundError, "Unable to find task: ")
    def get_task(self, task_id: str) -> Task:
        return self.tasks[task_id]

    @wraps_keyerror(TaskNotFoundError, "Unable to find task: ")
    def pop_task(self, task_id: str) -> None:
        # Pop from dict and graph
        self.tasks.pop(task_id)
        self.graph.remove_node(task_id)

    def task_exists(self, task_id: str) -> bool:
        return task_id in self.tasks

    def log_timeout_warning(self, task_settings: TaskSettings) -> bool:
        if task_settings is not None and self.timeout_seconds is not None:
            if task_settings.timeout_seconds is not None:
                if task_settings.timeout_seconds > self.timeout_seconds:
                    return True
        return False

    def _set_active_task(self, task_id: str) -> None:
        self.active_task = task_id

    def _reset_active_task(self) -> None:
        self.active_task = None

    # TODO: is this even needed?
    # def get_return_value(self, f: Callable, default=None):
    #     return default

    def _add_edge_to_graph(
        self,
        depends_on: Union[List[Union[Callable, str]], Union[Callable, str]],
        task_id: str,
    ) -> None:
        depends_on_list = depends_on if isinstance(depends_on, list) else [depends_on]
        for t in depends_on_list:
            if isinstance(t, str):
                self.graph.add_edge(t, task_id)
            else:
                self.graph.add_edge(t.__name__, task_id)

    def _add_task(
        self,
        f: Callable,
        task_id: str,
        description: Optional[str] = None,
        cluster: Optional[Cluster] = None,
        libraries: Optional[List[TaskLibrary]] = None,
        task_type: TaskType = TaskType.BRICKFLOW_TASK,
        depends_on: Optional[Union[Callable, str, List[Union[Callable, str]]]] = None,
        trigger_rule: BrickflowTriggerRule = BrickflowTriggerRule.ALL_SUCCESS,
        custom_execute_callback: Optional[Callable] = None,
        task_settings: Optional[TaskSettings] = None,
        ensure_brickflow_plugins: bool = False,
        if_else_outcome: Optional[Dict[Union[str, str], str]] = None,
    ) -> None:
        if self.task_exists(task_id):
            raise TaskAlreadyExistsError(
                f"Task: {task_id} already exists, please rename your function."
            )

        if self.default_cluster is None:
            raise RuntimeError(
                "Some how default cluster wasnt set please raise a github issue."
            )

        if self.log_timeout_warning(task_settings):  # type: ignore
            logging.warning(
                "Task timeout_seconds should not exceed workflow timeout_seconds",
            )

        _libraries = libraries or [] + self.libraries
        _depends_on = (
            [depends_on]
            if isinstance(depends_on, str) or callable(depends_on)
            else depends_on
        )

        if self.enable_plugins is not None:
            ensure_plugins = self.enable_plugins
        else:
            ensure_plugins = ensure_brickflow_plugins

        # NOTE: REMOTE WORKSPACE RUN JOB OVERRIDE
        # This is a temporary override for the RunJobTask because Databricks does not natively support
        # triggering the job run in the remote workspace. By default, Databricks SDK derives the workspace URL
        # from the runtime, and hence it is not required by the RunJobTask. The assumption is that if `host` parameter
        # is set, user wants to trigger a remote job, in this case we set the task type to BRICKFLOW_TASK to
        # enforce notebook type execution and replacing the original callable function with the RunJobInRemoteWorkspace
        if task_type == TaskType.RUN_JOB_TASK:
            func = f()
            if func.host:
                from brickflow_plugins.databricks.run_job import RunJobInRemoteWorkspace

                task_type = TaskType.BRICKFLOW_TASK

                def run_job_func() -> Callable:
                    # Using parameter values from the original RunJobTask
                    return RunJobInRemoteWorkspace(
                        job_name=func.job_name,
                        databricks_host=func.host,
                        databricks_token=func.token,
                    ).execute()

                f = run_job_func
        # NOTE: END REMOTE WORKSPACE RUN JOB OVERRIDE

        self.tasks[task_id] = Task(
            task_id=task_id,
            task_func=f,
            workflow=self,
            description=description,
            libraries=_libraries,
            cluster=cluster or self.default_cluster,
            depends_on=_depends_on or [],
            task_type=task_type,
            trigger_rule=trigger_rule,
            task_settings=task_settings,
            custom_execute_callback=custom_execute_callback,
            ensure_brickflow_plugins=ensure_plugins,
            if_else_outcome=if_else_outcome,
        )

        # attempt to create task object before adding to graph
        if _depends_on is None:
            self.graph.add_edge(ROOT_NODE, task_id)
        else:
            self._add_edge_to_graph(_depends_on, task_id)

    def dlt_task(
        self,
        task_func: Optional[Callable] = None,
        name: Optional[str] = None,
        task_settings: Optional[TaskSettings] = None,
        depends_on: Optional[Union[Callable, str, List[Union[Callable, str]]]] = None,
        if_else_outcome: Optional[Dict[Union[str, str], str]] = None,
    ) -> Callable:
        return self.task(
            task_func,
            name,
            task_type=TaskType.DLT,
            task_settings=task_settings,
            depends_on=depends_on,
            if_else_outcome=if_else_outcome,
        )

    def notebook_task(
        self,
        task_func: Optional[Callable] = None,
        name: Optional[str] = None,
        cluster: Optional[Cluster] = None,
        libraries: Optional[List[TaskLibrary]] = None,
        task_settings: Optional[TaskSettings] = None,
        depends_on: Optional[Union[Callable, str, List[Union[Callable, str]]]] = None,
        if_else_outcome: Optional[Dict[Union[str, str], str]] = None,
    ) -> Callable:
        return self.task(
            task_func,
            name,
            cluster=cluster,
            libraries=libraries,
            task_type=TaskType.NOTEBOOK_TASK,
            task_settings=task_settings,
            depends_on=depends_on,
            if_else_outcome=if_else_outcome,
        )

    def spark_jar_task(
        self,
        task_func: Optional[Callable] = None,
        name: Optional[str] = None,
        cluster: Optional[Cluster] = None,
        libraries: Optional[List[TaskLibrary]] = None,
        task_settings: Optional[TaskSettings] = None,
        depends_on: Optional[Union[Callable, str, List[Union[Callable, str]]]] = None,
        if_else_outcome: Optional[Dict[Union[str, str], str]] = None,
    ) -> Callable:
        return self.task(
            task_func,
            name,
            cluster=cluster,
            libraries=libraries,
            task_type=TaskType.SPARK_JAR_TASK,
            task_settings=task_settings,
            depends_on=depends_on,
            if_else_outcome=if_else_outcome,
        )

    def spark_python_task(
        self,
        task_func: Optional[Callable] = None,
        name: Optional[str] = None,
        cluster: Optional[Cluster] = None,
        libraries: Optional[List[TaskLibrary]] = None,
        task_settings: Optional[TaskSettings] = None,
        depends_on: Optional[Union[Callable, str, List[Union[Callable, str]]]] = None,
        if_else_outcome: Optional[Dict[Union[str, str], str]] = None,
    ) -> Callable:
        return self.task(
            task_func,
            name,
            cluster=cluster,
            libraries=libraries,
            task_type=TaskType.SPARK_PYTHON_TASK,
            task_settings=task_settings,
            depends_on=depends_on,
            if_else_outcome=if_else_outcome,
        )

    def run_job_task(
        self,
        task_func: Optional[Callable] = None,
        name: Optional[str] = None,
        task_settings: Optional[TaskSettings] = None,
        depends_on: Optional[Union[Callable, str, List[Union[Callable, str]]]] = None,
        if_else_outcome: Optional[Dict[Union[str, str], str]] = None,
    ) -> Callable:
        return self.task(
            task_func,
            name,
            task_type=TaskType.RUN_JOB_TASK,
            task_settings=task_settings,
            depends_on=depends_on,
            if_else_outcome=if_else_outcome,
        )

    def sql_task(
        self,
        task_func: Optional[Callable] = None,
        name: Optional[str] = None,
        task_settings: Optional[TaskSettings] = None,
        depends_on: Optional[Union[Callable, str, List[Union[Callable, str]]]] = None,
        if_else_outcome: Optional[Dict[Union[str, str], str]] = None,
    ) -> Callable:
        return self.task(
            task_func,
            name,
            task_type=TaskType.SQL,
            task_settings=task_settings,
            depends_on=depends_on,
            if_else_outcome=if_else_outcome,
        )

    def if_else_condition_task(
        self,
        task_func: Optional[Callable] = None,
        name: Optional[str] = None,
        task_settings: Optional[TaskSettings] = None,
        depends_on: Optional[Union[Callable, str, List[Union[Callable, str]]]] = None,
        if_else_outcome: Optional[Dict[Union[str, str], str]] = None,
    ) -> Callable:
        return self.task(
            task_func,
            name,
            task_type=TaskType.IF_ELSE_CONDITION_TASK,
            task_settings=task_settings,
            depends_on=depends_on,
            if_else_outcome=if_else_outcome,
        )

    def task(
        self,
        task_func: Optional[Callable] = None,
        name: Optional[str] = None,
        cluster: Optional[Cluster] = None,
        libraries: Optional[List[TaskLibrary]] = None,
        task_type: TaskType = TaskType.BRICKFLOW_TASK,
        depends_on: Optional[Union[Callable, str, List[Union[Callable, str]]]] = None,
        trigger_rule: BrickflowTriggerRule = BrickflowTriggerRule.ALL_SUCCESS,
        custom_execute_callback: Optional[Callable] = None,
        task_settings: Optional[TaskSettings] = None,
        ensure_brickflow_plugins: bool = False,
        if_else_outcome: Optional[Dict[Union[str, str], str]] = None,
    ) -> Callable:
        if len(self.tasks) >= self.max_tasks_in_workflow:
            raise ValueError(
                "You have reached the maximum number of tasks allowed in a databricks workflow. "
                "Please split your workflow into multiple workflows or raise a feature request "
                "with your Databricks team."
            )

        def task_wrapper(f: Callable) -> Callable:
            task_id = name or f.__name__

            self._add_task(
                f,
                task_id,
                cluster=cluster,
                task_type=task_type,
                libraries=libraries,
                depends_on=depends_on,
                trigger_rule=trigger_rule,
                custom_execute_callback=custom_execute_callback,
                task_settings=task_settings,
                ensure_brickflow_plugins=ensure_brickflow_plugins,
                if_else_outcome=if_else_outcome,
            )

            @functools.wraps(f)
            def func(*args, **kwargs):  # type: ignore
                try:
                    self.check_no_active_task()
                    self._set_active_task(task_id)
                    resp = f(*args, **kwargs)
                    return resp
                except Exception as e:
                    self._reset_active_task()
                    raise e
                finally:
                    self._reset_active_task()

            return func

        if task_func is not None:
            if callable(task_func):
                return task_wrapper(task_func)
            else:
                raise NoCallableTaskError(
                    "Please use task decorator against a callable function."
                )

        return task_wrapper
