from __future__ import annotations

import abc
import base64
import functools
import os
from typing import Optional, Tuple, Union, List
from urllib.parse import urlparse, ParseResult

import pluggy

try:
    from airflow.secrets import BaseSecretsBackend
except ImportError:
    raise ImportError(
        "You must install airflow to use airflow plugins, "
        "please try pip install brickflow[apache-airflow]"
    )

from brickflow_plugins import log

BRICKFLOW_SECRETS_BACKEND = "brickflow_secrets_backend"

brickflow_secrets_plugin_spec = pluggy.HookspecMarker(BRICKFLOW_SECRETS_BACKEND)


class BrickflowSecretPluginSpec:
    @staticmethod
    @brickflow_secrets_plugin_spec(firstresult=True)
    def get_secret_value(url_parsed_result: ParseResult) -> Optional["str"]:
        """Custom execute method that is able to be plugged in."""


@functools.lru_cache
def get_brickflow_tasks_hook() -> BrickflowSecretPluginSpec:
    pm = pluggy.PluginManager(BRICKFLOW_SECRETS_BACKEND)
    pm.add_hookspecs(BrickflowSecretPluginSpec)
    pm.load_setuptools_entrypoints(BRICKFLOW_SECRETS_BACKEND)
    pm.register(CerberusBrickflowSecretPluginImpl())
    pm.register(Base64BrickflowSecretPluginImpl())
    for name, plugin_instance in pm.list_name_plugin():
        log.info(
            "Loaded plugin with name: %s and class: %s",
            name,
            plugin_instance.__class__.__name__,
        )
    return pm.hook


brickflow_secrets_backend_plugin_impl = pluggy.HookimplMarker(BRICKFLOW_SECRETS_BACKEND)


class AbstractSecretsHelper(abc.ABC):
    PROTOCOL_STARTS_WITH: Optional[Union[str, List[str]]] = None

    def get_secret_value_from_url(self, url_parsed_result: ParseResult):
        allowed_protocols = (
            [self.PROTOCOL_STARTS_WITH]
            if isinstance(self.PROTOCOL_STARTS_WITH, str)
            else self.PROTOCOL_STARTS_WITH
        )
        if self.PROTOCOL_STARTS_WITH is not None and not any(
            [
                url_parsed_result.scheme.lower().startswith(protocol)
                for protocol in allowed_protocols
            ]
        ):
            return None
        return self._get_secret_value_from_url(url_parsed_result)

    @staticmethod
    @abc.abstractmethod
    def _get_secret_value_from_url(url_parsed_result: ParseResult) -> str:
        pass


class B64SecretsHelper(AbstractSecretsHelper):
    PROTOCOL_STARTS_WITH = ["base64", "b64"]

    @staticmethod
    def _get_secret_value_from_url(url_parsed_result: ParseResult) -> str:
        b64data = url_parsed_result.netloc.encode("utf-8")
        return base64.b64decode(b64data).decode("utf-8")


class CerberusSecretsHelper(AbstractSecretsHelper):
    PROTOCOL_STARTS_WITH = "cerberus"

    @staticmethod
    def parse_path_and_key(path: Optional[str]) -> Optional[Tuple[str, str]]:
        if path is not None:
            _cleaned_path = path.lstrip("/").rstrip("/")
            return "/".join(_cleaned_path.split("/")[:-1]), _cleaned_path.split("/")[-1]
        return None

    @staticmethod
    def _get_secret_value_from_url(url_parsed_result: ParseResult) -> str:
        try:
            from cerberus.client import CerberusClient
        except ImportError:
            raise ImportError(
                "You must install cerberus-client to use the cerberus secrets backend, "
                "please try pip install brickflow[cerberus]"
            )
        parts = url_parsed_result.scheme.lower().split("+")
        protocol = "https"
        if len(parts) == 2:
            protocol = parts[1]
        _client = CerberusClient(f"{protocol}://{url_parsed_result.netloc}")
        _path, _key = CerberusSecretsHelper.parse_path_and_key(url_parsed_result.path)
        data = _client.get_secrets_data(_path)
        return data[_key]


class CerberusBrickflowSecretPluginImpl(BrickflowSecretPluginSpec):
    @staticmethod
    @brickflow_secrets_backend_plugin_impl
    def get_secret_value(url_parsed_result: ParseResult) -> Optional["str"]:
        return CerberusSecretsHelper().get_secret_value_from_url(url_parsed_result)


class Base64BrickflowSecretPluginImpl(BrickflowSecretPluginSpec):
    @staticmethod
    @brickflow_secrets_backend_plugin_impl
    def get_secret_value(url_parsed_result: ParseResult) -> Optional["str"]:
        return B64SecretsHelper().get_secret_value_from_url(url_parsed_result)


class DatabricksSecretsBrickflowSecretPluginImpl(BrickflowSecretPluginSpec):
    @staticmethod
    @brickflow_secrets_backend_plugin_impl
    def get_secret_value(url_parsed_result: ParseResult) -> Optional["str"]:
        # not implemented yet
        return None


class BrickflowSecretsBackend(BaseSecretsBackend):  # noqa
    def __enter__(self):
        self.set_backend_env()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.unset_backend_env()

    def get_conn_value(self, conn_id: str) -> str | None:
        parsed_url = urlparse(conn_id)
        return get_brickflow_tasks_hook().get_secret_value(url_parsed_result=parsed_url)

    def _get_secrets_backend_env(self):
        return {
            "AIRFLOW__SECRETS__BACKEND": f"{self.__class__.__module__}.{self.__class__.__name__}",
            "AIRFLOW__SECRETS__BACKEND_KWARGS": "",
        }

    def set_backend_env(self):
        for k, v in self._get_secrets_backend_env().items():
            os.environ[k] = v

    def unset_backend_env(self):
        for k in self._get_secrets_backend_env().keys():
            os.environ.pop(k, None)
