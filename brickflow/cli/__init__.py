from __future__ import annotations

import logging
import os
import os.path
import webbrowser
from typing import Optional, Tuple, Callable, List, Any, Dict

import click
from click import ClickException
from decouple import config

from brickflow import (
    BrickflowEnvVars,
    BrickflowDefaultEnvs,
    _ilog,
)
from brickflow.cli.bundles import (
    bundle_sync,
    bundle_deploy,
    bundle_destroy,
    bundle_cli_setup,
)
from brickflow.cli.commands import exec_command, exec_cdktf_command
from brickflow.cli.configure import (
    idempotent_cdktf_out,
    bind_env_var,
    log_important_versions,
)
from brickflow.cli.constants import BrickflowDeployMode, INTERACTIVE_MODE
from brickflow.cli.projects import projects, init


def cdktf_command(base_command: Optional[str] = None) -> click.Command:
    @click.command(
        name="cdktf_cmd",
        short_help="CLI for proxying to CDKTF cli.",
        context_settings={"ignore_unknown_options": True},
        add_help_option=False,
        deprecated=True,
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
        # during entry of command enable logging
        _ilog.setLevel(logging.INFO)
        if cmd_name == BrickflowDeployMode.CDKTF.value:
            return cdktf_command()
        elif cmd_name == BrickflowDeployMode.BUNDLE.value:
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


cli.add_command(projects)  # type: ignore
# TODO: init is deprecated, remove in next major release
cli.add_command(init)  # type: ignore


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
            if (
                click.confirm(
                    "This can delete all of your other workflows that are already deployed? Are you sure?"
                )
                is False
            ):
                ctx.exit(0)
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


def get_deployment_mode(**kwargs: Dict[str, Any]) -> BrickflowDeployMode:
    # set deployment mode for cdktf or bundle
    os.environ[BrickflowEnvVars.BRICKFLOW_DEPLOYMENT_MODE.value] = str(
        kwargs.get("deploy_mode", BrickflowDeployMode.CDKTF.value)
    )
    if (
        kwargs.get("deploy_mode", BrickflowDeployMode.CDKTF.value)
        == BrickflowDeployMode.CDKTF.value
    ):
        return BrickflowDeployMode.CDKTF
    else:
        return BrickflowDeployMode.BUNDLE


def disable_project_name_in_env() -> None:
    # TODO: delete this when deploy commands are gone
    # used for legacy bundles deploy and destroy commands
    # disable multiple projects in same directory
    os.environ[BrickflowEnvVars.BRICKFLOW_USE_PROJECT_NAME.value] = "False"


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
        disable_project_name_in_env()
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
        disable_project_name_in_env()
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


def make_cdktf_json(**kwargs: Any) -> None:
    wd: Optional[str] = kwargs.get("workflows_dir")
    if wd is None:
        raise ValueError(
            "workflows_dir not set, please set it using --workflows-dir or -wd"
        )
    idempotent_cdktf_out(wd)
