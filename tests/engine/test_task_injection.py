"""Unit tests for task injection functionality."""

import os
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from brickflow.engine.task_injection_config import (
    TaskInjectionConfig,
    TaskDefinition,
)
from brickflow.engine.task_executor import GenericTaskExecutor, ArtifactoryClient
from brickflow.engine.workflow import Workflow


class TestTaskInjectionConfig:
    """Test suite for TaskInjectionConfig."""

    def test_from_yaml_basic(self, tmp_path):
        """Test loading basic YAML configuration."""
        yaml_content = """
global:
  enabled: true
  default_libraries:
    - "requests>=2.28.0"

tasks:
  - task_name: "test_task"
    enabled: true
    libraries:
      - "pytest>=7.0.0"
    depends_on_strategy: "leaf_nodes"
    template_context:
      imports:
        - "from test import TestClass"
      config_class: "TestConfig"
      config_params:
        param1: "value1"
      utility_class: "TestUtility"
      method_name: "run"
"""
        yaml_file = tmp_path / "test_config.yaml"
        yaml_file.write_text(yaml_content)

        config = TaskInjectionConfig.from_yaml(str(yaml_file))

        assert config.global_config.enabled is True
        assert len(config.global_config.default_libraries) == 1
        assert len(config.tasks) == 1
        assert config.tasks[0].task_name == "test_task"
        assert config.tasks[0].enabled is True

    def test_disabled_task(self, tmp_path):
        """Test that disabled tasks are not loaded."""
        yaml_content = """
global:
  enabled: true

tasks:
  - task_name: "enabled_task"
    enabled: true
    libraries:
      - "requests>=2.28.0"
  
  - task_name: "disabled_task"
    enabled: false
    libraries:
      - "pandas>=1.0.0"
"""
        yaml_file = tmp_path / "test_config.yaml"
        yaml_file.write_text(yaml_content)

        config = TaskInjectionConfig.from_yaml(str(yaml_file))

        assert len(config.tasks) == 2
        assert config.tasks[0].enabled is True
        assert config.tasks[1].enabled is False

    def test_resolve_env_var(self):
        """Test environment variable resolution."""
        os.environ["TEST_VAR"] = "test_value"

        # Test ${VAR} format
        result = TaskInjectionConfig._resolve_env_var("${TEST_VAR}")
        assert result == "test_value"

        # Test $VAR format
        result = TaskInjectionConfig._resolve_env_var("$TEST_VAR")
        assert result == "test_value"

        # Test plain string
        result = TaskInjectionConfig._resolve_env_var("plain_value")
        assert result == "plain_value"

        # Cleanup
        del os.environ["TEST_VAR"]

    def test_artifact_config(self, tmp_path):
        """Test artifact configuration parsing."""
        yaml_content = """
global:
  enabled: true
  artifactory_username: "user"
  artifactory_api_key: "key"

tasks:
  - task_name: "test_task"
    enabled: true
    artifact:
      url: "https://example.com/artifact.whl"
      install_as_library: true
"""
        yaml_file = tmp_path / "test_config.yaml"
        yaml_file.write_text(yaml_content)

        config = TaskInjectionConfig.from_yaml(str(yaml_file))

        assert config.tasks[0].artifact is not None
        assert config.tasks[0].artifact.url == "https://example.com/artifact.whl"
        assert config.tasks[0].artifact.install_as_library is True
        assert config.tasks[0].artifact.username == "user"
        assert config.tasks[0].artifact.api_key == "key"


class TestGenericTaskExecutor:
    """Test suite for GenericTaskExecutor."""

    def test_create_task_function_basic(self, tmp_path):
        """Test creating a basic task function."""
        # Create a simple template
        template_file = tmp_path / "test_template.py.j2"
        template_file.write_text(
            """
{{ imports[0] }}

result = "test_result"
return result
"""
        )

        task_def = TaskDefinition(
            task_name="test_task",
            enabled=True,
            template_file=str(template_file),
            template_context={"imports": ["import sys"]},
            libraries=["pytest>=7.0.0"],
            depends_on_strategy="leaf_nodes",
        )

        executor = GenericTaskExecutor(task_def)
        task_func = executor.create_task_function()

        assert callable(task_func)
        assert task_func.__name__ == "test_task"

    def test_load_and_render_template(self, tmp_path):
        """Test template loading and rendering."""
        template_file = tmp_path / "test_template.py.j2"
        template_file.write_text(
            """
from {{ package }} import {{ class_name }}

config = {{ class_name }}(value="{{ value }}")
"""
        )

        task_def = TaskDefinition(
            task_name="test_task",
            template_file=str(template_file),
            template_context={
                "package": "mypackage",
                "class_name": "MyClass",
                "value": "test_value",
            },
        )

        executor = GenericTaskExecutor(task_def)
        rendered = executor._load_and_render_template(task_def)

        assert "from mypackage import MyClass" in rendered
        assert 'config = MyClass(value="test_value")' in rendered

    def test_uses_default_template_when_not_specified(self):
        """Test that default template is used when not specified."""
        task_def = TaskDefinition(
            task_name="test_task",
            template_context={
                "imports": ["import datetime"],
                "task_name": "test_task",
                "message": "This is a test task",
                "params": {"key": "value", "timestamp": "2025-11-20"},
            },
        )

        executor = GenericTaskExecutor(task_def)

        # Should use default template without error
        rendered = executor._load_and_render_template(task_def)
        assert "import datetime" in rendered
        assert "test_task" in rendered
        assert "This is a test task" in rendered
        assert "key: value" in rendered


class TestArtifactoryClient:
    """Test suite for ArtifactoryClient."""

    @patch("brickflow.engine.task_executor.requests.get")
    def test_download_artifact_success(self, mock_get):
        """Test successful artifact download."""
        # Mock response
        mock_response = Mock()
        mock_response.iter_content = Mock(return_value=[b"test", b"data"])
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        client = ArtifactoryClient(username="user", api_key="key")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".whl") as tmp:
            tmp_path = Path(tmp.name)

        try:
            result = client.download_artifact(
                "https://example.com/artifact.whl", tmp_path
            )

            assert result == tmp_path
            assert mock_get.called

            # Verify headers
            call_args = mock_get.call_args
            assert "X-JFrog-Art-Api" in call_args.kwargs["headers"]

        finally:
            if tmp_path.exists():
                tmp_path.unlink()

    @patch("brickflow.engine.task_executor.requests.get")
    def test_download_artifact_failure(self, mock_get):
        """Test artifact download failure."""
        # Mock failed response
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = Exception("Download failed")
        mock_get.return_value = mock_response

        client = ArtifactoryClient()

        with pytest.raises(Exception, match="Download failed"):
            client.download_artifact("https://example.com/artifact.whl")


class TestWorkflowInjection:
    """Test suite for workflow task injection."""

    def test_find_leaf_nodes(self):
        """Test finding leaf nodes in a workflow."""
        from brickflow.engine.project import _Project

        # Create a workflow with tasks
        workflow = Workflow("test_workflow")

        # Add tasks to create a DAG
        # task1 -> task2 -> task3 (leaf)
        # task1 -> task4 (leaf)
        @workflow.task()
        def task1():
            return "task1"

        @workflow.task(depends_on="task1")
        def task2():
            return "task2"

        @workflow.task(depends_on="task2")
        def task3():
            return "task3"

        @workflow.task(depends_on="task1")
        def task4():
            return "task4"

        project = _Project(name="test_project")
        leaf_nodes = project._find_leaf_nodes(workflow)

        # task3 and task4 should be leaf nodes
        assert set(leaf_nodes) == {"task3", "task4"}

    def test_get_injection_dependencies_leaf_nodes(self):
        """Test dependency resolution for leaf_nodes strategy."""
        from brickflow.engine.project import _Project

        workflow = Workflow("test_workflow")

        @workflow.task()
        def task1():
            return "task1"

        @workflow.task(depends_on="task1")
        def task2():
            return "task2"

        project = _Project(name="test_project")
        depends_on = project._get_injection_dependencies(workflow, "leaf_nodes")

        assert depends_on == ["task2"]

    def test_get_injection_dependencies_all_tasks(self):
        """Test dependency resolution for all_tasks strategy."""
        from brickflow.engine.project import _Project

        workflow = Workflow("test_workflow")
        project = _Project(name="test_project")

        depends_on = project._get_injection_dependencies(workflow, "all_tasks")

        # Should return None (no dependencies, runs first)
        assert depends_on is None

    def test_find_root_tasks(self):
        """Test finding root tasks in a workflow."""
        from brickflow.engine.project import _Project

        workflow = Workflow("test_workflow")

        # Create a workflow with multiple root tasks and dependencies
        @workflow.task()
        def root_task1():
            return "root1"

        @workflow.task()
        def root_task2():
            return "root2"

        @workflow.task(depends_on="root_task1")
        def child_task():
            return "child"

        project = _Project(name="test_project")
        root_tasks = project._find_root_tasks(workflow)

        # root_task1 and root_task2 should be root tasks (no dependencies)
        # child_task depends on root_task1, so it's not a root task
        assert set(root_tasks) == {"root_task1", "root_task2"}

    def test_find_root_tasks_empty_workflow(self):
        """Test finding root tasks in an empty workflow."""
        from brickflow.engine.project import _Project

        workflow = Workflow("test_workflow")
        project = _Project(name="test_project")

        root_tasks = project._find_root_tasks(workflow)

        # Empty workflow should have no root tasks
        assert not root_tasks

    def test_update_root_tasks_dependencies(self):
        """Test updating root tasks to depend on injected task."""
        from brickflow.engine.project import _Project

        workflow = Workflow("test_workflow")

        # Create root tasks
        @workflow.task()
        def root_task1():
            return "root1"

        @workflow.task()
        def root_task2():
            return "root2"

        # Simulate injected task
        workflow.graph.add_node("injected_task")
        workflow.graph.add_edge("root", "injected_task")

        project = _Project(name="test_project")

        # Find current root tasks
        root_tasks = project._find_root_tasks(workflow)
        assert set(root_tasks) == {"root_task1", "root_task2"}

        # Update dependencies
        project._update_root_tasks_dependencies(workflow, root_tasks, "injected_task")

        # Verify edges were added
        assert workflow.graph.has_edge("injected_task", "root_task1")
        assert workflow.graph.has_edge("injected_task", "root_task2")

        # Verify injected_task has no dependencies (except root)
        injected_predecessors = list(workflow.graph.predecessors("injected_task"))
        assert injected_predecessors == ["root"]

    def test_all_tasks_strategy_complete_flow(self):
        """Test complete flow of all_tasks strategy with dependency updates."""
        from brickflow.engine.project import _Project

        workflow = Workflow("test_workflow")

        # Create three parallel root tasks
        @workflow.task()
        def task1():
            return "task1"

        @workflow.task()
        def task2():
            return "task2"

        @workflow.task()
        def task3():
            return "task3"

        project = _Project(name="test_project")

        # Before injection, verify all are root tasks
        root_tasks_before = project._find_root_tasks(workflow)
        assert set(root_tasks_before) == {"task1", "task2", "task3"}

        # Simulate injecting task with all_tasks strategy
        # Add injected task with no dependencies
        workflow.graph.add_node("injected_task")
        workflow.graph.add_edge("root", "injected_task")

        # Add to tasks dict (simulating what _add_task does)
        mock_task = Mock()
        mock_task.name = "injected_task"
        workflow.tasks["injected_task"] = mock_task

        # Update root tasks to depend on injected task
        project._update_root_tasks_dependencies(
            workflow, root_tasks_before, "injected_task"
        )

        # After injection, verify dependencies
        # injected_task should run first (only depends on root)
        injected_preds = [
            p for p in workflow.graph.predecessors("injected_task") if p != "root"
        ]
        assert injected_preds == []

        # All original root tasks should now depend on injected_task
        task1_preds = list(workflow.graph.predecessors("task1"))
        task2_preds = list(workflow.graph.predecessors("task2"))
        task3_preds = list(workflow.graph.predecessors("task3"))

        assert "injected_task" in task1_preds
        assert "injected_task" in task2_preds
        assert "injected_task" in task3_preds

        # Verify new root task is only injected_task
        new_root_tasks = project._find_root_tasks(workflow)
        assert new_root_tasks == ["injected_task"]

    def test_get_injection_dependencies_specific_tasks(self):
        """Test dependency resolution for specific_tasks strategy."""
        from brickflow.engine.project import _Project

        workflow = Workflow("test_workflow")
        project = _Project(name="test_project")

        depends_on = project._get_injection_dependencies(
            workflow, "specific_tasks:task1,task2,task3"
        )

        assert depends_on == ["task1", "task2", "task3"]

    @patch.dict(os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": ""})
    def test_injection_disabled_when_no_config(self):
        """Test that injection is skipped when config path not set."""
        from brickflow.engine.project import _Project

        workflow = Workflow("test_workflow")

        @workflow.task()
        def task1():
            return "task1"

        project = _Project(name="test_project")
        initial_task_count = len(workflow.tasks)

        # Should not raise error, just skip injection
        project._inject_tasks_from_yaml(workflow)

        # Task count should remain the same
        assert len(workflow.tasks) == initial_task_count


class TestIntegration:
    """Integration tests for task injection."""

    def test_end_to_end_injection(self, tmp_path):
        """Test complete task injection flow."""
        # Create template
        template_file = tmp_path / "template.py.j2"
        template_file.write_text(
            """
{{ imports[0] }}

result = "{{ task_name }}_result"
return result
"""
        )

        # Create YAML config
        yaml_content = f"""
global:
  enabled: true

tasks:
  - task_name: "injected_task"
    enabled: true
    template_file: "{template_file}"
    template_context:
      imports:
        - "import sys"
      task_name: "injected_task"
    depends_on_strategy: "leaf_nodes"
"""
        yaml_file = tmp_path / "config.yaml"
        yaml_file.write_text(yaml_content)

        # Create workflow
        workflow = Workflow("test_workflow")

        @workflow.task()
        def original_task():
            return "original"

        # Inject task
        from brickflow.engine.project import _Project

        project = _Project(name="test_project")

        with patch.dict(os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(yaml_file)}):
            project._inject_tasks_from_yaml(workflow)

        # Verify injection
        assert "injected_task" in workflow.tasks
        assert len(workflow.tasks) == 2

        # Verify dependencies
        injected_task = workflow.tasks["injected_task"]
        assert injected_task is not None

    def test_end_to_end_all_tasks_strategy(self, tmp_path):
        """Test complete task injection flow with all_tasks strategy."""
        # Create template
        template_file = tmp_path / "template.py.j2"
        template_file.write_text(
            """
{{ imports[0] }}

result = "{{ task_name }}_result"
return result
"""
        )

        # Create YAML config with all_tasks strategy
        yaml_content = f"""
global:
  enabled: true

tasks:
  - task_name: "setup_task"
    enabled: true
    template_file: "{template_file}"
    template_context:
      imports:
        - "import sys"
      task_name: "setup_task"
    depends_on_strategy: "all_tasks"
"""
        yaml_file = tmp_path / "config.yaml"
        yaml_file.write_text(yaml_content)

        # Create workflow with multiple root tasks
        workflow = Workflow("test_workflow")

        @workflow.task()
        def task1():
            return "task1"

        @workflow.task()
        def task2():
            return "task2"

        @workflow.task(depends_on="task1")
        def task3():
            return "task3"

        # Inject task
        from brickflow.engine.project import _Project

        project = _Project(name="test_project")

        # Before injection: task1 and task2 are root tasks
        root_before = project._find_root_tasks(workflow)
        assert set(root_before) == {"task1", "task2"}

        with patch.dict(os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(yaml_file)}):
            project._inject_tasks_from_yaml(workflow)

        # Verify injection
        assert "setup_task" in workflow.tasks
        assert len(workflow.tasks) == 4

        # After injection: setup_task should be the only root task
        root_after = project._find_root_tasks(workflow)
        assert root_after == ["setup_task"]

        # Verify all original root tasks now depend on setup_task
        assert workflow.graph.has_edge("setup_task", "task1")
        assert workflow.graph.has_edge("setup_task", "task2")

        # task3 should still depend on task1 (unchanged)
        assert workflow.graph.has_edge("task1", "task3")

        # setup_task should have no dependencies except root
        setup_preds = [
            p for p in workflow.graph.predecessors("setup_task") if p != "root"
        ]
        assert setup_preds == []


class TestTaskInjectionEdgeCases:
    """Test edge cases and error handling for task injection."""

    def test_empty_yaml_file(self, tmp_path):
        """Test handling of empty YAML configuration file."""
        yaml_file = tmp_path / "empty_config.yaml"
        yaml_file.write_text("")

        config = TaskInjectionConfig.from_yaml(str(yaml_file))

        assert config.global_config.enabled is True
        assert len(config.tasks) == 0

    def test_global_config_disabled(self, tmp_path):
        """Test that task injection is skipped when global config is disabled."""
        yaml_content = """
global:
  enabled: false

tasks:
  - task_name: "test_task"
    enabled: true
"""
        yaml_file = tmp_path / "config.yaml"
        yaml_file.write_text(yaml_content)

        workflow = Workflow("test_workflow")

        @workflow.task()
        def task1():
            return "task1"

        from brickflow.engine.project import _Project

        project = _Project(name="test_project")

        with patch.dict(os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(yaml_file)}):
            project._inject_tasks_from_yaml(workflow)

        # Verify no tasks were injected
        assert "test_task" not in workflow.tasks
        assert len(workflow.tasks) == 1  # Only the original task1

    def test_task_with_artifact_download(self, tmp_path):
        """Test task creation with artifact download."""
        # Create a simple template
        template_file = tmp_path / "test_template.py.j2"
        template_file.write_text(
            """
import sys
result = "artifact_test_result"
"""
        )

        # Create a mock artifact file
        artifact_file = tmp_path / "test_artifact.whl"
        artifact_file.write_text("mock artifact content")

        from brickflow.engine.task_injection_config import ArtifactConfig

        task_def = TaskDefinition(
            task_name="test_task_with_artifact",
            enabled=True,
            template_file=str(template_file),
            template_context={"task_name": "test_task_with_artifact"},
            libraries=["pytest>=7.0.0"],
            depends_on_strategy="leaf_nodes",
            artifact=ArtifactConfig(
                url=f"file://{artifact_file}",
                username=None,
                api_key=None,
                install_as_library=False,
            ),
        )

        executor = GenericTaskExecutor(task_def)

        # Mock the download to avoid actual HTTP calls
        with patch.object(
            ArtifactoryClient, "download_artifact", return_value=artifact_file
        ):
            task_func = executor.create_task_function()
            result = task_func()

        assert result == "artifact_test_result"

    def test_disabled_task_workflow_integration(self, tmp_path):
        """Test that disabled tasks are skipped during workflow injection."""
        template_file = tmp_path / "test_template.py.j2"
        template_file.write_text(
            """
result = "test_result"
"""
        )

        yaml_content = f"""
global:
  enabled: true

tasks:
  - task_name: "enabled_task"
    enabled: true
    template_file: "{template_file}"
    depends_on_strategy: "leaf_nodes"
  
  - task_name: "disabled_task"
    enabled: false
    template_file: "{template_file}"
    depends_on_strategy: "leaf_nodes"
"""
        yaml_file = tmp_path / "config.yaml"
        yaml_file.write_text(yaml_content)

        workflow = Workflow("test_workflow")

        @workflow.task()
        def task1():
            return "task1"

        from brickflow.engine.project import _Project

        project = _Project(name="test_project")

        with patch.dict(os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(yaml_file)}):
            project._inject_tasks_from_yaml(workflow)

        # Verify only enabled task was injected
        assert "enabled_task" in workflow.tasks
        assert "disabled_task" not in workflow.tasks
        assert len(workflow.tasks) == 2  # task1 + enabled_task


class TestWorkflowSpecificConfigFiles:
    """Test suite for workflow-specific config files feature."""

    def test_global_config_only(self, tmp_path):
        """Test that global config injects tasks into all workflows."""
        template_file = tmp_path / "test_template.py.j2"
        template_file.write_text(
            """
result = "test_result"
"""
        )

        # Create global config
        global_yaml_content = f"""
global:
  enabled: true

tasks:
  - task_name: "global_task"
    enabled: true
    template_file: "{template_file}"
    depends_on_strategy: "leaf_nodes"
"""
        global_yaml_file = tmp_path / "global_config.yaml"
        global_yaml_file.write_text(global_yaml_content)

        # Create two workflows
        workflow1 = Workflow("etl_daily")
        workflow2 = Workflow("ml_training")

        @workflow1.task()
        def task1():
            return "task1"

        @workflow2.task()
        def task1_w2():
            return "task1"

        from brickflow.engine.project import _Project

        project = _Project(name="test_project")

        with patch.dict(
            os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(global_yaml_file)}
        ):
            project._inject_tasks_from_yaml(workflow1)
            project._inject_tasks_from_yaml(workflow2)

        # Verify global task was injected into both workflows
        assert "global_task" in workflow1.tasks
        assert "global_task" in workflow2.tasks

    def test_workflow_specific_config_only(self, tmp_path):
        """Test that workflow-specific config only injects into matching workflow."""
        template_file = tmp_path / "test_template.py.j2"
        template_file.write_text(
            """
result = "test_result"
"""
        )

        # Create workflow-specific config directory
        config_dir = tmp_path / "injected_tasks"
        config_dir.mkdir()

        # Create config for etl_daily workflow
        etl_yaml_content = f"""
global:
  enabled: true

tasks:
  - task_name: "etl_specific_task"
    enabled: true
    template_file: "{template_file}"
    depends_on_strategy: "leaf_nodes"
"""
        etl_yaml_file = config_dir / "etl_daily.yaml"
        etl_yaml_file.write_text(etl_yaml_content)

        # Create two workflows
        workflow1 = Workflow("etl_daily")
        workflow2 = Workflow("ml_training")

        @workflow1.task()
        def task1():
            return "task1"

        @workflow2.task()
        def task1_w2():
            return "task1"

        from brickflow.engine.project import _Project

        project = _Project(name="test_project")

        with patch.dict(os.environ, {"BRICKFLOW_INJECT_TASKS_DIR": str(config_dir)}):
            project._inject_tasks_from_yaml(workflow1)
            project._inject_tasks_from_yaml(workflow2)

        # Verify etl_specific_task was only injected into etl_daily
        assert "etl_specific_task" in workflow1.tasks
        assert "etl_specific_task" not in workflow2.tasks
        assert len(workflow1.tasks) == 2  # task1 + etl_specific_task
        assert len(workflow2.tasks) == 1  # task1 only

    def test_both_global_and_workflow_specific(self, tmp_path):
        """Test that both global and workflow-specific configs work together."""
        template_file = tmp_path / "test_template.py.j2"
        template_file.write_text(
            """
result = "test_result"
"""
        )

        # Create global config
        global_yaml_content = f"""
global:
  enabled: true

tasks:
  - task_name: "global_task"
    enabled: true
    template_file: "{template_file}"
    depends_on_strategy: "leaf_nodes"
"""
        global_yaml_file = tmp_path / "global_config.yaml"
        global_yaml_file.write_text(global_yaml_content)

        # Create workflow-specific config directory
        config_dir = tmp_path / "injected_tasks"
        config_dir.mkdir()

        # Create config for etl_daily workflow
        etl_yaml_content = f"""
global:
  enabled: true

tasks:
  - task_name: "etl_specific_task"
    enabled: true
    template_file: "{template_file}"
    depends_on_strategy: "leaf_nodes"
"""
        etl_yaml_file = config_dir / "etl_daily.yaml"
        etl_yaml_file.write_text(etl_yaml_content)

        # Create two workflows
        workflow1 = Workflow("etl_daily")
        workflow2 = Workflow("ml_training")

        @workflow1.task()
        def task1():
            return "task1"

        @workflow2.task()
        def task1_w2():
            return "task1"

        from brickflow.engine.project import _Project

        project = _Project(name="test_project")

        with patch.dict(
            os.environ,
            {
                "BRICKFLOW_INJECT_TASKS_CONFIG": str(global_yaml_file),
                "BRICKFLOW_INJECT_TASKS_DIR": str(config_dir),
            },
        ):
            project._inject_tasks_from_yaml(workflow1)
            project._inject_tasks_from_yaml(workflow2)

        # Verify etl_daily gets both global and specific tasks
        assert "global_task" in workflow1.tasks
        assert "etl_specific_task" in workflow1.tasks
        assert len(workflow1.tasks) == 3  # task1 + global_task + etl_specific_task

        # Verify ml_training gets only global task
        assert "global_task" in workflow2.tasks
        assert "etl_specific_task" not in workflow2.tasks
        assert len(workflow2.tasks) == 2  # task1 + global_task

    def test_missing_workflow_specific_file_no_error(self, tmp_path):
        """Test that missing workflow-specific file doesn't cause errors."""
        # Create empty config directory
        config_dir = tmp_path / "injected_tasks"
        config_dir.mkdir()

        # Create workflow
        workflow = Workflow("etl_daily")

        @workflow.task()
        def task1():
            return "task1"

        from brickflow.engine.project import _Project

        project = _Project(name="test_project")

        # Should not raise error even though etl_daily.yaml doesn't exist
        with patch.dict(os.environ, {"BRICKFLOW_INJECT_TASKS_DIR": str(config_dir)}):
            project._inject_tasks_from_yaml(workflow)

        # Verify no tasks were injected
        assert len(workflow.tasks) == 1  # Only task1

    def test_workflow_specific_wrong_workflow(self, tmp_path):
        """Test that workflow-specific config doesn't apply to wrong workflow."""
        template_file = tmp_path / "test_template.py.j2"
        template_file.write_text(
            """
result = "test_result"
"""
        )

        # Create workflow-specific config directory
        config_dir = tmp_path / "injected_tasks"
        config_dir.mkdir()

        # Create config for etl_daily workflow
        etl_yaml_content = f"""
global:
  enabled: true

tasks:
  - task_name: "etl_task"
    enabled: true
    template_file: "{template_file}"
    depends_on_strategy: "leaf_nodes"
"""
        etl_yaml_file = config_dir / "etl_daily.yaml"
        etl_yaml_file.write_text(etl_yaml_content)

        # Create a different workflow
        workflow = Workflow("ml_training")

        @workflow.task()
        def task1():
            return "task1"

        from brickflow.engine.project import _Project

        project = _Project(name="test_project")

        with patch.dict(os.environ, {"BRICKFLOW_INJECT_TASKS_DIR": str(config_dir)}):
            project._inject_tasks_from_yaml(workflow)

        # Verify etl_task was NOT injected into ml_training workflow
        assert "etl_task" not in workflow.tasks
        assert len(workflow.tasks) == 1  # Only task1


class TestRuntimeInjectionReconstruction:
    """Tests for file-based injection: serialize at deploy, reconstruct at runtime."""

    def test_serialize_for_runtime_writes_file(self, tmp_path, monkeypatch):
        """serialize_for_runtime writes a .py file and returns a JSON pointer."""
        import json

        monkeypatch.chdir(tmp_path)

        template_file = tmp_path / "tmpl.py.j2"
        template_file.write_text('result = "{{ greeting }}"')

        task_def = TaskDefinition(
            task_name="hello_task",
            template_file=str(template_file),
            template_context={"greeting": "hi_from_deploy"},
        )

        executor = GenericTaskExecutor(task_def)
        config_json = executor.serialize_for_runtime()

        config = json.loads(config_json)
        assert config["task_name"] == "hello_task"
        assert config["task_type"] == "BRICKFLOW_TASK"
        assert config["file_ref"] == "_brickflow_injected/hello_task.py"
        assert "rendered_code" not in config
        assert "artifact" not in config

        written = (tmp_path / "_brickflow_injected" / "hello_task.py").read_text()
        assert 'result = "hi_from_deploy"' in written

    def test_serialize_for_runtime_with_artifact(self, tmp_path, monkeypatch):
        """Artifact metadata is preserved in the lightweight JSON pointer."""
        import json
        from brickflow.engine.task_injection_config import ArtifactConfig

        monkeypatch.chdir(tmp_path)

        template_file = tmp_path / "tmpl.py.j2"
        template_file.write_text("result = 1")

        task_def = TaskDefinition(
            task_name="art_task",
            template_file=str(template_file),
            artifact=ArtifactConfig(
                url="https://example.com/my.whl",
                install_as_library=True,
            ),
        )

        executor = GenericTaskExecutor(task_def)
        config = json.loads(executor.serialize_for_runtime())

        assert config["artifact"]["url"] == "https://example.com/my.whl"
        assert config["artifact"]["install_as_library"] is True
        assert config["file_ref"] == "_brickflow_injected/art_task.py"

    def test_create_task_function_from_workspace_file(self, tmp_path):
        """Runtime reads code from a workspace file when path is provided."""
        import json

        ws_file = tmp_path / "task_code.py"
        ws_file.write_text('result = "from_workspace"')

        config_json = json.dumps({
            "task_name": "ws_task",
            "task_type": "BRICKFLOW_TASK",
            "file_ref": "_brickflow_injected/ws_task.py",
        })

        task_func = GenericTaskExecutor.create_task_function_from_config(
            config_json, workspace_file_path=str(ws_file)
        )

        assert callable(task_func)
        assert task_func.__name__ == "ws_task"
        assert task_func() == "from_workspace"

    def test_create_task_function_fallback_to_inline(self):
        """Falls back to inline rendered_code for backward compat."""
        import json

        config_json = json.dumps({
            "task_name": "legacy_task",
            "task_type": "BRICKFLOW_TASK",
            "rendered_code": 'result = "rebuilt"',
        })

        task_func = GenericTaskExecutor.create_task_function_from_config(config_json)

        assert callable(task_func)
        assert task_func.__name__ == "legacy_task"
        assert task_func() == "rebuilt"

    def test_create_task_function_file_missing_falls_back(self, tmp_path):
        """When workspace file is missing, falls back to inline code."""
        import json

        config_json = json.dumps({
            "task_name": "fallback_task",
            "task_type": "BRICKFLOW_TASK",
            "rendered_code": 'result = "inline_fallback"',
        })

        task_func = GenericTaskExecutor.create_task_function_from_config(
            config_json, workspace_file_path=str(tmp_path / "does_not_exist.py")
        )

        assert task_func() == "inline_fallback"

    def test_create_task_function_no_code_raises(self):
        """Raises RuntimeError when neither file nor inline code is available."""
        import json

        config_json = json.dumps({
            "task_name": "empty_task",
            "task_type": "BRICKFLOW_TASK",
        })

        task_func = GenericTaskExecutor.create_task_function_from_config(config_json)

        with pytest.raises(RuntimeError, match="No code available"):
            task_func()

    def test_injection_config_json_stored_on_task(self, tmp_path, monkeypatch):
        """Injection config with file_ref is stored on the Task after injection."""
        monkeypatch.chdir(tmp_path)

        template_file = tmp_path / "tmpl.py.j2"
        template_file.write_text("result = 42")

        yaml_content = f"""
global:
  enabled: true

tasks:
  - task_name: "injected_task"
    enabled: true
    template_file: "{template_file}"
    depends_on_strategy: "leaf_nodes"
"""
        yaml_file = tmp_path / "config.yaml"
        yaml_file.write_text(yaml_content)

        workflow = Workflow("test_workflow")

        @workflow.task()
        def original_task():
            return "original"

        from brickflow.engine.project import _Project

        project = _Project(name="test_project")

        with patch.dict(
            os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(yaml_file)}
        ):
            project._inject_tasks_from_yaml(workflow)

        assert "injected_task" in workflow.tasks
        injected = workflow.tasks["injected_task"]
        assert injected.injection_config_json is not None

        import json

        baked = json.loads(injected.injection_config_json)
        assert baked["task_name"] == "injected_task"
        assert baked["file_ref"] == "_brickflow_injected/injected_task.py"

    def test_reconstruct_injected_task_from_workspace_file(self, tmp_path, monkeypatch):
        """End-to-end: serialize at deploy, reconstruct from workspace file at runtime."""
        import json

        monkeypatch.chdir(tmp_path)

        template_file = tmp_path / "tmpl.py.j2"
        template_file.write_text('result = "runtime_ok"')

        yaml_content = f"""
global:
  enabled: true

tasks:
  - task_name: "compliance_task"
    enabled: true
    template_file: "{template_file}"
    depends_on_strategy: "leaf_nodes"
"""
        yaml_file = tmp_path / "config.yaml"
        yaml_file.write_text(yaml_content)

        workflow = Workflow("my_workflow")

        @workflow.task()
        def setup():
            return "setup"

        from brickflow.engine.project import _Project, Project
        from brickflow.context import BrickflowInternalVariables

        project = _Project(name="test_project")

        with patch.dict(
            os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(yaml_file)}
        ):
            project._inject_tasks_from_yaml(workflow)

        baked_json = workflow.tasks["compliance_task"].injection_config_json
        assert baked_json is not None

        ws_file = tmp_path / "_brickflow_injected" / "compliance_task.py"
        assert ws_file.exists()

        runtime_workflow = Workflow("my_workflow")

        @runtime_workflow.task()
        def setup_rt():  # noqa: F811
            return "setup"

        assert "compliance_task" not in runtime_workflow.tasks

        def _mock_get_parameter(name, default=None):
            if name == BrickflowInternalVariables.injection_config.value:
                return baked_json
            if name == BrickflowInternalVariables.injection_file_path.value:
                return str(ws_file)
            return default

        with patch("brickflow.engine.project.ctx") as mock_ctx:
            mock_ctx.get_parameter.side_effect = _mock_get_parameter
            task = Project._reconstruct_injected_task(
                runtime_workflow, "compliance_task"
            )

        assert task is not None
        assert task.name == "compliance_task"
        assert "compliance_task" in runtime_workflow.tasks

    def test_reconstruct_raises_without_baked_config(self):
        """Reconstruction must fail clearly when no baked config is available."""
        from brickflow.engine.project import Project
        from brickflow.engine.task import TaskNotFoundError

        workflow = Workflow("my_workflow")

        @workflow.task()
        def task1():
            return "task1"

        with patch("brickflow.engine.project.ctx") as mock_ctx:
            mock_ctx.get_parameter.return_value = None

            with pytest.raises(TaskNotFoundError, match="compliance_task"):
                Project._reconstruct_injected_task(workflow, "compliance_task")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
