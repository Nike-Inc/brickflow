import json
import logging
import os
from http import HTTPStatus

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from airflow.models import Connection
from airflow.sensors.base import BaseSensorOperator
from brickflow_plugins import log


class MapDagSchedule:
    def get_schedule(self, wf_id: str, **args):
        """
        Function that the sensors defined while deriving this class should
        override.
        """
        raise Exception("Override me.")

    def get_task_run_status(
        self, wf_id: str, task_id: str, run_date=None, cluster_id=None, **args
    ):
        """
        Function that the sensors defined while deriving this class should
        override.
        """
        raise Exception("Override me.")


# TODO: implement Delta Json


class MapDagScheduleHelper(MapDagSchedule):
    def __init__(self, okta_conn_id: str):
        self._okta_conn: Connection = Connection.get_connection_from_secrets(
            okta_conn_id
        )

    def get_okta_url(self) -> str:
        conn_type = self._okta_conn.conn_type
        host = self._okta_conn.host
        schema = self._okta_conn.schema
        return f"{conn_type}://{host}/{schema}"

    def get_okta_client_id(self) -> str:
        return self._okta_conn.login

    def get_okta_client_secret(self) -> str:
        return self._okta_conn.get_password()

    def get_access_token(self) -> str:
        okta_url = self.get_okta_url()
        client_id = self.get_okta_client_id()
        client_secret = self.get_okta_client_secret()

        okta_url = os.getenv("OKTA_URL", okta_url)
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

    def get_airflow_api_url(self, cluster_id: str) -> str:
        # TODO: templatize this to a env variable
        base_api_url = f"https://proxy.us-east-1.map.nike.com/{cluster_id}"
        return base_api_url

    def get_version(self, cluster_id: str) -> str:
        session = requests.Session()
        retries = Retry(
            total=10, backoff_factor=1, status_forcelist=[502, 503, 504, 500]
        )
        session.mount("https://", HTTPAdapter(max_retries=retries))
        version_check_url = (
            self.get_airflow_api_url(cluster_id) + "/admin/rest_api/api?api=version"
        )
        logging.info(version_check_url)
        otoken = self.get_access_token()
        headers = {"Authorization": "Bearer " + otoken, "Accept": "application/json"}
        out_version = "UKN"
        response = session.get(version_check_url, headers=headers, verify=False)
        if response.status_code == HTTPStatus.OK:
            out_version = response.json()["output"]
        log.info(response.text.encode("utf8"))
        session.close()
        return out_version

    def get_task_run_status(
        self, wf_id: str, task_id: str, run_date=None, cluster_id=None, **args
    ):
        token_data = self.get_access_token()
        api_url = self.get_airflow_api_url(cluster_id)
        version_nr = self.get_version(cluster_id)
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

    def get_schedule(self, wf_id: str, **kwargs):
        """
        get work flow schedule cron syntax
        """
        raise Exception("Do not have implementation")


class TaskDependencySensor(BaseSensorOperator):
    def __init__(
        self,
        external_dag_id,
        external_task_id,
        okta_conn_id,
        allowed_states=None,
        execution_delta=None,
        execution_delta_json=None,
        cluster_id=None,
        *args,
        **kwargs,
    ):
        super(TaskDependencySensor, self).__init__(*args, **kwargs)
        self.okta_conn_id = okta_conn_id
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
        self.cluster_id = cluster_id

        self._poke_count = 0
        self.dbx_wf_id = kwargs.get("dbx_wf_id")

    def poke(self, context):
        log.info(f"executing poke.. {self._poke_count}")
        self._poke_count = self._poke_count + 1
        logging.info("Poking.. {0} round".format(str(self._poke_count)))

        exec_time = context["execution_date"]

        task_status = MapDagScheduleHelper(self.okta_conn_id).get_task_run_status(
            wf_id=self.external_dag_id,
            task_id=self.external_task_id,
            run_date=exec_time,
            cluster_id=self.cluster_id,
        )
        log.info(f"task_status= {task_status}")

        if task_status not in self.allowed_states:
            count = 0
        else:
            count = 1

        return count
