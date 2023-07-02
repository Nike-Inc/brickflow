import requests
from datetime import datetime, timedelta
import time
import os
import logging
from requests.adapters import HTTPAdapter
import functools
from brickflow.context import ctx


class WorkflowDependencySensorException(Exception):
    pass


class WorkflowDependencySensorTimeOutException(TimeoutError):
    pass


class WorkflowDependencySensor:
    """
    This is used to have dependencies on the databricks workflow

    Example Usage in your brickflow task:
        WorkflowDependencySensor(
            databricks_host=https://your_workspace_url.cloud.databricks.com,
            databricks_secrets_scope="brickflow-demo-tobedeleted",
            databricks_secrets_key="service_principle_id"
            dependency_job_id=job_id,
            poke_interval=20,
            timeout=60,
            delta=timedelta(days=1)
        )
    """

    def __init__(
        self,
        databricks_host: str,
        databricks_secrets_scope: str,
        databricks_secrets_key: str,
        dependency_job_id: int,
        delta: timedelta,
        timeout_seconds: int,
        poke_interval_seconds: int = 60,
    ):
        self.databricks_host = databricks_host
        self.dependency_job_id = dependency_job_id
        self.databricks_secrets_scope = databricks_secrets_scope
        self.databricks_secrets_key = databricks_secrets_key
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

    def get_the_execution_date(self) -> str:
        session = self.get_http_session()
        url = f"{self.databricks_host.rstrip('/')}/api/2.0/jobs/runs/get"
        headers = {
            "Authorization": f"Bearer {self.get_token()}",
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

        # Convert Unix timestamp to datetime object
        start_time = datetime.fromtimestamp(resp["start_time"] / 1000)
        execution_date = start_time - self.delta
        self.log.info(start_time)
        self.log.info(execution_date)
        self.log.info(execution_date.strftime("%s"))
        return execution_date.strftime("%s")

    @functools.lru_cache
    def get_token(self):
        return ctx.dbutils.secrets.get(
            self.databricks_secrets_scope, self.databricks_secrets_key
        )

    def execute(self):
        session = self.get_http_session()
        url = f"{self.databricks_host.rstrip('/')}/api/2.0/jobs/runs/list"
        headers = {
            "Authorization": f"Bearer {self.get_token()}",
            "Content-Type": "application/json",
        }
        # http://www.unixtimestampconverter.com/
        params = {
            "limit": 25,
            "job_id": self.dependency_job_id,
            "expand_tasks": "true",
            "start_time_from": self.get_the_execution_date(),
        }

        while True:
            offset = 0
            has_more = True
            while has_more is True:
                params["offset"] = offset
                resp = session.get(url, params=params, headers=headers).json()
                for run in resp.get("runs", []):
                    self.log.info(
                        f"Found the run_id: {run['run_id']}, and it's result_state is: {run.get('state', {}).get('result_state', None)}"
                    )
                    if run.get("state", {}).get("result_state", None) == "SUCCESS":
                        self.log.info(f"Found a successful run: {run['run_id']}")
                        return

                offset += params["limit"]
                has_more = resp.get("has_more", False)
                self.log.info(f"This is offset: {offset}, this is has_more: {has_more}")

            self.log.info("Didn't find a successful run yet")
            if (
                self.timeout is not None
                and (time.time() - self.start_time) > self.timeout
            ):
                raise WorkflowDependencySensorTimeOutException(f"The job has timed out")

            self.log.info(f"sleeping for: {self.poke_interval}")
            time.sleep(self.poke_interval)
