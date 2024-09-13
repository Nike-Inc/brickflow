# pylint: disable=too-many-lines
from __future__ import annotations

import base64
import dataclasses
import functools
import inspect
import json
import logging
import os
import textwrap
from dataclasses import dataclass, field
from enum import Enum
from io import StringIO
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Iterator,
    List,
    Literal,
    Optional,
    Tuple,
    Union,
)

import pluggy
from decouple import config

from brickflow import (
    BrickflowDefaultEnvs,
    BrickflowEnvVars,
    BrickflowProjectDeploymentSettings,
    _ilog,
    get_brickflow_version,
)
from brickflow.bundles.model import (
    JobsTasksConditionTask,
    JobsTasksHealthRules,
    JobsTasksNotebookTask,
    JobsTasksNotificationSettings,
    JobsTasksRunJobTask,
    JobsTasksSparkJarTask,
    JobsTasksSparkPythonTask,
    JobsTasksSqlTask,
    JobsTasksSqlTaskAlert,
    JobsTasksSqlTaskAlertSubscriptions,
    JobsTasksSqlTaskDashboard,
    JobsTasksSqlTaskDashboardSubscriptions,
    JobsTasksSqlTaskFile,
    JobsTasksSqlTaskQuery,
)
from brickflow.cli.projects import DEFAULT_BRICKFLOW_VERSION_MODE
from brickflow.context import (
    BRANCH_SKIP_EXCEPT,
    RETURN_VALUE_KEY,
    SKIP_EXCEPT_HACK,
    BrickflowBuiltInTaskVariables,
    BrickflowInternalVariables,
    ctx,
)
from brickflow.engine import ROOT_NODE, with_brickflow_logger
from brickflow.engine.compute import Cluster
from brickflow.engine.hooks import BRICKFLOW_TASK_PLUGINS, BrickflowTaskPluginSpec
from brickflow.engine.utils import get_job_id

if TYPE_CHECKING:
    from brickflow.engine.workflow import Workflow  # pragma: no cover

brickflow_task_plugin_impl = pluggy.HookimplMarker(BRICKFLOW_TASK_PLUGINS)


class TaskNotFoundError(Exception):
    pass


class AnotherActiveTaskError(Exception):
    pass


class TaskAlreadyExistsError(Exception):
    pass


class UnsupportedBrickflowTriggerRuleError(Exception):
    pass


class InvalidTaskSignatureDefinition(Exception):
    pass


class NoCallableTaskError(Exception):
    pass


class InvalidTaskLibraryError(Exception):
    pass


class BrickflowUserCodeException(Exception):
    pass


class BrickflowTaskEnvVars(Enum):
    BRICKFLOW_SELECT_TASKS = "BRICKFLOW_SELECT_TASKS"


class BrickflowTriggerRule(Enum):
    ALL_SUCCESS = "all_success"
    NONE_FAILED = "none_failed"


class TaskType(Enum):
    BRICKFLOW_TASK = "brickflow_task"
    SQL = "sql_task"
    DLT = "pipeline_task"
    CUSTOM_PYTHON_TASK = "custom_python_task"
    NOTEBOOK_TASK = "notebook_task"
    SPARK_JAR_TASK = "spark_jar_task"
    SPARK_PYTHON_TASK = "spark_python_task"
    RUN_JOB_TASK = "run_job_task"
    IF_ELSE_CONDITION_TASK = "condition_task"


class TaskRunCondition(Enum):
    ALL_SUCCESS = "ALL_SUCCESS"
    AT_LEAST_ONE_SUCCESS = "AT_LEAST_ONE_SUCCESS"
    NONE_FAILED = "NONE_FAILED"
    ALL_DONE = "ALL_DONE"
    AT_LEAST_ONE_FAILED = "AT_LEAST_ONE_FAILED"
    ALL_FAILED = "ALL_FAILED"


class Operator(Enum):
    EQUAL_TO = "=="
    NOT_EQUAL = "!="
    GREATER_THAN = ">"
    LESS_THAN = "<"
    GREATER_THAN_OR_EQUAL = ">="
    LESS_THAN_OR_EQUAL = "<="


@dataclass(frozen=True)
class TaskLibrary:
    @staticmethod
    def unique_libraries(
        library_list: Optional[List["TaskLibrary"]],
    ) -> List["TaskLibrary"]:
        if library_list is None:
            return []
        return list(set(library_list))

    @property
    def dict(self) -> Dict[str, Union[str, Dict[str, str]]]:
        return dataclasses.asdict(self)

    @staticmethod
    def starts_with_values(value: str, prefix_list: List[str]) -> bool:
        return any(value.startswith(prefix) for prefix in prefix_list)

    def validate_starts_with_values(self, value: str, prefix_list: List[str]) -> None:
        if not TaskLibrary.starts_with_values(value, prefix_list):
            raise InvalidTaskLibraryError(
                f"Invalid library configured for: {self.__class__.__name__}; "
                f"with value {value}; the valid prefix lists are: {prefix_list}"
            )


@dataclass(frozen=True)
class StorageBasedTaskLibrary(TaskLibrary):
    def __post_init__(self) -> None:
        storage_lib = dataclasses.asdict(self)
        for _, v in storage_lib.items():
            self.validate_starts_with_values(v, ["dbfs:/", "s3://"])


@dataclass(frozen=True)
class JarTaskLibrary(StorageBasedTaskLibrary):
    """
    Args:
        jar: String to s3/dbfs path for jar
    """

    jar: str


@dataclass(frozen=True)
class EggTaskLibrary(StorageBasedTaskLibrary):
    """
    Args:
        egg: String to s3/dbfs path for egg
    """

    egg: str


@dataclass(frozen=True)
class WheelTaskLibrary(StorageBasedTaskLibrary):
    """
    Args:
        whl: String to s3/dbfs path for whl
    """

    whl: str


@dataclass(frozen=True)
class PypiTaskLibrary(TaskLibrary):
    """
    Args:
        package: The package in pypi i.e. requests, requests==x.y.z, git+https://github.com/Nike-Inc/brickflow.git
        repo: The repository where the package can be found. By default pypi is used
    """

    package: str
    repo: Optional[str] = None

    @property
    def dict(self) -> Dict[str, Union[str, Dict[str, str]]]:
        return {"pypi": dataclasses.asdict(self)}


@dataclass(frozen=True)
class MavenTaskLibrary(TaskLibrary):
    """
    Args:
        coordinates: Gradle-style Maven coordinates. For example: org.jsoup:jsoup:1.7.2.
        repo: Maven repo to install the Maven package from.
            If omitted, both Maven Central Repository and Spark Packages are searched.
        exclusions: List of dependences to exclude. For example: ["slf4j:slf4j", "*:hadoop-client"].
            Maven dependency exclusions:
            https://maven.apache.org/guides/introduction/introduction-to-optional-and-excludes-dependencies.html.
    """

    coordinates: str
    repo: Optional[str] = None
    exclusions: Optional[List[str]] = None

    @property
    def dict(self) -> Dict[str, Union[str, Dict[str, str]]]:
        return {"maven": dataclasses.asdict(self)}


@dataclass(frozen=True)
class CranTaskLibrary(TaskLibrary):
    """
    Args:
        package: The name of the CRAN package to install.
        repo: The repository where the package can be found. If not specified, the default CRAN repo is used.
    """

    package: str
    repo: Optional[str] = None

    @property
    def dict(self) -> Dict[str, Union[str, Dict[str, str]]]:
        return {"cran": dataclasses.asdict(self)}


@dataclass(frozen=True)
class EmailNotifications:
    on_failure: Optional[List[str]] = None
    on_success: Optional[List[str]] = None
    on_start: Optional[List[str]] = None

    def to_tf_dict(self) -> Dict[str, Optional[List[str]]]:
        return {
            "on_start": self.on_start,
            "on_failure": self.on_failure,
            "on_success": self.on_success,
        }


class TaskNotificationSettings(JobsTasksNotificationSettings):
    pass


@dataclass(frozen=True)
class TaskSettings:
    email_notifications: Optional[EmailNotifications] = None
    notification_settings: Optional[TaskNotificationSettings] = None
    timeout_seconds: Optional[int] = None
    max_retries: Optional[int] = None
    min_retry_interval_millis: Optional[int] = None
    retry_on_timeout: Optional[bool] = None
    run_if: Optional[TaskRunCondition] = None

    def merge(self, other: Optional["TaskSettings"]) -> "TaskSettings":
        # overrides top level values
        if other is None:
            return self
        return TaskSettings(
            other.email_notifications or self.email_notifications,
            other.notification_settings or self.notification_settings,
            other.timeout_seconds or self.timeout_seconds or 0,
            other.max_retries or self.max_retries,
            other.min_retry_interval_millis or self.min_retry_interval_millis,
            other.retry_on_timeout or self.retry_on_timeout,
            other.run_if or self.run_if,
        )

    def to_tf_dict(
        self,
    ) -> Dict[
        str,
        Optional[str]
        | Optional[int]
        | Optional[bool]
        | Optional[Dict[str, Optional[List[str]]]],
    ]:
        email_not = (
            self.email_notifications.to_tf_dict()
            if self.email_notifications is not None
            else {}
        )
        notification_settings = (
            {}
            if self.notification_settings is None
            else {"notification_settings": self.notification_settings.dict()}
        )
        return {
            **notification_settings,
            "email_notifications": email_not,
            "timeout_seconds": self.timeout_seconds,
            "max_retries": self.max_retries,
            "min_retry_interval_millis": self.min_retry_interval_millis,
            "retry_on_timeout": self.retry_on_timeout,
            **({"run_if": self.run_if.value} if self.run_if else {}),
        }


@dataclass
class TaskResponse:
    response: Any
    push_return_value: bool = True
    user_code_error: Optional[Exception] = None
    input_kwargs: Optional[Dict[str, Any]] = None


@dataclass(frozen=True)
class DLTChannels:
    CURRENT: str = "current"
    PREVIEW: str = "preview"


@dataclass(frozen=True)
class DLTEdition:
    CORE: str = "core"
    PRO: str = "pro"
    ADVANCED: str = "advanced"


@dataclass(frozen=True)
class DLTPipeline:
    name: str
    language: Literal["SQL", "PYTHON"]
    notebook_path: str
    configuration: Optional[Dict[str, str]] = None
    allow_duplicate_names: Optional[bool] = None

    # node type is required and everything is stubbed for future support
    cluster: Cluster = Cluster("dlt-cluster", "dlt-spark-version", "dlt-vm")
    channel: str = DLTChannels.CURRENT

    # continuous: bool = False  # forced to be false
    development: bool = True
    edition: str = DLTEdition.ADVANCED
    photon: bool = False

    # Catalog for unity catalog.
    catalog: Optional[str] = None
    storage: Optional[str] = None
    target: Optional[str] = None

    def to_b64(self, working_dir: str) -> str:
        with (Path(working_dir) / Path(self.notebook_path)).open(
            "r", encoding="utf-8"
        ) as f:
            return base64.b64encode(f.read().encode("utf-8")).decode("utf-8")

    @staticmethod
    def cleanup(d: Dict[str, Any]) -> None:
        d.pop("language", None)
        d.pop("notebook_path", None)
        d.pop("cluster", None)
        d.pop("allow_duplicate_names", None)

    def to_dict(self) -> Dict[str, Any]:
        d = dataclasses.asdict(self)
        d["continuous"] = False
        if self.allow_duplicate_names is not None:
            if self.configuration is None:
                d["configuration"] = {}
            d["configuration"]["allow_duplicate_names"] = self.allow_duplicate_names
        self.cleanup(d)
        return d


class NotebookTask(JobsTasksNotebookTask):
    pass


class SparkJarTask(JobsTasksSparkJarTask):
    """
    The SparkJarTask class  is designed to handle the execution of a Spark job which had JAR dependencies in a
    Databricks workspace.One has to make sure that the JAR file(s) are uploaded to the dbfs (or) s3 and provide
    the absolute path in library.An instance of SparkJarTask represents a Spark job that is identified by its main
    class name and optionally by its parameters.

    Attributes:
        main_class_name (str, optional): The main class name of the Spark job to be run.
        parameters (List[str], optional): The parameters for the Spark job. If not provided, default
        parameters are used.

    Examples:
        Below are the different ways in which the SparkJarTask class can be used:
        @wf.spark_jar_task(
                    libraries=[
                        JarTaskLibrary(
                            jar="dbfs:/Volumes/development/global_sustainability_dev/spark_jar_test/PrintArgs.jar"
                        )
                    ]
                )
            def spark_jar_task_a():
                return SparkJarTask(
                    main_class_name="PrintArgs",
                    parameters=["Hello", "World!"],
                )
         -------------------------------------------------------------------------------
        @wf.spark_jar_task(
                    libraries=[
                        JarTaskLibrary(
                            jar="s3:/Volumes/development/global_sustainability_dev/spark_jar_test/PrintArgs.jar"
                        )
                    ]
                )
            def spark_jar_task_a():
                return SparkJarTask(
                    main_class_name="PrintArgs",
                    parameters=["Hello", "World!"],
                )
    """

    main_class_name: Optional[str]
    parameters: Optional[List[str]] = None

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.main_class_name = kwargs.get("main_class_name", None)
        self.parameters = kwargs.get("parameters", None)


class SparkPythonTask(JobsTasksSparkPythonTask):
    """
    The SparkPythonTask class is designed to handle the execution of a Spark job with Python dependencies in a
    Databricks workspace. One has to make sure that the Python file(s) are uploaded to the worksapce (or) git
    and provide the absolute path in the library. An instance of SparkPythonTask represents a Spark job that
    is identified by its main class name and optionally by its parameters.

    Attributes:
        main_class_name (str, optional): The main class name of the Spark job to be run.
        parameters (List[str], optional): The parameters for the Spark job. If not provided, default
        parameters are used.

    Examples:
        Below are the different ways in which the SparkPythonTask class can be used:
        @wf.spark_python_task(
                    libraries=[
                        PypiTaskLibrary(
                            package="koheesio"
                        )
                    ]
                )
            def spark_python_task_a():
                return SparkPythonTask(
                    python_file="path/to/python/file.py",
                    source="GIT",
                    parameters=["--param1", "World!"],
                )
    """

    python_file: str
    source: Optional[str] = None
    parameters: Optional[List[str]] = None

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.source = kwargs.get("source", None)
        self.parameters = kwargs.get("parameters", None)
        self.python_file = kwargs.get("python_file", None)


class RunJobTask(JobsTasksRunJobTask):
    """
    The RunJobTask class is designed to handle the execution of a specific job in a Databricks workspace.

    An instance of RunJobTask represents a job that is identified by its name. The job can also be executed on a
    specific host, which is authenticated using a token. The job can also be provided with parameters.

    The RunJobTask class provides additional functionality for retrieving the job ID based on the job name, host,
    and token.

    Attributes:
        job_name (str): The name of the job to be run.
        host (str, optional): The host on which the job is to be run. If not provided, a default host is used.
        token (str, optional): The token used for authentication. If not provided, a default token is used.
        job_parameters (Any, optional): The parameters for the job. If not provided, default parameters are used.

    Examples:
        Below are the different ways in which the RunJobTask class can be used inside workflow (run_job_task).:
            1. RunJobTask(job_name="dev_object_raw_to_cleansed", host="YOUR_WORKSPACE_URL",
            token="***********",job_parameters={"param1": "value1", "param2": "value2"})

            2. RunJobTask(job_name="dev_object_raw_to_cleansed",
            job_parameters={"param1": "value1", "param2": "value2"})

            3. RunJobTask(job_name="dev_object_raw_to_cleansed")
    """

    job_name: str
    job_id: Optional[float] = None
    host: Optional[str] = None
    token: Optional[str] = None
    job_parameters: Optional[Any] = None

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.job_id = get_job_id(self.job_name, self.host, self.token)
        self.job_parameters = kwargs.get("job_parameters", None)


class SqlTask(JobsTasksSqlTask):
    """
    The SqlTask class is designed to handle SQL tasks in a more specific context.

    An instance of SqlTask represents a SQL task that can be associated with either a SQL query, a file path, an alert,
    or a dashboard. Each of these associations is represented by a unique identifier (ID).
    The SqlTask class ensures that only one of these associations is present for any given instance.

    The SqlTask class also provides additional functionality for handling subscriptions. Subscriptions can be paused,
    and custom subjects can be set for dashboard-related tasks.

    Attributes:
        dashboard_id (str, optional): The ID of the dashboard.
        dashboard_custom_subject (str, optional): The custom subject of the dashboard.
        file_path (str, optional): The path of the SQL file.
        alert_id (str, optional): The ID of the alert.
        pause_subscriptions (bool, optional): If true, the alert notifications are not sent to subscribers.
        subscriptions (dict, optional): The subscriptions for the alert or dashboard.
        parameters (dict, optional): The parameters for the SQL task.
        query_id (str, optional): The ID of the SQL query.
        warehouse_id (str): The ID of the warehouse.

    Examples:
        Below are the different ways in which the SqlTask class can be used inside workflow (sql_task).:
            For SQL query: SqlTask(query_id= "YOUR_QUERY_ID", warehouse_id="YOUR_WAREHOUSE_ID")
            For SQL file: SqlTask(file_path="/Workspace/Users/YOUR_USERNAME/raju_sql_test_brickflow.sql",
              warehouse_id="your_warehouse_id")
            For Sql alerts: SqlTask(alert_id="Your_Alert_ID", pause_subscriptions=False,
                subscriptions={"usernames":["YOUR_USERNAME", 'YOUR_USERNAME']}
                ,warehouse_id="your_warehouse_id")
            For SQL dashboards: SqlTask(dashboard_id="Your_Dashboard_ID",
                dashboard_custom_subject="Raju Legacy Dashboard Test", pause_subscriptions=True,
                subscriptions={"usernames":["YOUR_USERNAME", 'YOUR_USERNAME'],
                "destination_id":["your_destination_id"]},warehouse_id="your_warehouse_id")
    """

    dashboard_id: Optional[str] = None
    dashboard_custom_subject: Optional[str] = None
    file_path: Optional[str] = None
    alert_id: Optional[str] = None
    pause_subscriptions: Optional[bool] = None
    subscriptions: Optional[Dict[str, List[str]]] = None
    parameters: Optional[Dict[str, str]] = None
    query_id: Optional[str] = None
    warehouse_id: str

    def __init__(self, *args: Any, **kwds: Any):
        super().__init__(*args, **kwds)
        # logging and handling conditions
        if (
            sum(
                [
                    self.query_id is not None,
                    self.file_path is not None,
                    self.alert_id is not None,
                    self.dashboard_id is not None,
                ]
            )
            != 1
        ):
            ctx.log.warning(
                "SqlTask must have exactly one of query_id or file_path or alert or dashboard.\
                  Find more examples on how to use SqlTask in the documentation."
            )
        else:
            if self.query_id:
                self.query = JobsTasksSqlTaskQuery(query_id=self.query_id)
            if self.file_path:
                self.file = JobsTasksSqlTaskFile(path=self.file_path)
            if self.alert_id:
                if self.subscriptions:
                    self.alert = JobsTasksSqlTaskAlert(
                        alert_id=self.alert_id,
                        pause_subscriptions=self.pause_subscriptions,
                        subscriptions=[
                            JobsTasksSqlTaskAlertSubscriptions(user_name=username)
                            for username in self.subscriptions.get("usernames", "")
                        ]
                        + [
                            JobsTasksSqlTaskAlertSubscriptions(
                                destination_id=destination_id
                            )
                            for destination_id in self.subscriptions.get(
                                "destination_id", ""
                            )
                        ],
                    )
            if self.dashboard_id:
                if self.subscriptions:
                    self.dashboard = JobsTasksSqlTaskDashboard(
                        dashboard_id=self.dashboard_id,
                        custom_subject=self.dashboard_custom_subject,
                        pause_subscriptions=self.pause_subscriptions,
                        subscriptions=[
                            JobsTasksSqlTaskDashboardSubscriptions(user_name=username)
                            for username in self.subscriptions.get("usernames", "")
                        ]
                        + [
                            JobsTasksSqlTaskDashboardSubscriptions(
                                destination_id=destination_id
                            )
                            for destination_id in self.subscriptions.get(
                                "destination_id", ""
                            )
                        ],
                    )


class IfElseConditionTask(JobsTasksConditionTask):
    """
    The IfElseConditionTask class is designed to handle conditional tasks in a workflow.
    An instance of IfElseConditionTask represents a conditional task that compares two values (left and right)
    using a specified operator. The operator can be one of the following: "==", "!=", ">", "<", ">=", "<=".

    The IfElseConditionTask class provides additional functionality for
    mapping the provided operator to a specific operation. For example,
    the operator "==" is mapped to "EQUAL_TO", and the operator "!=" is mapped to "NOT_EQUAL".

    Attributes:
        left (str): The left operand in the condition.
        right (str): The right operand in the condition.
        It can be one of the following: "==", "!=", ">", "<", ">=", "<=".
        op (Operator): The operation corresponding to the operator.
        It is determined based on the operator.

    Examples:
        Below are the different ways in which the IfElseConditionTask class
        can be used inside a workflow (if_else_condition_task).:
            1. IfElseConditionTask(left="value1", right="value2", op="==")
            2. IfElseConditionTask(left="value1", right="value2", op="!=")
            3. IfElseConditionTask(left="value1", right="value2", op=">")
            4. IfElseConditionTask(left="value1", right="value2", op="<")
            5. IfElseConditionTask(left="value1", right="value2", op=">=")
            6. IfElseConditionTask(left="value1", right="value2", op="<=")
    """

    left: str
    right: str
    op: str

    def __init__(self, *args: Any, **kwds: Any):
        super().__init__(*args, **kwds)
        self.left = kwds["left"]
        self.right = kwds["right"]
        self.op = str(Operator(self.op).name)


class DefaultBrickflowTaskPluginImpl(BrickflowTaskPluginSpec):
    @staticmethod
    @brickflow_task_plugin_impl
    def handle_results(resp: "TaskResponse", task: "Task", workflow: "Workflow") -> Any:
        _ilog.info("using default for handling results")

        BrickflowTaskPluginSpec.handle_user_result_errors(resp)
        # by default don't do anything just return the response as is
        return resp

    @staticmethod
    @brickflow_task_plugin_impl
    def task_execute(task: "Task", workflow: "Workflow") -> TaskResponse:
        """default execute implementation method."""
        _ilog.info("using default plugin for handling task execute")

        if (
            task.task_type == TaskType.CUSTOM_PYTHON_TASK
            and task.custom_execute_callback is not None
        ):
            _ilog.info("handling custom execute")
            return task.custom_execute_callback(task)
        else:
            kwargs = task.get_runtime_parameter_values()
            try:
                return TaskResponse(
                    task.task_func(**kwargs),
                    user_code_error=None,
                    push_return_value=True,
                    input_kwargs=kwargs,
                )
            except Exception as e:
                return TaskResponse(
                    None, push_return_value=True, user_code_error=e, input_kwargs=kwargs
                )


@functools.lru_cache
def get_plugin_manager() -> pluggy.PluginManager:
    pm = pluggy.PluginManager(BRICKFLOW_TASK_PLUGINS)
    pm.add_hookspecs(BrickflowTaskPluginSpec)
    pm.load_setuptools_entrypoints(BRICKFLOW_TASK_PLUGINS)
    pm.register(DefaultBrickflowTaskPluginImpl(), name="default")
    for name, plugin_instance in pm.list_name_plugin():
        _ilog.info(
            "Loaded plugin with name: %s and class: %s",
            name,
            plugin_instance.__class__.__name__,
        )
    return pm


@functools.lru_cache
def get_brickflow_tasks_hook(
    cache_bust: Optional[pluggy.PluginManager] = None,
) -> BrickflowTaskPluginSpec:
    """cache_bust is only used for unit testing"""
    try:
        from brickflow_plugins import load_plugins, ensure_installation  # noqa

        ensure_installation()
        load_plugins(cache_bust)
    except ImportError as e:
        _ilog.info(
            "If you need airflow support: brickflow extras not installed "
            "please pip install brickflow[airflow] and py4j! Error: %s",
            str(e.msg),
        )
    return get_plugin_manager().hook


def pretty_print_function_source(
    task_name: str,
    func: Callable,
    start_line: Optional[int] = None,
    end_line: Optional[int] = None,
) -> str:
    source_lines, start_line_num = inspect.getsourcelines(func)
    source_code = "".join(source_lines)
    formatted_code = textwrap.dedent(source_code)

    if start_line is None:
        start_line = start_line_num
    if end_line is None:
        end_line = start_line_num + len(source_lines) - 1

    buffer = StringIO()
    file_name = inspect.getfile(func)
    buffer.write(
        r"""
      | # ======================================================================
      | #     ____                                     ____             _       
      | #    / ___|   ___   _   _  _ __   ___   ___   / ___|  ___    __| |  ___ 
      | #    \___ \  / _ \ | | | || '__| / __| / _ \ | |     / _ \  / _` | / _ \
      | #     ___) || (_) || |_| || |   | (__ |  __/ | |___ | (_) || (_| ||  __/
      | #    |____/  \___/  \__,_||_|    \___| \___|  \____| \___/  \__,_| \___|
      | # ======================================================================"""  # noqa
        + f"\n"
        f"      | # Task Name: {task_name}\n"
        f"      | # Function Name: '{func.__name__}'\n"
        f"      | # File: {file_name}\n"
        f"      | # Lines: {start_line}-{end_line}\n"
    )

    for line_num, line in enumerate(formatted_code.split("\n"), start=start_line_num):
        if start_line <= line_num <= end_line:
            buffer.write(f"{line_num:5d} | {line}\n")
    buffer.write("      | # ========================================================\n")
    buffer.seek(0)
    return buffer.read()


@dataclass(frozen=True)
class Task:
    task_id: str
    task_func: Callable
    workflow: Workflow  # noqa
    cluster: Cluster
    description: Optional[str] = None
    libraries: List[TaskLibrary] = field(default_factory=lambda: [])
    depends_on: List[Union[Callable, str]] = field(default_factory=lambda: [])
    task_type: TaskType = TaskType.BRICKFLOW_TASK
    trigger_rule: BrickflowTriggerRule = BrickflowTriggerRule.ALL_SUCCESS
    task_settings: Optional[TaskSettings] = None
    custom_execute_callback: Optional[Callable] = None
    ensure_brickflow_plugins: bool = False
    health: Optional[List[JobsTasksHealthRules]] = None
    if_else_outcome: Optional[Dict[Union[str, str], str]] = None

    def __post_init__(self) -> None:
        self.is_valid_task_signature()

    @property
    def task_func_name(self) -> str:
        return self.task_func.__name__

    @property
    def parents(self) -> List[str]:
        return list(self.workflow.parents(self.task_id))

    @property
    def depends_on_names(self) -> Iterator[Dict[str, Optional[str]]]:
        for i in self.depends_on:
            if self.if_else_outcome:
                outcome = list(self.if_else_outcome.values())[0]
            else:
                outcome = None

            if callable(i) and hasattr(i, "__name__"):
                yield {i.__name__: outcome}
            else:
                yield {str(i): outcome}

    @property
    def databricks_task_type_str(self) -> str:
        if self.task_type == TaskType.BRICKFLOW_TASK:
            return TaskType.NOTEBOOK_TASK.value
        if self.task_type == TaskType.CUSTOM_PYTHON_TASK:
            return TaskType.NOTEBOOK_TASK.value
        return self.task_type.value

    @property
    def builtin_notebook_params(self) -> Dict[str, str]:
        # 2 braces to escape for 1
        return {i.value: f"{{{{{i.name}}}}}" for i in BrickflowBuiltInTaskVariables}

    @property
    def name(self) -> str:
        return self.task_id

    @property
    def brickflow_default_params(self) -> Dict[str, str]:
        return {
            BrickflowInternalVariables.workflow_id.value: self.workflow.name,
            # 2 braces to escape 1
            BrickflowInternalVariables.task_id.value: f"{{{{{BrickflowBuiltInTaskVariables.task_key.name}}}}}",
            BrickflowInternalVariables.only_run_tasks.value: "",
            BrickflowInternalVariables.workflow_prefix.value: self.workflow.prefix
            or "",
            BrickflowInternalVariables.workflow_suffix.value: self.workflow.suffix
            or "",
            BrickflowInternalVariables.env.value: ctx.env,
        }

    @staticmethod
    def handle_notebook_path(entrypoint: str) -> str:
        # local will get created as workspace notebook job and not a git source job
        if ctx.env == BrickflowDefaultEnvs.LOCAL.value:
            # check and ensure suffix has .py extension
            return entrypoint if entrypoint.endswith(".py") else f"{entrypoint}.py"
        return entrypoint

    def get_obj_dict(self, entrypoint: str) -> Dict[str, Any]:
        return {
            "notebook_path": self.handle_notebook_path(entrypoint),
            "base_parameters": {
                **self.builtin_notebook_params,
                **self.brickflow_default_params,
                **self.custom_task_parameters,  # type: ignore
                # **(self.custom_unique_task_parameters or {}),
                # TODO: implement only after validating limit on parameters
            },
        }

    def _ensure_brickflow_plugins(self) -> None:
        if self.ensure_brickflow_plugins is False:
            return
        try:
            import brickflow_plugins  # noqa
        except ImportError as e:
            raise ImportError(
                f"Brickflow Plugins not available for task: {self.name}. "
                "If you need airflow support: brickflow extras not installed "
                "please pip install brickflow[airflow] and py4j! Error: %s",
                str(e.msg),
            )

    # TODO: error if star isn't there
    def is_valid_task_signature(self) -> None:
        # only supports kwonlyargs with defaults
        spec: inspect.FullArgSpec = inspect.getfullargspec(self.task_func)
        sig: inspect.Signature = inspect.signature(self.task_func)
        signature_error_msg = (
            "Task signatures only supports kwargs with defaults. or catch all varkw **kwargs"
            "For example def execute(*, variable_a=None, variable_b=None, **kwargs). "
            f"Please fix function def {self.task_func_name}{sig}: ..."
        )
        kwargs_default_error_msg = (
            f"Keyword arguments must be Strings. "
            f"Please handle booleans and numbers via strings. "
            f"Please fix function def {self.task_func_name}{sig}: ..."
        )

        valid_case = spec.args == [] and spec.varargs is None and spec.defaults is None
        for _, v in (spec.kwonlydefaults or {}).items():
            # in python boolean is a type of int must be captured here via short circuit
            if not (isinstance(v, str) or v is None):
                raise InvalidTaskSignatureDefinition(kwargs_default_error_msg)
        if valid_case:
            return

        raise InvalidTaskSignatureDefinition(signature_error_msg)

    @property
    def custom_task_parameters(self) -> Dict[str, str]:
        final_task_parameters: Dict[str, str] = {}
        if self.workflow.common_task_parameters is not None:
            final_task_parameters = self.workflow.common_task_parameters.copy() or {}
        spec: inspect.FullArgSpec = inspect.getfullargspec(self.task_func)

        if spec.kwonlydefaults:
            # convert numbers into strings for base parameters
            final_task_parameters.update(
                {k: str(v) for k, v in spec.kwonlydefaults.items()}
            )

        if (
            BrickflowEnvVars.BRICKFLOW_PROJECT_PARAMS.value in os.environ
            and os.environ.get(BrickflowEnvVars.BRICKFLOW_PROJECT_PARAMS.value)
        ):
            final_task_parameters[
                BrickflowEnvVars.BRICKFLOW_PROJECT_PARAMS.value.lower()
            ] = str(os.environ[BrickflowEnvVars.BRICKFLOW_PROJECT_PARAMS.value])
        return final_task_parameters

    # @property
    # def custom_unique_task_parameters(self) -> Dict[str, str]:
    #     return {f"uniq_{self.name}_k": v for k, v in self.custom_task_parameters.items()}

    def get_runtime_parameter_values(self) -> Dict[str, Any]:
        # if dbutils returns None then return v instead
        return {
            k: (ctx.get_parameter(k, str(v)) or v)
            for k, v in (
                inspect.getfullargspec(self.task_func).kwonlydefaults or {}
            ).items()
        }

    @staticmethod
    def _get_skip_with_reason(cond: bool, reason: str) -> Tuple[bool, Optional[str]]:
        if cond is True:
            return cond, reason
        return cond, None

    def should_skip(self) -> Tuple[bool, Optional[str]]:
        # return true or false and reason
        node_skip_checks = []
        for parent in self.parents:
            if parent != ROOT_NODE:
                try:
                    task_to_not_skip = ctx.task_coms.get(parent, BRANCH_SKIP_EXCEPT)
                    if self.name != task_to_not_skip:
                        # set this task to skip hack to keep to empty to trigger failure
                        # key look up will fail
                        node_skip_checks.append(True)
                    else:
                        node_skip_checks.append(False)
                except Exception:
                    # ignore errors as it probably doesnt exist
                    # TODO: log errors
                    node_skip_checks.append(False)
        if not node_skip_checks:
            return False, None
        if self.trigger_rule == BrickflowTriggerRule.NONE_FAILED:
            # by default a task failure automatically skips
            return self._get_skip_with_reason(
                all(node_skip_checks),
                "At least one task before this were not successful",
            )
        # default is BrickflowTriggerRule.ALL_SUCCESS
        return self._get_skip_with_reason(
            any(node_skip_checks), "All tasks before this were not successful"
        )

    def _skip_because_not_selected(self) -> Tuple[bool, Optional[str]]:
        selected_tasks = ctx.get_parameter(
            BrickflowInternalVariables.only_run_tasks.value,
            config(BrickflowTaskEnvVars.BRICKFLOW_SELECT_TASKS.value, ""),
        )
        if selected_tasks is None or selected_tasks == "":
            return False, None

        if selected_tasks.startswith("[") and selected_tasks.endswith("]"):
            try:
                selected_task_list = json.loads(selected_tasks)
            except json.JSONDecodeError:
                selected_task_list = []
                _ilog.info(
                    "Invalid JSON list in `brickflow_internal_only_run_tasks` parameter. Nothing will be skipped."
                )
            except Exception as e:
                selected_task_list = []
                _ilog.info(
                    "Error parsing `brickflow_internal_only_run_tasks` parameter as JSON, nothing to skip. Error: %s",
                    str(e),
                )
        else:
            selected_task_list = selected_tasks.split(",")

        selected_task_list = [task.strip() for task in selected_task_list]

        if self.name not in selected_task_list:
            return (
                True,
                f"This task: {self.name} is not a selected task: {selected_task_list}",
            )
        return False, None

    @with_brickflow_logger
    def execute(self, ignore_all_deps: bool = False) -> Any:
        # Workflow is:
        #   1. Check to see if there selected tasks and if there are is this task in the list
        #   2. Check to see if the previous task is skipped and trigger rule.
        #   3. Check to see if this a custom python task and execute it
        #   4. Execute the task function
        _ilog.setLevel(logging.INFO)  # enable logging for task execution
        ctx._set_current_task(self.name)
        self._ensure_brickflow_plugins()  # if you are expecting brickflow plugins to be installed
        if ignore_all_deps is True:
            _ilog.info(
                "Ignoring all dependencies for task: %s due to debugging", self.name
            )
        _select_task_skip, _select_task_skip_reason = self._skip_because_not_selected()
        if _select_task_skip is True and ignore_all_deps is False:
            # check if this task is skipped due to task selection
            _ilog.info(
                "Skipping task... %s for reason: %s",
                self.name,
                _select_task_skip_reason,
            )
            ctx._reset_current_task()
            return
        _skip, reason = self.should_skip()
        if _skip is True and ignore_all_deps is False:
            _ilog.info("Skipping task... %s for reason: %s", self.name, reason)
            ctx.task_coms.put(self.name, BRANCH_SKIP_EXCEPT, SKIP_EXCEPT_HACK)
            ctx._reset_current_task()
            return

        _ilog.info("Executing task... %s", self.name)
        _ilog.info("%s", pretty_print_function_source(self.name, self.task_func))

        brickflow_execution_hook = get_brickflow_tasks_hook()

        initial_resp: TaskResponse = brickflow_execution_hook.task_execute(
            task=self, workflow=self.workflow
        )
        resp: TaskResponse = brickflow_execution_hook.handle_results(
            resp=initial_resp, task=self, workflow=self.workflow
        )
        if resp.push_return_value is True:
            ctx.task_coms.put(self.name, RETURN_VALUE_KEY, resp.response)
        ctx._reset_current_task()
        return resp.response


def filter_bf_related_libraries(
    libraries: Optional[List[TaskLibrary]],
) -> List[TaskLibrary]:
    if libraries is None:
        return []
    resp: List[TaskLibrary] = []
    for lib in libraries:
        if isinstance(lib, PypiTaskLibrary):
            if lib.package.startswith("brickflows") is True:
                continue
        if isinstance(lib, PypiTaskLibrary):
            if lib.package.startswith("apache-airflow") is True:
                continue
        if isinstance(lib, MavenTaskLibrary):
            # TODO: clean this up but no one should really be using cron-utils at the moment for outside of brickflow
            if lib.coordinates.startswith("com.cronutils:cron-utils:9.2.0") is True:
                continue
        resp.append(lib)
    return resp


def is_semver(v: str) -> bool:
    return len(v.split(".")) >= 3


def get_brickflow_lib_version(bf_version: str, cli_version: str) -> str:
    bf_version = bf_version.lstrip(
        "v"
    )  # users can provide v1.0.0 we want to normalize it to 1.0.0; it could be a tag
    cli_version_is_actual_tag = all(
        v.isnumeric() for v in cli_version.split(".")
    )  # is it a proper tag for pypi
    bf_version_is_actual_tag = all(
        v.isnumeric() for v in bf_version.split(".")
    )  # is it a proper tag for pypi
    # TODO: make these if conditions into sentences
    if (
        bf_version is not None
        and is_semver(bf_version) is True
        and bf_version_is_actual_tag is True
    ):
        bf_version = bf_version.lstrip("v")
    elif (
        bf_version is not None
        and is_semver(bf_version) is True
        and bf_version_is_actual_tag is False
    ):
        bf_version = f"v{bf_version.lstrip('v')}"
    elif (
        bf_version is not None
        and bf_version == DEFAULT_BRICKFLOW_VERSION_MODE
        and cli_version_is_actual_tag is True
    ):
        bf_version = cli_version
    elif (
        bf_version is not None
        and bf_version != DEFAULT_BRICKFLOW_VERSION_MODE
        and is_semver(bf_version) is False
    ):
        pass  # do nothing and use the version as is
    else:
        bf_version = "main"
    return bf_version


def get_brickflow_libraries(enable_plugins: bool = False) -> List[TaskLibrary]:
    settings = BrickflowProjectDeploymentSettings()
    bf_version = settings.brickflow_project_runtime_version
    cli_version = get_brickflow_version()
    bf_version = get_brickflow_lib_version(bf_version, cli_version)
    is_bf_version_semver = is_semver(bf_version)
    is_all_parts_numeric = all(v.isnumeric() for v in bf_version.split("."))

    if is_bf_version_semver is True and is_all_parts_numeric is True:
        bf_lib = PypiTaskLibrary(f"brickflows=={bf_version}")
    else:
        bf_lib = PypiTaskLibrary(
            f"brickflows @ git+https://github.com/Nike-Inc/brickflow.git@{bf_version}"
        )

    if settings.brickflow_enable_plugins is True or enable_plugins is True:
        return [
            bf_lib,
            PypiTaskLibrary("apache-airflow==2.7.3"),
            PypiTaskLibrary("snowflake==0.6.0"),
            PypiTaskLibrary("tableauserverclient==0.25"),
            PypiTaskLibrary("boxsdk==3.9.2"),
            PypiTaskLibrary("cerberus-python-client==2.5.4"),
            MavenTaskLibrary("com.cronutils:cron-utils:9.2.0"),
        ]
    else:
        return [bf_lib]
