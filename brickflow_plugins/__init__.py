import logging
from typing import List

from brickflow import get_default_log_handler


def setup_logger():
    _log = logging.getLogger(__name__)  # Logger
    _log.setLevel(logging.INFO)
    logger_handler = get_default_log_handler("brickflow-plugins")
    _log.addHandler(logger_handler)
    _log.propagate = False
    return _log


log = setup_logger()

from brickflow_plugins.airflow.operators.external_tasks import TaskDependencySensor
from brickflow_plugins.airflow.operators.native_operators import (
    BashOperator,
    BranchPythonOperator,
    ShortCircuitOperator,
)
from brickflow_plugins.databricks.workflow_dependency_sensor import (
    WorkflowDependencySensor,
)

__all__: List[str] = [
    "TaskDependencySensor",
    "BashOperator",
    "BranchPythonOperator",
    "ShortCircuitOperator",
    "WorkflowDependencySensor",
]
