from __future__ import annotations

import functools
import logging
import subprocess
import sys
from typing import Callable, Optional

from brickflow import log, get_default_log_handler


def _call(cmd: str, **kwargs: bool) -> bytes:
    return subprocess.check_output(  # type: ignore
        [
            cmd,
        ],
        **kwargs,
    )


def get_git_remote_url_https() -> Optional[str]:
    git_url = get_git_remote_url()
    if git_url.startswith("https://"):
        return git_url.replace(".git", "")
    if git_url.startswith("git@github.com"):
        return (
            git_url.replace("git@", "https://")
            .replace(".com:", ".com/")
            .replace(".git", "")
        )
    return None


def get_git_remote_url() -> str:
    p = _call("git config --get remote.origin.url", shell=True).decode("utf-8")
    return p.strip()


def is_git_dirty() -> bool:
    p = _call("git diff --stat", shell=True).decode("utf-8")
    if len(p) > 10:
        return True
    return False


def get_current_branch() -> str:
    p = _call("git rev-parse --abbrev-ref HEAD", shell=True)
    return p.strip().decode("utf-8")


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
