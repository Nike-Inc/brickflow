import functools
import logging
import os
import time
from datetime import datetime, timedelta
from typing import Union
from warnings import warn

import requests
from pydantic import SecretStr
from requests.adapters import HTTPAdapter
from databricks.sdk import WorkspaceClient

from brickflow.context import ctx
from brickflow.engine.utils import get_job_id


class WorkflowDependencySensorException(Exception):
    pass


class WorkflowDependencySensorTimeOutException(TimeoutError):
    pass


class WorkflowDependencySensor:
    """
    This is used to have dependencies on the databricks workflow

    Example Usage in your brickflow task:
        service_principle_pat = ctx.dbutils.secrets.get("brickflow-demo-tobedeleted", "service_principle_id")
        WorkflowDependencySensor(
            databricks_host=https://your_workspace_url.cloud.databricks.com,
            databricks_token=service_principle_pat,
            dependency_job_id=job_id,
            poke_interval=20,
            timeout=60,
            delta=timedelta(days=1)
        )
        In above snippet Databricks secrets is used as a secure service to store the databricks token.
        If you get your token from another secret management service, like AWS Secrets Manager, GCP Secret Manager or Azure Key Vault,
        just pass it in the databricks_token argument.
    """

    def __init__(
        self,
        databricks_host: str,
        databricks_token: Union[str, SecretStr],
        delta: timedelta,
        timeout_seconds: int,
        dependency_job_id: int = None,
        dependency_job_name: str = None,
        poke_interval_seconds: int = 60,
    ):
        self.databricks_host = databricks_host
        self.databricks_token = (
            databricks_token
            if isinstance(databricks_token, SecretStr)
            else SecretStr(databricks_token)
        )
        self.poke_interval = poke_interval_seconds
        self.timeout = timeout_seconds
        self.delta = delta
        self.log = logging
        self.start_time = time.time()

        if dependency_job_id:
            warn(
                "Please use 'dependency_job_name' instead of 'dependency_job_id'",
                DeprecationWarning,
                stacklevel=2,
            )

        if not dependency_job_id and not dependency_job_name:
            raise WorkflowDependencySensorException(
                "Either dependency_job_id or dependency_job_name should be provided"
            )

        self.dependency_job_id = dependency_job_id
        self.dependency_job_name = dependency_job_name

        self._workspace_obj = WorkspaceClient(
            host=self.databricks_host, token=self.databricks_token.get_secret_value()
        )

    def get_retry_class(self, max_retries):
        from urllib3 import Retry

        log = self.log

        class LogRetry(Retry):
            """
            Adding extra logs before making a retry request
            """

            def __init__(self, *args, **kwargs):
                if (
                    kwargs.get("total", None) != max_retries
                    and kwargs.get("total", None) > 0
                ):
                    log.info(f"Retrying with kwargs: {kwargs}")
                super().__init__(*args, **kwargs)

        return LogRetry

    @functools.lru_cache(maxsize=None)
    def get_http_session(self):
        session = requests.Session()
        max_retries = int(os.getenv("DATABRICKS_REQUEST_RETRY_COUNT", 10))
        retries = self.get_retry_class(max_retries)(
            total=max_retries,
            backoff_factor=1,
            status_forcelist=[500, 501, 502, 503, 504, 429],
        )
        session.mount("https://", HTTPAdapter(max_retries=retries))
        session.mount("http://", HTTPAdapter(max_retries=retries))
        return session

    def get_execution_start_time_unix_milliseconds(self) -> int:
        run_id = ctx.dbutils_widget_get_or_else("brickflow_parent_run_id", None)
        if run_id is None:
            raise WorkflowDependencySensorException(
                "run_id is empty, brickflow_parent_run_id parameter is not found "
                "or no value present"
            )

        run = self._workspace_obj.jobs.get_run(run_id=run_id)

        # Convert Unix timestamp in milliseconds to datetime object to easily incorporate the delta
        start_time = datetime.fromtimestamp(run.start_time / 1000)
        execution_start_time = start_time - self.delta

        # Convert datetime object back to Unix timestamp in miliseconds
        execution_start_time_unix_miliseconds = int(
            execution_start_time.timestamp() * 1000
        )

        self.log.info(f"This workflow started at {start_time}")
        self.log.info(
            f"Going to check runs for job_id {self.dependency_job_id} from {execution_start_time} onwards"
        )
        self.log.info(
            f"{execution_start_time} in UNIX miliseconds is {execution_start_time_unix_miliseconds}"
        )
        return execution_start_time_unix_miliseconds

    @property
    def _get_job_id(self):
        return get_job_id(
            host=self.databricks_host,
            token=self.databricks_token,
            job_name=self.dependency_job_name,
        )

    def execute(self):
        if not self.dependency_job_id:
            self.dependency_job_id = self._get_job_id

        session = self.get_http_session()
        url = f"{self.databricks_host.rstrip('/')}/api/2.1/jobs/runs/list"
        headers = {
            "Authorization": f"Bearer {self.databricks_token.get_secret_value()}",
            "Content-Type": "application/json",
        }
        params = {
            "limit": 25,
            "job_id": self.dependency_job_id,
            "start_time_from": self.get_execution_start_time_unix_milliseconds(),
        }

        while True:
            page_index = 0
            has_more = True
            while has_more is True:
                resp = session.get(url, params=params, headers=headers).json()
                for run in resp.get("runs", []):
                    self.log.info(
                        f"Found the run_id: {run['run_id']}, and it's result_state is: {run.get('state', {}).get('result_state', None)}"
                    )
                    if run.get("state", {}).get("result_state", None) == "SUCCESS":
                        self.log.info(f"Found a successful run: {run['run_id']}")
                        return

                has_more = resp.get("has_more", False)
                if has_more:
                    params["page_token"] = resp["next_page_token"]
                self.log.info(
                    f"This is page_index: {page_index}, this is has_more: {has_more}"
                )
                page_index += 1

            self.log.info("Didn't find a successful run yet")
            if (
                self.timeout is not None
                and (time.time() - self.start_time) > self.timeout
            ):
                raise WorkflowDependencySensorTimeOutException(f"The job has timed out")

            self.log.info(f"sleeping for: {self.poke_interval}")
            time.sleep(self.poke_interval)


class WorkflowTaskDependencySensor(WorkflowDependencySensor):
    """
    This is used to have dependencies on the specific task within a databricks workflow

    Example Usage in your brickflow task:
        service_principle_pat = ctx.dbutils.secrets.get("scope", "service_principle_id")
        WorkflowDependencySensor(
            databricks_host=https://your_workspace_url.cloud.databricks.com,
            databricks_token=service_principle_pat,
            dependency_job_id=job_id,
            dependency_task_name="foo",
            poke_interval=20,
            timeout=60,
            delta=timedelta(days=1)
        )
        In the above snippet Databricks secrets are used as a secure service to store the databricks token.
        If you get your token from another secret management service, like AWS Secrets Manager, GCP Secret Manager
        or Azure Key Vault, just pass it in the databricks_token argument.
    """

    def __init__(
        self,
        dependency_job_name: str,
        dependency_task_name: str,
        delta: timedelta,
        timeout_seconds: int,
        databricks_host: str = None,
        databricks_token: Union[str, SecretStr] = None,
        poke_interval_seconds: int = 60,
    ):
        super().__init__(
            databricks_host=databricks_host,
            databricks_token=databricks_token,
            dependency_job_name=dependency_job_name,
            delta=delta,
            timeout_seconds=timeout_seconds,
            poke_interval_seconds=poke_interval_seconds,
        )

        self.dependency_task_name = dependency_task_name

    def execute(self):
        self.dependency_job_id = self._get_job_id

        while True:
            runs_list = self._workspace_obj.jobs.list_runs(
                job_id=self.dependency_job_id,
                limit=25,
                start_time_from=self.get_execution_start_time_unix_milliseconds(),
                expand_tasks=True,
            )

            for run in runs_list:
                for task in run.tasks:
                    if task.task_key == self.dependency_task_name:
                        task_state = task.state.result_state
                        if task_state:
                            self.log.info(
                                f"Found the run_id '{run.run_id}' and '{self.dependency_task_name}' "
                                f"task with state: {task_state.value}"
                            )
                            if task_state.value == "SUCCESS":
                                self.log.info(f"Found a successful run: {run.run_id}")
                                return
                        else:
                            self.log.info(
                                f"Found the run_id '{run.run_id}' and '{self.dependency_task_name}' "
                                f"but the task has not started yet..."
                            )

            self.log.info("Didn't find a successful task run yet...")

            if (
                self.timeout is not None
                and (time.time() - self.start_time) > self.timeout
            ):
                raise WorkflowDependencySensorTimeOutException(
                    f"The job has timed out..."
                )

            self.log.info(f"Sleeping for: {self.poke_interval}")
            time.sleep(self.poke_interval)
