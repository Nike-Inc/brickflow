import abc
import functools
import itertools
import os
import re
import typing
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Dict, Iterator, List, Optional, Union

import yaml
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.pipelines import GetPipelineResponse
from decouple import config
from pydantic import BaseModel

from brickflow import (
    BrickflowDefaultEnvs,
    BrickflowEnvVars,
    Task,
    TaskType,
    Workflow,
    _ilog,
    ctx,
    get_brickflow_version,
    get_bundles_project_env,
)
from brickflow.bundles.model import (
    Bundle,
    DatabricksAssetBundles,
    Jobs,
    JobsGitSource,
    JobsJobClusters,
    JobsPermissions,
    JobsRunAs,
    JobsSchedule,
    JobsTasks,
    JobsTasksConditionTask,
    JobsTasksDependsOn,
    JobsTasksLibraries,
    JobsTasksNotebookTask,
    JobsTasksPipelineTask,
    JobsTasksRunJobTask,
    JobsTasksSparkJarTask,
    JobsTasksSparkPythonTask,
    JobsTasksSqlTask,
    Pipelines,
    PipelinesLibraries,
    PipelinesLibrariesNotebook,
    Resources,
    Targets,
    Workspace,
)
from brickflow.codegen import (
    CodegenInterface,
    DatabricksDefaultClusterTagKeys,
    handle_mono_repo_path,
)
from brickflow.engine.task import (
    DLTPipeline,
    TaskLibrary,
    TaskSettings,
    filter_bf_related_libraries,
    get_brickflow_libraries,
)

if typing.TYPE_CHECKING:
    from brickflow.engine.project import (
        _Project,
    )


class DatabricksBundleResourceMutator(abc.ABC):
    @abc.abstractmethod
    def mutate_resource(self, resource: Resources, ci: CodegenInterface) -> Resources:
        pass


def normalize_resource_name(text: str) -> str:
    # TODO: support hyphens (-) and underscores (_) in resource names when databricks bundles have interpolation fixed
    pattern = r"[^a-zA-Z0-9]+"
    converted_text = re.sub(pattern, "_", text)
    return converted_text.strip("_")


class DatabricksBundleTagsAndNameMutator(DatabricksBundleResourceMutator):
    def __init__(self, databricks_client: Optional[WorkspaceClient] = None):
        self.databricks_client = databricks_client or WorkspaceClient()

    @functools.lru_cache(maxsize=1)
    def _get_current_user_alphanumeric(self) -> str:
        user_email = self.databricks_client.current_user.me().user_name
        return re.sub(r"\W", "_", user_email.split("@", maxsplit=1)[0])

    def _get_default_tags(self, ci: CodegenInterface) -> Dict[str, str]:
        return {
            DatabricksDefaultClusterTagKeys.ENVIRONMENT.value: ctx.env,
            DatabricksDefaultClusterTagKeys.DEPLOYED_BY.value: self._get_current_user_alphanumeric(),
            DatabricksDefaultClusterTagKeys.DEPLOYED_AT.value: str(
                ctx.get_current_timestamp()
            ),
            DatabricksDefaultClusterTagKeys.BRICKFLOW_PROJECT_NAME.value: ci.project.name,
            DatabricksDefaultClusterTagKeys.BRICKFLOW_DEPLOYMENT_MODE.value: "Databricks Asset Bundles",
            DatabricksDefaultClusterTagKeys.BRICKFLOW_VERSION.value: get_brickflow_version(),
        }

    def _rewrite_name(self, name: str) -> str:
        if ctx.is_local() is True:
            return f"{self._get_current_user_alphanumeric()}_{name}"
        else:
            return f"{ctx.env}_{name}"

    def _mutate_jobs(self, resource: Resources, ci: CodegenInterface) -> Resources:
        if resource.jobs is not None:
            for job in resource.jobs.values():
                # set correct names
                job.name = self._rewrite_name(job.name)

                if job.job_clusters:
                    # update cluster tags
                    for cluster in job.job_clusters:
                        if cluster.new_cluster:
                            cluster.new_cluster.custom_tags = {
                                **self._get_default_tags(ci),
                                **self._get_runtime_tags(),
                                **(cluster.new_cluster.custom_tags or {}),
                            }
                # update job tags
                job.tags = {
                    **self._get_default_tags(ci),
                    **self._get_runtime_tags(),
                    **(job.tags or {}),
                }
        return resource

    @staticmethod
    def _get_runtime_tags() -> Dict[str, str]:
        project_tags = os.environ.get(BrickflowEnvVars.BRICKFLOW_PROJECT_TAGS.value)
        if project_tags:
            tags = dict(tag.split("=") for tag in project_tags.split(","))
            return {k.strip(): v.strip() for (k, v) in tags.items()}
        return {}

    def _mutate_pipelines(self, resource: Resources, ci: CodegenInterface) -> Resources:
        if resource.pipelines is not None:
            for pipeline in resource.pipelines.values():
                pipeline.name = self._rewrite_name(pipeline.name)
                if pipeline.clusters is None:
                    continue
                for cluster in pipeline.clusters:
                    # set correct tags
                    cluster.custom_tags = {
                        **self._get_default_tags(ci),
                        **self._get_runtime_tags(),
                        **(cluster.custom_tags or {}),
                    }
        return resource

    def mutate_resource(self, resource: Resources, ci: CodegenInterface) -> Resources:
        self._mutate_jobs(resource, ci)
        self._mutate_pipelines(resource, ci)
        return resource


class SupportedResolverTypes(Enum):
    PIPELINE = "pipeline"
    JOB = "job"


class ResourceReference(BaseModel):
    type_: SupportedResolverTypes
    name: str
    reference: str


class ImportBlock(BaseModel):
    to: str
    id_: Union[str, int]


class ResourceAlreadyUsedByOtherProjectError(Exception):
    pass


class ResourceAlreadyExistsWithNoProjectError(Exception):
    pass


class CurrentProjectDoesNotExistError(Exception):
    pass


def belongs_to_current_project(
    ref: ResourceReference, resource_project: Optional[str]
) -> bool:
    handle_project_validation = config(
        BrickflowEnvVars.BRICKFLOW_USE_PROJECT_NAME.value, default=True, cast=bool
    )
    belongs_to_project = (
        ctx.current_project is not None and resource_project == ctx.current_project
    )
    _ilog.info(
        "Checking if resource %s: %s belongs to current project: %s; "
        "handle project validation mode is %s, and the resource belongs to project: %s",
        ref.type_,
        ref.name,
        resource_project,
        handle_project_validation,
        belongs_to_project,
    )
    return handle_project_validation is True and belongs_to_project is True


class ProjectResourceResolver(abc.ABC):
    """
    Helps resolve import blocks for jobs and pipelines

    Logic:
        1. Check if resource belongs to current project
        2. If yes, return import block
        3. If no, check if resource belongs to other project
        4. Collect all possible import blocks, workflows can have duplicate names
        5. If there are no import blocks, return None
        6. If there is one import block, return it
        7. If there are multiple import blocks, raise error
    """

    def __init__(self, databricks_client: WorkspaceClient = None):
        self.databricks_client = databricks_client or WorkspaceClient()

    @abc.abstractmethod
    def supported_types(self) -> List[SupportedResolverTypes]:
        pass

    @abc.abstractmethod
    def _resolve(self, ref: ResourceReference) -> List[ImportBlock]:
        pass

    def resolve(self, ref: ResourceReference) -> Optional[ImportBlock]:
        if ref.type_ not in self.supported_types():
            return None
        if ctx.current_project is None:
            _ilog.info(
                "Skipping pipeline import for %s due to current project being None",
                ref.name,
            )
            return None
        import_blocks = self._resolve(ref)
        if len(import_blocks) == 0:
            return None
        if len(import_blocks) > 1:
            raise ResourceAlreadyUsedByOtherProjectError(
                f"Job {ref.name} is used by multiple projects"
            )
        return import_blocks[0]


class JobResolver(ProjectResourceResolver):
    def supported_types(self) -> List[SupportedResolverTypes]:
        return [SupportedResolverTypes.JOB]

    def _resolve(self, ref: ResourceReference) -> List[ImportBlock]:
        blocks = []
        jobs = list(self.databricks_client.jobs.list(name=ref.name))

        for job in jobs:
            if job.settings is None or job.settings.tags is None:
                continue  # skip this job for import
            job_project_tag = job.settings.tags.get(
                DatabricksDefaultClusterTagKeys.BRICKFLOW_PROJECT_NAME.value, None
            )
            if belongs_to_current_project(ref, job_project_tag) is True:
                # only add import blocks for jobs that belong to the current project
                blocks.append(ImportBlock(to=ref.reference, id_=job.job_id))

        return blocks


class PipelineResolver(ProjectResourceResolver):
    def supported_types(self) -> List[SupportedResolverTypes]:
        return [SupportedResolverTypes.PIPELINE]

    def _resolve(self, ref: ResourceReference) -> List[ImportBlock]:
        blocks = []
        for pipeline in self.databricks_client.pipelines.list_pipelines(
            filter=f"name LIKE '{ref.name}'"
        ):
            pipeline_details: GetPipelineResponse = (
                self.databricks_client.pipelines.get(pipeline_id=pipeline.pipeline_id)
            )

            if pipeline_details.spec.clusters is None:
                continue  # no clusters no way to identify if pipeline belongs to project
            project_tag = DatabricksDefaultClusterTagKeys.BRICKFLOW_PROJECT_NAME.value
            pipeline_belongs_to_current_project = any(
                cluster.custom_tags is not None
                and cluster.custom_tags.get(project_tag, None) == ctx.current_project
                for cluster in pipeline_details.spec.clusters
            )
            if pipeline_belongs_to_current_project is True:
                blocks.append(ImportBlock(to=ref.reference, id_=pipeline.pipeline_id))

        return blocks


class ImportResolverChain:
    def __init__(self, databricks_client: Optional[WorkspaceClient] = None) -> None:
        self.chain = [
            JobResolver(databricks_client),
            PipelineResolver(databricks_client),
        ]

    def resolve(self, ref: ResourceReference) -> Optional[ImportBlock]:
        for resolver in self.chain:
            if ref.type_ in resolver.supported_types():
                return resolver.resolve(ref)
        return None


class DatabricksBundleImportMutator(DatabricksBundleResourceMutator):
    def __init__(self, databricks_client: Optional[WorkspaceClient] = None) -> None:
        self.import_resolver_chain = ImportResolverChain(databricks_client)

    def _job_ref_iter(self, resource: Resources) -> Iterator[ResourceReference]:
        if resource.jobs is None:
            return None
        for job_ref, job in resource.jobs.items():
            yield ResourceReference(
                type_=SupportedResolverTypes.JOB,
                name=job.name,
                reference=f"databricks_job.{job_ref}",
            )

    def _pipeline_ref_iter(self, resource: Resources) -> Iterator[ResourceReference]:
        if resource.pipelines is None:
            return None
        for pipeline_ref, pipeline in resource.pipelines.items():
            yield ResourceReference(
                type_=SupportedResolverTypes.PIPELINE,
                name=pipeline.name,
                reference=f"databricks_pipeline.{pipeline_ref}",
            )

    def _imports_iter(self, resource: Resources) -> Iterator[ImportBlock]:
        for unresolved_ref in itertools.chain(
            self._job_ref_iter(resource), self._pipeline_ref_iter(resource)
        ):
            resolved_ref = self.import_resolver_chain.resolve(unresolved_ref)
            if resolved_ref is not None:
                yield resolved_ref

    def mutate_resource(self, resource: Resources, ci: "CodegenInterface") -> Resources:
        if isinstance(ci, DatabricksBundleCodegen) is False:
            _ilog.info(
                "Skipping mutating resource due to not being DatabricksBundleCodegen for mutator: %s",
                self.__class__.__name__,
            )
            return resource

        for import_ in self._imports_iter(resource):
            if isinstance(ci, DatabricksBundleCodegen):
                ci.add_import(import_)

        return resource


class DatabricksBundleResourceTransformer:
    def __init__(self, resource: Resources, ci: CodegenInterface) -> None:
        self.ci = ci
        self.resource = resource

    def transform(self, mutators: List[DatabricksBundleResourceMutator]) -> Resources:
        for mutator in mutators:
            self.resource = mutator.mutate_resource(self.resource, self.ci)
        return self.resource


class ImportManager:
    @staticmethod
    def create_import_str(import_blocks: List[ImportBlock]) -> str:
        import_statements = []
        for import_block in import_blocks:
            _ilog.info("Reusing import for %s - %s", import_block.to, import_block.id_)
            import_statements.append(
                f"import {{ \n"
                f"  to = {import_block.to} \n"
                f'  id = "{import_block.id_}" \n'
                f"}}"
            )
        return "\n\n".join(import_statements)

    @staticmethod
    def create_import_tf(env: str, import_blocks: List[ImportBlock]) -> None:
        file_path = f".databricks/bundle/{env}/terraform/extra_imports.tf"
        # Ensure directory structure exists
        directory = os.path.dirname(file_path)
        os.makedirs(directory, exist_ok=True)
        import_content = ImportManager.create_import_str(import_blocks)
        # Create file
        with open(file_path, "w", encoding="utf-8") as f:
            f.truncate()
            f.flush()
            f.write(import_content)


class DatabricksBundleCodegen(CodegenInterface):
    def __init__(
        self,
        project: "_Project",
        id_: str,
        env: str,
        mutators: Optional[List[DatabricksBundleResourceMutator]] = None,
        **_kwargs: Any,
    ) -> None:
        super().__init__(project, id_, env, **_kwargs)
        self.imports: List[ImportBlock] = []
        self.mutators = mutators or [
            DatabricksBundleTagsAndNameMutator(),
            DatabricksBundleImportMutator(),
        ]

    def add_import(self, import_: ImportBlock) -> None:
        self.imports.append(import_)

    @staticmethod
    def workflow_obj_to_schedule(workflow: Workflow) -> Optional[JobsSchedule]:
        if workflow.schedule_quartz_expression is not None:
            return JobsSchedule(
                quartz_cron_expression=workflow.schedule_quartz_expression,
                timezone_id=workflow.timezone,
                pause_status=workflow.schedule_pause_status,
            )
        return None

    def adjust_source(self) -> str:
        return "WORKSPACE" if self.env == BrickflowDefaultEnvs.LOCAL.value else "GIT"

    def adjust_file_path(self, file_path: str) -> str:
        """
        Adjusts the given file path based on the environment and project settings.
        If the environment is local and the project has a defined bundle base path and bundle object name,
        the method constructs a new file path by appending the local bundle path to the given file path.
        Args:
            file_path (str): The original file path to be adjusted.
        Returns:
            str: The adjusted file path.
        """
        if (
            self.env == BrickflowDefaultEnvs.LOCAL.value
            and self.project.bundle_base_path is not None
            and self.project.bundle_obj_name is not None
        ):
            bundle_files_local_path = "/".join(
                [
                    "/Workspace",
                    self.project.bundle_base_path,
                    self.project.bundle_obj_name,
                    self.project.name,
                    str(BrickflowDefaultEnvs.LOCAL.value),
                    "files",
                ]
            ).replace("//", "/")

            #  Finds the start position of the project name in the given file path and calculates the cut position.
            #   - `file_path.find(self.project.name)`: Finds the start index of the project name in the file path.
            #   - `+ len(self.project.name) + 1`: Moves the start position to the character after the project name.
            # - Adjusts the file path by appending the local bundle path to the cut file path.
            cut_file_path = file_path[
                file_path.find(self.project.name) + len(self.project.name) + 1 :
            ]
            file_path = (
                bundle_files_local_path + file_path
                if file_path.startswith("/")
                else f"{bundle_files_local_path}/{cut_file_path}"
            )
        return file_path

    def task_to_task_obj(self, task: Task) -> JobsTasksNotebookTask:
        if task.task_type in [TaskType.BRICKFLOW_TASK, TaskType.CUSTOM_PYTHON_TASK]:
            generated_path = handle_mono_repo_path(self.project, self.env)
            return JobsTasksNotebookTask(
                **task.get_obj_dict(generated_path),
                source=self.adjust_source(),
            )

    def workflow_obj_to_pipelines(self, workflow: Workflow) -> Dict[str, Pipelines]:
        pipelines_dict = {}
        for task in workflow.tasks.values():
            if task.task_type == TaskType.DLT:
                dlt_task: DLTPipeline = task.task_func()
                pipeline_ref = self.get_pipeline_reference(workflow, dlt_task)
                pipeline_library = PipelinesLibraries(
                    notebook=PipelinesLibrariesNotebook(path=dlt_task.notebook_path)
                )
                pipelines_dict[pipeline_ref] = Pipelines(
                    **dlt_task.to_dict(), libraries=[pipeline_library]
                )

        return pipelines_dict

    @staticmethod
    def get_pipeline_reference(workflow: Workflow, pipeline: DLTPipeline) -> str:
        return normalize_resource_name(f"{workflow.name}-{pipeline.name}")

    def _build_native_notebook_task(
        self,
        task_name: str,
        task: Task,
        task_libraries: List[JobsTasksLibraries],
        task_settings: TaskSettings,
        depends_on: List[JobsTasksDependsOn],
        **_kwargs: Any,
    ) -> JobsTasks:
        notebook_task: JobsTasksNotebookTask = task.task_func()

        try:
            assert isinstance(notebook_task, JobsTasksNotebookTask)
        except AssertionError as e:
            raise ValueError(
                f"Error while building notebook task {task_name}. "
                f"Make sure {task_name} returns a NotebookTask object."
            ) from e

        return JobsTasks(
            **task_settings.to_tf_dict(),
            notebook_task=notebook_task,
            libraries=task_libraries,
            depends_on=depends_on,
            task_key=task_name,
            # unpack dictionary provided by cluster object, will either be key or
            # existing cluster id
            **task.cluster.job_task_field_dict,
        )

    def _build_native_spark_jar_task(
        self,
        task_name: str,
        task: Task,
        task_libraries: List[JobsTasksLibraries],
        task_settings: TaskSettings,
        depends_on: List[JobsTasksDependsOn],
        **_kwargs: Any,
    ) -> JobsTasks:
        spark_jar_task: JobsTasksSparkJarTask = task.task_func()

        try:
            assert isinstance(spark_jar_task, JobsTasksSparkJarTask)
        except AssertionError as e:
            raise ValueError(
                f"Error while building jar task {task_name}. "
                f"Make sure {task_name} returns a SparkJarTask object."
            ) from e

        return JobsTasks(
            **task_settings.to_tf_dict(),
            spark_jar_task=spark_jar_task,
            libraries=task_libraries,
            depends_on=depends_on,
            task_key=task_name,
            # unpack dictionary provided by cluster object, will either be key or
            # existing cluster id
            **task.cluster.job_task_field_dict,
        )

    def _build_native_spark_python_task(
        self,
        task_name: str,
        task: Task,
        task_libraries: List[JobsTasksLibraries],
        task_settings: TaskSettings,
        depends_on: List[JobsTasksDependsOn],
        **kwargs: Any,
    ) -> JobsTasks:
        spark_python_task = task.task_func()

        try:
            assert isinstance(spark_python_task, JobsTasksSparkPythonTask)
        except AssertionError as e:
            raise ValueError(
                f"Error while building python task {task_name}. "
                f"Make sure {task_name} returns a SparkPythonTask object."
            ) from e

        spark_python_task.source = self.adjust_source()
        spark_python_task.python_file = self.adjust_file_path(
            file_path=spark_python_task.python_file
        )
        workflow: Optional[Workflow] = kwargs.get("workflow")
        commom_task_parameters = workflow.common_task_parameters if workflow else None

        if commom_task_parameters:
            spark_python_task.parameters = spark_python_task.parameters or []
            for k, v in commom_task_parameters.items():
                if k not in spark_python_task.parameters:
                    spark_python_task.parameters.append(k)
                    spark_python_task.parameters.append(v)

        return JobsTasks(
            **task_settings.to_tf_dict(),
            spark_python_task=spark_python_task,
            libraries=task_libraries,
            depends_on=depends_on,
            task_key=task_name,
            # unpack dictionary provided by cluster object, will either be key or
            # existing cluster id
            **task.cluster.job_task_field_dict,
        )

    def _build_native_run_job_task(
        self,
        task_name: str,
        task: Task,
        task_settings: TaskSettings,
        depends_on: List[JobsTasksDependsOn],
        **_kwargs: Any,
    ) -> JobsTasks:
        run_job_task: JobsTasksRunJobTask = task.task_func()

        try:
            assert isinstance(run_job_task, JobsTasksRunJobTask)
        except AssertionError as e:
            raise ValueError(
                f"Error while building run job task {task_name}. "
                f"Make sure {task_name} returns a RunJobTask object."
            ) from e

        return JobsTasks(
            **task_settings.to_tf_dict(),  # type: ignore
            run_job_task=JobsTasksRunJobTask(job_id=run_job_task.job_id),
            depends_on=depends_on,
            task_key=task_name,
        )

    def _build_native_sql_file_task(
        self,
        task_name: str,
        task: Task,
        task_settings: TaskSettings,
        depends_on: List[JobsTasksDependsOn],
        **_kwargs: Any,
    ) -> JobsTasks:
        sql_task: JobsTasksSqlTask = task.task_func()

        try:
            assert isinstance(sql_task, JobsTasksSqlTask)
        except AssertionError as e:
            raise ValueError(
                f"Error while building sql file task {task_name}. "
                f"Make sure {task_name} returns a JobsTasksSqlTask object."
            ) from e

        return JobsTasks(
            **task_settings.to_tf_dict(),  # type: ignore
            sql_task=sql_task,
            depends_on=depends_on,
            task_key=task_name,
        )

    def _build_native_condition_task(
        self,
        task_name: str,
        task: Task,
        task_settings: TaskSettings,
        depends_on: List[JobsTasksDependsOn],
        **_kwargs: Any,
    ) -> JobsTasks:
        condition_task: JobsTasksConditionTask = task.task_func()

        try:
            assert isinstance(condition_task, JobsTasksConditionTask)
        except AssertionError as e:
            raise ValueError(
                f"Error while building If/else task {task_name}. "
                f"Make sure {task_name} returns a JobsTasksConditionTask object."
            ) from e
        return JobsTasks(
            **task_settings.to_tf_dict(),  # type: ignore
            condition_task=condition_task,
            depends_on=depends_on,
            task_key=task_name,
        )

    def _build_dlt_task(
        self,
        task_name: str,
        task: Task,
        workflow: Workflow,
        task_settings: TaskSettings,
        depends_on: List[JobsTasksDependsOn],
        **_kwargs: Any,
    ) -> JobsTasks:
        dlt_task: DLTPipeline = task.task_func()

        try:
            assert isinstance(dlt_task, DLTPipeline)
        except AssertionError as e:
            raise ValueError(
                f"Error while building DLT task {task_name}. "
                f"Make sure {task_name} returns a DLTPipeline object."
            ) from e

        # tasks.append(Pipelines(**dlt_task.to_dict())) # TODO: fix this so pipeline also gets created
        pipeline_ref = self.get_pipeline_reference(workflow, dlt_task)
        return JobsTasks(
            **task_settings.to_tf_dict(),  # type: ignore
            pipeline_task=JobsTasksPipelineTask(
                pipeline_id=f"${{resources.pipelines.{pipeline_ref}.id}}",
                # full_refresh=..., TODO: add full refresh
            ),  # type: ignore
            depends_on=depends_on,
            task_key=task_name,
        )

    def _build_brickflow_entrypoint_task(
        self,
        task_name: str,
        task: Task,
        task_settings: TaskSettings,
        depends_on: List[JobsTasksDependsOn],
        task_libraries: List[JobsTasksLibraries],
        **_kwargs: Any,
    ) -> JobsTasks:
        task_obj = JobsTasks(
            **{
                task.databricks_task_type_str: self.task_to_task_obj(task),
                **task_settings.to_tf_dict(),
            },  # type: ignore
            libraries=task_libraries,
            depends_on=depends_on,
            task_key=task_name,
            # unpack dictionary provided by cluster object, will either be key or
            # existing cluster id
            **task.cluster.job_task_field_dict,
        )
        return task_obj

    def workflow_obj_to_tasks(
        self, workflow: Workflow
    ) -> List[Union[JobsTasks, Pipelines]]:
        tasks = []

        map_task_type_to_builder: Dict[TaskType, Callable[..., Any]] = {
            TaskType.DLT: self._build_dlt_task,
            TaskType.NOTEBOOK_TASK: self._build_native_notebook_task,
            TaskType.SPARK_JAR_TASK: self._build_native_spark_jar_task,
            TaskType.SPARK_PYTHON_TASK: self._build_native_spark_python_task,
            TaskType.RUN_JOB_TASK: self._build_native_run_job_task,
            TaskType.SQL: self._build_native_sql_file_task,
            TaskType.IF_ELSE_CONDITION_TASK: self._build_native_condition_task,
        }

        for task_name, task in workflow.tasks.items():
            builder_func = map_task_type_to_builder.get(
                task.task_type, self._build_brickflow_entrypoint_task
            )

            # TODO: DLT
            # pipeline_task: Pipeline = self._create_dlt_notebooks(stack, task)
            if task.depends_on_names:
                depends_on = [
                    JobsTasksDependsOn(task_key=depends_key, outcome=expected_outcome)
                    for i in task.depends_on_names
                    for depends_key, expected_outcome in i.items()
                ]  # type: ignore
            else:
                depends_on = []
            libraries = TaskLibrary.unique_libraries(
                task.libraries + (self.project.libraries or [])
            )
            if workflow.enable_plugins is True:
                libraries = filter_bf_related_libraries(libraries)
                libraries += get_brickflow_libraries(workflow.enable_plugins)

            task_libraries = [
                JobsTasksLibraries(**library.dict) for library in libraries
            ]  # type: ignore
            task_settings = workflow.default_task_settings.merge(task.task_settings)  # type: ignore
            task = builder_func(
                task_name=task_name,
                task=task,
                workflow=workflow,
                task_libraries=task_libraries,
                task_settings=task_settings,
                depends_on=depends_on,
            )
            tasks.append(task)

        tasks.sort(key=lambda t: (t.task_key is None, t.task_key))

        return tasks

    @staticmethod
    def workflow_obj_to_permissions(
        workflow: Workflow,  # noqa
    ) -> Optional[List[JobsPermissions]]:
        # TODO: add permissions
        perms = workflow.permissions.to_access_controls()
        job_perms = []
        for perm in perms:
            this_perm = perm.copy()
            this_perm["level"] = this_perm.pop("permission_level")
            job_perms.append(JobsPermissions(**this_perm))

        if len(job_perms) == 0:
            return None

        return job_perms

    @staticmethod
    def workflow_handle_run_as(workflow: Workflow) -> Dict[str, Any]:
        # guard against both being set
        if workflow.run_as_user and workflow.run_as_service_principal is not None:
            raise ValueError("Cannot set both run_as_user and run_as_service_principal")

        if workflow.run_as_user is not None:
            return {"run_as": JobsRunAs(user_name=workflow.run_as_user)}
        elif workflow.run_as_service_principal is not None:
            return {
                "run_as": JobsRunAs(
                    service_principal_name=workflow.run_as_service_principal
                )
            }
        return {}

    def proj_to_bundle(self) -> DatabricksAssetBundles:
        jobs = {}
        pipelines = {}  # noqa

        selected_workflows = (
            str(
                os.getenv(BrickflowEnvVars.BRICKFLOW_DEPLOY_ONLY_WORKFLOWS.value)
            ).split(",")
            if os.getenv(BrickflowEnvVars.BRICKFLOW_DEPLOY_ONLY_WORKFLOWS.value)
            else []
        )

        if self.env != BrickflowDefaultEnvs.LOCAL.value and selected_workflows:
            raise ValueError(
                "Cannot set BRICKFLOW_DEPLOY_ONLY_WORKFLOWS in non-local environments"
            )

        for workflow_name, workflow in self.project.workflows.items():
            if selected_workflows and workflow_name not in selected_workflows:
                _ilog.info(
                    "Skipping workflow %s as it is not in the selected workflows %s",
                    workflow_name,
                    selected_workflows,
                )
                continue

            git_ref = self.project.git_reference or ""
            ref_type = git_ref.split("/", maxsplit=1)[0]
            ref_type = (
                ref_type if ref_type.startswith("git_") else f"git_{ref_type}"
            )  # handle git_branch and git_tag
            ref_value = "/".join(git_ref.split("/")[1:])

            # only add git source if not local
            git_conf = (
                JobsGitSource(
                    git_url=self.project.git_repo or "",
                    git_provider=self.project.provider,
                    **{ref_type: ref_value},
                )
                if self.env != BrickflowDefaultEnvs.LOCAL.value
                else None
            )
            workflow_clusters = workflow.unique_new_clusters_dict()
            tasks = self.workflow_obj_to_tasks(workflow)
            job = Jobs(
                name=workflow_name,
                tasks=tasks,
                git_source=git_conf,
                tags=workflow.tags,
                health=workflow.health,
                job_clusters=[JobsJobClusters(**c) for c in workflow_clusters],
                schedule=self.workflow_obj_to_schedule(workflow),
                max_concurrent_runs=workflow.max_concurrent_runs,
                **self.workflow_handle_run_as(workflow),
                permissions=self.workflow_obj_to_permissions(
                    workflow
                ),  # will be none if not set
                timeout_seconds=workflow.timeout_seconds,
                email_notifications=workflow.email_notifications,
                notification_settings=workflow.notification_settings,
                webhook_notifications=workflow.webhook_notifications,
                trigger=workflow.trigger,
                continuous=workflow.schedule_continuous,
                parameters=workflow.parameters,
            )
            jobs[workflow_name] = job

            pipelines.update(self.workflow_obj_to_pipelines(workflow))

        resources = Resources(
            jobs=jobs,
            pipelines=pipelines,
        )
        DatabricksBundleResourceTransformer(resources, self).transform(self.mutators)

        if self.project.bundle_base_path is None:
            raise ValueError("project.bundle_base_path is None")

        if self.project.bundle_obj_name is None:
            raise ValueError("project.bundle_obj_name is None")

        if self.project.name is None:
            raise ValueError("project.name is None")

        bundle_root_path = (
            Path(self.project.bundle_base_path)
            / self.project.bundle_obj_name
            / self.project.name
            / self.env
        )

        bundle_suffix = config(
            BrickflowEnvVars.BRICKFLOW_WORKFLOW_SUFFIX.value,
            default=None,
        )

        bundle_prefix = config(
            BrickflowEnvVars.BRICKFLOW_WORKFLOW_PREFIX.value,
            default=None,
        )

        if bundle_prefix is not None:
            bundle_root_path = bundle_root_path / bundle_prefix

        if bundle_suffix is not None:
            bundle_root_path = bundle_root_path / bundle_suffix

        env_content = Targets(
            workspace=Workspace(
                root_path=str(bundle_root_path.as_posix()),
                file_path=str((bundle_root_path / "files").as_posix()),
                state_path=str((bundle_root_path / "state").as_posix()),
            ),
            resources=resources,
        )

        return DatabricksAssetBundles(
            targets={
                get_bundles_project_env(): env_content,
            },
            bundle=Bundle(name=self.project.name),
            workspace=Workspace(),  # empty required not optional
        )

    def synth(self) -> None:
        # set the context's current project needed for imports
        ctx.set_current_project(self.project.name)
        bundle = self.proj_to_bundle()

        if self.env == BrickflowDefaultEnvs.LOCAL.value:
            # it should use the bundles project env field as that is the folder bundles makes
            ImportManager.create_import_tf(get_bundles_project_env(), self.imports)

        def quoted_presenter(dumper, data):  # type: ignore[no-untyped-def]
            return dumper.represent_scalar("tag:yaml.org,2002:str", data, style='"')

        yaml.add_representer(str, quoted_presenter)

        with open("bundle.yml", "w", encoding="utf-8") as f:
            f.write(yaml.dump(bundle.dict(exclude_unset=True)))
