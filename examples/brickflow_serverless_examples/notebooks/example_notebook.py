# Databricks notebook source
# MAGIC %pip install pytz==2024.2

# COMMAND ----------
import pytz
from datetime import datetime


def get_current_time_in_timezone(timezone_str):
    # Get the timezone object
    timezone = pytz.timezone(timezone_str)
    # Get the current time in the specified timezone
    current_time = datetime.now(timezone)
    return current_time


# Example usage
timezones = ["UTC", "Europe/Amsterdam", "Asia/Tokyo", "America/New_York"]
for tz in timezones:
    print(f"Current time in {tz}: {get_current_time_in_timezone(tz)}")
