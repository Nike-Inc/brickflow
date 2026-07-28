"""
Tableau Refresh Operators.

Native brickflow operators that refresh Tableau data sources or workbooks
by triggering async refresh jobs and polling the Tableau server until they
complete. No Airflow dependency -- plain Python classes with an
``execute()`` method.
"""

from __future__ import annotations

import concurrent.futures
import time
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, Union

import urllib3

from brickflow_plugins import log

if TYPE_CHECKING:
    import tableauserverclient as TSC  # noqa: F401 -- only for type hints

# Optional third-party tableauserverclient is loaded lazily on first operator
# instantiation. ``TSC`` is bound at module scope so existing references like
# ``TSC.TableauAuth(...)`` and ``TSC.Server(...)`` continue to work unchanged
# once ``_ensure_tableau()`` has been called.
TSC = None  # type: ignore[assignment]


_TABLEAU_INSTALL_HINT = """You must install tableauserverclient library to use Tableau plugins, please add - 'tableauserverclient' 
    library either at project level in entrypoint or at workflow level or at task level.
    
    Entrypoint:
        with Project(
            ... 
            libraries=[PypiTaskLibrary(package="tableauserverclient==0.25")]
            ...
        )
    Workflow:
        wf=Workflow(
            ...
            libraries=[PypiTaskLibrary(package="tableauserverclient==0.25")]
            ...
        )
    Task:
        @wf.task(Library=[PypiTaskLibrary(package="tableauserverclient==0.25")]
        def run_snowflake_queries(*args):
            ...
    """


def _ensure_tableau() -> None:
    """Lazily import tableauserverclient on first use; raise a helpful error
    if missing. Rebinds the module-level ``TSC`` name so all subsequent
    ``TSC.X`` references resolve to the real package. Safe to call multiple
    times -- subsequent calls are a no-op.
    """
    global TSC
    if TSC is not None:
        return
    try:
        import tableauserverclient as _tsc
    except (ImportError, ModuleNotFoundError) as exc:
        raise ModuleNotFoundError(_TABLEAU_INSTALL_HINT) from exc
    TSC = _tsc


# Try the import eagerly so that (a) callers who patch ``TSC.Server`` (etc.)
# by fully-qualified module path continue to work when the extra is installed,
# and (b) users who already have the extra installed see identical behaviour
# to the pre-refactor version. If the extra is missing, the placeholder value
# remains and ``_ensure_tableau()`` will retry (and raise the helpful
# ModuleNotFoundError) at construction time.
try:
    _ensure_tableau()
except ModuleNotFoundError:
    pass


class TableauRefreshException(Exception):
    pass


class TableauRefreshEmptyException(Exception):
    pass


class TableauWrapper:
    """
    Facilitates interaction with a Tableau server for the purpose of
    refreshing data sources or workbooks. Refresh is triggered
    asynchronously, and the Tableau server is polled until every job is
    finished or the ``polling_timeout`` is reached.
    """

    _server: "TSC.Server"
    _authenticator: "TSC.TableauAuth"

    def __init__(
        self,
        server: str,
        username: str,
        password: str,
        site: str,
        project: Optional[str] = None,
        parent_project: Optional[str] = None,
        version: str = "3.14",
        max_async_workers: int = 5,
        polling_required: bool = True,
        polling_interval: int = 30,
        polling_timeout: int = 600,
    ) -> None:
        """
        Parameters
        ----------
        server : str
            Tableau server address, e.g. ``https://tableau-server.com``.
        username : str
            Log in username.
        password : str
            Log in password.
        site : str
            Tableau site.
        project : str
            Tableau project.
        parent_project : str
            Name of the parent Tableau project. Use ``"/"`` for the site root.
        version : str
            Tableau server API version.
        max_async_workers : int
            Maximum number of asynchronous tasks that will trigger jobs and
            wait for completion.
        polling_required : bool
            Wait for job completion to proceed, otherwise trigger the job and
            proceed without waiting.
        polling_interval : int
            Polling interval for the job status updates (seconds).
        polling_timeout : int
            Stop polling if the job was not completed within the specified
            interval (seconds).
        """
        _ensure_tableau()
        self.server = server
        self.version = version
        self.username = username
        self.password = password
        self.site = site
        self.project = project
        self.parent_project = parent_project

        self.max_async_workers = max_async_workers
        self.polling_required = polling_required
        self.polling_interval = polling_interval
        self.polling_timeout = polling_timeout

        self._logger = log
        self._ip = None

    class MultipleWorkingProjectsException(Exception):
        def __init__(self):
            self.message = (
                "Multiple projects with the same name exist on the server! Set "
                "'parent_project' parameter!"
            )
            super().__init__(self.message)

    class UnidentifiedWorkingProjectException(Exception):
        def __init__(self):
            self.message = "Could not identify working project, check that the spelling is correct!"
            super().__init__(self.message)

    def _authenticate(self):
        """Authenticate on the Tableau server."""
        # Suppress 'InsecureRequestWarning'
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self._authenticator = TSC.TableauAuth(self.username, self.password, self.site)
        self._server = TSC.Server(self.server)
        self._server.version = self.version
        self._server.add_http_options({"verify": False})

        return self._server.auth.sign_in(self._authenticator)

    def _get_job_status(self, job_id: str) -> dict:
        """
        Retrieve initial job status from ID and periodically poll the server
        for updates until the status changes or the timeout is reached.

        Finish codes: -1 unknown / not yet started, 0 success, 1 error,
        2 cancelled, -2 timeout.
        """
        finish_code, status = -1, "Unknown"
        response = None
        total_polling_time = 0

        self._logger.debug(f"Retrieving execution status for job '{job_id}'...")
        while finish_code == -1 and self.polling_required is True:
            response = self._server.jobs.get_by_id(job_id)
            finish_code = int(response.finish_code)

            if finish_code == -1:
                time.sleep(self.polling_interval)
                total_polling_time += self.polling_interval

            if total_polling_time == self.polling_timeout:
                self._logger.warning(
                    f"The job '{job_id}' did not complete within expected time, "
                    "exiting... "
                )
                finish_code, status = -2, "Timeout"
                break

        if finish_code == 0:
            status = "Success"
        elif finish_code == 1:
            status = "Error"
        elif finish_code == 2:
            status = "Cancelled"

        self._logger.debug(f"Job '{job_id}' finished with code ({finish_code})...")

        return {
            "job_id": job_id,
            "job_status": status,
            "finish_code": finish_code,
            "started_at": (
                response.started_at.strftime("%Y-%m-%d %H:%M:%S %Z")
                if response and response.started_at
                else None
            ),
            "completed_at": (
                response.completed_at.strftime("%Y-%m-%d %H:%M:%S %Z")
                if response and response.completed_at
                else None
            ),
            "job_status_details": (
                response.notes
                if response and response.notes and finish_code == 1
                else None
            ),
        }

    def _refresh_datasource(self, ds: "TSC.DatasourceItem") -> dict:
        """Trigger refresh of the specific data source and poll for completion."""
        self._logger.info(f"Triggering refresh of '{ds.name}' datasource...")
        response = self._server.datasources.refresh(datasource_item=ds)
        job_status = self._get_job_status(job_id=response.id)
        self._logger.info(f"Data source '{ds.name}' refresh status: {job_status}!")
        return {"data_source": ds.name, **job_status}

    def _refresh_workbook(self, wb: "TSC.WorkbookItem") -> dict:
        """Trigger refresh of the specific workbook and poll for completion."""
        self._logger.info(f"Triggering refresh of '{wb.name}' workbook...")
        response = self._server.workbooks.refresh(workbook_id=wb)
        job_status = self._get_job_status(job_id=response.id)
        self._logger.info(f"Workbook '{wb.name}' refresh status: {job_status}!")
        return {"work_book": wb.name, **job_status}

    def _filter_datasources(self, data_sources: list) -> list:
        """Filter data sources by name and project."""
        all_ds = TSC.Pager(self._server.datasources)

        # Only interact with selected data sources
        lim_ds = [ds for ds in all_ds if ds.name in data_sources]

        working_project = self._get_working_project()
        if working_project:
            lim_ds = [ds for ds in lim_ds if ds.project_id == working_project.id]
        return lim_ds

    def _filter_workbooks(self, work_books: list) -> list:
        """Filter workbooks by name and project."""
        all_wb = TSC.Pager(self._server.workbooks)

        # Only interact with selected work books
        lim_wb = [wb for wb in all_wb if wb.name in work_books]

        working_project = self._get_working_project()
        if working_project:
            lim_wb = [wb for wb in lim_wb if wb.project_id == working_project.id]
        return lim_wb

    def _get_working_project(
        self, project_id: Optional[str] = None
    ) -> Union["TSC.ProjectItem", None]:
        """
        Identify the working project by using ``project`` and (optionally)
        ``parent_project``. If ``project_id`` is provided, it takes precedence.
        """
        if not self.project and not project_id:
            self._logger.warning(
                "Skip working project identification because 'project' parameter of "
                "TableauWrapper was not provided."
            )
            return None

        all_projects = TSC.Pager(self._server.projects)
        parent, lim_p = None, []

        for project in all_projects:
            if project.id == project_id:
                lim_p = [project]
                self._logger.info(
                    f"\nProject ID provided directly:\n\tName: {lim_p[0].name}"
                    f"\n\tID: {lim_p[0].id}"
                )
                break

            # Identify parent project
            if project.name.strip() == self.parent_project and not project_id:
                parent = project
                self._logger.info(
                    f"\nParent project identified:\n\tName: {parent.name}"
                    f"\n\tID: {parent.id}"
                )

            # Identify project(s)
            if project.name.strip() == self.project and not project_id:
                lim_p.append(project)

        if self.parent_project == "/" and not project_id:
            parent = TSC.ProjectItem(name="ROOT")
            self._logger.info("Site root will be treated as parent project.")

        # Further filter the list of projects by parent project id
        if self.parent_project and parent and not project_id:
            lim_p = [
                p
                for p in lim_p
                if (p.parent_id == parent.id)
                or (not p.parent_id and parent.name == "ROOT")
            ]

        if len(lim_p) > 1:
            raise self.MultipleWorkingProjectsException()
        if len(lim_p) == 0:
            raise self.UnidentifiedWorkingProjectException()
        self._logger.info(
            f"\nWorking project identified:\n\tName: {lim_p[0].name}\n\tID: {lim_p[0].id}"
        )
        return lim_p[0]

    def refresh_datasources(self, data_sources: list) -> list:
        """Asynchronously refresh a list of Tableau data sources."""
        with self._authenticate():
            # Only refresh selected data sources
            lim_ds = self._filter_datasources(data_sources=data_sources)

            # Start async execution and collect results
            with concurrent.futures.ThreadPoolExecutor(
                max_workers=self.max_async_workers
            ) as executor:
                executor_results = executor.map(self._refresh_datasource, lim_ds)

                results = [result[1] for result in enumerate(executor_results)]

            return results

    def refresh_workbooks(self, work_books: list) -> list:
        """Asynchronously refresh a list of Tableau workbooks."""
        with self._authenticate():
            # Only refresh selected workbooks
            lim_wb = self._filter_workbooks(work_books=work_books)

            # Start async execution and collect results
            with concurrent.futures.ThreadPoolExecutor(
                max_workers=self.max_async_workers
            ) as executor:
                executor_results = executor.map(self._refresh_workbook, lim_wb)

                results = [result[1] for result in enumerate(executor_results)]

            return results


class TableauRefreshABCOperator(ABC):
    """
    Abstract base class that implements generic functionality for Tableau
    refresh operators. No Airflow inheritance -- plain Python.
    """

    def __init__(
        self,
        server: str,
        username: str,
        password: str,
        site: str,
        project: Optional[str] = None,
        parent_project: Optional[str] = None,
        version: str = "3.14",
        max_async_workers: int = 5,
        polling_required: bool = True,
        polling_interval: int = 30,
        polling_timeout: int = 600,
        fail_operator: bool = True,
    ) -> None:
        _ensure_tableau()
        self._logger = log

        self.wrapper_options = {
            "server": server,
            "username": username,
            "password": password,
            "site": site,
            "project": project,
            "parent_project": parent_project,
            "version": version,
            "max_async_workers": max_async_workers,
            "polling_required": polling_required,
            "polling_interval": polling_interval,
            "polling_timeout": polling_timeout,
        }

        self._logger.info(f"Tableau wrapper options:{self.wrapper_options}")

        self.tableau_wrapper: Optional[TableauWrapper] = None
        self.fail_operator = fail_operator

    def _analyze_refresh_result(self, results: list) -> bool:
        """
        Analyze refresh results returned by the TableauWrapper and raise an
        exception if the operator is configured to fail on error.
        """
        results_bool = [False if r["finish_code"] > 0 else True for r in results]

        if len(results_bool) == 0 and self.fail_operator:
            raise TableauRefreshEmptyException(
                "Nothing was refreshed, check that refreshable object names are "
                "set correctly!"
            )
        if len(results_bool) > 0 and not all(results_bool) and self.fail_operator:
            raise TableauRefreshException(
                f"There was an error during the refresh of Tableau objects:\n{results}"
            )
        return True

    @abstractmethod
    def execute(self):
        raise NotImplementedError


class TableauRefreshDataSourceOperator(TableauRefreshABCOperator):
    """
    Refresh a list of Tableau data sources.

    Example
    -------
    ::

        TableauRefreshDataSourceOperator(
            server="https://tableau.example.com",
            username="me",
            password="pw",
            site="my_site",
            project="my_project",
            data_sources=["ds_a", "ds_b"],
        ).execute()
    """

    def __init__(
        self,
        data_sources: list,
        skip: bool = False,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.data_sources = data_sources
        self._skip = skip

    def execute(self):
        """Refresh data sources in Tableau."""
        if not self._skip:
            self.tableau_wrapper = TableauWrapper(**self.wrapper_options)
            results = self.tableau_wrapper.refresh_datasources(
                data_sources=self.data_sources
            )
            self._analyze_refresh_result(results)
        else:
            self._logger.info("Skipping task execution...")


class TableauRefreshWorkBookOperator(TableauRefreshABCOperator):
    """
    Refresh a list of Tableau workbooks.

    Example
    -------
    ::

        TableauRefreshWorkBookOperator(
            server="https://tableau.example.com",
            username="me",
            password="pw",
            site="my_site",
            project="my_project",
            workbooks=["wb_a", "wb_b"],
        ).execute()
    """

    def __init__(
        self,
        workbooks: list,
        skip: bool = False,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.workbooks = workbooks
        self._skip = skip

    def execute(self):
        """Refresh workbooks in Tableau."""
        if not self._skip:
            self.tableau_wrapper = TableauWrapper(**self.wrapper_options)
            results = self.tableau_wrapper.refresh_workbooks(work_books=self.workbooks)
            self._analyze_refresh_result(results)
        else:
            self._logger.info("Skipping task execution...")
