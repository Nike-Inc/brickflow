import logging as log
from pathlib import Path
from brickflow.engine.utils import get_bf_project_root

try:
    import snowflake.connector
except ImportError:
    raise ImportError(
        """You must install snowflake library to use run snowflake plugins, please add - 'snowflake' library either
         at project level in entrypoint or at workflow level or at task level. Examples shown below 
        entrypoint:
            with Project( ... 
                          libraries=[PypiTaskLibrary(package="snowflake==0.6.0")]
                          ...)
        workflow:
            wf=Workflow( ...
                         libraries=[PypiTaskLibrary(package="snowflake==0.6.0")]
                         ...)
        Task:
            @wf.task(Library=[PypiTaskLibrary(package="snowflake==0.6.0")]
            def run_snowflake_queries(*args):
                ...
        """
    )

try:
    from brickflow import ctx
except ImportError:
    raise ImportError(
        "plugin requires brickflow context , please install library at cluster/workflow/task level"
    )


class SnowflakeOperatorException(Exception):
    pass


class SnowflakeOperatorTimeOutException(TimeoutError):
    pass


class SnowflakeOperator:
    """
    This is used to run any sql query in snowflake environment

    Example Usage in your brickflow task
    SnowflakeOperator(
    secret_scope=databricks_secrets_psc
    query_string=queries separated by semicolon
    )

    As databricks secrets is a key value store, code expects the secret scope to contain the below exact keys
    username : user id created for connecting to snowflake for ex: sample_user
    password : password information for about user for ex: P@$$word
    account  : snowflake account information, not entire url for ex: sample_enterprise
    warehouse: warehouse/cluster information that user has access for ex: sample_warehouse
    database : default database that we want to connect for ex: sample_database
    role     : role to which the user has write access for ex: sample_write_role

    In above snippet secret_scope refers to databricks secrets secure service to store the snowflake credentials.
       Support for other stores will be added as a future enhancement

    above code snippet expects the data as follows
    databricks_secrets_psc contains username, password, account, warehouse, database and role keys with snowflake values
    query_string : Optional parameter with queries separeted by semicolon(;)
    sql_file : Optional parameter with file path (relative to brickflow project root) to .sql file
    parameters: optional parameter dictionary with key value pairs to substitute in the query
    """

    def __init__(
        self,
        secret_scope,
        query_string=None,
        sql_file=None,
        parameters={},
        *args,
        **kwargs,
    ):
        self.cur = None
        self.query = None
        self.sql_file = None
        self.secret_scope = secret_scope
        self.log = log
        self.query = query_string
        self.parameters = parameters
        self.sql_file = sql_file
        self.brickflow_root = get_bf_project_root()

        if query_string is not None and sql_file is not None:
            raise ValueError("Cannot specify both sql_file and query_string !")
        if not self.secret_scope:
            raise ValueError(
                "Must provide reference to Snowflake connection in databricks secretes !"
            )

        try:
            self.authenticator = ctx.dbutils.secrets.get(
                self.secret_scope, "authenticator"
            )
        except:
            self.authenticator = None

        try:
            self.username = ctx.dbutils.secrets.get(self.secret_scope, "username")
            self.password = ctx.dbutils.secrets.get(self.secret_scope, "password")
            self.account = ctx.dbutils.secrets.get(self.secret_scope, "account")
            self.warehouse = ctx.dbutils.secrets.get(self.secret_scope, "warehouse")
            self.database = ctx.dbutils.secrets.get(self.secret_scope, "database")
            self.role = ctx.dbutils.secrets.get(self.secret_scope, "role")
        except:
            raise ValueError(
                "Failed to fetch details from secret scope for username, password, account, warehouse, \
                             database, role  !"
            )

    def get_snowflake_connection(self):
        """
        logic to connect to snowflake instance with provided details and return a connection object
        """
        if self.authenticator is not None:
            self.log.info(
                "snowflake_account_name={0}, database={1}, username={2}, warehouse={3}, role={4}, authenticator={5}".format(
                    self.account,
                    self.database,
                    self.username,
                    self.warehouse,
                    self.role,
                    self.authenticator,
                )
            )
            con = snowflake.connector.connect(
                user=self.username,
                password=self.password,
                account=self.account,
                warehouse=self.warehouse,
                database=self.database,
                role=self.role,
                authenticator=self.authenticator,
            )
        else:
            self.log.info(
                "snowflake_account_name={0}, database={1}, username={2}, warehouse={3}, role={4}".format(
                    self.account,
                    self.database,
                    self.username,
                    self.warehouse,
                    self.role,
                )
            )
            con = snowflake.connector.connect(
                user=self.username,
                password=self.password,
                account=self.account,
                warehouse=self.warehouse,
                database=self.database,
                role=self.role,
            )

        self.parameters.update(
            {
                "account_name": self.account,
                "database": self.database,
                "username": self.username,
                "warehouse": self.warehouse,
                "role": self.role,
            }
        )

        return con

    def read_sql_file(self):
        """
        logic to read the sql file and return the query string
        """
        try:
            if self.sql_file is not None:
                sql_loc = Path(self.sql_file)
                sql_path = self.brickflow_root / sql_loc
                if not sql_path.exists():
                    raise FileNotFoundError(
                        f"Unable to locate specified {sql_path.as_posix()}"
                    )
                self.query = sql_path.read_text(encoding="utf-8")
                return self
            if self.query is None or len(self.query) == 0:
                raise ValueError("SQL Query is empty")
            return self
        except Exception as e:
            self.log.error("Failed to read the sql file")
            raise ValueError("Failed to read the sql file")

    def get_cursor(self):
        """
        logic to create a cursor for a successful snowflake connection to execute queries
        """
        try:
            self.log.info(
                "establishing connection for secret scope id {}".format(
                    self.secret_scope
                )
            )
            con = self.get_snowflake_connection()
        except snowflake.connector.errors.ProgrammingError as e:
            raise ValueError(
                "Error {0} ({1}): {2} ({3})".format(e.errno, e.sqlstate, e.msg, e.sfqid)
            )
        self.cur = con.cursor()

    def snowflake_query_exec(self, cur, database, query_string):
        """
        Executes the snowflake query(ies) by replacing varibales with appropriate values
        """
        for key, value in self.parameters.items():
            if isinstance(key, str) and isinstance(value, str):
                query_string = query_string.replace("$" + key, value)
            if isinstance(key, str) and isinstance(value, list):
                # just to be on safer side and avoid unwanted failure here added another check
                # specifically for incremental filter
                is_filter_check = lambda x: (len(x) == 3) and isinstance(x, tuple)
                if list(filter(is_filter_check, value)) == value:
                    new_string_filter = ""
                    string_filter = ["{}{}'{}'".format(t[0], t[1], t[2]) for t in value]

                    for i, _filter in enumerate(string_filter):
                        new_string_filter += _filter
                        if i == len(value) - 1:
                            continue
                        else:
                            new_string_filter += " and "
                    query_string = query_string.replace("$" + key, new_string_filter)

        sql_statements = query_string.split(";")
        self.log.info("SQL queries are parsed out")

        cur.execute("use " + database)
        self.log.info("Database Connected is {0}".format(database))

        for sql_qry in sql_statements:
            self.log.info("Query to be executed is {0}".format(sql_qry))
            if sql_qry is not None and len(sql_qry) > 1:
                try:
                    cur.execute(sql_qry)
                except snowflake.connector.errors.ProgrammingError as e:
                    # default error message
                    self.log.warning(e)
                    # customer error message
                    raise ValueError(
                        "Error {0} ({1}): {2} ({3})".format(
                            e.errno, e.sqlstate, e.msg, e.sfqid
                        )
                    )
            self.log.info("Query completed successfully")
        self.log.info("All Query/Queries completed successfully")

    def execute(self):
        """
        logic that triggers the flow of events
        """
        if self.sql_file is not None:
            self.read_sql_file()
        self.log.info("Executing SQL Query: " + str(self.query))
        self.get_cursor()
        query_string = str(self.query).strip()
        # Run the query against SnowFlake
        try:
            self.snowflake_query_exec(self.cur, self.database, self.query)
        except:
            self.log.error("failed to execute")
        finally:
            self.cur.close()
            self.log.info("Closed connection")


class UcToSnowflakeOperatorException(Exception):
    pass


class UcToSnowflakeOperatorTimeOutException(TimeoutError):
    pass


class UcToSnowflakeOperator(SnowflakeOperator):
    """
    This is used to copy data from unity catalpg table to a snowflake table

    Example Usage in your brickflow task
    UcToSnowflakeOperator(
    secret_scope=databricks_secrets_psc,
    parameters= uc_parameters
    )

    In above snippet secret_scope refers to databricks secrets secure service to store the snowflake credentials.
       Support for other stores will be added as a future enhancement

    As databricks secrets is a key value store, code expects the secret scope to contain the below exact keys
    username : user id created for connecting to snowflake for ex: sample_user
    password : password information for about user for ex: P@$$word
    account  : snowflake account information, not entire url for ex: sample_enterprise
    warehouse: warehouse/cluster information that user has access for ex: sample_warehouse
    database : default database that we want to connect for ex: sample_database
    role     : role to which the user has write access for ex: sample_write_role
    Authenticator: optional additional authenticator needed for connection for ex: okta_connection_url

    above code snippet expects the data as follows
    databricks_secrets_psc contains username, password, account, warehouse, database and role keys with snowflake values
    parameters = {'load_type':'incremental','dbx_catalog':'sample_catalog','dbx_database':'sample_schema',
                      'dbx_table':'sf_operator_1', 'sf_schema':'stage','sf_table':'SF_OPERATOR_1',
                      'sf_grantee_roles':'downstream_read_role', 'incremental_filter':"dt='2023-10-22'",
                      'sf_cluster_keys':''
                      'dbx_sql':'select * from sample_catalog.sample_schema.sf_operator_1 where dt='2023-10-22'}

    in the parameters dictionary we have mandatory keys as follows
    load_type(required): incremental/full
    dbx_catalog (required): name of the catalog in unity
    dbx_database  (required): schema name within the catalog
    dbx_table   (required): name of the object in the schema
    sf_database (optional): database name in snowflake
    sf_schema   (required): snowflake schema in the database provided as part of scope
    sf_table    (required): name of the table in snowflake to which we want to append or overwrite
    incremental_filter (optional): mandatory parameter for incremental load type to delete existing data in snowflake table
    dbx_data_filter (optional): parameter to filter databricks table if different from snowflake filter
    sf_cluster_keys (optional): list of keys to cluster the data in snowflake
    dbx_sql (optional): sql query to extract data from unity catalog

    One of dbx_sql or dbx_catalog, dbx_database, dbx_table should be provided
    If custom sql is mentioned in db_sql, for incremental process make sure to include to write_mode or adjust incremental filter in the Operator to align with custom sql
    if not, there could be duplicates in Snowflake table

    """

    def __init__(self, secret_scope, parameters={}, write_mode=None, *args, **kwargs):
        super().__init__(secret_scope, *args, **kwargs)
        self.parameters = parameters
        self.dbx_data_filter = self.parameters.get("dbx_data_filter") or None
        self.dbx_sql = self.parameters.get("dbx_sql") or None
        self.write_mode = write_mode
        """
        self.authenticator = None
        try:
            import base64
            from brickflow import ctx

            self.username = ctx.dbutils.secrets.get(self.secret_scope, "username")
            self.password = ctx.dbutils.secrets.get(self.secret_scope, "password")
            self.account = ctx.dbutils.secrets.get(self.secret_scope, "account")
            self.warehouse = ctx.dbutils.secrets.get(self.secret_scope, "warehouse")
            self.database = ctx.dbutils.secrets.get(self.secret_scope, "database")
            self.role = ctx.dbutils.secrets.get(self.secret_scope, "role")
        except:
            raise ValueError(
                "Failed to fetch details from secret scope for username, password, account, warehouse, \
                             database, role  !"
            )
        """

    def get_sf_presteps(self):
        queries = """  
                     CREATE OR REPLACE TABLE {sfDatabase}.{sfSchema}.{sfTable_clone} CLONE {sfDatabase}.{sfSchema}.{sfTable};
                     DELETE FROM {sfDatabase}.{sfSchema}.{sfTable_clone} WHERE {data_filter}""".format(
            sfSchema=self.parameters["sf_schema"],
            sfTable_clone=self.parameters["sf_table"] + "_clone",
            sfTable=self.parameters["sf_table"],
            sfDatabase=self.sf_database,
            data_filter=self.parameters["incremental_filter"],
        )
        return queries

    def get_sf_poststeps(self):
        queries = """ ALTER TABLE {sfDatabase}.{sfSchema}.{sfTable_clone} SWAP WITH {sfDatabase}.{sfSchema}.{sfTable}; 
                      DROP TABLE {sfDatabase}.{sfSchema}.{sfTable_clone} """.format(
            sfSchema=self.parameters["sf_schema"],
            sfTable_clone=self.parameters["sf_table"] + "_clone",
            sfTable=self.parameters["sf_table"],
            sfDatabase=self.sf_database,
        )
        return queries

    def get_sf_postgrants(self):
        post_grantee_role = (
            self.parameters["sf_grantee_roles"]
            if "sf_grantee_roles" in self.parameters.keys()
            else self.role
        )
        queries = """ GRANT SELECT ON TABLE {sfDatabase}.{sfSchema}.{sfTable} TO ROLE {sfGrantee_roles};""".format(
            sfSchema=self.parameters["sf_schema"],
            sfTable=self.parameters["sf_table"],
            sfGrantee_roles=post_grantee_role,
            sfDatabase=self.sf_database,
        )
        return queries

    def validate_input_params(self):
        """
        Function to validate the input parameters
        """
        if isinstance(self.parameters, dict):
            # Setup the mandatory params for snowflake load
            mandatory_keys = (
                "load_type",
                "sf_schema",
                "sf_table",
            )
            if self.dbx_sql is not None:
                mandatory_keys = mandatory_keys + ("dbx_sql",)
            else:
                mandatory_keys = mandatory_keys + (
                    "dbx_catalog",
                    "dbx_database",
                    "dbx_table",
                )
            if not all(key in self.parameters for key in mandatory_keys):
                self.log.info(
                    "Mandatory keys for UcToSnowflakeOperator(parameters): %s\n"
                    % format(mandatory_keys)
                )
                self.log.error(
                    "Mandatory key(s) NOT exists in UcToSnowflakeOperator(parameters): %s\n"
                    % format(self.parameters)
                )
                raise Exception("Job failed due to missing manadatory key")
            # Setting up pre,post and grants scripts for snowflake
            self.sf_post_grants_sql = self.get_sf_postgrants()

            if self.parameters["load_type"] == "incremental":
                if "incremental_filter" not in self.parameters.keys():
                    self.log.info(
                        "manadatory key incremntal_filter is missing for incremntal loads"
                    )
                    self.log.error(
                        "manadatory key incremntal_filter is missing for incremntal loads"
                    )
                    raise Exception("Job failed due to missing manadatory key")
                self.sf_pre_steps_sql = self.get_sf_presteps()
                self.sf_post_steps_sql = self.get_sf_poststeps()

        else:
            self.log.error("Input is NOT a dictionary: %s\n" % format(self.parameters))
            raise Exception("Job failed due to missing manadatory key")

    def submit_job_snowflake(self, query_input):
        """
        Function to establish snowflake connection
        and submit commands for execution
        """
        try:
            self.get_snowflake_connection()
            self.get_cursor()
            query_string_list = str(query_input).strip().split(";")
            for query_string in query_string_list:
                self.log.info(query_string)
                self.snowflake_query_exec(self.cur, self.database, query_string.strip())

        except Exception as e:
            self.log.info(e)
            self.cur.close()
            raise Exception("Snowflake step Failed, Job failed")
        finally:
            self.cur.close()

    def apply_grants(self):
        """
        Function to apply grants after successful execution
        """
        grantee_roles = self.parameters.get("sf_grantee_roles") or self.role
        for grantee_role in grantee_roles.split(","):
            self.parameters.update({"sf_grantee_roles": grantee_role})
            self.submit_job_snowflake(self.sf_post_grants_sql)

    def extract_source(self):
        if self.dbx_sql is not None:
            self.log.info(
                f"Executing Custom sql to extract data from Unity catalog. Query -: {self.dbx_sql}"
            )
            df = ctx.spark.sql(self.dbx_sql)
            return df
        else:
            if self.parameters["load_type"] == "incremental":
                self.dbx_data_filter = (
                    self.parameters.get("dbx_data_filter")
                    or self.parameters.get("incremental_filter")
                    or "1=1"
                )
            else:
                self.dbx_data_filter = self.parameters.get("dbx_data_filter") or "1=1"

            df = ctx.spark.sql(
                """select * from {}.{}.{} where {}""".format(
                    self.parameters["dbx_catalog"],
                    self.parameters["dbx_database"],
                    self.parameters["dbx_table"],
                    self.dbx_data_filter,
                )
            )
            return df

    def load_snowflake(self, source_df, target_table):
        sf_package = "net.snowflake.spark.snowflake"
        sf_url = "{}.snowflakecomputing.com".format(self.account)
        sf_options = {
            "sfURL": sf_url,
            "sfUser": self.username,
            "sfPassword": self.password,
            "sfWarehouse": self.warehouse,
            "sfDatabase": self.sf_database,
            "sfSchema": self.parameters["sf_schema"],
            "sfRole": self.role,
        }
        if self.authenticator is not None:
            sf_options["sfAuthenticator"] = self.authenticator
        self.log.info("snowflake package and options defined...!!!")
        if len(source_df.take(1)) == 0:
            self.write_mode = "Append"
        if len(self.sf_cluster_keys) == 0:
            # Without order by clause compared to above
            source_df.write.format(sf_package).options(**sf_options).option(
                "dbtable",
                "{0}.{1}.{2}".format(
                    self.sf_database, self.parameters["sf_schema"], target_table
                ),
            ).mode("{0}".format(self.write_mode)).save()

        elif len(self.sf_cluster_keys) > 0:
            # Included order by clause compared to above
            source_df.orderBy(self.sf_cluster_keys).write.format(sf_package).options(
                **sf_options
            ).option(
                "dbtable",
                "{0}.{1}.{2}".format(
                    self.sf_database, self.parameters["sf_schema"], target_table
                ),
            ).mode(
                "{0}".format(self.write_mode)
            ).save()

    def submit_job_compute(self):
        self.log.info("extracting data from databricks")
        target_table = (
            self.parameters["sf_table"] + "_clone"
            if self.parameters["load_type"].lower() == "incremental"
            else self.parameters["sf_table"]
        )
        source_data = self.extract_source()
        if self.write_mode is None:
            self.write_mode = (
                "Overwrite" if self.parameters["load_type"] == "full" else "Append"
            )
        self.sf_cluster_keys = (
            []
            if "sf_cluster_keys" not in self.parameters.keys()
            else self.parameters["sf_cluster_keys"]
        )
        self.log.info("loading data to snowflake table")
        self.load_snowflake(source_data, target_table)
        self.log.info("successfully loaded data to snowflake table ")

    def execute(self):
        """
        Main method for execution
        """
        # Validate the input parameters
        self.sf_database = self.parameters.get("sf_database") or self.database
        self.validate_input_params()

        # Identify the execution environment
        self.log.info(self.parameters)
        self.log.info(self.parameters.get("load_type").lower())
        # Perform action based on the load type
        if self.parameters.get("load_type").lower() == "incremental":
            self.log.info("Incremental Load Type Requested")
            # Snowflake Presteps execution
            self.submit_job_snowflake(self.sf_pre_steps_sql)
            self.log.info("Snowflake pre-steps execution succeeded")
            # Calling the spark job to load into snowflake table
            self.submit_job_compute()
            # Snowflake Poststeps execution
            self.submit_job_snowflake(self.sf_post_steps_sql)
            self.apply_grants()
            self.log.info("Snowflake post-steps execution succeeded")

        elif self.parameters.get("load_type").lower() == "full":
            self.log.info("Full Load Type Requested")
            self.submit_job_compute()
            self.apply_grants()

        else:
            raise Exception(
                "NOT a supported value for load_type: %s \n please provide either full or incremental"
                % format(self.parameters.get("load_type"))
            )
