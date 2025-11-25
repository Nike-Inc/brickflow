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


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
