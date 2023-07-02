from brickflow.engine.compute import Cluster
from brickflow.engine.task import BrickflowTriggerRule, TaskType, TaskResponse
from brickflow.engine.workflow import Workflow

wf = Workflow(
    "test",
    default_cluster=Cluster.from_existing_cluster("XXXX-XXXXXX-XXXXXXXX"),
    tags={"test": "test2"},
    common_task_parameters={"all_tasks1": "test", "all_tasks3": "123"},  # type: ignore
)


@wf.task()
def task_function():
    return "hello world"


@wf.task
def task_function_no_deco_args():
    return "hello world"


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
    task_type=TaskType.CUSTOM_PYTHON_TASK,
    trigger_rule=BrickflowTriggerRule.NONE_FAILED,
    custom_execute_callback=lambda x: TaskResponse(x.name, push_return_value=True),
)
def custom_python_task_push():
    pass
