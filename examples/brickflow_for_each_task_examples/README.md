# Brickflow for each task examples
This repository contains some examples on how to use the fo each task type in brickflow.

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

### Customize the workflow

Replace all the placeholders in workflows/for_each_task_workflow.py with configuration values compatible with your databricks workspace


### Deploy the workflow to databricks
```shell
brickflow projects deploy --project for_each_task_examples -e local
```

### Run the demo workflow
- login to databricks workspace
- go to the workflows and select the workflow
- click on the run button
