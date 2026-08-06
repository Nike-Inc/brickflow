---
search:
  exclude: true
---

# Airflow Task Dependency Sensor

The `AirflowTaskDependencySensor` is a native brickflow sensor that polls a
remote Airflow cluster's REST API to wait for a specific DAG task to reach
an allowed state. It has **no dependency on `apache-airflow`** on the
Databricks side -- it only needs `requests`.

Prior versions shipped a `TaskDependencySensor` and an
`AirflowProxyOktaClusterAuth` class that both subclassed Airflow. Those
classes are still importable from `brickflow_plugins` but now raise
`RuntimeError` on instantiation. Migrate to
`AirflowTaskDependencySensor` and the plain `AirflowCluster` dataclass:

```python
from datetime import timedelta

from brickflow_plugins import AirflowCluster, AirflowTaskDependencySensor

sensor = AirflowTaskDependencySensor(
    dag_id="my_upstream_dag",
    task_id="final_task",
    cluster=AirflowCluster(
        url="https://airflow.example.com",
        version="2.0.2",
        token=my_bearer_token,  # compute this from Okta/etc. yourself
    ),
    allowed_states=["success"],
    execution_delta=timedelta(hours=0),
    timeout_seconds=3600,
    poke_interval=60,
)
sensor.execute()
```

## Supported Airflow versions

The sensor auto-routes to the correct REST API dialect based on the
`AirflowCluster.version` string:

| `version` starts with | Endpoint prefix | Notes |
|---|---|---|
| `"1."` | `/api/experimental` | Airflow 1.x |
| any other value (default) | `/api/v1` | Airflow 2.x |
| `"3."` | `/api/v2` | Airflow 3.x (FastAPI). Uses `logical_date_gte` in place of `execution_date_gte`, and drops asset-triggered runs that have `logical_date=null`. |

### Airflow 3.x example

```python
from datetime import timedelta

from brickflow_plugins import AirflowCluster, AirflowTaskDependencySensor

sensor = AirflowTaskDependencySensor(
    dag_id="my_upstream_dag",
    task_id="final_task",
    cluster=AirflowCluster(
        url="https://airflow.example.com",
        version="3.0.0",
        token=my_jwt,  # short-lived JWT from Okta/MAP or POST /auth/token
    ),
    allowed_states=["success"],
    execution_delta=timedelta(hours=0),
    timeout_seconds=3600,
    poke_interval=60,
)
sensor.execute()
```

Auth is unchanged: bring your own bearer token in `cluster.token`. The sensor
does not call `/auth/token` for you.

## API Reference

::: brickflow_plugins.sensors.airflow_task_dependency_sensor
    handler: python
    options:
        members:
            - AirflowCluster
            - AirflowTaskDependencySensor
        filters:
            - "!^_[^_]"
            - "!^__[^__]"

## Autosys Sensor

::: brickflow_plugins.sensors.autosys_sensor
    handler: python
    options:
        members:
            - AutosysSensor
        filters:
            - "!^_[^_]"
            - "!^__[^__]"
