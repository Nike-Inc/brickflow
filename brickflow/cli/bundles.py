from __future__ import annotations

import functools
import io
import os
import platform
import zipfile
from typing import Callable, Any, Optional

import requests
from click import ClickException
from decouple import config

from brickflow import (
    BrickflowEnvVars,
    ctx as brickflow_ctx,
    _ilog,
    get_bundles_project_env,
    get_entrypoint_python,
)
from brickflow.cli.constants import BrickflowDeployMode
from brickflow.cli.commands import exec_command
from brickflow.cli.configure import get_entrypoint, log_important_versions

ENV_FLAG = "-t"


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
        ["validate", ENV_FLAG, brickflow_ctx.env],
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
        ["sync", ENV_FLAG, get_bundles_project_env(), *additional_args],
    )


def get_force_lock_flag() -> str:
    version_parts = get_bundle_cli_version().split(".")
    # TODO: remove this logic on the major version
    if (
        len(version_parts) > 2
        and version_parts[0] == "0"
        and int(version_parts[1]) <= 202
    ):
        return "--force"
    return "--force-lock"


@pre_bundle_hook
def bundle_deploy(
    bundle_cli: Optional[str] = None, force_acquire_lock: bool = False, **_: Any
) -> None:
    """CLI deploy the bundle."""
    deploy_args = ["deploy", ENV_FLAG, get_bundles_project_env()]
    if force_acquire_lock is True:
        # fix/issue-32
        deploy_args.append(get_force_lock_flag())
    exec_command(get_valid_bundle_cli(bundle_cli), "bundle", deploy_args)


@pre_bundle_hook
def bundle_destroy(
    bundle_cli: Optional[str] = None,
    force_acquire_lock: bool = False,
    auto_approve: bool = False,
    **_: Any,
) -> None:
    """CLI destroy the bundle."""
    destroy_args = ["destroy", ENV_FLAG, get_bundles_project_env()]
    if auto_approve is True:
        destroy_args.append("--auto-approve")
    if force_acquire_lock is True:
        destroy_args.append(get_force_lock_flag())

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


def bundle_synth(**kwargs: Any) -> None:
    entrypoint_file = get_entrypoint(**kwargs)
    os.environ[
        BrickflowEnvVars.BRICKFLOW_DEPLOYMENT_MODE.value
    ] = BrickflowDeployMode.BUNDLE.value
    os.environ[BrickflowEnvVars.BRICKFLOW_MODE.value] = "deploy"
    _ilog.info("Synthesizing bundle...")
    exec_command(get_entrypoint_python(), entrypoint_file, [])


def get_bundle_cli_version() -> str:
    return config(BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_VERSION.value, "0.210.2")


def bundle_cli_setup() -> None:
    # handle download bundle cli
    if config(BrickflowEnvVars.BRICKFLOW_BUNDLE_NO_DOWNLOAD.value, False, cast=bool):
        _ilog.info("Skipping bundle download...")
        return
    brickflow_bundle_version = get_bundle_cli_version()
    cli_download_url = bundle_download_path(brickflow_bundle_version)
    path = download_and_unzip_databricks_cli(cli_download_url, brickflow_bundle_version)
    os.environ[BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_EXEC.value] = path
