from __future__ import annotations

import logging
import os
import os.path
import webbrowser
from typing import Optional, Callable, List, Any, Dict

import click
from click import ClickException
from decouple import config

from brickflow import (
    BrickflowEnvVars,
    BrickflowDefaultEnvs,
    _ilog,
)
from brickflow.cli.bundles import (
    bundle_cli_setup,
)
from brickflow.cli.commands import exec_command
from brickflow.cli.configure import (
    bind_env_var,
    log_important_versions,
)
from brickflow.cli.constants import BrickflowDeployMode, INTERACTIVE_MODE
from brickflow.cli.projects import projects


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


class BundleCmd(click.Group):
    def get_command(self, ctx: click.Context, cmd_name: str) -> Optional[click.Command]:
        # during entry of command enable logging
        _ilog.setLevel(logging.INFO)

        if cmd_name == BrickflowDeployMode.BUNDLE.value:
            return bundles_proxy_command()
        else:
            rv = click.Group.get_command(self, ctx, cmd_name)
            if rv is not None:
                return rv
            raise ctx.fail(f"No such command '{cmd_name}'.")


@click.group(invoke_without_command=True, no_args_is_help=True, cls=BundleCmd)
@click.version_option(package_name="brickflows")
def cli() -> None:
    """CLI for managing Databricks Workflows"""


cli.add_command(projects)  # type: ignore


@cli.command
def docs() -> None:
    """Use to open docs in your browser"""
    docs_site = "https://engineering.nike.com/brickflow/"
    webbrowser.open(docs_site, new=2)
    click.echo(f"Opening browser for docs... site: {docs_site}")


@cli.command
def bundle() -> None:
    """CLI for proxying to databricks bundles cli"""
    # Hack for having bundle show up as a command in brickflow
    # with documentation.
    pass  # pragma: no cover


def bundle_env_set_options(f: Callable) -> Callable:
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

    def set_up_bundle_for_workflow_dir(
        ctx: click.Context, param: str, value: Any  # pylint: disable=unused-argument
    ) -> None:  # noqa
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
            callback=set_up_bundle_for_workflow_dir,
            help="Provide the workflow directory that has to be deployed",
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


def get_deployment_mode(**kwargs: Dict[str, Any]) -> BrickflowDeployMode:
    # set deployment mode for bundle
    os.environ[BrickflowEnvVars.BRICKFLOW_DEPLOYMENT_MODE.value] = str(
        kwargs.get("deploy_mode", BrickflowDeployMode.BUNDLE.value)
    )
    if (
        kwargs.get("deploy_mode", BrickflowDeployMode.BUNDLE.value)
        == BrickflowDeployMode.BUNDLE.value
    ):
        return BrickflowDeployMode.BUNDLE
    else:
        raise ClickException(
            "Unsupported deploy mode for sync; currently only supports bundle deploy mode."
        )


def disable_project_name_in_env() -> None:
    # TODO: delete this when deploy commands are gone
    # used for legacy bundles deploy and destroy commands
    # disable multiple projects in same directory
    os.environ[BrickflowEnvVars.BRICKFLOW_USE_PROJECT_NAME.value] = "False"
