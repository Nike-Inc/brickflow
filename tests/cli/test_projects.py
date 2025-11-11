from pathlib import Path
import shutil
import os
import pytest
from brickflow import ConfigFileType
from brickflow.cli.projects import MultiProjectManager, get_brickflow_root


@pytest.mark.parametrize(
    "project_folder,extension",
    [("sample_yml_project", "yml"), ("sample_yaml_project", "yaml")],
)
def test_get_brickflow_root(project_folder, extension):
    cwd = Path.cwd()
    test_folder = Path(__file__).parent.resolve()

    # Creating empty test directories
    test_dir = test_folder / project_folder / "some" / "dummy" / "dir"
    test_dir.mkdir(parents=True, exist_ok=True)

    try:
        os.chdir(test_dir)

        actual = get_brickflow_root()
        expected = test_folder / project_folder / f"brickflow-multi-project.{extension}"
        assert actual.resolve().as_posix() == expected.resolve().as_posix()
    finally:
        # Cleanup
        os.chdir(cwd)
        shutil.rmtree(test_folder / project_folder / "some")


@pytest.mark.parametrize(
    "project_folder, config_type",
    [
        ("sample_yml_project", ConfigFileType.YML),
        ("sample_yaml_project", ConfigFileType.YAML),
    ],
)
def test_multi_project_manager_yaml(project_folder, config_type):
    cwd = Path.cwd()
    test_folder = Path(__file__).parent

    try:
        os.chdir(test_folder)

        config_file_name = (
            test_folder
            / project_folder
            / f"brickflow-multi-project.{config_type.value}"
        )
        manager = MultiProjectManager(
            config_file_name=str(config_file_name), file_type=config_type
        )
        assert manager._brickflow_multi_project_config.version == "v1"
        expected_project_config = {
            "version": "v1",
            "projects": {
                "test_cli_project": {
                    "name": "test_cli_project",
                    "path_from_repo_root_to_project_root": "some/test/path",
                    "path_project_root_to_workflows_dir": "path/to/workflows",
                    "deployment_mode": "bundle",
                    "brickflow_version": "1.2.1",
                    "enable_plugins": False,
                }
            },
        }
        assert manager._project_config_dict["."].model_dump() == expected_project_config
    finally:
        os.chdir(cwd)
