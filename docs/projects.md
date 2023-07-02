The project is similar to a map cluster it can be composed of various different Workflows or dags.


Here is an example of an entrypoint. 
Click the plus buttons to understand all the parts of the entrypoint file.

```python title="entrypoint.py"
# Databricks notebook source  # (1)!

import examples.brickflow_examples.workflows

from brickflow import Project, PypiTaskLibrary, MavenTaskLibrary

ARTIFACTORY = ""


def main() -> None:
    """Project entrypoint"""
    with Project(
            "brickflow-demo",  # (3)!
            git_repo="https://github.com/Nike-Inc/brickflow",  # (4)!
            provider="github",  # (5)!
            libraries=[  # (6)!
                PypiTaskLibrary(package="brickflow==1.0.0 --extra-index-url " + ARTIFACTORY),
                MavenTaskLibrary(coordinates="com.cronutils:cron-utils:9.2.0"),
            ],
    ) as f:
        f.add_pkg(examples.brickflow_examples.workflows)  # (7)!


if __name__ == "__main__":  # (2)!
    main()
```


1. Uploading this Python file into databricks with this comment on the first line treats the python file
    as a notebook.
2. This makes sure this only runs when this file is run via python entrypoint.py
3. This is the project name you provided when you do `bf init`
4. This is the git repo that is introspected when running `bf init`
5. This is the github provider that you decide on.
6. You can provide a list of packages that need to be installed in all of your clusters when running ETL.
7. You can add multiple packages in your project where you are defining workflows.