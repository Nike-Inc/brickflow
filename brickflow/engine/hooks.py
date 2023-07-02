from typing import TYPE_CHECKING

import pluggy

if TYPE_CHECKING:
    from brickflow.engine.task import Task, TaskResponse  # pragma: no cover
    from brickflow.engine.workflow import Workflow  # pragma: no cover

BRICKFLOW_TASK_PLUGINS = "brickflow_task_plugins"

brickflow_plugin_spec = pluggy.HookspecMarker(BRICKFLOW_TASK_PLUGINS)


class BrickflowTaskPluginSpec:
    @staticmethod
    @brickflow_plugin_spec(firstresult=True)
    def task_execute(task: "Task", workflow: "Workflow") -> "TaskResponse":
        """Custom execute method that is able to be plugged in."""
        raise NotImplementedError("task_execute must be implemented by a plugin")

    @staticmethod
    @brickflow_plugin_spec(firstresult=True)
    def handle_results(
        resp: "TaskResponse", task: "Task", workflow: "Workflow"
    ) -> "TaskResponse":
        """Custom execute method that is able to be plugged in."""
        raise NotImplementedError("handle_results must be implemented by a plugin")
