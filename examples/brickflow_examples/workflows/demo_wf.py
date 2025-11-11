from datetime import timedelta

from airflow.operators.bash import BashOperator

from brickflow import (
    BrickflowTriggerRule,
    Cluster,
    EmailNotifications,
    IfElseConditionTask,
    JarTaskLibrary,
    NotebookTask,
    PypiTaskLibrary,
    PythonWheelTask,
    RunJobTask,
    SparkJarTask,
    SparkPythonTask,
    SqlTask,
    TaskSettings,
    User,
    Workflow,
    WorkflowPermissions,
    ctx,
)
from brickflow.engine.task import PypiTaskLibrary
from brickflow_plugins import (
    AirflowProxyOktaClusterAuth,
    AutosysSensor,
    BoxOperator,
    BoxToVolumesOperator,
    SnowflakeOperator,
    TableauRefreshDataSourceOperator,
    TableauRefreshWorkBookOperator,
    TaskDependencySensor,
    UcToSnowflakeOperator,
    VolumesToBoxOperator,
)

wf = Workflow(
    "brickflow-demo",
    # replace <all-purpose-cluster-id> with your cluster id
    default_cluster=Cluster.from_existing_cluster("<all-purpose-cluster-id>"),
    # Optional parameters below
    schedule_quartz_expression="0 0/20 0 ? * * *",
    tags={
        "product_id": "brickflow_demo",
        "slack_channel": "YOUR_SLACK_CHANNEL",
    },
    common_task_parameters={
        "catalog": "<unity-catalog-name>",
        "database": "<unity-schema-name>",
    },
    # replace <emails> with existing users' email on databricks
    permissions=WorkflowPermissions(
        can_manage_run=[User("abc@gmail.com"), User("xyz@gmail.com")],
        can_view=[User("def@gmail.com")],
        can_manage=[User("ghi@gmail.com")],
    ),
    libraries=[
        PypiTaskLibrary(package="snowflake==0.6.0"),
        PypiTaskLibrary(package="boxsdk==3.9.2"),
    ],
    # replace <emails> with existing users' email on databricks
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
    )  # type: ignore


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
        ctx.dbutils.secrets.get("brickflow-demo", "okta_conn_id").encode("utf-8")
    ).decode("utf-8")
    return TaskDependencySensor(
        task_id="sensor",
        timeout=180,
        airflow_cluster_auth=AirflowProxyOktaClusterAuth(
            oauth2_conn_id=f"b64://{data}",
            airflow_cluster_url="https://proxy.airflow/cluster_name",
            airflow_version="2.0.2",  # if you are using airflow 1.x please make sure this is the right value, the apis are different between them!
        ),
        external_dag_id="dag_id",
        external_task_id="task_id",
        allowed_states=["success"],
        execution_delta=timedelta(days=-1),
        execution_delta_json=None,
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
    # Alternative using pattern matching:
    # depends_on="lending_data_*_transform"
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
        # 'https://username:password@databricks.com:90909/?hello=world' - okta_conn_id sample
        okta_conn_id=f"b64://{data}",
        poke_interval=200,
        job_name="hello",
        time_delta={"days": 0},
    )


@wf.task
def run_snowflake_queries(*args):
    uc_to_sf_table_copy = UcToSnowflakeOperator(
        secret_cope="sample_scope",
        parameters={
            "load_type": "incremental",
            "dbx_catalog": "sample_catalog",
            "dbx_database": "sample_schema",
            "dbx_table": "sf_operator_1",
            "sf_schema": "stage",
            "sf_table": "SF_OPERATOR_1",
            "sf_grantee_roles": "downstream_read_role",
            "incremental_filter": "dt='2023-10-22'",
            "dbx_data_filter": "run_dt='2023-10-21'",
            "sf_cluster_keys": "",
        },
    )
    uc_to_sf_table_copy.execute()


# Operator usage to run custom sql, to extract data from Unity Catalog


@wf.task
def copy_uc_to_snowflake(*args):
    uc_to_sf_query_copy = UcToSnowflakeOperator(
        secret_scope="sample_scope",
        write_mode="overwrite",
        parameters={
            "load_type": "incremental",
            "sf_schema": "stage",
            "sf_table": "SF_OPERATOR_1",
            "sf_grantee_roles": "downstream_read_role",
            "incremental_filter": "dt='2023-10-22'",
            "dbx_data_filter": "run_dt='2023-10-21'",
            "sf_cluster_keys": "",
            "dbx_sql": "select cola, colb, colc from catalog.schema.table where some condition",
        },
    )
    uc_to_sf_query_copy.execute()


@wf.task
def run_snowflake_queries(*args):
    uc_to_sf_full_copy = UcToSnowflakeOperator(
        secret_cope="sample_scope",
        parameters={
            "load_type": "full",
            "dbx_catalog": "sample_catalog",
            "dbx_database": "sample_schema",
            "dbx_table": "sf_operator_1",
            "sf_schema": "stage",
            "sf_table": "SF_OPERATOR_1",
            "sf_grantee_roles": "downstream_read_role",
            "sf_cluster_keys": "",
        },
    )
    uc_to_sf_copy.execute()


@wf.task
def run_snowflake_queries(*args):
    sf_query_run = SnowflakeOperator(
        secret_cope="sample_scope",
        query_string="select * from table; insert into table1 select * from $database.table2",
        parameters={"database": "sample_db"},
    )
    sf_query_run.execute()


@wf.task
def run_snowflake_files(*args):
    sf_file_run = SnowflakeOperator(
        secret_cope="sample_scope",
        sql_file="src/sql/sample.sql",
        # adjust sql file path relative to your brickflow project path (Ex:examples/brickflow_examples/)
        parameters={"database": "sample_db"},
    )
    sf_file_run.execute()


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


@wf.python_wheel_task(libraries=[PypiTaskLibrary("data-mirror")])
def my_python_wheel_task():
    return PythonWheelTask(
        package_name="data-mirror",
        entry_point="datamirror",
        parameters=["--configuration_file", "dbfs:/path/to/config.json"],
    )


@wf.run_job_task
def run_job_task_a():
    return RunJobTask(job_name="raju_gujjalapati_example_workflow")


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
    )  # type: ignore


@wf.spark_python_task(libraries=[PypiTaskLibrary(package="koheesio")])
def spark_python_task_a():
    return SparkPythonTask(
        python_file="path/to/python/file.py",
        source="GIT",
        parameters=["--param1", "World!"],
    )  # type: ignore


@wf.sql_task(depends_on=start)
def sample_sql_task_query() -> any:
    """
    This function creates a SqlTask with a query_id and warehouse_id.

    Returns:
        SqlTask: A SqlTask object with a query_id and warehouse_id.
    """
    return SqlTask(
        query_id="your_sql_query_id",
        warehouse_id="your_warehouse_id",
    )


@wf.sql_task(depends_on=start)
def sample_sql_task_file() -> any:
    """
    This function creates a SqlTask with a file_path and warehouse_id.

    Returns:
        SqlTask: A SqlTask object with a file_path and warehouse_id.
    """
    if ctx.env == "local":
        my_path = "src/sql/sql_task_file_test.sql"
    else:
        my_path = "products/brickflow_test/src/sql/sql_task_file_test.sql"
    return SqlTask(file_path=my_path, warehouse_id="your_warehouse_id")


@wf.sql_task(depends_on=start)
def sample_sql_alert() -> any:
    """
    This function creates a SqlTask with an alert_id, pause_subscriptions, subscriptions, and warehouse_id.

    Returns:
        SqlTask: A SqlTask object with an alert_id, pause_subscriptions, subscriptions, and warehouse_id.
    """
    return SqlTask(
        alert_id="Your_Alert_ID",
        pause_subscriptions=False,
        subscriptions={"usernames": ["YOUR_USERNAME", "YOUR_USERNAME"]},
        warehouse_id="your_warehouse_id",
    )


@wf.sql_task(depends_on=start)
def sample_sql_dashboard() -> any:
    """
    This function creates a SqlTask with a dashboard_id, dashboard_custom_subject, pause_subscriptions, subscriptions, and warehouse_id.

    Returns:
        SqlTask: A SqlTask object with a dashboard_id, dashboard_custom_subject, pause_subscriptions, subscriptions, and warehouse_id.
    """
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


@wf.if_else_condition_task(depends_on=sample_sql_dashboard)
def sample_condition_task1():
    return IfElseConditionTask(left="1", op="==", right="2")


@wf.if_else_condition_task(
    depends_on=sample_condition_task1,
    name="new_conditon_tasl",
    if_else_outcome={"sample_condition_task1": "true"},
)
def sample_condition_task2():
    return IfElseConditionTask(left="{{job.id}}", op="==", right="{{job.id}}")


@wf.if_else_condition_task(
    depends_on=["sample_condition_task1", "new_conditon_tasl"],
    name="new_conditon_taslq",
    if_else_outcome={"sample_condition_task1": "false", "new_conditon_tasl": "true"},
)
def sample_condition_task4():
    return IfElseConditionTask(left="2", op="==", right="4")


@wf.if_else_condition_task(
    depends_on=["sample_condition_task1", "new_conditon_tasl"],
    name="new_conditon_tasly",
    if_else_outcome={"sample_condition_task1": "true", "new_conditon_tasl": "true"},
)
def sample_condition_task5():
    return IfElseConditionTask(left="2", op="==", right="4")


@wf.task(
    depends_on=sample_condition_task5,
    if_else_outcome={"sample_condition_task5": "true"},
)
def end():
    pass


if __name__ == "__main__":
    # wf.tasks["list_lending_club_data_files"].execute()
    # print(task_function_4())
    # wf.tasks["airflow_external_task_dependency_sensor"].execute()
    wf.tasks["print_sample_lending_club_data"].execute()
