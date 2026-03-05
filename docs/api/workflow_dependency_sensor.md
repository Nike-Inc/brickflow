---
search:
  exclude: true
---

# Workflow Dependency Sensor

The `WorkflowDependencySensor` and `WorkflowTaskDependencySensor` allow you to create cross-workflow dependencies in Databricks. Use these sensors to wait for an upstream workflow (or a specific task within it) to complete before proceeding with your own workflow's tasks.

## WorkflowDependencySensor

Monitors an entire Databricks workflow and waits for a successful run within a configurable time window. Suitable when you need to depend on the overall completion of an upstream job.

## WorkflowTaskDependencySensor

Monitors a **specific task** within a Databricks workflow. This provides finer-grained control when you only need a particular task to complete rather than the entire workflow.

### Handling skipped tasks

By default, the sensor only considers tasks with a `SUCCESS` result state as completed. Some workflows use conditional logic that causes certain tasks to be skipped (reported as `EXCLUDED` by Databricks). If a skipped task should be treated as a valid completion state, set the `allow_skipped` parameter to `True`:

```python
sensor = WorkflowTaskDependencySensor(
    dependency_job_name="upstream_job",
    dependency_task_name="conditional_task",
    delta=timedelta(days=1),
    timeout_seconds=300,
    allow_skipped=True,  # treat EXCLUDED tasks as successful
)
sensor.execute()
```

When `allow_skipped=False` (the default), only `SUCCESS` is accepted. When `allow_skipped=True`, both `SUCCESS` and `EXCLUDED` states are accepted.

## API Reference

::: brickflow_plugins.databricks.workflow_dependency_sensor
    handler: python
    options:
        members:
            - WorkflowDependencySensor
            - WorkflowTaskDependencySensor
        filters:
            - "!^_[^_]"
            - "!^__[^__]"
