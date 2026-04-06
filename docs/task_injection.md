# Task Injection in Brickflow

This feature allows you to automatically inject tasks into Brickflow workflows at deployment time using YAML configuration files. This is particularly useful for:

- Monitoring and logging tasks
- Data quality checks
- Cleanup operations
- Notification tasks
- Any cross-cutting concerns that should run with every workflow
- Compliance related tasks

## Two Approaches

Brickflow supports two complementary approaches for task injection:

1. **Global Task Injection** - Tasks are injected into **ALL workflows**
   - Use `BRICKFLOW_INJECT_TASKS_CONFIG` environment variable
   - Points to a single config file (e.g., `config/injected_tasks.yaml`)
   - All tasks in this file are injected into every workflow

2. **Workflow-Specific Task Injection** - Tasks are injected only into **matching workflows**
   - Use `BRICKFLOW_INJECT_TASKS_DIR` environment variable
   - Points to a directory containing workflow-specific config files
   - Files are named `<workflow_name>.yaml` (e.g., `etl_daily.yaml`)
   - Tasks only injected into the workflow with matching name

**Both approaches can be used together** to combine global tasks with workflow-specific tasks.

## Quick Start

### 1. Create a Task Injection Configuration File

Create a YAML file (e.g., `config/injected_tasks.yaml`) that defines the tasks you want to inject:

```yaml
global:
  enabled: true
  default_libraries:
    - "requests>=2.28.0"

tasks:
  - task_name: "logging_task"
    enabled: true
    depends_on_strategy: "leaf_nodes"
    template_context:
      imports:
        - "import datetime"
      task_name: "logging_task"
      message: "Workflow execution completed"
      params:
        timestamp: "{{datetime.datetime.now()}}"
        status: "success"
```

### 2. Deploy with Task Injection

Set the environment variable to point to your config file:

```bash
export BRICKFLOW_INJECT_TASKS_CONFIG="config/injected_tasks.yaml"
bf projects deploy --project my_project --env dev
```

That's it! The specified tasks will be automatically injected into all workflows during deployment.

## Configuration Reference

### YAML Structure

```yaml
global:
  enabled: bool                    # Enable/disable all task injection
  default_libraries: [str]         # Default PyPI packages for all injected tasks
  default_cluster: str             # Default cluster ID (optional)
  artifactory_username: str        # Artifactory username (supports ${ENV_VAR})
  artifactory_api_key: str         # Artifactory API key (supports ${ENV_VAR})

tasks:
  - task_name: str                 # Unique name for the injected task
    enabled: bool                  # Enable/disable this specific task
    task_type: str                 # TaskType enum name (default: BRICKFLOW_TASK)
                                   # Options: BRICKFLOW_TASK, NOTEBOOK_TASK,
                                   #   PYTHON_WHEEL_TASK, SPARK_JAR_TASK,
                                   #   SPARK_PYTHON_TASK, SQL, RUN_JOB_TASK,
                                   #   IF_ELSE_CONDITION_TASK
    artifact:                      # Optional: Download artifact from Artifactory
      url: str                     # Artifact URL
      username: str                # Optional: Override global username
      api_key: str                 # Optional: Override global API key
      install_as_library: bool     # Whether to install artifact as cluster library
    template_file: str             # Path to Jinja2 template (BRICKFLOW_TASK only)
    template_context: dict         # Variables to pass to template
    task_config: dict              # Task configuration (native task types only,
                                   # mutually exclusive with template_file)
    libraries: [str]               # PyPI packages for this task
    cluster: str                   # Optional: Cluster override
    depends_on_strategy: str       # Dependency strategy (see below)
```

### Environment Variables

Two environment variables control task injection:

**`BRICKFLOW_INJECT_TASKS_CONFIG`**
- Path to global config file
- Tasks in this file are injected into **ALL workflows**
- Example: `export BRICKFLOW_INJECT_TASKS_CONFIG="config/injected_tasks_global.yaml"`

**`BRICKFLOW_INJECT_TASKS_DIR`**
- Path to directory containing workflow-specific config files
- Files must be named `<workflow_name>.yaml`
- Tasks only injected into workflows with matching names
- Example: `export BRICKFLOW_INJECT_TASKS_DIR="config/injected_tasks/"`

**Using Both Together:**
```bash
# Global tasks for all workflows
export BRICKFLOW_INJECT_TASKS_CONFIG="config/injected_tasks_global.yaml"

# Workflow-specific tasks
export BRICKFLOW_INJECT_TASKS_DIR="config/injected_tasks/"

# Deploy
bf projects deploy --project my_project --env dev
```

Result:
- Workflow "etl_daily" gets: global tasks + tasks from `config/injected_tasks/etl_daily.yaml`
- Workflow "ml_training" gets: global tasks + tasks from `config/injected_tasks/ml_training.yaml`
- Workflow "api_service" gets: global tasks only (no specific config file)

### Dependency Strategies

The `depends_on_strategy` field controls where the injected task runs in the workflow:

1. **`leaf_nodes`** (default): Task runs after all leaf nodes (tasks with no downstream dependencies)
   ```
   task1 -> task2 -> injected_task
   task3 ----------^
   ```

2. **`all_tasks`**: Task runs first, all other tasks depend on it
   ```
   injected_task -> task1
                 -> task2
                 -> task3
   ```

3. **`specific_tasks:task1,task2`**: Task runs after specific named tasks
   ```
   task1 -> injected_task
   task2 -^
   task3 (independent)
   ```

## Usage Examples

### Example 1: Global Tasks Only

Inject the same tasks into all workflows:

```bash
export BRICKFLOW_INJECT_TASKS_CONFIG="config/injected_tasks.yaml"
bf projects deploy --project my_project --env dev
```

**File structure:**
```
config/
  injected_tasks.yaml    # Tasks for ALL workflows
```

**Result:** All workflows get tasks defined in `injected_tasks.yaml`

### Example 2: Workflow-Specific Tasks Only

Inject different tasks into different workflows:

```bash
export BRICKFLOW_INJECT_TASKS_DIR="config/injected_tasks/"
bf projects deploy --project my_project --env dev
```

**File structure:**
```
config/
  injected_tasks/
    etl_daily.yaml       # Tasks only for "etl_daily" workflow
    ml_training.yaml     # Tasks only for "ml_training" workflow
    api_service.yaml     # Tasks only for "api_service" workflow
```

**Result:**
- Workflow "etl_daily" gets tasks from `etl_daily.yaml`
- Workflow "ml_training" gets tasks from `ml_training.yaml`
- Workflow "api_service" gets tasks from `api_service.yaml`
- Other workflows get no injected tasks

### Example 3: Global + Workflow-Specific Tasks

Combine global tasks with workflow-specific tasks:

```bash
export BRICKFLOW_INJECT_TASKS_CONFIG="config/injected_tasks_global.yaml"
export BRICKFLOW_INJECT_TASKS_DIR="config/injected_tasks/"
bf projects deploy --project my_project --env dev
```

**File structure:**
```
config/
  injected_tasks_global.yaml    # Global tasks for ALL workflows
  injected_tasks/
    etl_daily.yaml              # Additional tasks for "etl_daily"
    ml_training.yaml            # Additional tasks for "ml_training"
```

**Result:**
- Workflow "etl_daily" gets: global tasks + `etl_daily.yaml` tasks
- Workflow "ml_training" gets: global tasks + `ml_training.yaml` tasks
- Workflow "api_service" gets: global tasks only

**Example config files:**

`config/injected_tasks_global.yaml`:
```yaml
global:
  enabled: true

tasks:
  - task_name: "global_logger"
    enabled: true
    depends_on_strategy: "leaf_nodes"
    template_context:
      task_name: "global_logger"
      message: "Logging workflow execution"
```

`config/injected_tasks/etl_daily.yaml`:
```yaml
global:
  enabled: true

tasks:
  - task_name: "etl_data_quality"
    enabled: true
    depends_on_strategy: "leaf_nodes"
    libraries:
      - "great-expectations>=0.15.0"
    template_context:
      task_name: "etl_data_quality"
      message: "Running ETL data quality checks"
```

## Python Templates

### Using the Default Template

If you don't specify a `template_file`, Brickflow uses the default template located at:
`brickflow/templates/injected_task_default.py.j2`

The default template expects these context variables:
- `imports`: List of import statements (optional)
- `task_name`: Name of the task
- `message`: Custom message to print (optional)
- `params`: Dictionary of parameters to display (optional)

### Creating a Custom Template

Create a Python file with Jinja2 template syntax:

```python
# custom_template.py.j2
{% for import_stmt in imports %}
{{ import_stmt }}
{% endfor %}

import logging
logger = logging.getLogger(__name__)

logger.info("Starting custom task: {{ task_name }}")

# Your custom logic here
{% if execute_function %}
result = {{ execute_function }}()
{% else %}
result = "Task executed successfully"
{% endif %}

logger.info(f"Task completed: {result}")
```

Reference it in your YAML:

```yaml
tasks:
  - task_name: "my_task"
    template_file: "path/to/custom_template.py.j2"
    template_context:
      imports:
        - "import sys"
      task_name: "my_task"
      execute_function: "my_custom_function"
```

## Native Databricks Task Types

In addition to `BRICKFLOW_TASK` (which renders a Jinja2 template to a notebook), you can inject native Databricks task types using `task_type` and `task_config`. The `task_config` fields match the corresponding Brickflow task class constructor arguments.

### PYTHON_WHEEL_TASK

```yaml
tasks:
  - task_name: "compliance_check"
    task_type: "PYTHON_WHEEL_TASK"
    task_config:
      package_name: "goodbyepii"
      entry_point: "databricks_task_runner.run_compliance_check_cli"
      parameters: ["{{catalog}}", "{{schema}}", "{{table}}"]
    template_context:
      catalog: "hive_metastore"
      schema: "gold"
      table: "customer_data"
    libraries:
      - "goodbyepii>=1.0.0"
    depends_on_strategy: "leaf_nodes"
```

### NOTEBOOK_TASK

```yaml
tasks:
  - task_name: "run_analysis"
    task_type: "NOTEBOOK_TASK"
    task_config:
      notebook_path: "/Workspace/notebooks/{{notebook_name}}"
      base_parameters:
        env: "{{env}}"
      source: "WORKSPACE"
    template_context:
      notebook_name: "data_processing"
      env: "prod"
```

### SPARK_JAR_TASK

```yaml
tasks:
  - task_name: "spark_jar_job"
    task_type: "SPARK_JAR_TASK"
    task_config:
      main_class_name: "com.example.DataProcessor"
      parameters: ["--input", "{{input_path}}", "--output", "{{output_path}}"]
    template_context:
      input_path: "s3://bucket/input"
      output_path: "s3://bucket/output"
```

### SPARK_PYTHON_TASK

```yaml
tasks:
  - task_name: "spark_python_job"
    task_type: "SPARK_PYTHON_TASK"
    task_config:
      python_file: "scripts/{{script_name}}.py"
      source: "GIT"
      parameters: ["--env", "{{env}}"]
    template_context:
      script_name: "process_data"
      env: "prod"
```

### SQL

```yaml
tasks:
  - task_name: "sql_query"
    task_type: "SQL"
    task_config:
      warehouse_id: "abc123"
      query_id: "query_{{env}}"
      parameters:
        catalog: "{{catalog}}"
        schema: "{{schema}}"
    template_context:
      env: "dev"
      catalog: "production"
      schema: "analytics"
```

> **Note:** Native task types require `task_config`. `template_file` and `template_context` are only used by `BRICKFLOW_TASK`.

## Example Use Cases

### 1. Simple Logging Task

```yaml
tasks:
  - task_name: "workflow_logger"
    enabled: true
    depends_on_strategy: "leaf_nodes"
    template_context:
      imports:
        - "import datetime"
        - "import socket"
      task_name: "workflow_logger"
      message: "Workflow completed successfully"
      params:
        hostname: "{{socket.gethostname()}}"
        timestamp: "{{datetime.datetime.now()}}"
```

### 2. Data Quality Validation

```yaml
tasks:
  - task_name: "data_quality_validation"
    enabled: true
    libraries:
      - "great-expectations>=0.15.0"
    depends_on_strategy: "leaf_nodes"
    template_file: "templates/data_quality_template.py.j2"
    template_context:
      checkpoint_name: "my_checkpoint"
      data_source: "gold_tables"
```

### 3. Cleanup Task Running First

```yaml
tasks:
  - task_name: "cleanup_temp_tables"
    enabled: true
    depends_on_strategy: "all_tasks"
    template_context:
      imports:
        - "from pyspark.sql import SparkSession"
      task_name: "cleanup_temp_tables"
      message: "Cleaning up temporary tables before workflow execution"
      params:
        cleanup_database: "temp_db"
        retention_days: 7
```

### 4. Notification Task

```yaml
tasks:
  - task_name: "send_notification"
    enabled: true
    libraries:
      - "slack-sdk>=3.0.0"
    depends_on_strategy: "leaf_nodes"
    template_context:
      imports:
        - "from slack_sdk import WebClient"
      task_name: "send_notification"
      message: "Sending workflow completion notification"
      params:
        channel: "#data-pipeline-alerts"
        webhook_url: "${SLACK_WEBHOOK_URL}"
```

### 5. Download and Use Custom Artifact

```yaml
tasks:
  - task_name: "custom_validation"
    enabled: true
    artifact:
      url: "https://artifactory.company.com/validators/validator-1.0.0-py3-none-any.whl"
      username: ${ARTIFACTORY_USERNAME}
      api_key: ${ARTIFACTORY_API_KEY}
      install_as_library: false
    libraries:
      - "custom-validators>=1.0.0"
    template_context:
      imports:
        - "from custom_validators import DataValidator"
      task_name: "custom_validation"
      message: "Running custom validation checks"
```

## Environment-Specific Configuration

To vary behaviour per environment, maintain separate YAML config files per environment and point `BRICKFLOW_INJECT_TASKS_CONFIG` (or `BRICKFLOW_INJECT_TASKS_DIR`) at the appropriate one during deployment:

```bash
# Dev deployment
export BRICKFLOW_INJECT_TASKS_CONFIG="config/injected_tasks_dev.yaml"
bf projects deploy --project my_project --env dev

# Prod deployment
export BRICKFLOW_INJECT_TASKS_CONFIG="config/injected_tasks_prod.yaml"
bf projects deploy --project my_project --env prod
```

Alternatively, use `enabled: false` in tasks that should be skipped in certain environments and swap the config file.

## Best Practices

### 1. Keep Templates Simple

Templates should focus on the execution logic. Complex setup should be in the imported modules.

### 2. Use Environment Variables for Credentials

Never hardcode credentials in YAML:

```yaml
global:
  artifactory_username: ${ARTIFACTORY_USERNAME}
  artifactory_api_key: ${ARTIFACTORY_API_KEY}
```

### 3. Test Injection Locally

Before deploying, test your configuration:

```bash
export BRICKFLOW_INJECT_TASKS_CONFIG="config/injected_tasks.yaml"
export BRICKFLOW_ENV=dev
bf projects deploy --project my_project --env dev --mode bundle
```

### 4. Version Your Templates

Store custom templates in version control alongside your workflows:

```
project/
├── workflows/
├── config/
│   └── injected_tasks.yaml
├── templates/
│   ├── logging_template.py.j2
│   └── notification_template.py.j2
└── README.md
```

### 5. Monitor Task Execution

Injected tasks appear in Databricks job runs like any other task. Monitor their execution and adjust dependencies as needed.

## Troubleshooting

### Task Not Appearing in Workflow

1. Check environment variable is set:
   ```bash
   echo $BRICKFLOW_INJECT_TASKS_CONFIG
   ```

2. Verify YAML syntax:
   ```bash
   python -c "import yaml; yaml.safe_load(open('config/injected_tasks.yaml'))"
   ```

3. Check logs during deployment for errors — injection logs at `ERROR` level only by default.

### Template Rendering Errors

1. Verify template syntax with Jinja2:
   ```python
   from jinja2 import Template
   template = Template(open('my_template.py.j2').read())
   print(template.render(**context))
   ```

2. Check all required context variables are provided in YAML

### Import Errors in Injected Tasks

1. Verify libraries are specified in YAML:
   ```yaml
   libraries:
     - "my-package>=1.0.0"
   ```

2. Check artifact download if using custom artifacts:
   ```yaml
   artifact:
     url: "https://..."
     install_as_library: false
   ```

## Advanced Usage

### Dynamic Context Variables

Use environment variables in template context:

```yaml
template_context:
  params:
    database: "${DATABRICKS_DATABASE}"
    environment: "${BRICKFLOW_ENV}"
```

### Generated Notebooks Directory

When `BRICKFLOW_TASK` is used, brickflow renders the Jinja2 template to a `.py` notebook file in `_brickflow_injected_notebooks/` at deploy time. This directory is:

- Auto-created during `bf projects deploy`
- Synced to Databricks Workspace by DAB as part of the bundle
- Listed in `.gitignore` — **do not commit it**

```
project/
├── workflows/
├── config/
│   └── injected_tasks.yaml
├── templates/
│   └── my_template.py.j2
├── _brickflow_injected_notebooks/   # auto-generated, gitignored
└── README.md
```

## API Reference

See the following modules for detailed API documentation:

- `brickflow.engine.task_injection_config.TaskInjectionConfig`: Configuration parsing
- `brickflow.engine.task_executor.GenericTaskExecutor`: Task execution
- `brickflow.engine.project._Project._inject_tasks_from_yaml()`: Injection logic

## Contributing

To add new features to task injection:

1. Update configuration schema in `task_injection_config.py`
2. Extend executor in `task_executor.py`
3. Update default template in `templates/injected_task_default.py.j2`
4. Add tests in `tests/test_task_injection.py`
5. Update this documentation

