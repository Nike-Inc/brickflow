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

from brickflow_plugins._timing.timezone import (
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
    """Human-readable description of the timetable."""

    periodic: bool = True
    """Whether this timetable runs periodically."""

    can_run: bool = True
    """Whether this timetable can actually schedule runs."""

    run_ordering: Sequence[str] = ("data_interval_end", "execution_date")
    """How runs triggered from this timetable should be ordered in UI."""

    @classmethod
    def deserialize(cls, data: dict[str, Any]) -> Timetable:
        """Deserialize a timetable from data."""
        return cls()

    def serialize(self) -> dict[str, Any]:
        """Serialize the timetable for JSON encoding."""
        return {}

    def validate(self) -> None:
        """Validate the timetable is correctly specified."""

    @property
    def summary(self) -> str:
        """A short summary for the timetable."""
        return type(self).__name__


class _DataIntervalTimetable(Timetable):
    """Basis for timetable implementations that schedule data intervals."""

    def _skip_to_latest(self, earliest: DateTime | None) -> DateTime:
        """Bound the earliest time a run can be scheduled."""
        raise NotImplementedError()

    def align_to_next(self, current: DateTime) -> DateTime:
        """Align given time to the next scheduled time."""
        raise NotImplementedError()

    def align_to_prev(self, current: DateTime) -> DateTime:
        """Align given time to the previous scheduled time."""
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
    """

    def _skip_to_latest(self, earliest: DateTime | None) -> DateTime:
        """Bound the earliest time a run can be scheduled."""
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
