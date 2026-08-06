---
search:
  boost: 2
---

# Upgrading to the Airflow-free release

This release removes the hard dependency on `apache-airflow`. Users who
never used the Airflow-based plugins can now install `brickflows`
**without** pulling in Airflow (and its transitive dependencies).

## What changed

* `apache-airflow` is no longer a dependency of `brickflows` -- neither
  as a required install nor via an "airflow" extra. It is not attached
  to Databricks clusters by `enable_plugins=True` anymore.
* The `brickflow_plugins.airflow` and `brickflow_plugins.databricks`
  subpackages have been removed. Their contents were rehomed:
    * `brickflow_plugins.sensors` -- `AirflowTaskDependencySensor`,
      `AutosysSensor`, `SLASensor`, `WorkflowDependencySensor`,
      `WorkflowTaskDependencySensor`.
    * `brickflow_plugins.operators` -- `BoxOperator`,
      `BoxToVolumesOperator`, `VolumesToBoxOperator`,
      `RunJobInRemoteWorkspace`, `SnowflakeOperator`,
      `UcToSnowflakeOperator`, `TableauRefreshDataSourceOperator`,
      `TableauRefreshWorkBookOperator`.
* The following classes have been removed. Their names are still
  importable from `brickflow_plugins` so existing code fails loudly at
  the point of use rather than silently at import time:
    * `BashOperator`, `BranchPythonOperator`, `ShortCircuitOperator`
    * `TaskDependencySensor`, `AirflowProxyOktaClusterAuth`
    * `BrickflowSecretsBackend`
* `AirflowTaskDependencySensor` is a **new** native replacement for
  `TaskDependencySensor`. It shares the same wire behavior (polling the
  same Airflow REST endpoints) but requires only `requests` and no
  `apache-airflow`. It routes to `/api/experimental` (Airflow 1.x),
  `/api/v1` (Airflow 2.x), or `/api/v2` (Airflow 3.x) based on the
  `AirflowCluster.version` string — set `version="3.0.0"` to target
  Airflow 3.x, which uses `logical_date` filters in place of
  `execution_date` filters.

## Migration table

| Removed | Replacement |
| --- | --- |
| `BashOperator` | A Databricks notebook that shells out (`%sh`), or `dbutils.notebook.run` a helper notebook. |
| `BranchPythonOperator` | `IfElseConditionTask`. |
| `ShortCircuitOperator` | `IfElseConditionTask`. |
| `TaskDependencySensor` | `AirflowTaskDependencySensor`. |
| `AirflowProxyOktaClusterAuth` | Compute the bearer token yourself and pass it into the plain `AirflowCluster` dataclass. |
| `BrickflowSecretsBackend` | Use `brickflow_plugins.secrets.resolve_secret(url)` directly, or the Cerberus / Base64 helper classes. |

## Example: migrating `TaskDependencySensor`

Before:

```python
from brickflow_plugins import TaskDependencySensor, AirflowProxyOktaClusterAuth

sensor = TaskDependencySensor(
    task_id="sensor",
    timeout=180,
    airflow_cluster_auth=AirflowProxyOktaClusterAuth(
        oauth2_conn_id=f"b64://{data}",
        airflow_cluster_url="https://proxy.../.../cluster_id/",
        airflow_version="2.0.2",
    ),
    external_dag_id="external_airflow_dag",
    external_task_id="hello",
    allowed_states=["success"],
    execution_delta=timedelta(hours=-2),
    poke_interval=60,
)
```

After:

```python
from brickflow_plugins import AirflowCluster, AirflowTaskDependencySensor

sensor = AirflowTaskDependencySensor(
    dag_id="external_airflow_dag",
    task_id="hello",
    cluster=AirflowCluster(
        url="https://proxy.../.../cluster_id/",
        version="2.0.2",
        token=my_bearer_token,
    ),
    allowed_states=["success"],
    execution_delta=timedelta(hours=-2),
    timeout_seconds=180,
    poke_interval=60,
)
sensor.execute()
```

### Migrating URL-based secrets (`b64://` / `cerberus://`)

Before the Airflow-free release, ``AirflowProxyOktaClusterAuth`` accepted
``oauth2_conn_id`` values like ``b64://...`` or ``cerberus://...``. Airflow
resolved those URLs through ``BrickflowSecretsBackend`` at connection lookup
time. That backend is removed — call ``resolve_secret`` yourself and pass the
decoded value into ``AirflowCluster.token``:

```python
import base64
from datetime import timedelta

from brickflow import Workflow, ctx
from brickflow_plugins import AirflowCluster, AirflowTaskDependencySensor
from brickflow_plugins.secrets import resolve_secret

wf = Workflow(...)


@wf.task
def airflow_external_task_dependency_sensor():
    # b64:// — same encoding pattern as the old oauth2_conn_id argument
    encoded = base64.b64encode(
        ctx.dbutils.secrets.get("scope", "okta_conn_id").encode("utf-8")
    ).decode("utf-8")
    token = resolve_secret(f"b64://{encoded}")

    # cerberus:// — requires brickflows[cerberus] on the cluster
    # token = resolve_secret("cerberus://cerberus-host/path/to/secret_key")

    sensor = AirflowTaskDependencySensor(
        dag_id="external_airflow_dag",
        task_id="hello",
        cluster=AirflowCluster(
            url="https://proxy.../.../cluster_id/",
            version="2.0.2",
            token=token,
        ),
        allowed_states=["success"],
        execution_delta=timedelta(hours=-2),
        timeout_seconds=180,
        poke_interval=60,
    )
    sensor.execute()
```

## Import-path updates

If you had imported directly from the removed subpackages, update the
paths:

| Old import path | New import path |
| --- | --- |
| `brickflow_plugins.airflow.operators.external_tasks` | `brickflow_plugins.sensors.airflow_task_dependency_sensor` (and `brickflow_plugins.sensors.autosys_sensor`) |
| `brickflow_plugins.airflow.operators.external_tasks_tableau` | `brickflow_plugins.operators.tableau_refresh_operator` |
| `brickflow_plugins.airflow.cronhelper` | `brickflow_plugins._timing.cronhelper` |
| `brickflow_plugins.databricks.workflow_dependency_sensor` | `brickflow_plugins.sensors.workflow_dependency_sensor` |
| `brickflow_plugins.databricks.sla_sensor` | `brickflow_plugins.sensors.sla_sensor` |
| `brickflow_plugins.databricks.box_operator` | `brickflow_plugins.operators.box_operator` |
| `brickflow_plugins.databricks.uc_to_snowflake_operator` | `brickflow_plugins.operators.uc_to_snowflake_operator` |
| `brickflow_plugins.databricks.run_job` | `brickflow_plugins.operators.run_job` |

Continuing to `from brickflow_plugins import X` for the re-exported
public names (`AirflowTaskDependencySensor`, `AutosysSensor`, `SLASensor`,
`WorkflowDependencySensor`, `BoxOperator`, `SnowflakeOperator`, etc.)
works unchanged.

## Optional install extras

Plugin backends (Snowflake, Tableau, Box, Cerberus) are declared as
optional extras. To install them locally, pick the ones you need:

```
pip install "brickflows[snowflake]"
pip install "brickflows[tableau]"
pip install "brickflows[box]"
pip install "brickflows[cerberus]"
# or, all of them:
pip install "brickflows[all-plugins]"
```

At runtime on a Databricks cluster the individual libraries are attached
via `enable_plugins=True` on your `Project` (or manually via
`PypiTaskLibrary` on your workflow / task).
