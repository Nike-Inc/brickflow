---
hide:
  - toc
---

## Environment Variables

### Note: CDKTF is deprecated please keep in mind as you read the list

| Environment Variable                   | Default Value                                  | Deploment Mode Support          | Description                                                                                                      |
|----------------------------------------|------------------------------------------------|---------------------------------|------------------------------------------------------------------------------------------------------------------|
| BRICKFLOW_ENV                          | local                                          | bundle & cdktf (**deprecated**) | The environment name for Brickflow                                                                               |
| BRICKFLOW_FORCE_DEPLOY                 | False                                          | cdktf (**deprecated**)          | Flag indicating whether to force deployment                                                                      |
| BRICKFLOW_DEPLOYMENT_MODE              | cdktf (**deprecated**)                         | bundle & cdktf (**deprecated**) | The deployment mode for Brickflow (cdktf, bundles)                                                               |
| BRICKFLOW_GIT_REPO                     | N/A                                            | bundle & cdktf (**deprecated**) | The URL of the Git repository for Brickflow                                                                      |
| BRICKFLOW_GIT_REF                      | N/A                                            | bundle & cdktf (**deprecated**) | The Git reference (branch, tag, commit) for Brickflow                                                            |
| BRICKFLOW_GIT_PROVIDER                 | github                                         | bundle & cdktf (**deprecated**) | The Git provider (e.g., GitHub, GitLab) for Brickflow                                                            |
| DATABRICKS_CONFIG_PROFILE              | default                                        | bundle & cdktf (**deprecated**) | The profile name for Databricks configuration                                                                    |
| BRICKFLOW_DEPLOY_ONLY_WORKFLOWS        | N/A                                            | bundle & cdktf (**deprecated**) | List of workflows to deploy exclusively                                                                          |
| BRICKFLOW_WORKFLOW_PREFIX              | N/A                                            | bundle & cdktf (**deprecated**) | Prefix to add to workflow names during deployment                                                                |
| BRICKFLOW_WORKFLOW_SUFFIX              | N/A                                            | bundle & cdktf (**deprecated**) | Suffix to add to workflow names during deployment                                                                |
| BRICKFLOW_S3_BACKEND_BUCKET            | N/A                                            | cdktf (**deprecated**)          | The name of the S3 bucket for Brickflow backend                                                                  |
| BRICKFLOW_S3_BACKEND_KEY               | N/A                                            | cdktf (**deprecated**)          | The key or path in the S3 bucket for Brickflow backend                                                           |
| BRICKFLOW_S3_BACKEND_REGION            | N/A                                            | cdktf (**deprecated**)          | The AWS region for the S3 backend                                                                                |
| BRICKFLOW_S3_BACKEND_DYNAMODB_TABLE    | N/A                                            | cdktf (**deprecated**)          | The DynamoDB table name for tracking S3 backend                                                                  |
| BRICKFLOW_INTERACTIVE_MODE             | True                                           | bundle & cdktf (**deprecated**) | Flag indicating whether to enable interactive mode                                                               |
| BRICKFLOW_BUNDLE_BASE_PATH             | /Users/<br/>${workspace.current_user.userName} | bundle                          | The base path for the bundle in the S3 backend                                                                   |
| BRICKFLOW_BUNDLE_OBJ_NAME              | .brickflow_bundles                             | bundle                          | The name of the folder post appended to your base path                                                           |
| BRICKFLOW_BUNDLE_CLI_EXEC              | databricks                                     | bundle                          | The executable command for bundle execution. By default it will be downloaded on the fly.                        |
| BRICKFLOW_BUNDLE_NO_DOWNLOAD           | False                                          | bundle                          | Flag indicating whether to skip downloading the databricks bundle cli. Useful if you are in locked down network. |
| BRICKFLOW_BUNDLE_CLI_VERSION           | 0.200.0                                        | bundle                          | The version of the bundle CLI tool                                                                               |
| BRICKFLOW_MONOREPO_PATH_TO_BUNDLE_ROOT | N/A                                            | bundle & cdktf (**deprecated**) | The path to the bundle root directory in a monorepo. Default assumes you are not using a monorepo                |

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
