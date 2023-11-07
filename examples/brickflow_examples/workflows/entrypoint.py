# Databricks notebook source

import brickflow
from brickflow import Project, PypiTaskLibrary
import workflows


def main() -> None:
    with Project(
        "brickflow-demo",
        git_repo="https://github.com/Nike-Inc/brickflow",
        provider="github",
        libraries=[
            PypiTaskLibrary(package="spark-expectations==0.8.0"),  # comment if spark-expectations is not needed
        ],
    ) as f:
        f.add_pkg(workflows)


if __name__ == "__main__":
    main()
