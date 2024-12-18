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

#### Notebook Task

The `Notebook Task` is used as a decorator in conjunction with the `notebook_task` method of a `Workflow` instance. This method registers the task within the workflow.

Here's an example of how to use the `Notebook` Task type:

```python
@wf.task
def notebook_task():
   pass

@wf.notebook_task
# this task runs a databricks notebook
def example_notebook():
    return NotebookTask(
        notebook_path="notebooks/example_notebook.py",
        base_parameters={
            "some_parameter": "some_value",  # in the notebook access these via dbutils.widgets.get("some_parameter")
        },
    )

```

NotebookTask class can accept the following as inputs:<br />
&emsp;<b>base_parameters: Optional[Dict[str, str]]</b> = parameters to pass to notebook and can be accessed through dbutils widgets<br>
   &emsp; <b>notebook_path</b>:'The path of the notebook to be run in the Databricks workspace or remote repository.For notebooks stored in the Databricks workspace, the path must be absolute and begin with a slash.<br>For notebooks stored in a remote repository, the path must be relative.,
    <br>
  &emsp;  <b>source: Optional[str]</b> :'Optional location type of the Python file. When set to `WORKSPACE` or not specified, the file will be retrieved from the local <Databricks> workspace or cloud location (if the `python_file` has a URI format). When set to `GIT`,the Python file will be retrieved from a Git repository defined in `git_source`.*`WORKSPACE`: The Python file is located in a <Databricks> workspace or at a cloud filesystem URI.* `GIT`: The Python file is located in a remote Git repository.',

#### Run Job Task

The `Run Job Task` is used as a decorator in conjunction with the `run_job_task` method of a `Workflow` instance. This method registers the task within the workflow.

Here's an example of how to use the `Run Job` Task type:

```python
from brickflow import RunJobTask

@wf.run_job_task
def run_job_task_a():
    return RunJobTask(job_name="run_job_task")

# we can also pass task type as parameter
@wf.task(task_type=TaskType.RUN_JOB_TASK)
def run_job_task_a():
    return RunJobTask(job_name="run_job_task")
```

RunJobTask class can accept the following as inputs:<br />

&emsp;<b>job_name</b>: The name of the job (case-insensitive).<br />
&emsp;<b>host [Optional]</b>: The URL of the Databricks workspace.<br />
&emsp;<b>token [Optional]</b>: The Databricks API token.

!!! important

    Databricks does not natively support triggering the job run in the remote workspace. Only set `host` and `token`
    parameters when remote trigger is required, it will envoke RunJobInRemoteWorkspace plugin which will transparently 
    substitute the native execution. No extra action will be required from the user.

#### JAR Task

The `JAR Task` is used as a decorator in conjunction with the `spark_jar_task` method of a `Workflow` instance. This method registers the task within the workflow.<br>
Make sure to upload `JAR` file into `dbfs` (or) `S3` paths and provide relative path of the uploaded jar.<br>
Here's an example of how to use the `JAR` Task type:

```python
# Example:1
@wf.spark_jar_task(
    libraries=[
        JarTaskLibrary(
            jar="dbfs:/Volumes/development/global_sustainability_dev/raju_spark_jar_test/PrintArgs.jar"
        )
    ]
)
def spark_jar_task_a():
    return SparkJarTask(
        main_class_name="PrintArgs",
        parameters=["Hello", "World!"],
    ) 
# Example: 2
@wf.spark_jar_task(
    libraries=[
        JarTaskLibrary(
            jar="s3:/Volumes/development/global_sustainability_dev/raju_spark_jar_test/PrintArgs.jar"
        )
    ]
)
def spark_jar_task_test():
    return SparkJarTask(
        main_class_name="PrintArgs",
    )
# Example: 3
# we can also pass task type as parameter
@wf.task(task_type=TaskType.SPARK_JAR_TASK, libraries=[
        JarTaskLibrary(
            jar="dbfs:/Volumes/development/global_sustainability_dev/raju_spark_jar_test/PrintArgs.jar"
        )])
def run_job_task_a():
    return SparkJarTask(main_class_name="MainClass")
```

JarTask class can accept the following as inputs:<br />

&emsp;<b>main_class_name</b>: The full name of the class containing the main method to be executed.<br />
&emsp;<b>parameters [Optional]</b>: Parameters passed to the main method.

#### PYTHON Task

The `PYTHON Task` is used as a decorator in conjunction with the `spark_python_task` method of a `Workflow` instance. This method registers the task within the workflow.<br>
Make sure to provide correct path to  `PYTHON` file from workspace or relative path from git repo.<br>
Here's an example of how to use the `PYTHON` Task type:

```python
# Example:1
@wf.spark_python_task(
        libraries=[
            PypiTaskLibrary(
                package="koheesio"
            )
        ]
    )
def spark_python_task_a():
    return SparkPythonTask(
        python_file="path/to/python/file.py",
        source="GIT",
        parameters=["--param1", "World!"],
    )
# Example: 2
# we can also pass task type as parameter
@wf.task(task_type=TaskType.SPARK_PYTHON_TASK, libraries=[
            PypiTaskLibrary(
                package="koheesio"
            )
        ]
def run_job_task_a():
    return SparkPythonTask(
        python_file="path/to/python/file.py",
        source="GIT",
        parameters=["--param1", "World!"],
    )
```

PythonTask class can accept the following as inputs:<br />

&emsp;<b>python_file</b>:
The Python file to be executed. Cloud file URIs (such as dbfs:/, s3:/, adls:/, gcs:/) and workspace paths are supported. For python files stored in the Databricks workspace, the path must be absolute and begin with `/`. For files stored in a remote repository, the path must be relative. This field is required.'
<br />
&emsp;<b>source</b>: When set to `WORKSPACE` or not specified, the file will be retrieved from the local Databricks workspace or cloud location (if the `python_file` has a URI format). When set to `GIT`,\nthe Python file will be retrieved from a Git repository defined in `git_source`.\n\n* `WORKSPACE`: The Python file is located in a Databricks workspace or at a cloud filesystem URI.\n* `GIT`: The Python file is located in a remote Git repository..<br />
&emsp;<b>parameters [Optional]</b>: Parameters passed to the main method.

#### SQL Task

The SqlTask class is used to create SQL tasks in the workflow. It can be used to create tasks with a query ID, file path, alert ID, and dashboard ID.<br>
The `SQL Task` is used as a decorator in conjunction with the `sql_task` method of a `Workflow` instance.
This method registers the task within the workflow.

SQLTask class can accept the following as inputs:<br />
&emsp; <b>query_id[Optional]</b>: A string representing the ID of the query.<br>
&emsp; <b>file_path[Optional]</b>: A string representing the path to the SQL file.<br>
&emsp; <b>alert_id[Optional]</b>: A string representing the ID of the alert.<br>
&emsp; <b>pause_subscriptions[Optional]</b>: A boolean indicating whether to pause subscriptions or not.<br>
&emsp; <b>subscriptions[Optional]</b>:<span class="nowrap"> A dictionary containing usernames and destination IDs for subscriptions.</span><br>
&emsp; <b>dashboard_id[Optional]</b>: A string representing the ID of the dashboard.<br>
&emsp; <b>dashboard_custom_subject[Optional]</b>: A string representing the custom subject of the dashboard.&nbsp;<br>
&emsp; <b>warehouse_id</b>: A string representing the ID of the warehouse.<br>

Here's an example of how to use the `SQL` Task type:

```python
@wf.sql_task
def sample_sql_task_query():
    return SqlTask(
        query_id="your_sql_query_id", warehouse_id="your_warehouse_id"
    )


@wf.sql_task
def sample_sql_task_file() -> any:
    return SqlTask(file_path="products/brickflow_test/src/sql/sql_task_file_test.sql", warehouse_id="your_warehouse_id")


@wf.sql_task
def sample_sql_alert() -> any:
    return SqlTask(
        alert_id="Your_Alert_ID",
        pause_subscriptions=False,
        subscriptions={
            "usernames": ["YOUR_USERNAME", "YOUR_USERNAME"]
        },
        warehouse_id="your_warehouse_id",
    )


@wf.sql_task
def sample_sql_dashboard() -> any:
    return SqlTask(
        dashboard_id="Your_Dashboard_ID",
        dashboard_custom_subject="Raju Legacy Dashboard Test",
        pause_subscriptions=True,
        subscriptions={
            "usernames": ["YOUR_USERNAME", "YOUR_USERNAME"],
            "destination_id": ["your_destination_id"],
        },
        warehouse_id="your_warehouse_id",
    )

# we can also pass task type as parameter
@wf.task(task_type=TaskType.SQL)
def sample_sql_dashboard_task() -> any:
    return SqlTask(
        dashboard_id="Your_Dashboard_ID",
        dashboard_custom_subject="Raju Legacy Dashboard Test",
        pause_subscriptions=True,
        subscriptions={
            "usernames": ["YOUR_USERNAME", "YOUR_USERNAME"],
            "destination_id": ["your_destination_id"],
        },
        warehouse_id="your_warehouse_id",
    )

```

#### If/Else Task

The `IfElseConditionTask` class is used to create conditional tasks in the workflow. It can be used to create tasks with a left operand, a right operand, and an operator.

The `IfElseConditionTask` is used as a decorator in conjunction with the `if_else_condition_task` method of a `Workflow` instance. This method registers the task within the workflow.

`IfElseConditionTask` class can accept the following as inputs:

- **left[Optional]**: A string representing the left operand in the condition.
- **right[Optional]**: A string representing the right operand in the condition.
- **operator[Optional]**: A string representing the operator used in the condition. It can be one of the following: "==", "!=", ">", "<", ">=", "<=".

Here's an example of how to use the `IfElseConditionTask` type:

```python
# Example 1: creating a if/else task with some params
@wf.if_else_condition_task
def sample_if_else_condition_task():
    return IfElseConditionTask(
        left="value1", right="value2", op="=="
    )
# Let me walk you through how we can make use of if/else condition task. we created a task with name `sample_if_else_condition_task` and it will return either true ot false. Now based on the returned bool, now we're going to decide which task to run. check the below examples.

# Example 2: creating a if/else task that depends on example 1 and this task only triggers if example 1 returns true.
@wf.if_else_condition_task(depends_on="sample_if_else_condition_task", name="new_conditon_task", if_else_outcome={"sample_if_else_condition_task":"true"})
def sample_condition_true():
    return IfElseConditionTask(
        left='{{job.id}}',
        op="==",
        right='{{job.id}}')

'''
 Now i created on more condition task (you can create any task type), since my new task named `new_conditon_task` is dependent on `sample_if_else_condition_task` (if/else task). Now, If my parent tasks runs sucessfully (returns true) then only this task will trigger, cz i mentioned 
if_else_outcome={"sample_if_else_condition_task":"true"}, to seee the false case see the example below.
'''
#Example 3: this task will trigger only when example1 task fails (returns false).
@wf.if_else_condition_task(depends_on="sample_if_else_condition_task", name="example_task_3", if_else_outcome={"sample_if_else_condition_task":"false"})
def sample_condition_false():
    return IfElseConditionTask(
        left='{{job.trigger.type}}',
        op="==",
        right='{{job.trigger.type}}')

# Note: As we can have multiple deps same way we can keep multiple deps for if_else_outcome:
# Ex: if_else_outcome={"task1":"false", "task2":"true"}

# Example 4: creating a SQL Alert Task that depends on example_task_3, now the below sql task will trigger only if above tasks returns true.
@wf.sql_task(depends_on="example_task_3", if_else_outcome={"example_task_3":"true"})
def sample_sql_alert() ->any:
    # it automatically validates user emails
    return SqlTask(alert_id="ALERT_ID", pause_subscriptions=False, subscriptions={"usernames":["YOUR_EMAIL", 'YOUR_EMAIL']} ,warehouse_id="WAREHOUSE_ID")
# Note: Since SQL task doesn't return any bool, we can't make use of if_else_outcome params for the tasks that depends on sql Task
```

#### For each Task
The for each task is used to iterate the execution of a task over a set of input values. Iteration of a task over a set of input values can be achieved decorating your task function with the `for_each_task` method of the `Workflow` instance.

Iteration of tasks is possible only for task types:

- Notebook
- Spark Jar
- Python
- Run Job
- Sql

The `for_each_task` decorator can be configured by providing in the `for_each_task_conf` param a `JobsTasksForEachTaskConfigs` config in which you specify:

- **inputs: Optional[str]**: the list of input values to iterate over. This can be a python iterable, or a string representing a JSON formatted array of values.
- **for_each_task_concurrency: Optional[int]**: the number of concurrent executions of the task. Default is 1.

A reference to the current input value we are iterating on can be accessed using `{{input}}` databricks workflow parameter.

Here are some examples of how to use the for each task type:

```python

@wf.for_each_task(
    depends_on=example_task,
    for_each_task_conf=JobsTasksForEachTaskConfigs(
        # Inputs can be provided by either a python iterable or a json-string
        inputs=[
            "AZ",
            "CA",
            "IL",
        ],
        concurrency=3,
    ),
)
def example_notebook():
    return NotebookTask(
        notebook_path="notebooks/example_notebook.py",
        base_parameters={"looped_parameter": "{{input}}"},
    )


@wf.for_each_task(
    depends_on=example_task,
    for_each_task_conf=JobsTasksForEachTaskConfigs(
        inputs='["1", "2", "3"]', concurrency=3
    ),
)
def example_brickflow_task(*, test_param="{{input}}"):
    print(f"Test param: {test_param}")
    param = ctx.get_parameter("looped_parameter")
    print(f"Nested brickflow task running with input: {param}")


@wf.for_each_task(
    depends_on=example_task,
    libraries=[
        JarTaskLibrary(
            jar="<dbfs:/some/path/to/The.jar>"
        ) 
    ],
    for_each_task_conf=JobsTasksForEachTaskConfigs(
        inputs="[1,2,3]",
        concurrency=1,
    ),
)
def for_each_spark_jar():
    return SparkJarTask(
        main_class_name="com.example.MainClass", 
        parameters=["{{input}}"],
    )


@wf.for_each_task(
    depends_on=example_task,
    for_each_task_conf=JobsTasksForEachTaskConfigs(
        inputs="[1,2,3]",
        concurrency=1,
    ),
)
def for_each_spark_python():
    return SparkPythonTask(
        python_file="src/python/print_args.py",
        source="WORKSPACE",
        parameters=["{{input}}"],
    )


@wf.for_each_task(
    depends_on=example_notebook,
    for_each_task_conf=JobsTasksForEachTaskConfigs(
        inputs="[1,2,3]",
        concurrency=1,
    ),
)
def for_each_sql_task() -> any:
    return SqlTask(
        query_id="<some-query-id>", 
        warehouse_id="<some-warehouse-id>", 
        parameters={"looped_parameter": "{{input}}"},
    )

```

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

Run snowflake queries from the databricks environment

As databricks secrets is a key value store, code expects the secret scope to contain the below exact keys

- `username` : user id created for connecting to snowflake for ex: sample_user  
- `password` : password information for about user for ex: P@$$word  
- `account`  : snowflake account information, not entire url for ex: sample_enterprise  
- `warehouse`: warehouse/cluster information that user has access for ex: sample_warehouse  
- `database` : default database that we want to connect for ex: sample_database  
- `role`     : role to which the user has write access for ex: sample_write_role

SnowflakeOperator can accept the following as inputs

- `secret_scope` : **(required)** databricks secret scope identifier
- `query_string` : **(required)** queries separated by semicolon
- `sql_file` : (optional) path to the sql file
- `parameters` : (optional) dictionary with variables that can be used to substitute in queries
- `fail_on_error` : (optional) bool to fail the task if there is a sql error, default is True

Operator only takes one of either query_string or sql_file needs to be passed

```python title="snowflake_operator using sql queries "
from brickflow_plugins import SnowflakeOperator

wf = Workflow(...)

@wf.task
def run_snowflake_queries(*args):
  sf_query_run = SnowflakeOperator(
    secret_scope = "your_databricks secrets scope name",
    query_string ="select * from database.$schema.$table where $filter_condition1; select * from sample_schema.test_table",
    parameters = {"schema":"test_schema","table":"sample_table","filter_condition":"col='something'"},
    fail_on_error=True,
  )
  sf_query_run.execute()

```

```python title="snowflake_operator_using_sql_files"
#Sql file path is relative from the brickflow project root (Ex: root/products/{product_name})
@wf.task
def run_snowflake_files(*args):
    sf_file_run = SnowflakeOperator(
        secret_cope="sample_scope",
        sql_file=f"src/sql/sample.sql",
        parameters={"database": "sample_db"},
    )
    sf_file_run.execute()
```

#### UC to Snowflake Operator

copy data from databricks to snowflake

As databricks secrets is a key value store, code expects the secret scope to contain the below exact keys
- `username` : user id created for connecting to snowflake for ex: sample_user  
- `password` : password information for about user for ex: P@$$word  
- `account`  : snowflake account information, not entire url for ex: sample_enterprise  
- `warehouse`: warehouse/cluster information that user has access for ex: sample_warehouse  
- `database` : default database that we want to connect for ex: sample_database  
- `role`     : role to which the user has write access for ex: sample_write_role

UcToSnowflakeOperator can expects the following as inputs to copy data in parameters  
one of Either dbx_sql or (dbx_catalog, dbx_database, dbx_table ) needs to be provided
- `load_type`: (required) type of data load , acceptable values full or incremental
- `dbx_catalog`: (optional) name of the databricks catalog in which object resides
- `dbx_database`: (optional) name of the databricks schema in which object is available
- `dbx_table`: (optional) name of the databricks object we want to copy to snowflake
- `dbx_sql`: (optional) Custom sql to extract data from databricks Unity Catalog
- `sf_database`: (optional) name of the snowflake database if different from the one in secret_scope
- `sf_schema`: (required) name of the snowflake schema in which we want to copy the data
- `sf_table`: (required) name of the snowflake object to which we want to copy from databricks
- `incremental_filter`: (required for incrmental mode) condition to manage data before writing to snowflake
- `dbx_data_filter`: (optional) filter condition on databricks source for full or incremental (if different from inremental_filter)
- `sf_grantee_roles`: (optional) snowflake roles to which we want to grant select/read access, can be a comma seperated string
- `sf_cluster_keys`: (optional) list of keys we want to cluster our snowflake table.
- `write_mode`: (optional) write mode to write into snowflake table ( overwrite, append etc)

```python title="uc_to_snowflake_operator"
from brickflow_plugins import UcToSnowflakeOperator

wf = Workflow(...)

@wf.task
def run_snowflake_queries(*args):
  uc_to_sf_copy = UcToSnowflakeOperator(
    secret_scope = "your_databricks secrets scope name",
    write_mode ="overwrite",
    parameters = {'load_type':'incremental','dbx_catalog':'sample_catalog','dbx_database':'sample_schema',
                      'dbx_table':'sf_operator_1', 'sf_schema':'stage','sf_table':'SF_OPERATOR_1',
                      'sf_grantee_roles':'downstream_read_role1,downstream_read_role2', 'incremental_filter':"dt='2023-10-22'",
                      'sf_cluster_keys':'', 'dbx_sql':'Custom sql query to read data from UC'}
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

#### Box Operators

The Box Operator provides a comprehensive solution for authenticating with Box and efficiently managing file transfers
between Box and Databricks Unity Catalog (UC) volumes.  It includes classes for downloading and uploading files,
leveraging JWT authentication via BoxAuthenticator.

To properly authenticate with Box using JWT within the Databricks or Cerberus environments,
ensure that your secrets scope contains the following exact keys:

`Dbutils or Cerberus`
The secrets scope should contain the following keys for Box authentication:

- `client_id`: `your_client_id` The client ID for the Box application.
- `client_secret`: `your_client_secret` The client secret for the Box application.
- `jwt_key_id`: `your_jwt_key_id` The JWT key ID for the Box application.
- `rsa_private_key_data`: `your_rsa_private_key_data` The RSA private key data for the Box application. This is encoded in UTF-8.
- `rsa_private_key_passphrase`: `your_rsa_private_key_passphrase` The passphrase for the RSA private key.
- `enterprise_id`: `your_enterprise_id` The enterprise ID for the Box application.

The `BoxToVolumesOperator` downloads files from Box to Databricks Unity Catalog (UC) volume.

The `VolumesToBoxOperator` uploads files from a Databricks Unity Catalog (UC) volume to a Box folder.

The `BoxOperator` manages the high-level operations for interacting with Box (download/upload).

`BoxToVolumesOperator, VolumesToBoxOperator and BoxOperator Parameters:`

- `secret_scope`: (required) The scope within Databricks or Cerberus where the secrets are stored.
- `cerberus_client_url`: (optional) The URL for the Cerberus client, used to retrieve secrets if not found in the secret_scope.
- `folder_id`: (required) The ID of the Box folder from which files will be downloaded.
- `volume_path`: (required) The local path to the volume where files will be downloaded.
- `file_names`: (optional) A list of specific file names to be downloaded. If not specified, all files in the folder will be downloaded.
- `file_pattern`: (optional) The pattern to match file names starting with or ending with the given file pattern to be downloaded or uploaded.
- `file_id`: (optional for BoxToVolumesOperator) The ID of a specific file to be downloaded. If specified, only this file will be downloaded. This parameter is not used in VolumesToBoxOperator.
- `operation`: (required only for BoxOperator) Specifies the operation to be performed: `"download"` or `"upload"`.

```python title="box_operators"
from brickflow.context import ctx
from brickflow_plugins import BoxToVolumesOperator, VolumeToBoxOperator, BoxOperator

wf = Workflow(...)

@wf.task
def box_to_volume():
    box_to_volume_copy = BoxToVolumesOperator(
        secret_scope="my_secret_scope",
        cerberus_client_url="https://cerberus-url.com",
        folder_id="12345",
        volume_path="/path/to/local/volume",
        file_names=["file1.txt", "file2.txt"],
        file_pattern=".txt",
        file_id="678910",
    )
    box_to_volume_copy.execute()


@wf.task
def volume_to_box():
    volumes_to_box_copy = VolumesToBoxOperator(
        secret_scope="my_secret_scope",
        folder_id="12345",
        volume_path="/path/to/local/volume",
        file_names=["file1.txt", "file2.txt"],
        file_pattern=".txt",
    )
    volumes_to_box_copy.execute()


@wf.task
def download_box_to_volume():
    download_box_to_volume_copy = BoxOperator(
        secret_scope="my_secret_scope",
        folder_id="12345",
        volume_path="/path/to/local/volume",
        file_names=["file1.txt", "file2.txt"],
        file_pattern=".txt",
        file_id="678910",
        operation="download",
    )
    download_box_to_volume_copy.execute()


@wf.task
def upload_volume_to_box():
    upload_volumes_to_box_copy = BoxOperator(
        secret_scope="my_secret_scope",
        cerberus_client_url="https://cerberus-url.com",
        folder_id="12345",
        volume_path="/path/to/local/volume",
        file_names=["file1.txt", "file2.txt"],
        file_pattern=".txt",
        operation="upload",
    )
    upload_volumes_to_box_copy.execute()
```

Check operator logs for more details on the status of the connection and the refresh.
