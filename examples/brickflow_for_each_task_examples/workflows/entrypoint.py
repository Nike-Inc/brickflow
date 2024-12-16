# Databricks notebook source

import brickflow
from brickflow import Project
import workflows


def main() -> None:
    with Project(
        "for_each_task_examples",
        git_repo="https://github.com/Nike-Inc/brickflow",
        provider="github",
    ) as f:
        f.add_pkg(workflows)


if __name__ == "__main__":
    main()
