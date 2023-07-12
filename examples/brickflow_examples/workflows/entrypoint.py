# Databricks notebook source

import resolver
import workflows

from brickflow import Project, PypiTaskLibrary, MavenTaskLibrary

ARTIFACTORY = ""


def main() -> None:
    """Project entrypoint"""
    with Project(
        "brickflow-demo",
        git_repo="https://github.com/Nike-Inc/brickflow",
        provider="github",
        libraries=[
            PypiTaskLibrary(
                package="brickflow==1.0.0 --extra-index-url " + ARTIFACTORY
            ),
            MavenTaskLibrary(coordinates="com.cronutils:cron-utils:9.2.0"),
        ],
    ) as f:
        f.add_pkg(workflows)


if __name__ == "__main__":
    main()
