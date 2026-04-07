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
from brickflow.engine.project import _Project
from brickflow.engine.task import TaskType


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
        assert config.tasks[0].task_type == TaskType.BRICKFLOW_TASK

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

    def test_from_yaml_task_type_by_databricks_value(self, tmp_path):
        """task_type may use TaskType enum value strings (e.g. python_wheel_task)."""
        yaml_content = """
global:
  enabled: true
tasks:
  - task_name: "wheel_task"
    task_type: python_wheel_task"""
        yaml_file = tmp_path / "config.yaml"
        yaml_file.write_text(yaml_content)

        config = TaskInjectionConfig.from_yaml(str(yaml_file))

        assert config.tasks[0].task_type == TaskType.PYTHON_WHEEL_TASK


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


class TestNativeTaskInjection:
    """Tests for native Databricks task injection (unified approach)."""

    def test_inject_python_wheel_task_with_parameters(self, tmp_path):
        """Test injecting PYTHON_WHEEL_TASK with template variable resolution."""
        config_file = tmp_path / "inject_config.yaml"
        config_file.write_text(
            """
global:
  enabled: true
  default_libraries:
    - "goodbyepii>=1.0.0"

tasks:
  - task_name: "compliance_check_customers"
    enabled: true
    task_type: "PYTHON_WHEEL_TASK"
    task_config:
      package_name: "goodbyepii"
      entry_point: "databricks_task_runner.run_compliance_check_cli"
      parameters: ["{{catalog}}", "{{schema}}", "{{table}}"]
    template_context:
      catalog: "hive_metastore"
      schema: "gold"
      table: "customer_data"
    depends_on_strategy: "leaf_nodes"
    libraries:
      - "goodbyepii>=1.0.0"
"""
        )

        workflow = Workflow("test_workflow")

        @workflow.task()
        def root_task():
            return "root"

        project = _Project(name="test_project")

        with patch.dict(
            os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(config_file)}
        ):
            project._inject_tasks_from_yaml(workflow)

        # Verify task was injected
        assert "compliance_check_customers" in workflow.tasks
        injected_task = workflow.tasks["compliance_check_customers"]
        assert injected_task.task_type == TaskType.PYTHON_WHEEL_TASK

        # Verify task function returns correct object with resolved parameters
        from brickflow.engine.task import PythonWheelTask

        result = injected_task.task_func()
        assert isinstance(result, PythonWheelTask)
        assert result.package_name == "goodbyepii"
        assert result.entry_point == "databricks_task_runner.run_compliance_check_cli"
        assert result.parameters == ["hive_metastore", "gold", "customer_data"]

    def test_inject_spark_jar_task(self, tmp_path):
        """Test injecting SPARK_JAR_TASK with parameter resolution."""
        config_file = tmp_path / "inject_config.yaml"
        config_file.write_text(
            """
global:
  enabled: true

tasks:
  - task_name: "spark_jar_job"
    enabled: true
    task_type: "SPARK_JAR_TASK"
    task_config:
      main_class_name: "com.example.DataProcessor"
      parameters: ["--input", "{{input_path}}", "--output", "{{output_path}}"]
    template_context:
      input_path: "s3://bucket/input"
      output_path: "s3://bucket/output"
"""
        )

        workflow = Workflow("test_workflow")
        project = _Project(name="test_project")

        with patch.dict(
            os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(config_file)}
        ):
            project._inject_tasks_from_yaml(workflow)

        # Verify task
        from brickflow.engine.task import SparkJarTask

        result = workflow.tasks["spark_jar_job"].task_func()
        assert isinstance(result, SparkJarTask)
        assert result.main_class_name == "com.example.DataProcessor"
        assert result.parameters == [
            "--input",
            "s3://bucket/input",
            "--output",
            "s3://bucket/output",
        ]

    def test_inject_sql_task_with_named_parameters(self, tmp_path):
        """Test injecting SQL task with dict parameter resolution."""
        config_file = tmp_path / "inject_config.yaml"
        config_file.write_text(
            """
global:
  enabled: true

tasks:
  - task_name: "sql_query"
    enabled: true
    task_type: "SQL"
    task_config:
      warehouse_id: "abc123"
      query_id: "query_{{env}}"
      parameters:
        catalog: "{{catalog}}"
        schema: "{{schema}}"
    template_context:
      env: "dev"
      catalog: "production"
      schema: "analytics"
"""
        )

        workflow = Workflow("test_workflow")
        project = _Project(name="test_project")

        with patch.dict(
            os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(config_file)}
        ):
            project._inject_tasks_from_yaml(workflow)

        # Verify task
        from brickflow.engine.task import SqlTask

        result = workflow.tasks["sql_query"].task_func()
        assert isinstance(result, SqlTask)
        assert result.warehouse_id == "abc123"
        assert result.query_id == "query_dev"
        assert result.parameters == {"catalog": "production", "schema": "analytics"}

    def test_inject_notebook_task(self, tmp_path):
        """Test injecting NOTEBOOK_TASK with base_parameters."""
        config_file = tmp_path / "inject_config.yaml"
        config_file.write_text(
            """
global:
  enabled: true

tasks:
  - task_name: "run_analysis_notebook"
    enabled: true
    task_type: "NOTEBOOK_TASK"
    task_config:
      notebook_path: "/Workspace/notebooks/{{notebook_name}}"
      base_parameters:
        env: "{{env}}"
        table: "{{table}}"
      source: "WORKSPACE"
    template_context:
      notebook_name: "data_processing"
      env: "prod"
      table: "transactions"
"""
        )

        workflow = Workflow("test_workflow")
        project = _Project(name="test_project")

        with patch.dict(
            os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(config_file)}
        ):
            project._inject_tasks_from_yaml(workflow)

        # Verify task
        from brickflow.engine.task import NotebookTask

        result = workflow.tasks["run_analysis_notebook"].task_func()
        assert isinstance(result, NotebookTask)
        assert result.notebook_path == "/Workspace/notebooks/data_processing"
        assert result.base_parameters == {"env": "prod", "table": "transactions"}
        assert result.source == "WORKSPACE"

    def test_inject_spark_python_task(self, tmp_path):
        """Test injecting SPARK_PYTHON_TASK."""
        config_file = tmp_path / "inject_config.yaml"
        config_file.write_text(
            """
global:
  enabled: true

tasks:
  - task_name: "spark_python_job"
    enabled: true
    task_type: "SPARK_PYTHON_TASK"
    task_config:
      python_file: "scripts/{{script_name}}.py"
      source: "GIT"
      parameters: ["--env", "{{env}}"]
    template_context:
      script_name: "process_data"
      env: "prod"
"""
        )

        workflow = Workflow("test_workflow")
        project = _Project(name="test_project")

        with patch.dict(
            os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(config_file)}
        ):
            project._inject_tasks_from_yaml(workflow)

        # Verify task
        from brickflow.engine.task import SparkPythonTask

        result = workflow.tasks["spark_python_job"].task_func()
        assert isinstance(result, SparkPythonTask)
        assert result.python_file == "scripts/process_data.py"
        assert result.source == "GIT"
        assert result.parameters == ["--env", "prod"]

    def test_mixed_task_types_in_one_config(self, tmp_path, monkeypatch):
        """Test injecting both BRICKFLOW_TASK and native tasks in one config."""
        monkeypatch.chdir(tmp_path)

        template_file = tmp_path / "template.py.j2"
        template_file.write_text('result = "{{ message }}"')

        config_file = tmp_path / "inject_config.yaml"
        config_file.write_text(
            f"""
global:
  enabled: true
  default_libraries:
    - "goodbyepii>=1.0.0"

tasks:
  # File-based BRICKFLOW_TASK
  - task_name: "custom_validation"
    task_type: "BRICKFLOW_TASK"
    template_file: "{template_file}"
    template_context:
      message: "Validation logic"
    depends_on_strategy: "leaf_nodes"
  
  # Native PYTHON_WHEEL_TASK
  - task_name: "compliance_check"
    task_type: "PYTHON_WHEEL_TASK"
    task_config:
      package_name: "goodbyepii"
      entry_point: "run_cli"
      parameters: ["{{{{catalog}}}}"]
    template_context:
      catalog: "main"
  
  # Native SQL task
  - task_name: "sql_query"
    task_type: "SQL"
    task_config:
      warehouse_id: "warehouse_123"
      query_id: "query_{{{{env}}}}"
    template_context:
      env: "dev"
"""
        )

        workflow = Workflow("test_workflow")

        @workflow.task()
        def root_task():
            return "root"

        project = _Project(name="test_project")

        with patch.dict(
            os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(config_file)}
        ):
            project._inject_tasks_from_yaml(workflow)

        # Verify all tasks were injected
        assert "custom_validation" in workflow.tasks
        assert "compliance_check" in workflow.tasks
        assert "sql_query" in workflow.tasks

        # Verify BRICKFLOW_TASK
        custom_task = workflow.tasks["custom_validation"]
        assert custom_task.task_type == TaskType.BRICKFLOW_TASK

        # Verify native tasks return correct objects
        from brickflow.engine.task import PythonWheelTask, SqlTask

        compliance_result = workflow.tasks["compliance_check"].task_func()
        assert isinstance(compliance_result, PythonWheelTask)
        assert compliance_result.package_name == "goodbyepii"
        # Note: PythonWheelTask doesn't store parameters - it's passed in config only
        # assert compliance_result.parameters == ["main"]

        sql_result = workflow.tasks["sql_query"].task_func()
        assert isinstance(sql_result, SqlTask)
        assert sql_result.warehouse_id == "warehouse_123"
        assert sql_result.query_id == "query_dev"

    def test_native_task_with_workflow_specific_config(self, tmp_path):
        """Test native tasks work with BRICKFLOW_INJECT_TASKS_DIR."""
        config_dir = tmp_path / "inject_tasks"
        config_dir.mkdir()

        workflow_config = config_dir / "my_workflow.yaml"
        workflow_config.write_text(
            """
global:
  enabled: true

tasks:
  - task_name: "workflow_specific_wheel_task"
    enabled: true
    task_type: "PYTHON_WHEEL_TASK"
    task_config:
      package_name: "mypackage"
      entry_point: "run_task"
      parameters: ["param1", "param2"]
"""
        )

        workflow = Workflow("my_workflow")
        project = _Project(name="test_project")

        with patch.dict(os.environ, {"BRICKFLOW_INJECT_TASKS_DIR": str(config_dir)}):
            project._inject_tasks_from_yaml(workflow)

        # Verify injection worked
        assert "workflow_specific_wheel_task" in workflow.tasks
        from brickflow.engine.task import PythonWheelTask

        result = workflow.tasks["workflow_specific_wheel_task"].task_func()
        assert isinstance(result, PythonWheelTask)
        assert result.package_name == "mypackage"
        assert result.parameters == ["param1", "param2"]

    def test_error_on_native_task_without_config(self, tmp_path):
        """Test that native task types require task_config."""
        config_file = tmp_path / "inject_config.yaml"
        config_file.write_text(
            """
global:
  enabled: true

tasks:
  - task_name: "bad_task"
    task_type: "PYTHON_WHEEL_TASK"
"""
        )

        workflow = Workflow("test_workflow")
        project = _Project(name="test_project")

        with patch.dict(
            os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(config_file)}
        ):
            with pytest.raises(ValueError, match="task_config"):
                project._inject_tasks_from_yaml(workflow)

    def test_error_on_unsupported_native_task_type(self, tmp_path):
        """Test that unsupported native task types raise error."""
        config_file = tmp_path / "inject_config.yaml"
        config_file.write_text(
            """
global:
  enabled: true

tasks:
  - task_name: "bad_task"
    task_type: "INVALID_TASK_TYPE"
    task_config:
      some_config: "value"
"""
        )

        workflow = Workflow("test_workflow")
        project = _Project(name="test_project")

        with patch.dict(
            os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(config_file)}
        ):
            with pytest.raises(ValueError, match="Unknown task_type"):
                project._inject_tasks_from_yaml(workflow)

    def test_nested_parameter_resolution(self, tmp_path):
        """Test that template variables work in nested dicts and lists."""
        config_file = tmp_path / "inject_config.yaml"
        config_file.write_text(
            """
global:
  enabled: true

tasks:
  - task_name: "complex_params"
    enabled: true
    task_type: "PYTHON_WHEEL_TASK"
    task_config:
      package_name: "mypackage"
      entry_point: "main"
      parameters: ["{{arg1}}", "literal", "{{arg2}}"]
      named_parameters:
        key1: "{{value1}}"
        key2: "literal_value"
        key3: "{{value2}}"
    template_context:
      arg1: "resolved_arg1"
      arg2: "resolved_arg2"
      value1: "resolved_value1"
      value2: "resolved_value2"
"""
        )

        workflow = Workflow("test_workflow")
        project = _Project(name="test_project")

        with patch.dict(
            os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(config_file)}
        ):
            project._inject_tasks_from_yaml(workflow)

        # Verify nested parameter resolution
        from brickflow.engine.task import PythonWheelTask

        result = workflow.tasks["complex_params"].task_func()
        assert isinstance(result, PythonWheelTask)
        assert result.parameters == ["resolved_arg1", "literal", "resolved_arg2"]
        assert result.named_parameters == {
            "key1": "resolved_value1",
            "key2": "literal_value",
            "key3": "resolved_value2",
        }

    def test_inject_notebook_task(self, tmp_path):
        """Test injecting NOTEBOOK_TASK."""
        config_file = tmp_path / "inject_config.yaml"
        config_file.write_text(
            """
global:
  enabled: true

tasks:
  - task_name: "run_analysis_notebook"
    enabled: true
    task_type: "NOTEBOOK_TASK"
    task_config:
      notebook_path: "/Workspace/notebooks/{{notebook_name}}"
      base_parameters:
        env: "{{env}}"
        table: "{{table}}"
      source: "WORKSPACE"
    template_context:
      notebook_name: "data_processing"
      env: "prod"
      table: "transactions"
"""
        )

        workflow = Workflow("test_workflow")
        project = _Project(name="test_project")

        with patch.dict(
            os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(config_file)}
        ):
            project._inject_tasks_from_yaml(workflow)

        # Verify task
        from brickflow.engine.task import NotebookTask

        result = workflow.tasks["run_analysis_notebook"].task_func()
        assert isinstance(result, NotebookTask)
        assert result.notebook_path == "/Workspace/notebooks/data_processing"
        assert result.base_parameters == {"env": "prod", "table": "transactions"}
        assert result.source == "WORKSPACE"

    def test_inject_spark_python_task(self, tmp_path):
        """Test injecting SPARK_PYTHON_TASK."""
        config_file = tmp_path / "inject_config.yaml"
        config_file.write_text(
            """
global:
  enabled: true

tasks:
  - task_name: "spark_python_job"
    enabled: true
    task_type: "SPARK_PYTHON_TASK"
    task_config:
      python_file: "scripts/{{script_name}}.py"
      source: "GIT"
      parameters: ["--env", "{{env}}"]
    template_context:
      script_name: "process_data"
      env: "prod"
"""
        )

        workflow = Workflow("test_workflow")
        project = _Project(name="test_project")

        with patch.dict(
            os.environ, {"BRICKFLOW_INJECT_TASKS_CONFIG": str(config_file)}
        ):
            project._inject_tasks_from_yaml(workflow)

        # Verify task
        from brickflow.engine.task import SparkPythonTask

        result = workflow.tasks["spark_python_job"].task_func()
        assert isinstance(result, SparkPythonTask)


class TestNotebookBasedInjection:
    """Test direct notebook generation from BRICKFLOW_TASK templates"""

    def test_render_to_notebook_creates_file(self, tmp_path):
        """Test that render_to_notebook creates a .py file with Databricks header"""
        os.chdir(tmp_path)

        template_file = tmp_path / "test_template.py.j2"
        template_file.write_text("print('Hello from {{name}}')")

        task_def = TaskDefinition(
            task_name="test_notebook_task",
            task_type=TaskType.BRICKFLOW_TASK,
            template_file=str(template_file),
        )

        executor = GenericTaskExecutor(task_def)
        notebook_path = executor.render_to_notebook()

        # Verify file was created
        assert notebook_path == "_brickflow_injected_notebooks/test_notebook_task.py"
        notebook_file = tmp_path / notebook_path
        assert notebook_file.exists()
        
        # Verify Databricks notebook header is present
        content = notebook_file.read_text()
        assert content.startswith("# Databricks notebook source\n")
        assert "print('Hello from" in content

    def test_injected_task_has_notebook_path(self, tmp_path):
        """Test that injected BRICKFLOW_TASK has injected_notebook_path set"""
        os.chdir(tmp_path)

        template_file = tmp_path / "compliance_template.py.j2"
        template_file.write_text("print('Compliance check for {{catalog}}')")

        config_file = tmp_path / "injection_config.yaml"
        config_content = f"""
tasks:
  - task_name: compliance_check
    task_type: BRICKFLOW_TASK
    template_file: {template_file}
    template_context:
      catalog: main_catalog
"""
        config_file.write_text(config_content)

        with patch.dict(
            os.environ,
            {"BRICKFLOW_INJECT_TASKS_CONFIG": str(config_file)},
        ):
            project = _Project(
                name="test_project",
                git_repo="https://github.com/test/repo.git",
                provider="github",
                git_reference="main",
            )

            wf = Workflow("test_wf", schedule_quartz_expression="0 0 * * *")
            project.add_workflow(wf)

            # Verify task was injected with notebook path
            assert "compliance_check" in wf.tasks
            task = wf.tasks["compliance_check"]
            assert hasattr(task, "injected_notebook_path")
            assert (
                task.injected_notebook_path
                == "_brickflow_injected_notebooks/compliance_check.py"
            )

    def test_bundle_builder_creates_notebook_task_reference(self, tmp_path):
        """Test that bundle builder creates correct NOTEBOOK_TASK reference"""
        from brickflow.codegen.databricks_bundle import DatabricksBundleCodegen
        from brickflow.engine.task import Task, TaskType
        from brickflow.engine.workflow import Workflow

        os.chdir(tmp_path)

        # Create a workflow with an injected notebook task
        wf = Workflow("test_wf", schedule_quartz_expression="0 0 * * *")

        def dummy_func():
            pass

        task = Task(
            task_id="injected_task",
            task_func=dummy_func,
            workflow=wf,
            task_type=TaskType.BRICKFLOW_TASK,
            injected_notebook_path="_brickflow_injected_notebooks/injected_task.py",
        )

        wf.tasks["injected_task"] = task

        project = _Project(
            name="test_project",
            git_repo="https://github.com/test/repo.git",
            provider="github",
            git_reference="main",
        )
        project.workflows["test_wf"] = wf

        # Build the bundle
        builder = DatabricksBundleCodegen(
            project=project,
            id_="test",
            env="local",
        )

        tasks = builder.workflow_obj_to_tasks(wf)

        # Verify task is built as NOTEBOOK_TASK
        assert len(tasks) == 1
        job_task = tasks[0]
        assert job_task.notebook_task is not None
        assert (
            "${workspace.file_path}/_brickflow_injected_notebooks/injected_task"
            in job_task.notebook_task.notebook_path
        )
        assert job_task.notebook_task.source == "WORKSPACE"

    def test_template_variables_resolved_in_notebook(self, tmp_path):
        """Test that Jinja2 variables are resolved in generated notebook"""
        os.chdir(tmp_path)

        template_file = tmp_path / "param_template.py.j2"
        template_file.write_text("catalog = '{{catalog}}'\nschema = '{{schema}}'")

        task_def = TaskDefinition(
            task_name="param_task",
            task_type=TaskType.BRICKFLOW_TASK,
            template_file=str(template_file),
            template_context={"catalog": "prod_catalog", "schema": "prod_schema"},
        )

        executor = GenericTaskExecutor(task_def)
        notebook_path = executor.render_to_notebook()

        notebook_file = tmp_path / notebook_path
        content = notebook_file.read_text()

        # Verify variables were resolved
        assert "catalog = 'prod_catalog'" in content
        assert "schema = 'prod_schema'" in content
        assert "{{catalog}}" not in content
        assert "{{schema}}" not in content

    def test_service_principal_support_with_workspace_path(self, tmp_path):
        """Test that ${workspace.file_path} works with service principals"""
        from brickflow.codegen.databricks_bundle import DatabricksBundleCodegen
        from brickflow.engine.task import Task, TaskType
        from brickflow.engine.workflow import Workflow

        os.chdir(tmp_path)

        wf = Workflow("test_wf", schedule_quartz_expression="0 0 * * *")

        def dummy_func():
            pass

        task = Task(
            task_id="sp_task",
            task_func=dummy_func,
            workflow=wf,
            task_type=TaskType.BRICKFLOW_TASK,
            injected_notebook_path="_brickflow_injected_notebooks/sp_task.py",
        )

        wf.tasks["sp_task"] = task

        project = _Project(
            name="test_project",
            git_repo="https://github.com/test/repo.git",
            provider="github",
            git_reference="main",
        )
        project.workflows["test_wf"] = wf

        builder = DatabricksBundleCodegen(
            project=project,
            id_="test",
            env="prod",  # Non-local environment (service principal scenario)
        )

        tasks = builder.workflow_obj_to_tasks(wf)

        # Verify ${workspace.file_path} is used (works with service principals)
        job_task = tasks[0]
        assert "${workspace.file_path}" in job_task.notebook_task.notebook_path
        # This variable is resolved by DAB at runtime, working with both
        # user principals and service principals

    def test_sync_config_includes_notebooks_directory(self, tmp_path):
        """Test that bundle includes Sync config for notebooks directory"""
        from brickflow.codegen.databricks_bundle import DatabricksBundleCodegen

        os.chdir(tmp_path)

        project = _Project(
            name="test_project",
            git_repo="https://github.com/test/repo.git",
            provider="github",
            git_reference="branch/main",
            bundle_base_path=str(tmp_path),
            bundle_obj_name="bundles",
        )

        wf = Workflow("test_wf", schedule_quartz_expression="0 0 * * *")
        project.add_workflow(wf)

        builder = DatabricksBundleCodegen(
            project=project,
            id_="test",
            env="dev",
        )

        bundle = builder.proj_to_bundle()

        # Verify Sync configuration exists
        target = bundle.targets[list(bundle.targets.keys())[0]]
        assert target.sync is not None
        assert "_brickflow_injected_notebooks/**" in target.sync.include

    def test_multiple_injected_notebooks(self, tmp_path):
        """Test multiple BRICKFLOW_TASK injections create separate notebooks"""
        os.chdir(tmp_path)

        template1 = tmp_path / "template1.py.j2"
        template1.write_text("print('Task 1')")

        template2 = tmp_path / "template2.py.j2"
        template2.write_text("print('Task 2')")

        config_file = tmp_path / "multi_injection.yaml"
        config_content = f"""
tasks:
  - task_name: task_one
    task_type: BRICKFLOW_TASK
    template_file: {template1}
  - task_name: task_two
    task_type: BRICKFLOW_TASK
    template_file: {template2}
"""
        config_file.write_text(config_content)

        with patch.dict(
            os.environ,
            {"BRICKFLOW_INJECT_TASKS_CONFIG": str(config_file)},
        ):
            project = _Project(
                name="test_project",
                git_repo="https://github.com/test/repo.git",
                provider="github",
                git_reference="main",
            )

            wf = Workflow("test_wf", schedule_quartz_expression="0 0 * * *")
            project.add_workflow(wf)

            # Verify both tasks were injected
            assert "task_one" in wf.tasks
            assert "task_two" in wf.tasks

            # Verify separate notebook paths
            assert (
                wf.tasks["task_one"].injected_notebook_path
                == "_brickflow_injected_notebooks/task_one.py"
            )
            assert (
                wf.tasks["task_two"].injected_notebook_path
                == "_brickflow_injected_notebooks/task_two.py"
            )

            # Verify both files exist
            assert (tmp_path / "_brickflow_injected_notebooks" / "task_one.py").exists()
            assert (tmp_path / "_brickflow_injected_notebooks" / "task_two.py").exists()

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
