import abc
import re
from pathlib import Path
from typing import List, Optional, Union, Dict, Any

import yaml

from brickflow import (
    Workflow,
    Task,
    TaskType,
    BrickflowDefaultEnvs,
    ctx,
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
    PipelinesClusters,
    JobsRunAs,
    Environments,
    PipelinesLibraries,
    PipelinesLibrariesNotebook,
)
from brickflow.codegen import CodegenInterface, handle_mono_repo_path
from brickflow.engine.task import TaskLibrary, DLTPipeline


class DatabricksBundleResourceMutator(abc.ABC):
    @abc.abstractmethod
    def mutate_resource(self, resource: Resources, ci: CodegenInterface) -> Resources:
        pass


def normalize_resource_name(text):
    # TODO: support hyphens (-) and underscores (_) in resource names when databricks bundles have interpolation fixed
    pattern = r"[^a-zA-Z0-9]+"
    converted_text = re.sub(pattern, "_", text)
    return converted_text.strip("_")


class DatabricksBundleTagsAndNameMutator(DatabricksBundleResourceMutator):
    def _get_current_user_alphanumeric(self):
        from databricks.sdk import WorkspaceClient

        user_email = WorkspaceClient().current_user.me().user_name
        return re.sub(r"\W", "_", user_email.split("@", maxsplit=1)[0])

    def _get_default_tags(self, ci: CodegenInterface):
        return {
            "environment": ctx.env,
            "deployed_by": self._get_current_user_alphanumeric(),
            "brickflow_project_name": ci.project.name,
            "databricks_deploy_mode": "Databricks Asset Bundles",
        }

    def _rewrite_name(self, name: str):
        if ctx.is_local() is True:
            return f"{self._get_current_user_alphanumeric()}_{name}"
        else:
            return f"{ctx.env}_{name}"

    def _mutate_jobs(self, resource: Resources, ci: CodegenInterface):
        if resource.jobs is not None:
            for job in resource.jobs.values():
                # set correct names
                job.name = self._rewrite_name(job.name)
                # set tags
                job.tags = {**self._get_default_tags(ci), **(job.tags or {})}
        return resource

    def _mutate_pipelines(self, resource: Resources, ci: CodegenInterface):
        if resource.pipelines is not None:
            for pipeline in resource.pipelines.values():
                pipeline.name = self._rewrite_name(pipeline.name)
                if pipeline.clusters is None:
                    continue
                for cluster in pipeline.clusters:
                    cluster: PipelinesClusters
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


class DatabricksBundleResourceTransformer:
    def __init__(self, resource: Resources, ci: CodegenInterface):
        self.ci = ci
        self.resource = resource

    def transform(self, mutators: List[DatabricksBundleResourceMutator]) -> Resources:
        for mutator in mutators:
            self.resource = mutator.mutate_resource(self.resource, self.ci)
        return self.resource


class DatabricksBundleCodegen(CodegenInterface):
    @staticmethod
    def workflow_obj_to_schedule(workflow: Workflow) -> Optional[JobsSchedule]:
        if workflow.schedule_quartz_expression is not None:
            return JobsSchedule(
                quartz_cron_expression=workflow.schedule_quartz_expression,
                timezone_id=workflow.timezone,
            )
        return None

    def get_entrypoint_notebook_source(self) -> str:
        return "WORKSPACE" if self.env == BrickflowDefaultEnvs.LOCAL.value else "GIT"

    def task_to_task_obj(self, task: Task) -> Union[JobsTasksNotebookTask]:
        if task.task_type in [TaskType.NOTEBOOK, TaskType.CUSTOM_PYTHON_TASK]:
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
    def get_pipeline_reference(workflow: Workflow, pipeline: DLTPipeline):
        return normalize_resource_name(f"{workflow.name}-{pipeline.name}")

    def workflow_obj_to_tasks(
        self, workflow: Workflow
    ) -> List[Union[JobsTasks, Pipelines]]:
        tasks = []
        for task_name, task in workflow.tasks.items():
            # TODO: DLT
            # pipeline_task: Pipeline = self._create_dlt_notebooks(stack, task)
            depends_on = [JobsTasksDependsOn(task_key=f) for f in task.depends_on_names]
            task_type = (
                task.task_type_str
                if task.task_type_str != TaskType.CUSTOM_PYTHON_TASK.value
                else TaskType.NOTEBOOK.value
            )
            libraries = TaskLibrary.unique_libraries(
                task.libraries + (self.project.libraries or [])
            )
            task_libraries = [
                JobsTasksLibraries(**library.dict) for library in libraries
            ]
            task_settings = workflow.default_task_settings.merge(task.task_settings)
            if task.task_type == TaskType.DLT:
                dlt_task: DLTPipeline = task.task_func()
                # tasks.append(Pipelines(**dlt_task.to_dict())) # TODO: fix this so pipeline also gets created
                pipeline_ref = self.get_pipeline_reference(workflow, dlt_task)
                tasks.append(
                    JobsTasks(
                        pipeline_task=JobsTasksPipelineTask(
                            pipeline_id=f"${{resources.pipelines.{pipeline_ref}.id}}",
                            # full_refresh=..., TODO: add full refresh
                        ),
                        depends_on=depends_on,
                        task_key=task_name,
                    )
                )
            else:
                task_obj = JobsTasks(
                    **{
                        task_type: self.task_to_task_obj(task),
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
                job_clusters=[JobsJobClusters(**c) for c in workflow_clusters],
                schedule=self.workflow_obj_to_schedule(workflow),
                max_concurrent_runs=workflow.max_concurrent_runs,
                **self.workflow_handle_run_as(workflow),
                permissions=self.workflow_obj_to_permissions(
                    workflow
                ),  # will be none if not set
            )
            jobs[workflow_name] = job

            pipelines.update(self.workflow_obj_to_pipelines(workflow))

        resources = Resources(
            jobs=jobs,
            pipelines=pipelines,
        )
        DatabricksBundleResourceTransformer(resources, self).transform(
            [DatabricksBundleTagsAndNameMutator()]
        )
        bundle_root_path = (
            Path(self.project.bundle_base_path)
            / self.project.bundle_obj_name
            / self.project.name
            / self.env
        )
        env_content = Environments(
            workspace=Workspace(
                root_path=str(bundle_root_path),
                file_path=str(bundle_root_path / "files"),
                state_path=str(bundle_root_path / "state"),
            ),
            resources=resources,
        )

        return DatabricksAssetBundles(
            environments={
                self.env: env_content,
            },
            bundle=Bundle(name=self.project.name),
            workspace=Workspace(),  # empty required not optional
        )

    def synth(self):
        bundle = self.proj_to_bundle()

        with open("bundle.yml", "w", encoding="utf-8") as f:
            f.write(yaml.dump(bundle.dict(exclude_unset=True)))
