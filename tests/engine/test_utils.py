import pytest
from requests_mock.mocker import Mocker as RequestsMocker

from pydantic import SecretStr

from brickflow.engine.utils import get_job_id, ctx


class TestUtils:
    workspace_url = "https://42.cloud.databricks.com"
    endpoint_url = f"{workspace_url}/api/2.1/jobs/list"

    ctx.log.propagate = True

    @pytest.fixture(autouse=True, name="api", scope="class")
    def mock_api(self):
        rm = RequestsMocker()
        rm.register_uri(
            method="GET",
            url=self.endpoint_url,
            response_list=[
                {
                    "json": {"jobs": [{"job_id": 1234, "settings": {"name": "foo"}}]},
                    "status_code": int(200),
                },
                {
                    "json": {"has_more": False},
                    "status_code": int(200),
                },
                {
                    "json": {},
                    "status_code": int(404),
                },
            ],
        )
        yield rm

    def test_get_job_id_success(self, api):
        with api:
            job_id = get_job_id(
                job_name="foo",
                host=self.workspace_url,
                token=SecretStr("token"),
            )
        assert job_id == 1234

    def test_get_job_id_failure(self, api):
        with pytest.raises(ValueError):
            with api:
                get_job_id(job_name="bar", host=self.workspace_url, token="token")

    def test_get_job_id_non_200(self, caplog, api):
        with api:
            get_job_id(job_name="buz", host=self.workspace_url, token="token")
        assert "An error occurred: request failed" in caplog.text
