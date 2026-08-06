"""
Airflow Task Dependency Sensor.

Native brickflow sensor that polls an external Airflow API to check the
status of a specific task in an Airflow DAG. Supports Airflow 1.x
(``/api/experimental``), 2.x (``/api/v1``), and 3.x (``/api/v2``) API
shapes. Requires only ``requests`` -- no ``apache-airflow`` package
needs to be installed on the Databricks cluster.
"""

from __future__ import annotations

import time
from datetime import datetime, timedelta
from typing import List, Optional

import requests

from brickflow_plugins import log
from brickflow_plugins.sensors import Sensor


def _api_variant(version: str) -> str:
    """Map an Airflow version string to the REST API dialect used by the sensor.

    Returns one of:

    - ``"experimental"`` for Airflow 1.x (``/api/experimental``)
    - ``"v2"`` for Airflow 3.x (``/api/v2``, FastAPI, ``logical_date``)
    - ``"v1"`` for Airflow 2.x and anything else (``/api/v1``, default)
    """
    if version.startswith("1."):
        return "experimental"
    if version.startswith("3."):
        return "v2"
    return "v1"


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
        Airflow major version string, e.g. ``"1.10"``, ``"2.0.2"``, or
        ``"3.0.0"``. Used to select between the ``/api/experimental``
        (Airflow 1.x), ``/api/v1`` (Airflow 2.x), and ``/api/v2``
        (Airflow 3.x) endpoint shapes.
    token : str
        Bearer token that will be sent in the ``Authorization`` header.
        For Airflow 3.x, this is typically a short-lived JWT obtained
        out-of-band (e.g. via Okta, MAP, or ``POST /auth/token``).
    """

    def __init__(self, url: str, version: str, token: str) -> None:
        self.url = str(url).rstrip("/")
        self.version = version
        self.token = token


class AirflowTaskDependencySensor(Sensor):
    """
    Sensor that polls an external Airflow cluster's API to wait until a
    given task in a given DAG reaches an allowed state.

    The API dialect used is selected from ``cluster.version``:

    - ``"1.x"`` -> ``/api/experimental``
    - ``"2.x"`` (default) -> ``/api/v1``
    - ``"3.x"`` -> ``/api/v2`` (FastAPI, ``logical_date`` filters)

    Example
    -------
    ::

        sensor = AirflowTaskDependencySensor(
            dag_id="my_upstream_dag",
            task_id="final_task",
            cluster=AirflowCluster(
                url="https://airflow.example.com",
                version="2.0.2",   # use "3.0.0" for Airflow 3.x (/api/v2)
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
        variant = _api_variant(self.cluster.version)
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
        if variant == "experimental":
            log.info("this is 1.x cluster")
            url = f"{self.cluster.url}/api/experimental/dags/{self.dag_id}/dag_runs/"
        elif variant == "v2":
            # Airflow 3.x FastAPI: /api/v2 replaces /api/v1, and the
            # execution_date_* filters were replaced by logical_date_*.
            url = (
                f"{self.cluster.url}/api/v2/dags/{self.dag_id}"
                f"/dagRuns?logical_date_gte={execution_window_tz}{max_end_date_filter}"
            )
        else:
            # Airflow 2.x API limits 100 records, so only picking runs
            # within the execution window provided.
            url = (
                f"{self.cluster.url}/api/v1/dags/{self.dag_id}"
                f"/dagRuns?execution_date_gte={execution_window_tz}{max_end_date_filter}"
            )

        log.info("URL to poke for dag runs %s", url)
        response = requests.get(url, headers=headers, verify=False, timeout=10)
        response.raise_for_status()

        list_of_dictionaries = response.json()["dag_runs"]
        # Airflow 3.x drops `execution_date` from DagRun payloads in favor of
        # `logical_date`; older APIs still expose `execution_date`.
        sort_key = "logical_date" if variant == "v2" else "execution_date"
        if variant == "v2":
            # In Airflow 3.x `logical_date` is nullable for asset-triggered runs.
            # This sensor is fundamentally a date-window check, so runs without
            # a logical_date are not eligible dependency targets -- drop them
            # before sorting so they can't be selected by `[-1]` / `[0]`.
            list_of_dictionaries = [
                r for r in list_of_dictionaries if r.get(sort_key) is not None
            ]
        list_of_dictionaries = sorted(
            list_of_dictionaries,
            key=lambda k: k[sort_key],
            reverse=True,
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

        if variant == "experimental":
            # For Airflow 1.x the execution date is needed to check the status.
            dag_run_id = list_of_dictionaries[0]["execution_date"]
        else:
            # For Airflow 2.x/3.x the dag_run_id is needed to check the status.
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

        if variant == "experimental":
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
            api_prefix = "/api/v2" if variant == "v2" else "/api/v1"
            task_url = (
                f"{self.cluster.url}{api_prefix}/dags/{self.dag_id}"
                f"/dagRuns/{dag_run_id}/taskInstances/{self.task_id}"
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
