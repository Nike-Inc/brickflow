from __future__ import annotations

import functools
import logging
import subprocess
import sys
from typing import Callable

from brickflow import log, get_default_log_handler


def _call(cmd: str, **kwargs: bool) -> bytes:
    return subprocess.check_output(  # type: ignore
        [
            cmd,
        ],
        **kwargs,
    )


def get_current_commit() -> str:
    p = _call('git log -n 1 --pretty=format:"%H"', shell=True)
    return p.strip().decode("utf-8")


def with_brickflow_logger(f: Callable) -> Callable:
    @functools.wraps(f)
    def func(*args, **kwargs):  # type: ignore
        _self = args[0]
        log.handlers = []
        logger_handler = logging.StreamHandler(
            stream=sys.stdout
        )  # Handler for the logger
        # First, generic formatter:
        logger_handler.setFormatter(
            logging.Formatter(
                f"[%(asctime)s] [%(levelname)s] [brickflow:{_self.name}] "
                "{%(module)s.py:%(funcName)s:%(lineno)d} - %(message)s"
            )
        )
        log.addHandler(logger_handler)
        resp = f(*args, **kwargs)

        log.handlers = [get_default_log_handler()]

        return resp

    return func


ROOT_NODE = "root"
