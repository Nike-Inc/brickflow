# Task Injection in Brickflow

This feature allows you to automatically inject tasks into all Brickflow workflows at deployment time using a YAML configuration file. This is particularly useful for:

- Monitoring and logging tasks
- Data quality checks
- Cleanup operations
- Notification tasks
- Any cross-cutting concerns that should run with every workflow
- Compliance related tasks

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
    artifact:                      # Optional: Download artifact from Artifactory
      url: str                     # Artifact URL
      username: str                # Optional: Override global username
      api_key: str                 # Optional: Override global API key
      install_as_library: bool     # Whether to install artifact as cluster library
    template_file: str             # Optional: Path to custom Python template
    template_context: dict         # Variables to pass to template
    libraries: [str]               # PyPI packages for this task
    cluster: str                   # Optional: Cluster override
    depends_on_strategy: str       # Dependency strategy (see below)
    task_type: str                 # Task type (default: BRICKFLOW_TASK)

environment_overrides:
  dev:                             # Environment-specific overrides
    global: {...}
    tasks:
      task_name: {...}
```

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

Use `environment_overrides` to customize behavior per environment:

```yaml
global:
  enabled: true

tasks:
  - task_name: "environment_logger"
    enabled: true
    template_context:
      task_name: "environment_logger"
      params:
        environment: "dev"
        log_level: "DEBUG"

environment_overrides:
  prod:
    global:
      enabled: true
    tasks:
      environment_logger:
        template_context:
          params:
            environment: "prod"
            log_level: "INFO"
  
  dev:
    tasks:
      environment_logger:
        enabled: true  # Enabled in dev
```

Deploy with environment:

```bash
export BRICKFLOW_ENV=prod
export BRICKFLOW_INJECT_TASKS_CONFIG="config/injected_tasks.yaml"
bf projects deploy --project my_project --env prod
```

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

3. Check logs during deployment for warnings:
   ```
   INFO:brickflow:Injecting task 'logging_task' into workflow 'my_workflow'
   ```

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

### Multiple Templates per Environment

```yaml
tasks:
  - task_name: "logger"
    template_file: "templates/logging_dev.py.j2"

environment_overrides:
  prod:
    tasks:
      logger:
        template_file: "templates/logging_prod.py.j2"
```

### Conditional Task Injection

Use the `enabled` flag with environment-specific overrides:

```yaml
tasks:
  - task_name: "debug_task"
    enabled: true

environment_overrides:
  prod:
    tasks:
      debug_task:
        enabled: false  # Disable in production
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

