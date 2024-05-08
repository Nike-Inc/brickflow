import pytest
from requests.exceptions import HTTPError
from requests_mock.mocker import Mocker as RequestsMocker

from brickflow_plugins.airflow.operators.external_tasks import AutosysSensor


class TestAutosysSensor:
    @pytest.fixture(autouse=True, name="api", scope="class")
    def mock_api(self):
        rm = RequestsMocker()
        rm.register_uri(
            method="GET",
            url="https://42.autosys.my-org.com/foo",
            response_list=[
                # Test 1: Success
                {
                    "json": {"status": "SU", "lastEndUTC": "2024-01-01T00:55:00Z"},
                    "status_code": int(200),
                },
                # Test 2: Raise Error
                {
                    "json": {},
                    "status_code": int(404),
                },
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

    @pytest.fixture()
    def sensor(self):
        yield AutosysSensor(
            task_id="test",
            url="https://42.autosys.my-org.com/",
            job_name="foo",
            poke_interval=1,
            time_delta={"hours": 1},
        )

    def test_success(self, api, caplog, sensor):
        with api:
            sensor.poke(context={"execution_date": "2024-01-01T01:00:00Z"})
        assert caplog.text.count("Poking again") == 0
        assert "Success criteria met. Exiting" in caplog.text

    def test_non_200(self, api, sensor):
        with pytest.raises(HTTPError):
            with api:
                sensor.poke(context={"execution_date": "2024-01-01T01:00:00Z"})

    def test_poking(self, api, caplog, sensor):
        with api:
            sensor.poke(context={"execution_date": "2024-01-01T02:00:00Z"})
        assert caplog.text.count("Poking again") == 3
        assert "Success criteria met. Exiting" in caplog.text
