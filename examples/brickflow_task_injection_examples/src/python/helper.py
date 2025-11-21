"""
Helper utilities for the demo workflow.

These utilities can be used by both the main workflow tasks
and the injected tasks.
"""

import datetime
import logging
from typing import Dict, Any


def get_timestamp() -> str:
    """Get current timestamp in ISO format."""
    return datetime.datetime.now().isoformat()


def format_task_result(task_name: str, status: str, **kwargs: Any) -> Dict[str, Any]:
    """
    Format a task result dictionary.

    Args:
        task_name: Name of the task
        status: Status of the task (e.g., 'success', 'failed')
        **kwargs: Additional key-value pairs to include

    Returns:
        Formatted result dictionary
    """
    result = {
        "task": task_name,
        "status": status,
        "timestamp": get_timestamp(),
    }
    result.update(kwargs)
    return result


def log_task_start(task_name: str, logger: logging.Logger = None) -> None:
    """
    Log the start of a task with formatted output.

    Args:
        task_name: Name of the task
        logger: Logger instance (creates new one if not provided)
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    logger.info("=" * 70)
    logger.info(f"Starting Task: {task_name}")
    logger.info(f"Timestamp: {get_timestamp()}")
    logger.info("=" * 70)


def log_task_end(
    task_name: str, status: str = "success", logger: logging.Logger = None
) -> None:
    """
    Log the end of a task with formatted output.

    Args:
        task_name: Name of the task
        status: Status of the task
        logger: Logger instance (creates new one if not provided)
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    logger.info("=" * 70)
    logger.info(f"Task Completed: {task_name}")
    logger.info(f"Status: {status}")
    logger.info(f"Timestamp: {get_timestamp()}")
    logger.info("=" * 70)


def validate_config(config: Dict[str, Any], required_keys: list) -> bool:
    """
    Validate that a configuration dictionary has all required keys.

    Args:
        config: Configuration dictionary to validate
        required_keys: List of required keys

    Returns:
        True if all keys present, False otherwise
    """
    missing_keys = [key for key in required_keys if key not in config]

    if missing_keys:
        logging.error(f"Missing required configuration keys: {missing_keys}")
        return False

    return True


# Example usage in injected tasks:
# from src.python.helper import get_timestamp, format_task_result, log_task_start
