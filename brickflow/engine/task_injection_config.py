"""Configuration for task injection from YAML files."""

import os
from dataclasses import dataclass, field
from typing import Any, cast
import yaml
from brickflow import log


@dataclass
class ArtifactConfig:
    """Configuration for artifact download from Artifactory."""

    url: str
    """URL of the artifact to download"""

    username: str | None = None
    """Artifactory username (can use env var)"""

    api_key: str | None = None
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

    artifact: ArtifactConfig | None = None
    """Artifact configuration for downloading from Artifactory"""

    template_file: str | None = None
    """Path to custom Python template file. If not provided, uses default template."""

    template_context: dict[str, Any] = field(default_factory=dict)
    """Context variables to pass to the template for rendering"""

    libraries: list[str] = field(default_factory=list)
    """List of PyPI packages to attach as libraries (e.g., ['requests>=2.28.0', 'pandas>=1.0.0'])"""

    cluster: str | None = None
    """Cluster ID for cluster override (optional)"""

    depends_on_strategy: str = "leaf_nodes"
    """Strategy for dependencies: 'leaf_nodes', 'all_tasks', or comma-separated task names"""

    task_type: str = "BRICKFLOW_TASK"
    """Task type for the injected task"""


@dataclass
class GlobalConfig:
    """Global configuration for task injection."""

    enabled: bool = True
    """Global enable/disable for all task injection"""

    default_libraries: list[str] = field(default_factory=list)
    """Default libraries to attach to all injected tasks"""

    default_cluster: str | None = None
    """Default cluster ID for all injected tasks"""

    artifactory_username: str | None = None
    """Default Artifactory username"""

    artifactory_api_key: str | None = None
    """Default Artifactory API key"""


@dataclass
class TaskInjectionConfig:
    """Complete task injection configuration."""

    global_config: GlobalConfig
    tasks: list[TaskDefinition]

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
        global_data = cast(dict[str, Any], data.get("global", {}))
        global_config = GlobalConfig(
            enabled=cast(bool, global_data.get("enabled", True)),
            default_libraries=cast(list[str], global_data.get("default_libraries", [])),
            default_cluster=(
                cast(str, global_data["default_cluster"])
                if "default_cluster" in global_data
                else None
            ),
            artifactory_username=cls._resolve_env_var(
                cast(str | None, global_data.get("artifactory_username"))
            ),
            artifactory_api_key=cls._resolve_env_var(
                cast(str | None, global_data.get("artifactory_api_key"))
            ),
        )

        # Parse tasks
        tasks_data = cast(list[dict[str, Any]], data.get("tasks", []))
        tasks: list[TaskDefinition] = []

        for task_data in tasks_data:
            artifact_data = cast(dict[str, Any] | None, task_data.get("artifact"))
            artifact: ArtifactConfig | None = None

            if artifact_data:
                artifact = ArtifactConfig(
                    url=cast(str, artifact_data["url"]),
                    username=cls._resolve_env_var(
                        cast(
                            str | None,
                            artifact_data.get(
                                "username", global_config.artifactory_username
                            ),
                        )
                    ),
                    api_key=cls._resolve_env_var(
                        cast(
                            str | None,
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
                task_type=cast(str, task_data.get("task_type", "BRICKFLOW_TASK")),
            )
            tasks.append(task)

        return cls(global_config=global_config, tasks=tasks)

    @staticmethod
    def _resolve_env_var(value: str | None) -> str | None:
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
