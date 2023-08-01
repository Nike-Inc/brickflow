from __future__ import annotations

import datetime
from functools import cached_property
from typing import Any
from typing import Sequence, Protocol, runtime_checkable

from cron_descriptor import (
    CasingTypeEnum,
    ExpressionDescriptor,
    FormatException,
    MissingFieldException,
)
from croniter import CroniterBadCronError, CroniterBadDateError, croniter
from pendulum import DateTime
from pendulum.tz.timezone import Timezone

from brickflow_plugins.airflow.vendor.timezone import (
    make_naive,
    convert_to_utc,
    make_aware,
)

cron_presets: dict[str, str] = {
    "@hourly": "0 * * * *",
    "@daily": "0 0 * * *",
    "@weekly": "0 0 * * 0",
    "@monthly": "0 0 1 * *",
    "@quarterly": "0 0 1 */3 *",
    "@yearly": "0 0 1 1 *",
}


class TimetableInvalidError(Exception):
    pass


def _is_schedule_fixed(expression: str) -> bool:
    """Figures out if the schedule has a fixed time (e.g. 3 AM every day).

    :return: True if the schedule has a fixed time, False if not.

    Detection is done by "peeking" the next two cron trigger time; if the
    two times have the same minute and hour value, the schedule is fixed,
    and we *don't* need to perform the DST fix.

    This assumes DST happens on whole minute changes (e.g. 12:59 -> 12:00).
    """
    cron = croniter(expression)
    next_a = cron.get_next(datetime.datetime)
    next_b = cron.get_next(datetime.datetime)
    return next_b.minute == next_a.minute and next_b.hour == next_a.hour


class CronMixin:
    """Mixin to provide interface to work with croniter."""

    def __init__(self, cron: str, timezone: str | Timezone) -> None:
        self._expression = cron_presets.get(cron, cron)

        if isinstance(timezone, str):
            timezone = Timezone(timezone)
        self._timezone = timezone

        descriptor = ExpressionDescriptor(
            expression=self._expression,
            casing_type=CasingTypeEnum.Sentence,
            use_24hour_time_format=True,
        )
        try:
            # checking for more than 5 parameters in Cron and avoiding evaluation for now,
            # as Croniter has inconsistent evaluation with other libraries
            if len(croniter(self._expression).expanded) > 5:
                raise FormatException()
            interval_description = descriptor.get_description()
        except (CroniterBadCronError, FormatException, MissingFieldException):
            interval_description = ""
        self.description = interval_description

    def __eq__(self, other: Any) -> bool:
        """Both expression and timezone should match.

        This is only for testing purposes and should not be relied on otherwise.
        """
        if not isinstance(other, type(self)):
            return NotImplemented
        return (
            self._expression == other._expression and self._timezone == other._timezone
        )

    @property
    def summary(self) -> str:
        return self._expression

    def validate(self) -> None:
        try:
            croniter(self._expression)
        except (CroniterBadCronError, CroniterBadDateError) as e:
            raise TimetableInvalidError(str(e))

    @cached_property
    def _should_fix_dst(self) -> bool:
        # This is lazy so instantiating a schedule does not immediately raise
        # an exception. Validity is checked with validate() during DAG-bagging.
        return not _is_schedule_fixed(self._expression)

    def get_next(self, current: DateTime) -> DateTime:
        """Get the first schedule after specified time, with DST fixed."""
        naive = make_naive(current, self._timezone)
        cron = croniter(self._expression, start_time=naive)
        scheduled = cron.get_next(datetime.datetime)
        if not self._should_fix_dst:
            return convert_to_utc(make_aware(scheduled, self._timezone))
        delta = scheduled - naive
        return convert_to_utc(current.in_timezone(self._timezone) + delta)

    def get_prev(self, current: DateTime) -> DateTime:
        """Get the first schedule before specified time, with DST fixed."""
        naive = make_naive(current, self._timezone)
        cron = croniter(self._expression, start_time=naive)
        scheduled = cron.get_prev(datetime.datetime)
        if not self._should_fix_dst:
            return convert_to_utc(make_aware(scheduled, self._timezone))
        delta = naive - scheduled
        return convert_to_utc(current.in_timezone(self._timezone) - delta)

    def align_to_next(self, current: DateTime) -> DateTime:
        """Get the next scheduled time.

        This is ``current + interval``, unless ``current`` falls right on the
        interval boundary, when ``current`` is returned.
        """
        next_time = self.get_next(current)
        if self.get_prev(next_time) != current:
            return next_time
        return current

    def align_to_prev(self, current: DateTime) -> DateTime:
        """Get the prev scheduled time.

        This is ``current - interval``, unless ``current`` falls right on the
        interval boundary, when ``current`` is returned.
        """
        prev_time = self.get_prev(current)
        if self.get_next(prev_time) != current:
            return prev_time
        return current


@runtime_checkable
class Timetable(Protocol):
    """Protocol that all Timetable classes are expected to implement."""

    description: str = ""
    """Human-readable description of the timetable.

    For example, this can produce something like ``'At 21:30, only on Friday'``
    from the cron expression ``'30 21 * * 5'``. This is used in the webserver UI.
    """

    periodic: bool = True
    """Whether this timetable runs periodically.

    This defaults to and should generally be *True*, but some special setups
    like ``schedule=None`` and ``"@once"`` set it to *False*.
    """

    can_run: bool = True
    """Whether this timetable can actually schedule runs.

    This defaults to and should generally be *True*, but ``NullTimetable`` sets
    this to *False*.
    """

    run_ordering: Sequence[str] = ("data_interval_end", "execution_date")
    """How runs triggered from this timetable should be ordered in UI.

    This should be a list of field names on the DAG run object.
    """

    @classmethod
    def deserialize(cls, data: dict[str, Any]) -> Timetable:
        """Deserialize a timetable from data.

        This is called when a serialized DAG is deserialized. ``data`` will be
        whatever was returned by ``serialize`` during DAG serialization. The
        default implementation constructs the timetable without any arguments.
        """
        return cls()

    def serialize(self) -> dict[str, Any]:
        """Serialize the timetable for JSON encoding.

        This is called during DAG serialization to store timetable information
        in the database. This should return a JSON-serializable dict that will
        be fed into ``deserialize`` when the DAG is deserialized. The default
        implementation returns an empty dict.
        """
        return {}

    def validate(self) -> None:
        """Validate the timetable is correctly specified.

        Override this method to provide run-time validation raised when a DAG
        is put into a dagbag. The default implementation does nothing.

        :raises: AirflowTimetableInvalid on validation failure.
        """

    @property
    def summary(self) -> str:
        """A short summary for the timetable.

        This is used to display the timetable in the web UI. A cron expression
        timetable, for example, can use this to display the expression. The
        default implementation returns the timetable's type name.
        """
        return type(self).__name__


class _DataIntervalTimetable(Timetable):
    """Basis for timetable implementations that schedule data intervals.

    This kind of timetable classes create periodic data intervals from an
    underlying schedule representation (e.g. a cron expression, or a timedelta
    instance), and schedule a DagRun at the end of each interval.
    """

    def _skip_to_latest(self, earliest: DateTime | None) -> DateTime:
        """Bound the earliest time a run can be scheduled.

        This is called when ``catchup=False``. See docstring of subclasses for
        exact skipping behaviour of a schedule.
        """
        raise NotImplementedError()

    def align_to_next(self, current: DateTime) -> DateTime:
        """Align given time to the next scheduled time.

        For fixed schedules (e.g. every midnight); this finds the next time that
        aligns to the declared time, if the given time does not align. If the
        schedule is not fixed (e.g. every hour), the given time is returned.
        """
        raise NotImplementedError()

    def align_to_prev(self, current: DateTime) -> DateTime:
        """Align given time to the previous scheduled time.

        For fixed schedules (e.g. every midnight); this finds the prev time that
        aligns to the declared time, if the given time does not align. If the
        schedule is not fixed (e.g. every hour), the given time is returned.

        It is not enough to use ``_get_prev(_align_to_next())``, since when a
        DAG's schedule changes, this alternative would make the first scheduling
        after the schedule change remain the same.
        """
        raise NotImplementedError()

    def get_next(self, current: DateTime) -> DateTime:
        """Get the first schedule after the current time."""
        raise NotImplementedError()

    def get_prev(self, current: DateTime) -> DateTime:
        """Get the last schedule before the current time."""
        raise NotImplementedError()


class CronDataIntervalTimetable(CronMixin, _DataIntervalTimetable):
    """Timetable that schedules data intervals with a cron expression.

    This corresponds to ``schedule=<cron>``, where ``<cron>`` is either
    a five/six-segment representation, or one of ``cron_presets``.

    The implementation extends on croniter to add timezone awareness. This is
    because croniter works only with naive timestamps, and cannot consider DST
    when determining the next/previous time.

    Don't pass ``@once`` in here; use ``OnceTimetable`` instead.
    """

    @classmethod
    def deserialize(cls, data: dict[str, Any]) -> Timetable:
        from airflow.serialization.serialized_objects import decode_timezone

        return cls(data["expression"], decode_timezone(data["timezone"]))

    def serialize(self) -> dict[str, Any]:
        from airflow.serialization.serialized_objects import encode_timezone

        return {
            "expression": self._expression,
            "timezone": encode_timezone(self._timezone),
        }

    def _skip_to_latest(self, earliest: DateTime | None) -> DateTime:
        """Bound the earliest time a run can be scheduled.

        The logic is that we move start_date up until one period before, so the
        current time is AFTER the period end, and the job can be created...

        This is slightly different from the delta version at terminal values.
        If the next schedule should start *right now*, we want the data interval
        that start now, not the one that ends now.
        """
        current_time = DateTime.utcnow()
        last_start = self.get_prev(current_time)
        next_start = self.get_next(last_start)
        if next_start == current_time:  # Current time is on interval boundary.
            new_start = last_start
        elif next_start > current_time:  # Current time is between boundaries.
            new_start = self.get_prev(last_start)
        else:
            raise AssertionError("next schedule shouldn't be earlier")
        if earliest is None:
            return new_start
        return max(new_start, self.align_to_next(earliest))


def create_timetable(interval: str, timezone: Timezone) -> CronDataIntervalTimetable:
    """Create a Timetable instance from a ``schedule_interval`` argument."""
    return CronDataIntervalTimetable(interval, timezone)
