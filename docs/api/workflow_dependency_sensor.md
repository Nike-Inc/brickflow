---
search:
  exclude: true
---

::: brickflow_plugins.databricks.workflow_dependency_sensor
    handler: python
    options:
        members:
            - WorkflowDependencySensor
            - WorkflowTaskDependencySensor
        filters:
            - "!^_[^_]"
            - "!^__[^__]"
