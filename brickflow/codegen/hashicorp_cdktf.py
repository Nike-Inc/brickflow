import os
from pathlib import Path
from typing import List, Optional

from decouple import config

from brickflow import (
    TaskType,
    DLTPipeline,
    ctx,
    BrickflowEnvVars,
    _ilog,
)
from brickflow.codegen import (
    CodegenInterface,
    GitRepoIsDirtyError,
    handle_mono_repo_path,
)
from brickflow.engine import is_git_dirty
from brickflow.engine.task import Task, TaskLibrary
from brickflow.engine.utils import get_properties
from brickflow.engine.workflow import Workflow


class HashicorpCDKTFGen(CodegenInterface):
    def _generate_app(self):
        # local import to avoid node req
        from cdktf import App

        app = App()
        self._generate_tf_objs(
            app,
            self.id_,
        )
        return app

    def _create_workflow_schedule(self, workflow: Workflow) -> "JobSchedule":  # type: ignore
        # Avoid node reqs
        from brickflow.tf.databricks.job import (
            JobSchedule,
        )

        if workflow.schedule_quartz_expression is not None:
            return JobSchedule(
                quartz_cron_expression=workflow.schedule_quartz_expression,
                timezone_id=workflow.timezone,
            )
        return None

    def _create_dlt_notebooks(
        self, stack: "TerraformStack", task: Task  # type:ignore # noqa
    ) -> Optional["Pipeline"]:  # type:ignore # noqa
        # Avoid node reqs
        from brickflow.tf.databricks.notebook import Notebook
        from brickflow.tf.databricks.pipeline import (
            Pipeline,
            PipelineCluster,
            PipelineLibrary,
            PipelineLibraryNotebook,
        )
        from brickflow.codegen.cdktf_aspects import get_current_user

        if task.task_type == TaskType.DLT:
            dlt_task: DLTPipeline = task.task_func()
            _path = (
                Path(get_current_user(stack).home)
                / "brickflow"
                / "projects"
                / Path(self.project.name)
                / "env"
                / ctx.env
                / dlt_task.notebook_path.lstrip("/")
            )
            nb = Notebook(
                stack,
                dlt_task.notebook_path,
                language=dlt_task.language,
                content_base64=dlt_task.to_b64(os.getcwd()),
                path=str(_path),
            )
            pipeline_library = PipelineLibrary(
                notebook=PipelineLibraryNotebook(path=nb.path)
            )

            clusters = [
                PipelineCluster(
                    **dlt_task.cluster.as_dict(
                        is_dlt_cluster=True,
                        allowed_fields=get_properties(PipelineCluster),
                    )
                )
            ]
            return Pipeline(
                stack,
                task.name,
                **dlt_task.to_dict(),
                cluster=clusters,
                library=[pipeline_library],
            )
        return None

    def _get_notebook_tf_obj(self, task: Task) -> "JobTaskNotebookTask":  # type: ignore  # noqa
        from brickflow.tf.databricks.job import JobTaskNotebookTask

        new_entrypoint = handle_mono_repo_path(self.project, self.env)
        if task.task_type in [TaskType.NOTEBOOK, TaskType.CUSTOM_PYTHON_TASK]:
            return JobTaskNotebookTask(
                **task.get_obj_dict(new_entrypoint),
                source="GIT",
            )

    # TODO: test terraform objects
    def _create_workflow_tasks(
        self, stack: "TerraformStack", workflow: Workflow  # type: ignore  # noqa
    ) -> List["JobTask"]:  # type: ignore  # noqa
        # Avoid node reqs
        from brickflow.tf.databricks.job import (
            JobTask,
            JobTaskPipelineTask,
            JobTaskDependsOn,
        )
        from brickflow.tf.databricks.pipeline import Pipeline

        tasks = []
        for task_name, task in workflow.tasks.items():
            pipeline_task: Pipeline = self._create_dlt_notebooks(stack, task)
            depends_on = [JobTaskDependsOn(task_key=f) for f in task.depends_on_names]

            tf_task_type = (
                task.task_type_str
                if task.task_type_str != TaskType.CUSTOM_PYTHON_TASK.value
                else TaskType.NOTEBOOK.value
            )

            libraries = TaskLibrary.unique_libraries(
                task.libraries + (self.project.libraries or [])
            )
            task_libraries = [library.dict for library in libraries]

            task_settings = workflow.default_task_settings.merge(task.task_settings)
            # dlt task is different
            if task.task_type == TaskType.DLT:
                tf_task = JobTask(
                    pipeline_task=JobTaskPipelineTask(pipeline_id=pipeline_task.id),
                    depends_on=depends_on,
                    task_key=task_name,
                    **task_settings.to_tf_dict(),
                )
            else:
                tf_task = JobTask(
                    **{
                        tf_task_type: self._get_notebook_tf_obj(task),
                        **task_settings.to_tf_dict(),
                    },
                    library=task_libraries,
                    depends_on=depends_on,
                    task_key=task_name,
                    # unpack dictionary provided by cluster object, will either be key or
                    # existing cluster id
                    **task.cluster.job_task_field_dict,
                )
            tasks.append(tf_task)
        tasks.sort(key=lambda t: (t.task_key is None, t.task_key))
        return tasks

    def _create_workflow_permissions(  # type: ignore
        self, stack: "TerraformStack", workflow: Workflow, job_obj: "Job"  # type: ignore   # noqa
    ):
        # Avoid node reqs
        from brickflow.tf.databricks.permissions import (
            Permissions,
            PermissionsAccessControl,
        )

        return Permissions(
            stack,
            id_=f"{workflow.name}_permissions",
            job_id=job_obj.id,
            access_control=[
                PermissionsAccessControl(**i)
                for i in workflow.permissions.to_access_controls()
            ],
        )

    def _should_use_s3_backend(self) -> bool:
        return self.project.s3_backend is not None and ctx.is_local() is False

    def _generate_tf_objs(self, app, id_) -> None:  # type: ignore
        if (
            is_git_dirty()
            and config(BrickflowEnvVars.BRICKFLOW_FORCE_DEPLOY.value, default="false")
            == "false"
        ):
            raise GitRepoIsDirtyError(
                "Please commit all your changes before attempting to deploy."
            )

        # Avoid node reqs
        from cdktf import TerraformStack, Aspects
        from brickflow.tf.databricks.provider import DatabricksProvider
        from brickflow.tf.databricks.job import Job, JobGitSource, JobJobCluster
        from brickflow.codegen.cdktf_aspects import BrickflowTerraformNodeVisitor

        stacks = []
        stack = None
        if self.project.batch is True:
            stack = TerraformStack(app, id_)
            DatabricksProvider(
                stack,
                "Databricks",
            )
            stacks.append(stack)

        _ilog.info("Loading git ref: %s", self.project.git_reference or "")
        for workflow_name, workflow in self.project.workflows.items():
            if self.project.batch is False:
                stack = TerraformStack(app, f"{id_}_{workflow_name}")
                DatabricksProvider(
                    stack,
                    "Databricks",
                )
                stacks.append(stack)

            git_ref = self.project.git_reference or ""
            ref_type = git_ref.split("/", maxsplit=1)[0]
            ref_value = "/".join(git_ref.split("/")[1:])
            git_conf = JobGitSource(
                url=self.project.git_repo or "",
                provider=self.project.provider,
                **{ref_type: ref_value},
            )
            workflow_clusters = workflow.unique_new_clusters_dict()
            tasks = self._create_workflow_tasks(stack, workflow)
            job = Job(
                stack,
                id_=workflow_name,
                name=workflow_name,
                task=tasks,
                git_source=git_conf,
                tags=workflow.tags,
                job_cluster=[JobJobCluster(**c) for c in workflow_clusters],
                schedule=self._create_workflow_schedule(workflow),
                max_concurrent_runs=workflow.max_concurrent_runs,
            )
            if workflow.permissions.to_access_controls():
                self._create_workflow_permissions(stack, workflow, job)
        for stack in stacks:
            stack_aspects = Aspects.of(stack)
            stack_aspects.add(BrickflowTerraformNodeVisitor(self.project, stack))
            if self._should_use_s3_backend():
                from cdktf import S3Backend

                S3Backend(stack, **self.project.s3_backend)

    def synth(self):
        app = self._generate_app()
        app.synth()
