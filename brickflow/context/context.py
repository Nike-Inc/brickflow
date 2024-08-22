import base64
import time

import binascii
import copy
import functools
import logging
import pickle
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Any, Union, Callable, Hashable, Dict, List, TypeVar

from decouple import config

from brickflow import log, _ilog, BrickflowEnvVars, BrickflowDefaultEnvs, deprecated

BRANCH_SKIP_EXCEPT = "branch_skip_except"
SKIP_EXCEPT_HACK = "brickflow_hack_skip_all"
RETURN_VALUE_KEY = "return_value"

T = TypeVar("T")


# TODO: remove
class ContextMode(Enum):
    databricks = "databricks"
    not_databricks = "not_databricks"


class BrickflowBuiltInTaskVariables(Enum):
    # key is the {{ }} and value is the key
    job_id = "brickflow_job_id"
    run_id = "brickflow_run_id"
    start_date = "brickflow_start_date"
    start_time = "brickflow_start_time"
    task_retry_count = "brickflow_task_retry_count"
    parent_run_id = "brickflow_parent_run_id"
    task_key = "brickflow_task_key"


class BrickflowInternalVariables(Enum):
    workflow_id = "brickflow_internal_workflow_name"
    task_id = "brickflow_internal_task_name"
    only_run_tasks = "brickflow_internal_only_run_tasks"
    workflow_prefix = "brickflow_internal_workflow_prefix"
    workflow_suffix = "brickflow_internal_workflow_suffix"
    env = BrickflowEnvVars.BRICKFLOW_ENV.value.lower()


def bind_variable(builtin: BrickflowBuiltInTaskVariables) -> Callable:
    def wrapper(f: Callable) -> Callable:
        @functools.wraps(f)
        def func(*args, **kwargs):  # type: ignore
            _self: Context = args[0]  # type: ignore
            debug = kwargs["debug"]
            f(*args, **kwargs)  # no-op
            if _self.dbutils is not None:
                return _self.get_parameter(builtin.value, debug)
            return debug

        return func

    return wrapper


class TaskComsObjectResult(Enum):
    NO_RESULTS = "NO_RESULTS"


@dataclass
class BrickflowTaskComsObject:
    # Use to encode any hashable value into bytes and then pickle.unloads
    @dataclass(frozen=True)
    class _TaskComsObject:
        value: Hashable

    _value: Any = None
    _task_coms_obj: _TaskComsObject = field(init=False)

    def __post_init__(self) -> None:
        self._task_coms_obj = self._TaskComsObject(self._value)

    @property
    def value(self) -> Any:
        return self._task_coms_obj.value

    @property
    def to_encoded_value(self) -> str:
        results_bytes = pickle.dumps(self._task_coms_obj)
        return base64.b64encode(results_bytes).decode("utf-8")

    @classmethod
    def from_encoded_value(
        cls, encoded_value: Union[str, bytes]
    ) -> "BrickflowTaskComsObject":
        try:
            _encoded_value = (
                encoded_value
                if isinstance(encoded_value, bytes)
                else encoded_value.encode("utf-8")
            )
            b64_bytes = base64.b64decode(_encoded_value)
            return cls(pickle.loads(b64_bytes).value)
        except binascii.Error:
            _decoded_value = (
                encoded_value.decode("utf-8")
                if isinstance(encoded_value, bytes)
                else encoded_value
            )
            return cls(_decoded_value)


@dataclass
class BrickflowTaskComsDict:
    task_id: str
    task_coms: "BrickflowTaskComs"

    def __getitem__(self, key: str) -> Any:
        # fake behavior in airflow for: {{ ti.xcom_pull(task_ids='task_id')['arg'] }}
        return self.task_coms.get(task_id=self.task_id, key=key)


@dataclass(frozen=True)
class BrickflowTaskComs:
    dbutils: Optional[Any] = None
    storage: Dict[str, Any] = field(init=False, default_factory=lambda: {})

    @staticmethod
    def _key(task_id: str, key: str) -> str:
        return f"{task_id}::{key}"

    def put(self, task_id: str, key: str, value: Any) -> None:
        encoded_value = BrickflowTaskComsObject(value).to_encoded_value
        if self.dbutils is not None:
            self.dbutils.jobs.taskValues.set(key, encoded_value)
        else:
            # TODO: logging using local task coms
            self.storage[self._key(task_id, key)] = encoded_value

    def get(self, task_id: str, key: Optional[str] = None) -> Any:
        if key is None:
            return BrickflowTaskComsDict(task_id=task_id, task_coms=self)
        if self.dbutils is not None:
            encoded_value = self.dbutils.jobs.taskValues.get(
                key=key, taskKey=task_id, debugValue="debug"
            )
            return BrickflowTaskComsObject.from_encoded_value(encoded_value).value
        else:
            # TODO: logging using local task coms
            encoded_value = self.storage[self._key(task_id, key)]
            return BrickflowTaskComsObject.from_encoded_value(encoded_value).value


class Context:
    def __init__(self) -> None:
        # Order of init matters todo: fix this

        self._dbutils: Optional[Any] = None
        self._spark: Optional[Any] = None
        self._task_coms: BrickflowTaskComs
        self._current_task: Optional[str] = None
        self._configure()
        self._current_project: Optional[str] = None

    def __new__(cls) -> "Context":
        if not hasattr(cls, "instance"):
            cls.instance = super(Context, cls).__new__(cls)
        return cls.instance  # noqa

    def _configure(self) -> None:
        # testing purposes only
        self._set_spark_session()
        self._configure_dbutils()
        self._task_coms = BrickflowTaskComs(self._dbutils)

    @property
    def current_task(self) -> Optional[str]:
        return self._current_task

    def get_current_timestamp(self) -> int:
        return int(time.time() * 1000)

    def _set_current_task(self, task_key: str) -> None:
        self._current_task = task_key

    def _reset_current_task(self) -> None:
        self._current_task = None

    def get_return_value(self, task_key: Union[str, Callable]) -> Any:
        task_key = task_key.__name__ if callable(task_key) else task_key
        return self.task_coms.get(task_key, RETURN_VALUE_KEY)

    def skip_all_except(self, branch_task: Union[Callable, str]) -> None:
        if self._current_task is None:
            raise RuntimeError("Current task is empty unable to skip...")
        branch_task_key = (
            branch_task.__name__
            if callable(branch_task) and hasattr(branch_task, "__name__") is True
            else branch_task
        )
        self._task_coms.put(self._current_task, BRANCH_SKIP_EXCEPT, branch_task_key)

    def skip_all_following(self) -> None:
        if self._current_task is None:
            raise RuntimeError("Current task is empty unable to skip...")
        self._task_coms.put(self._current_task, BRANCH_SKIP_EXCEPT, SKIP_EXCEPT_HACK)

    @property
    def task_coms(self) -> BrickflowTaskComs:
        return self._task_coms

    @property
    def current_project(self) -> Optional[str]:
        # TODO: not a public api move to internal context or deployment context
        return self._current_project or config(
            BrickflowEnvVars.BRICKFLOW_PROJECT_NAME.value, None
        )

    @staticmethod
    def _ensure_valid_project(project: str) -> None:
        env_project = config(BrickflowEnvVars.BRICKFLOW_PROJECT_NAME.value, None)
        if env_project is None:
            return
        if env_project != project:
            raise RuntimeError(
                f"Project: {project} does not match with env var: {BrickflowEnvVars.BRICKFLOW_PROJECT_NAME.value} "
                f"value: {env_project}"
            )

    def set_current_project(self, project: str) -> None:
        # TODO: not a public api move to internal context or deployment context
        self._ensure_valid_project(project)
        self._current_project = project

    @bind_variable(BrickflowBuiltInTaskVariables.task_key)
    def task_key(self, *, debug: Optional[str] = None) -> Any:
        """
        This function fetches the task_key value using the bind_variable decorator.
        The implementation is intentionally empty because the decorator handles the logic.
        """
        pass

    @bind_variable(BrickflowBuiltInTaskVariables.task_retry_count)
    def task_retry_count(self, *, debug: Optional[str] = None) -> Any:
        """
        This function fetches the task_retry_count value using the bind_variable decorator.
        The implementation is intentionally empty because the decorator handles the logic.
        """
        pass

    @bind_variable(BrickflowBuiltInTaskVariables.run_id)
    def run_id(self, *, debug: Optional[str] = None) -> Any:
        """
        This function fetches the run_id value using the bind_variable decorator.
        The implementation is intentionally empty because the decorator handles the logic.
        """
        pass

    @bind_variable(BrickflowBuiltInTaskVariables.job_id)
    def job_id(self, *, debug: Optional[str] = None) -> Any:
        """
        This function fetches the job_id value using the bind_variable decorator.
        The implementation is intentionally empty because the decorator handles the logic.
        """
        pass

    @bind_variable(BrickflowBuiltInTaskVariables.parent_run_id)
    def parent_run_id(self, *, debug: Optional[str] = None) -> Any:
        """
        This function fetches the parent_run_id value using the bind_variable decorator.
        The implementation is intentionally empty because the decorator handles the logic.
        """
        pass

    @bind_variable(BrickflowBuiltInTaskVariables.start_date)
    def start_date(self, *, debug: Optional[str] = None) -> Any:
        """
        This function fetches the start_date value using the bind_variable decorator.
        The implementation is intentionally empty because the decorator handles the logic.
        """
        pass

    @bind_variable(BrickflowBuiltInTaskVariables.start_time)
    def start_time(self, *, debug: Optional[str] = None) -> Any:
        """
        This function fetches the start_time value using the bind_variable decorator.
        The implementation is intentionally empty because the decorator handles the logic.
        """
        pass

    @property
    def log(self) -> logging.Logger:
        return log

    @property
    def dbutils(self) -> "DBUtils":  # type: ignore # noqa: F821
        return self._dbutils

    @property
    def spark(self) -> "SparkSession":  # type: ignore # noqa: F821
        return self._spark

    def is_local(self) -> bool:
        return self.env == BrickflowDefaultEnvs.LOCAL.value

    @property
    def env(self) -> str:
        # reused during deploy time, it uses env variable when deploying or testing locally, and uses
        # dbutils widgets during runtime time in jobs
        return config(
            BrickflowEnvVars.BRICKFLOW_ENV.value,
            self.get_parameter(
                BrickflowInternalVariables.env.value,
                BrickflowDefaultEnvs.LOCAL.value,
            ),
        )

    def get_by_env(
        self,
        purpose: str,
        *,
        default: Optional[T] = None,
        local: Optional[T] = None,
        dev: Optional[T] = None,
        non_prod: Optional[T] = None,
        test: Optional[T] = None,
        qa: Optional[T] = None,
        prod: Optional[T] = None,
        uat: Optional[T] = None,
        **kwargs: Optional[T],
    ) -> Optional[T]:
        # deep copy without modifying kwargs
        def add_if_not_none(
            _d: Dict[str, Optional[T]], _k: str, _v: Optional[T]
        ) -> None:
            if _v is None:
                return
            _d[_k] = _v

        _dict = copy.deepcopy(kwargs)
        add_if_not_none(_dict, "local", local)
        add_if_not_none(_dict, "non_prod", non_prod)
        add_if_not_none(_dict, "dev", dev)
        add_if_not_none(_dict, "test", test)
        add_if_not_none(_dict, "qa", qa)
        add_if_not_none(_dict, "prod", prod)
        add_if_not_none(_dict, "uat", uat)
        _env = self.env
        _ilog.info("Configuring: %s; Using env: '%s' to fetch value...", purpose, _env)
        if _env not in _dict and default is None:
            raise KeyError(
                f"Configuring: {purpose}; Unable to find environment key: {_env}, "
                f"only found env definitions: {list(_dict.keys())}"
            )
        if _env not in _dict and default is not None:
            _ilog.info(
                "Configuring: %s; Found no value configured with env: '%s' using default value...",
                purpose,
                _env,
            )
        res = _dict.get(_env, default)
        return res

    @deprecated
    def dbutils_widget_get_or_else(
        self, key: str, debug: Optional[str]
    ) -> Optional[str]:
        try:
            return self.dbutils.widgets.get(key)
        except Exception:
            # todo: log error
            return debug

    def get_parameter(self, key: str, debug: Optional[str] = None) -> Optional[str]:
        try:
            return self.dbutils.widgets.get(key)
        except Exception:
            # todo: log error
            _ilog.debug("Unable to get parameter: %s from dbutils", key)
            return debug

    def get_project_parameter(
        self, key: str, debug: Optional[str] = None
    ) -> Optional[str]:
        project_params = str(
            self.get_parameter(
                BrickflowEnvVars.BRICKFLOW_PROJECT_PARAMS.value.lower(), debug=debug
            )
        )
        if project_params == debug:
            return debug
        try:
            pairs = project_params.split(",")
            kv_dict = {pair.split("=")[0]: pair.split("=")[1] for pair in pairs}
            value = kv_dict.get(key)
            if value is None:
                _ilog.debug(
                    "Could not find the key in %s project params", project_params
                )
                return debug
            return value
        except KeyError:
            # todo: log error
            _ilog.debug("Could not find the key in %s project params", project_params)
            return debug

    def _try_import_chaining(self, callables: List[Callable]) -> Optional[Any]:
        for c in callables:
            try:
                return c()
            except (ImportError, AttributeError, KeyError, RuntimeError):
                if hasattr(c, "__name__"):
                    _ilog.info("Skipping execution of function: %s", c.__name__)
        return None

    def _set_spark_session(self) -> None:
        def __try_spark_from_ipython_notebook() -> None:
            import IPython  # noqa # pylint: disable=import-error

            self._spark = IPython.get_ipython().user_ns.get("spark", None)
            if self._spark is None:
                raise AttributeError("spark is not set")

        def __try_spark_from_spark_session() -> None:
            from pyspark.sql import (  # noqa # pylint: disable=import-error
                SparkSession,  # noqa
            )

            self._spark = SparkSession.getActiveSession()

        self._try_import_chaining(
            [__try_spark_from_ipython_notebook, __try_spark_from_spark_session]
        )
        _ilog.info("Spark Session object: ctx.spark is set to: %s", self.spark)

    def _configure_dbutils(self) -> ContextMode:
        def __try_dbutils_from_ipython_notebook() -> ContextMode:
            import IPython  # noqa # pylint: disable=import-error

            self._dbutils = IPython.get_ipython().user_ns.get("dbutils")
            if self._dbutils is None:
                raise AttributeError("dbutils is not set")
            return ContextMode.databricks

        def __try_dbutils_from_db_connect_jar() -> None:
            from pyspark.dbutils import (  # noqa # pylint: disable=import-error
                DBUtils,  # noqa
            )

            self._dbutils = DBUtils(self.spark)
            # cant gaurantee databricks

        resp = self._try_import_chaining(
            [__try_dbutils_from_ipython_notebook, __try_dbutils_from_db_connect_jar]
        )

        _ilog.info("DBUtils object: ctx.dbutils is set to: %s", self.dbutils)

        if resp is not None:
            return ContextMode.databricks

        return ContextMode.not_databricks


ctx = Context()
