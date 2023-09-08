# brickflow-examples
This repository consists of examples for brickflow

## Getting Started

### Prerequisites
```shell
pip install brickflows
```
### Clone the repository

```shell
git clone https://github.com/Nike-Inc/brickflow.git
cd brickflow/examples/brickflow_examples
```

### Update demo_wf.py
```diff
- library "common-utils-cicd@0.17.0"
+ library "common-utils-cicd@0.17.1"
```


### Deploy the workflow to databricks
```shell
brickflow projects deploy --project brickflow-demo -e local
```