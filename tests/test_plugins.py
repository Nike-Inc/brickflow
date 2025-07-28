import copy
from pathlib import Path
from typing import List
from unittest import mock

import pluggy
import pytest
import toml

from brickflow.engine.task import get_brickflow_tasks_hook, get_plugin_manager


def assert_plugin_manager(
    pm: pluggy.PluginManager, expected_plugins: List[str]
) -> None:
    num_expected_plugins = len(expected_plugins)
    assert (
        len(pm.get_plugins()) == num_expected_plugins
    ), f"import error should only {num_expected_plugins} plugins"
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

    @pytest.mark.parametrize(
        "quartz_cron, expected_unix_cron",
        [
            ("0 * * ? * * *", "* * * * *"),
            ("0 */5 * ? * * *", "*/5 * * * *"),
            ("0 30 * ? * * *", "30 * * * *"),
            ("0 0 12 ? * * *", "0 12 * * *"),
            ("0 0 12 ? * 2 *", "0 12 * * 1"),
            ("0 0 0 10 * ? *", "0 0 10 * *"),
            ("0 0 0 1 1 ? *", "0 0 1 1 *"),
            ("0 0/5 14,18 * * ?", "0/5 14,18 * * *"),
            ("0 0 12 ? * 1,2,5-7 *", "0 12 * * 0,1,4-6"),
            ("0 0 12 ? * SUN,MON,THU-SAT *", "0 12 * * SUN,MON,THU-SAT"),
        ],
    )
    def test_cron_conversion(self, quartz_cron, expected_unix_cron):
        import brickflow_plugins.airflow.cronhelper as cronhelper  # noqa

        converted_unix_cron = cronhelper.cron_helper.quartz_to_unix(quartz_cron)
        converted_quartz_cron = cronhelper.cron_helper.unix_to_quartz(
            converted_unix_cron
        )
        converted_unix_cron_second = cronhelper.cron_helper.quartz_to_unix(
            converted_quartz_cron
        )

        assert (
            converted_unix_cron == converted_unix_cron_second
        ), "cron conversion should be idempotent"
        assert converted_unix_cron == expected_unix_cron

    @pytest.mark.parametrize(
        "quartz_cron",
        [
            "0 0 12 ? * L *",
            "0 0 12 ? * 1L *",
            "0 0 12 ? * 1W *",
            "0 0 12 ? * 1#5 *",
        ],
    )
    def test_unsupported_cron_expressions(self, quartz_cron):
        import brickflow_plugins.airflow.cronhelper as cronhelper  # noqa

        with pytest.raises(ValueError):
            cronhelper.cron_helper.quartz_to_unix(quartz_cron)

    def test_plugins_dependency_versions(self):
        from brickflow import BrickflowProjectDeploymentSettings
        from brickflow.engine.task import get_brickflow_libraries

        settings = BrickflowProjectDeploymentSettings()
        settings.brickflow_project_runtime_version = "1.0.0"

        # List of libraries resolved from (dev)dependencies
        expected_libs = {}
        with open(
            str(Path(__file__).parent.parent / "poetry.lock"), "r", encoding="utf-8"
        ) as f:
            data = toml.load(f)
        for lib in data.get("package", []):
            expected_libs[lib.get("name")] = lib.get("version")

        # Libraries used for plugins expected to be available in the dev environment
        # and should match the versions in poetry.lock to ensure consistency
        for lib in get_brickflow_libraries(enable_plugins=True):
            name, version = lib.package.split("==")
            if name != "brickflows":
                assert name in expected_libs
                assert (
                    version == expected_libs[name]
                ), f"Version mismatch for {name}: expected {expected_libs[name]}, got {version}"
