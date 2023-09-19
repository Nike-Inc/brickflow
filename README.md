# Brickflow

[//]: # ([![CodeQL]&#40;https://github.com/Nike-Inc/brickflow/actions/workflows/codeql-analysis.yml/badge.svg&#41;]&#40;https://github.com/Nike-Inc/brickflow/actions/workflows/codeql-analysis.yml&#41;)
[![build](https://github.com/Nike-Inc/brickflow/actions/workflows/onpush.yml/badge.svg)](https://github.com/Nike-Inc/brickflow/actions/workflows/onpush.yml)
[![codecov](https://codecov.io/gh/Nike-Inc/brickflow/branch/main/graph/badge.svg)](https://codecov.io/gh/Nike-Inc/brickflow)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![PYPI version](https://img.shields.io/pypi/v/brickflows.svg)
![PYPI - Downloads](https://static.pepy.tech/badge/brickflows)
![PYPI - Python Version](https://img.shields.io/pypi/pyversions/brickflows.svg)

<p align="center">
BrickFlow is specifically designed to enable the development of Databricks workflows using Python, streamlining the 
process through a command-line interface (CLI) tool.</p>

<p align="center">
<img src=https://raw.githubusercontent.com/Nike-Inc/brickflow/master/docs/img/bf_logo_1.png width="400" height="400"></p>

---

### Contributors

Thanks to all the [contributors](https://github.com/Nike-Inc/brickflow/blob/main/CONTRIBUTORS.md) who have helped ideate, develop and bring Brickflow to its current state. 

### Contributing

We're delighted that you're interested in contributing to our project! To get started, 
please carefully read and follow the guidelines provided in our [contributing](https://github.com/Nike-Inc/brickflow/blob/main/CONTRIBUTING.md) document.

### Documentation

Brickflow documentation can be found [here](https://engineering.nike.com/brickflow/).

### Getting Started

#### Prerequisites
1. Install brickflows

```shell
pip install brickflows
```

2. Install [Databricks CLI](https://docs.databricks.com/en/dev-tools/cli/databricks-cli.html)

```shell
curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sudo sh
```

3. Configure Databricks cli with workspace token. This configures your `~/.databrickscfg` file.

```shell
databricks configure --token
```

#### Hello World workflow
1. Create your first workflow using brickflow
```shell
mkdir hello-world-brickflow
cd hello-world-brickflow
brickflow projects add
```

2. Provide the following inputs
```shell
Project name: hello-world-brickflow
Path from repo root to project root (optional) [.]: .
Path from project root to workflows dir: workflows
Git https url: https://github.com/Nike-Inc/brickflow.git
Brickflow version [auto]:<hit enter>
Spark expectations version [0.5.0]: 0.8.0
Skip entrypoint [y/N]: N
```
_Note: You can provide your own github repo url._

3. Create a new file hello_world_wf.py in the workflows directory
```shell
touch workflows/hello_world_wf.py
```

4. Copy the following code in hello_world_wf.py file
```python
from brickflow import (
    ctx,
    Cluster,
    Workflow,
    NotebookTask,
)
from airflow.operators.bash import BashOperator


cluster = Cluster(
    name="job_cluster",
    node_type_id="m6gd.xlarge",
    spark_version="13.3.x-scala2.12",
    min_workers=1,
    max_workers=2,
)

wf = Workflow(
    "hello_world_workflow",
    default_cluster=cluster,
    tags={
        "product_id": "brickflow_demo",
    },
    common_task_parameters={
        "catalog": "<uc-catalog-name>",
        "database": "<uc-schema-name>",
    },
)

@wf.task
# this task does nothing but explains the use of context object
def start():
    print(f"Environment: {ctx.env}")

@wf.notebook_task
# this task runs a databricks notebook
def example_notebook():
    return NotebookTask(
        notebook_path="notebooks/example_notebook.py",
        base_parameters={
            "some_parameter": "some_value",  # in the notebook access these via dbutils.widgets.get("some_parameter")
        },
    )


@wf.task(depends_on=[start, example_notebook])
# this task runs a bash command
def list_lending_club_data_files():
    return BashOperator(
        task_id=list_lending_club_data_files.__name__,
        bash_command="ls -lrt /dbfs/databricks-datasets/samples/lending_club/parquet/",
    )

@wf.task(depends_on=list_lending_club_data_files)
# this task runs the pyspark code
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
```
_Note: Modify the values of catalog/database for common_task_parameters._


5. Create a new file example_notebook.py in the notebooks directory
```shell
mkdir notebooks
touch notebooks/example_notebook.py
```
6. Copy the following code in the example_notebook.py file
```python
# Databricks notebook source

print("hello world")
```

#### Deploy the workflow to databricks
```shell
brickflow projects deploy --project hello-world-brickflow -e local
```

### Run the demo workflow
1. Login to databricks workspace
2. Go to the workflows and select the workflow
<p align="center">
<img src=https://raw.githubusercontent.com/Nike-Inc/brickflow/master/docs/img/workflow.png?raw=true width=1000></p>
4. click on the run button

### Examples
Refer to the [examples](https://github.com/Nike-Inc/brickflow/tree/main/examples/brickflow_examples) for more examples.


