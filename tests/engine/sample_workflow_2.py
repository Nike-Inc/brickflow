from brickflow import Cluster, Workflow

wf = Workflow("test1", default_cluster=Cluster.from_existing_cluster("existing_cluster_id"))


@wf.task()
def task_function(*, test="var"):
    return test
