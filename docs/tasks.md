A task in Databricks workflows refers to a single unit of work that is executed as part of a larger data processing 
pipeline. Tasks are typically designed to perform a specific set of operations on data, such as loading data from a 
source, transforming the data, and storing it in a destination. In brickflow, tasks as designed in such a way that 

Assuming, that this is already read - [workflow](workflows.md) and workflow object is created

### Task

Databricks workflow task can be created by decorating a python function with brickflow's task function

```python title="task"
from brickflow import Workflow
wf = Workflow(...)

@wf.task  # (1)!
def start():
    pass

@wf.task(name="custom_end")  # (2)!
def end():
    pass
```

1. Create a task using a decorator pattern. The task name would default to the python function name. So a task will be 
    created with the name "start"
2. Creating a task and defining the task name explicitly instead of using the function name "end". The task will be
   created with the new name "custom_end"

### Task dependency

Define task dependency by using a variable "depends_on" in the task function. You can provide the dependent tasks as
direct python callables or string or list of callables/strings

```python title="task_dependency"
from brickflow import Workflow
wf = Workflow(...)

@wf.task
def start():
    pass

@wf.task(depends_on=start)  # (1)!
def bronze_layer():
    pass

@wf.task(depends_on="bronze_layer")  # (2)!
def x_silver():
    pass

@wf.task(depends_on=bronze_layer)
def y_silver():
    pass

@wf.task(depends_on=[x_silver, y_silver])  # (3)!
def xy_gold():
    pass

@wf.task(name="custom_z_gold", depends_on=[x_silver, "y_silver"])  # (4)!
def z_gold():
    pass

@wf.task(depends_on=["xy_gold", "custom_z_gold"])  # (5)!
def end():
    pass
```

1. Create dependency on task "start" and it is passed as callable
2. Create dependency on task "bronze_layer" and it is passed as a string
3. Create dependency on multiple tasks using list and the tasks are callables
4. Create dependency on multiple tasks using list but one task is a callable and another is a string
5. Create dependency on multiple tasks using list and tasks are passed as string. "custom_z_gold" is the task name that
   is explicitly defined - should not use "z_gold" which is a function name

### Task parameters

Task parameters can be defined as key value pairs in the function definition on which task is defined

```python title="task_parameters"
from brickflow import Workflow
wf = Workflow(...)

@wf.task
def task_function(*, test="var", test1="var1"):  # (1)!
    print(test)
    print(test1)
```

1. To pass the task specific parameters, need to start with "*" and then key value pairs start

### Common task parameters

In the [workflows](workflows.md#common-task-parameters) section, we saw how the common task parameters are created at 
the workflow level. Now in this section, we shall see how to use the common task parameters

```python title="use_common_task_parameters"
from brickflow import Workflow, ctx
wf = Workflow(...)

@wf.task
def common_params():
    import some_pyspark_function  # (1)!

    catalog_env = ctx.get_parameter(key="catalog", debug="local")  # (2)!
    some_pyspark_function(catalog_env)  # (3)!
```

1. It is recommended to use localized imports in tasks rather than the global imports
2. Brickflow provides the context using which we can fetch the task parameters that are defined. Providing debug is
   mandatory or else there will be a compilation error while deploying
3. The extracted task_parameter_value can be used as any python variable. In this example, we are just passing the
   variable to "some_pyspark_function"

### Inbuilt task parameters

There are many inbuilt task parameters that be accessed using brickflow context like above

```python title="inbuilt_task_parameters"
from brickflow import Workflow, ctx
wf = Workflow(...)

@wf.task
def inbuilt_params():
   print(ctx.get_parameter(
        key="brickflow_env",  # (1)! 
        debug="local"))
   print(ctx.get_parameter(
        key="brickflow_run_id",  # (2)! 
        debug="788868"))
   print(ctx.get_parameter(
        key="brickflow_job_id",  # (3)! 
        debug="987987987987987"))
   print(ctx.get_parameter(
        key="brickflow_start_date",  # (4)! 
        debug="2023-05-03"))
   print(ctx.get_parameter(
        key="brickflow_start_time",  # (5)! 
        debug="1683102411626"))
   print(ctx.get_parameter(
        key="brickflow_task_retry_count",  # (6)! 
        debug="2"))
   print(ctx.get_parameter(
        key="brickflow_parent_run_id",  # (7)! 
        debug="788869"))
   print(ctx.get_parameter(
        key="brickflow_task_key",  # (8)! 
        debug="inbuilt_params"))
   print(ctx.get_parameter(
        key="brickflow_internal_workflow_name",  # (9)! 
        debug="Sample_Workflow"))
   print(ctx.get_parameter(
        key="brickflow_internal_task_name",  # (10)! 
        debug="inbuilt_params"))
   print(ctx.get_parameter(
        key="brickflow_internal_workflow_prefix",  # (11)! 
        debug="inbuilt_params"))
   print(ctx.get_parameter(
        key="brickflow_internal_workflow_suffix",  # (12)! 
        debug="inbuilt_params"))
```

1. "brickflow_env" holds the value of the --env variable which was used when brickflow is deployed
2. "brickflow_run_id" holds the value of the current task run id
3. "brickflow_job_id" holds the value of the current workflow job id
4. "brickflow_start_date" holds the value of the current workflow start date
5. "brickflow_start_time" holds the value of the current task start time
6. "brickflow_task_retry_count" holds the value of number of retries a task can run, when a failure occurs
7. "brickflow_parent_run_id" hold the value of the current workflow run_id
8. "brickflow_task_key" holds the value of the current task name
9. "brickflow_internal_workflow_name" holds the value of the current workflow name
10. "brickflow_internal_task_name" holds the value of the current task name
11. "brickflow_internal_workflow_prefix" holds the value of the prefix used for the current workflow name
12. "brickflow_internal_workflow_suffix" holds the value of the suffix used for the current workflow name


### Clusters

There is a flexibility to use different clusters for each task or assign custom clusters

```python title="clusters"
from brickflow import Workflow, Cluster
wf = Workflow(...)

@wf.task(cluster=Cluster(...))  # (1)!
def custom_cluster():
    pass
```

1. You will be able to create a job cluster or use existing cluster. Refer to this [section](workflows.md#clusters) in 
   the workflows to understand how to implement

### Libraries

There is a flexibility to use specific libraries for a particular task

```python title="libraries"
from brickflow import Workflow
wf = Workflow(...)

@wf.task(libraries=[...])  # (1)!
def custom_libraries():
    pass
```

1. You will be able to install libraries that are specific to a task. Refer to this [section](workflows.md#libraries) in
   the workflows to understand how to implement


### Task types

There are different task types that are supported by brickflow right now. The default task type that is used by 
brickflow is NOTEBOOK


```python title="task_types"
from brickflow import Workflow, TaskType, BrickflowTriggerRule, TaskResponse
wf = Workflow(...)

@wf.task
def notebook_task():
   pass

@wf.task(task_type=TaskType.DLT)
def dlt_task():
    pass
```

1. Provide the task type that is to be used for this task. Default is a notebook task
2. Trigger rule can be attached. It can be ALL_SUCCESS or NONE_FAILED. In this case, this task will be triggered, if all
   the upstream tasks are at-least run and completed.


### Trigger rules

There are two types of trigger rules that can be applied on a task. It can be either ALL_SUCCESS or NONE_FAILED

```python title="task_types"
from brickflow import Workflow, BrickflowTriggerRule
wf = Workflow(...)

@wf.task(
   trigger_rule=BrickflowTriggerRule.NONE_FAILED  # (1)!
)
def none_failed_task():
   pass

@wf.task(
   trigger_rule=BrickflowTriggerRule.ALL_SUCCESS  # (2)!
)
def all_success_task():
   pass
```

1. NONE_FAILED - use this if you want to trigger the task irrespective of the upstream tasks success or failure state
2. ALL_SUCCESS - use this if you want to trigger the task only if all the upstream tasks are all having success state


### Tasks conditional run

Adding condition for task running based on result of parent tasks

```python title="task_conditional_run"
from brickflow import Workflow, TaskRunCondition, TaskSettings
wf = Workflow(...)

@wf.task(
   task_settings=TaskSettings(run_if=TaskRunCondition.AT_LEAST_ONE_FAILED)
)
def none_failed_task():
   pass
```

This option is determining whether the task is run once its dependencies have been completed. Available options:
1. `ALL_SUCCESS`: All dependencies have executed and succeeded
2. `AT_LEAST_ONE_SUCCESS`: At least one dependency has succeeded
3. `NONE_FAILED`: None of the dependencies have failed and at least one was executed
4. `ALL_DONE`: All dependencies completed and at least one was executed
5. `AT_LEAST_ONE_FAILED`: At least one dependency failed
6. `ALL_FAILED`: ALl dependencies have failed

### Airflow Operators

We have adopted/extended certain airflow operators that might be needed to run as a task in databricks workflows.
Typically for airflow operators we return the operator and brickflow will execute the operator based on task return
type.

#### Bash Operator

You will be able to use bash operator as below

```python title="bash_operator"
from brickflow import Workflow
from brickflow_plugins import BashOperator
wf = Workflow(...)

@wf.task
def bash_task():
    return BashOperator(task_id=bash_task.__name__, 
                        bash_command="ls -ltr")  # (1)!
```

1. Use Bashoperator like how we use in airflow but it has to be returned from task function


#### Task Dependency Sensor

Even if you migrate to databricks workflows, brickflow gives you the flexibility to have a dependency on the airflow job

```python title="task_dependency_sensor"
from brickflow import Workflow, ctx
from brickflow_plugins import TaskDependencySensor, AirflowProxyOktaClusterAuth

wf = Workflow(...)


@wf.task
def airflow_external_task_dependency_sensor():
   import base64
   from datetime import timedelta
   data = base64.b64encode(
      ctx.dbutils.secrets.get("brickflow-demo-tobedeleted", "okta_conn_id").encode(
         "utf-8"
      )
   ).decode("utf-8")
   return TaskDependencySensor(
      task_id="sensor",
      timeout=180,
      airflow_cluster_auth=AirflowProxyOktaClusterAuth(
         oauth2_conn_id=f"b64://{data}",
         airflow_cluster_url="https://proxy.../.../cluster_id/",
         airflow_version="2.0.2", # if you are using airflow 1.x please make sure this is the right value, the apis are different between them!
      ),
      external_dag_id="external_airlfow_dag",
      external_task_id="hello",
      allowed_states=["success"],
      execution_delta=timedelta(hours=-2),
      execution_delta_json=None,
      poke_interval= 60,
   )
```

#### Autosys Sensor

This operator calls an Autosys API and is used to place a dependency on Autosys jobs, when necessary.

```python title="autosys_sensor"
from brickflow import Workflow, ctx
from brickflow_plugins import AutosysSensor, AirflowProxyOktaClusterAuth

wf = Workflow(...)


@wf.task
def airflow_autosys_sensor():
   import base64

   data = base64.b64encode(
      ctx.dbutils.secrets.get("brickflow-demo-tobedeleted", "okta_conn_id").encode(
         "utf-8"
      )
   ).decode("utf-8")
   return AutosysSensor(
      task_id="sensor",
      url="https://autosys.../.../api/",
      airflow_cluster_auth=AirflowProxyOktaClusterAuth(
         oauth2_conn_id=f"b64://{data}",
         airflow_cluster_url="https://autosys.../.../api/",
         airflow_version="2.0.2", 
      ),
      poke_interval=200,
      job_name="hello",
      time_delta={"days": 0},
   )
```

#### Workflow Dependency Sensor

Wait for a workflow to finish before kicking off the current workflow's tasks

```python title="workflow_dependency_sensor"
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

#### Workflow Task Dependency Sensor

Wait for a specific task in a workflow to finish before kicking off the current workflow's tasks

```python title="workflow_dependency_sensor"
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

#### Snowflake Operator

run snowflake queries from the databricks environment 

As databricks secrets is a key value store, code expects the secret scope to contain the below exact keys   
&emsp;&emsp;&emsp;&emsp;username : user id created for connecting to snowflake for ex: sample_user  
&emsp;&emsp;&emsp;&emsp;password : password information for about user for ex: P@$$word  
&emsp;&emsp;&emsp;&emsp;account  : snowflake account information, not entire url for ex: sample_enterprise  
&emsp;&emsp;&emsp;&emsp;warehouse: warehouse/cluster information that user has access for ex: sample_warehouse  
&emsp;&emsp;&emsp;&emsp;database : default database that we want to connect for ex: sample_database  
&emsp;&emsp;&emsp;&emsp;role     : role to which the user has write access for ex: sample_write_role

SnowflakeOperator can accept the following as inputs 
&emsp;&emsp;&emsp;&emsp;secret_scope (required): databricks secret scope identifier
&emsp;&emsp;&emsp;&emsp;query_string (required): queries separated by semicolon
&emsp;&emsp;&emsp;&emsp;parameters (optional) : dictionary with variables that can be used to substitute in queries

```python title="snowflake_operator"
from brickflow_plugins import SnowflakeOperator

wf = Workflow(...)

@wf.task
def run_snowflake_queries(*args):
  sf_query_run = SnowflakeOperator(
    secret_scope = "your_databricks secrets scope name",
    query_string ="select * from database.$schema.$table where $filter_condition1; select * from sample_schema.test_table",
    parameters = {"schema":"test_schema","table":"sample_table","filter_condition":"col='something'"}
  )
  sf_query_run.execute()
```


#### UC to Snowflake Operator

copy data from databricks to snowflake 

As databricks secrets is a key value store, code expects the secret scope to contain the below exact keys   
&emsp;&emsp;&emsp;&emsp;username : user id created for connecting to snowflake for ex: sample_user  
&emsp;&emsp;&emsp;&emsp;password : password information for about user for ex: P@$$word  
&emsp;&emsp;&emsp;&emsp;account  : snowflake account information, not entire url for ex: sample_enterprise  
&emsp;&emsp;&emsp;&emsp;warehouse: warehouse/cluster information that user has access for ex: sample_warehouse  
&emsp;&emsp;&emsp;&emsp;database : default database that we want to connect for ex: sample_database  
&emsp;&emsp;&emsp;&emsp;role     : role to which the user has write access for ex: sample_write_role

UcToSnowflakeOperator can expects the following as inputs to copy data in parameters  
&emsp;&emsp;&emsp;&emsp;load_type (required): type of data load , acceptable values full or incremental
&emsp;&emsp;&emsp;&emsp;dbx_catalog (required) : name of the databricks catalog in which object resides 
&emsp;&emsp;&emsp;&emsp;dbx_database (required): name of the databricks schema in which object is available
&emsp;&emsp;&emsp;&emsp;dbx_table (required) : name of the databricks object we want to copy to snowflake 
&emsp;&emsp;&emsp;&emsp;sf_database (optional) : name of the snowflake database if different from the one in secret_scope 
&emsp;&emsp;&emsp;&emsp;sf_schema (required): name of the snowflake schema in which we want to copy the data 
&emsp;&emsp;&emsp;&emsp;sf_table (required) : name of the snowflake object to which we want to copy from databricks
&emsp;&emsp;&emsp;&emsp;incremental_filter (required for incrmental mode) :  condition to manage data before writing to snowflake
&emsp;&emsp;&emsp;&emsp;dbx_data_filter (optional): filter condition on databricks source for full or incremental (if different from inremental_filter)
&emsp;&emsp;&emsp;&emsp;sf_grantee_roles (optional) : snowflake roles to which we want to grant select/read access 
&emsp;&emsp;&emsp;&emsp;sf_cluster_keys (optional) : list of keys we want to cluster our snowflake table. 

```python title="uc_to_snowflake_operator"
from brickflow_plugins import UcToSnowflakeOperator

wf = Workflow(...)

@wf.task
def run_snowflake_queries(*args):
  uc_to_sf_copy = UcToSnowflakeOperator(
    secret_scope = "your_databricks secrets scope name",
    parameters = {'load_type':'incremental','dbx_catalog':'sample_catalog','dbx_database':'sample_schema',
                      'dbx_table':'sf_operator_1', 'sf_schema':'stage','sf_table':'SF_OPERATOR_1',
                      'sf_grantee_roles':'downstream_read_role', 'incremental_filter':"dt='2023-10-22'",
                      'sf_cluster_keys':''}
  )
  uc_to_sf_copy.execute()
```

#### Tableau Refresh Operators
Connect to the Tableau server and trigger the refresh of the data sources or workbooks.

Tableau client uses object GUIDs  to identify objects on the server. At the same time the server does not
enforce unique names for the objects across the server. This means that multiple objects, e.g. data sources, with the 
same name can exist on the server. 

To overcome this, operators are using the combination of `project` and `parent_project` parameters to uniquely
identify the project that owns data source or workbook on the server. Successfull project resolution will be indicated
in the logs as follows:
```
INFO - Querying all projects on site

Parent project identified:
	Name: My Parent Project
	ID: 2e14e111-036f-409e-b536-fb515ee534b9
Working project identified:
	Name: My Project
	ID: 2426e01f-c145-43fc-a7f6-1a7488aceec0
```
If project resolution is successful the refresh will be triggered and operator will poll the server for the refresh 
status:
```
Triggering refresh of 'my-datasource' datasource...
Query for information about job c3263ad0-1340-444d-8128-24ad742a943a
Data source 'my-datasource' refresh status: 
   { 
      'job_id': 'c3263ad0-1340-444d-8128-24ad742a943a', 
      'job_status': 'Success', 
      'finish_code': 0, 
      'started_at': '2024-02-05 20:36:03 UTC', 
      'completed_at': '2024-02-05 20:41:32 UTC', 
      'job_status_details': None
   }!
```
If refresh fails, `job_status_details` will contain the error message retrieved from the server and the operator will
fail. If fail behavior is not desired, `fail_operator = False` can be set in the operator parameters.

```python title="tableau_refresh_operators"
from brickflow.context import ctx
from brickflow_plugins import TableauRefreshDataSourceOperator, TableauRefreshWorkBookOperator

wf = Workflow(...)


@wf.task
def tableau_refresh_datasource():
    return TableauRefreshDataSourceOperator(
        server="https://my-tableau.com",
        username="foo",
        password="bar",
        site="site",
        project="project",
        data_sources=["datasource1", "datasource2"],
    )


@wf.task
def tableau_refresh_workbook():
    return TableauRefreshWorkBookOperator(
        server="https://my-tableau.com",
        username="foo",
        password="bar",
        site="site",
        project="project",
        workbooks=["workbook1", "workbook2"],
    )
```
Check operator logs for more details on the status of the connection and the refresh.