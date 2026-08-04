import importlib
import logging
from typing import TYPE_CHECKING, Any, List, Optional

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


# Deprecation stubs. These raise `RuntimeError` on instantiation with a pointer
# to the native replacement. Kept as eager imports because they have no
# third-party dependencies and are cheap to load.
from brickflow_plugins.operators.deprecated_airflow_operators import (
    AirflowProxyOktaClusterAuth,
    BashOperator,
    BranchPythonOperator,
    BrickflowSecretsBackend,
    ShortCircuitOperator,
    TaskDependencySensor,
)


# Native (Airflow-free) sensors and operators. Each entry maps a public
# attribute name to the submodule that defines it. Modules are imported
# lazily via ``__getattr__`` below, so users only pay the import cost --
# and the optional third-party dependency cost -- for operators they
# actually access. E.g. importing ``WorkflowDependencySensor`` does NOT
# trigger loading of ``box_operator`` (and therefore does not require
# ``boxsdk`` to be installed).
_LAZY_ATTRS: dict[str, str] = {
    # Sensors (native)
    "AirflowCluster": "brickflow_plugins.sensors.airflow_task_dependency_sensor",
    "AirflowTaskDependencySensor": "brickflow_plugins.sensors.airflow_task_dependency_sensor",
    "AutosysSensor": "brickflow_plugins.sensors.autosys_sensor",
    "SLASensor": "brickflow_plugins.sensors.sla_sensor",
    "WorkflowDependencySensor": "brickflow_plugins.sensors.workflow_dependency_sensor",
    "WorkflowTaskDependencySensor": "brickflow_plugins.sensors.workflow_dependency_sensor",
    # Operators -- each has its own optional third-party dependency that is
    # only required when the operator is actually instantiated.
    "BoxOperator": "brickflow_plugins.operators.box_operator",  # requires: boxsdk
    "BoxToVolumesOperator": "brickflow_plugins.operators.box_operator",  # requires: boxsdk
    "VolumesToBoxOperator": "brickflow_plugins.operators.box_operator",  # requires: boxsdk
    "SnowflakeOperator": "brickflow_plugins.operators.uc_to_snowflake_operator",  # requires: snowflake
    "UcToSnowflakeOperator": "brickflow_plugins.operators.uc_to_snowflake_operator",  # requires: snowflake
    "TableauRefreshDataSourceOperator": "brickflow_plugins.operators.tableau_refresh_operator",  # requires: tableauserverclient
    "TableauRefreshWorkBookOperator": "brickflow_plugins.operators.tableau_refresh_operator",  # requires: tableauserverclient
}


if TYPE_CHECKING:
    # Make static type checkers (mypy, pyright, IDE autocomplete) happy by
    # re-exporting the lazily-loaded names. These imports never run at runtime.
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
        AirflowCluster,
        AirflowTaskDependencySensor,
    )
    from brickflow_plugins.sensors.autosys_sensor import AutosysSensor
    from brickflow_plugins.sensors.sla_sensor import SLASensor
    from brickflow_plugins.sensors.workflow_dependency_sensor import (
        WorkflowDependencySensor,
        WorkflowTaskDependencySensor,
    )


def __getattr__(name: str) -> Any:
    """PEP 562 module ``__getattr__`` for lazy plugin loading.

    Resolves ``from brickflow_plugins import <name>`` by importing the
    corresponding submodule only when ``<name>`` is first accessed. Results
    are cached in module globals so subsequent lookups are O(1) and skip
    the import machinery entirely.
    """
    module_path = _LAZY_ATTRS.get(name)
    if module_path is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = importlib.import_module(module_path)
    attr = getattr(module, name)
    globals()[name] = attr  # cache for subsequent lookups
    return attr


def __dir__() -> List[str]:
    """Include lazy attributes in ``dir(brickflow_plugins)`` output."""
    return sorted(set(list(globals().keys()) + list(_LAZY_ATTRS.keys())))


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
    "BrickflowSecretsBackend",
    "ShortCircuitOperator",
    "TaskDependencySensor",
    # Plugin machinery (retained for backwards compat)
    "load_plugins",
    "ensure_installation",
]
