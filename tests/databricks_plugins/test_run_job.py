import re

import pytest
from requests_mock.mocker import Mocker as RequestsMocker

from brickflow.engine.utils import ctx
from brickflow_plugins.databricks.run_job import RunJobInRemoteWorkspace


class TestRunJob:
    workspace_url = "https://42.cloud.databricks.com"
    endpoint_url = f"{workspace_url}/api/.*/jobs/run-now"
    response = {"run_id": 37, "number_in_job": 42}

    ctx.log.propagate = True

    @pytest.fixture(autouse=True)
    def mock_get_job_id(self, mocker):
        mocker.patch(
            "brickflow_plugins.databricks.run_job.get_job_id",
            return_value=1,
        )

    @pytest.fixture(autouse=True, name="api")
    def mock_api(self):
        rm = RequestsMocker()
        rm.post(re.compile(self.endpoint_url), json=self.response, status_code=int(200))
        yield rm

    def test_run_job(self, api, caplog):
        with api:
            RunJobInRemoteWorkspace(
                databricks_host=self.workspace_url,
                databricks_token="token",
                job_name="foo",
            ).execute()

        assert "RunNowResponse(number_in_job=42, run_id=37)" in caplog.text
