from brickflow import (
    Workflow,
    NotebookTask,
    SparkPythonTask,
)
from brickflow.engine.task import PypiTaskLibrary

wf = Workflow(
    "brickflow-serverless-demo",
    schedule_quartz_expression="0 0/20 0 ? * * *",
    libraries=[
        PypiTaskLibrary(package="pytz==2024.2"),
        #  Custom repositories are not supported for serverless workloads, due to Databricks CLI limitations.
        #  Refer to: https://github.com/databricks/cli/pull/1842This will be fixed in the future releases, use wheel instead.
        # PypiTaskLibrary(
        #     package="my-lib==1.2.3", repo="https://artifactory.my-org.com/api/pypi/python-virtual/simple"
        # ),
    ],
)


@wf.task
def entrypoint_task():
    pass


@wf.notebook_task
def notebook_task():
    return NotebookTask(
        notebook_path="notebooks/example_notebook.py",
        base_parameters={
            "some_parameter": "some_value",  # in the notebook access these via dbutils.widgets.get("some_parameter")
        },
    )  # type: ignore


@wf.spark_python_task
def spark_python_task():
    return SparkPythonTask(
        python_file="/src/python/example.py",
        source="GIT",
        parameters=["--timezone", "UTC"],
    )  # type: ignore
