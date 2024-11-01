# Databricks notebook source
# This should point to the `brickflows` version with serverless support or the wheel file with the same
# MAGIC %pip install brickflows==1.2.1
# MAGIC %pip install koheesio==0.8.1
# MAGIC %restart_python

# COMMAND ----------
import brickflow
from brickflow import Project, PypiTaskLibrary
import workflows


def main() -> None:
    with Project(
        "brickflow-serverless-demo",
        git_repo="https://github.com/Nike-Inc/brickflow",
        provider="github",
    ) as f:
        f.add_pkg(workflows)


if __name__ == "__main__":
    main()
