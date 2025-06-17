from datetime import datetime, timezone
from collections import namedtuple


import pytest
from requests_mock.mocker import Mocker as RequestsMocker

from brickflow_plugins.databricks.sla_sensor import SLASensor


class TestSLASensor:
    workspace_url = "https://42.cloud.databricks.com"
    endpoint_url = f"{workspace_url}/api/2.2/jobs/runs/get"
    expected_sla_timestamp_utc_miss = datetime.now(timezone.utc).replace(
        hour=1, minute=0, second=0, microsecond=0
    )
    expected_sla_timestamp_utc_met = datetime.now(timezone.utc).replace(
        hour=1, minute=10, second=0, microsecond=0
    )

    settings = namedtuple("JobSettings", ["tags"])
    job = namedtuple("Job", ["settings"])
    JobSettings = job(
        settings(
            {"sla_met": "MyJob SLA - 10 1 @ @ 1-3", "sla_miss": "MyJob SLA - 0 1 @ @ @"}
        )
    )

    response = {
        "job_id": 1,
        "run_id": 1,
        "start_time": 1704063600000,
        "state": {"result_state": None, "life_cycle_state": "RUNNING"},
        "tasks": [
            {
                "run_id": 100,
                "task_key": "foo",
                "state": {"result_state": "SUCCESS", "life_cycle_state": "TERMINATED"},
            },
            {
                "run_id": 200,
                "task_key": "bar",
                "state": {"result_state": "FAILED", "life_cycle_state": "TERMINATED"},
            },
            {
                "run_id": 300,
                "task_key": "baz",
                "state": {"result_state": None, "life_cycle_state": "RUNNING"},
            },
        ],
    }

    @pytest.fixture(autouse=True)
    def mock_get_execution_start_time_unix_milliseconds(self, mocker):
        mocker.patch.object(
            SLASensor,
            "get_execution_start_time_unix_milliseconds",
            return_value=1704063600000,
        )

    @pytest.fixture(autouse=True)
    def mock_get_execution_start_timestamp(self, mocker):
        mocker.patch.object(
            SLASensor,
            "get_execution_start_timestamp",
            return_value=int(
                datetime.now(timezone.utc)
                .replace(hour=1, minute=0, second=1, microsecond=0)
                .timestamp()
            ),
        )

    @pytest.fixture(autouse=True)
    def mock_get_current_timestamp(self, mocker, request):
        return_value = (
            datetime.now(timezone.utc).replace(
                hour=1, minute=10, second=1, microsecond=0
            )
            if request.node.name == "test_sensor_sla_miss"
            else datetime.now(timezone.utc).replace(
                hour=1, minute=0, second=1, microsecond=0
            )
        )
        mocker.patch.object(
            SLASensor, "get_current_timestamp", return_value=return_value
        )

    @pytest.fixture(autouse=True)
    def mock_get_target_run_id(self, mocker):
        mocker.patch.object(SLASensor, "get_target_run_id", return_value=1)

    @pytest.fixture(autouse=True)
    def mock_get_job_configuration(self, mocker):
        mocker.patch.object(
            SLASensor, "get_job_configuration", return_value=self.JobSettings
        )

    @pytest.fixture(autouse=True, name="api")
    def mock_api(self):
        rm = RequestsMocker()
        rm.get(self.endpoint_url, json=self.response, status_code=int(200))
        yield rm

    def test_sensor_sla_miss(self, api):
        with api:
            sensor = SLASensor(
                expected_sla_timestamp_utc=self.expected_sla_timestamp_utc_miss,
                monitored_task_name="foo",
                env="dev",
                data_product="product",
                run_date=str(self.expected_sla_timestamp_utc_miss.date()),
                dependency_job_name="job",
                sla_sensor_task_names=["sla_sensor"],
                databricks_host=self.workspace_url,
                databricks_token="token",
                poke_interval_seconds=1,
            )

            sla_result = sensor.monitor()

            assert sla_result == "SLA Missed"

    def test_sensor_sla_met(self, api):
        with api:
            sensor = SLASensor(
                expected_sla_timestamp_utc=self.expected_sla_timestamp_utc_met,
                monitored_task_name="bar",
                env="dev",
                data_product="product",
                run_date=str(self.expected_sla_timestamp_utc_met.date()),
                dependency_job_name="job",
                sla_sensor_task_names=["sla_sensor"],
                databricks_host=self.workspace_url,
                databricks_token="token",
                poke_interval_seconds=1,
            )

            sla_result = sensor.monitor()

            assert sla_result == "SLA Met"

    def test_sensor_tagged_sla_miss(self, api):
        with api:
            sensor = SLASensor(
                sla_tag_key="sla_miss",
                monitored_task_name="foo",
                env="dev",
                data_product="product",
                run_date=str(self.expected_sla_timestamp_utc_miss.date()),
                dependency_job_name="job",
                sla_sensor_task_names=["sla_sensor"],
                databricks_host=self.workspace_url,
                databricks_token="token",
                poke_interval_seconds=1,
            )

            sla_result = sensor.monitor()

            assert sla_result == "SLA Missed"

    def test_sensor_tagged_sla_met(self, api):
        with api:
            sensor = SLASensor(
                sla_tag_key="sla_met",
                monitored_task_name="bar",
                env="dev",
                data_product="product",
                run_date=str(self.expected_sla_timestamp_utc_met.date()),
                dependency_job_name="job",
                sla_sensor_task_names=["sla_sensor"],
                databricks_host=self.workspace_url,
                databricks_token="token",
                poke_interval_seconds=1,
            )

            sla_result = sensor.monitor()

            assert sla_result == "SLA Met"
