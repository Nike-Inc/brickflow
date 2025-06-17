from datetime import timedelta

import pytest
from requests_mock.mocker import Mocker as RequestsMocker

from brickflow_plugins.databricks.workflow_dependency_sensor import (
    WorkflowDependencySensor,
)


class TestWorkflowDependencySensor:
    workspace_url = "https://42.cloud.databricks.com"
    endpoint_url = f"{workspace_url}/api/2.2/jobs/get"
    response = {}

    def test_sensor_failure_403(self):
        api = RequestsMocker()
        api.get(self.endpoint_url, json=self.response, status_code=int(403))

        # Databricks SDK will throw PermissionDenied exception if the job_id is not found or
        # user doesn't have permission
        from databricks.sdk.errors.platform import PermissionDenied

        with api:
            sensor = WorkflowDependencySensor(
                databricks_host=self.workspace_url,
                databricks_token="token",
                dependency_job_id="1",
                delta=timedelta(seconds=1),
                timeout_seconds=1,
                poke_interval_seconds=1,
            )

            with pytest.raises(PermissionDenied):
                sensor.execute()
