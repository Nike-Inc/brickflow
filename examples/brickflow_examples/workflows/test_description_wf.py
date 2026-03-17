from brickflow import (
    Cluster,
    Workflow,
    ctx,
)

wf = Workflow(
    "test-description-workflow",
    description="This is a test workflow to verify that workflow descriptions are properly deployed and displayed in Databricks.",
    default_cluster=Cluster.from_existing_cluster("<all-purpose-cluster-id>"),
)


@wf.task
def start():
    """Starting task for the test description workflow."""
    print("Test description workflow started!")
    return "Hello from test-description-workflow"


@wf.task(depends_on=start)
def end():
    """Ending task for the test description workflow."""
    print("Test description workflow completed!")
    return "Workflow finished successfully"
