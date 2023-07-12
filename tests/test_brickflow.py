# pylint: disable=unused-import
from pathlib import Path
from unittest.mock import patch

import pytest

from brickflow.resolver import RelativePathPackageResolver


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


def test_path_resolver():
    with patch("brickflow.resolver.add_to_sys_path") as mock_add_to_sys_path, patch(
        "brickflow.RelativePathPackageResolver._get_current_file_path"
    ) as mock_get_current_file_path:
        mock_add_to_sys_path.return_value = None
        mock_get_current_file_path.return_value = "/Some/Fake/Path/file.py"

        # go up a directory and use the same
        RelativePathPackageResolver.add_relative_path(
            globals(), current_file_to_root="../", root_to_module="."
        )

        # Assertions
        mock_add_to_sys_path.assert_called_once_with(Path("/Some/Fake"))
        assert mock_get_current_file_path.called


def test_path_resolver_complex():
    with patch("brickflow.resolver.add_to_sys_path") as mock_add_to_sys_path, patch(
        "brickflow.RelativePathPackageResolver._get_current_file_path"
    ) as mock_get_current_file_path:
        mock_add_to_sys_path.return_value = None
        mock_get_current_file_path.return_value = "/Some/Fake/Path/file.py"

        # go up 2 directories and then to /some/module
        RelativePathPackageResolver.add_relative_path(
            globals(), current_file_to_root="../../", root_to_module="./some/module"
        )

        # Assertions
        mock_add_to_sys_path.assert_called_once_with(Path("/Some/some/module"))
        assert mock_get_current_file_path.called


def test_path_resolver_root_to_module_abs():
    with patch("brickflow.resolver.add_to_sys_path") as mock_add_to_sys_path, patch(
        "brickflow.RelativePathPackageResolver._get_current_file_path"
    ) as mock_get_current_file_path:
        mock_add_to_sys_path.return_value = None
        mock_get_current_file_path.return_value = "/Some/Fake/Path"

        # go up 2 directories and then to /some/module
        with pytest.raises(
            ValueError,
            match="root_to_module must be relative to the root of the project",
        ):
            RelativePathPackageResolver.add_relative_path(
                globals(), current_file_to_root="../../", root_to_module="/some/module"
            )
