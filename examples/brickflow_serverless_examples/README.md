# Brickflows Serverless Example
This project contains the example of the serverless workflow, that contains:
- notebook task
- python task
- native Brickflow entrypoint task

Note that in notebook task and entrypoint task the dependencies are set through magic `pip install` commands within
the notebook.

## Getting Started

### Prerequisites
1.Install brickflows

```shell
pip install brickflows
```

2.Install [Databricks CLI](https://docs.databricks.com/en/dev-tools/cli/databricks-cli.html)

    ```shell
    curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sudo sh
    ```

3.Configure Databricks cli with workspace token. This configures your `~/.databrickscfg` file.

    ```shell
    databricks configure --token
    ```

### Clone the repository

```shell
git clone https://github.com/Nike-Inc/brickflow.git
cd brickflow/examples/brickflow_serverless_examples
```

### Deploy the workflow to databricks
```shell
brickflow projects deploy --project brickflow-serverless-demo -e local
```

### Run the demo workflow
- login to databricks workspace
- go to the workflows and select the workflow
- click on the run button
