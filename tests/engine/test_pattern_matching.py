"""
Tests for pattern matching in task dependencies.

Following TDD - these tests will fail initially until we implement the feature.
"""

import pytest

from brickflow import Workflow
from brickflow.engine.compute import Cluster


class TestPatternMatchingBasic:
    """Test basic pattern matching functionality."""

    def test_single_wildcard_matches_multiple_tasks(self):
        """Test that * wildcard matches multiple tasks."""
        wf = Workflow(
            "test_wf",
            default_cluster=Cluster(
                name="test_cluster",
                spark_version="13.3.x-scala2.12",
                node_type_id="m5.large",
            ),
        )

        # Define tasks to match
        @wf.task()
        def transform_source_a():
            pass

        @wf.task()
        def transform_source_b():
            pass

        @wf.task()
        def transform_source_c():
            pass

        # Task with pattern dependency
        @wf.task(depends_on="transform_*")
        def aggregate_task():
            pass

        # Verify pattern resolved to all three transform tasks
        agg_task = wf.get_task("aggregate_task")
        assert len(agg_task.depends_on) == 3
        assert "transform_source_a" in agg_task.depends_on
        assert "transform_source_b" in agg_task.depends_on
        assert "transform_source_c" in agg_task.depends_on

    def test_pattern_matches_single_task(self):
        """Test that pattern works when matching only one task."""
        wf = Workflow(
            "test_wf",
            default_cluster=Cluster(
                name="test_cluster",
                spark_version="13.3.x-scala2.12",
                node_type_id="m5.large",
            ),
        )

        @wf.task()
        def unique_task():
            pass

        @wf.task(depends_on="unique_*")
        def dependent_task():
            pass

        dep_task = wf.get_task("dependent_task")
        assert dep_task.depends_on == ["unique_task"]

    def test_question_mark_wildcard(self):
        """Test that ? wildcard matches single character."""
        wf = Workflow(
            "test_wf",
            default_cluster=Cluster(
                name="test_cluster",
                spark_version="13.3.x-scala2.12",
                node_type_id="m5.large",
            ),
        )

        @wf.task()
        def task_a():
            pass

        @wf.task()
        def task_b():
            pass

        @wf.task()
        def task_ab():  # Should not match
            pass

        @wf.task(depends_on="task_?")
        def dependent_task():
            pass

        dep_task = wf.get_task("dependent_task")
        assert len(dep_task.depends_on) == 2
        assert "task_a" in dep_task.depends_on
        assert "task_b" in dep_task.depends_on
        assert "task_ab" not in dep_task.depends_on

    def test_character_set_wildcard(self):
        """Test that [abc] character set works."""
        wf = Workflow(
            "test_wf",
            default_cluster=Cluster(
                name="test_cluster",
                spark_version="13.3.x-scala2.12",
                node_type_id="m5.large",
            ),
        )

        @wf.task()
        def process_a_data():
            pass

        @wf.task()
        def process_b_data():
            pass

        @wf.task()
        def process_c_data():
            pass

        @wf.task()
        def process_d_data():  # Should not match
            pass

        @wf.task(depends_on="process_[abc]_data")
        def aggregate_abc():
            pass

        agg_task = wf.get_task("aggregate_abc")
        assert len(agg_task.depends_on) == 3
        assert "process_a_data" in agg_task.depends_on
        assert "process_b_data" in agg_task.depends_on
        assert "process_c_data" in agg_task.depends_on
        assert "process_d_data" not in agg_task.depends_on


class TestPatternMatchingMultiple:
    """Test multiple patterns and mixed dependencies."""

    def test_multiple_patterns_in_list(self):
        """Test that multiple patterns can be specified in a list."""
        wf = Workflow(
            "test_wf",
            default_cluster=Cluster(
                name="test_cluster",
                spark_version="13.3.x-scala2.12",
                node_type_id="m5.large",
            ),
        )

        @wf.task()
        def extract_source_a():
            pass

        @wf.task()
        def transform_source_a():
            pass

        @wf.task(depends_on=["extract_*", "transform_*"])
        def load_task():
            pass

        load = wf.get_task("load_task")
        assert len(load.depends_on) == 2
        assert "extract_source_a" in load.depends_on
        assert "transform_source_a" in load.depends_on

    def test_mixed_pattern_and_explicit_dependencies(self):
        """Test mixing patterns with explicit task references."""
        wf = Workflow(
            "test_wf",
            default_cluster=Cluster(
                name="test_cluster",
                spark_version="13.3.x-scala2.12",
                node_type_id="m5.large",
            ),
        )

        @wf.task()
        def init_task():
            pass

        @wf.task()
        def transform_a():
            pass

        @wf.task()
        def transform_b():
            pass

        @wf.task(depends_on=["init_task", "transform_*"])
        def final_task():
            pass

        final = wf.get_task("final_task")
        assert len(final.depends_on) == 3
        assert "init_task" in final.depends_on
        assert "transform_a" in final.depends_on
        assert "transform_b" in final.depends_on

    def test_mixed_pattern_and_callable_dependencies(self):
        """Test mixing patterns with callable task references."""
        wf = Workflow(
            "test_wf",
            default_cluster=Cluster(
                name="test_cluster",
                spark_version="13.3.x-scala2.12",
                node_type_id="m5.large",
            ),
        )

        @wf.task()
        def setup_task():
            pass

        @wf.task()
        def process_a():
            pass

        @wf.task()
        def process_b():
            pass

        @wf.task(depends_on=[setup_task, "process_*"])
        def cleanup_task():
            pass

        cleanup = wf.get_task("cleanup_task")
        assert len(cleanup.depends_on) == 3
        # Callable should be preserved as callable
        assert setup_task in cleanup.depends_on
        assert "process_a" in cleanup.depends_on
        assert "process_b" in cleanup.depends_on


class TestPatternMatchingEdgeCases:
    """Test edge cases and error conditions."""

    def test_pattern_matches_zero_tasks_raises_error(self):
        """Test that pattern matching zero tasks raises a clear error."""
        wf = Workflow(
            "test_wf",
            default_cluster=Cluster(
                name="test_cluster",
                spark_version="13.3.x-scala2.12",
                node_type_id="m5.large",
            ),
        )

        @wf.task()
        def some_task():
            pass

        with pytest.raises(ValueError) as exc_info:

            @wf.task(depends_on="nonexistent_*")
            def failing_task():
                pass

        error_msg = str(exc_info.value)
        assert "nonexistent_*" in error_msg
        assert "did not match any tasks" in error_msg.lower()

    def test_exact_string_match_still_works(self):
        """Test that exact string matches (no wildcards) still work."""
        wf = Workflow(
            "test_wf",
            default_cluster=Cluster(
                name="test_cluster",
                spark_version="13.3.x-scala2.12",
                node_type_id="m5.large",
            ),
        )

        @wf.task()
        def task_a():
            pass

        @wf.task(depends_on="task_a")
        def task_b():
            pass

        task_b_obj = wf.get_task("task_b")
        assert task_b_obj.depends_on == ["task_a"]

    def test_callable_dependencies_still_work(self):
        """Test that callable dependencies (no change) still work."""
        wf = Workflow(
            "test_wf",
            default_cluster=Cluster(
                name="test_cluster",
                spark_version="13.3.x-scala2.12",
                node_type_id="m5.large",
            ),
        )

        @wf.task()
        def task_a():
            pass

        @wf.task(depends_on=task_a)
        def task_b():
            pass

        task_b_obj = wf.get_task("task_b")
        assert task_a in task_b_obj.depends_on

    def test_pattern_does_not_match_itself(self):
        """Test that a pattern doesn't match the task it's defined on."""
        wf = Workflow(
            "test_wf",
            default_cluster=Cluster(
                name="test_cluster",
                spark_version="13.3.x-scala2.12",
                node_type_id="m5.large",
            ),
        )

        @wf.task()
        def process_a():
            pass

        @wf.task(depends_on="process_*")
        def process_b():  # Starts with "process_" but shouldn't match itself
            pass

        task_b_obj = wf.get_task("process_b")
        assert "process_a" in task_b_obj.depends_on
        assert "process_b" not in task_b_obj.depends_on

    def test_wildcard_only_pattern_matches_all(self):
        """Test that pure wildcard patterns work correctly."""
        wf = Workflow(
            "test_wf",
            default_cluster=Cluster(
                name="test_cluster",
                spark_version="13.3.x-scala2.12",
                node_type_id="m5.large",
            ),
        )

        @wf.task()
        def task_a():
            pass

        @wf.task()
        def task_b():
            pass

        # Pattern "*" should match all existing tasks
        @wf.task(depends_on="task_*")
        def aggregate_all():
            pass

        agg_task = wf.get_task("aggregate_all")
        assert len(agg_task.depends_on) == 2
        assert "task_a" in agg_task.depends_on
        assert "task_b" in agg_task.depends_on

    def test_pattern_with_no_wildcards_is_exact_match(self):
        """Test that a pattern with no wildcard characters is an exact match."""
        wf = Workflow(
            "test_wf",
            default_cluster=Cluster(
                name="test_cluster",
                spark_version="13.3.x-scala2.12",
                node_type_id="m5.large",
            ),
        )

        @wf.task()
        def exact_task_name():
            pass

        @wf.task(depends_on="exact_task_name")
        def dependent():
            pass

        dep_task = wf.get_task("dependent")
        assert dep_task.depends_on == ["exact_task_name"]


class TestPatternMatchingComplexScenarios:
    """Test complex real-world scenarios."""

    def test_fanout_fanin_pattern(self):
        """Test fan-out/fan-in pattern with multiple stages."""
        wf = Workflow(
            "test_wf",
            default_cluster=Cluster(
                name="test_cluster",
                spark_version="13.3.x-scala2.12",
                node_type_id="m5.large",
            ),
        )

        # Setup
        @wf.task()
        def init():
            pass

        # Fan-out: Multiple extract tasks
        @wf.task(depends_on=init)
        def extract_a():
            pass

        @wf.task(depends_on=init)
        def extract_b():
            pass

        @wf.task(depends_on=init)
        def extract_c():
            pass

        # Fan-in: Aggregate using pattern
        @wf.task(depends_on="extract_*")
        def aggregate():
            pass

        agg_task = wf.get_task("aggregate")
        assert len(agg_task.depends_on) == 3
        assert all(
            dep in agg_task.depends_on
            for dep in ["extract_a", "extract_b", "extract_c"]
        )

    def test_multiple_pattern_stages(self):
        """Test workflow with multiple stages using patterns."""
        wf = Workflow(
            "test_wf",
            default_cluster=Cluster(
                name="test_cluster",
                spark_version="13.3.x-scala2.12",
                node_type_id="m5.large",
            ),
        )

        # Stage 1: Extract
        @wf.task()
        def extract_source_a():
            pass

        @wf.task()
        def extract_source_b():
            pass

        # Stage 2: Transform (depends on extract pattern)
        @wf.task(depends_on="extract_*")
        def transform_data():
            pass

        # Stage 3: Load (depends on transform)
        @wf.task(depends_on=transform_data)
        def load_data():
            pass

        transform_task = wf.get_task("transform_data")
        assert len(transform_task.depends_on) == 2
        assert "extract_source_a" in transform_task.depends_on
        assert "extract_source_b" in transform_task.depends_on

        load_task = wf.get_task("load_data")
        assert transform_data in load_task.depends_on
