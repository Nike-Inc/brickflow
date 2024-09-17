from datetime import timedelta, datetime

import pytest
from requests.exceptions import HTTPError
from requests_mock.mocker import Mocker as RequestsMocker

from brickflow_plugins.airflow.operators.external_tasks import (
    TaskDependencySensor,
    AirflowProxyOktaClusterAuth,
    log,
    AirflowSensorTimeout,
)

BASE_URL = "https://42.airflow.my-org.com/foo"


class TestTaskDependencySensor:
    log.propagate = True

    @pytest.fixture(autouse=True, name="api", scope="class")
    def mock_api(self):
        """
        End-to-end test scenario for Airflow v2 API
        """
        rm = RequestsMocker()
        # DAG Run Endpoint
        rm.register_uri(
            method="GET",
            url=f"{BASE_URL}/api/v1/dags/test-dag/dagRuns?execution_date_gte=2024-01-01T00:00:00Z",
            response_list=[
                # Test 1: No Run
                {"json": {"dag_runs": [], "total_entries": 0}, "status_code": int(200)},
                # Test 2: Run Exists
                {
                    "json": {
                        "dag_runs": [
                            {
                                "conf": {},
                                "dag_id": "test-dag",
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
                    "status_code": int(200),
                },
                # Test 2: No Run
            ],
        )
        # Task Instance Endpoint
        rm.register_uri(
            method="GET",
            url=(
                f"{BASE_URL}"
                f"/api/v1/dags/test-dag/dagRuns/manual__2024-01-01T01:00:00.000000+00:00/taskInstances/test-task"
            ),
            response_list=[
                {"json": {"state": "running"}, "status_code": int(200)},
                {"json": {"state": "failed"}, "status_code": int(200)},
                {"json": {"state": "success"}, "status_code": int(200)},
            ],
        )
        # DAG Run Endpoint with max end date
        rm.register_uri(
            method="GET",
            url=f"{BASE_URL}/api/v1/dags/test-dag/dagRuns?execution_date_gte=2024-01-01T00:00:00Z&end_date_lte=2024-01-01T01:20:00Z",
            response_list=[
                # Test 3: max end date specified
                {
                    "json": {
                        "dag_runs": [
                            {
                                "conf": {},
                                "dag_id": "test-dag",
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
                    "status_code": int(200),
                },
            ],
        )
        yield rm

    @pytest.fixture()
    def sensor(self, mocker):
        auth_mock = mocker.MagicMock(spec=AirflowProxyOktaClusterAuth)
        auth_mock.get_access_token.return_value = "foo"
        auth_mock.get_airflow_api_url.return_value = BASE_URL
        auth_mock.get_version.return_value = "2.0.2"

        yield TaskDependencySensor(
            external_dag_id="test-dag",
            external_task_id="test-task",
            allowed_states=["success"],
            execution_delta=timedelta(**{"hours": -3}),
            airflow_auth=auth_mock,
            task_id="foo",
            poke_interval=1,
        )

    def test_api_airflow_v2(self, api, caplog, sensor):
        # Scenario
        # Airflow API poked 4 times
        # 1. No Run
        # 2. Run Exists - Task is in Running State
        # 3. Run Exists - Task is in Failed State
        # 4. Run Exists - Task is in Success State
        with api:
            sensor.execute(context={"execution_date": "2024-01-01T03:00:00Z"})

        assert (
            "No Runs found for test-dag dag in time window: 2024-01-01T00:00:00Z - now, please check upstream dag"
            in caplog.text
        )
        assert "task_status=running" in caplog.text
        assert "task_status=failed" in caplog.text
        assert "task_status=success" in caplog.text
        assert "Poking.. 4 round" in caplog.text

    def test_non_200(self, sensor):
        rm = RequestsMocker()
        rm.get(
            f"{BASE_URL}/api/v1/dags/test-dag/dagRuns?execution_date_gte=2024-01-01T00:00:00Z",
            status_code=404,
        )

        with pytest.raises(HTTPError):
            with rm:
                sensor.execute(context={"execution_date": "2024-01-01T03:00:00Z"})

    def test_timeout(self, sensor):
        sensor.timeout = 1

        rm = RequestsMocker()
        rm.get(
            url=f"{BASE_URL}/api/v1/dags/test-dag/dagRuns?execution_date_gte=2024-01-01T00:00:00Z",
            status_code=200,
            json={"dag_runs": [], "total_entries": 0},
        )

        with pytest.raises(AirflowSensorTimeout):
            with rm:
                sensor.execute(context={"execution_date": "2024-01-01T03:00:00Z"})

    def test_end_date(self, api, caplog, sensor):
        execution_date = datetime.strptime("2024-01-01T03:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
        max_end_date = datetime.strptime("2024-01-01T01:20:00Z", "%Y-%m-%dT%H:%M:%SZ")
        with api:
            task_status = sensor.get_execution_stats(
                execution_date=execution_date, max_end_date=max_end_date
            )
        assert task_status == "success"
