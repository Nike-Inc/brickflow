import functools
import os
from abc import abstractmethod, ABCMeta
from typing import Optional

try:
    from airflow.models import BaseOperator, Pool
    from airflow.utils.weight_rule import WeightRule
except ImportError:
    raise ImportError(
        "You must install airflow to use airflow plugins, "
        "please try pip install brickflow[apache-airflow]"
    )

from brickflow.engine.task import Task
from brickflow.engine.workflow import Workflow


class AirflowTaskDoesNotExistError(Exception):
    pass


class UnsupportedAirflowTaskFieldError(Exception):
    pass


class UnsupportedAirflowOperatorError(Exception):
    pass


class AbstractOperatorModifier(metaclass=ABCMeta):
    @abstractmethod
    def set_next(
        self, op_handler: "AbstractOperatorModifier"
    ) -> "AbstractOperatorModifier":
        pass

    @abstractmethod
    def modify(
        self, operator: BaseOperator, task: Task, workflow: Workflow
    ) -> "BaseOperator":
        pass


class OperatorModifier(AbstractOperatorModifier):
    def __init__(self):
        self._next_handler: Optional[AbstractOperatorModifier] = None

    def set_next(
        self, op_handler: "AbstractOperatorModifier"
    ) -> "AbstractOperatorModifier":
        self._next_handler = op_handler
        return op_handler

    @abstractmethod
    def modify(
        self, operator: BaseOperator, task: Task, workflow: Workflow
    ) -> Optional["BaseOperator"]:
        if self._next_handler is not None:
            return self._next_handler.modify(operator, task, workflow)

        return None


class InvalidFieldChecker(OperatorModifier):
    UNSUPPORTED_TASK_NONE_FIELDS = {
        "email_on_retry": True,
        "email_on_failure": True,
        "sla": None,
        "execution_timeout": None,
        "on_failure_callback": None,
        "on_success_callback": None,
        "on_retry_callback": None,
        "inlets": [],
        "outlets": [],
        "task_concurrency": None,
        "max_active_tis_per_dag": None,
        "run_as_user": None,
        "depends_on_past": False,
        "wait_for_downstream": False,
        "max_retry_delay": None,
        "priority_weight": 1,
        "weight_rule": WeightRule.DOWNSTREAM,
        "pool": Pool.DEFAULT_POOL_NAME,
        "pool_slots": 1,
        "resources": None,
        "executor_config": {},
        "email": None,
    }

    def _validate_task_fields(self, operator: BaseOperator, task: Task) -> None:
        unsupported_fields = []
        for field, default_value in self.UNSUPPORTED_TASK_NONE_FIELDS.items():
            if hasattr(operator, field) is False:
                continue
            value = getattr(operator, field)
            if value != default_value:
                unsupported_fields.append(field)
        if unsupported_fields:
            raise UnsupportedAirflowTaskFieldError(
                f"Unsupported fields: {unsupported_fields} for task: {task.task_id}"
            )

    def modify(
        self, operator: BaseOperator, task: Task, workflow: Workflow
    ) -> Optional["BaseOperator"]:
        if isinstance(operator, BaseOperator):
            self._validate_task_fields(operator, task)
            return super().modify(operator, task, workflow)


class CatchAllOperatorModifier(OperatorModifier):
    SUPPORTED_OPERATORS = [
        "BranchPythonOperator",
        "PythonOperator",
        "BashOperator",
        "ShortCircuitOperator",
        "TaskDependencySensor",
        "AutosysSensor",
        "TableauRefreshDataSourceOperator",
        "TableauRefreshWorkBookOperator",
    ]

    def _validate_operators(self, operator: BaseOperator, task: Task) -> None:
        if (
            issubclass(operator.__class__, BaseOperator)
            and operator.__class__.__name__ in self.SUPPORTED_OPERATORS
        ):
            return
        raise UnsupportedAirflowOperatorError(
            f"Unsupported airflow operator: {type(task)} for task: {task.task_id}"
        )

    def modify(
        self, operator: BaseOperator, task: Task, workflow: Workflow
    ) -> Optional["BaseOperator"]:
        if isinstance(operator, BaseOperator):
            self._validate_operators(operator, task)
            return operator


def get_modifier_chain():
    from brickflow_plugins.airflow import operators
    import importlib
    import inspect

    start_chain = InvalidFieldChecker()
    next_node = start_chain
    pkg = operators
    file_name = pkg.__file__
    for module in os.listdir(os.path.dirname(file_name)):
        # only find python files and ignore __init__.py
        if module == "__init__.py" or module[-3:] != ".py":
            continue
        module_name = module.replace(".py", "")
        # import all the modules into the mod object and not actually import them using __import__
        mod = importlib.import_module(f"{pkg.__name__}.{module_name}")
        for obj in dir(mod):
            module_item = getattr(mod, obj)
            # if issubclass(module_item, OperatorModifier):
            if (
                inspect.isclass(module_item)
                and module_item != operators.OperatorModifier
                and issubclass(module_item, operators.OperatorModifier)
            ):
                # print(module_item)
                next_node = next_node.set_next(module_item())

    next_node.set_next(CatchAllOperatorModifier())
    return start_chain


def check_if(klass):
    def outer(f):
        @functools.wraps(f)
        def inner(*args, **kwargs) -> Optional["BaseOperator"]:
            self, operator = args[0], args[1]
            super_func = getattr(super(type(self), self), f.__name__)
            if not isinstance(operator, klass):
                # super function won't accept self
                # this is to go along the chain
                return super_func(*args[1:], **kwargs)
            return f(*args, **kwargs)

        return inner

    return outer
