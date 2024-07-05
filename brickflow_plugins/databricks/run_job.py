from typing import Union
from pydantic import SecretStr

from databricks.sdk import WorkspaceClient
from brickflow.context import ctx
from brickflow.engine.utils import get_job_id


class RunJobInRemoteWorkspace:
    """
    Currently Databricks does not natively support running a job in a remote workspace via the RunJobTask.
    This plugin adds this functionality. However, it aims to be a temporary solution until Databricks adds this
    functionality natively.
    The plugin does not support neither passing the parameters to the remote job, nor waiting for the job to finish.

    Examples
    --------
        service_principle_pat = ctx.dbutils.secrets.get("scope", "service_principle_id")
        WorkflowDependencySensor(
            databricks_host=https://your_workspace_url.cloud.databricks.com,
            databricks_token=service_principle_pat,
            job_name="foo",
        )
        In the above snippet Databricks secrets are used as a secure service to store the databricks token.
        If you get your token from another secret management service, like AWS Secrets Manager, GCP Secret Manager
        or Azure Key Vault, just pass it in the databricks_token argument.
    """

    def __init__(
        self,
        databricks_host: str,
        databricks_token: Union[str, SecretStr],
        job_name: str,
    ):
        self.databricks_host = databricks_host
        self.databricks_token = (
            databricks_token
            if isinstance(databricks_token, SecretStr)
            else SecretStr(databricks_token)
        )
        self.job_name = job_name
        self._workspace_obj = WorkspaceClient(
            host=self.databricks_host, token=self.databricks_token.get_secret_value()
        )

    def execute(self):
        job_id = get_job_id(
            host=self.databricks_host,
            token=self.databricks_token,
            job_name=self.job_name,
        )
        # TODO: add support for passing parameters to the remote job
        # TODO: wait for the job to finish
        run = self._workspace_obj.jobs.run_now(job_id)
        ctx.log.info("Job run status: %s", run.response)
