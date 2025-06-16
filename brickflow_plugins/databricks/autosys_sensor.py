"""
AutosysSensor
"""

import time
import logging
from typing import Union
from datetime import timedelta

import pytz
import requests
from requests import HTTPError
from dateutil.parser import parse  # type: ignore[import-untyped]


class AutosysSensor:
    def __init__(
        self,
        url: str,
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
        self.url = url
        self.job_name = job_name
        self.poke_interval = poke_interval
        self.time_delta = time_delta
        self.url = self.url + self.job_name

    def poke(self, context):
        logging.info("Poking: %s", self.url)

        headers = {
            "Accept": "application/json",
            "cache-control": "no-cache",
        }

        response = requests.get(
            self.url,
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

            execution_timestamp = parse(context["execution_date"])
            run_timestamp = execution_timestamp - time_delta

            if (
                "SU" in status
                and last_end_timestamp
                and last_end_timestamp >= run_timestamp
            ):
                logging.info(
                    "Last End: %s, Run Timestamp: %s", last_end_timestamp, run_timestamp
                )
                logging.info("Success criteria met. Exiting")
                return True
            else:
                logging.info(
                    "Last End: %s, Run Timestamp: %s", last_end_timestamp, run_timestamp
                )
                time.sleep(self.poke_interval)
                logging.info("Poking again")
                AutosysSensor.poke(self, context)
