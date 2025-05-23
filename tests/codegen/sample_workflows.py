from typing import Dict, List, Optional

from pydantic import BaseModel

from brickflow import JarTaskLibrary, PypiTaskLibrary
from brickflow.bundles.model import (
    JobsContinuous,
    JobsParameters,
    JobsTasksRunJobTaskPipelineParams,
    JobsTasksSqlTaskAlert,
    JobsTasksSqlTaskDashboard,
    JobsTasksSqlTaskFile,
    JobsTasksSqlTaskQuery,
    JobsHealthRules,
)
from brickflow.engine.compute import Cluster
from brickflow.engine.task import (
    BrickflowTriggerRule,
    DLTPipeline,
    IfElseConditionTask,
    JobsTasksForEachTaskConfigs,
    NotebookTask,
    PythonWheelTask,
    RunJobTask,
    SparkJarTask,
    SparkPythonTask,
    SqlTask,
    TaskResponse,
    TaskRunCondition,
    TaskSettings,
    TaskType,
)
from brickflow.engine.workflow import User, Workflow, WorkflowPermissions

wf = Workflow(
    "test",
    default_cluster=Cluster.from_existing_cluster("existing_cluster_id"),
    schedule_quartz_expression="* * * * *",
    permissions=WorkflowPermissions(
        owner=User("abc@abc.com"),
        can_manage_run=[User("abc@abc.com")],
        can_view=[User("abc@abc.com")],
        can_manage=[User("abc@abc.com")],
    ),
    run_as_user="abc@abc.com",
    tags={"test": "test2"},
    common_task_parameters={"all_tasks1": "test", "all_tasks3": "123"},  # type: ignore
    health=[
        JobsHealthRules(metric="RUN_DURATION_SECONDS", op="GREATER_THAN", value=7200.0)
    ],
    trigger={
        "file_arrival": {"url": "<my_url>"},
        "pause_status": "UNPAUSED",
    },  # type: ignore
    parameters=[
        JobsParameters(
            default="value1",
            name="wf_param1",
        )
    ],
)


@wf.task()
def task_function(*, test="var"):
    return test


@wf.task
def task_function_no_deco_args(*, test="var"):
    print(test)
    return "hello world"


@wf.notebook_task()
def notebook_task_a(*, test="var"):
    print(test)
    return NotebookTask(
        notebook_path="notebooks/notebook_a",
    )  # type: ignore


@wf.python_wheel_task(
    libraries=[PypiTaskLibrary("data-mirror")],
    depends_on=notebook_task_a,
)
def my_python_wheel_task():
    return PythonWheelTask(
        package_name="data-mirror",
        entry_point="datamirror",
        parameters=["--configuration_file", "dbfs:/path/to/config.json"],
    )


@wf.spark_jar_task(
    libraries=[
        JarTaskLibrary(
            jar="dbfs:/Volumes/development/global_sustainability_dev/raju_spark_jar_test/PrintArgs.jar"
        )
    ],
    depends_on=notebook_task_a,
)
def spark_jar_task_a():
    return SparkJarTask(
        main_class_name="PrintArgs",
        parameters=["Hello", "World!"],
    )  # type: ignore


@wf.spark_python_task(
    libraries=[PypiTaskLibrary(package="koheesio")],
    depends_on=spark_jar_task_a,
)
def spark_python_task_a():
    return SparkPythonTask(
        python_file="./products/test-project/spark/python/src/run_task.py",
        source="GIT",
        parameters=["--param1", "World!"],
    )  # type: ignore


@wf.run_job_task(
    depends_on=notebook_task_a,
)
def run_job_task_a():
    return RunJobTask(job_name="dev_object_raw_to_cleansed")  # type: ignore


@wf.run_job_task(
    depends_on=notebook_task_a,
)
def run_job_task_b():
    return RunJobTask(
        job_name="dev_object_raw_to_cleansed", host="https://foo.cloud.databricks.com"
    )  # type: ignore


@wf.sql_task
def sample_sql_task_query() -> any:
    return SqlTask(
        query_id="your_sql_query_id",
        warehouse_id="your_warehouse_id",
    )


@wf.sql_task
def sample_sql_task_file() -> any:
    return SqlTask(
        file_path="products/brickflow_test/src/sql/sql_task_file_test.sql",
        warehouse_id="your_warehouse_id",
    )


@wf.sql_task(depends_on=notebook_task_a)
def sample_sql_alert() -> any:
    # we need to create kind of dict format for subscriptions to accept usenames and one destination_id..
    # we can either send username or destination_id (not both)
    # it automatically validates user emails
    return SqlTask(
        alert_id="Your_Alert_ID",
        pause_subscriptions=False,
        subscriptions={"usernames": ["YOUR_USERNAME", "YOUR_USERNAME"]},
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


@wf.if_else_condition_task(depends_on=[sample_sql_task_query])
def condtion_task_test() -> any:
    return IfElseConditionTask(
        left="1",
        op="==",
        right="2",
    )


@wf.if_else_condition_task(depends_on=[sample_sql_task_query])
def condition_task_test2() -> any:
    return IfElseConditionTask(
        left="1",
        op="==",
        right="1",
    )


@wf.spark_python_task(
    libraries=[PypiTaskLibrary(package="koheesio")],
    depends_on=[spark_python_task_a, condition_task_test2],
    if_else_outcome={"condition_task_test2": "false"},
)
def spark_python_task_depended():
    return SparkPythonTask(
        python_file="./products/test-project/spark/python/src/run_task.py",
        source="GIT",
        parameters=["--param1", "World!"],
    )  # type: ignore


@wf.spark_python_task(
    libraries=[PypiTaskLibrary(package="koheesio")],
    depends_on=[condtion_task_test, condition_task_test2],
    if_else_outcome={"condtion_task_test": "true", "condition_task_test2": "false"},
)
def spark_python_task_depended2():
    return SparkPythonTask(
        python_file="./products/test-project/spark/python/src/run_task.py",
        source="GIT",
        parameters=["--param1", "World!"],
    )  # type: ignore


@wf.dlt_task
def dlt_pipeline():
    # pass
    return DLTPipeline(
        name="hello world",
        storage="123",
        language="PYTHON",
        configuration={},
        cluster=Cluster(
            "test",
            "someversion",
            "vm-node",
            custom_tags={"name": "test"},
            min_workers=2,
            max_workers=10,
        ),
        notebook_path="scripts/spark_script_1.py",
    )


@wf.dlt_task
def dlt_pipeline_2():
    # pass
    return DLTPipeline(
        name="hello world",
        storage="123",
        language="PYTHON",
        configuration={},
        notebook_path="scripts/spark_script_2.py",
    )


@wf.task()
def task_function_nokwargs():
    return "hello world"


@wf.task(depends_on=task_function)
def task_function_2():
    return "hello world"


@wf.task(depends_on="task_function_2")
def task_function_3():
    return "hello world"


@wf.task(depends_on="task_function_3", trigger_rule=BrickflowTriggerRule.NONE_FAILED)
def task_function_4():
    return "hello world"


@wf.task(
    depends_on="task_function_4",
    task_settings=TaskSettings(run_if=TaskRunCondition.AT_LEAST_ONE_FAILED),
)
def task_function_5():
    return "hello world"


@wf.task(
    task_type=TaskType.CUSTOM_PYTHON_TASK,
    trigger_rule=BrickflowTriggerRule.NONE_FAILED,
    custom_execute_callback=lambda x: TaskResponse(x.name, push_return_value=True),
)
def custom_python_task_push():
    pass


job_cluster = Cluster(
    name="sample_job_cluster",
    node_type_id="m6gd.xlarge",
    spark_version="13.3.x-scala2.12",
    num_workers=1,
)

wf2 = Workflow(
    "wf-test-2",
    default_cluster=job_cluster,
    schedule_continuous=JobsContinuous(pause_status="PAUSED"),
    permissions=WorkflowPermissions(
        owner=User("abc@abc.com"),
        can_manage_run=[User("abc@abc.com")],
        can_view=[User("abc@abc.com")],
        can_manage=[User("abc@abc.com")],
    ),
    run_as_user="abc@abc.com",
    tags={"test": "test2"},
    common_task_parameters={"all_tasks1": "test", "all_tasks3": "123"},  # type: ignore
    health=[
        JobsHealthRules(metric="RUN_DURATION_SECONDS", op="GREATER_THAN", value=7200.0)
    ],
)


@wf2.task()
def task_function2(*, test="var"):
    return test


wf_bad_tasks = Workflow(
    "wf_bad_tasks",
    default_cluster=Cluster.from_existing_cluster("existing_cluster_id"),
    schedule_continuous=JobsContinuous(pause_status="PAUSED"),
    permissions=WorkflowPermissions(
        owner=User("abc@abc.com"),
        can_manage_run=[User("abc@abc.com")],
        can_view=[User("abc@abc.com")],
        can_manage=[User("abc@abc.com")],
    ),
    run_as_user="abc@abc.com",
    tags={"test": "test2"},
    common_task_parameters={"all_tasks1": "test", "all_tasks3": "123"},  # type: ignore
    health=[
        JobsHealthRules(metric="RUN_DURATION_SECONDS", op="GREATER_THAN", value=7200.0)
    ],
)


class BadPythonModel(BaseModel):
    python_file: str
    source: str
    parameters: List[str]


class BadPythonWheelModel(BaseModel):
    package_name: str
    entry_point: str
    named_parameters: Optional[Dict[str, str]] = None
    parameters: Optional[List[str]] = None


class BadSparkJar(BaseModel):
    jar_uri: str
    main_class_name: str
    parameters: List[str]


class BadRunJob(BaseModel):
    dbt_commands: List[str]
    jar_params: List[str]
    job_id: float
    job_parameters: Optional[Dict[str, str]]
    notebook_params: Optional[Dict[str, str]]
    pipeline_params: Optional[JobsTasksRunJobTaskPipelineParams]
    python_named_params: Optional[Dict[str, str]]
    python_params: Optional[List[str]]
    spark_submit_params: Optional[List[str]]
    sql_params: Optional[Dict[str, str]]
    host: str


class BadSql(BaseModel):
    alert: Optional[JobsTasksSqlTaskAlert]
    dashboard: Optional[JobsTasksSqlTaskDashboard]
    file: Optional[JobsTasksSqlTaskFile]
    parameters: Optional[Dict[str, str]]
    query: Optional[JobsTasksSqlTaskQuery]
    warehouse_id: str


class BadCondition(BaseModel):
    left: str
    op: str
    right: str


class BadDLT(BaseModel):
    catalog: str
    commands: List[str]
    profiles_directory: Optional[str]
    project_directory: Optional[str]
    schema_: Optional[str]
    source: Optional[str]
    warehouse_id: Optional[str]


@wf_bad_tasks.task(task_type=TaskType.PYTHON_WHEEL_TASK)
def task_python_wheel():
    return BadPythonWheelModel(
        package_name="data-mirror",
        entry_point="datamirror",
        parameters=["--configuration_file", "dbfs:/path/to/config.json"],
    )


@wf_bad_tasks.task(task_type=TaskType.SPARK_PYTHON_TASK)
def task_python():
    return BadPythonModel(
        python_file="./products/test-project/spark/python/src/run_task.py",
        source="GIT",
        parameters=["--param1", "World!"],
    )


@wf_bad_tasks.task(task_type=TaskType.SPARK_JAR_TASK)
def task_spark_jar():
    return BadSparkJar(
        jar_uri="dbfs:/path/to/jar",
        main_class_name="com.example.MainClass",
        parameters=["param1", "param2"],
    )


wf3 = Workflow(
    "wf-foreach-task-test",
    default_cluster=job_cluster,
    permissions=WorkflowPermissions(
        owner=User("abc@abc.com"),
        can_manage_run=[User("abc@abc.com")],
        can_view=[User("abc@abc.com")],
        can_manage=[User("abc@abc.com")],
    ),
    run_as_user="abc@abc.com",
    tags={"test": "test2"},
)


@wf3.notebook_task()
def first_notebook():
    return NotebookTask(notebook_path="notebooks/notebook_a", source="WORKSPACE")


@wf3.for_each_task(
    depends_on=first_notebook,
    for_each_task_conf=JobsTasksForEachTaskConfigs(
        concurrency=3, inputs="[1, 2, 3]", task_type=TaskType.NOTEBOOK_TASK
    ),
)
def for_each_notebook():
    return NotebookTask(
        notebook_path="notebooks/notebook_b",
        base_parameters={"looped_parameter": "{{input}}"},
        source="WORKSPACE",
    )


@wf3.for_each_task(
    depends_on=first_notebook,
    for_each_task_conf=JobsTasksForEachTaskConfigs(
        inputs=["1", "2", "3"], concurrency=1, task_type=TaskType.BRICKFLOW_TASK
    ),
)
def for_each_bf_task(*, looped_parameter="{{input}}"):
    print(f"This is a nested bf task running with input: {looped_parameter}")
    raise ValueError(
        "This should not be raised during codegen if we provide the task_type!"
    )


@wf3.for_each_task(
    depends_on=for_each_bf_task,
    for_each_task_conf=JobsTasksForEachTaskConfigs(inputs="[1,2,3]", concurrency=1),
    libraries=[JarTaskLibrary(jar="dbfs:/some/path/to/The.jar")],
)
def for_each_spark_jar():
    return SparkJarTask(
        main_class_name="com.example.MainClass",
        parameters=["{{input}}"],
    )


@wf3.for_each_task(
    depends_on=first_notebook,
    for_each_task_conf=JobsTasksForEachTaskConfigs(inputs="[1,2,3]", concurrency=1),
)
def for_each_spark_python():
    return SparkPythonTask(
        python_file="/test-project/path/to/python_script.py",
        source="WORKSPACE",
        parameters=["{{input}}"],
    )


@wf3.for_each_task(
    depends_on=first_notebook,
    for_each_task_conf=JobsTasksForEachTaskConfigs(
        inputs='["job_param_1","job_param_2"]', concurrency=1
    ),
)
def for_each_run_job():
    return RunJobTask(job_name="some_job_name")


@wf3.for_each_task(
    depends_on=first_notebook,
    for_each_task_conf=JobsTasksForEachTaskConfigs(inputs="[1,2,3]", concurrency=1),
)
def for_each_sql_task() -> any:
    return SqlTask(
        query_id="some_sql_query_id",
        warehouse_id="some_warehouse_id",
        parameters={"looped_parameter": "{{input}}"},
    )
