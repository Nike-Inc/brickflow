## Brickflow Overview

The objective of Brickflow is to provide a thin layer on top of databricks workflows to help deploy 
and manage workflows in Databricks. It also provides plugins/extras to be able to run airflow 
operators directly in the workflows.

## Brickflow to Airflow Term Mapping

| Object                                    | Airflow                           | Brickflow                                         |
|-------------------------------------------|-----------------------------------|---------------------------------------------------|
| Collection of Workflows                   | Airflow Cluster (Airflow Dag Bag) | Project/Entrypoint                                |
| Workflow                                  | Airflow Dag                       | Workflow                                          |
| Task                                      | Airflow Operator                  | Task                                              |
| Schedule                                  | Unix Cron                         | Quartz Cron                                       |
| Inter Task Communication                  | XComs                             | Task Values                                       |
| Managing Connections to External Services | Airflow Connections               | Mocked Airflow connections or Databricks Secrets  |
| Variables to Tasks                        | Variables                         | Task Parameters [ctx.get_parameter(key, default)] |
| Context values (execution_date, etc.)     | Airflow Macros, context["ti"]     | ctx.<task parameter\>                             |
