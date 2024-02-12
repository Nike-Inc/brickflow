from typing import TYPE_CHECKING

import pluggy

if TYPE_CHECKING:
    from brickflow.engine.task import Task, TaskResponse  # pragma: no cover
    from brickflow.engine.workflow import Workflow  # pragma: no cover

BRICKFLOW_TASK_PLUGINS = "brickflow_task_plugins"

brickflow_plugin_spec = pluggy.HookspecMarker(BRICKFLOW_TASK_PLUGINS)


class BrickflowTaskPluginSpec:
    @staticmethod
    def handle_user_result_errors(resp: "TaskResponse") -> None:
        """Custom execute method that is able to be plugged in."""
        if resp.user_code_error is not None:
            original_message = str(resp.user_code_error)
            additional_info = (
                "BRICKFLOW_USER_OR_DBR_ERROR: This is an error thrown in user code. \n"
                f"BRICKFLOW_INPUT_ARGS: {resp.input_kwargs}\n"
                "Original Exception Message: "
            )
            new_message = additional_info + original_message
            resp.user_code_error.args = (new_message,)
            raise resp.user_code_error

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
