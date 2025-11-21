"""
Demo Workflow - Task Injection Example

This workflow demonstrates automatic task injection.
When deployed with BRICKFLOW_INJECT_TASKS_CONFIG set, additional tasks
will be automatically added based on the configuration.

Original workflow structure:
  task_1 -> task_2 -> task_3

After injection (see config/injected_tasks.yaml):
  initialization_task (runs first)
    ↓
  task_1
    ↓
  task_2
    ↓
  monitoring_task (runs after task_1 and task_2)
    ↓
  task_3
    ↓
  completion_logger (runs last)
"""

from brickflow import Workflow, ctx
from brickflow.engine.task import PypiTaskLibrary


# Create the workflow
wf = Workflow(
    "brickflow-task-injection-demo",
    schedule_quartz_expression="0 0/30 * ? * * *",  # Every 30 minutes
    libraries=[
        PypiTaskLibrary(package="pytz==2024.2"),
    ],
    tags={
        "example": "task_injection",
        "feature": "auto_injection",
    },
)


@wf.task
def task_1():
    """
    First task in the workflow.

    After injection, this will run after the initialization_task.
    """
    print("=" * 70)
    print("Executing task_1")
    print("=" * 70)

    # Simulate some work
    import time

    print("Processing data in task_1...")
    time.sleep(1)

    # Get workflow parameters
    env = ctx.get_parameter("brickflow_env", "local")
    print(f"Running in environment: {env}")

    result = {
        "task": "task_1",
        "status": "completed",
        "records_processed": 1000,
    }

    print(f"Task 1 result: {result}")
    print("=" * 70)
    return result


@wf.task(depends_on=task_1)
def task_2():
    """
    Second task in the workflow.

    Depends on task_1. After injection, monitoring_task will run after this.
    """
    print("=" * 70)
    print("Executing task_2")
    print("=" * 70)

    # Simulate some work
    import time

    print("Processing data in task_2...")
    time.sleep(1)

    # Get result from previous task
    task_1_result = ctx.task_coms.get("task_1", "result")
    print(f"Received from task_1: {task_1_result}")

    result = {
        "task": "task_2",
        "status": "completed",
        "records_processed": 2000,
    }

    print(f"Task 2 result: {result}")
    print("=" * 70)

    # Store result for next task
    ctx.task_coms.put("task_2", "result", result)

    return result


@wf.task(depends_on=task_2)
def task_3():
    """
    Third task in the workflow.

    This is a leaf node, so completion_logger will run after this.
    """
    print("=" * 70)
    print("Executing task_3")
    print("=" * 70)

    # Simulate some work
    import time

    print("Processing data in task_3...")
    time.sleep(1)

    # Get result from previous task
    task_2_result = ctx.task_coms.get("task_2", "result")
    print(f"Received from task_2: {task_2_result}")

    result = {
        "task": "task_3",
        "status": "completed",
        "records_processed": 3000,
        "final": True,
    }

    print(f"Task 3 result: {result}")
    print("=" * 70)

    return result


# Note: When deployed with task injection enabled, additional tasks will be
# automatically added to this workflow based on config/injected_tasks.yaml
#
# To deploy with task injection:
# export BRICKFLOW_INJECT_TASKS_CONFIG="config/injected_tasks.yaml"
# brickflow projects deploy --project brickflow-task-injection-demo -e local
#
# To deploy without task injection:
# brickflow projects deploy --project brickflow-task-injection-demo -e local
