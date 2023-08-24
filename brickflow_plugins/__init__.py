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

from brickflow_plugins.airflow.operators.external_tasks import (
    TaskDependencySensor,
    AirflowProxyOktaClusterAuth,
)
from brickflow_plugins.airflow.operators.native_operators import (
    BashOperator,
    BranchPythonOperator,
    ShortCircuitOperator,
)
from brickflow_plugins.databricks.workflow_dependency_sensor import (
    WorkflowDependencySensor,
)


def load_plugins(cache_bust: Optional[pluggy.PluginManager] = None) -> None:
    from brickflow.engine.task import get_plugin_manager
    from brickflow_plugins.airflow.brickflow_task_plugin import (
        AirflowOperatorBrickflowTaskPluginImpl,
    )

    if cache_bust is not None:
        cache_bust.register(
            AirflowOperatorBrickflowTaskPluginImpl(), name="airflow-plugin"
        )
        return

    get_plugin_manager().register(AirflowOperatorBrickflowTaskPluginImpl())


def ensure_installation():
    """Ensures that the brickflow_plugins package is installed in the current environment."""
    from brickflow_plugins.airflow.cronhelper import cron_helper  # noqa
    import airflow  # noqa


__all__: List[str] = [
    "TaskDependencySensor",
    "AirflowProxyOktaClusterAuth",
    "BashOperator",
    "BranchPythonOperator",
    "ShortCircuitOperator",
    "WorkflowDependencySensor",
    "load_plugins",
    "ensure_installation",
]
