from typing import Optional

try:
    from airflow.models import BaseOperator
    from airflow.utils.context import Context
except ImportError:
    raise ImportError(
        "You must install airflow to use airflow plugins, "
        "please try pip install brickflow[apache-airflow]"
    )

from pendulum import DateTime
from brickflow.context import ctx, RETURN_VALUE_KEY
from brickflow_plugins.airflow.cronhelper import cron_helper
from brickflow_plugins.airflow.vendor.timetable import create_timetable
from brickflow_plugins.airflow.vendor.timezone import TIMEZONE


class CrossDagXComsNotSupportedError(Exception):
    pass


class XComsPullMultipleTaskIdsError(Exception):
    pass


class FakeTaskInstance(object):
    def __init__(
        self,
        task_id: str,
        operator: BaseOperator,
        execution_date: str,
    ):
        self._operator = operator
        self._execution_date = execution_date
        self._task_id = task_id

    def xcom_push(self, key, value):
        ctx.task_coms.put(task_id=self._task_id, key=key, value=value)

    def xcom_pull(self, task_ids, key=RETURN_VALUE_KEY, dag_id=None):
        if dag_id is not None:
            raise CrossDagXComsNotSupportedError(
                "Cross dag xcoms not supported in framework raise feature request."
            )
        if isinstance(task_ids, list) and len(task_ids) > 1:
            raise XComsPullMultipleTaskIdsError(
                "Currently xcoms pull only supports one task_id please raise feature "
                "request."
            )
        task_id = task_ids[0] if isinstance(task_ids, list) else task_ids
        return ctx.task_coms.get(task_id, key)

    @property
    def execution_date(self):
        return self._execution_date

    @property
    def operator(self):
        return self._operator


def execution_timestamp(
    quartz_cron_statement: Optional[str] = None,
    ts: Optional[DateTime] = None,
    tz=TIMEZONE,
) -> DateTime:
    if quartz_cron_statement is None:
        return DateTime.utcnow()
    if ts is None:
        ts = DateTime.utcnow()
    cron = cron_helper.quartz_to_unix(quartz_cron_statement)
    tt = create_timetable(cron, tz)
    return tt.align_to_prev(ts)


def get_task_context(
    task_id, operator: BaseOperator, quartz_cron_statement, ts, tz=TIMEZONE
) -> Context:
    execution_ts = execution_timestamp(quartz_cron_statement, ts, tz)
    return Context(
        **{
            "execution_date": str(execution_ts),
            "ds": execution_ts.strftime("%Y-%m-%d"),
            "ds_nodash": execution_ts.strftime("%Y%m%d"),
            "ts": str(execution_ts),
            "ts_nodash": execution_ts.strftime("%Y%m%d%H%M%S"),
            "ti": FakeTaskInstance(task_id, operator, str(execution_ts)),
        }
    )
