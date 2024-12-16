from brickflow import (
    Workflow,
    WorkflowPermissions,
    User,
    NotebookTask,
    Cluster,
    JarTaskLibrary,
    SparkJarTask,
    SparkPythonTask,
    SqlTask,
)

from brickflow.context import ctx

cluster = Cluster(
    name=f"job_cluster_for_each_task_examples",
    driver_node_type_id="r7g.large",
    node_type_id="r7g.large",
    spark_version="13.3.x-scala2.12",
    min_workers=1,
    max_workers=1,
    policy_id="<your-policy-id>",  # replace with an existing policy id
)

wf = Workflow(
    "for_each_task_examples_wf",
    default_cluster=cluster,
    permissions=WorkflowPermissions(
        can_manage=[
            User(
                "<someuser@somedomain.com>"  # replace email with existing users' email on databricks
            )
        ],
    ),
)


@wf.task
def example_task():
    print("This is a dependant task!")


@wf.for_each_task(
    for_each_task_inputs=[
        "AZ",
        "CA",
        "IL",
    ],  # Input can be provided by either a python iterable or a json-string
    for_each_task_concurrency=3,
    depends_on=example_task,
)
def example_notebook():
    return NotebookTask(
        notebook_path="notebooks/example_notebook.py",
        base_parameters={"looped_parameter": "{{input}}"},
    )


@wf.for_each_task(
    for_each_task_inputs='["1", "2", "3"]',
    for_each_task_concurrency=3,
    depends_on=example_task,
)
def example_brickflow_task(*, test_param="{{input}}"):
    print(f"Test param: {test_param}")
    param = ctx.get_parameter("looped_parameter")
    print(f"Nested brickflow task running with input: {param}")


@wf.for_each_task(
    depends_on=example_task,
    for_each_task_inputs="[1,2,3]",
    for_each_task_concurrency=1,
    libraries=[
        JarTaskLibrary(
            jar="<dbfs:/some/path/to/The.jar>"
        )  # Replace with actual jar path
    ],
)
def for_each_spark_jar():
    return SparkJarTask(
        main_class_name="com.example.MainClass",  # Replace with actual main class name
        parameters=["{{input}}"],
    )


@wf.for_each_task(
    depends_on=example_task, for_each_task_inputs="[1,2,3]", for_each_task_concurrency=1
)
def for_each_spark_python():
    return SparkPythonTask(
        python_file="src/python/print_args.py",
        source="WORKSPACE",
        parameters=["{{input}}"],
    )


@wf.for_each_task(
    depends_on=example_notebook,
    for_each_task_inputs="[1,2,3]",
    for_each_task_concurrency=1,
)
def for_each_sql_task() -> any:
    return SqlTask(
        query_id="<some-query-id>",  # Replace with actual query id
        warehouse_id="<some-warehouse-id>",  # Replace with actual warehouse id
        parameters={"looped_parameter": "{{input}}"},
    )
