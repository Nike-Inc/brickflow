from __future__ import annotations

import functools
import io
import os
import os.path
import platform
import subprocess
import webbrowser
import zipfile
from enum import Enum
from pathlib import Path
from typing import Optional, Tuple, Callable, Union, List, Any, Dict

import click
import requests
from click import ClickException
from decouple import config

from brickflow import (
    BrickflowEnvVars,
    BrickflowDefaultEnvs,
    get_brickflow_version,
    _ilog,
)
from brickflow import ctx as brickflow_ctx
from brickflow.cli.configure import (
    _update_gitignore,
    _validate_package,
    render_template,
    create_entry_point,
    idempotent_cdktf_out,
    _create_gitignore_if_not_exists,
)

INTERACTIVE_MODE = config(
    BrickflowEnvVars.BRICKFLOW_INTERACTIVE_MODE.value, default=True, cast=bool
)

LOG_PACKAGE = "brickflow.cli"


class BrickflowDeployMode(Enum):
    CDKTF = "cdktf"
    BUNDLE = "bundle"


def exec_command(
    path_to_executable: str,
    base_command: Optional[str],
    args: Union[Tuple[str] | List[str]],
    capture_output: bool = False,
) -> Optional[str]:
    os.environ["PYTHONPATH"] = os.getcwd()
    my_env = os.environ.copy()
    try:
        _args = list(args)
        # add a base command if its provided for proxying for brickflow deploy
        if base_command is not None:
            _args = [base_command] + _args
        _ilog.info("Executing command: %s", " ".join([path_to_executable, *_args]))

        if capture_output is True:
            res = subprocess.run(
                [path_to_executable, *_args],
                check=True,
                env=my_env,
                capture_output=True,
                text=True,
            )
            return res.stdout.strip()

        subprocess.run([path_to_executable, *_args], check=True, env=my_env)
    except subprocess.CalledProcessError as e:
        raise ClickException(str(e))

    return None


def exec_cdktf_command(
    base_command: Optional[str], args: Union[Tuple[str] | List[str]]
) -> None:
    os.environ["PYTHONPATH"] = os.getcwd()
    my_env = os.environ.copy()
    try:
        _args = list(args)
        # add a base command if its provided for proxying for brickflow deploy
        if base_command is not None:
            _args = [base_command] + _args
        subprocess.run(["cdktf", *_args], check=True, env=my_env)
    except subprocess.CalledProcessError as e:
        raise ClickException(str(e))


def cdktf_command(base_command: Optional[str] = None) -> click.Command:
    @click.command(
        name="cdktf_cmd",
        short_help="CLI for proxying to CDKTF cli.",
        context_settings={"ignore_unknown_options": True},
        add_help_option=False,
    )
    @click.argument("args", nargs=-1)
    def cmd(args: Tuple[str]) -> None:
        # check to make sure you are in project root and then set python path to whole dir
        exec_cdktf_command(base_command, args)

    return cmd


def bundles_proxy_command() -> click.Command:
    def run_bundle_command(args: Optional[List[str]] = None, **_: Any) -> None:
        bundle_cli_setup()
        bundle_cli = config(
            BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_EXEC.value, "databricks"
        )
        log_important_versions(bundle_cli)
        exec_command(bundle_cli, "bundle", args or [])

    @click.command(
        name="bundles_cmd",
        short_help="CLI for proxying to databricks bundles cli..",
        context_settings={"ignore_unknown_options": True},
        add_help_option=False,
    )
    @click.argument("args", nargs=-1)
    def cmd(args: List[str]) -> None:
        # check to make sure you are in project root and then set python path to whole dir
        run_bundle_command(args=args)

    return cmd


class CdktfCmd(click.Group):
    def get_command(self, ctx: click.Context, cmd_name: str) -> Optional[click.Command]:
        if cmd_name == "cdktf":
            return cdktf_command()
        elif cmd_name == "bundle":
            return bundles_proxy_command()
        # elif cmd_name in ["deploy", "diff"]:
        #     return cdktf_command(cmd_name)
        else:
            rv = click.Group.get_command(self, ctx, cmd_name)
            if rv is not None:
                return rv
            raise ctx.fail(f"No such command '{cmd_name}'.")


@click.group(invoke_without_command=True, no_args_is_help=True, cls=CdktfCmd)
@click.version_option(prog_name="brickflow")
def cli() -> None:
    """CLI for managing Databricks Workflows"""


@cli.command
@click.option("-n", "--project-name", type=str, prompt=INTERACTIVE_MODE)
@click.option(
    "-g",
    "--git-https-url",
    type=str,
    prompt=INTERACTIVE_MODE,
    help="Provide the github URL for your project, example: https://github.com/Nike-Inc/brickflow",
)
@click.option(
    "-wd",
    "--workflows-dir",
    default="src/workflows",
    type=click.Path(exists=False, file_okay=False),
    prompt=INTERACTIVE_MODE,
)
@click.option(
    "-bfv",
    "--brickflow-version",
    default=get_brickflow_version(),
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
def init(
    project_name: str,
    git_https_url: str,
    workflows_dir: str,
    brickflow_version: str,
    spark_expectations_version: str,
) -> None:
    """Initialize your project with Brickflow..."""
    try:
        workflows_dir_p = Path(workflows_dir)
        workflows_dir_p.mkdir(
            parents=True, exist_ok=True
        )  # create dir if it does not exist
        # make __init__.py at where the template will be rendered
        Path(workflows_dir_p / "__init__.py").touch(mode=0o755)

        _create_gitignore_if_not_exists()
        _update_gitignore()

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
    except Exception as e:
        raise ClickException(
            "An Exception occurred. Please make sure you create a .gitignore file in the root directory."
        ) from e


@cli.command
def docs() -> None:
    """Use to open docs in your browser..."""
    docs_site = "https://verbose-garbanzo-6b8a1ae2.pages.github.io/"
    webbrowser.open(docs_site, new=2)
    click.echo(f"Opening browser for docs... site: {docs_site}")


@cli.command
def cdktf() -> None:
    """CLI for proxying to cdktf cli."""
    # Hack for having cdktf show up as a command in brickflow
    # with documentation.
    pass  # pragma: no cover


@cli.command
def bundle() -> None:
    """CLI for proxying to databricks bundles cli."""
    # Hack for having bundle show up as a command in brickflow
    # with documentation.
    pass  # pragma: no cover


def cdktf_env_set_options(f: Callable) -> Callable:
    def bind_env_var(env_var: str) -> Callable:
        def callback(
            ctx: click.Context,  # noqa
            param: str,  # noqa
            value: Any,
        ) -> None:
            # pylint: disable=unused-argument
            if value is not None:
                _ilog.info("Setting env var: %s to %s...", env_var, value)
                os.environ[env_var] = (
                    str(value).lower() if isinstance(value, bool) else value
                )

        return callback

    def local_mode_callback(ctx: click.Context, param: str, value: Any) -> None:  # noqa
        # pylint: disable=unused-argument
        if value is not None and value is True:
            _ilog.info(
                "Configuring environment to %s...",
                BrickflowDefaultEnvs.LOCAL.value,
            )
            os.environ[
                BrickflowEnvVars.BRICKFLOW_ENV.value
            ] = BrickflowDefaultEnvs.LOCAL.value

    def deploy_only_workflows(
        ctx: click.Context, param: str, value: Any
    ) -> None:  # noqa
        # pylint: disable=unused-argument
        if value:
            for file in value:
                if file[-3:] != ".py":
                    raise ClickException("Should pass only python files as workflows")
            _ilog.info("Brickflow will only deploy workflows: %s", ", ".join(value))
            os.environ[
                BrickflowEnvVars.BRICKFLOW_DEPLOY_ONLY_WORKFLOWS.value
            ] = ",".join(value)

    def set_up_cdktf_for_workflow_dir(
        ctx: click.Context, param: str, value: Any  # noqa
    ) -> None:
        if value is not None:
            return value

    options = [
        click.option(
            "--local-mode",
            "-l",
            is_flag=True,
            callback=local_mode_callback,
            help="Set the environment flag to local and other components [TBD] are disabled in local mode.",
        ),
        click.option(
            "--workflows-dir",
            "-wd",
            type=click.Path(exists=True, file_okay=False),
            prompt=INTERACTIVE_MODE,
            callback=set_up_cdktf_for_workflow_dir,
            help="Provide the workflow directory that has to be deployed",
        ),
        click.option(
            "--workflow",
            "-w",
            type=str,
            multiple=True,
            callback=deploy_only_workflows,
            help="""Provide the workflow file names which you want to deploy, each file name separated by space!
                    Example: bf deploy -p DEFAULT -l -w wf1.py -w wf2.py""",
        ),
        click.option(
            "--env",
            "-e",
            default=BrickflowDefaultEnvs.LOCAL.value,
            type=str,
            callback=bind_env_var(BrickflowEnvVars.BRICKFLOW_ENV.value),
            help="Set the environment value, certain tags [TBD] get added to the workflows based on this value.",
        ),
        click.option(
            "--repo-url",
            "-r",
            default=None,
            type=str,
            callback=bind_env_var(BrickflowEnvVars.BRICKFLOW_GIT_REPO.value),
            help="The github url in which to run brickflow with.",
        ),
        click.option(
            "--git-ref",
            default=None,
            type=str,
            callback=bind_env_var(BrickflowEnvVars.BRICKFLOW_GIT_REF.value),
            help="The commit/tag/branch to use in github.",
        ),
        click.option(
            "--git-provider",
            default=None,
            type=str,
            callback=bind_env_var(BrickflowEnvVars.BRICKFLOW_GIT_PROVIDER.value),
            help="The github provider for brickflow this is used for configuring github on DBX jobs.",
        ),
        click.option(
            "--profile",
            "-p",
            default=None,
            type=str,
            callback=bind_env_var(
                BrickflowEnvVars.BRICKFLOW_DATABRICKS_CONFIG_PROFILE.value
            ),
            help="The databricks profile to use for authenticating to databricks during deployment.",
        ),
    ]
    for option in options:
        f = option(f)
    return f


def get_cdktf_specific_args(**kwargs: Dict[str, Any]) -> List[str]:
    args = []
    if kwargs.get("auto_approve", False) is True:
        args.append("--auto-approve")
    return args


def bundle_cli_setup() -> None:
    # handle download bundle cli
    if config(BrickflowEnvVars.BRICKFLOW_BUNDLE_NO_DOWNLOAD.value, False, cast=bool):
        _ilog.info("Skipping bundle download...")
        return
    brickflow_bundle_version = config(
        BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_VERSION.value, "0.200.0"
    )
    cli_download_url = bundle_download_path(brickflow_bundle_version)
    path = download_and_unzip_databricks_cli(cli_download_url, brickflow_bundle_version)
    os.environ[BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_EXEC.value] = path


def get_deployment_mode(**kwargs: Dict[str, Any]) -> BrickflowDeployMode:
    # set deployment mode for cdktf or bundle
    os.environ[BrickflowEnvVars.BRICKFLOW_DEPLOYMENT_MODE.value] = str(
        kwargs.get("deploy_mode", "cdktf")
    )
    kwargs.get("deploy_mode", "cdktf")
    if kwargs.get("deploy_mode", "cdktf") == "cdktf":
        return BrickflowDeployMode.CDKTF
    else:
        return BrickflowDeployMode.BUNDLE


@cli.command
@click.option(
    "--auto-approve",
    type=bool,
    is_flag=True,
    show_default=True,
    default=False,
    help="Auto approve brickflow pipeline without being prompted to approve.",
)
@click.option(
    "--deploy-mode",
    type=click.Choice(["cdktf", "bundle"]),
    show_default=True,
    default="cdktf",
    help="Which deployment framework to use to deploy.",
)
@click.option(
    "--force-acquire-lock",
    type=bool,
    is_flag=True,
    show_default=True,
    default=False,
    help="Force acquire lock for databricks bundles deploy.",
)
@cdktf_env_set_options
def deploy(**kwargs: Any) -> None:
    """CLI for deploying workflow projects."""
    # Hack for having cdktf show up as a command in brickflow
    # with documentation.
    deploy_mode = get_deployment_mode(**kwargs)
    if deploy_mode == BrickflowDeployMode.CDKTF:
        make_cdktf_json(**kwargs)
        exec_cdktf_command("deploy", get_cdktf_specific_args(**kwargs))
    else:
        bundle_deploy(**kwargs)
    # pass  # pragma: no cover


@cli.command
@cdktf_env_set_options
def diff(**kwargs: Any) -> None:
    """CLI for identifying diff in projects (only cdktf supported)."""
    # Hack for having cdktf show up as a command in brickflow
    # with documentation.
    make_cdktf_json(**kwargs)
    exec_cdktf_command("diff", [])


@cli.command
@click.option(
    "--auto-approve",
    type=bool,
    is_flag=True,
    show_default=True,
    default=False,
    help="Auto approve brickflow pipeline without being prompted to approve.",
)
@click.option(
    "--deploy-mode",
    type=click.Choice(["cdktf", "bundle"]),
    show_default=True,
    default="cdktf",
    help="Which deployment framework to use to deploy.",
)
@click.option(
    "--force-acquire-lock",
    type=bool,
    is_flag=True,
    show_default=True,
    default=False,
    help="Force acquire lock for databricks bundles destroy.",
)
@cdktf_env_set_options
def destroy(**kwargs: Any) -> None:
    """CLI for destroying workflow projects."""
    # Hack for having cdktf show up as a command in brickflow
    # with documentation.
    deploy_mode = get_deployment_mode(**kwargs)

    if deploy_mode == BrickflowDeployMode.CDKTF:
        make_cdktf_json(**kwargs)
        exec_cdktf_command("destroy", get_cdktf_specific_args(**kwargs))
    else:
        bundle_destroy(**kwargs)


@cli.command
@click.option(
    "--deploy-mode",
    type=click.Choice(["bundle"]),
    show_default=True,
    default="bundle",
    help="Which deployment framework to use to deploy.",
)
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
    type=str,
    show_default=True,
    default=None,
    help="File system polling interval (for --watch).",
)
@cdktf_env_set_options
def sync(**kwargs: Any) -> None:
    """Synchronize your bundle tree to databricks workspace (only supported by bundle deployment mode)."""
    deploy_mode = get_deployment_mode(**kwargs)
    if deploy_mode == BrickflowDeployMode.BUNDLE:
        bundle_sync(**kwargs)
    else:
        raise ClickException(
            "Unsupported deploy mode for sync; currently only supports bundle deploy mode."
        )


def get_entrypoint(**kwargs: Any) -> str:
    wd: Optional[str] = kwargs.get("workflows_dir")
    if wd is None:
        raise ValueError(
            "workflows_dir not set, please set it using --workflows-dir or -wd"
        )
    return str(Path(wd) / "entrypoint.py")


def make_cdktf_json(**kwargs: Any) -> None:
    wd: Optional[str] = kwargs.get("workflows_dir")
    if wd is None:
        raise ValueError(
            "workflows_dir not set, please set it using --workflows-dir or -wd"
        )
    idempotent_cdktf_out(wd)


def bundle_synth(**kwargs: Any) -> None:
    entrypoint_file = get_entrypoint(**kwargs)
    os.environ[BrickflowEnvVars.BRICKFLOW_MODE.value] = "deploy"
    _ilog.info("Synthesizing bundle...")
    exec_command("python", entrypoint_file, [])


def log_important_versions(bundle_cli: str) -> None:
    version = exec_command(bundle_cli, "--version", [], capture_output=True)
    _ilog.info("Using bundle version: %s", version)
    log_python_version()


def log_python_version() -> None:
    version = exec_command("python", "--version", [], capture_output=True)
    _ilog.info("Using python version: %s", version)


def pre_bundle_hook(f: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(f)
    def wrapped_bundle_func(*args: Any, **kwargs: Any) -> None:
        bundle_cli_setup()
        bundle_cli = config(
            BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_EXEC.value, "databricks"
        )
        log_important_versions(bundle_cli)
        bundle_synth(**kwargs)
        return f(*args, **kwargs, bundle_cli=bundle_cli)

    return wrapped_bundle_func


def get_valid_bundle_cli(bundle_cli: Optional[str]) -> str:
    if bundle_cli is None:
        return "databricks"
    return bundle_cli


@pre_bundle_hook
def bundle_validate(bundle_cli: Optional[str] = None, **_: Any) -> None:
    """CLI validate the bundle."""
    exec_command(
        get_valid_bundle_cli(bundle_cli),
        "bundle",
        ["validate", "-e", brickflow_ctx.env],
    )


@pre_bundle_hook
def bundle_sync(
    bundle_cli: Optional[str] = None,
    watch: bool = False,
    debug: bool = False,
    interval_duration: Optional[int] = None,
    full: bool = False,
    **_: Any,
) -> None:
    """CLI deploy the bundle."""
    additional_args = []
    if full is True:
        additional_args.append("--full")
    if watch is True:
        additional_args.append("--watch")
    if interval_duration is not None:
        additional_args.append("--interval-duration")
        additional_args.append(str(interval_duration))
    if debug is True:
        additional_args.append("--log-level")
        additional_args.append("debug")

    exec_command(
        get_valid_bundle_cli(bundle_cli),
        "bundle",
        ["sync", "-e", brickflow_ctx.env, *additional_args],
    )


@pre_bundle_hook
def bundle_deploy(
    bundle_cli: Optional[str] = None, force_acquire_lock: bool = False, **_: Any
) -> None:
    """CLI deploy the bundle."""
    deploy_args = ["deploy", "-e", brickflow_ctx.env]
    if force_acquire_lock is True:
        deploy_args.append("--force")
    exec_command(get_valid_bundle_cli(bundle_cli), "bundle", deploy_args)


@pre_bundle_hook
def bundle_destroy(
    bundle_cli: Optional[str] = None,
    force_acquire_lock: bool = False,
    auto_approve: bool = False,
    **_: Any,
) -> None:
    """CLI destroy the bundle."""
    destroy_args = ["destroy", "-e", brickflow_ctx.env]
    if auto_approve is True:
        destroy_args.append("--auto-approve")
    if force_acquire_lock is True:
        destroy_args.append("--force")

    exec_command(get_valid_bundle_cli(bundle_cli), "bundle", destroy_args)


def get_arch() -> str:
    architecture = platform.machine()

    if architecture in ("i386", "i686"):
        architecture = "386"
    elif architecture == "x86_64":
        architecture = "amd64"
    elif architecture.startswith("arm"):
        architecture = "arm64"
    return architecture


def bundle_download_path(version: str) -> str:
    system = platform.system().lower()
    arch = get_arch()
    if version == "snapshot":
        return (
            f"https://github.com/databricks/cli/releases/download/"
            f"{version}/databricks_cli_{system}_{arch}.zip"
        )

    return (
        f"https://github.com/databricks/cli/releases/download/"
        f"v{version}/databricks_cli_{version}_{system}_{arch}.zip"
    )


def download_url(url: str) -> requests.Response:
    try:
        return requests.get(
            url, timeout=60
        )  # Set a suitable timeout value (e.g., 10 seconds)
    except requests.exceptions.Timeout:
        _ilog.error("Request timed out. Failed to download the file.")
        raise
    except requests.exceptions.RequestException as e:
        _ilog.error("An error occurred while downloading the file: %s", e)
        raise


def download_and_unzip_databricks_cli(url: str, version: str) -> str:
    save_directory = os.path.join(".databricks/bin/cli", version)
    databricks_file_path = os.path.join(save_directory, "databricks")
    if os.path.exists(databricks_file_path):
        _ilog.info("Databricks cli already exists. Skipping download.")
        return databricks_file_path

    # Download the file using requests
    response = download_url(url)
    if response.status_code != 200:
        _ilog.error(
            "Failed to download the file from %s. Error code: %s",
            url,
            response.status_code,
        )
        raise ClickException(f"Unable to download databricks cli from: {url}")

    # Create an in-memory byte buffer
    file_bytes = io.BytesIO(response.content)

    # Unzip the files from the byte buffer
    with zipfile.ZipFile(file_bytes, "r") as zip_ref:
        for file in zip_ref.namelist():
            # Extract the file name from the path
            file_name = os.path.basename(file)

            # Create the .databricks/bin/<version> directory if it doesn't exist
            os.makedirs(save_directory, exist_ok=True)

            # Save the file in .databricks/bin/<version> directory
            save_path = os.path.join(save_directory, file_name)
            with open(save_path, "wb") as output_file:
                output_file.write(zip_ref.read(file))

            _ilog.info(
                "File '%s' downloaded and saved in .databricks/bin/cli/%s directory.",
                file_name,
                version,
            )

            # Set the 'databricks' file to be executable
            if file_name == "databricks":
                os.chmod(save_path, 0o755)
                _ilog.info("File '%s' set as executable.", file_name)
                databricks_file_path = os.path.abspath(save_path)

    return databricks_file_path
