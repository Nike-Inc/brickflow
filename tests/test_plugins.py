import copy
from typing import List
from unittest import mock
from unittest.mock import patch

import pluggy
import pytest

from brickflow.engine.task import get_plugin_manager, get_brickflow_tasks_hook


def assert_plugin_manager(pm: pluggy.PluginManager, expected_plugins: List[str]) -> None:
    num_expected_plugins = len(expected_plugins)
    assert len(pm.get_plugins()) == num_expected_plugins, f"import error should only {num_expected_plugins} plugins"
    for plugin in expected_plugins:
        assert pm.has_plugin(plugin), f"plugin manager should have {plugin} plugin"

    all_plugins = set([pm.get_name(plugin_impl) for plugin_impl in pm.get_plugins()])
    assert all_plugins == set(expected_plugins), (
        f"plugin manager should have {expected_plugins} " f"plugins and nothing more"
    )


class TestBrickflowPlugins:
    def test_plugins_installed(self):
        pm = copy.deepcopy(get_plugin_manager())
        get_brickflow_tasks_hook(pm)
        assert_plugin_manager(pm, ["airflow-plugin", "default"])

    def test_plugins_load_plugins_import_error(self):
        with mock.patch("brickflow_plugins.load_plugins") as load_plugins_mock:
            load_plugins_mock.side_effect = ImportError
            pm = copy.deepcopy(get_plugin_manager())
            get_brickflow_tasks_hook(pm)
            assert_plugin_manager(pm, ["default"])

    def test_plugins_ensure_installation_import_error(self):
        with mock.patch("brickflow_plugins.ensure_installation") as load_plugins_mock:
            load_plugins_mock.side_effect = ImportError
            pm = copy.deepcopy(get_plugin_manager())
            get_brickflow_tasks_hook(pm)
            assert_plugin_manager(pm, ["default"])

    def test_cron_import_nopy4j(self):
        remove_cron_helper = {
            "brickflow_plugins.airflow.cronhelper": None,
            "py4j": None,
            "py4j.protocol": None,
            "py4j.java_gateway": None,
        }
        with patch.dict("sys.modules", remove_cron_helper):
            with pytest.raises(ImportError):
                import brickflow_plugins.airflow.cronhelper as cronhelper  # noqa

    def test_cron_conversion(self):
        import brickflow_plugins.airflow.cronhelper as cronhelper  # noqa

        unix_cron = cronhelper.cron_helper.quartz_to_unix("0 0 12 * * ?")
        quartz_cron = cronhelper.cron_helper.unix_to_quartz(unix_cron)
        unix_cron_second = cronhelper.cron_helper.quartz_to_unix(quartz_cron)
        assert unix_cron == unix_cron_second, "cron conversion should be idempotent"
