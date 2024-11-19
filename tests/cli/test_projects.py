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
    cwd = os.getcwd()
    test_folder = str(Path(__file__).parent)

    # Creating empty test directories
    os.makedirs(f"{test_folder}/{project_folder}/some/dummy/dir", exist_ok=True)
    os.chdir(f"{test_folder}/{project_folder}/some/dummy/dir")

    actual = get_brickflow_root()
    assert actual == Path(
        f"{test_folder}/{project_folder}/brickflow-multi-project.{extension}"
    )

    # Cleanup
    shutil.rmtree(f"{test_folder}/{project_folder}/some")
    os.chdir(cwd)


@pytest.mark.parametrize(
    "project_folder, config_type",
    [
        ("sample_yml_project", ConfigFileType.YML),
        ("sample_yaml_project", ConfigFileType.YAML),
    ],
)
def test_multi_project_manager_yaml(project_folder, config_type):
    cwd = os.getcwd()
    test_folder = str(Path(__file__).parent)
    os.chdir(test_folder)

    config_file_name = (
        f"{test_folder}/{project_folder}/brickflow-multi-project.{config_type.value}"
    )
    manager = MultiProjectManager(
        config_file_name=config_file_name, file_type=config_type
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

    os.chdir(cwd)
