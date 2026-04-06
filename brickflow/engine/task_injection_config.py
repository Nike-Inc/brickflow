"""Configuration for task injection from YAML files."""

import os
from dataclasses import dataclass, field
from typing import Any, cast, Optional, List, Dict
import yaml
from brickflow import _ilog as log
from brickflow.engine.task import TaskType


@dataclass
class ArtifactConfig:
    """Configuration for artifact download from Artifactory."""

    url: str
    """URL of the artifact to download"""

    username: Optional[str] = None
    """Artifactory username (can use env var)"""

    api_key: Optional[str] = None
    """Artifactory API key (can use env var)"""

    install_as_library: bool = False
    """Whether to install the artifact as a library on the cluster"""


@dataclass
class TaskDefinition:
    """Definition for a single injected task."""

    task_name: str
    """Name of the task to inject"""

    enabled: bool = True
    """Whether this task is enabled"""

    artifact: Optional[ArtifactConfig] = None
    """Artifact configuration for downloading from Artifactory"""

    template_file: Optional[str] = None
    """Path to custom Python template file. If not provided, uses default template."""

    template_context: Dict[str, Any] = field(default_factory=dict)
    """Context variables to pass to the template for rendering"""

    libraries: List[str] = field(default_factory=list)
    """List of PyPI packages to attach as libraries (e.g., ['requests>=2.28.0', 'pandas>=1.0.0'])"""

    cluster: Optional[str] = None
    """Cluster ID for cluster override (optional)"""

    depends_on_strategy: str = "leaf_nodes"
    """Strategy for dependencies: 'leaf_nodes', 'all_tasks', or comma-separated task names"""

    task_type: TaskType = TaskType.BRICKFLOW_TASK
    """Task type for the injected task (same ``TaskType`` enum as workflow tasks)."""

    task_config: Optional[Dict[str, Any]] = None
    """
    Configuration for native Databricks task types.
    Only used when task_type is a native type (PYTHON_WHEEL_TASK, NOTEBOOK_TASK, etc.).
    
    For BRICKFLOW_TASK, use template_file instead.
    
    Structure depends on task_type. Examples:
    
    PYTHON_WHEEL_TASK:
        task_config:
          package_name: "mypackage"
          entry_point: "module.function"
          parameters: ["{{arg}}"]
          named_parameters: {"key": "{{value}}"}
    
    NOTEBOOK_TASK:
        task_config:
          notebook_path: "/path/to/notebook"
          base_parameters: {"key": "{{value}}"}
          source: "WORKSPACE"
    
    SPARK_JAR_TASK:
        task_config:
          main_class_name: "com.example.Main"
          parameters: ["{{arg}}"]
    
    SPARK_PYTHON_TASK:
        task_config:
          python_file: "path/to/script.py"
          source: "GIT"
          parameters: ["--arg", "{{value}}"]
    
    SQL:
        task_config:
          warehouse_id: "warehouse_id"
          query_id: "query_id"
          parameters: {"key": "{{value}}"}
    
    RUN_JOB_TASK:
        task_config:
          job_name: "job_name"
          job_parameters: {"key": "{{value}}"}
    
    IF_ELSE_CONDITION_TASK:
        task_config:
          left: "{{value1}}"
          right: "{{value2}}"
          op: "=="
    """


@dataclass
class GlobalConfig:
    """Global configuration for task injection."""

    enabled: bool = True
    """Global enable/disable for all task injection"""

    default_libraries: List[str] = field(default_factory=list)
    """Default libraries to attach to all injected tasks"""

    default_cluster: Optional[str] = None
    """Default cluster ID for all injected tasks"""

    artifactory_username: Optional[str] = None
    """Default Artifactory username"""

    artifactory_api_key: Optional[str] = None
    """Default Artifactory API key"""


@dataclass
class TaskInjectionConfig:
    """Complete task injection configuration."""

    global_config: GlobalConfig
    tasks: List[TaskDefinition]

    @classmethod
    def from_yaml(cls, yaml_path: str) -> "TaskInjectionConfig":
        """
        Load task injection configuration from YAML file.

        Args:
            yaml_path: Path to the YAML configuration file

        Returns:
            TaskInjectionConfig instance
        """
        log.info("Loading task injection config from: %s", yaml_path)

        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        if not data:
            log.warning("Empty YAML configuration file: %s", yaml_path)
            return cls(global_config=GlobalConfig(), tasks=[])

        # Parse global config
        global_data = cast(Dict[str, Any], data.get("global", {}))
        global_config = GlobalConfig(
            enabled=cast(bool, global_data.get("enabled", True)),
            default_libraries=cast(List[str], global_data.get("default_libraries", [])),
            default_cluster=(
                cast(str, global_data["default_cluster"])
                if "default_cluster" in global_data
                else None
            ),
            artifactory_username=cls._resolve_env_var(
                cast(Optional[str], global_data.get("artifactory_username"))
            ),
            artifactory_api_key=cls._resolve_env_var(
                cast(Optional[str], global_data.get("artifactory_api_key"))
            ),
        )

        # Parse tasks
        tasks_data = cast(List[Dict[str, Any]], data.get("tasks", []))
        tasks: List[TaskDefinition] = []

        for task_data in tasks_data:
            artifact_data = cast(Optional[Dict[str, Any]], task_data.get("artifact"))
            artifact: Optional[ArtifactConfig] = None

            if artifact_data:
                artifact = ArtifactConfig(
                    url=cast(str, artifact_data["url"]),
                    username=cls._resolve_env_var(
                        cast(
                            Optional[str],
                            artifact_data.get(
                                "username", global_config.artifactory_username
                            ),
                        )
                    ),
                    api_key=cls._resolve_env_var(
                        cast(
                            Optional[str],
                            artifact_data.get(
                                "api_key", global_config.artifactory_api_key
                            ),
                        )
                    ),
                    install_as_library=cast(
                        bool, artifact_data.get("install_as_library", False)
                    ),
                )

            task = TaskDefinition(
                task_name=cast(str, task_data["task_name"]),
                enabled=cast(bool, task_data.get("enabled", True)),
                artifact=artifact,
                template_file=(
                    cast(str, task_data["template_file"])
                    if "template_file" in task_data
                    else None
                ),
                template_context=cast(
                    dict[str, Any], task_data.get("template_context", {})
                ),
                libraries=cast(list[str], task_data.get("libraries", [])),
                cluster=(
                    cast(str, task_data["cluster"])
                    if "cluster" in task_data
                    else global_config.default_cluster
                ),
                depends_on_strategy=cast(
                    str, task_data.get("depends_on_strategy", "leaf_nodes")
                ),
                task_type=cls._coerce_task_type(task_data.get("task_type")),
                task_config=cast(
                    Optional[Dict[str, Any]], task_data.get("task_config")
                ),
            )
            tasks.append(task)

        return cls(global_config=global_config, tasks=tasks)

    @staticmethod
    def _coerce_task_type(raw: Any) -> TaskType:
        if isinstance(raw, TaskType):
            return raw
        if not isinstance(raw, str):
            if raw is not None:
                raise ValueError(
                    f"task_type must be a string or TaskType, got {type(raw).__name__}"
                )
            return TaskType.BRICKFLOW_TASK
        if not (s := raw.strip()):
            return TaskType.BRICKFLOW_TASK
        try:
            return TaskType[s.upper()]
        except KeyError:
            valid = ", ".join(m.name for m in TaskType)
            raise ValueError(f"Unknown task_type {raw!r}. Expected one of: {valid}")

    @staticmethod
    def _resolve_env_var(value: Optional[str]) -> Optional[str]:
        """
        Resolve environment variable references.

        Supports format: ${ENV_VAR_NAME} or $ENV_VAR_NAME
        """
        if not value:
            return value

        if value.startswith("${") and value.endswith("}"):
            env_var = value[2:-1]
            return os.getenv(env_var)
        elif value.startswith("$"):
            env_var = value[1:]
            return os.getenv(env_var)

        return value
