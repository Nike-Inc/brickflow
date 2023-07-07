from __future__ import annotations

from enum import Enum

from decouple import config

from brickflow import BrickflowEnvVars


class BrickflowDeployMode(Enum):
    CDKTF = "cdktf"
    BUNDLE = "bundle"


INTERACTIVE_MODE = config(
    BrickflowEnvVars.BRICKFLOW_INTERACTIVE_MODE.value, default=True, cast=bool
)
