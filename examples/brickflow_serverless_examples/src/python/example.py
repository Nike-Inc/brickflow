import pytz
from datetime import datetime
import argparse


def get_current_time_in_timezone(timezone_str):
    # Get the timezone object
    timezone = pytz.timezone(timezone_str)
    # Get the current time in the specified timezone
    current_time = datetime.now(timezone)
    return current_time


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get the current time in a specified timezone."
    )
    parser.add_argument(
        "--timezone",
        type=str,
        required=True,
        help="The timezone to get the current time for.",
    )
    args = parser.parse_args()

    try:
        current_time = get_current_time_in_timezone(args.timezone)
        print(f"Current time in {args.timezone}: {current_time}")
    except pytz.UnknownTimeZoneError:
        print(f"Unknown timezone: {args.timezone}")
