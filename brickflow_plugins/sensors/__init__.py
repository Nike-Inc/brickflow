"""
Base sensor class for plugins
"""

# TODO: unify approach for timeouts
# TODO: unify entrypoint method for sensors, e.g. always execute() or always poke()

from abc import abstractmethod
from datetime import datetime
from functools import cached_property
from typing import Optional

import pendulum
from databricks.sdk import WorkspaceClient
from pendulum.tz.timezone import Timezone

from brickflow.context import ctx

# from brickflow_plugins.airflow import execution_timestamp
from brickflow_plugins.airflow.cronhelper import cron_helper
from brickflow_plugins.airflow.vendor.timetable import create_timetable
from brickflow_plugins.airflow.vendor.timezone import TIMEZONE


class Sensor:
    """
    Base class for all sensors in the Databricks plugin.
    Sensors are used to monitor the status of jobs, tasks, or other entities in Databricks.
    """

    def __init__(self):
        self._workspace_obj = WorkspaceClient()

    @staticmethod
    def _get_airflow_execution_timestamp(
        quartz_cron_statement: Optional[str] = None,
        ts: Optional[pendulum.DateTime] = None,
        tz=TIMEZONE,
    ) -> pendulum.DateTime:
        """
        Returns Airflow-style execution timestamp based on the provided Quartz cron statement.
        If no cron statement is provided, it defaults to the current UTC time.
        """
        if quartz_cron_statement is None:
            return pendulum.DateTime.utcnow()
        if ts is None:
            ts = pendulum.DateTime.utcnow()
        cron = cron_helper.quartz_to_unix(quartz_cron_statement)
        tt = create_timetable(cron, tz)
        return tt.align_to_prev(ts)

    @cached_property
    def _execution_timestamp(self) -> pendulum.DateTime:
        """
        Get current run details from Databricks workspace and calculate the Airflow-like
        execution timestamp based on the Quartz cron statement and the start time of the current run.

        Returns:
            pendulum.DateTime: The execution timestamp aligned to the Quartz cron schedule.
        """
        run_id = ctx.dbutils_widget_get_or_else("brickflow_parent_run_id", None)
        if run_id is None:
            raise ValueError(
                "'brickflow_parent_run_id' parameter is not found or no value present, cannot get job run id!"
            )

        run = self._workspace_obj.jobs.get_run(run_id=run_id)
        if run is None:
            raise LookupError(f"Run with id {run_id} not found in the workspace.")

        if run.schedule is None:
            raise ValueError(
                f"Run with id {run_id} does not have a schedule defined, cannot get execution timestamp."
            )

        return self._get_airflow_execution_timestamp(
            quartz_cron_statement=run.schedule.quartz_cron_expression,
            ts=pendulum.instance(
                datetime.fromtimestamp(int(ctx.start_time(debug=None)) / 1000)
            ),
            tz=Timezone(run.schedule.timezone_id),
        )

    @abstractmethod
    def poke(self):
        """
        This method should be overridden by subclasses to implement the specific logic for
        checking the status of the entity being monitored.
        """
        raise NotImplementedError("Subclasses must implement this method.")
