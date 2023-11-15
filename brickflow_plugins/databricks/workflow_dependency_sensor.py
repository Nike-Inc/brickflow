import functools
import logging
import os
from datetime import datetime, timedelta
from typing import Union

import requests
import time
from pydantic import SecretStr
from requests.adapters import HTTPAdapter

from brickflow.context import ctx


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
        dependency_job_id: int,
        delta: timedelta,
        timeout_seconds: int,
        poke_interval_seconds: int = 60,
    ):
        self.databricks_host = databricks_host
        self.dependency_job_id = dependency_job_id
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

    def get_execution_start_time_unix_miliseconds(self) -> int:
        session = self.get_http_session()
        url = f"{self.databricks_host.rstrip('/')}/api/2.1/jobs/runs/get"
        headers = {
            "Authorization": f"Bearer {self.databricks_token.get_secret_value()}",
            "Content-Type": "application/json",
        }
        run_id = ctx.dbutils_widget_get_or_else("brickflow_parent_run_id", None)
        if run_id is None:
            raise WorkflowDependencySensorException(
                "run_id is empty, brickflow_parent_run_id parameter is not found "
                "or no value present"
            )
        params = {"run_id": run_id}
        resp = session.get(url, params=params, headers=headers).json()

        # Convert Unix timestamp in miliseconds to datetime object to easily incorporate the delta
        start_time = datetime.fromtimestamp(resp["start_time"] / 1000)
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

    def execute(self):
        session = self.get_http_session()
        url = f"{self.databricks_host.rstrip('/')}/api/2.1/jobs/runs/list"
        headers = {
            "Authorization": f"Bearer {self.databricks_token.get_secret_value()}",
            "Content-Type": "application/json",
        }
        params = {
            "limit": 25,
            "job_id": self.dependency_job_id,
            "start_time_from": self.get_execution_start_time_unix_miliseconds(),
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
