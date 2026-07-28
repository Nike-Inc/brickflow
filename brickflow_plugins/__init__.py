import logging
from typing import List, Optional

import pluggy

from brickflow import get_default_log_handler


def setup_logger():
    _log = logging.getLogger(__name__)  # Logger
    _log.setLevel(logging.INFO)
    logger_handler = get_default_log_handler("brickflow-plugins")
    _log.addHandler(logger_handler)
    _log.propagate = False
    return _log


log = setup_logger()

# Native (Airflow-free) sensors and operators. These imports are the public API
# and drive `from brickflow_plugins import <Foo>` for downstream users.
from brickflow_plugins.sensors.airflow_task_dependency_sensor import (
    AirflowCluster,
    AirflowTaskDependencySensor,
)
from brickflow_plugins.sensors.autosys_sensor import AutosysSensor
from brickflow_plugins.sensors.sla_sensor import SLASensor
from brickflow_plugins.sensors.workflow_dependency_sensor import (
    WorkflowDependencySensor,
    WorkflowTaskDependencySensor,
)
from brickflow_plugins.operators.box_operator import (
    BoxOperator,
    BoxToVolumesOperator,
    VolumesToBoxOperator,
)
from brickflow_plugins.operators.tableau_refresh_operator import (
    TableauRefreshDataSourceOperator,
    TableauRefreshWorkBookOperator,
)
from brickflow_plugins.operators.uc_to_snowflake_operator import (
    SnowflakeOperator,
    UcToSnowflakeOperator,
)

# Deprecation stubs. These raise `RuntimeError` on instantiation with a pointer
# to the native replacement. Kept re-exported so `from brickflow_plugins import
# BashOperator` fails loudly at usage rather than silently at import time.
from brickflow_plugins.operators.deprecated_airflow_operators import (
    AirflowProxyOktaClusterAuth,
    BashOperator,
    BranchPythonOperator,
    ShortCircuitOperator,
    TaskDependencySensor,
)


def load_plugins(cache_bust: Optional[pluggy.PluginManager] = None) -> None:
    """
    No-op. Retained so `brickflow.engine.task.get_brickflow_tasks_hook` can
    keep calling it. There is no longer an Airflow-operator handler plugin
    to register, so this is intentionally empty.
    """
    return None


def ensure_installation() -> None:
    """
    No-op. Previously imported ``airflow`` to eagerly fail if the extra
    wasn't installed. Airflow is no longer a dependency of brickflow, so
    this is intentionally empty.
    """
    return None


__all__: List[str] = [
    # Sensors (native)
    "AirflowCluster",
    "AirflowTaskDependencySensor",
    "AutosysSensor",
    "SLASensor",
    "WorkflowDependencySensor",
    "WorkflowTaskDependencySensor",
    # Operators
    "BoxOperator",
    "BoxToVolumesOperator",
    "VolumesToBoxOperator",
    "SnowflakeOperator",
    "UcToSnowflakeOperator",
    "TableauRefreshDataSourceOperator",
    "TableauRefreshWorkBookOperator",
    # Deprecation stubs (raise RuntimeError on instantiation)
    "AirflowProxyOktaClusterAuth",
    "BashOperator",
    "BranchPythonOperator",
    "ShortCircuitOperator",
    "TaskDependencySensor",
    # Plugin machinery (retained for backwards compat)
    "load_plugins",
    "ensure_installation",
]
