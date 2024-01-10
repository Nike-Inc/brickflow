import os

try:
    from brickflow import BrickflowEnvVars
    from brickflow.cli import bundle_cli_setup
    from brickflow.cli.bundles import get_valid_bundle_cli
    from brickflow.engine import _call
except ImportError:
    raise ImportError("Please install brickflow to use this script")

if __name__ == "__main__":
    cli_version = os.environ.get("BUNDLE_CODE_GEN_CLI_VERSION", None)
    if cli_version is not None and cli_version != "":
        os.environ[BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_VERSION.value] = cli_version

    bundle_cli_setup()
    bundle_cli = get_valid_bundle_cli(
        os.environ[BrickflowEnvVars.BRICKFLOW_BUNDLE_CLI_EXEC.value]
    )
    print(f"Using Databricks CLI: {bundle_cli}")
    print(_call(f"{bundle_cli} --version", shell=True).decode("utf-8"))
    _call(f"{bundle_cli} bundle schema > brickflow/bundles/schema.json", shell=True)
