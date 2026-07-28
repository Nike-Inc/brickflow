---
search:
  exclude: true
---

# Tableau Refresh Operators

`TableauRefreshDataSourceOperator` and `TableauRefreshWorkBookOperator`
refresh Tableau data sources or workbooks by triggering async refresh
jobs and polling the Tableau server until they complete.

Previously these operators subclassed Airflow's `BaseOperator`. They have
been rewritten as plain Python classes with an `execute()` method -- no
`apache-airflow` install is required. The public constructor signature and
behavior remain unchanged apart from no longer accepting `task_id` (which
was an Airflow concept).

```python
from brickflow_plugins import (
    TableauRefreshDataSourceOperator,
    TableauRefreshWorkBookOperator,
)

TableauRefreshDataSourceOperator(
    server="https://tableau.example.com",
    username="me",
    password="pw",
    site="my_site",
    project="my_project",
    data_sources=["ds_a", "ds_b"],
).execute()
```

Requires the `tableauserverclient` library to be installed on the cluster
(via `PypiTaskLibrary("tableauserverclient==0.25")` or the
`brickflow[tableau]` extra during local development).

## API Reference

::: brickflow_plugins.operators.tableau_refresh_operator
    handler: python
    options:
        filters:
            - "!^_[^_]"
            - "!^__[^__]"
