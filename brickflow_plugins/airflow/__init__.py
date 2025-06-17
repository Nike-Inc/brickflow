from typing import Optional
from pendulum import DateTime

from brickflow_plugins.airflow.cronhelper import cron_helper
from brickflow_plugins.airflow.vendor.timetable import create_timetable
from brickflow_plugins.airflow.vendor.timezone import TIMEZONE


def execution_timestamp(
    quartz_cron_statement: Optional[str] = None,
    ts: Optional[DateTime] = None,
    tz=TIMEZONE,
) -> DateTime:
    """
    Returns Airflow-style execution timestamp based on the provided Quartz cron statement.
    If no cron statement is provided, it defaults to the current UTC time.
    """
    if quartz_cron_statement is None:
        return DateTime.utcnow()
    if ts is None:
        ts = DateTime.utcnow()
    cron = cron_helper.quartz_to_unix(quartz_cron_statement)
    tt = create_timetable(cron, tz)
    return tt.align_to_prev(ts)
