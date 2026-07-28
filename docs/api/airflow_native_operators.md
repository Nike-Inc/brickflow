---
search:
  exclude: true
---

# Deprecated Airflow-based Operators

As of the Airflow-free release, brickflow no longer depends on
`apache-airflow` at runtime. The following operators used to subclass
Airflow's `BaseOperator` and required `apache-airflow` installed on the
Databricks cluster:

- `BashOperator`
- `BranchPythonOperator`
- `ShortCircuitOperator`

They are still importable so existing user code fails loudly at *usage*
rather than silently at *import*, but instantiating any of them now raises
`RuntimeError` with a pointer to the native replacement.

## Migration

| Removed | Replacement |
| --- | --- |
| `BashOperator` | Run your shell command from a Databricks notebook cell (`%sh`) invoked via `RunJobTask`, or `dbutils.notebook.run` a helper notebook. |
| `BranchPythonOperator` | Use `IfElseConditionTask` on your workflow. |
| `ShortCircuitOperator` | Use `IfElseConditionTask` to skip downstream tasks. |
| `TaskDependencySensor` | Use `AirflowTaskDependencySensor` from `brickflow_plugins`. |
| `AirflowProxyOktaClusterAuth` | Compute the bearer token yourself and pass it into the plain `AirflowCluster` dataclass. |
| `BrickflowSecretsBackend` | Removed. Use `brickflow_plugins.secrets.resolve_secret(url)` directly or call the Cerberus/Base64 helpers. |

## API Reference

::: brickflow_plugins.operators.deprecated_airflow_operators
    handler: python
    options:
        filters:
            - "!^_[^_]"
            - "!^__[^__]"
