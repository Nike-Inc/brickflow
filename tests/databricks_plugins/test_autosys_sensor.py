from datetime import datetime, timezone

import pytest
from requests.exceptions import HTTPError
from requests_mock.mocker import Mocker as RequestsMocker

from brickflow_plugins.sensors.autosys_sensor import AutosysSensor


class TestAutosysSensor:
    @pytest.fixture(autouse=True, name="api", scope="class")
    def mock_api(self):
        rm = RequestsMocker()
        rm.register_uri(
            method="GET",
            url="https://42.autosys.my-org.com/foo",
            response_list=[
                # Test 1: Success on first poke
                {
                    "json": {"status": "SU", "lastEndUTC": "2024-01-01T00:55:00Z"},
                    "status_code": int(200),
                },
                # Test 2: Non-200 response
                {"json": {}, "status_code": int(404)},
                # Test 3: Poke 4 times until success
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
        yield rm

    def _make_sensor(self, mocker, execution_ts_iso: str):
        """
        Build an AutosysSensor with the Databricks WorkspaceClient patched out
        and ``_execution_timestamp`` pinned to a specific instant. This
        isolates the sensor's own logic from Databricks SDK plumbing.
        """
        mocker.patch("brickflow_plugins.sensors.WorkspaceClient", autospec=True)
        sensor = AutosysSensor(
            url="https://42.autosys.my-org.com/",
            job_name="foo",
            poke_interval=1,
            time_delta={"hours": 1},
        )
        # Pin the "current run" timestamp.
        pinned = datetime.strptime(execution_ts_iso, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc
        )
        sensor.__dict__["_execution_timestamp"] = pinned
        return sensor

    def test_success(self, api, caplog, mocker):
        sensor = self._make_sensor(mocker, "2024-01-01T01:00:00Z")
        with api:
            sensor.poke()
        assert caplog.text.count("Poking again") == 0
        assert "Success criteria met. Exiting" in caplog.text

    def test_non_200(self, api, mocker):
        sensor = self._make_sensor(mocker, "2024-01-01T01:00:00Z")
        with pytest.raises(HTTPError):
            with api:
                sensor.poke()

    def test_poking(self, api, caplog, mocker):
        sensor = self._make_sensor(mocker, "2024-01-01T02:00:00Z")
        with api:
            sensor.poke()
        assert caplog.text.count("Poking again") == 3
        assert "Success criteria met. Exiting" in caplog.text
