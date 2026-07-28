from datetime import datetime, timedelta, timezone

import pytest
from requests.exceptions import HTTPError
from requests_mock.mocker import Mocker as RequestsMocker

from brickflow_plugins.sensors.airflow_task_dependency_sensor import (
    AirflowCluster,
    AirflowTaskDependencySensor,
    log,
)

AIRFLOW_BASE_URL = "https://42.airflow.my-org.com/foo"


class TestAirflowTaskDependencySensor:
    log.propagate = True

    @pytest.fixture(autouse=True, name="api", scope="class")
    def mock_api(self):
        """
        End-to-end fixture mocking the Airflow v2 API for four test DAGs.
        """
        rm = RequestsMocker()

        # test-dag-1: eventually succeeds after 4 pokes.
        rm.register_uri(
            method="GET",
            url=(
                f"{AIRFLOW_BASE_URL}/api/v1/dags/test-dag-1/dagRuns"
                f"?execution_date_gte=2024-01-01T00:00:00Z"
            ),
            response_list=[
                {"json": {"dag_runs": [], "total_entries": 0}, "status_code": 200},
                {
                    "json": {
                        "dag_runs": [
                            {
                                "conf": {},
                                "dag_id": "test-dag-1",
                                "dag_run_id": "manual__2024-01-01T01:00:00.000000+00:00",
                                "end_date": "2024-01-01T01:10:00.000000+00:00",
                                "execution_date": "2024-01-01T01:00:00.000000+00:00",
                                "external_trigger": True,
                                "logical_date": "2024-01-01T01:00:00.000000+00:00",
                                "start_date": "2024-01-01T01:00:00.000000+00:00",
                                "state": "success",
                            },
                        ],
                        "total_entries": 1,
                    },
                    "status_code": 200,
                },
            ],
        )
        rm.register_uri(
            method="GET",
            url=(
                f"{AIRFLOW_BASE_URL}/api/v1/dags/test-dag-1/dagRuns/"
                "manual__2024-01-01T01:00:00.000000+00:00/taskInstances/test-task"
            ),
            response_list=[
                {"json": {"state": "running"}, "status_code": 200},
                {"json": {"state": "failed"}, "status_code": 200},
                {"json": {"state": "success"}, "status_code": 200},
            ],
        )

        # test-dag-2: non-existent DAG.
        rm.register_uri(
            method="GET",
            url=(
                f"{AIRFLOW_BASE_URL}/api/v1/dags/test-dag-2/dagRuns"
                f"?execution_date_gte=2024-01-01T00:00:00Z"
            ),
            status_code=404,
        )

        # test-dag-3: always empty (timeout scenario).
        rm.register_uri(
            method="GET",
            url=(
                f"{AIRFLOW_BASE_URL}/api/v1/dags/test-dag-3/dagRuns"
                f"?execution_date_gte=2024-01-01T00:00:00Z"
            ),
            status_code=200,
            json={"dag_runs": [], "total_entries": 0},
        )

        # test-dag-4: end-date window.
        rm.register_uri(
            method="GET",
            url=(
                f"{AIRFLOW_BASE_URL}/api/v1/dags/test-dag-4/dagRuns"
                f"?execution_date_gte=2024-01-01T00:00:00Z"
                f"&end_date_lte=2024-01-01T01:20:00Z"
            ),
            response_list=[
                {
                    "json": {
                        "dag_runs": [
                            {
                                "conf": {},
                                "dag_id": "test-dag-4",
                                "dag_run_id": "manual__2024-01-01T01:00:00.000000+00:00",
                                "end_date": "2024-01-01T01:10:00.000000+00:00",
                                "execution_date": "2024-01-01T01:00:00.000000+00:00",
                                "external_trigger": True,
                                "logical_date": "2024-01-01T01:00:00.000000+00:00",
                                "start_date": "2024-01-01T01:00:00.000000+00:00",
                                "state": "success",
                            },
                        ],
                        "total_entries": 1,
                    },
                    "status_code": 200,
                },
            ],
        )
        rm.register_uri(
            method="GET",
            url=(
                f"{AIRFLOW_BASE_URL}/api/v1/dags/test-dag-4/dagRuns/"
                "manual__2024-01-01T01:00:00.000000+00:00/taskInstances/test-task"
            ),
            response_list=[{"json": {"state": "success"}, "status_code": 200}],
        )
        yield rm

    def _make_sensor(self, mocker, dag_id: str) -> AirflowTaskDependencySensor:
        """
        Build an ``AirflowTaskDependencySensor`` with a pinned
        ``_execution_timestamp`` so tests don't hit the real Databricks
        WorkspaceClient.
        """
        mocker.patch("brickflow_plugins.sensors.WorkspaceClient", autospec=True)
        sensor = AirflowTaskDependencySensor(
            dag_id=dag_id,
            task_id="test-task",
            cluster=AirflowCluster(url=AIRFLOW_BASE_URL, version="2.0.2", token="foo"),
            allowed_states=["success"],
            execution_delta=timedelta(hours=-3),
            poke_interval=1,
        )
        pinned = datetime(2024, 1, 1, 3, 0, 0, tzinfo=timezone.utc)
        sensor.__dict__["_execution_timestamp"] = pinned
        return sensor

    def test_api_airflow_v2(self, api, caplog, mocker):
        # Poke sequence:
        # 1. No run
        # 2. Run exists, task Running
        # 3. Run exists, task Failed
        # 4. Run exists, task Success
        sensor = self._make_sensor(mocker, "test-dag-1")
        with api:
            sensor.execute()

        assert "No runs found for test-dag-1 dag in time window" in caplog.text
        assert "task_status=running" in caplog.text
        assert "task_status=failed" in caplog.text
        assert "task_status=success" in caplog.text
        assert "Poking... 4 round" in caplog.text

    def test_non_200(self, api, mocker):
        sensor = self._make_sensor(mocker, "test-dag-2")
        with pytest.raises(HTTPError):
            with api:
                sensor.execute()

    def test_timeout(self, api, mocker):
        sensor = self._make_sensor(mocker, "test-dag-3")
        sensor.timeout = 1
        with pytest.raises(TimeoutError):
            with api:
                sensor.execute()

    def test_end_date(self, api, mocker):
        sensor = self._make_sensor(mocker, "test-dag-4")
        execution_date = datetime.strptime("2024-01-01T03:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
        max_end_date = datetime.strptime("2024-01-01T01:20:00Z", "%Y-%m-%dT%H:%M:%SZ")
        with api:
            task_status = sensor.get_execution_stats(
                execution_date=execution_date, max_end_date=max_end_date
            )
        assert task_status == "success"
