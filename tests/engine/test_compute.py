import pytest

from brickflow.engine.compute import Cluster


class TestCompute:
    def test_autoscale(self):
        workers = 1234
        cluster = Cluster("name", "spark_version", "vm-node", min_workers=workers, max_workers=workers)
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
        assert cluster.job_task_field_dict == {"existing_cluster_id": "existing_cluster_id"}
        cluster = Cluster("name", "spark_version", "vm-node")
        assert cluster.job_task_field_dict == {"job_cluster_key": "name"}

    def test_dict(self):
        cluster = Cluster.from_existing_cluster("existing_cluster_id")
        assert "existing_cluster_id" not in cluster.as_dict()

    def test_valid_cluster(self):
        with pytest.raises(AssertionError):
            Cluster("some_name", "some_version", "some_vm", min_workers=8, max_workers=4)

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

    def test_node_type_or_instance_pool(self):
        assert (
            Cluster(
                "some_name",
                "some_version",
                node_type_id="some_vm",
                driver_node_type_id="other_vm",
            ).node_type_id
            == "some_vm"
        )
        assert (
            Cluster("some_name", "some_version", instance_pool_id="some_instance_pool_id").instance_pool_id
            == "some_instance_pool_id"
        )
        with pytest.raises(AssertionError, match="Must specify either instance_pool_id or node_type_id"):
            Cluster(
                "some_name",
                "some_version",
            )

        with pytest.raises(
            AssertionError,
            match="Cannot specify instance_pool_id if node_type_id has been specified",
        ):
            Cluster(
                "some_name",
                "some_version",
                node_type_id="some_vm",
                instance_pool_id="1234",
            )
        with pytest.raises(
            AssertionError,
            match=(
                "Cannot specify driver_node_type_id if instance_pool_id"
                " or driver_instance_pool_id has been specified"
            ),
        ):
            Cluster(
                "some_name",
                "some_version",
                driver_node_type_id="other_vm",
                instance_pool_id="1234",
            )
        with pytest.raises(
            AssertionError,
            match=(
                "Cannot specify driver_node_type_id if instance_pool_id"
                " or driver_instance_pool_id has been specified"
            ),
        ):
            Cluster(
                "some_name",
                "some_version",
                node_type_id="some_vm",
                driver_node_type_id="other_vm",
                driver_instance_pool_id="1234",
            )
        with pytest.raises(
            AssertionError,
            match=(
                "Cannot specify driver_node_type_id if instance_pool_id"
                " or driver_instance_pool_id has been specified"
            ),
        ):
            Cluster(
                "some_name",
                "some_version",
                driver_node_type_id="other_vm",
                instance_pool_id="1234",
                driver_instance_pool_id="12345",
            )
