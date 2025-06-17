"""
Airflow Task Dependency Sensor

This sensor checks the status of a specific task in an Airflow DAG, allowing for dependencies
to be managed within Databricks workflows. It supports both Airflow 1.x and 2.x APIs,
and can handle execution timestamps based on Quartz cron expressions.
"""

import time
from datetime import datetime, timedelta

import requests
from yarl import URL

from brickflow_plugins import log
from brickflow_plugins.sensors import Sensor


class AirflowCluster:
    """
    Class to hold Airflow cluster information for authentication and API access.
    """

    def __init__(
        self,
        url: URL,
        version: str,
        token: str,
    ):
        self.url = url
        self.version = version
        self.token = token


class AirflowTaskDependencySensor(Sensor):
    def __init__(
        self,
        dag_id: str,
        task_id: str,
        cluster: AirflowCluster,
        allowed_states: list = None,
        execution_delta: timedelta = timedelta(days=0),
        latest=False,
        timeout_seconds: int = 3600,  # 1 hour
        poke_interval=60,
    ):
        super().__init__()
        self.dag_id = dag_id
        self.task_id = task_id
        self.cluster = cluster
        self.allowed_states = allowed_states if allowed_states else ["success"]
        self.execution_delta = execution_delta
        self.latest = latest
        self.poke_interval = poke_interval
        self.timeout = timeout_seconds

        self._poke_count = 0
        self._start_time = time.time()

    def get_execution_stats(
        self, execution_date: datetime, max_end_date: datetime = None
    ) -> str:
        """Function to get the execution stats for task_id within a execution start time and
        (optionally) allowed job end time.

        Returns:
            string: state of the desired task id and dag_run_id (success/failure/running)
        """
        execution_window_tz = (execution_date + self.execution_delta).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )
        max_end_date_filter = (
            f"&end_date_lte={max_end_date.strftime('%Y-%m-%dT%H:%M:%SZ')}"
            if max_end_date
            else ""
        )
        headers = {
            "Content-Type": "application/json",
            "cache-control": "no-cache",
            "Authorization": f"Bearer {self.cluster.token}",
        }
        if self.cluster.version.startswith("1."):
            log.info("this is 1.x cluster")
            url = f"{self.cluster.url}/api/experimental/dags/{self.dag_id}/dag_runs/"
        else:
            # Airflow API for 2.X version limits 100 records, so only picking runs within the execution window provided
            url = f"{self.cluster.url}/api/v1/dags/{self.dag_id}/dagRuns?execution_date_gte={execution_window_tz}{max_end_date_filter}"

        log.info("URL to poke for dag runs %s", url)
        response = requests.request(
            "GET", url, headers=headers, verify=False, timeout=10
        )
        response.raise_for_status()

        list_of_dictionaries = response.json()["dag_runs"]
        list_of_dictionaries = sorted(
            list_of_dictionaries, key=lambda k: k["execution_date"], reverse=True
        )

        if len(list_of_dictionaries) == 0:
            log.info(
                "No runs found for %s dag in time window: %s - %s, please check upstream dag",
                self.dag_id,
                execution_window_tz,
                max_end_date.strftime("%Y-%m-%dT%H:%M:%SZ") if max_end_date else "now",
            )
            return "none"

        if self.cluster.version.startswith("1."):
            # For airflow 1.X Execution date is needed to check the status of the task
            dag_run_id = list_of_dictionaries[0]["execution_date"]
        else:
            # For airflow 2.X or higher dag_run_id is needed to check the status of the task
            dag_run_id = (
                list_of_dictionaries[-1]["dag_run_id"]
                if not self.latest
                else list_of_dictionaries[0]["dag_run_id"]
            )

        log.info("Latest run for the dag is with execution date of %s", dag_run_id)
        log.info(
            "Poking %s dag for %s run_id status as latest flag is set to %s",
            self.dag_id,
            dag_run_id,
            self.latest,
        )

        if self.cluster.version.startswith("1."):
            if dag_run_id >= execution_window_tz:
                task_url = f"{url}/{dag_run_id}/tasks/{self.task_id}"
            else:
                log.info(
                    "No airflow runs found for %s dag after %s",
                    self.dag_id,
                    execution_window_tz,
                )
                return "none"
        else:
            task_url = (
                url[: url.rfind("/")]
                + f"/dagRuns/{dag_run_id}/taskInstances/{self.task_id}"
            )
        log.info("Pinging airflow API %s for task status ", task_url)
        task_response = requests.request(
            "GET", task_url, headers=headers, verify=False, timeout=10
        )
        task_response.raise_for_status()
        task_state = task_response.json()["state"]
        return task_state

    def poke(self) -> str:
        """Function to poke the Airflow API for the task status"""
        log.info("executing poke... %s", self._poke_count)
        self._poke_count = self._poke_count + 1
        log.info("Poking... %s round", self._poke_count)

        task_status = self.get_execution_stats(execution_date=self._execution_timestamp)
        log.info("task_status=%s", task_status)
        return task_status

    def execute(self):
        """Function inherited from the BaseSensor Operator to execute the Poke Function

        Raises:
            Exception: If Upstream Dag is Failed
        """
        # Execution date is extracted from context and will be based on the task schedule, e.g.
        # 0 0 1 ? * MON-SAT * -> 2024-01-01T01:00:00.000000+00:00
        # This means that the relative delta between workflow execution and target Airflow DAG always stays the same.
        log.info("Execution date derived from context: %s", self._execution_timestamp)

        execution_window_tz = self._execution_timestamp + self.execution_delta
        log.info(
            "Executing the sensor to check for %s for %s DAG and task %s after %s.",
            self.allowed_states,
            self.dag_id,
            self.task_id,
            execution_window_tz,
        )
        status = ""
        while status not in self.allowed_states:
            status = self.poke()
            if status == "failed":
                # Log the fact that upstream failed, however do not fail the task and continue poking until timeout
                log.error(
                    "Upstream dag '%s' failed at '%s' task, continue poking till timeout is reached...",
                    self.dag_id,
                    self.task_id,
                )
                time.sleep(self.poke_interval)
            elif status != "success":
                time.sleep(self.poke_interval)

            if (time.time() - self._start_time) > self.timeout:
                raise TimeoutError("The job has timed out!")
        log.info("Upstream DAG '%s' is successful", self.dag_id)
