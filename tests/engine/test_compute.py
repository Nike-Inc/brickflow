import pytest

from brickflow.engine.compute import Cluster


class TestCompute:
    def test_autoscale(self):
        workers = 1234
        cluster = Cluster(
            "name", "spark_version", "vm-node", min_workers=workers, max_workers=workers
        )
        assert cluster.autoscale() == {
            "autoscale": {
                "min_workers": workers,
                "max_workers": workers,
            }
        }

        cluster = Cluster("name", "spark_version", "vm-node")
        assert not cluster.autoscale()

    def test_job_task_field(self):
        cluster = Cluster.from_existing_cluster("existing_cluster_id")
        assert cluster.job_task_field_dict == {
            "existing_cluster_id": "existing_cluster_id"
        }
        cluster = Cluster("name", "spark_version", "vm-node")
        assert cluster.job_task_field_dict == {"job_cluster_key": "name"}

    def test_dict(self):
        cluster = Cluster.from_existing_cluster("existing_cluster_id")
        assert "existing_cluster_id" not in cluster.as_dict()

    def test_valid_cluster(self):
        with pytest.raises(AssertionError):
            Cluster(
                "some_name", "some_version", "some_vm", min_workers=8, max_workers=4
            )

        with pytest.raises(AssertionError):
            Cluster(
                "some_name",
                "some_version",
                "some_vm",
                num_workers=3,
                min_workers=2,
                max_workers=4,
            )

        with pytest.raises(AssertionError):
            Cluster("some_name", "some_version", "some_vm", max_workers=4)
