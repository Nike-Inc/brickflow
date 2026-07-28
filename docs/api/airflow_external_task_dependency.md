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
