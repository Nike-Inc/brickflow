import unittest
from unittest.mock import MagicMock, patch
from datetime import datetime
from brickflow_plugins.airflow.operators.external_tasks import AutosysSensor


class TestAutosysSensor(unittest.TestCase):
    @patch("brickflow_plugins.airflow.operators.external_tasks.requests.get")
    def test_autosys_sensor(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "SU",
            "lastEndUTC": "2023-08-27T19:17:17Z",
        }

        mock_requests_get.return_value = mock_response

        mock_context = MagicMock()
        mock_context.__getitem__.return_value = datetime(2023, 8, 28)
        autosys_sensor = AutosysSensor(
            task_id="autosys-sensor",
            url="https://dummyjson.com/products/",
            headers={},
            poke_interval=10,
            job_name="1",
            time_delta={"days": 1},
        )

        response = autosys_sensor.poke(context=mock_context)
        self.assertTrue(response)
