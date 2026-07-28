## Brickflow Overview

The objective of Brickflow is to provide a thin layer on top of databricks workflows to help deploy
and manage workflows in Databricks. Brickflow also ships a set of native (Airflow-free) sensors and
operators for common integrations (remote Airflow, Autosys, Tableau, Snowflake, Box, cross-workflow
dependencies).

!!! note "Airflow dependency removed"

    As of the 2.0 version (Airflow-free) release, brickflow no longer requires `apache-airflow`. The Airflow-based
    `BashOperator`, `BranchPythonOperator`, `ShortCircuitOperator`, `TaskDependencySensor`,
    `AirflowProxyOktaClusterAuth`, and `BrickflowSecretsBackend` have been removed. See the
    [pre-0.10.0 upgrade guide](upgrades/upgrade-pre-0-10-0-to-0-10-0.md) for migration details.

## Brickflow to Airflow Term Mapping

| Object                                    | Airflow                           | Brickflow                                         |
|-------------------------------------------|-----------------------------------|---------------------------------------------------|
| Collection of Workflows                   | Airflow Cluster (Airflow Dag Bag) | Project/Entrypoint                                |
| Workflow                                  | Airflow Dag                       | Workflow                                          |
| Task                                      | Airflow Operator                  | Task                                              |
| Schedule                                  | Unix Cron                         | Quartz Cron                                       |
| Inter Task Communication                  | XComs                             | Task Values                                       |
| Managing Connections to External Services | Airflow Connections               | Databricks Secrets                                |
| Variables to Tasks                        | Variables                         | Task Parameters [ctx.get_parameter(key, default)] |
| Context values (execution_date, etc.)     | Airflow Macros, context["ti"]     | ctx.<task parameter\>                             |
