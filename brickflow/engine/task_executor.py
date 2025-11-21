"""Generic task executor for injected tasks."""

import sys
import tempfile
from pathlib import Path
from typing import Any, Callable, Dict, Optional
import requests
from jinja2 import Template
from brickflow import log
from brickflow.engine.task_injection_config import TaskDefinition


class ArtifactoryClient:
    """Client for downloading artifacts from Artifactory."""

    def __init__(self, username: Optional[str] = None, api_key: Optional[str] = None):
        self.username = username
        self.api_key = api_key

    def download_artifact(self, url: str, destination: Optional[Path] = None) -> Path:
        """
        Download artifact from Artifactory.

        Args:
            url: URL of the artifact
            destination: Optional destination path. If not provided, creates temp file.

        Returns:
            Path to downloaded artifact
        """
        log.info(f"Downloading artifact from: {url}")

        try:
            headers = {}
            if self.username and self.api_key:
                headers["X-JFrog-Art-Api"] = self.api_key

            response = requests.get(url, headers=headers, stream=True)
            response.raise_for_status()

            if destination is None:
                # Create temp file with appropriate extension
                suffix = Path(url).suffix or ".whl"
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
                destination = Path(temp_file.name)

            with open(destination, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            log.info(f"Downloaded artifact to: {destination}")
            return destination

        except Exception as e:
            log.error(f"Failed to download artifact from {url}: {e}")
            raise


class GenericTaskExecutor:
    """Executor for generic injected tasks with template support."""

    DEFAULT_TEMPLATE_PATH = (
        Path(__file__).parent.parent / "templates" / "injected_task_default.py.j2"
    )

    def __init__(self, task_def: TaskDefinition):
        self.task_def = task_def
        self.artifactory_client = None

        if task_def.artifact:
            self.artifactory_client = ArtifactoryClient(
                username=task_def.artifact.username, api_key=task_def.artifact.api_key
            )

    def create_task_function(self) -> Callable:
        """
        Create the task function that will be executed on Databricks.

        This function:
        1. Downloads artifact if needed (at task runtime on cluster)
        2. Renders the Python template with provided context
        3. Executes the rendered code

        Returns:
            Callable task function
        """
        task_def = self.task_def

        def injected_task_function() -> Any:
            """Dynamically generated task function."""
            # Download and setup artifact if specified
            if task_def.artifact:
                artifact_path = self._download_and_setup_artifact(
                    task_def.artifact.url,
                    task_def.artifact.username,
                    task_def.artifact.api_key,
                )
                log.info(f"Artifact setup complete: {artifact_path}")

            # Load and render template
            template_code = self._load_and_render_template(task_def)

            # Execute the rendered code
            log.info(f"Executing task: {task_def.task_name}")
            local_vars: Dict[str, Any] = {}
            exec(template_code, globals(), local_vars)

            # Return result if present
            return local_vars.get("result")

        # Set function name for better debugging
        injected_task_function.__name__ = task_def.task_name

        return injected_task_function

    def _load_and_render_template(self, task_def: TaskDefinition) -> str:
        """
        Load Python template file and render with Jinja2.

        Args:
            task_def: Task definition with template info

        Returns:
            Rendered Python code as string
        """
        # Determine template file to use
        if task_def.template_file:
            template_path = Path(task_def.template_file)
            if not template_path.is_absolute():
                # Resolve relative to workspace or config file location
                template_path = Path.cwd() / template_path

            if not template_path.exists():
                log.warning(
                    f"Custom template file not found: {template_path}. Using default."
                )
                template_path = self.DEFAULT_TEMPLATE_PATH
        else:
            template_path = self.DEFAULT_TEMPLATE_PATH

        log.info(f"Using template: {template_path}")

        # Load template
        with open(template_path, "r") as f:
            template_content = f.read()

        # Render template with context
        template = Template(template_content)
        rendered_code = template.render(**task_def.template_context)

        log.debug(f"Rendered template for {task_def.task_name}:\n{rendered_code}")

        return rendered_code

    @staticmethod
    def _download_and_setup_artifact(
        url: str, username: Optional[str], api_key: Optional[str]
    ) -> Path:
        """
        Download artifact and add to sys.path if needed.

        This runs at task execution time on the Databricks cluster.
        """
        client = ArtifactoryClient(username=username, api_key=api_key)
        artifact_path = client.download_artifact(url)

        # If it's a wheel or zip, add to sys.path
        if artifact_path.suffix in [".whl", ".zip"]:
            sys.path.insert(0, str(artifact_path))
            log.info(f"Added {artifact_path} to sys.path")

        return artifact_path
