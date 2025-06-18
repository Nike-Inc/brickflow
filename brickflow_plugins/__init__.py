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

from brickflow_plugins.airflow.operators.native_operators import (
    # BashOperator,
    BranchPythonOperator,
    ShortCircuitOperator,
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
from brickflow_plugins.sensors.airflow_task_dependency_sensor import (
    AirflowTaskDependencySensor,
)
from brickflow_plugins.sensors.autosys_sensor import AutosysSensor
from brickflow_plugins.sensors.sla_sensor import SLASensor
from brickflow_plugins.sensors.workflow_dependency_sensor import (
    WorkflowDependencySensor,
    WorkflowTaskDependencySensor,
)


def load_plugins(cache_bust: Optional[pluggy.PluginManager] = None) -> None:
    from brickflow.engine.task import get_plugin_manager

    # TODO: takeout dependency installation and plugin flags (or discuss if needed)
    # TODO: cleanup pyproject.toml
    # TODO: Determine if plugin for operators is actually needed
    # from brickflow_plugins.airflow.brickflow_task_plugin import (
    #     AirflowOperatorBrickflowTaskPluginImpl,
    # )

    # if cache_bust is not None:
    #     cache_bust.register(
    #         AirflowOperatorBrickflowTaskPluginImpl(), name="airflow-plugin"
    #     )
    #     return

    # get_plugin_manager().register(AirflowOperatorBrickflowTaskPluginImpl())


def ensure_installation():
    """Ensures that the brickflow_plugins package is installed in the current environment."""
    from brickflow_plugins.airflow.cronhelper import cron_helper  # noqa
    import airflow  # noqa


__all__: List[str] = [
    "AirflowTaskDependencySensor",
    "AutosysSensor",
    # "BashOperator",
    "BranchPythonOperator",
    "ShortCircuitOperator",
    "WorkflowDependencySensor",
    "WorkflowTaskDependencySensor",
    "SnowflakeOperator",
    "UcToSnowflakeOperator",
    "TableauRefreshDataSourceOperator",
    "TableauRefreshWorkBookOperator",
    "BoxToVolumesOperator",
    "VolumesToBoxOperator",
    "BoxOperator",
    "SLASensor",
    # "load_plugins",
    "ensure_installation",
]
