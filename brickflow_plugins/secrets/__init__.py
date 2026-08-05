from __future__ import annotations

import abc
import base64
import functools
from typing import Optional, Tuple, Union, List
from urllib.parse import ParseResult, urlparse

import pluggy

from brickflow_plugins import log
from brickflow_plugins.operators.deprecated_airflow_operators import (
    BrickflowSecretsBackend,
)

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


def resolve_secret(secret_url: str) -> Optional[str]:
    """
    Resolve a secret from a URL like ``cerberus://.../path/key`` or
    ``base64://<b64-encoded-value>``. Returns ``None`` if no registered
    handler recognizes the scheme.
    """
    parsed_url = urlparse(secret_url)
    return get_brickflow_tasks_hook().get_secret_value(url_parsed_result=parsed_url)
