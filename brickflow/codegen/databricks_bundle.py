import abc
import functools
import itertools
import os
import re
import typing
from enum import Enum
from pathlib import Path
from typing import List, Optional, Union, Dict, Any, Iterator

import yaml
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.pipelines import GetPipelineResponse
from decouple import config
from pydantic import BaseModel

from brickflow import (
    Workflow,
    Task,
    TaskType,
    BrickflowDefaultEnvs,
    ctx,
    _ilog,
    get_bundles_project_env,
    BrickflowEnvVars,
    get_brickflow_version,
)
from brickflow.bundles.model import (
    Jobs,
    JobsSchedule,
    JobsTasks,
    JobsPermissions,
    JobsGitSource,
    DatabricksAssetBundles,
    JobsJobClusters,
    JobsTasksPipelineTask,
    JobsTasksDependsOn,
    JobsTasksLibraries,
    JobsTasksNotebookTask,
    Resources,
    Workspace,
    Bundle,
    Pipelines,
    JobsRunAs,
    PipelinesLibraries,
    PipelinesLibrariesNotebook,
    Targets,
)
from brickflow.codegen import (
    CodegenInterface,
    handle_mono_repo_path,
    DatabricksDefaultClusterTagKeys,
)
from brickflow.engine.task import (
    TaskLibrary,
    DLTPipeline,
    TaskSettings,
    filter_bf_related_libraries,
    get_brickflow_libraries,
)

if typing.TYPE_CHECKING:
    from brickflow.engine.project import (
        _Project,
    )  # noqa


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
                # set tags
                job.tags = {**self._get_default_tags(ci), **(job.tags or {})}
        return resource

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
        **kwargs: Any,
    ) -> None:
        super().__init__(project, id_, env, **kwargs)
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

    def get_entrypoint_notebook_source(self) -> str:
        return "WORKSPACE" if self.env == BrickflowDefaultEnvs.LOCAL.value else "GIT"

    def task_to_task_obj(self, task: Task) -> Union[JobsTasksNotebookTask]:
        if task.task_type in [TaskType.BRICKFLOW_TASK, TaskType.CUSTOM_PYTHON_TASK]:
            generated_path = handle_mono_repo_path(self.project, self.env)
            return JobsTasksNotebookTask(
                **task.get_obj_dict(generated_path),
                source=self.get_entrypoint_notebook_source(),
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
    ) -> JobsTasks:
        try:
            notebook_task: JobsTasksNotebookTask = task.task_func()
        except Exception as e:
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

    def _build_dlt_task(
        self,
        task_name: str,
        task: Task,
        workflow: Workflow,
        depends_on: List[JobsTasksDependsOn],
    ) -> JobsTasks:
        dlt_task: DLTPipeline = task.task_func()
        # tasks.append(Pipelines(**dlt_task.to_dict())) # TODO: fix this so pipeline also gets created
        pipeline_ref = self.get_pipeline_reference(workflow, dlt_task)
        return JobsTasks(
            pipeline_task=JobsTasksPipelineTask(
                pipeline_id=f"${{resources.pipelines.{pipeline_ref}.id}}",
                # full_refresh=..., TODO: add full refresh
            ),
            depends_on=depends_on,
            task_key=task_name,
        )

    def workflow_obj_to_tasks(
        self, workflow: Workflow
    ) -> List[Union[JobsTasks, Pipelines]]:
        tasks = []
        for task_name, task in workflow.tasks.items():
            # TODO: DLT
            # pipeline_task: Pipeline = self._create_dlt_notebooks(stack, task)
            depends_on = [JobsTasksDependsOn(task_key=f) for f in task.depends_on_names]
            libraries = TaskLibrary.unique_libraries(
                task.libraries + (self.project.libraries or [])
            )
            if workflow.enable_plugins is True:
                libraries = filter_bf_related_libraries(libraries)
                libraries += get_brickflow_libraries(workflow.enable_plugins)

            task_libraries = [
                JobsTasksLibraries(**library.dict) for library in libraries
            ]
            task_settings = workflow.default_task_settings.merge(task.task_settings)
            if task.task_type == TaskType.DLT:
                # native dlt task
                tasks.append(
                    self._build_dlt_task(task_name, task, workflow, depends_on)
                )
            elif task.task_type == TaskType.NOTEBOOK_TASK:
                # native notebook task
                tasks.append(
                    self._build_native_notebook_task(
                        task_name, task, task_libraries, task_settings, depends_on
                    )
                )
            else:
                # brickflow entrypoint task
                task_obj = JobsTasks(
                    **{
                        task.databricks_task_type_str: self.task_to_task_obj(task),
                        **task_settings.to_tf_dict(),
                    },
                    libraries=task_libraries,
                    depends_on=depends_on,
                    task_key=task_name,
                    # unpack dictionary provided by cluster object, will either be key or
                    # existing cluster id
                    **task.cluster.job_task_field_dict,
                )
                tasks.append(task_obj)
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
        for workflow_name, workflow in self.project.workflows.items():
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
