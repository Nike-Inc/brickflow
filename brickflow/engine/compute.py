from __future__ import annotations

import dataclasses
import json
from dataclasses import dataclass
from typing import Optional, Dict, Any, List, Literal


class DuplicateClustersDefinitionError(Exception):
    pass


# Not an enum but collection of constants, generated via script
class Runtimes:
    RUNTIME_15_4_X_SCALA2_12_LTS = "15.4.x-scala2.12"
    RUNTIME_15_4_X_PHOTON_SCALA2_12_LTS = "15.4.x-photon-scala2.12"
    RUNTIME_15_4_X_GPU_ML_SCALA2_12_LTS = "15.4.x-gpu-ml-scala2.12"
    RUNTIME_15_4_X_CPU_ML_SCALA2_12_LTS = "15.4.x-cpu-ml-scala2.12"
    RUNTIME_15_4_X_AARCH64_SCALA2_12_LTS = "15.4.x-aarch64-scala2.12"
    RUNTIME_15_4_X_AARCH64_PHOTON_SCALA2_12_LTS = "15.4.x-aarch64-photon-scala2.12"
    RUNTIME_15_3_X_SCALA2_12 = "15.3.x-scala2.12"
    RUNTIME_15_3_X_PHOTON_SCALA2_12 = "15.3.x-photon-scala2.12"
    RUNTIME_15_3_X_GPU_ML_SCALA2_12 = "15.3.x-gpu-ml-scala2.12"
    RUNTIME_15_3_X_CPU_ML_SCALA2_12 = "15.3.x-cpu-ml-scala2.12"
    RUNTIME_15_3_X_AARCH64_SCALA2_12 = "15.3.x-aarch64-scala2.12"
    RUNTIME_15_3_X_AARCH64_PHOTON_SCALA2_12 = "15.3.x-aarch64-photon-scala2.12"
    RUNTIME_15_2_X_SCALA2_12 = "15.2.x-scala2.12"
    RUNTIME_15_2_X_PHOTON_SCALA2_12 = "15.2.x-photon-scala2.12"
    RUNTIME_15_2_X_GPU_ML_SCALA2_12 = "15.2.x-gpu-ml-scala2.12"
    RUNTIME_15_2_X_CPU_ML_SCALA2_12 = "15.2.x-cpu-ml-scala2.12"
    RUNTIME_15_2_X_AARCH64_SCALA2_12 = "15.2.x-aarch64-scala2.12"
    RUNTIME_15_2_X_AARCH64_PHOTON_SCALA2_12 = "15.2.x-aarch64-photon-scala2.12"
    RUNTIME_15_1_X_SCALA2_12 = "15.1.x-scala2.12"
    RUNTIME_15_1_X_PHOTON_SCALA2_12 = "15.1.x-photon-scala2.12"
    RUNTIME_15_1_X_GPU_ML_SCALA2_12 = "15.1.x-gpu-ml-scala2.12"
    RUNTIME_15_1_X_CPU_ML_SCALA2_12 = "15.1.x-cpu-ml-scala2.12"
    RUNTIME_15_1_X_AARCH64_SCALA2_12 = "15.1.x-aarch64-scala2.12"
    RUNTIME_15_1_X_AARCH64_PHOTON_SCALA2_12 = "15.1.x-aarch64-photon-scala2.12"
    RUNTIME_14_3_X_SCALA2_12_LTS = "14.3.x-scala2.12"
    RUNTIME_14_3_X_PHOTON_SCALA2_12_LTS = "14.3.x-photon-scala2.12"
    RUNTIME_14_3_X_GPU_ML_SCALA2_12_LTS = "14.3.x-gpu-ml-scala2.12"
    RUNTIME_14_3_X_CPU_ML_SCALA2_12_LTS = "14.3.x-cpu-ml-scala2.12"
    RUNTIME_14_3_X_AARCH64_SCALA2_12_LTS = "14.3.x-aarch64-scala2.12"
    RUNTIME_14_3_X_AARCH64_PHOTON_SCALA2_12_LTS = "14.3.x-aarch64-photon-scala2.12"
    RUNTIME_14_2_X_SCALA2_12 = "14.2.x-scala2.12"
    RUNTIME_14_2_X_PHOTON_SCALA2_12 = "14.2.x-photon-scala2.12"
    RUNTIME_14_2_X_GPU_ML_SCALA2_12 = "14.2.x-gpu-ml-scala2.12"
    RUNTIME_14_2_X_CPU_ML_SCALA2_12 = "14.2.x-cpu-ml-scala2.12"
    RUNTIME_14_2_X_AARCH64_SCALA2_12 = "14.2.x-aarch64-scala2.12"
    RUNTIME_14_2_X_AARCH64_PHOTON_SCALA2_12 = "14.2.x-aarch64-photon-scala2.12"
    RUNTIME_14_1_X_SCALA2_12 = "14.1.x-scala2.12"
    RUNTIME_14_1_X_PHOTON_SCALA2_12 = "14.1.x-photon-scala2.12"
    RUNTIME_14_1_X_GPU_ML_SCALA2_12 = "14.1.x-gpu-ml-scala2.12"
    RUNTIME_14_1_X_CPU_ML_SCALA2_12 = "14.1.x-cpu-ml-scala2.12"
    RUNTIME_14_1_X_AARCH64_SCALA2_12 = "14.1.x-aarch64-scala2.12"
    RUNTIME_14_1_X_AARCH64_PHOTON_SCALA2_12 = "14.1.x-aarch64-photon-scala2.12"
    RUNTIME_11_3_X_SCALA2_12 = "11.3.x-scala2.12"
    RUNTIME_11_3_X_PHOTON_SCALA2_12 = "11.3.x-photon-scala2.12"
    RUNTIME_11_3_X_GPU_ML_SCALA2_12 = "11.3.x-gpu-ml-scala2.12"
    RUNTIME_11_3_X_CPU_ML_SCALA2_12 = "11.3.x-cpu-ml-scala2.12"
    RUNTIME_11_3_X_AARCH64_SCALA2_12 = "11.3.x-aarch64-scala2.12"
    RUNTIME_11_3_X_AARCH64_PHOTON_SCALA2_12 = "11.3.x-aarch64-photon-scala2.12"
    RUNTIME_11_2_X_SCALA2_12 = "11.2.x-scala2.12"
    RUNTIME_11_2_X_PHOTON_SCALA2_12 = "11.2.x-photon-scala2.12"
    RUNTIME_11_2_X_GPU_ML_SCALA2_12 = "11.2.x-gpu-ml-scala2.12"
    RUNTIME_11_2_X_CPU_ML_SCALA2_12 = "11.2.x-cpu-ml-scala2.12"
    RUNTIME_11_2_X_AARCH64_SCALA2_12 = "11.2.x-aarch64-scala2.12"
    RUNTIME_11_2_X_AARCH64_PHOTON_SCALA2_12 = "11.2.x-aarch64-photon-scala2.12"
    RUNTIME_11_1_X_SCALA2_12 = "11.1.x-scala2.12"
    RUNTIME_11_1_X_PHOTON_SCALA2_12 = "11.1.x-photon-scala2.12"
    RUNTIME_11_1_X_GPU_ML_SCALA2_12 = "11.1.x-gpu-ml-scala2.12"
    RUNTIME_11_1_X_CPU_ML_SCALA2_12 = "11.1.x-cpu-ml-scala2.12"
    RUNTIME_11_1_X_AARCH64_SCALA2_12 = "11.1.x-aarch64-scala2.12"
    RUNTIME_11_1_X_AARCH64_PHOTON_SCALA2_12 = "11.1.x-aarch64-photon-scala2.12"
    RUNTIME_11_0_X_SCALA2_12 = "11.0.x-scala2.12"
    RUNTIME_11_0_X_PHOTON_SCALA2_12 = "11.0.x-photon-scala2.12"
    RUNTIME_11_0_X_GPU_ML_SCALA2_12 = "11.0.x-gpu-ml-scala2.12"
    RUNTIME_11_0_X_CPU_ML_SCALA2_12 = "11.0.x-cpu-ml-scala2.12"
    RUNTIME_11_0_X_AARCH64_SCALA2_12 = "11.0.x-aarch64-scala2.12"
    RUNTIME_11_0_X_AARCH64_PHOTON_SCALA2_12 = "11.0.x-aarch64-photon-scala2.12"
    RUNTIME_10_5_X_SCALA2_12 = "10.5.x-scala2.12"
    RUNTIME_10_5_X_PHOTON_SCALA2_12 = "10.5.x-photon-scala2.12"
    RUNTIME_10_5_X_GPU_ML_SCALA2_12 = "10.5.x-gpu-ml-scala2.12"
    RUNTIME_10_5_X_CPU_ML_SCALA2_12 = "10.5.x-cpu-ml-scala2.12"
    RUNTIME_10_5_X_AARCH64_SCALA2_12 = "10.5.x-aarch64-scala2.12"
    RUNTIME_10_5_X_AARCH64_PHOTON_SCALA2_12 = "10.5.x-aarch64-photon-scala2.12"
    RUNTIME_10_4_X_SCALA2_12_LTS = "10.4.x-scala2.12"
    RUNTIME_10_4_X_PHOTON_SCALA2_12_LTS = "10.4.x-photon-scala2.12"
    RUNTIME_10_4_X_GPU_ML_SCALA2_12_LTS = "10.4.x-gpu-ml-scala2.12"
    RUNTIME_10_4_X_CPU_ML_SCALA2_12_LTS = "10.4.x-cpu-ml-scala2.12"
    RUNTIME_10_4_X_AARCH64_SCALA2_12_LTS = "10.4.x-aarch64-scala2.12"
    RUNTIME_10_4_X_AARCH64_PHOTON_SCALA2_12_LTS = "10.4.x-aarch64-photon-scala2.12"
    RUNTIME_9_1_X_SCALA2_12_LTS = "9.1.x-scala2.12"
    RUNTIME_9_1_X_PHOTON_SCALA2_12_LTS = "9.1.x-photon-scala2.12"
    RUNTIME_9_1_X_GPU_ML_SCALA2_12_LTS = "9.1.x-gpu-ml-scala2.12"
    RUNTIME_9_1_X_CPU_ML_SCALA2_12_LTS = "9.1.x-cpu-ml-scala2.12"
    RUNTIME_9_1_X_AARCH64_SCALA2_12_LTS = "9.1.x-aarch64-scala2.12"
    RUNTIME_7_3_X_SCALA2_12_LTS = "7.3.x-scala2.12"
    RUNTIME_7_3_X_HLS_SCALA2_12_LTS = "7.3.x-hls-scala2.12"
    RUNTIME_7_3_X_GPU_ML_SCALA2_12_LTS = "7.3.x-gpu-ml-scala2.12"
    RUNTIME_7_3_X_CPU_ML_SCALA2_12_LTS = "7.3.x-cpu-ml-scala2.12"


@dataclass(frozen=True)
class DataSecurityMode:
    SINGLE_USER: str = "SINGLE_USER"


@dataclass(eq=True, frozen=True)
class Cluster:
    name: str
    spark_version: str
    node_type_id: Optional[str] = None
    data_security_mode: str = DataSecurityMode.SINGLE_USER
    existing_cluster_id: Optional[str] = None
    num_workers: Optional[int] = None
    min_workers: Optional[int] = None
    max_workers: Optional[int] = None
    dlt_auto_scale_mode: Optional[str] = None  # only used for DLT
    spark_conf: Optional[Dict[str, str]] = None
    aws_attributes: Optional[Dict[str, Any]] = None
    driver_node_type_id: Optional[str] = None
    custom_tags: Optional[Dict[str, str]] = None
    init_scripts: Optional[List[Dict[str, str]]] = None
    spark_env_vars: Optional[Dict[str, str]] = None
    enable_elastic_disk: Optional[bool] = None
    driver_instance_pool_id: Optional[str] = None
    instance_pool_id: Optional[str] = None
    runtime_engine: Optional[Literal["STANDARD", "PHOTON"]] = None
    policy_id: Optional[str] = None

    def __hash__(self) -> int:
        # dedupe dicts and lists which are default un hashable. Easiest way to identify dupes.
        return hash(json.dumps(self.as_dict()))

    def validate(self) -> None:
        assert not (
            self.num_workers is not None
            and self.min_workers is not None
            and self.max_workers is not None
        ), "Num workers should not be provided with min and max workers"
        assert not (
            (self.min_workers is None and self.max_workers is not None)
            or (self.min_workers is not None and self.max_workers is None)
        ), "Both min workers and max workers should be present if one is provided"
        # noinspection PyTypeChecker
        assert not (
            (self.min_workers is not None and self.max_workers is not None)
            and (self.min_workers > self.max_workers)
        ), "Min workers should be less than max workers"
        assert not (
            self.instance_pool_id is None and self.node_type_id is None
        ), "Must specify either instance_pool_id or node_type_id"
        assert not (
            self.instance_pool_id is not None and self.node_type_id is not None
        ), "Cannot specify instance_pool_id if node_type_id has been specified"
        assert not (
            (self.driver_node_type_id is not None)
            and (
                self.instance_pool_id is not None
                or self.driver_instance_pool_id is not None
            )
        ), "Cannot specify driver_node_type_id if instance_pool_id or driver_instance_pool_id has been specified"

    def __post_init__(self) -> None:
        self.validate()

    @classmethod
    def from_existing_cluster(cls, existing_cluster_id: str) -> "Cluster":
        # just some stub value
        return Cluster(
            existing_cluster_id,
            existing_cluster_id,
            existing_cluster_id,
            existing_cluster_id=existing_cluster_id,
        )

    @property
    def is_new_job_cluster(self) -> bool:
        return self.existing_cluster_id is None

    def autoscale(self, is_dlt_cluster: bool = False) -> Dict[str, Any]:
        if self.min_workers is not None and self.max_workers is not None:
            resp: Dict[str, Dict[str, Optional[str | int]]] = {
                "autoscale": {
                    "min_workers": self.min_workers,
                    "max_workers": self.max_workers,
                }
            }
            if is_dlt_cluster is True:
                resp["autoscale"]["mode"] = self.dlt_auto_scale_mode
            return resp
        return {}

    @property
    def job_task_field_dict(self) -> Dict[str, str]:
        if self.existing_cluster_id is not None:
            return {"existing_cluster_id": self.existing_cluster_id}
        return {"job_cluster_key": self.name}

    @staticmethod
    def cleanup(
        d: Dict[str, Any],
        allowed_fields: Optional[List[str]] = None,
        remove_fields: Optional[List[str]] = None,
    ) -> None:
        d.pop("min_workers", None)
        d.pop("max_workers", None)
        d.pop("dlt_auto_scale_mode", None)
        d.pop("existing_cluster_id", None)
        remove_fields = remove_fields or []
        for k in list(d.keys()):
            # if allowed fields are provided and check if value is in set
            if allowed_fields and k not in allowed_fields:
                d.pop(k, None)
            if k in remove_fields:
                d.pop(k, None)

    def as_dict(
        self,
        is_dlt_cluster: bool = False,
        allowed_fields: Optional[List[str]] = None,
        remove_fields: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        d = dataclasses.asdict(self)
        d = {**d, **self.autoscale(is_dlt_cluster=is_dlt_cluster)}
        # if allowed fields are provided and check if value is in set
        self.cleanup(d, allowed_fields=allowed_fields, remove_fields=remove_fields)
        return d
