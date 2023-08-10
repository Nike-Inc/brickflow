import resolver
from datetime import timedelta

from airflow.operators.bash import BashOperator
from brickflow import (
    ctx,
    Cluster,
    BrickflowTriggerRule,
    TaskSettings,
    EmailNotifications,
    Workflow,
    WorkflowPermissions,
    User,
    NotebookTask,
)
from brickflow_plugins import TaskDependencySensor

wf = Workflow(
    "brickflow-demo",
    default_cluster=Cluster.from_existing_cluster("YOUR_CLUSTER_ID"),
    # Optional parameters below
    schedule_quartz_expression="0 0/20 0 ? * * *",
    tags={
        "product_id": "brickflow_demo",
        "slack_channel": "YOUR_SLACK_CHANNEL",
    },
    common_task_parameters={
        "catalog": "development",
        "database": "your_database",
    },
    permissions=WorkflowPermissions(
        can_manage_run=[User("abc@gmail.com"), User("xyz@gmail.com")],
        can_view=[User("def@gmail.com")],
        can_manage=[User("ghi@gmail.com")],
    ),
    default_task_settings=TaskSettings(
        email_notifications=EmailNotifications(
            on_start=["xyz@gmail.com"],
            on_success=["xyz@gmail.com"],
            on_failure=["xyz@gmail.com"],
        ),
        timeout_seconds=timedelta(hours=2).seconds,
    ),
    prefix="my_prefix_",
    suffix="_my_suffix",
)


@wf.task
def start():
    pass


@wf.notebook_task
def example_notebook():
    return NotebookTask(
        notebook_path="notebooks/example_notebook.py",
        base_parameters={
            "some_parameter": "some_value",  # in the notebook access these via dbutils.widgets.get("some_parameter")
        },
    )


@wf.task(depends_on=start)
def list_lending_club_data_files():
    return BashOperator(
        task_id=list_lending_club_data_files.__name__,
        bash_command="ls -lrt /dbfs/databricks-datasets/samples/lending_club/parquet/",
    )


@wf.task(depends_on=start)
def print_sample_lending_club_data():
    from src.python.lending_data_show import (
        lending_data_print,
    )

    lending_data_print()


@wf.task(depends_on=print_sample_lending_club_data)
def airflow_external_task_dependency_sensor():
    import base64

    data = base64.b64encode(
        ctx.dbutils.secrets.get("brickflow-demo-tobedeleted", "okta_conn_id").encode(
            "utf-8"
        )
    ).decode("utf-8")
    return TaskDependencySensor(
        task_id="sensor",
        timeout=180,
        # 'https://username:password@databricks.com:90909/?hello=world' - okta_conn_id sample
        okta_conn_id=f"b64://{data}",
        external_dag_id="airflow_test_dag",
        external_task_id="hello",
        allowed_states=["success"],
        execution_delta=None,
        execution_delta_json=None,
        cluster_id="your_cluster_id",
    )


@wf.task(depends_on=airflow_external_task_dependency_sensor)
def lending_data_ingest():
    ctx.spark.sql(
        f"""
        CREATE TABLE IF NOT EXISTS 
        {ctx.dbutils_widget_get_or_else(key="catalog", debug="development")}.\
        {ctx.dbutils_widget_get_or_else(key="database", debug="dummy_database")}.\
        {ctx.dbutils_widget_get_or_else(key="brickflow_env", debug="local")}_lending_data_ingest
        USING DELTA -- this is default just for explicit purpose
        SELECT * FROM parquet.`dbfs:/databricks-datasets/samples/lending_club/parquet/`
    """
    )


@wf.task(depends_on=lending_data_ingest)
def lending_data_optimize():
    ctx.spark.sql(
        f"""
        OPTIMIZE 
        {ctx.dbutils_widget_get_or_else(key="catalog", debug="development")}.\
        {ctx.dbutils_widget_get_or_else(key="database", debug="dummy_database")}.\
        {ctx.dbutils_widget_get_or_else(key="brickflow_env", debug="local")}_lending_data_ingest;
    """
    )


@wf.task(depends_on=lending_data_optimize)
def lending_data_az_transform():
    ctx.spark.sql(
        f"""
        CREATE OR REPLACE TABLE 
        {ctx.dbutils_widget_get_or_else(key="catalog", debug="development")}.\
        {ctx.dbutils_widget_get_or_else(key="database", debug="dummy_database")}.\
        {ctx.dbutils_widget_get_or_else(key="brickflow_env", debug="local")}_lending_data_az_transform
        USING DELTA -- this is default just for explicit purpose
        SELECT * FROM 
        {ctx.dbutils_widget_get_or_else(key="catalog", debug="development")}.\
        {ctx.dbutils_widget_get_or_else(key="database", debug="dummy_database")}.\
        {ctx.dbutils_widget_get_or_else(key="brickflow_env", debug="local")}_lending_data_ingest where addr_state = 'AZ' 
    """
    )


@wf.task(depends_on=lending_data_optimize)
def lending_data_ca_transform():
    ctx.spark.sql(
        f"""
        CREATE OR REPLACE TABLE 
        {ctx.dbutils_widget_get_or_else(key="catalog", debug="development")}.\
        {ctx.dbutils_widget_get_or_else(key="database", debug="dummy_database")}.\
        {ctx.dbutils_widget_get_or_else(key="brickflow_env", debug="local")}_lending_data_ca_transform
        USING DELTA -- this is default just for explicit purpose
        SELECT * FROM 
        {ctx.dbutils_widget_get_or_else(key="catalog", debug="development")}.\
        {ctx.dbutils_widget_get_or_else(key="database", debug="dummy_database")}.\
        {ctx.dbutils_widget_get_or_else(key="brickflow_env", debug="local")}_lending_data_ingest where addr_state = 'CA' 
    """
    )


@wf.task(depends_on=lending_data_optimize)
def lending_data_il_transform():
    ctx.spark.sql(
        f"""
        CREATE OR REPLACE TABLE 
        {ctx.dbutils_widget_get_or_else(key="catalog", debug="development")}.\
        {ctx.dbutils_widget_get_or_else(key="database", debug="dummy_database")}.\
        {ctx.dbutils_widget_get_or_else(key="brickflow_env", debug="local")}_lending_data_il_transform
        USING DELTA -- this is default just for explicit purpose
        SELECT * FROM 
        {ctx.dbutils_widget_get_or_else(key="catalog", debug="development")}.\
        {ctx.dbutils_widget_get_or_else(key="database", debug="dummy_database")}.\
        {ctx.dbutils_widget_get_or_else(key="brickflow_env", debug="local")}_lending_data_ingest where addr_state = 'IL' 
    """
    )


@wf.task(
    depends_on=[
        lending_data_az_transform,
        lending_data_ca_transform,
        lending_data_il_transform,
    ]
)
def lending_data_serve():
    ctx.spark.sql(
        f"""
        CREATE OR REPLACE TABLE {ctx.dbutils_widget_get_or_else(key="catalog", debug="development")}.\
        {ctx.dbutils_widget_get_or_else(key="database", debug="dummy_database")}.\
        {ctx.dbutils_widget_get_or_else(key="brickflow_env", debug="local")}_lending_data_serve
        USING DELTA
        SELECT * FROM {ctx.dbutils_widget_get_or_else(key="catalog", debug="development")}.\
        {ctx.dbutils_widget_get_or_else(key="database", debug="dummy_database")}.\
        {ctx.dbutils_widget_get_or_else(key="brickflow_env", debug="local")}_lending_data_az_transform
        UNION ALL
        SELECT * FROM {ctx.dbutils_widget_get_or_else(key="catalog", debug="development")}.\
        {ctx.dbutils_widget_get_or_else(key="database", debug="dummy_database")}.\
        {ctx.dbutils_widget_get_or_else(key="brickflow_env", debug="local")}_lending_data_ca_transform
        UNION ALL
        SELECT * FROM {ctx.dbutils_widget_get_or_else(key="catalog", debug="development")}.\
        {ctx.dbutils_widget_get_or_else(key="database", debug="dummy_database")}.\
        {ctx.dbutils_widget_get_or_else(key="brickflow_env", debug="local")}_lending_data_il_transform
    """
    )


@wf.task(depends_on=lending_data_serve, trigger_rule=BrickflowTriggerRule.NONE_FAILED)
def lending_data_csv_extract():
    # script_dir = os.path.dirname(os.path.realpath(__file__))
    df = (
        ctx.spark.sql(
            f"""
        SELECT * FROM {ctx.dbutils_widget_get_or_else(key="catalog", debug="development")}.\
        {ctx.dbutils_widget_get_or_else(key="database", debug="dummy_database")}.\
        {ctx.dbutils_widget_get_or_else(key="brickflow_env", debug="local")}_lending_data_serve
    """
        )
        .limit(10)
        .toPandas()
    )

    username_row = ctx.spark.sql("SELECT current_user()").first()
    username = username_row[0]

    # create user-specific path
    csv_path = f"/Workspace/Users/{username}/data.csv"

    print(f"extract path is: {csv_path}")
    df.to_csv(csv_path, index=False)
    # with open(csv_path, "r") as f:
    #     print(f.read())


@wf.task(depends_on=lending_data_csv_extract)
def list_file():
    return BashOperator(task_id=list_file.__name__, bash_command="ls -ltr")


@wf.task(depends_on=list_file)
def end():
    pass


if __name__ == "__main__":
    # wf.tasks["list_lending_club_data_files"].execute()
    # print(task_function_4())
    # wf.tasks["airflow_external_task_dependency_sensor"].execute()
    wf.tasks["print_sample_lending_club_data"].execute()
