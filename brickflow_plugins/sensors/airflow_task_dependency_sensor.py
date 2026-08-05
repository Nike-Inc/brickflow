"""
Airflow Task Dependency Sensor.

Native brickflow sensor that polls an external Airflow API to check the
status of a specific task in an Airflow DAG. Supports both Airflow 1.x
and 2.x API shapes. Requires only ``requests`` -- no ``apache-airflow``
package needs to be installed on the Databricks cluster.
"""

from __future__ import annotations

import time
from datetime import datetime, timedelta
from typing import List, Optional

import requests

from brickflow_plugins import log
from brickflow_plugins.sensors import Sensor


class AirflowClusterAuthError(Exception):
    """Raised when Airflow cluster authentication fails."""


class AirflowCluster:
    """
    Represents an Airflow cluster the sensor polls.

    Parameters
    ----------
    url : str
        Base URL of the Airflow API (e.g. ``https://airflow.example.com``).
    version : str
        Airflow major version string, e.g. ``"1.10"`` or ``"2.0.2"``. Used
        to select between the ``/api/experimental`` and ``/api/v1``
        endpoint shapes.
    token : str
        Bearer token that will be sent in the ``Authorization`` header.
    """

    def __init__(self, url: str, version: str, token: str) -> None:
        self.url = str(url).rstrip("/")
        self.version = version
        self.token = token


class AirflowTaskDependencySensor(Sensor):
    """
    Sensor that polls an external Airflow cluster's API to wait until a
    given task in a given DAG reaches an allowed state.

    Example
    -------
    ::

        sensor = AirflowTaskDependencySensor(
            dag_id="my_upstream_dag",
            task_id="final_task",
            cluster=AirflowCluster(
                url="https://airflow.example.com",
                version="2.0.2",
                token=my_token,
            ),
            execution_delta=timedelta(hours=0),
            timeout_seconds=3600,
            poke_interval=60,
        )
        sensor.execute()
    """

    def __init__(
        self,
        dag_id: str,
        task_id: str,
        cluster: AirflowCluster,
        allowed_states: Optional[List[str]] = None,
        execution_delta: timedelta = timedelta(days=0),
        latest: bool = False,
        timeout_seconds: int = 3600,
        poke_interval: int = 60,
    ) -> None:
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
        self,
        execution_date: datetime,
        max_end_date: Optional[datetime] = None,
    ) -> str:
        """
        Return the state of ``self.task_id`` for the most recent
        ``self.dag_id`` DAG run in the given window.

        Returns "none" when no matching DAG run is found.
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
            # Airflow API for 2.X version limits 100 records, so only picking runs
            # within the execution window provided.
            url = (
                f"{self.cluster.url}/api/v1/dags/{self.dag_id}"
                f"/dagRuns?execution_date_gte={execution_window_tz}{max_end_date_filter}"
            )

        log.info("URL to poke for dag runs %s", url)
        response = requests.get(url, headers=headers, verify=False, timeout=10)
        response.raise_for_status()

        list_of_dictionaries = response.json()["dag_runs"]
        list_of_dictionaries = sorted(
            list_of_dictionaries, key=lambda k: k["execution_date"], reverse=True
        )

        if len(list_of_dictionaries) == 0:
            log.info(
                "No runs found for %s dag in time window: %s - %s, please check "
                "upstream dag",
                self.dag_id,
                execution_window_tz,
                max_end_date.strftime("%Y-%m-%dT%H:%M:%SZ") if max_end_date else "now",
            )
            return "none"

        if self.cluster.version.startswith("1."):
            # For airflow 1.X the execution date is needed to check the status.
            dag_run_id = list_of_dictionaries[0]["execution_date"]
        else:
            # For airflow 2.X or higher the dag_run_id is needed to check the status.
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
        task_response = requests.get(
            task_url, headers=headers, verify=False, timeout=10
        )
        task_response.raise_for_status()
        return task_response.json()["state"]

    def poke(self) -> str:  # type: ignore[override]
        """Poke the Airflow API once and return the task state."""
        log.info("executing poke... %s", self._poke_count)
        self._poke_count += 1
        log.info("Poking... %s round", self._poke_count)

        task_status = self.get_execution_stats(execution_date=self._execution_timestamp)
        log.info("task_status=%s", task_status)
        return task_status

    def execute(self) -> None:
        """
        Poll the Airflow API until the task reaches an allowed state or the
        timeout is exceeded.

        Raises
        ------
        TimeoutError
            If ``self.timeout`` seconds elapse before the task reaches an
            allowed state.
        """
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
                # Log the fact that upstream failed, however do not fail the task
                # and continue poking until timeout.
                log.error(
                    "Upstream dag '%s' failed at '%s' task, continue poking till "
                    "timeout is reached...",
                    self.dag_id,
                    self.task_id,
                )
                time.sleep(self.poke_interval)
            elif status != "success":
                time.sleep(self.poke_interval)

            if (time.time() - self._start_time) > self.timeout:
                raise TimeoutError("The job has timed out!")
        log.info("Upstream DAG '%s' is successful", self.dag_id)
