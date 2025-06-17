import re
from datetime import datetime, timedelta

import pytest
from databricks.sdk import WorkspaceClient
from requests.exceptions import HTTPError
from requests_mock.mocker import Mocker as RequestsMocker
from yarl import URL

from brickflow_plugins.databricks.airflow_task_dependency_sensor import (
    AirflowCluster,
    AirflowTaskDependencySensor,
    log,
)

AIRFLOW_BASE_URL = URL("https://42.airflow.my-org.com/foo")
DATABRICKS_BASE_URL = URL("https://42.cloud.databricks.com")


class TestAirflowTaskDependencySensor:
    log.propagate = True

    @pytest.fixture(autouse=True)
    def mock_brickflow_scaffolding(self, mocker):
        mocker.patch(
            "brickflow_plugins.databricks.ctx.dbutils_widget_get_or_else",
            return_value=1,
        )
        mocker.patch(
            "brickflow_plugins.databricks.ctx.start_time",
            return_value="1704078102000",
        )

    @pytest.fixture(autouse=True, name="api", scope="class")
    def mock_api(self):
        """
        End-to-end test scenario for Airflow v2 API
        """
        rm = RequestsMocker()
        # TEST-DAG-1: Success after 4 pokes
        rm.register_uri(
            method="GET",
            url=f"{AIRFLOW_BASE_URL}/api/v1/dags/test-dag-1/dagRuns?execution_date_gte=2024-01-01T00:00:00Z",
            response_list=[
                # Test 1: No Run
                {"json": {"dag_runs": [], "total_entries": 0}, "status_code": int(200)},
                # Test 2: Run Exists
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
                    "status_code": int(200),
                },
            ],
        )
        # TEST-DAG-1: Task Instance Endpoint
        rm.register_uri(
            method="GET",
            url=(
                f"{AIRFLOW_BASE_URL}"
                f"/api/v1/dags/test-dag-1/dagRuns/manual__2024-01-01T01:00:00.000000+00:00/taskInstances/test-task"
            ),
            response_list=[
                {"json": {"state": "running"}, "status_code": int(200)},
                {"json": {"state": "failed"}, "status_code": int(200)},
                {"json": {"state": "success"}, "status_code": int(200)},
            ],
        )

        # TEST-DAG-2: Non-existent DAG
        rm.register_uri(
            method="GET",
            url=f"{AIRFLOW_BASE_URL}/api/v1/dags/test-dag-2/dagRuns?execution_date_gte=2024-01-01T00:00:00Z",
            response_list=[{"status_code": int(404)}],
        )

        # TEST-DAG-3: Timeout
        rm.register_uri(
            method="GET",
            url=f"{AIRFLOW_BASE_URL}/api/v1/dags/test-dag-3/dagRuns?execution_date_gte=2024-01-01T00:00:00Z",
            status_code=200,
            json={"dag_runs": [], "total_entries": 0},
        )

        # TEST-DAG-4: End date specified
        rm.register_uri(
            method="GET",
            url=(
                f"{AIRFLOW_BASE_URL}/api/v1/dags/test-dag-4"
                f"/dagRuns?execution_date_gte=2024-01-01T00:00:00Z&end_date_lte=2024-01-01T01:20:00Z"
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
                    "status_code": int(200),
                },
            ],
        )
        # TEST-DAG-4: Task Instance Endpoint
        rm.register_uri(
            method="GET",
            url=(
                f"{AIRFLOW_BASE_URL}"
                f"/api/v1/dags/test-dag-4/dagRuns/manual__2024-01-01T01:00:00.000000+00:00/taskInstances/test-task"
            ),
            response_list=[
                {"json": {"state": "success"}, "status_code": int(200)},
            ],
        )

        # Databricks API Mock
        rm.register_uri(
            method="GET",
            url=re.compile(rf"{DATABRICKS_BASE_URL}/api/.*/jobs/runs/get\?run_id=1"),
            response_list=[
                {
                    "json": {
                        "schedule": {
                            "quartz_cron_expression": "0 0 3 * * ?",
                            "timezone_id": "UTC",
                        }
                    },
                    "status_code": int(200),
                }
            ],
        )
        yield rm

    @pytest.fixture()
    def sensor(self):
        cluster = AirflowCluster(
            url=AIRFLOW_BASE_URL,
            version="2.0.2",
            token="foo",
        )
        sensor = AirflowTaskDependencySensor(
            dag_id="test-dag-x",
            task_id="test-task",
            cluster=cluster,
            allowed_states=["success"],
            execution_delta=timedelta(**{"hours": -3}),
            poke_interval=1,
        )
        sensor._workspace_obj = WorkspaceClient(
            host=str(DATABRICKS_BASE_URL), token="foo"
        )
        yield sensor

    def test_api_airflow_v2(self, api, caplog, sensor):
        # Scenario
        # Airflow API poked 4 times
        # 1. No Run
        # 2. Run Exists - Task is in Running State
        # 3. Run Exists - Task is in Failed State
        # 4. Run Exists - Task is in Success State
        sensor.dag_id = "test-dag-1"

        with api:
            sensor.execute()

        assert (
            "No runs found for test-dag-1 dag in time window: 2024-01-01T00:00:00Z - now, please check upstream dag"
            in caplog.text
        )
        assert "task_status=running" in caplog.text
        assert "task_status=failed" in caplog.text
        assert "task_status=success" in caplog.text
        assert "Poking... 4 round" in caplog.text

    def test_non_200(self, sensor, api):
        sensor.dag_id = "test-dag-2"
        with pytest.raises(HTTPError):
            with api:
                sensor.execute()

    def test_timeout(self, sensor, api):
        sensor.timeout = 1
        sensor.dag_id = "test-dag-3"

        with pytest.raises(TimeoutError):
            with api:
                sensor.execute()

    def test_end_date(self, api, sensor):
        sensor.dag_id = "test-dag-4"

        execution_date = datetime.strptime("2024-01-01T03:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
        max_end_date = datetime.strptime("2024-01-01T01:20:00Z", "%Y-%m-%dT%H:%M:%SZ")
        with api:
            task_status = sensor.get_execution_stats(
                execution_date=execution_date, max_end_date=max_end_date
            )
        assert task_status == "success"
