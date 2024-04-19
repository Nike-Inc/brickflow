---
search:
  boost: 3
---

## How do I enable airflow features?

!!! warning

    Only certain operators are supported so please make sure you read the documentation before using them. If your operator is not supported 
    please raise a new [issue](https://github.com/Nike-Inc/brickflow/issues/new/choose) in github.

Supported Operators:

* BranchPythonOperator
* PythonOperator
* BashOperator
* ShortCircuitOperator
* TaskDependencySensor

To enable the usage of airflow operators, you need to set the `enable_plugins` flag to `True` in the `Project`
constructor.

## How do I run only one task in a workflow?

Databricks and Airflow use different task scheduling mechanisms. Due to the way airflow manages state in a database, it
is possible to run only one task in a workflow.
Though this works very differently at Databricks as our job scheduler is very different and needs to scale to much large
volume of tasks and workflows.

To provide this capability, brickflow offers a parameter to do this:

1. Go to workflow UI
2. On the top right click the drop down next to `Run Now`
3. Select `Run now with different parameters`
4. Then select switch to legacy parameters
5. Scroll down to: `brickflow_internal_only_run_tasks` and then type the tasks you want to run as a CSV.
6. Please do not modify any other parameter!

## How do I wait for a workflow to finish before kicking off my own workflow's tasks?

```python
from brickflow.context import ctx
from brickflow_plugins import WorkflowDependencySensor

wf = Workflow(...)


@wf.task
def wait_on_workflow(*args):
    api_token_key = ctx.dbutils.secrets.get("brickflow-demo-tobedeleted", "api_token_key")
    sensor = WorkflowDependencySensor(
        databricks_host="https://your_workspace_url.cloud.databricks.com",
        databricks_token=api_token_key,
        dependency_job_id=job_id,
        poke_interval=20,
        timeout=60,
        delta=timedelta(days=1)
    )
    sensor.execute()
```

## How do I wait for a specific task in a workflow to finish before kicking off my own workflow's tasks?

```python
from brickflow.context import ctx
from brickflow_plugins import WorkflowTaskDependencySensor

wf = Workflow(...)


@wf.task
def wait_on_workflow(*args):
    api_token_key = ctx.dbutils.secrets.get("scope", "api_token_key")
    sensor = WorkflowTaskDependencySensor(
        databricks_host="https://your_workspace_url.cloud.databricks.com",
        databricks_token=api_token_key,
        dependency_job_id=job_id,
        dependency_task_name="foo",
        poke_interval=20,
        timeout=60,
        delta=timedelta(days=1)
    )
    sensor.execute()
```

## How do I run a sql query on snowflake from DBX?
```python
from brickflow_plugins import SnowflakeOperator

wf = Workflow(...)

@wf.task
def run_snowflake_queries(*args):
  sf_query_run = SnowflakeOperator(
    secret_scope = "your_databricks secrets scope name",
    query_string = "string of queries separated by semicolon(;)",
    parameters={"key1":"value1", "key2":"value2"}
  )
  sf_query_run.execute()
```

## How do I copy a part/entire data of a UC table to snowflake table?
```python

from brickflow_plugins import UcToSnowflakeOperator

wf = Workflow(...)

@wf.task
def copy_from_uc_sf(*args):
  uc_to_sf_copy = UcToSnowflakeOperator(
    secret_scope = "your_databricks secrets scope name",
    parameters = {'load_type':'incremental','dbx_catalog':'sample_catalog','dbx_database':'sample_schema',
                      'dbx_table':'sf_operator_1', 'sf_schema':'stage','sf_table':'SF_OPERATOR_1',
                      'sf_grantee_roles':'downstream_read_role', 'incremental_filter':"dt='2023-10-22'",
                      'sf_cluster_keys':''}
  )
  uc_to_sf_copy.execute()
```
