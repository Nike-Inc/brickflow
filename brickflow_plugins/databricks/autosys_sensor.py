"""
Aytosys Sensor

This sensor checks the status of a specific Autosys job by sending an HTTP GET request to the Autosys API.
"""

import time
from datetime import timedelta
from typing import Union

import pytz
import requests
from dateutil.parser import parse  # type: ignore[import-untyped]
from requests import HTTPError
from yarl import URL

from brickflow_plugins import log
from brickflow_plugins.databricks import Sensor


class AutosysSensor(Sensor):
    def __init__(
        self,
        url: URL,
        job_name: str,
        poke_interval: int,
        time_delta: Union[timedelta, dict] = timedelta(days=0),
    ):
        """
        Takes in url, job_name, poke_interval, execution delta and as parameters
        and sends a http get() request, checks the API response and exits the process
        if the specified conditions are met.
        If not, waits for the given poke interval, then pokes again and again until the conditions
        are met or times out.
        """
        super().__init__()
        self.url = url
        self.job_name = job_name
        self.poke_interval = poke_interval
        self.time_delta = time_delta

    def poke(self):
        url = f"{self.url}/{self.job_name}"
        log.info("Poking: %s", url)

        headers = {
            "Accept": "application/json",
            "cache-control": "no-cache",
        }

        response = requests.get(
            url,
            headers=headers,
            verify=False,  # nosec
            timeout=10,
        )

        if response.status_code != 200:
            raise HTTPError(f"Request failed with '{response.status_code}' code. \n{response.text}")  # type: ignore
        else:
            status = response.json()["status"][:2].upper()

            last_end_timestamp = None
            if last_end_utc := response.json().get("lastEndUTC"):
                last_end_timestamp = parse(last_end_utc).replace(tzinfo=pytz.UTC)

            time_delta = (
                self.time_delta
                if isinstance(self.time_delta, timedelta)
                else timedelta(**self.time_delta)
            )

            run_timestamp = self._execution_timestamp - time_delta

            if (
                "SU" in status
                and last_end_timestamp
                and last_end_timestamp >= run_timestamp
            ):
                log.info(
                    "Last End: %s, Run Timestamp: %s", last_end_timestamp, run_timestamp
                )
                log.info("Success criteria met. Exiting")
                return True
            else:
                log.info(
                    "Last End: %s, Run Timestamp: %s", last_end_timestamp, run_timestamp
                )
                time.sleep(self.poke_interval)
                log.info("Poking again")
                AutosysSensor.poke(self)
