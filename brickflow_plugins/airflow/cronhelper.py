import re
import functools

from brickflow_plugins import log


class CronHelper:
    EVERY_X_UNITS_REPLACE_PLACEHOLDER = "%s"
    QUARTZ_EVERY_X_UNITS_REGEX = re.compile(r"^0/(\d+)$")  # For handling 0/5 units
    UNIX_EVERY_X_UNITS_REGEX = re.compile(r"^\*/(\d+)$")  # For handling */5 units
    QUARTZ_EVERY_X_UNITS_REPLACE_PATTERN = f"0/{EVERY_X_UNITS_REPLACE_PLACEHOLDER}"
    UNIX_EVERY_X_UNITS_REPLACE_PATTERN = f"*/{EVERY_X_UNITS_REPLACE_PLACEHOLDER}"

    @staticmethod
    def __get_expression_parts(expression: str) -> list:
        parts = [part.strip() for part in expression.split(" ")]

        # Unix cron expression have 5 parts, Quartz cron expression have 6 or 7 parts
        if len(parts) in [5, 7]:
            return parts
        # Year is an optional part in Quartz cron expression, adding the extra element to mimic 7 part Quartz expression
        if len(parts) == 6:
            parts.append("*")
            return parts

        raise ValueError("Invalid cron expression!")

    @staticmethod
    def convert_interval_parts(part: str, is_quartz: bool = False) -> str:
        every_x_units_pattern = (
            CronHelper.QUARTZ_EVERY_X_UNITS_REGEX
            if is_quartz
            else CronHelper.UNIX_EVERY_X_UNITS_REGEX
        )
        matches = every_x_units_pattern.match(part)
        every_x_units_replace_pattern = (
            CronHelper.QUARTZ_EVERY_X_UNITS_REPLACE_PATTERN
            if is_quartz
            else CronHelper.UNIX_EVERY_X_UNITS_REPLACE_PATTERN
        )

        if matches:
            return every_x_units_replace_pattern.replace(
                CronHelper.EVERY_X_UNITS_REPLACE_PLACEHOLDER, matches.group(1)
            )

        return part

    @functools.lru_cache(maxsize=128)  # cron expression conversion will not change
    def unix_to_quartz(self, unix_cron: str) -> str:
        parts = self.__get_expression_parts(expression=unix_cron)

        if len(parts) != 5:
            raise ValueError("Invalid Unix cron expression")

        minute, hour, dom, month, dow = map(self.convert_interval_parts, parts)

        # Converting Unix DOW to Quartz DOW
        def shift_days(day: str) -> str:
            """
            Quartz DOW starts from 1 (Sunday) while Unix DOW starts from 0 (Sunday)
            """
            if "-" in day:
                return "-".join([shift_days(day=d) for d in day.split("-")])

            # Unix cron Sunday can be represented as 0 or 7, but only as 1 in Quartz cron
            if day in ["0", "7"]:
                return "1"
            if day in ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]:
                return day
            return str(int(day) + 1)

        if "," in dow:
            quartz_dow = ",".join([shift_days(day=day) for day in dow.split(",")])
        elif dow == "*":
            quartz_dow = dow
        else:
            quartz_dow = shift_days(day=dow)

        quartz_dom = dom

        if dom != "*" and dow == "*":
            quartz_dow = "?"
        elif dom == "*":
            quartz_dom = "?"

        quartz_cron = f"0 {minute} {hour} {quartz_dom} {month} {quartz_dow} *"
        log.info("Converted unix cron %s to quartz cron %s", unix_cron, quartz_cron)
        return quartz_cron

    @functools.lru_cache(maxsize=128)  # cron expression conversion will not change
    def quartz_to_unix(self, quartz_cron: str) -> str:
        parts = self.__get_expression_parts(expression=quartz_cron)

        if len(parts) != 7:
            raise ValueError("Invalid Quartz cron expression")

        if "L" in quartz_cron or "W" in quartz_cron or "#" in quartz_cron:
            raise ValueError("Support for 'L, W, #' in Quartz cron is not implemented")

        # Unix cron expression does not support '?'
        parts = [part.replace("?", "*") for part in parts]

        _, minute, hour, dom, month, dow, _ = map(
            lambda part: self.convert_interval_parts(part, True), parts
        )

        # Converting Quartz DOW to Unix DOW
        def shift_days(day: str) -> str:
            """
            Quartz DOW starts from 1 (Sunday) while Unix DOW starts from 0 (Sunday)
            """
            if "-" in day:
                return "-".join([shift_days(day=d) for d in day.split("-")])
            if day in ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]:
                return day

            return str(int(day) - 1)

        if "," in dow:
            unix_dow = ",".join([shift_days(day=day) for day in dow.split(",")])
        elif dow == "*":
            unix_dow = "*"
        else:
            unix_dow = shift_days(day=dow)

        unix_dom = dom

        unix_cron = f"{minute} {hour} {unix_dom} {month} {unix_dow}"
        log.info("Converted quartz cron %s to unix cron %s", quartz_cron, unix_cron)
        return unix_cron


cron_helper = CronHelper()
