import re
from datetime import timedelta

import pytest
from requests_mock.mocker import Mocker as RequestsMocker

from brickflow_plugins.databricks.workflow_dependency_sensor import (
    WorkflowDependencySensorTimeOutException,
    WorkflowTaskDependencySensor,
)


class TestWorkflowTaskDependencySensor:
    workspace_url = "https://42.cloud.databricks.com"
    endpoint_url = f"{workspace_url}/api/.*/jobs/runs/list"
    response = {
        "runs": [
            {
                "job_id": 1,
                "run_id": 1,
                "start_time": 1704063600000,
                "state": {
                    "result_state": "SUCCESS",
                },
                "tasks": [
                    {
                        "run_id": 100,
                        "task_key": "foo",
                        "state": {
                            "result_state": "SUCCESS",
                        },
                    },
                    {
                        "run_id": 200,
                        "task_key": "bar",
                        "state": {
                            "result_state": "FAILED",
                        },
                    },
                    {
                        "run_id": 300,
                        "task_key": "baz",
                        "state": {},
                    },
                ],
            }
        ]
    }

    @pytest.fixture(autouse=True)
    def mock_get_execution_start_time_unix_milliseconds(self, mocker):
        mocker.patch.object(
            WorkflowTaskDependencySensor,
            "get_execution_start_time_unix_milliseconds",
            return_value=1704063600000,
        )

    @pytest.fixture(autouse=True)
    def mock_get_job_id(self, mocker):
        mocker.patch(
            "brickflow_plugins.databricks.workflow_dependency_sensor.get_job_id",
            return_value=1,
        )

    @pytest.fixture(autouse=True, name="api")
    def mock_api(self):
        rm = RequestsMocker()
        rm.get(re.compile(self.endpoint_url), json=self.response, status_code=int(200))
        yield rm

    def test_sensor_success(self, caplog, api):
        with api:
            sensor = WorkflowTaskDependencySensor(
                databricks_host=self.workspace_url,
                databricks_token="token",
                dependency_job_name="job",
                dependency_task_name="foo",
                delta=timedelta(seconds=1),
                timeout_seconds=1,
                poke_interval_seconds=1,
            )

            sensor.execute()

            assert (
                "Found the run_id '1' and 'foo' task with state: SUCCESS" in caplog.text
            )
            assert "Found a successful run: 1" in caplog.text

    def test_sensor_failure(self, caplog, api):
        with api:
            sensor = WorkflowTaskDependencySensor(
                databricks_host=self.workspace_url,
                databricks_token="token",
                dependency_job_name="job",
                dependency_task_name="bar",
                delta=timedelta(seconds=1),
                timeout_seconds=1,
                poke_interval_seconds=1,
            )

            with pytest.raises(WorkflowDependencySensorTimeOutException):
                sensor.execute()

            assert (
                "Found the run_id '1' and 'bar' task with state: FAILED"
                in caplog.messages
            )
            assert "Didn't find a successful task run yet..." in caplog.messages

    def test_sensor_no_state(self, caplog, api):
        with api:
            sensor = WorkflowTaskDependencySensor(
                databricks_host=self.workspace_url,
                databricks_token="token",
                dependency_job_name="job",
                dependency_task_name="baz",
                delta=timedelta(seconds=1),
                timeout_seconds=1,
                poke_interval_seconds=1,
            )

            with pytest.raises(WorkflowDependencySensorTimeOutException):
                sensor.execute()

            assert (
                "Found the run_id '1' and 'baz' but the task has not started yet..."
                in caplog.messages
            )
            assert "Didn't find a successful task run yet..." in caplog.messages
