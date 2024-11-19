# pylint: disable=unused-import
import pytest
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


@pytest.mark.parametrize(
    "config_file_name,expected_extension",
    [
        (".brickflow-project-root.yaml", ConfigFileType.YAML),
        (".brickflow-project-root.yml", ConfigFileType.YML),
        (".brickflow-project-root.json", ConfigFileType.YAML),
    ],
)
def test_get_config_type(config_file_name, expected_extension):
    actual = get_config_file_type(f"some/brickflow/root/{config_file_name}")
    assert actual == expected_extension
