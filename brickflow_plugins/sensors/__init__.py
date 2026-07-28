"""
Base sensor class for brickflow plugins.

Sensors are used to monitor the status of jobs, tasks, or other entities in
Databricks or external systems. This module provides:

- :class:`Sensor`: the abstract base class every sensor plugin should subclass.
- Helpers to derive an Airflow-style ``execution_date`` from the current
  Databricks job run schedule using the pure-python cron/timetable helpers in
  :mod:`brickflow_plugins._timing`.

All logic here is Airflow-free.
"""

from __future__ import annotations

from abc import abstractmethod
from datetime import datetime
from functools import cached_property
from typing import Optional

import pendulum
from databricks.sdk import WorkspaceClient
from pendulum.tz.timezone import Timezone

from brickflow.context import ctx
from brickflow_plugins._timing.cronhelper import cron_helper
from brickflow_plugins._timing.timetable import create_timetable
from brickflow_plugins._timing.timezone import TIMEZONE


class Sensor:
    """
    Base class for all brickflow sensor plugins.

    Subclasses must implement :meth:`poke`. The :attr:`_execution_timestamp`
    helper mimics Airflow's ``execution_date`` by taking the current
    Databricks job run's quartz cron schedule and aligning the run's start
    time to the previous scheduled trigger.
    """

    def __init__(self) -> None:
        self._workspace_obj = WorkspaceClient()

    @staticmethod
    def _get_airflow_execution_timestamp(
        quartz_cron_statement: Optional[str] = None,
        ts: Optional[pendulum.DateTime] = None,
        tz: Timezone = TIMEZONE,
    ) -> pendulum.DateTime:
        """
        Return an Airflow-style execution timestamp for the given Quartz cron
        statement. If no cron statement is provided, defaults to the current
        UTC time.
        """
        if quartz_cron_statement is None:
            return pendulum.DateTime.utcnow()
        if ts is None:
            ts = pendulum.DateTime.utcnow()
        unix_cron = cron_helper.quartz_to_unix(quartz_cron_statement)
        tt = create_timetable(unix_cron, tz)
        return tt.align_to_prev(ts)

    @cached_property
    def _execution_timestamp(self) -> pendulum.DateTime:
        """
        Return the Airflow-style execution timestamp for the current run.

        Reads ``brickflow_parent_run_id`` from the brickflow context, looks
        up the run in the Databricks workspace, and aligns its start time to
        the previous trigger of its quartz schedule.
        """
        run_id = ctx.dbutils_widget_get_or_else("brickflow_parent_run_id", None)
        if run_id is None:
            raise ValueError(
                "'brickflow_parent_run_id' parameter is not found or no value present, "
                "cannot get job run id!"
            )

        run = self._workspace_obj.jobs.get_run(run_id=run_id)
        if run is None:
            raise LookupError(f"Run with id {run_id} not found in the workspace.")

        if run.schedule is None:
            raise ValueError(
                f"Run with id {run_id} does not have a schedule defined, "
                "cannot get execution timestamp."
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
        Subclasses must implement this to check the status of the entity
        being monitored.
        """
        raise NotImplementedError("Subclasses must implement this method.")
