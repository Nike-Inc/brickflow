import functools
from typing import Callable, Type, List, Iterator, Union
import pathlib
import os

from pydantic import SecretStr
from databricks.sdk import WorkspaceClient

from brickflow.context import ctx
from brickflow.hints import propagate_hint


@propagate_hint
def wraps_keyerror(error_class: Type[Exception], msg: str) -> Callable:
    def wrapper(f: Callable) -> Callable:
        @functools.wraps(f)
        def func(*args, **kwargs):  # type: ignore
            try:
                return f(*args, **kwargs)
            except KeyError as e:
                raise error_class(
                    f"{msg}; err: {str(e)}; args: {args}; kwargs: {kwargs}"
                )

        return func

    return wrapper


def get_properties(some_obj: Type) -> List[str]:
    def _property_iter() -> Iterator[str]:
        for k, v in some_obj.__dict__.items():
            if isinstance(v, property):
                yield k

    return list(_property_iter())


def get_job_id(
    job_name: str, host: Union[str, None] = None, token: Union[str, SecretStr] = None
) -> Union[float, None]:
    """
    Get the job id from the specified Databricks workspace for a given job name.

    Parameters
    ----------
    job_name: str
        Job name (case-insensitive)
    host: str
        Databricks workspace URL
    token: str
        Databricks API token

    Returns
    -------
    str
        Databricks job id
    """
    ctx.log.info("Searching job id for job name: %s", job_name)

    if host:
        host = host.rstrip("/")
    token = token.get_secret_value() if isinstance(token, SecretStr) else token

    workspace_obj = WorkspaceClient(host=host, token=token)
    jobs_list = workspace_obj.jobs.list(name=job_name)

    try:
        for job in jobs_list:
            ctx.log.info("Job id for job '%s' is %s", job_name, job.job_id)
            return job.job_id
        else:  # pylint: disable=useless-else-on-loop
            raise ValueError
    except ValueError:
        raise ValueError(f"No job found with name {job_name}")
    except Exception as e:
        ctx.log.info("An error occurred: %s", e)

    return None


def get_bf_project_root() -> pathlib.Path:
    """Returns the root directory of the current Brickflow project

    Parameters:
        _file (str): file path where the function is called

    Returns:
        pathlib.Path: Brickflow project root directory
    """
    try:
        _file_name = os.getcwd()
        _project_root = pathlib.Path(_file_name).resolve().parents[0]
        ctx.log.info("Setting Brickflow project root as %s", _project_root)
        return _project_root
    except Exception as e:
        ctx.log.info("An error occurred: %s", e)
        raise e
