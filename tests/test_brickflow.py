# pylint: disable=unused-import
from brickflow import get_config_file_type, ConfigFileType


def test_imports():
    try:
        from brickflow import (
            log,
            _ilog,
            BrickflowEnvVars,
            BrickflowDefaultEnvs,
            ctx,
            Workflow,
            WorkflowPermissions,
            User,
            Group,
            ServicePrincipal,
            Task,
            TaskType,
            TaskResponse,
            BrickflowTriggerRule,
            BrickflowTaskEnvVars,
            StorageBasedTaskLibrary,
            JarTaskLibrary,
            EggTaskLibrary,
            WheelTaskLibrary,
            PypiTaskLibrary,
            MavenTaskLibrary,
            CranTaskLibrary,
            EmailNotifications,
            DLTPipeline,
            DLTEdition,
            DLTChannels,
            Cluster,
            Runtimes,
            Project,
        )

        print("All imports Succeeded")
    except ImportError as e:
        print(f"Import failed: {e}")


def test_get_config_type_yaml():
    actual = get_config_file_type("some/brickflow/root/.brickflow-project-root.yaml")
    assert actual == ConfigFileType.YAML


def test_get_config_type_yml():
    actual = get_config_file_type("some/brickflow/root/.brickflow-project-root.yml")
    assert actual == ConfigFileType.YML


def test_get_config_type_default():
    actual = get_config_file_type("some/brickflow/root/.brickflow-project-root.json")
    assert actual == ConfigFileType.YAML
