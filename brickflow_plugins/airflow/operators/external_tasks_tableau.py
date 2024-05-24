import concurrent.futures
import time
from abc import abstractmethod
from typing import Union

import urllib3
from airflow.operators.python import BaseOperator

from brickflow_plugins import log

try:
    import tableauserverclient as TSC
except (ImportError, ModuleNotFoundError):
    raise ModuleNotFoundError(
        """You must install tableauserverclient library to use Tableau plugins, please add - 'tableauserverclient' 
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
    )


class TableauWrapper:
    """
    Class facilitates interaction with Tableau server for the purpose of refreshing
    data sources or work books.
    Refresh is triggered asynchronously, and Tableau server is polled for results for each job,
    until the job is finished or timeout is reached (default: 10 minutes).
    """

    _server: TSC.Server
    _authenticator: TSC.TableauAuth

    def __init__(
        self,
        server: str,
        username: str,
        password: str,
        site: str,
        project: str = None,
        parent_project: str = None,
        version: str = "3.14",
        max_async_workers: int = 5,
        polling_required: bool = True,
        polling_interval: int = 30,
        polling_timeout: int = 600,
    ):
        """
        Initialize TableauWrapper object with the specified parameters.

        Parameters
        ----------
        server : str
            Tableau server address, e.g. https://tableau-server.com
        username : str
            Log in username
        password : str
            Log in password
        site : str
            Tableau site
        project : str
            Tableau project
        parent_project : str
            Name of the parent Tableau project
        version : str
            Tableau server API version
        max_async_workers : int
            Maximum number of asynchronous tasks that will trigger jobs and wait for completion
        polling_required : bool
            Wait for job completion to proceed, otherwise just trigger the job and proceed
        polling_interval : int
            Polling interval for the job status updates (seconds)
        polling_timeout : int
            Stop polling if the job was not completed within the specified interval (seconds)
        """
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
            self.message = "Multiple projects with the same name exist on the server! Set 'parent_project' parameter!"
            super().__init__(self.message)

    class UnidentifiedWorkingProjectException(Exception):
        def __init__(self):
            self.message = "Could not identify working project, check that the spelling is correct!"
            super().__init__(self.message)

    def _authenticate(self):
        """
        Authenticate on the Tableau server.
        """
        # Suppress 'InsecureRequestWarning'
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self._authenticator = TSC.TableauAuth(self.username, self.password, self.site)
        self._server = TSC.Server(self.server)
        self._server.version = self.version
        self._server.add_http_options({"verify": False})

        return self._server.auth.sign_in(self._authenticator)

    def _get_job_status(self, job_id: str) -> dict:
        """
        Retrieve initial job status from ID and periodically poll the server for update until status changes or
        timeout is reached.

        Below status codes are used:
            -1: Unknown / Not yet started;
            0: Success;
            1: Error;
            2: Cancelled

        Parameters
        ----------
        job_id : str
            ID of the Tableau job

        Returns
        -------
        dict
            Job status dictionary
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
                    f"The job '{job_id}' did not complete within expected time, exiting... "
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

    def _refresh_datasource(self, ds: TSC.DatasourceItem) -> dict:
        """
        Trigger refresh of the specific data source object and poll for refresh status until completed or timeout.

        Parameters
        ----------
        ds : TSC.DatasourceItem
            Tableau data source object

        Returns
        -------
        dict
            Dictionary with data source name and refresh result
        """
        self._logger.info(f"Triggering refresh of '{ds.name}' datasource...")
        response = self._server.datasources.refresh(datasource_item=ds)
        job_status = self._get_job_status(job_id=response.id)
        self._logger.info(f"Data source '{ds.name}' refresh status: {job_status}!")
        return {"data_source": ds.name, **job_status}

    def _refresh_workbook(self, wb: TSC.WorkbookItem) -> dict:
        """
        Trigger refresh of the specific workbook object and poll for refresh status until completed or timeout.

        Parameters
        ----------
        wb : TSC.WorkbookItem
            Tableau workbook object

        Returns
        -------
        dict
            Dictionary with workbook name and refresh result
        """
        self._logger.info(f"Triggering refresh of '{wb.name}' workbook...")
        response = self._server.workbooks.refresh(workbook_id=wb)
        job_status = self._get_job_status(job_id=response.id)
        self._logger.info(f"Workbook '{wb.name}' refresh status: {job_status}!")
        return {"work_book": wb.name, **job_status}

    def _filter_datasources(self, data_sources: list) -> list:
        """
        Filter data sources by name and project.
        """
        all_ds = TSC.Pager(self._server.datasources)

        # Only interact with selected data sources
        lim_ds = [ds for ds in all_ds if ds.name in data_sources]

        working_project = self._get_working_project()
        if working_project:
            lim_ds = [ds for ds in lim_ds if ds.project_id == working_project.id]
        return lim_ds

    def _filter_workbooks(self, work_books: list) -> list:
        """
        Filter workbooks by name and project.
        """
        all_wb = TSC.Pager(self._server.workbooks)

        # Only interact with selected work books
        lim_wb = [wb for wb in all_wb if wb.name in work_books]

        working_project = self._get_working_project()
        if working_project:
            lim_wb = [wb for wb in lim_wb if wb.project_id == working_project.id]
        return lim_wb

    def _get_working_project(
        self, project_id: str = None
    ) -> Union[TSC.ProjectItem, None]:
        """
        Identify working project by using `project` and `parent_project` (if necessary) class properties.
        The goal is to uniquely identify specific project on the server, if multiple projects have the same
        name, the `parent_project` attribute of the TableauWrapper is required.

        If `id` of the project is known, it can be used in the method call and `project` and `parent_project`
        attributes of the TableauWrapper will be ignored.

        Parameters
        ----------
        project_id : str
            Project identifier on the Tableau server

        Returns
        -------
        ProjectItem
            ProjectItem, that represents unique project that was identified by using `project` and `parent_project`
            parameters of the TableauWrapper class.

        Raises
        ------
        MultipleWorkingProjectsException
            If multiple projects with the same name exist on the server
        UnidentifiedWorkingProjectException
            If working project could not be identified
        """
        if not self.project and not project_id:
            self._logger.warning(
                "Skip working project identification because 'project' parameter of TableauWrapper was not provided."
            )
            return None

        all_projects = TSC.Pager(self._server.projects)
        parent, lim_p = None, []

        for project in all_projects:
            if project.id == project_id:
                lim_p = [project]
                self._logger.info(
                    f"\nProject ID provided directly:\n\tName: {lim_p[0].name}\n\tID: {lim_p[0].id}"
                )
                break

            # Identify parent project
            if project.name.strip() == self.parent_project and not project_id:
                parent = project
                self._logger.info(
                    f"\nParent project identified:\n\tName: {parent.name}\n\tID: {parent.id}"
                )

            # Identify project(s)
            if project.name.strip() == self.project and not project_id:
                lim_p.append(project)

        # Further filter the list of projects by parent project id
        if self.parent_project and parent and not project_id:
            lim_p = [p for p in lim_p if p.parent_id == parent.id]

        if len(lim_p) > 1:
            raise self.MultipleWorkingProjectsException()
        elif len(lim_p) == 0:
            raise self.UnidentifiedWorkingProjectException()
        else:
            self._logger.info(
                f"\nWorking project identified:\n\tName: {lim_p[0].name}\n\tID: {lim_p[0].id}"
            )
            return lim_p[0]

    def refresh_datasources(self, data_sources: list) -> list:
        """
        Asynchronously refresh specified list of Tableau data sources.

        Parameters
        ----------
        data_sources : list
            List of data sources

        Returns
        -------
        list
            List of dictionaries with data sources and their respective refresh statuses
        """
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
        """
        Asynchronously refresh specified list of Tableau workbooks.

        Parameters
        ----------
        work_books : list
            List of work books

        Returns
        -------
        list
            List of dictionaries with work books and their respective refresh statuses
        """
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


class TableauRefreshABCOperator(BaseOperator):
    def __init__(
        self,
        server: str,
        username: str,
        password: str,
        site: str,
        project: str = None,
        parent_project: str = None,
        version: str = "3.14",
        max_async_workers: int = 5,
        polling_required: bool = True,
        polling_interval: int = 30,
        polling_timeout: int = 600,
        fail_operator: bool = True,
        *args,
        **kwargs,
    ):
        """
        Abstract class that implements generic functionality for TableauRefresh operators.

        Parameters
        ----------
        server : str
            Tableau server address, e.g. https://tableau-server.com
        username : str
            Log in username
        password : str
            Log in password
        site : str
            Tableau site
        project : str
            Tableau project
        parent_project : str
            Name of the parent Tableau project
        version : str
            Tableau server API version
        max_async_workers : int
            Maximum number of asynchronous tasks that will trigger jobs and wait for completion
        polling_required : bool
            Wait for job completion to proceed, otherwise just trigger the job and proceed
        polling_interval : int
            Polling interval for the job status updates (seconds)
        polling_timeout : int
            Stop polling if the job was not completed within the specified interval (seconds)
        fail_operator : bool
            Check Tableau refresh status and fail operator if any status is 'Failure' or 'Cancelled'
        """
        self.__logger = log

        super().__init__(*args, **kwargs)

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

        self.__logger.info(f"Tableau wrapper options:{self.wrapper_options}")

        self.tableau_wrapper = None
        self.fail_operator = fail_operator

    def _analyze_refresh_result(self, results: list) -> bool:
        """
        Analyze refresh results returned by the TableauWrapper and raise exception if necessary.

        Parameters
        ----------
        results : list
            List of dictionaries with Tableau refresh results

        Returns
        -------
        bool
            True if result is successful

        Raises
        ------
        TableauRefreshEmptyException
            If nothing was refreshed
        TableauRefreshException
            If there was an error during refresh
        """
        results_bool = [False if r["finish_code"] > 0 else True for r in results]

        if len(results_bool) == 0 and self.fail_operator:
            raise TableauRefreshEmptyException(
                "Nothing was refreshed, check that refreshable object names are set correctly!"
            )
        elif len(results_bool) > 0 and not all(results_bool) and self.fail_operator:
            raise TableauRefreshException(
                f"There was an error during the refresh of Tableau objects:\n{results}"
            )
        else:
            return True

    @abstractmethod
    def execute(self, context):
        raise NotImplementedError


class TableauRefreshDataSourceOperator(TableauRefreshABCOperator):
    def __init__(
        self,
        data_sources: list,
        skip: bool = False,
        task_id: str = "tableau_refresh_datasource",
        *args,
        **kwargs,
    ):
        """
        Airflow operator that handles refresh of Tableau data sources.

        Parameters
        ----------
        data_sources : list
            List of data source names that will be refreshed
        skip : bool
            Skip execution
        task_id : str
            ID for Airflow task
        """
        super().__init__(task_id=task_id, *args, **kwargs)
        self.data_sources = data_sources
        self.__skip = skip

    def execute(self, context):
        """
        Refresh data source in Tableau.
        """
        if not self.__skip:
            self.tableau_wrapper = TableauWrapper(**self.wrapper_options)
            results = self.tableau_wrapper.refresh_datasources(
                data_sources=self.data_sources
            )
            self._analyze_refresh_result(results)
        else:
            self.__logger.info("Skipping task execution...")


class TableauRefreshWorkBookOperator(TableauRefreshABCOperator):
    def __init__(
        self,
        workbooks: list,
        skip: bool = False,
        task_id: str = "tableau_refresh_workbooks",
        *args,
        **kwargs,
    ):
        """
        Airflow operator that handles refresh of Tableau workbooks.

        Parameters
        ----------
        workbooks : list
            List of workbook names that will be refreshed
        skip : bool
            Skip execution
        task_id : str
            ID for Airflow task
        """
        super().__init__(task_id=task_id, *args, **kwargs)
        self.workbooks = workbooks
        self.__skip = skip

    def execute(self, context):
        """
        Refresh workbooks in Tableau
        """
        if not self.__skip:
            self.tableau_wrapper = TableauWrapper(**self.wrapper_options)
            results = self.tableau_wrapper.refresh_workbooks(work_books=self.workbooks)
            self._analyze_refresh_result(results)
        else:
            self.__logger.info("Skipping task execution...")


class TableauRefreshException(Exception):
    pass


class TableauRefreshEmptyException(Exception):
    pass
