"""
Base sensor class for plugins
"""

# TODO: unify approach for timeouts
# TODO: unify entrypoint method for sensors, e.g. always execute() or always poke()

from abc import abstractmethod
from datetime import datetime
from functools import cached_property

import pendulum
from pendulum.tz.timezone import Timezone
from databricks.sdk import WorkspaceClient

from brickflow.context import ctx
from brickflow_plugins.airflow import execution_timestamp


class Sensor:
    """
    Base class for all sensors in the Databricks plugin.
    Sensors are used to monitor the status of jobs, tasks, or other entities in Databricks.
    """

    def __init__(self):
        self._workspace_obj = WorkspaceClient()

    @cached_property
    def _execution_timestamp(self) -> pendulum.DateTime:
        """
        Get Airflow-style execution timestamp based on the Quartz cron statement of the workflow
        and the start time of the current run.

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

        return execution_timestamp(
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
