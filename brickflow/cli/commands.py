from __future__ import annotations

import os
import subprocess
from typing import Optional, Union, Tuple, List

from click import ClickException

from brickflow import _ilog


def exec_command(
    path_to_executable: str,
    base_command: Optional[str],
    args: Union[Tuple[str] | List[str]],
    capture_output: bool = False,
) -> Optional[str]:
    os.environ["PYTHONPATH"] = os.getcwd()
    my_env = os.environ.copy()
    try:
        _args = list(args)
        # add a base command if its provided for proxying for brickflow deploy
        if base_command is not None:
            _args = [base_command] + _args
        _ilog.info("Executing command: %s", " ".join([path_to_executable, *_args]))

        if capture_output is True:
            res = subprocess.run(
                [path_to_executable, *_args],
                check=True,
                env=my_env,
                capture_output=True,
                text=True,
            )
            return res.stdout.strip()

        subprocess.run([path_to_executable, *_args], check=True, env=my_env)
    except subprocess.CalledProcessError as e:
        raise ClickException(str(e))

    return None
