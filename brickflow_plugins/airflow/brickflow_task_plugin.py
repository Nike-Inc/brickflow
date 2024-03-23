from typing import Optional
import datetime
import pendulum

try:
    from airflow import macros
    from airflow.models import BaseOperator
    from airflow.utils.context import Context
except ImportError:
    raise ImportError(
        "You must install airflow to use airflow plugins, "
        "please try pip install brickflow[apache-airflow]"
    )

from jinja2 import Environment
from brickflow.context import ctx
from brickflow.engine.hooks import BrickflowTaskPluginSpec
from brickflow.engine.task import brickflow_task_plugin_impl, Task, TaskResponse
from brickflow.engine.workflow import Workflow

from brickflow_plugins import log
from brickflow_plugins.airflow.context import get_task_context
from brickflow_plugins.airflow.operators import get_modifier_chain
from brickflow_plugins.secrets import BrickflowSecretsBackend


def epoch_to_pendulum_datetime(epoch_str: Optional[str]):
    if epoch_str is None:
        return None
    return pendulum.instance(datetime.datetime.fromtimestamp(int(epoch_str) / 1000))


class AirflowOperatorBrickflowTaskPluginImpl(BrickflowTaskPluginSpec):
    @staticmethod
    @brickflow_task_plugin_impl(tryfirst=True)
    def handle_results(
        resp: "TaskResponse", task: "Task", workflow: "Workflow"
    ) -> "TaskResponse":
        log.info(
            "using AirflowOperatorBrickflowTaskPlugin for handling results for task: %s",
            task.task_id,
        )

        BrickflowTaskPluginSpec.handle_user_result_errors(resp)

        _operator = resp.response

        if not isinstance(_operator, BaseOperator):
            return resp

        operator_modifier_chain = get_modifier_chain()
        # modify any functionality of operators and then
        _operator = operator_modifier_chain.modify(_operator, task, workflow)

        if hasattr(_operator, "log"):
            # overwrite the operator logger if it has one to the brickflow logger
            setattr(_operator, "_log", ctx.log)

        context: Context = get_task_context(
            task.task_id,
            _operator,
            workflow.schedule_quartz_expression,
            epoch_to_pendulum_datetime(ctx.start_time(debug=None)),
            tz=workflow.timezone,
        )

        env: Optional[Environment] = Environment()
        env.globals.update({"macros": macros, "ti": context})
        with BrickflowSecretsBackend():
            _operator.render_template_fields(context, jinja_env=env)
            op_resp = _operator.execute(context)
            return TaskResponse(
                response=op_resp,
                push_return_value=_operator.do_xcom_push,
            )
