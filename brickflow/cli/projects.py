import contextlib
import os
from enum import Enum
from pathlib import Path
from typing import Dict, Optional, List, Generator, Any, Callable

import click
import yaml
from pydantic import BaseModel, Field

from brickflow import (
    BrickflowProjectConstants,
    BrickflowDefaultEnvs,
    BrickflowEnvVars,
    _ilog,
    BrickflowProjectDeploymentSettings,
    ctx,
)
from brickflow.cli.bundles import (
    bundle_deploy,
    bundle_destroy,
    pre_bundle_hook,
    bundle_sync,
)
from brickflow.cli.configure import (
    _create_gitignore_if_not_exists,
    _update_gitignore,
    create_entry_point,
    render_template,
    _validate_package,
    create_brickflow_project_root_marker,
    bind_env_var,
)
from brickflow.cli.constants import INTERACTIVE_MODE, BrickflowDeployMode
from brickflow.resolver import get_notebook_ws_path

DEFAULT_BRICKFLOW_VERSION_MODE = "auto"


class BrickflowProject(BaseModel):
    name: str
    path_from_repo_root_to_project_root: str = "."  # used for mono repo
    path_project_root_to_workflows_dir: (
        str  # used for repos with multiple batches of workflows
    )
    deployment_mode: str = BrickflowDeployMode.BUNDLE.value
    brickflow_version: str = DEFAULT_BRICKFLOW_VERSION_MODE
    enable_plugins: bool = False

    class Config:
        extra = "forbid"

    def is_brickflow_version_auto(self) -> bool:
        return self.brickflow_version == DEFAULT_BRICKFLOW_VERSION_MODE


class BrickflowRootProjectConfig(BaseModel):
    version: str = "v1"
    projects: Dict[str, BrickflowProject]

    class Config:
        extra = "forbid"


class ProjectRef(BaseModel):
    root_yaml_rel_path: str

    class Config:
        extra = "forbid"


class BrickflowMultiRootProjectConfig(BaseModel):
    version: str = "v1"
    project_roots: Dict[str, ProjectRef] = Field(default_factory=dict)

    class Config:
        extra = "forbid"

    def remove(self, project_name: str) -> None:
        self.project_roots.pop(project_name)

    def has_projects(self) -> bool:
        return self.project_roots is not None and len(self.project_roots) > 0


class ConfigFileType(Enum):
    YAML = "yaml"
    JSON = "json"  # unsupported


class MultiProjectManager:
    def __init__(
        self,
        config_file_name: str = BrickflowProjectConstants.DEFAULT_MULTI_PROJECT_CONFIG_FILE_NAME.value,
        file_type: ConfigFileType = ConfigFileType.YAML,
    ) -> None:
        self.file_type = file_type
        self._config_file: Path = Path(config_file_name)
        self._brickflow_multi_project_config: BrickflowMultiRootProjectConfig
        self._brickflow_multi_project_config = (
            self._load_config()
            if self._config_exists()
            else BrickflowMultiRootProjectConfig(project_roots={})
        )
        self._project_config_dict: Dict[str, BrickflowRootProjectConfig] = (
            self._load_roots()
            if self._brickflow_multi_project_config.has_projects()
            else {}
        )

    def __new__(cls, *args: Any, **kwargs: Any) -> "MultiProjectManager":
        # singleton
        if not hasattr(cls, "instance"):
            cls.instance = super(MultiProjectManager, cls).__new__(cls)
            if "config_file_name" in kwargs:
                cls.instance._config_file = Path(kwargs["config_file_name"])
        return cls.instance  # noqa

    def _config_exists(self) -> bool:
        return self._config_file.exists()

    def _load_config(self) -> BrickflowMultiRootProjectConfig:
        with self._config_file.open("r", encoding="utf-8") as f:
            config = BrickflowMultiRootProjectConfig.parse_obj(yaml.safe_load(f.read()))
            if config.project_roots is not None:
                return config
            return BrickflowMultiRootProjectConfig(project_roots={})

    def _root_config_path(self, root: str) -> Path:
        root_file = BrickflowProjectConstants.DEFAULT_MULTI_PROJECT_ROOT_FILE_NAME.value
        return self._config_file.parent / root / root_file

    def _load_roots(self) -> Dict[str, BrickflowRootProjectConfig]:
        if self._brickflow_multi_project_config.project_roots is None:
            return {}
        roots = list(
            set(
                root.root_yaml_rel_path
                for root in self._brickflow_multi_project_config.project_roots.values()
            )
        )
        root_dict = {}
        for root in roots:
            with self._root_config_path(root).open("r", encoding="utf-8") as f:
                root_dict[root] = BrickflowRootProjectConfig.parse_obj(
                    yaml.safe_load(f.read())
                )
        return root_dict

    def root(self) -> Path:
        return self._config_file.parent

    def add_project(self, project: BrickflowProject) -> None:
        if self.project_exists(project) is True:
            raise ValueError(f"Project with name {project.name} already exists")
        self._brickflow_multi_project_config.project_roots[project.name] = ProjectRef(
            root_yaml_rel_path=project.path_from_repo_root_to_project_root
        )
        project_root_config = self._project_config_dict.get(
            project.path_from_repo_root_to_project_root,
            BrickflowRootProjectConfig(projects={}),
        )
        project_root_config.projects[project.name] = project
        self._project_config_dict[
            project.path_from_repo_root_to_project_root
        ] = project_root_config

    def project_exists(self, project: BrickflowProject) -> bool:
        return project.name in self._brickflow_multi_project_config.project_roots

    def get_project(self, project_name: str) -> BrickflowProject:
        project_path = self._brickflow_multi_project_config.project_roots[
            project_name
        ].root_yaml_rel_path
        project_root_config = self._project_config_dict[project_path]
        return project_root_config.projects[project_name]

    def get_project_ref(self, project_name: str) -> ProjectRef:
        return self._brickflow_multi_project_config.project_roots[project_name]

    def update_project(self, project: BrickflowProject) -> None:
        self._project_config_dict[project.path_from_repo_root_to_project_root].projects[
            project.name
        ] = project

    @staticmethod
    def set_current_project_settings(project: BrickflowProject) -> None:
        settings = BrickflowProjectDeploymentSettings()
        settings.brickflow_project_runtime_version = project.brickflow_version
        settings.brickflow_enable_plugins = project.enable_plugins
        settings.brickflow_project_name = project.name
        settings.brickflow_monorepo_path_to_bundle_root = (
            project.path_from_repo_root_to_project_root
        )

    def list_project_names(self) -> List[str]:
        return list(self._brickflow_multi_project_config.project_roots.keys())

    def list_projects(self) -> List[BrickflowProject]:
        return [
            project
            for project_root in self._project_config_dict.values()
            for project in project_root.projects.values()
        ]

    def remove_project(self, project_name: str) -> None:
        project_path = self._brickflow_multi_project_config.project_roots[
            project_name
        ].root_yaml_rel_path
        self._project_config_dict[project_path].projects.pop(project_name, None)
        self._brickflow_multi_project_config.remove(project_name)

    def persist_project_path(self, project_root_path: str) -> None:
        with self._root_config_path(project_root_path).open("w", encoding="utf-8") as f:
            f.write(
                "# DO NOT MODIFY THIS FILE - IT IS AUTO GENERATED BY BRICKFLOW AND RESERVED FOR FUTURE USAGE\n"
            )
            yaml.dump(self._project_config_dict[project_root_path].dict(), f)
        self.save()

    def save_project(self, project: BrickflowProject) -> None:
        project_root_path = project.path_from_repo_root_to_project_root
        self.persist_project_path(project_root_path)

    def save(self) -> None:
        with self._config_file.open("w", encoding="utf-8") as f:
            yaml.dump(self._brickflow_multi_project_config.dict(), f)


class BrickflowRootNotFound(Exception):
    pass


def get_brickflow_root(current_path: Optional[Path] = None) -> Path:
    current_dir = Path(current_path or get_notebook_ws_path(ctx.dbutils) or os.getcwd())
    potential_config_file_path = (
        current_dir
        / BrickflowProjectConstants.DEFAULT_MULTI_PROJECT_CONFIG_FILE_NAME.value
    )
    if potential_config_file_path.exists():
        return potential_config_file_path
    elif current_dir.parent == current_dir:
        # Reached the filesystem root, return just raw file value
        return Path(
            BrickflowProjectConstants.DEFAULT_MULTI_PROJECT_CONFIG_FILE_NAME.value
        )
    else:
        return get_brickflow_root(current_dir.parent)


multi_project_manager = MultiProjectManager(config_file_name=str(get_brickflow_root()))


def initialize_project_entrypoint(
    project_name: str,
    git_https_url: str,
    workflows_dir: str,
    brickflow_version: str,
    spark_expectations_version: str,
) -> None:
    workflows_dir_p = Path(workflows_dir)
    workflows_dir_p.mkdir(
        parents=True, exist_ok=True
    )  # create dir if it does not exist
    # make __init__.py at where the template will be rendered
    Path(workflows_dir_p / "__init__.py").touch(mode=0o755)

    create_entry_point(
        workflows_dir,
        render_template(
            project_name=project_name,
            git_provider="github",
            git_https_url=git_https_url,
            pkg=_validate_package(workflows_dir),
            brickflow_version=brickflow_version,
            spark_expectations_version=spark_expectations_version,
        ),
    )


@click.group()
def projects() -> None:
    """Manage one to many brickflow projects"""
    pass


@contextlib.contextmanager
def use_project(
    name: str,
    project: BrickflowProject,
    brickflow_root: Optional[Path] = None,
    project_root_dir: Optional[str] = None,
) -> Generator[None, None, None]:
    # if no directory is provided do nothing
    if brickflow_root is not None and project_root_dir is not None:
        current_directory = os.getcwd()
        project_path = str(brickflow_root / project_root_dir)
        _ilog.info("Changed to directory: %s", project_path)
        os.chdir(brickflow_root / project_root_dir)
        os.environ[BrickflowEnvVars.BRICKFLOW_PROJECT_NAME.value] = name
        multi_project_manager.set_current_project_settings(project)
        try:
            yield
        finally:
            os.environ.pop(BrickflowEnvVars.BRICKFLOW_PROJECT_NAME.value, None)
            os.chdir(current_directory)
    else:
        yield


@projects.command()
@click.option("--name", prompt="Project name", help="Name of the project")
@click.option(
    "--path-from-repo-root-to-project-root",
    prompt="Path from repo root to project root (optional)",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    help="Path from repo root to project root",
    default=".",
)
@click.option(
    "--path-project-root-to-workflows-dir",
    prompt="Path from project root to workflows dir",
    type=str,
    help="Path from project root to workflows dir",
)
@click.option(
    "-g",
    "--git-https-url",
    type=str,
    prompt=INTERACTIVE_MODE,
    help="Provide the github URL for your project, example: https://github.com/nike-eda-apla/brickflow",
)
@click.option(
    "-bfv",
    "--brickflow-version",
    default=DEFAULT_BRICKFLOW_VERSION_MODE,
    type=str,
    prompt=INTERACTIVE_MODE,
)
@click.option(
    "-sev",
    "--spark-expectations-version",
    default="0.5.0",
    type=str,
    prompt=INTERACTIVE_MODE,
)
@click.option(
    "--skip-entrypoint",
    is_flag=True,
    default=False,
    type=bool,
    help="Skip creating entrypoint.py file",
    prompt=INTERACTIVE_MODE,
)
def add(
    name: str,
    path_from_repo_root_to_project_root: str,
    path_project_root_to_workflows_dir: str,
    git_https_url: str,
    brickflow_version: str,
    spark_expectations_version: str,
    skip_entrypoint: bool,
) -> None:
    """Adds a project to the brickflow-multi-project.yml file and a entrypoint.py file in workflows dir"""
    project = BrickflowProject(
        name=name,
        path_from_repo_root_to_project_root=path_from_repo_root_to_project_root,
        path_project_root_to_workflows_dir=path_project_root_to_workflows_dir,
        deployment_mode=BrickflowDeployMode.BUNDLE.value,
    )
    multi_project_manager.add_project(project)

    _create_gitignore_if_not_exists()
    _update_gitignore()

    with use_project(
        name,
        project,
        multi_project_manager.root(),
        project.path_from_repo_root_to_project_root,
    ):
        if skip_entrypoint is False:
            initialize_project_entrypoint(
                project.name,
                git_https_url,
                project.path_project_root_to_workflows_dir,
                brickflow_version,
                spark_expectations_version,
            )
        create_brickflow_project_root_marker()

    # commit project after entrypoint
    multi_project_manager.save_project(project)


@projects.command()
@click.option(
    "--name",
    prompt="Project name",
    help="Name of the project",
    type=click.Choice(multi_project_manager.list_project_names()),
)
def remove(name: str) -> None:
    """Removes a project from the brickflow-multi-project.yml file"""
    # get project, remove it from the in memory state and persist the project and the main yaml file
    project = multi_project_manager.get_project(name)
    multi_project_manager.remove_project(name)
    multi_project_manager.persist_project_path(
        project.path_from_repo_root_to_project_root
    )
    multi_project_manager.save()
    click.echo(f"Project {name} removed.")


@projects.command(name="list")
def list_proj_names() -> None:
    """Lists all projects in the brickflow-multi-project.yml file"""
    click.echo("Projects List: \n")
    for prj in multi_project_manager.list_projects():
        click.echo(
            f"Project Name: {prj.name}; Project Path: {prj.path_project_root_to_workflows_dir}"
        )


def apply_bundles_deployment_options(
    cmd: Optional[Callable] = None, exclude_options: Optional[List[str]] = None
) -> Callable[..., Any]:
    options = {
        "env": click.option(
            "--env",
            "-e",
            default=BrickflowDefaultEnvs.LOCAL.value,
            type=str,
            callback=bind_env_var(BrickflowEnvVars.BRICKFLOW_ENV.value),
            help="Set the environment value, certain tags [TBD] get added to the workflows based on this value.",
        ),
        "project": click.option(
            "--project",
            type=click.Choice(multi_project_manager.list_project_names()),
            prompt=INTERACTIVE_MODE,
            help="Select the project of workflows you would like to deploy.",
        ),
        "profile": click.option(
            "--profile",
            "-p",
            default=None,
            type=str,
            callback=bind_env_var(
                BrickflowEnvVars.BRICKFLOW_DATABRICKS_CONFIG_PROFILE.value
            ),
            help="The databricks profile to use for authenticating to databricks during deployment.",
        ),
        "auto-approve": click.option(
            "--auto-approve",
            type=bool,
            is_flag=True,
            show_default=True,
            default=False,
            help="Auto approve brickflow pipeline without being prompted to approve.",
        ),
        "skip-libraries": click.option(
            "--skip-libraries",
            type=bool,
            is_flag=True,
            show_default=True,
            default=False,
            help="Skip automatically adding brickflow libraries.",
        ),
        "force-acquire-lock": click.option(
            "--force-acquire-lock",
            type=bool,
            is_flag=True,
            show_default=True,
            default=False,
            help="Force acquire lock for databricks bundles destroy.",
        ),
        "workflow": click.option(
            "--workflow",
            "-w",
            type=str,
            multiple=True,
            callback=bind_env_var(
                BrickflowEnvVars.BRICKFLOW_DEPLOY_ONLY_WORKFLOWS.value
            ),
            help="""Provide the workflow names (local mode only) to deploy, each workflow separated by space!
            Note: provide the workflow names without the env prefix or the file extension.
            Example: bf projects deploy -p DEFAULT -e local -w wf1 -w wf2""",
        ),
        "--key-value": click.option(
            "--key-value",
            "-kv",
            type=str,
            multiple=True,
            callback=bind_env_var(BrickflowEnvVars.BRICKFLOW_PROJECT_PARAMS.value),
            help="""Provide the runtime key-value parameters, each key-value separated by space!
        Example: bf projects deploy -p DEFAULT -e local -kv key1=value1 -kv key2=value2""",
        ),
        "--tag": click.option(
            "--tag",
            "-t",
            type=str,
            multiple=True,
            callback=bind_env_var(BrickflowEnvVars.BRICKFLOW_PROJECT_TAGS.value),
            help="""Provide the runtime key-value tags, each key-value separated by space!
        Example: bf projects deploy -p DEFAULT -e local -t t_key1=value1 -kv t_key2=value2""",
        ),
    }

    def _apply_bundles_deployment_options(func: Callable) -> Callable[..., Any]:
        _func = func
        for key, option in options.items():
            if key is not None and key not in (exclude_options or []):
                _func = option(_func)
        return _func

    if cmd is not None:
        if callable(cmd):
            return _apply_bundles_deployment_options(cmd)

    return _apply_bundles_deployment_options


def handle_libraries(skip_libraries: Optional[bool] = None, **_: Any) -> None:
    if skip_libraries is True:
        BrickflowProjectDeploymentSettings().brickflow_auto_add_libraries = False
    else:
        BrickflowProjectDeploymentSettings().brickflow_auto_add_libraries = True


@projects.command(name="destroy")
@apply_bundles_deployment_options
def destroy_project(project: str, **kwargs: Any) -> None:
    """Destroys the deployed resources and workflows in databricks for the project"""
    bf_project = multi_project_manager.get_project(project)
    dir_to_change = multi_project_manager.get_project_ref(project).root_yaml_rel_path
    handle_libraries(**kwargs)
    with use_project(project, bf_project, multi_project_manager.root(), dir_to_change):
        bundle_destroy(
            workflows_dir=bf_project.path_project_root_to_workflows_dir, **kwargs
        )


@pre_bundle_hook
def project_synth(**_: Any) -> None:
    # empty stub to invoke the pre_bundle_hook
    pass


@projects.command(name="sync")
@click.option(
    "--watch",
    type=bool,
    is_flag=True,
    show_default=True,
    default=False,
    help="Enable filewatcher to sync files over.",
)
@click.option(
    "--full",
    type=bool,
    is_flag=True,
    show_default=True,
    default=False,
    help="Run a full sync.",
)
@click.option(
    "--interval-duration",
    type=str,
    show_default=True,
    default=None,
    help="File system polling interval (for --watch).",
)
@click.option(
    "--debug",
    type=bool,
    is_flag=True,
    show_default=True,
    default=False,
    help="Enable debug logs",
)
@apply_bundles_deployment_options
def sync_project(project: str, **kwargs: Any) -> None:
    """Sync project file tree into databricks workspace from local.
    It is only one way from local to databricks workspace."""
    bf_project = multi_project_manager.get_project(project)
    dir_to_change = multi_project_manager.get_project_ref(project).root_yaml_rel_path
    handle_libraries(**kwargs)
    with use_project(project, bf_project, multi_project_manager.root(), dir_to_change):
        bundle_sync(
            workflows_dir=bf_project.path_project_root_to_workflows_dir, **kwargs
        )


@projects.command(name="synth")
@apply_bundles_deployment_options(
    exclude_options=[
        "auto-approve",
        "force-acquire-lock",
    ]
)
def synth_bundles_for_project(project: str, **kwargs: Any) -> None:
    """Synth the bundle.yml for project"""
    bf_project = multi_project_manager.get_project(project)
    dir_to_change = multi_project_manager.get_project_ref(project).root_yaml_rel_path
    handle_libraries(**kwargs)
    with use_project(project, bf_project, multi_project_manager.root(), dir_to_change):
        # wf dir is required for generating the bundle.yml in the workflows dir
        project_synth(
            workflows_dir=bf_project.path_project_root_to_workflows_dir, **kwargs
        )
    _ilog.info("SUCCESSFULLY SYNTHESIZED BUNDLE.YML FOR PROJECT %s", project)


@projects.command(name="deploy")
@apply_bundles_deployment_options
def deploy_project(project: str, **kwargs: Any) -> None:
    """Deploy the resources and workflows to databricks for the project
    configured in the brickflow-project-root.yml file"""
    bf_project = multi_project_manager.get_project(project)
    dir_to_change = multi_project_manager.get_project_ref(project).root_yaml_rel_path
    handle_libraries(**kwargs)
    with use_project(project, bf_project, multi_project_manager.root(), dir_to_change):
        bundle_deploy(
            workflows_dir=bf_project.path_project_root_to_workflows_dir, **kwargs
        )
