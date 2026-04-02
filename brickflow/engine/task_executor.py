"""Generic task executor for injected tasks."""

import json
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
        log.info("Downloading artifact from: %s", url)

        try:
            headers = {}
            if self.username and self.api_key:
                headers["X-JFrog-Art-Api"] = self.api_key

            response = requests.get(url, headers=headers, stream=True, timeout=300)
            response.raise_for_status()

            if destination is None:
                # Create temp file with appropriate extension
                suffix = Path(url).suffix or ".whl"
                with tempfile.NamedTemporaryFile(
                    delete=False, suffix=suffix
                ) as temp_file:
                    destination = Path(temp_file.name)

            with open(destination, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            log.info("Downloaded artifact to: %s", destination)
            return destination

        except Exception as e:
            log.error("Failed to download artifact from %s: %s", url, e)
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
                log.info("Artifact setup complete: %s", artifact_path)

            # Load and render template
            template_code = self._load_and_render_template(task_def)

            # Execute the rendered code
            log.info("Executing task: %s", task_def.task_name)
            local_vars: Dict[str, Any] = {}
            exec(template_code, globals(), local_vars)  # pylint: disable=exec-used

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
                    "Custom template file not found: %s. Using default.",
                    template_path,
                )
                template_path = self.DEFAULT_TEMPLATE_PATH
        else:
            template_path = self.DEFAULT_TEMPLATE_PATH

        log.info("Using template: %s", template_path)

        # Load template
        with open(template_path, "r", encoding="utf-8") as f:
            template_content = f.read()

        # Render template with context
        template = Template(template_content)
        rendered_code = template.render(**task_def.template_context)

        log.debug("Rendered template for %s:\n%s", task_def.task_name, rendered_code)

        return rendered_code

    def render_template(self) -> str:
        """Pre-render the template at deploy time so the code can be baked into the config."""
        return self._load_and_render_template(self.task_def)

    def serialize_for_runtime(self) -> str:
        """
        Render the template, write it to a local file that DAB will sync to the
        workspace, and return a lightweight JSON pointer (no inline code).

        The rendered ``.py`` file is placed under ``_brickflow_injected/`` in the
        current working directory (the project root during ``bf projects deploy``).
        DAB uploads everything in the project tree to
        ``${workspace.file_path}/…`` so the file will be available on the cluster
        at ``/Workspace/${workspace.file_path}/_brickflow_injected/<task>.py``.
        """
        rendered_code = self.render_template()

        injected_dir = Path("_brickflow_injected")
        injected_dir.mkdir(exist_ok=True)

        file_name = f"{self.task_def.task_name}.py"
        (injected_dir / file_name).write_text(rendered_code, encoding="utf-8")
        log.info("Wrote injected task code to %s", injected_dir / file_name)

        data: Dict[str, Any] = {
            "task_name": self.task_def.task_name,
            "task_type": self.task_def.task_type,
            "file_ref": f"_brickflow_injected/{file_name}",
        }
        if self.task_def.artifact:
            data["artifact"] = {
                "url": self.task_def.artifact.url,
                "install_as_library": self.task_def.artifact.install_as_library,
            }
        return json.dumps(data, separators=(",", ":"))

    @staticmethod
    def create_task_function_from_config(
        config_json: str, workspace_file_path: Optional[str] = None
    ) -> Callable:
        """
        Reconstruct a task function at runtime from baked injection config.

        Prefers reading the rendered code from a workspace file that was synced
        by DAB at deploy time.  Falls back to inline ``rendered_code`` in the
        JSON for backward compatibility with older deployments.
        """
        config = json.loads(config_json)
        task_name: str = config["task_name"]
        artifact_cfg: Optional[Dict[str, Any]] = config.get("artifact")
        inline_code: Optional[str] = config.get("rendered_code")

        def injected_task_function() -> Any:
            if artifact_cfg:
                GenericTaskExecutor._download_and_setup_artifact(
                    url=artifact_cfg["url"],
                    username=None,
                    api_key=None,
                )

            code: Optional[str] = None

            if workspace_file_path:
                try:
                    with open(workspace_file_path, "r", encoding="utf-8") as fh:
                        code = fh.read()
                    log.info(
                        "Loaded injected task code from workspace file: %s",
                        workspace_file_path,
                    )
                except FileNotFoundError:
                    log.warning(
                        "Workspace file not found: %s — falling back to inline code",
                        workspace_file_path,
                    )

            if code is None:
                code = inline_code

            if not code:
                raise RuntimeError(
                    f"No code available for injected task '{task_name}'. "
                    "Neither workspace file nor inline rendered_code found in "
                    "the injection config."
                )

            log.info("Executing injected task: %s", task_name)
            local_vars: Dict[str, Any] = {}
            exec(code, globals(), local_vars)  # pylint: disable=exec-used
            return local_vars.get("result")

        injected_task_function.__name__ = task_name
        return injected_task_function

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
            log.info("Added %s to sys.path", artifact_path)

        return artifact_path
