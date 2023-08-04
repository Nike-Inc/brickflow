import functools
from typing import Dict, TYPE_CHECKING

import constructs
import jsii

from cdktf import IAspect, TerraformStack

from brickflow.codegen import get_brickflow_tags, DatabricksDefaultClusterTagKeys
from brickflow.context import ctx
from brickflow.tf import DATABRICKS_TERRAFORM_PROVIDER_VERSION
from brickflow.tf.databricks.data_databricks_current_user import (
    DataDatabricksCurrentUser,
)
from brickflow.tf.databricks.job import Job
from brickflow.tf.databricks.pipeline import PipelineCluster, Pipeline

if TYPE_CHECKING:
    from brickflow.engine.project import _Project  # pragma: no cover


def has_tags(node: constructs.IConstruct) -> bool:
    return hasattr(node, "tags") and hasattr(node, "tags_input")


def add_brickflow_tags(node: constructs.IConstruct, other_tags: Dict[str, str]) -> None:
    if has_tags(node) is True:
        node.tags = get_brickflow_tags(node.tags_input, other_tags)


@functools.lru_cache
def get_current_user(stack: TerraformStack) -> DataDatabricksCurrentUser:
    return DataDatabricksCurrentUser(stack, "current_user")


@jsii.implements(IAspect)
class BrickflowTerraformNodeVisitor:
    def __init__(self, project: "_Project", stack: TerraformStack) -> None:
        self._project = project
        self._stack = stack
        self._current_user = get_current_user(self._stack)

    def _modify_names(self, node: constructs.IConstruct) -> None:
        if isinstance(node, (Job, Pipeline)):
            if ctx.is_local() is True:
                node.name = f"{self._current_user.alphanumeric}_{node.name_input}"
            else:
                node.name = f"{ctx.env}_{node.name_input}"

    def visit(self, node: constructs.IConstruct) -> None:
        if isinstance(node, TerraformStack):
            # skip the terraform stack
            return

        self._modify_names(node)

        default_tags = {
            DatabricksDefaultClusterTagKeys.ENVIRONMENT.value: ctx.env,
            DatabricksDefaultClusterTagKeys.DEPLOYED_BY.value: self._current_user.user_name,
            DatabricksDefaultClusterTagKeys.BRICKFLOW_PROJECT_NAME.value: self._project.name,
            DatabricksDefaultClusterTagKeys.DATABRICKS_TF_PROVIDER_VERSION.value: DATABRICKS_TERRAFORM_PROVIDER_VERSION,
            DatabricksDefaultClusterTagKeys.BRICKFLOW_DEPLOYMENT_MODE.value: "CDKTF",
        }

        # pass
        if isinstance(node, Pipeline):
            cluster_input = node.cluster_input[0].__dict__.get("_values", {})
            user_set_tags = cluster_input.get("custom_tags", {})
            new_tags = get_brickflow_tags(user_set_tags, default_tags)
            node.put_cluster(
                [PipelineCluster(**{**cluster_input, **{"custom_tags": new_tags}})]
            )

        # pass
        if isinstance(node, Job):
            add_brickflow_tags(node, default_tags)
