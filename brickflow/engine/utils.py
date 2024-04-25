import functools
from typing import Callable, Type, List, Iterator, Union

import requests
from pydantic import SecretStr

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
    job_name: str, workspace_url: str, api_token: Union[str, SecretStr]
) -> Union[str, None]:
    """
    Get the job id from the specified Databricks workspace for a given job name.

    Parameters
    ----------
    job_name: str
        Job name (case-insensitive)
    workspace_url: str
        Databricks workspace URL
    api_token: str
        Databricks API token
    Returns
    -------
    str
        Databricks job id
    """
    ctx.log.info("Searching job id for job name: %s", job_name)

    api_token = (
        api_token.get_secret_value() if isinstance(api_token, SecretStr) else api_token
    )

    workspace_url = workspace_url.rstrip("/")
    response = requests.get(
        url=f"{workspace_url}/api/2.1/jobs/list",
        headers={"Authorization": f"Bearer {api_token}"},
        params={"name": job_name},
        timeout=10,
    )

    data = response.json()
    if response.status_code == 200:
        if "jobs" in data:
            job_id = data["jobs"][0].get("job_id")
            ctx.log.info("Job id for job '%s' is %s", job_name, job_id)
            return job_id
        else:
            raise ValueError(f"No job found with name '{job_name}'")
    else:
        ctx.log.info(
            "Request returned a %s code, with data '%s'", response.status_code, data
        )
        return None
