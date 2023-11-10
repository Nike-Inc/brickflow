from brickflow.engine.compute import Cluster
from brickflow.engine.task import (
    BrickflowTriggerRule,
    TaskType,
    TaskResponse,
    DLTPipeline,
    NotebookTask,
    TaskSettings,
    TaskRunCondition,
)
from brickflow.engine.workflow import Workflow, WorkflowPermissions, User

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
    health={"rules": [{"metric": "RUN_DURATION_SECONDS", "op": "GREATER_THAN", "value": 7200.0}]},
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
    )


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
