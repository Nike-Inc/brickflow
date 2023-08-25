import abc
import json
import logging
from http import HTTPStatus
from typing import Callable

import requests
from airflow.models import Connection
from airflow.sensors.base import BaseSensorOperator
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from brickflow_plugins import log


class DagSchedule:
    def get_schedule(self, wf_id: str, **args):
        """
        Function that the sensors defined while deriving this class should
        override.
        """
        raise Exception("Override me.")

    def get_task_run_status(self, wf_id: str, task_id: str, run_date=None, **args):
        """
        Function that the sensors defined while deriving this class should
        override.
        """
        raise Exception("Override me.")


# TODO: implement Delta Json


class AirflowClusterAuth(abc.ABC):
    @abc.abstractmethod
    def get_access_token(self) -> str:
        pass

    @abc.abstractmethod
    def get_airflow_api_url(self) -> str:
        pass

    @abc.abstractmethod
    def get_version(self) -> str:
        pass


class AirflowProxyOktaClusterAuth(AirflowClusterAuth):
    def __init__(
        self,
        oauth2_conn_id: str,
        airflow_cluster_url: str,
        airflow_version: str = None,
        get_airflow_version_callback: Callable[[str, str], str] = None,
    ):
        self._airflow_version = airflow_version
        self._get_airflow_version_callback = get_airflow_version_callback
        self._oauth2_conn_id = oauth2_conn_id
        self._airflow_url = airflow_cluster_url.rstrip("/")
        if airflow_version is None and get_airflow_version_callback is None:
            raise Exception(
                "Either airflow_version or get_airflow_version_callback must be provided"
            )

    def get_okta_conn(self):
        return Connection.get_connection_from_secrets(self._oauth2_conn_id)

    def get_okta_url(self) -> str:
        conn_type = self.get_okta_conn().conn_type
        host = self.get_okta_conn().host
        schema = self.get_okta_conn().schema
        return f"{conn_type}://{host}/{schema}"

    def get_okta_client_id(self) -> str:
        return self.get_okta_conn().login

    def get_okta_client_secret(self) -> str:
        return self.get_okta_conn().get_password()

    def get_access_token(self) -> str:
        okta_url = self.get_okta_url()
        client_id = self.get_okta_client_id()
        client_secret = self.get_okta_client_secret()

        payload = (
            "client_id="
            + client_id
            + "&client_secret="
            + client_secret
            + "&grant_type=client_credentials"
        )
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "cache-control": "no-cache",
        }
        response = requests.post(okta_url, data=payload, headers=headers, timeout=600)
        if (
            response.status_code < HTTPStatus.OK
            or response.status_code > HTTPStatus.PARTIAL_CONTENT
        ):
            log.error(
                "Failed request to Okta for JWT status_code={} response={} client_id={}".format(
                    response.status_code, response.text, client_id
                )
            )
        token_data = response.json()["access_token"]
        return token_data

    def get_airflow_api_url(self) -> str:
        # TODO: templatize this to a env variable
        return self._airflow_url

    def get_version(self) -> str:
        if self._airflow_version is not None:
            return self._airflow_version
        else:
            return self._get_airflow_version_callback(
                self._airflow_url, self.get_access_token()
            )


class AirflowScheduleHelper(DagSchedule):
    def __init__(self, airflow_auth: AirflowClusterAuth):
        self._airflow_auth = airflow_auth

    def get_task_run_status(self, wf_id: str, task_id: str, run_date=None, **kwargs):
        token_data = self._airflow_auth.get_access_token()
        api_url = self._airflow_auth.get_airflow_api_url()
        version_nr = self._airflow_auth.get_version()
        dag_id = wf_id
        headers = {
            "Content-Type": "application/json",
            "cache-control": "no-cache",
            "Authorization": "Bearer " + token_data,
        }
        o_task_status = "UKN"
        session = requests.Session()
        retries = Retry(
            total=5, backoff_factor=1, status_forcelist=[502, 503, 504, 500]
        )
        session.mount("https://", HTTPAdapter(max_retries=retries))
        if version_nr.startswith("1."):
            log.info("this is 1.x cluster")
            url = (
                api_url
                + "/api/experimental"
                + "/dags/"
                + dag_id
                + "/dag_runs/"
                + run_date
                + "/tasks/"
                + task_id
            )
        else:
            url = (
                api_url
                + "/api/v1/dags/"
                + dag_id
                + "/dagRuns/scheduled__"
                + run_date
                + "/taskInstances/"
                + task_id
            )

        log.info(f"url= {url.replace(' ', '')}")
        response = session.get(url.replace(" ", ""), headers=headers)

        log.info(
            f"response.status_code= {response.status_code} response.text= {response.text}"
        )
        if response.status_code == 200:
            log.info(f"response= {response.text}")
            json_obj = json.loads(response.text)
            if type(json_obj) == dict:
                o_task_status = json_obj["state"]

            return o_task_status

        return o_task_status


class TaskDependencySensor(BaseSensorOperator):
    def __init__(
        self,
        external_dag_id,
        external_task_id,
        airflow_cluster_auth: AirflowClusterAuth,
        allowed_states=None,
        execution_delta=None,
        execution_delta_json=None,
        *args,
        **kwargs,
    ):
        super(TaskDependencySensor, self).__init__(*args, **kwargs)
        self.airflow_auth = airflow_cluster_auth
        self.allowed_states = allowed_states or ["success"]

        if execution_delta_json and execution_delta:
            raise Exception(
                "Only one of `execution_date` or `execution_delta_json` maybe provided to Sensor; not more than one."
            )

        self.external_dag_id = external_dag_id
        self.external_task_id = external_task_id
        self.allowed_states = allowed_states
        self.execution_delta = execution_delta
        self.execution_delta_json = execution_delta_json

        self._poke_count = 0

    def poke(self, context):
        log.info(f"executing poke.. {self._poke_count}")
        self._poke_count = self._poke_count + 1
        logging.info("Poking.. {0} round".format(str(self._poke_count)))

        exec_time = context["execution_date"]

        task_status = AirflowScheduleHelper(self.airflow_auth).get_task_run_status(
            wf_id=self.external_dag_id,
            task_id=self.external_task_id,
            run_date=exec_time,
        )
        log.info(f"task_status= {task_status}")

        if task_status not in self.allowed_states:
            count = 0
        else:
            count = 1

        return count
