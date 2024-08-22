---
hide:
  - toc
---

## Environment Variables


| Environment Variable                   | Default Value                                  | Description                                                                                                      |
|----------------------------------------|------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| BRICKFLOW_ENV                          | local                                          | The environment name for Brickflow                                                                               |
| BRICKFLOW_GIT_REPO                     | N/A                                            | The URL of the Git repository for Brickflow                                                                      |
| BRICKFLOW_GIT_REF                      | N/A                                            | The Git reference (branch, tag, commit) for Brickflow                                                            |
| BRICKFLOW_GIT_PROVIDER                 | github                                         | The Git provider (e.g., GitHub, GitLab) for Brickflow                                                            |
| DATABRICKS_CONFIG_PROFILE              | default                                        | The profile name for Databricks configuration                                                                    |
| BRICKFLOW_DEPLOY_ONLY_WORKFLOWS        | N/A                                            | List of workflows seperated by "," (e.g. wf1,wf2) to deploy exclusively                                          |
| BRICKFLOW_WORKFLOW_PREFIX              | N/A                                            | Prefix to add to workflow names during deployment                                                                |
| BRICKFLOW_WORKFLOW_SUFFIX              | N/A                                            | Suffix to add to workflow names during deployment                                                                |
| BRICKFLOW_INTERACTIVE_MODE             | True                                           | Flag indicating whether to enable interactive mode                                                               |
| BRICKFLOW_BUNDLE_BASE_PATH             | /Users/<br/>${workspace.current_user.userName} | The base path for the bundle in the S3 backend                                                                   |
| BRICKFLOW_BUNDLE_OBJ_NAME              | .brickflow_bundles                             | The name of the folder post appended to your base path                                                           |
| BRICKFLOW_BUNDLE_CLI_EXEC              | databricks                                     | The executable command for bundle execution. By default it will be downloaded on the fly.                        |
| BRICKFLOW_BUNDLE_NO_DOWNLOAD           | False                                          | Flag indicating whether to skip downloading the databricks bundle cli. Useful if you are in locked down network. |
| BRICKFLOW_BUNDLE_CLI_VERSION           | 0.200.0                                        | The version of the bundle CLI tool                                                                               |
| BRICKFLOW_MONOREPO_PATH_TO_BUNDLE_ROOT | N/A                                            | The path to the bundle root directory in a monorepo. Default assumes you are not using a monorepo                |
| BRICKFLOW_PROJECT_PARAMS               | N/A                                            | Runtime/Deployment time parameters seperated by "," (e.g. k1=v1,k2=v2) to pass to workflow tasks                 |

# Runtime project parameters

This allows for passing runtime parameters to the workflow tasks for given project.

### Environment Variable
The parameters are passed as a comma separated list when setting through environment variable.
The key-value pairs are separated by an equal sign.

```shell
export BRICKFLOW_PROJECT_PARAMS="key1=value1,key2=value2"
bf projects deploy -p DEFAULT -e local
```

### CLI

Provide the runtime key-value parameters, each key-value separated by space when using CLI.

```shell
bf projects deploy -p DEFAULT -e local -kv key1=value1 -kv key2=value2
```

### Accessing the parameters in the workflow tasks

The parameters can be accessed in the workflow tasks using the brickflow context object.

```python
from brickflow.context import ctx
ctx.get_project_parameter("key1") ## returns value1
ctx.get_project_parameter("key2") ## returns value2
```


# Workflow prefixing or suffixing

This allows for adding suffixes or prefixes in the name of the workflow:

* **BRICKFLOW_WORKFLOW_PREFIX**
* **BRICKFLOW_WORKFLOW_SUFFIX**

Setting the above is semantically the same as doing this in code:

```python

wf = Workflow(
    "thanks",
    prefix="so_long_",  # same as BRICKFLOW_WORKFLOW_PREFIX
    suffix="_and_thanks_for_all_the_fish"  # same as BRICKFLOW_WORKFLOW_SUFFIX
)
```

`wf.name` would then result in "so_long_and_thanks_for_all_the_fish"

this is to allow 'unique' names while deploying the same workflow to same environments while still needing to keep them
separate.

For example, consider this scenario:

- You have a workflow named `inventory_upsert`;
- Two features are being developed on in parallel in the DEV environment, let's name these `feature_1` and `feature_2`;
- If you don't have the ability to uniquely set the name for a workflow, the workflow you are creating in dev (no matter
  in which feature/branch they originate from) will always be named `dev_inventory_upsert`;
- with using the prefix/suffix mechanism, we can set a ENV variable and end up with unique names for each feature,
  i.e. `dev_inventory_upsert_feature_1` and `dev_inventory_upsert_feature_2`.

Ideal usage for this is in CI/CD pipelines.
