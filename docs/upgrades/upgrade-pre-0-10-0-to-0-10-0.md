## Upgrade checklist

* [x] Update brickflow version to 0.10.0
    ```
    pip install brickflows --upgrade
    bf --version
    ```

* [x] If you are upgrading from a CDKTF version of brickflow then do not worry, the existing workflows as long as you do
  not change their names will be imported.

* [x] Confirm the existence of the following files:

  * brickflow-multi-project.yml
  * brickflow-project-root.yml
  * Please reference [concepts](../../bundles-quickstart/#concepts)
    and [initialize project](../../bundles-quickstart/#initialize-project) for more details.

* [x] RelativePathPackageResolver has been removed from the project to offer a seamless import
  as long as you import brickflow at the top.

* [x] Ensure import for brickflow is at the top of your entrypoint.py

* [x] Ensure import for brickflow is at the top of your entrypoint.py


* [x] Ensure your entrypoint looks like this:

```python linenums="1" hl_lines="5 7 15 18"
# Databricks notebook source

# COMMAND ----------

from brickflow import Project # (1)!

import workflows # (2)!

def main() -> None:
    """Project entrypoint"""
    with Project(
        "product_abc_workflows_2",
        git_repo="https://github.com/stikkireddy/mono-repo-test",
        provider="github",
        libraries=[  # (3)!
            # PypiTaskLibrary(package="spark-expectations==0.5.0"), # Uncomment if spark-expectations is needed
        ],
        enable_plugins=True, # (4)!
    ) as f:
        f.add_pkg(workflows)


if __name__ == "__main__":
    main()
```

1. Make sure brickflow is at the top of your imports! This will help resolve paths and allow other libraries to be
   imported correctly.
2. Import your modules after brickflow has been imported! Make sure your optimize imports doesnt reorder your imports!
3. Make sure you remove brickflow and brickflow plugins and cron utils from this list.
4. Make sure you have enable_plugins=True. This will enable the plugins to be loaded to support airflow operators, etc.
   Disable this if you dont want to install airflow.


