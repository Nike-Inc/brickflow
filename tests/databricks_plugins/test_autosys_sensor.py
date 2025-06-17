import re

import pytest
from databricks.sdk import WorkspaceClient
from requests.exceptions import HTTPError
from requests_mock.mocker import Mocker as RequestsMocker
from yarl import URL

from brickflow_plugins.databricks.autosys_sensor import AutosysSensor

AUTOSYS_BASE_URL = URL("https://42.autosys.my-org.com")
DATABRICKS_BASE_URL = URL("https://42.cloud.databricks.com")


class TestAutosysSensor:
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
        rm = RequestsMocker()
        # JOB-FOO-1: Success
        rm.register_uri(
            method="GET",
            url=f"{AUTOSYS_BASE_URL}/foo-1",
            response_list=[
                {
                    "json": {"status": "SU", "lastEndUTC": "2024-01-01T00:55:00Z"},
                    "status_code": int(200),
                },
            ],
        )

        # JOB-FOO-2: Raise Error
        rm.register_uri(
            method="GET",
            url=f"{AUTOSYS_BASE_URL}/foo-2",
            response_list=[
                {
                    "json": {},
                    "status_code": int(404),
                },
            ],
        )

        # JOB-FOO-3: Poke 4 times until success
        rm.register_uri(
            method="GET",
            url=f"{AUTOSYS_BASE_URL}/foo-3",
            response_list=[
                {
                    "json": {"status": "FA", "lastEndUTC": "2024-01-01T00:55:00Z"},
                    "status_code": int(200),
                },
                {
                    "json": {"status": "UNK", "lastEndUTC": None},
                    "status_code": int(200),
                },
                {
                    "json": {"status": "UNK", "lastEndUTC": ""},
                    "status_code": int(200),
                },
                {
                    "json": {"status": "SU", "lastEndUTC": "2024-01-01T01:55:00Z"},
                    "status_code": int(200),
                },
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
                            "quartz_cron_expression": "0 0 1 * * ?",
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
        sensor = AutosysSensor(
            url=AUTOSYS_BASE_URL,
            job_name="foo-x",
            poke_interval=1,
            time_delta={"hours": 1},
        )
        sensor._workspace_obj = WorkspaceClient(
            host=str(DATABRICKS_BASE_URL), token="foo"
        )
        yield sensor

    def test_success(self, api, caplog, sensor):
        sensor.job_name = "foo-1"
        with api:
            sensor.poke()
        assert caplog.text.count("Poking again") == 0
        assert "Success criteria met. Exiting" in caplog.text

    def test_non_200(self, api, sensor):
        sensor.job_name = "foo-2"
        with pytest.raises(HTTPError):
            with api:
                sensor.poke()

    def test_poking(self, api, caplog, sensor):
        sensor.job_name = "foo-3"
        with api:
            sensor.poke()
        assert caplog.text.count("Poking again") == 3
        assert "Success criteria met. Exiting" in caplog.text
