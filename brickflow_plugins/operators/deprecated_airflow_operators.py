"""
Deprecation stubs for airflow-based operators that were part of brickflow
prior to the removal of the ``apache-airflow`` dependency.

These stubs exist purely to give a clear migration message; instantiating
them raises :class:`RuntimeError` with a pointer to the native replacement.
"""


class _RemovedAirflowOperator:
    """Base marker class for operators that used to subclass an Airflow operator."""

    _replacement: str = "a native Databricks task"
    _docs_url: str = "https://engineering.nike.com/brickflow/main/tasks/"

    def __init__(self, *args, **kwargs) -> None:
        raise RuntimeError(
            f"{type(self).__name__} is deprecated and no longer supported after "
            "brickflow removed its apache-airflow dependency. Please use "
            f"{self._replacement}. Ref: {self._docs_url}"
        )


class BashOperator(_RemovedAirflowOperator):
    """
    Deprecated: use ``dbutils.notebook.run`` for shell commands, or run a
    native Databricks task with ``brickflow.RunJobTask`` and invoke your
    shell script from within a notebook cell.
    """

    _replacement = "a native Databricks notebook/task that shells out via dbutils"
    _docs_url = "https://engineering.nike.com/brickflow/main/tasks/"


class BranchPythonOperator(_RemovedAirflowOperator):
    """
    Deprecated: use ``IfElseConditionTask`` for conditional task execution.
    """

    _replacement = "IfElseConditionTask"
    _docs_url = "https://engineering.nike.com/brickflow/main/tasks/?h=if#ifelse-task"


class ShortCircuitOperator(_RemovedAirflowOperator):
    """
    Deprecated: use ``IfElseConditionTask`` to short-circuit downstream tasks.
    """

    _replacement = "IfElseConditionTask"
    _docs_url = "https://engineering.nike.com/brickflow/main/tasks/?h=if#ifelse-task"


class AirflowProxyOktaClusterAuth(_RemovedAirflowOperator):
    """
    Deprecated: replaced by the plain ``AirflowCluster`` dataclass in
    ``brickflow_plugins.sensors.airflow_task_dependency_sensor``. Compute
    the token yourself (from Okta or another IdP) and pass it in directly.
    """

    _replacement = (
        "brickflow_plugins.sensors.airflow_task_dependency_sensor.AirflowCluster "
        "with a pre-computed bearer token"
    )
    _docs_url = "https://engineering.nike.com/brickflow/main/tasks/"


class TaskDependencySensor(_RemovedAirflowOperator):
    """
    Deprecated: replaced by
    ``brickflow_plugins.sensors.airflow_task_dependency_sensor.AirflowTaskDependencySensor``.
    """

    _replacement = "brickflow_plugins.sensors.airflow_task_dependency_sensor.AirflowTaskDependencySensor"
    _docs_url = "https://engineering.nike.com/brickflow/main/tasks/"


class BrickflowSecretsBackend(_RemovedAirflowOperator):
    """
    Deprecated: replaced by ``brickflow_plugins.secrets.resolve_secret(url)`` or
    the Cerberus / Base64 helper classes.
    """

    _replacement = (
        "brickflow_plugins.secrets.resolve_secret(url), CerberusSecretsHelper, "
        "or B64SecretsHelper"
    )
    _docs_url = (
        "https://engineering.nike.com/brickflow/main/upgrades/upgrade-airflow-free/"
    )
