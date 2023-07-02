'''
# `data_databricks_cluster`

Refer to the Terraform Registory for docs: [`data_databricks_cluster`](https://www.terraform.io/docs/providers/databricks/d/cluster).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class DataDatabricksCluster(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/d/cluster databricks_cluster}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        cluster_id: typing.Optional[builtins.str] = None,
        cluster_info: typing.Optional[typing.Union["DataDatabricksClusterClusterInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/d/cluster databricks_cluster} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_id DataDatabricksCluster#cluster_id}.
        :param cluster_info: cluster_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_info DataDatabricksCluster#cluster_info}
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_name DataDatabricksCluster#cluster_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#id DataDatabricksCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1c34b6757ec75a7e345694812782e8b53d0c659ffbbb23408d5fb560269d735)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataDatabricksClusterConfig(
            cluster_id=cluster_id,
            cluster_info=cluster_info,
            cluster_name=cluster_name,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putClusterInfo")
    def put_cluster_info(
        self,
        *,
        default_tags: typing.Mapping[builtins.str, builtins.str],
        spark_version: builtins.str,
        state: builtins.str,
        autoscale: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoAutoscale", typing.Dict[builtins.str, typing.Any]]] = None,
        autotermination_minutes: typing.Optional[jsii.Number] = None,
        aws_attributes: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoAwsAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_attributes: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoAzureAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_cores: typing.Optional[jsii.Number] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        cluster_log_conf: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoClusterLogConf", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_log_status: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoClusterLogStatus", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_memory_mb: typing.Optional[jsii.Number] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        cluster_source: typing.Optional[builtins.str] = None,
        creator_user_name: typing.Optional[builtins.str] = None,
        custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        data_security_mode: typing.Optional[builtins.str] = None,
        docker_image: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoDockerImage", typing.Dict[builtins.str, typing.Any]]] = None,
        driver: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoDriver", typing.Dict[builtins.str, typing.Any]]] = None,
        driver_instance_pool_id: typing.Optional[builtins.str] = None,
        driver_node_type_id: typing.Optional[builtins.str] = None,
        enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_local_disk_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        executors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksClusterClusterInfoExecutors", typing.Dict[builtins.str, typing.Any]]]]] = None,
        gcp_attributes: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoGcpAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        init_scripts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksClusterClusterInfoInitScripts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        instance_pool_id: typing.Optional[builtins.str] = None,
        jdbc_port: typing.Optional[jsii.Number] = None,
        last_activity_time: typing.Optional[jsii.Number] = None,
        last_state_loss_time: typing.Optional[jsii.Number] = None,
        node_type_id: typing.Optional[builtins.str] = None,
        num_workers: typing.Optional[jsii.Number] = None,
        policy_id: typing.Optional[builtins.str] = None,
        runtime_engine: typing.Optional[builtins.str] = None,
        single_user_name: typing.Optional[builtins.str] = None,
        spark_conf: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        spark_context_id: typing.Optional[jsii.Number] = None,
        spark_env_vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        start_time: typing.Optional[jsii.Number] = None,
        state_message: typing.Optional[builtins.str] = None,
        terminate_time: typing.Optional[jsii.Number] = None,
        termination_reason: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoTerminationReason", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param default_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#default_tags DataDatabricksCluster#default_tags}.
        :param spark_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_version DataDatabricksCluster#spark_version}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#state DataDatabricksCluster#state}.
        :param autoscale: autoscale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#autoscale DataDatabricksCluster#autoscale}
        :param autotermination_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#autotermination_minutes DataDatabricksCluster#autotermination_minutes}.
        :param aws_attributes: aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#aws_attributes DataDatabricksCluster#aws_attributes}
        :param azure_attributes: azure_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#azure_attributes DataDatabricksCluster#azure_attributes}
        :param cluster_cores: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_cores DataDatabricksCluster#cluster_cores}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_id DataDatabricksCluster#cluster_id}.
        :param cluster_log_conf: cluster_log_conf block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_log_conf DataDatabricksCluster#cluster_log_conf}
        :param cluster_log_status: cluster_log_status block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_log_status DataDatabricksCluster#cluster_log_status}
        :param cluster_memory_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_memory_mb DataDatabricksCluster#cluster_memory_mb}.
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_name DataDatabricksCluster#cluster_name}.
        :param cluster_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_source DataDatabricksCluster#cluster_source}.
        :param creator_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#creator_user_name DataDatabricksCluster#creator_user_name}.
        :param custom_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#custom_tags DataDatabricksCluster#custom_tags}.
        :param data_security_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#data_security_mode DataDatabricksCluster#data_security_mode}.
        :param docker_image: docker_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#docker_image DataDatabricksCluster#docker_image}
        :param driver: driver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver DataDatabricksCluster#driver}
        :param driver_instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver_instance_pool_id DataDatabricksCluster#driver_instance_pool_id}.
        :param driver_node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver_node_type_id DataDatabricksCluster#driver_node_type_id}.
        :param enable_elastic_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_elastic_disk DataDatabricksCluster#enable_elastic_disk}.
        :param enable_local_disk_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_local_disk_encryption DataDatabricksCluster#enable_local_disk_encryption}.
        :param executors: executors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#executors DataDatabricksCluster#executors}
        :param gcp_attributes: gcp_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#gcp_attributes DataDatabricksCluster#gcp_attributes}
        :param init_scripts: init_scripts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#init_scripts DataDatabricksCluster#init_scripts}
        :param instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_pool_id DataDatabricksCluster#instance_pool_id}.
        :param jdbc_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#jdbc_port DataDatabricksCluster#jdbc_port}.
        :param last_activity_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_activity_time DataDatabricksCluster#last_activity_time}.
        :param last_state_loss_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_state_loss_time DataDatabricksCluster#last_state_loss_time}.
        :param node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_type_id DataDatabricksCluster#node_type_id}.
        :param num_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#num_workers DataDatabricksCluster#num_workers}.
        :param policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#policy_id DataDatabricksCluster#policy_id}.
        :param runtime_engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#runtime_engine DataDatabricksCluster#runtime_engine}.
        :param single_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#single_user_name DataDatabricksCluster#single_user_name}.
        :param spark_conf: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_conf DataDatabricksCluster#spark_conf}.
        :param spark_context_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_context_id DataDatabricksCluster#spark_context_id}.
        :param spark_env_vars: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_env_vars DataDatabricksCluster#spark_env_vars}.
        :param ssh_public_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ssh_public_keys DataDatabricksCluster#ssh_public_keys}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#start_time DataDatabricksCluster#start_time}.
        :param state_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#state_message DataDatabricksCluster#state_message}.
        :param terminate_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#terminate_time DataDatabricksCluster#terminate_time}.
        :param termination_reason: termination_reason block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#termination_reason DataDatabricksCluster#termination_reason}
        '''
        value = DataDatabricksClusterClusterInfo(
            default_tags=default_tags,
            spark_version=spark_version,
            state=state,
            autoscale=autoscale,
            autotermination_minutes=autotermination_minutes,
            aws_attributes=aws_attributes,
            azure_attributes=azure_attributes,
            cluster_cores=cluster_cores,
            cluster_id=cluster_id,
            cluster_log_conf=cluster_log_conf,
            cluster_log_status=cluster_log_status,
            cluster_memory_mb=cluster_memory_mb,
            cluster_name=cluster_name,
            cluster_source=cluster_source,
            creator_user_name=creator_user_name,
            custom_tags=custom_tags,
            data_security_mode=data_security_mode,
            docker_image=docker_image,
            driver=driver,
            driver_instance_pool_id=driver_instance_pool_id,
            driver_node_type_id=driver_node_type_id,
            enable_elastic_disk=enable_elastic_disk,
            enable_local_disk_encryption=enable_local_disk_encryption,
            executors=executors,
            gcp_attributes=gcp_attributes,
            init_scripts=init_scripts,
            instance_pool_id=instance_pool_id,
            jdbc_port=jdbc_port,
            last_activity_time=last_activity_time,
            last_state_loss_time=last_state_loss_time,
            node_type_id=node_type_id,
            num_workers=num_workers,
            policy_id=policy_id,
            runtime_engine=runtime_engine,
            single_user_name=single_user_name,
            spark_conf=spark_conf,
            spark_context_id=spark_context_id,
            spark_env_vars=spark_env_vars,
            ssh_public_keys=ssh_public_keys,
            start_time=start_time,
            state_message=state_message,
            terminate_time=terminate_time,
            termination_reason=termination_reason,
        )

        return typing.cast(None, jsii.invoke(self, "putClusterInfo", [value]))

    @jsii.member(jsii_name="resetClusterId")
    def reset_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterId", []))

    @jsii.member(jsii_name="resetClusterInfo")
    def reset_cluster_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterInfo", []))

    @jsii.member(jsii_name="resetClusterName")
    def reset_cluster_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="clusterInfo")
    def cluster_info(self) -> "DataDatabricksClusterClusterInfoOutputReference":
        return typing.cast("DataDatabricksClusterClusterInfoOutputReference", jsii.get(self, "clusterInfo"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterInfoInput")
    def cluster_info_input(self) -> typing.Optional["DataDatabricksClusterClusterInfo"]:
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfo"], jsii.get(self, "clusterInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterNameInput")
    def cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1362b5c144022c4061f55358a67328d0bfdb54fa18ca548a90a41457417ed814)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaac8b5d6ffc42289a6393bd5bb7aecf591a05d7fdabffed88a8e77014688a03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__966dd3e8ead2ea020bea9709d896fa618505ab438e8c09f91c442f59713092b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfo",
    jsii_struct_bases=[],
    name_mapping={
        "default_tags": "defaultTags",
        "spark_version": "sparkVersion",
        "state": "state",
        "autoscale": "autoscale",
        "autotermination_minutes": "autoterminationMinutes",
        "aws_attributes": "awsAttributes",
        "azure_attributes": "azureAttributes",
        "cluster_cores": "clusterCores",
        "cluster_id": "clusterId",
        "cluster_log_conf": "clusterLogConf",
        "cluster_log_status": "clusterLogStatus",
        "cluster_memory_mb": "clusterMemoryMb",
        "cluster_name": "clusterName",
        "cluster_source": "clusterSource",
        "creator_user_name": "creatorUserName",
        "custom_tags": "customTags",
        "data_security_mode": "dataSecurityMode",
        "docker_image": "dockerImage",
        "driver": "driver",
        "driver_instance_pool_id": "driverInstancePoolId",
        "driver_node_type_id": "driverNodeTypeId",
        "enable_elastic_disk": "enableElasticDisk",
        "enable_local_disk_encryption": "enableLocalDiskEncryption",
        "executors": "executors",
        "gcp_attributes": "gcpAttributes",
        "init_scripts": "initScripts",
        "instance_pool_id": "instancePoolId",
        "jdbc_port": "jdbcPort",
        "last_activity_time": "lastActivityTime",
        "last_state_loss_time": "lastStateLossTime",
        "node_type_id": "nodeTypeId",
        "num_workers": "numWorkers",
        "policy_id": "policyId",
        "runtime_engine": "runtimeEngine",
        "single_user_name": "singleUserName",
        "spark_conf": "sparkConf",
        "spark_context_id": "sparkContextId",
        "spark_env_vars": "sparkEnvVars",
        "ssh_public_keys": "sshPublicKeys",
        "start_time": "startTime",
        "state_message": "stateMessage",
        "terminate_time": "terminateTime",
        "termination_reason": "terminationReason",
    },
)
class DataDatabricksClusterClusterInfo:
    def __init__(
        self,
        *,
        default_tags: typing.Mapping[builtins.str, builtins.str],
        spark_version: builtins.str,
        state: builtins.str,
        autoscale: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoAutoscale", typing.Dict[builtins.str, typing.Any]]] = None,
        autotermination_minutes: typing.Optional[jsii.Number] = None,
        aws_attributes: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoAwsAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_attributes: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoAzureAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_cores: typing.Optional[jsii.Number] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        cluster_log_conf: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoClusterLogConf", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_log_status: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoClusterLogStatus", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_memory_mb: typing.Optional[jsii.Number] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        cluster_source: typing.Optional[builtins.str] = None,
        creator_user_name: typing.Optional[builtins.str] = None,
        custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        data_security_mode: typing.Optional[builtins.str] = None,
        docker_image: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoDockerImage", typing.Dict[builtins.str, typing.Any]]] = None,
        driver: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoDriver", typing.Dict[builtins.str, typing.Any]]] = None,
        driver_instance_pool_id: typing.Optional[builtins.str] = None,
        driver_node_type_id: typing.Optional[builtins.str] = None,
        enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_local_disk_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        executors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksClusterClusterInfoExecutors", typing.Dict[builtins.str, typing.Any]]]]] = None,
        gcp_attributes: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoGcpAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        init_scripts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksClusterClusterInfoInitScripts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        instance_pool_id: typing.Optional[builtins.str] = None,
        jdbc_port: typing.Optional[jsii.Number] = None,
        last_activity_time: typing.Optional[jsii.Number] = None,
        last_state_loss_time: typing.Optional[jsii.Number] = None,
        node_type_id: typing.Optional[builtins.str] = None,
        num_workers: typing.Optional[jsii.Number] = None,
        policy_id: typing.Optional[builtins.str] = None,
        runtime_engine: typing.Optional[builtins.str] = None,
        single_user_name: typing.Optional[builtins.str] = None,
        spark_conf: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        spark_context_id: typing.Optional[jsii.Number] = None,
        spark_env_vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        start_time: typing.Optional[jsii.Number] = None,
        state_message: typing.Optional[builtins.str] = None,
        terminate_time: typing.Optional[jsii.Number] = None,
        termination_reason: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoTerminationReason", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param default_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#default_tags DataDatabricksCluster#default_tags}.
        :param spark_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_version DataDatabricksCluster#spark_version}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#state DataDatabricksCluster#state}.
        :param autoscale: autoscale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#autoscale DataDatabricksCluster#autoscale}
        :param autotermination_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#autotermination_minutes DataDatabricksCluster#autotermination_minutes}.
        :param aws_attributes: aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#aws_attributes DataDatabricksCluster#aws_attributes}
        :param azure_attributes: azure_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#azure_attributes DataDatabricksCluster#azure_attributes}
        :param cluster_cores: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_cores DataDatabricksCluster#cluster_cores}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_id DataDatabricksCluster#cluster_id}.
        :param cluster_log_conf: cluster_log_conf block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_log_conf DataDatabricksCluster#cluster_log_conf}
        :param cluster_log_status: cluster_log_status block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_log_status DataDatabricksCluster#cluster_log_status}
        :param cluster_memory_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_memory_mb DataDatabricksCluster#cluster_memory_mb}.
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_name DataDatabricksCluster#cluster_name}.
        :param cluster_source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_source DataDatabricksCluster#cluster_source}.
        :param creator_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#creator_user_name DataDatabricksCluster#creator_user_name}.
        :param custom_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#custom_tags DataDatabricksCluster#custom_tags}.
        :param data_security_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#data_security_mode DataDatabricksCluster#data_security_mode}.
        :param docker_image: docker_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#docker_image DataDatabricksCluster#docker_image}
        :param driver: driver block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver DataDatabricksCluster#driver}
        :param driver_instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver_instance_pool_id DataDatabricksCluster#driver_instance_pool_id}.
        :param driver_node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver_node_type_id DataDatabricksCluster#driver_node_type_id}.
        :param enable_elastic_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_elastic_disk DataDatabricksCluster#enable_elastic_disk}.
        :param enable_local_disk_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_local_disk_encryption DataDatabricksCluster#enable_local_disk_encryption}.
        :param executors: executors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#executors DataDatabricksCluster#executors}
        :param gcp_attributes: gcp_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#gcp_attributes DataDatabricksCluster#gcp_attributes}
        :param init_scripts: init_scripts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#init_scripts DataDatabricksCluster#init_scripts}
        :param instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_pool_id DataDatabricksCluster#instance_pool_id}.
        :param jdbc_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#jdbc_port DataDatabricksCluster#jdbc_port}.
        :param last_activity_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_activity_time DataDatabricksCluster#last_activity_time}.
        :param last_state_loss_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_state_loss_time DataDatabricksCluster#last_state_loss_time}.
        :param node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_type_id DataDatabricksCluster#node_type_id}.
        :param num_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#num_workers DataDatabricksCluster#num_workers}.
        :param policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#policy_id DataDatabricksCluster#policy_id}.
        :param runtime_engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#runtime_engine DataDatabricksCluster#runtime_engine}.
        :param single_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#single_user_name DataDatabricksCluster#single_user_name}.
        :param spark_conf: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_conf DataDatabricksCluster#spark_conf}.
        :param spark_context_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_context_id DataDatabricksCluster#spark_context_id}.
        :param spark_env_vars: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_env_vars DataDatabricksCluster#spark_env_vars}.
        :param ssh_public_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ssh_public_keys DataDatabricksCluster#ssh_public_keys}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#start_time DataDatabricksCluster#start_time}.
        :param state_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#state_message DataDatabricksCluster#state_message}.
        :param terminate_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#terminate_time DataDatabricksCluster#terminate_time}.
        :param termination_reason: termination_reason block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#termination_reason DataDatabricksCluster#termination_reason}
        '''
        if isinstance(autoscale, dict):
            autoscale = DataDatabricksClusterClusterInfoAutoscale(**autoscale)
        if isinstance(aws_attributes, dict):
            aws_attributes = DataDatabricksClusterClusterInfoAwsAttributes(**aws_attributes)
        if isinstance(azure_attributes, dict):
            azure_attributes = DataDatabricksClusterClusterInfoAzureAttributes(**azure_attributes)
        if isinstance(cluster_log_conf, dict):
            cluster_log_conf = DataDatabricksClusterClusterInfoClusterLogConf(**cluster_log_conf)
        if isinstance(cluster_log_status, dict):
            cluster_log_status = DataDatabricksClusterClusterInfoClusterLogStatus(**cluster_log_status)
        if isinstance(docker_image, dict):
            docker_image = DataDatabricksClusterClusterInfoDockerImage(**docker_image)
        if isinstance(driver, dict):
            driver = DataDatabricksClusterClusterInfoDriver(**driver)
        if isinstance(gcp_attributes, dict):
            gcp_attributes = DataDatabricksClusterClusterInfoGcpAttributes(**gcp_attributes)
        if isinstance(termination_reason, dict):
            termination_reason = DataDatabricksClusterClusterInfoTerminationReason(**termination_reason)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__296ce555691258d87ac7958787edcb938924edb40d4f8f66eef6bb634906db09)
            check_type(argname="argument default_tags", value=default_tags, expected_type=type_hints["default_tags"])
            check_type(argname="argument spark_version", value=spark_version, expected_type=type_hints["spark_version"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument autoscale", value=autoscale, expected_type=type_hints["autoscale"])
            check_type(argname="argument autotermination_minutes", value=autotermination_minutes, expected_type=type_hints["autotermination_minutes"])
            check_type(argname="argument aws_attributes", value=aws_attributes, expected_type=type_hints["aws_attributes"])
            check_type(argname="argument azure_attributes", value=azure_attributes, expected_type=type_hints["azure_attributes"])
            check_type(argname="argument cluster_cores", value=cluster_cores, expected_type=type_hints["cluster_cores"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument cluster_log_conf", value=cluster_log_conf, expected_type=type_hints["cluster_log_conf"])
            check_type(argname="argument cluster_log_status", value=cluster_log_status, expected_type=type_hints["cluster_log_status"])
            check_type(argname="argument cluster_memory_mb", value=cluster_memory_mb, expected_type=type_hints["cluster_memory_mb"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument cluster_source", value=cluster_source, expected_type=type_hints["cluster_source"])
            check_type(argname="argument creator_user_name", value=creator_user_name, expected_type=type_hints["creator_user_name"])
            check_type(argname="argument custom_tags", value=custom_tags, expected_type=type_hints["custom_tags"])
            check_type(argname="argument data_security_mode", value=data_security_mode, expected_type=type_hints["data_security_mode"])
            check_type(argname="argument docker_image", value=docker_image, expected_type=type_hints["docker_image"])
            check_type(argname="argument driver", value=driver, expected_type=type_hints["driver"])
            check_type(argname="argument driver_instance_pool_id", value=driver_instance_pool_id, expected_type=type_hints["driver_instance_pool_id"])
            check_type(argname="argument driver_node_type_id", value=driver_node_type_id, expected_type=type_hints["driver_node_type_id"])
            check_type(argname="argument enable_elastic_disk", value=enable_elastic_disk, expected_type=type_hints["enable_elastic_disk"])
            check_type(argname="argument enable_local_disk_encryption", value=enable_local_disk_encryption, expected_type=type_hints["enable_local_disk_encryption"])
            check_type(argname="argument executors", value=executors, expected_type=type_hints["executors"])
            check_type(argname="argument gcp_attributes", value=gcp_attributes, expected_type=type_hints["gcp_attributes"])
            check_type(argname="argument init_scripts", value=init_scripts, expected_type=type_hints["init_scripts"])
            check_type(argname="argument instance_pool_id", value=instance_pool_id, expected_type=type_hints["instance_pool_id"])
            check_type(argname="argument jdbc_port", value=jdbc_port, expected_type=type_hints["jdbc_port"])
            check_type(argname="argument last_activity_time", value=last_activity_time, expected_type=type_hints["last_activity_time"])
            check_type(argname="argument last_state_loss_time", value=last_state_loss_time, expected_type=type_hints["last_state_loss_time"])
            check_type(argname="argument node_type_id", value=node_type_id, expected_type=type_hints["node_type_id"])
            check_type(argname="argument num_workers", value=num_workers, expected_type=type_hints["num_workers"])
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
            check_type(argname="argument runtime_engine", value=runtime_engine, expected_type=type_hints["runtime_engine"])
            check_type(argname="argument single_user_name", value=single_user_name, expected_type=type_hints["single_user_name"])
            check_type(argname="argument spark_conf", value=spark_conf, expected_type=type_hints["spark_conf"])
            check_type(argname="argument spark_context_id", value=spark_context_id, expected_type=type_hints["spark_context_id"])
            check_type(argname="argument spark_env_vars", value=spark_env_vars, expected_type=type_hints["spark_env_vars"])
            check_type(argname="argument ssh_public_keys", value=ssh_public_keys, expected_type=type_hints["ssh_public_keys"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument state_message", value=state_message, expected_type=type_hints["state_message"])
            check_type(argname="argument terminate_time", value=terminate_time, expected_type=type_hints["terminate_time"])
            check_type(argname="argument termination_reason", value=termination_reason, expected_type=type_hints["termination_reason"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_tags": default_tags,
            "spark_version": spark_version,
            "state": state,
        }
        if autoscale is not None:
            self._values["autoscale"] = autoscale
        if autotermination_minutes is not None:
            self._values["autotermination_minutes"] = autotermination_minutes
        if aws_attributes is not None:
            self._values["aws_attributes"] = aws_attributes
        if azure_attributes is not None:
            self._values["azure_attributes"] = azure_attributes
        if cluster_cores is not None:
            self._values["cluster_cores"] = cluster_cores
        if cluster_id is not None:
            self._values["cluster_id"] = cluster_id
        if cluster_log_conf is not None:
            self._values["cluster_log_conf"] = cluster_log_conf
        if cluster_log_status is not None:
            self._values["cluster_log_status"] = cluster_log_status
        if cluster_memory_mb is not None:
            self._values["cluster_memory_mb"] = cluster_memory_mb
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if cluster_source is not None:
            self._values["cluster_source"] = cluster_source
        if creator_user_name is not None:
            self._values["creator_user_name"] = creator_user_name
        if custom_tags is not None:
            self._values["custom_tags"] = custom_tags
        if data_security_mode is not None:
            self._values["data_security_mode"] = data_security_mode
        if docker_image is not None:
            self._values["docker_image"] = docker_image
        if driver is not None:
            self._values["driver"] = driver
        if driver_instance_pool_id is not None:
            self._values["driver_instance_pool_id"] = driver_instance_pool_id
        if driver_node_type_id is not None:
            self._values["driver_node_type_id"] = driver_node_type_id
        if enable_elastic_disk is not None:
            self._values["enable_elastic_disk"] = enable_elastic_disk
        if enable_local_disk_encryption is not None:
            self._values["enable_local_disk_encryption"] = enable_local_disk_encryption
        if executors is not None:
            self._values["executors"] = executors
        if gcp_attributes is not None:
            self._values["gcp_attributes"] = gcp_attributes
        if init_scripts is not None:
            self._values["init_scripts"] = init_scripts
        if instance_pool_id is not None:
            self._values["instance_pool_id"] = instance_pool_id
        if jdbc_port is not None:
            self._values["jdbc_port"] = jdbc_port
        if last_activity_time is not None:
            self._values["last_activity_time"] = last_activity_time
        if last_state_loss_time is not None:
            self._values["last_state_loss_time"] = last_state_loss_time
        if node_type_id is not None:
            self._values["node_type_id"] = node_type_id
        if num_workers is not None:
            self._values["num_workers"] = num_workers
        if policy_id is not None:
            self._values["policy_id"] = policy_id
        if runtime_engine is not None:
            self._values["runtime_engine"] = runtime_engine
        if single_user_name is not None:
            self._values["single_user_name"] = single_user_name
        if spark_conf is not None:
            self._values["spark_conf"] = spark_conf
        if spark_context_id is not None:
            self._values["spark_context_id"] = spark_context_id
        if spark_env_vars is not None:
            self._values["spark_env_vars"] = spark_env_vars
        if ssh_public_keys is not None:
            self._values["ssh_public_keys"] = ssh_public_keys
        if start_time is not None:
            self._values["start_time"] = start_time
        if state_message is not None:
            self._values["state_message"] = state_message
        if terminate_time is not None:
            self._values["terminate_time"] = terminate_time
        if termination_reason is not None:
            self._values["termination_reason"] = termination_reason

    @builtins.property
    def default_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#default_tags DataDatabricksCluster#default_tags}.'''
        result = self._values.get("default_tags")
        assert result is not None, "Required property 'default_tags' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def spark_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_version DataDatabricksCluster#spark_version}.'''
        result = self._values.get("spark_version")
        assert result is not None, "Required property 'spark_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def state(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#state DataDatabricksCluster#state}.'''
        result = self._values.get("state")
        assert result is not None, "Required property 'state' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def autoscale(self) -> typing.Optional["DataDatabricksClusterClusterInfoAutoscale"]:
        '''autoscale block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#autoscale DataDatabricksCluster#autoscale}
        '''
        result = self._values.get("autoscale")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoAutoscale"], result)

    @builtins.property
    def autotermination_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#autotermination_minutes DataDatabricksCluster#autotermination_minutes}.'''
        result = self._values.get("autotermination_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def aws_attributes(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoAwsAttributes"]:
        '''aws_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#aws_attributes DataDatabricksCluster#aws_attributes}
        '''
        result = self._values.get("aws_attributes")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoAwsAttributes"], result)

    @builtins.property
    def azure_attributes(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoAzureAttributes"]:
        '''azure_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#azure_attributes DataDatabricksCluster#azure_attributes}
        '''
        result = self._values.get("azure_attributes")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoAzureAttributes"], result)

    @builtins.property
    def cluster_cores(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_cores DataDatabricksCluster#cluster_cores}.'''
        result = self._values.get("cluster_cores")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_id DataDatabricksCluster#cluster_id}.'''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_log_conf(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoClusterLogConf"]:
        '''cluster_log_conf block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_log_conf DataDatabricksCluster#cluster_log_conf}
        '''
        result = self._values.get("cluster_log_conf")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoClusterLogConf"], result)

    @builtins.property
    def cluster_log_status(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoClusterLogStatus"]:
        '''cluster_log_status block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_log_status DataDatabricksCluster#cluster_log_status}
        '''
        result = self._values.get("cluster_log_status")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoClusterLogStatus"], result)

    @builtins.property
    def cluster_memory_mb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_memory_mb DataDatabricksCluster#cluster_memory_mb}.'''
        result = self._values.get("cluster_memory_mb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_name DataDatabricksCluster#cluster_name}.'''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_source(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_source DataDatabricksCluster#cluster_source}.'''
        result = self._values.get("cluster_source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def creator_user_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#creator_user_name DataDatabricksCluster#creator_user_name}.'''
        result = self._values.get("creator_user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#custom_tags DataDatabricksCluster#custom_tags}.'''
        result = self._values.get("custom_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def data_security_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#data_security_mode DataDatabricksCluster#data_security_mode}.'''
        result = self._values.get("data_security_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_image(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoDockerImage"]:
        '''docker_image block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#docker_image DataDatabricksCluster#docker_image}
        '''
        result = self._values.get("docker_image")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoDockerImage"], result)

    @builtins.property
    def driver(self) -> typing.Optional["DataDatabricksClusterClusterInfoDriver"]:
        '''driver block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver DataDatabricksCluster#driver}
        '''
        result = self._values.get("driver")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoDriver"], result)

    @builtins.property
    def driver_instance_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver_instance_pool_id DataDatabricksCluster#driver_instance_pool_id}.'''
        result = self._values.get("driver_instance_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def driver_node_type_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#driver_node_type_id DataDatabricksCluster#driver_node_type_id}.'''
        result = self._values.get("driver_node_type_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_elastic_disk(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_elastic_disk DataDatabricksCluster#enable_elastic_disk}.'''
        result = self._values.get("enable_elastic_disk")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_local_disk_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_local_disk_encryption DataDatabricksCluster#enable_local_disk_encryption}.'''
        result = self._values.get("enable_local_disk_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def executors(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksClusterClusterInfoExecutors"]]]:
        '''executors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#executors DataDatabricksCluster#executors}
        '''
        result = self._values.get("executors")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksClusterClusterInfoExecutors"]]], result)

    @builtins.property
    def gcp_attributes(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoGcpAttributes"]:
        '''gcp_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#gcp_attributes DataDatabricksCluster#gcp_attributes}
        '''
        result = self._values.get("gcp_attributes")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoGcpAttributes"], result)

    @builtins.property
    def init_scripts(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksClusterClusterInfoInitScripts"]]]:
        '''init_scripts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#init_scripts DataDatabricksCluster#init_scripts}
        '''
        result = self._values.get("init_scripts")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksClusterClusterInfoInitScripts"]]], result)

    @builtins.property
    def instance_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_pool_id DataDatabricksCluster#instance_pool_id}.'''
        result = self._values.get("instance_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jdbc_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#jdbc_port DataDatabricksCluster#jdbc_port}.'''
        result = self._values.get("jdbc_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def last_activity_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_activity_time DataDatabricksCluster#last_activity_time}.'''
        result = self._values.get("last_activity_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def last_state_loss_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_state_loss_time DataDatabricksCluster#last_state_loss_time}.'''
        result = self._values.get("last_state_loss_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def node_type_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_type_id DataDatabricksCluster#node_type_id}.'''
        result = self._values.get("node_type_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#num_workers DataDatabricksCluster#num_workers}.'''
        result = self._values.get("num_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def policy_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#policy_id DataDatabricksCluster#policy_id}.'''
        result = self._values.get("policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime_engine(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#runtime_engine DataDatabricksCluster#runtime_engine}.'''
        result = self._values.get("runtime_engine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_user_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#single_user_name DataDatabricksCluster#single_user_name}.'''
        result = self._values.get("single_user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spark_conf(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_conf DataDatabricksCluster#spark_conf}.'''
        result = self._values.get("spark_conf")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def spark_context_id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_context_id DataDatabricksCluster#spark_context_id}.'''
        result = self._values.get("spark_context_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def spark_env_vars(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spark_env_vars DataDatabricksCluster#spark_env_vars}.'''
        result = self._values.get("spark_env_vars")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def ssh_public_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ssh_public_keys DataDatabricksCluster#ssh_public_keys}.'''
        result = self._values.get("ssh_public_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def start_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#start_time DataDatabricksCluster#start_time}.'''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def state_message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#state_message DataDatabricksCluster#state_message}.'''
        result = self._values.get("state_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def terminate_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#terminate_time DataDatabricksCluster#terminate_time}.'''
        result = self._values.get("terminate_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def termination_reason(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoTerminationReason"]:
        '''termination_reason block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#termination_reason DataDatabricksCluster#termination_reason}
        '''
        result = self._values.get("termination_reason")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoTerminationReason"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoAutoscale",
    jsii_struct_bases=[],
    name_mapping={"max_workers": "maxWorkers", "min_workers": "minWorkers"},
)
class DataDatabricksClusterClusterInfoAutoscale:
    def __init__(
        self,
        *,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#max_workers DataDatabricksCluster#max_workers}.
        :param min_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#min_workers DataDatabricksCluster#min_workers}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49a9c2ad50c160d7885fc28045c24ffa6f000e4ccb7f453c8360c7a3d77148c8)
            check_type(argname="argument max_workers", value=max_workers, expected_type=type_hints["max_workers"])
            check_type(argname="argument min_workers", value=min_workers, expected_type=type_hints["min_workers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max_workers is not None:
            self._values["max_workers"] = max_workers
        if min_workers is not None:
            self._values["min_workers"] = min_workers

    @builtins.property
    def max_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#max_workers DataDatabricksCluster#max_workers}.'''
        result = self._values.get("max_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#min_workers DataDatabricksCluster#min_workers}.'''
        result = self._values.get("min_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoAutoscale(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoAutoscaleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoAutoscaleOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61a5c81af86f67b5c2927d3fa8ca85a14b8feb06e1b3597b657d85c6e5e7293c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxWorkers")
    def reset_max_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxWorkers", []))

    @jsii.member(jsii_name="resetMinWorkers")
    def reset_min_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinWorkers", []))

    @builtins.property
    @jsii.member(jsii_name="maxWorkersInput")
    def max_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="minWorkersInput")
    def min_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWorkers")
    def max_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxWorkers"))

    @max_workers.setter
    def max_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__074118ac5a361f1e65608b670769f47864bacd1802100f5247c02d79679c5076)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="minWorkers")
    def min_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minWorkers"))

    @min_workers.setter
    def min_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f9523a52774ddd02d17b6f470d6f590fdc919820f956b2077fccc98011d6e62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoAutoscale]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoAutoscale], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoAutoscale],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ceaa988b67b8b30e43067d9e427d6344f0506649836b3840a75953f3015bc60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoAwsAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "ebs_volume_count": "ebsVolumeCount",
        "ebs_volume_size": "ebsVolumeSize",
        "ebs_volume_type": "ebsVolumeType",
        "first_on_demand": "firstOnDemand",
        "instance_profile_arn": "instanceProfileArn",
        "spot_bid_price_percent": "spotBidPricePercent",
        "zone_id": "zoneId",
    },
)
class DataDatabricksClusterClusterInfoAwsAttributes:
    def __init__(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        ebs_volume_count: typing.Optional[jsii.Number] = None,
        ebs_volume_size: typing.Optional[jsii.Number] = None,
        ebs_volume_type: typing.Optional[builtins.str] = None,
        first_on_demand: typing.Optional[jsii.Number] = None,
        instance_profile_arn: typing.Optional[builtins.str] = None,
        spot_bid_price_percent: typing.Optional[jsii.Number] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.
        :param ebs_volume_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_count DataDatabricksCluster#ebs_volume_count}.
        :param ebs_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_size DataDatabricksCluster#ebs_volume_size}.
        :param ebs_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_type DataDatabricksCluster#ebs_volume_type}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#first_on_demand DataDatabricksCluster#first_on_demand}.
        :param instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_profile_arn DataDatabricksCluster#instance_profile_arn}.
        :param spot_bid_price_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spot_bid_price_percent DataDatabricksCluster#spot_bid_price_percent}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#zone_id DataDatabricksCluster#zone_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e817bc42c3681c9e8a03b7ecbd8503f33cea3d3e6f0e84468c0aac93b4eaa57)
            check_type(argname="argument availability", value=availability, expected_type=type_hints["availability"])
            check_type(argname="argument ebs_volume_count", value=ebs_volume_count, expected_type=type_hints["ebs_volume_count"])
            check_type(argname="argument ebs_volume_size", value=ebs_volume_size, expected_type=type_hints["ebs_volume_size"])
            check_type(argname="argument ebs_volume_type", value=ebs_volume_type, expected_type=type_hints["ebs_volume_type"])
            check_type(argname="argument first_on_demand", value=first_on_demand, expected_type=type_hints["first_on_demand"])
            check_type(argname="argument instance_profile_arn", value=instance_profile_arn, expected_type=type_hints["instance_profile_arn"])
            check_type(argname="argument spot_bid_price_percent", value=spot_bid_price_percent, expected_type=type_hints["spot_bid_price_percent"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability is not None:
            self._values["availability"] = availability
        if ebs_volume_count is not None:
            self._values["ebs_volume_count"] = ebs_volume_count
        if ebs_volume_size is not None:
            self._values["ebs_volume_size"] = ebs_volume_size
        if ebs_volume_type is not None:
            self._values["ebs_volume_type"] = ebs_volume_type
        if first_on_demand is not None:
            self._values["first_on_demand"] = first_on_demand
        if instance_profile_arn is not None:
            self._values["instance_profile_arn"] = instance_profile_arn
        if spot_bid_price_percent is not None:
            self._values["spot_bid_price_percent"] = spot_bid_price_percent
        if zone_id is not None:
            self._values["zone_id"] = zone_id

    @builtins.property
    def availability(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_volume_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_count DataDatabricksCluster#ebs_volume_count}.'''
        result = self._values.get("ebs_volume_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ebs_volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_size DataDatabricksCluster#ebs_volume_size}.'''
        result = self._values.get("ebs_volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ebs_volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_type DataDatabricksCluster#ebs_volume_type}.'''
        result = self._values.get("ebs_volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_on_demand(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#first_on_demand DataDatabricksCluster#first_on_demand}.'''
        result = self._values.get("first_on_demand")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_profile_arn DataDatabricksCluster#instance_profile_arn}.'''
        result = self._values.get("instance_profile_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_bid_price_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spot_bid_price_percent DataDatabricksCluster#spot_bid_price_percent}.'''
        result = self._values.get("spot_bid_price_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#zone_id DataDatabricksCluster#zone_id}.'''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoAwsAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoAwsAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoAwsAttributesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4962c90e92675d9b69d3d07780b1aa9353de6d9caeca25af34d73638cca4d8da)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAvailability")
    def reset_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailability", []))

    @jsii.member(jsii_name="resetEbsVolumeCount")
    def reset_ebs_volume_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsVolumeCount", []))

    @jsii.member(jsii_name="resetEbsVolumeSize")
    def reset_ebs_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsVolumeSize", []))

    @jsii.member(jsii_name="resetEbsVolumeType")
    def reset_ebs_volume_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsVolumeType", []))

    @jsii.member(jsii_name="resetFirstOnDemand")
    def reset_first_on_demand(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirstOnDemand", []))

    @jsii.member(jsii_name="resetInstanceProfileArn")
    def reset_instance_profile_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceProfileArn", []))

    @jsii.member(jsii_name="resetSpotBidPricePercent")
    def reset_spot_bid_price_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotBidPricePercent", []))

    @jsii.member(jsii_name="resetZoneId")
    def reset_zone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneId", []))

    @builtins.property
    @jsii.member(jsii_name="availabilityInput")
    def availability_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeCountInput")
    def ebs_volume_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ebsVolumeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeSizeInput")
    def ebs_volume_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ebsVolumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeTypeInput")
    def ebs_volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ebsVolumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="firstOnDemandInput")
    def first_on_demand_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "firstOnDemandInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceProfileArnInput")
    def instance_profile_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceProfileArnInput"))

    @builtins.property
    @jsii.member(jsii_name="spotBidPricePercentInput")
    def spot_bid_price_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "spotBidPricePercentInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="availability")
    def availability(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availability"))

    @availability.setter
    def availability(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90389a4992d69cce8807429e5298bc2c1cc1177f98116cb4ac91e6bd7ad39bf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeCount")
    def ebs_volume_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsVolumeCount"))

    @ebs_volume_count.setter
    def ebs_volume_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e463c10c4064d2a1cf2384b8bd86c677b3e44b47a5c38ff5d9d5da7a063d0ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeCount", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeSize")
    def ebs_volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsVolumeSize"))

    @ebs_volume_size.setter
    def ebs_volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a7c555fb9864e7b7ea2893ee8656bec28388e6efe8a644f8425e3b4295c878e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeType")
    def ebs_volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ebsVolumeType"))

    @ebs_volume_type.setter
    def ebs_volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d79a78c6a83e18463cf1032a4c82918c1070118b6f25e7343cc13a495b1800c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeType", value)

    @builtins.property
    @jsii.member(jsii_name="firstOnDemand")
    def first_on_demand(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "firstOnDemand"))

    @first_on_demand.setter
    def first_on_demand(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd0066c7f5d2fceee518fe6986fcfc373b148dd31ad3ff7f979c63496af978c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstOnDemand", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfileArn")
    def instance_profile_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceProfileArn"))

    @instance_profile_arn.setter
    def instance_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26b3a65bbd686c8664a67d9b401419d88c3c9d286d5a4ae2c9c0122cfa13b4d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="spotBidPricePercent")
    def spot_bid_price_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotBidPricePercent"))

    @spot_bid_price_percent.setter
    def spot_bid_price_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a089a5e2a5f599ff3f3f89347470dbdb5a96138da0f250f7f3f9366dae03e74e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotBidPricePercent", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a568ac2785e081711a111a7c33daa49bf86ab50998bc46ac3d0d3375b24ed8ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoAwsAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoAwsAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoAwsAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d171c079811861faa12c6cc55b94c0f801309ac1b3dd004f872f295bdbcb705)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoAzureAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "first_on_demand": "firstOnDemand",
        "spot_bid_max_price": "spotBidMaxPrice",
    },
)
class DataDatabricksClusterClusterInfoAzureAttributes:
    def __init__(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        first_on_demand: typing.Optional[jsii.Number] = None,
        spot_bid_max_price: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#first_on_demand DataDatabricksCluster#first_on_demand}.
        :param spot_bid_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spot_bid_max_price DataDatabricksCluster#spot_bid_max_price}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efc875c53a47a7040774d946307573f621908820fb158100ba31419d34d18ee1)
            check_type(argname="argument availability", value=availability, expected_type=type_hints["availability"])
            check_type(argname="argument first_on_demand", value=first_on_demand, expected_type=type_hints["first_on_demand"])
            check_type(argname="argument spot_bid_max_price", value=spot_bid_max_price, expected_type=type_hints["spot_bid_max_price"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability is not None:
            self._values["availability"] = availability
        if first_on_demand is not None:
            self._values["first_on_demand"] = first_on_demand
        if spot_bid_max_price is not None:
            self._values["spot_bid_max_price"] = spot_bid_max_price

    @builtins.property
    def availability(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_on_demand(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#first_on_demand DataDatabricksCluster#first_on_demand}.'''
        result = self._values.get("first_on_demand")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def spot_bid_max_price(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spot_bid_max_price DataDatabricksCluster#spot_bid_max_price}.'''
        result = self._values.get("spot_bid_max_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoAzureAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoAzureAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoAzureAttributesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba9f238e842f58ba6614df8520f163e45873948a2ec8746392379f74946a3993)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAvailability")
    def reset_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailability", []))

    @jsii.member(jsii_name="resetFirstOnDemand")
    def reset_first_on_demand(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirstOnDemand", []))

    @jsii.member(jsii_name="resetSpotBidMaxPrice")
    def reset_spot_bid_max_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotBidMaxPrice", []))

    @builtins.property
    @jsii.member(jsii_name="availabilityInput")
    def availability_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="firstOnDemandInput")
    def first_on_demand_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "firstOnDemandInput"))

    @builtins.property
    @jsii.member(jsii_name="spotBidMaxPriceInput")
    def spot_bid_max_price_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "spotBidMaxPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="availability")
    def availability(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availability"))

    @availability.setter
    def availability(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__551e03eb74c653fe04aeedf2bba8986e0db20fa09b22ed7df3752c2697867bbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="firstOnDemand")
    def first_on_demand(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "firstOnDemand"))

    @first_on_demand.setter
    def first_on_demand(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8769f9cfdb32087c731dc2bf75087e8023b4869017034772937dc415dfc749a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstOnDemand", value)

    @builtins.property
    @jsii.member(jsii_name="spotBidMaxPrice")
    def spot_bid_max_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotBidMaxPrice"))

    @spot_bid_max_price.setter
    def spot_bid_max_price(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__585c0ce9ac5cd64a4008cd7efcc0435388b40630e746dcfb3987bc17b3ac310e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotBidMaxPrice", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoAzureAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoAzureAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoAzureAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d64eace0e1c5d2053982513a78939185e0041d4492cfe4a8d0e430935f5b907)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoClusterLogConf",
    jsii_struct_bases=[],
    name_mapping={"dbfs": "dbfs", "s3": "s3"},
)
class DataDatabricksClusterClusterInfoClusterLogConf:
    def __init__(
        self,
        *,
        dbfs: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoClusterLogConfDbfs", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoClusterLogConfS3", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dbfs: dbfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#dbfs DataDatabricksCluster#dbfs}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#s3 DataDatabricksCluster#s3}
        '''
        if isinstance(dbfs, dict):
            dbfs = DataDatabricksClusterClusterInfoClusterLogConfDbfs(**dbfs)
        if isinstance(s3, dict):
            s3 = DataDatabricksClusterClusterInfoClusterLogConfS3(**s3)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__308585a3320755d3d67595bee59528447495820e87ef84d56eabc9d8a2ddea58)
            check_type(argname="argument dbfs", value=dbfs, expected_type=type_hints["dbfs"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dbfs is not None:
            self._values["dbfs"] = dbfs
        if s3 is not None:
            self._values["s3"] = s3

    @builtins.property
    def dbfs(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoClusterLogConfDbfs"]:
        '''dbfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#dbfs DataDatabricksCluster#dbfs}
        '''
        result = self._values.get("dbfs")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoClusterLogConfDbfs"], result)

    @builtins.property
    def s3(self) -> typing.Optional["DataDatabricksClusterClusterInfoClusterLogConfS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#s3 DataDatabricksCluster#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoClusterLogConfS3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoClusterLogConf(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoClusterLogConfDbfs",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class DataDatabricksClusterClusterInfoClusterLogConfDbfs:
    def __init__(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c778629d1c4e9c102b00bf38ac827799b2c6aaf332e02c4ee8a9c3f7b0444709)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoClusterLogConfDbfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoClusterLogConfDbfsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoClusterLogConfDbfsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a085a9c7d70ba5e0cf9cab09b260b1e8d56d5c75182914a68c23350ad53e154)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37393d2882c51e19ab26cb34984551e11d6476a465ff79e20d91a404c288dc2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfDbfs]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfDbfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfDbfs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42671a53bc53109241ab3115986b5503e4f5c46adb890b9ef1406c4c0997645c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksClusterClusterInfoClusterLogConfOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoClusterLogConfOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caa4816ee34df49743bd9c60c38049bbe415e66512b96dd0f503fb3263385089)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDbfs")
    def put_dbfs(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        '''
        value = DataDatabricksClusterClusterInfoClusterLogConfDbfs(
            destination=destination
        )

        return typing.cast(None, jsii.invoke(self, "putDbfs", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        destination: builtins.str,
        canned_acl: typing.Optional[builtins.str] = None,
        enable_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encryption_type: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#canned_acl DataDatabricksCluster#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_encryption DataDatabricksCluster#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#encryption_type DataDatabricksCluster#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#endpoint DataDatabricksCluster#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#kms_key DataDatabricksCluster#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#region DataDatabricksCluster#region}.
        '''
        value = DataDatabricksClusterClusterInfoClusterLogConfS3(
            destination=destination,
            canned_acl=canned_acl,
            enable_encryption=enable_encryption,
            encryption_type=encryption_type,
            endpoint=endpoint,
            kms_key=kms_key,
            region=region,
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="resetDbfs")
    def reset_dbfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbfs", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @builtins.property
    @jsii.member(jsii_name="dbfs")
    def dbfs(self) -> DataDatabricksClusterClusterInfoClusterLogConfDbfsOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoClusterLogConfDbfsOutputReference, jsii.get(self, "dbfs"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference":
        return typing.cast("DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="dbfsInput")
    def dbfs_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfDbfs]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfDbfs], jsii.get(self, "dbfsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoClusterLogConfS3"]:
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoClusterLogConfS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoClusterLogConf]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoClusterLogConf], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoClusterLogConf],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c8b57b13973a8886694e958656298ae80a259caa9b53e6cba5b5b0734330653)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoClusterLogConfS3",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "canned_acl": "cannedAcl",
        "enable_encryption": "enableEncryption",
        "encryption_type": "encryptionType",
        "endpoint": "endpoint",
        "kms_key": "kmsKey",
        "region": "region",
    },
)
class DataDatabricksClusterClusterInfoClusterLogConfS3:
    def __init__(
        self,
        *,
        destination: builtins.str,
        canned_acl: typing.Optional[builtins.str] = None,
        enable_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encryption_type: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#canned_acl DataDatabricksCluster#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_encryption DataDatabricksCluster#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#encryption_type DataDatabricksCluster#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#endpoint DataDatabricksCluster#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#kms_key DataDatabricksCluster#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#region DataDatabricksCluster#region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33e2eae95f0f0da44c2e421afc22f20f1052b57fbf255bcacbd5b39c2f4250f3)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument canned_acl", value=canned_acl, expected_type=type_hints["canned_acl"])
            check_type(argname="argument enable_encryption", value=enable_encryption, expected_type=type_hints["enable_encryption"])
            check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
        }
        if canned_acl is not None:
            self._values["canned_acl"] = canned_acl
        if enable_encryption is not None:
            self._values["enable_encryption"] = enable_encryption
        if encryption_type is not None:
            self._values["encryption_type"] = encryption_type
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def canned_acl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#canned_acl DataDatabricksCluster#canned_acl}.'''
        result = self._values.get("canned_acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_encryption DataDatabricksCluster#enable_encryption}.'''
        result = self._values.get("enable_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encryption_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#encryption_type DataDatabricksCluster#encryption_type}.'''
        result = self._values.get("encryption_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#endpoint DataDatabricksCluster#endpoint}.'''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#kms_key DataDatabricksCluster#kms_key}.'''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#region DataDatabricksCluster#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoClusterLogConfS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__790db488da489570a2eb67666dadb7e463ea57ad7cd3efe097f3ff1e66b688cd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCannedAcl")
    def reset_canned_acl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCannedAcl", []))

    @jsii.member(jsii_name="resetEnableEncryption")
    def reset_enable_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableEncryption", []))

    @jsii.member(jsii_name="resetEncryptionType")
    def reset_encryption_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionType", []))

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @jsii.member(jsii_name="resetKmsKey")
    def reset_kms_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKey", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @builtins.property
    @jsii.member(jsii_name="cannedAclInput")
    def canned_acl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cannedAclInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="enableEncryptionInput")
    def enable_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionTypeInput")
    def encryption_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyInput")
    def kms_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="cannedAcl")
    def canned_acl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cannedAcl"))

    @canned_acl.setter
    def canned_acl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3213b9cdea742252fb689169b7d320ab637df403b49bb098421b0f2005a55cfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cannedAcl", value)

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6820c2064d82e918fdd458d95ef83e3cb9d1964115f7898a867720f501e7f66e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="enableEncryption")
    def enable_encryption(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableEncryption"))

    @enable_encryption.setter
    def enable_encryption(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3d27d91fde45a20d321adfaf8d3d207d227bff609fce5f21e2a01e50d07d20c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionType")
    def encryption_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionType"))

    @encryption_type.setter
    def encryption_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0259bd6eb5c3c1197edc3dd47d99c8ef4c364f6f7cafc981eaca936ec7ec47c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0204aaed752737d1f1a04b88cfd8dff8e80757d245c9764ce081c78c3c79c7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dd4adf364d758b69f2bd5d6c3cf3f6facdfc2217f45462917f6d873154eff8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f997e6ca3f20220100e1b301baf307cc60d5280f70adeb525e4ab01519850471)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfS3]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfS3],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecd84ac45c6f25991bd9e9499631527e6b653c2288d8ffc01ebdc0444f5e20b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoClusterLogStatus",
    jsii_struct_bases=[],
    name_mapping={
        "last_attempted": "lastAttempted",
        "last_exception": "lastException",
    },
)
class DataDatabricksClusterClusterInfoClusterLogStatus:
    def __init__(
        self,
        *,
        last_attempted: typing.Optional[jsii.Number] = None,
        last_exception: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param last_attempted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_attempted DataDatabricksCluster#last_attempted}.
        :param last_exception: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_exception DataDatabricksCluster#last_exception}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ff391eca99d5918bdc6c7c11a04dc394463f020e26749fcd5413125fe96e41a)
            check_type(argname="argument last_attempted", value=last_attempted, expected_type=type_hints["last_attempted"])
            check_type(argname="argument last_exception", value=last_exception, expected_type=type_hints["last_exception"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if last_attempted is not None:
            self._values["last_attempted"] = last_attempted
        if last_exception is not None:
            self._values["last_exception"] = last_exception

    @builtins.property
    def last_attempted(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_attempted DataDatabricksCluster#last_attempted}.'''
        result = self._values.get("last_attempted")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def last_exception(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_exception DataDatabricksCluster#last_exception}.'''
        result = self._values.get("last_exception")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoClusterLogStatus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoClusterLogStatusOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoClusterLogStatusOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__085dc29d98a87251779c1e20fbff32d71c4cc041d89937b37d7a86e573308c5e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLastAttempted")
    def reset_last_attempted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastAttempted", []))

    @jsii.member(jsii_name="resetLastException")
    def reset_last_exception(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastException", []))

    @builtins.property
    @jsii.member(jsii_name="lastAttemptedInput")
    def last_attempted_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lastAttemptedInput"))

    @builtins.property
    @jsii.member(jsii_name="lastExceptionInput")
    def last_exception_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastExceptionInput"))

    @builtins.property
    @jsii.member(jsii_name="lastAttempted")
    def last_attempted(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lastAttempted"))

    @last_attempted.setter
    def last_attempted(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6aa79b8140c59f273fded0557793db02805e10fb04f5d7a9fa6764b661c49d51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastAttempted", value)

    @builtins.property
    @jsii.member(jsii_name="lastException")
    def last_exception(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastException"))

    @last_exception.setter
    def last_exception(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c1dd3ca5c41cef546ae53ffa59ec1d0d5f7f8d54234094357db06abc68f99fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastException", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoClusterLogStatus]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoClusterLogStatus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoClusterLogStatus],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bb9f299d0656cd14dc8aab73fa96c932a3429e3551539379e2bc42aa2cb7f38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoDockerImage",
    jsii_struct_bases=[],
    name_mapping={"url": "url", "basic_auth": "basicAuth"},
)
class DataDatabricksClusterClusterInfoDockerImage:
    def __init__(
        self,
        *,
        url: builtins.str,
        basic_auth: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoDockerImageBasicAuth", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#url DataDatabricksCluster#url}.
        :param basic_auth: basic_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#basic_auth DataDatabricksCluster#basic_auth}
        '''
        if isinstance(basic_auth, dict):
            basic_auth = DataDatabricksClusterClusterInfoDockerImageBasicAuth(**basic_auth)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c158ce94ca43385a0084cf6e326d51c915a2eccef4a366d1188c48937f779aa9)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument basic_auth", value=basic_auth, expected_type=type_hints["basic_auth"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if basic_auth is not None:
            self._values["basic_auth"] = basic_auth

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#url DataDatabricksCluster#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def basic_auth(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoDockerImageBasicAuth"]:
        '''basic_auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#basic_auth DataDatabricksCluster#basic_auth}
        '''
        result = self._values.get("basic_auth")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoDockerImageBasicAuth"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoDockerImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoDockerImageBasicAuth",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class DataDatabricksClusterClusterInfoDockerImageBasicAuth:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#password DataDatabricksCluster#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#username DataDatabricksCluster#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf62467def032fea8f55c256492570831bbaf48f6254bb9643384c6e29f2e4e9)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#password DataDatabricksCluster#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#username DataDatabricksCluster#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoDockerImageBasicAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoDockerImageBasicAuthOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoDockerImageBasicAuthOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0049d37fd051e7b304900466750303023a3f9d01f09ae85a7cebd42467047e1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc966efec25f2338418462de7de892c30f2326d9b67befd6136387269912dfb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad3538dd56aa772ee966f25abd298005ed2bcb91516245fd1a5b73eaf7ade85b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoDockerImageBasicAuth]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoDockerImageBasicAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoDockerImageBasicAuth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__281c56a91f9392b534ad7291a3ce9c107f355dcf591f262b316d3cc9391acaf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksClusterClusterInfoDockerImageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoDockerImageOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f997dd0c9902453755c451dafe7a992a29255aa5b7f849a1d3764e8961f033f9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBasicAuth")
    def put_basic_auth(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#password DataDatabricksCluster#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#username DataDatabricksCluster#username}.
        '''
        value = DataDatabricksClusterClusterInfoDockerImageBasicAuth(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putBasicAuth", [value]))

    @jsii.member(jsii_name="resetBasicAuth")
    def reset_basic_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuth", []))

    @builtins.property
    @jsii.member(jsii_name="basicAuth")
    def basic_auth(
        self,
    ) -> DataDatabricksClusterClusterInfoDockerImageBasicAuthOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoDockerImageBasicAuthOutputReference, jsii.get(self, "basicAuth"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthInput")
    def basic_auth_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoDockerImageBasicAuth]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoDockerImageBasicAuth], jsii.get(self, "basicAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf2f929c18dd13260d2cdeba2194bbef063a5224798eb0582d31222b820fadf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoDockerImage]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoDockerImage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoDockerImage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93272fa6d29f7ce25d5cd05cc5ea9fcac18dc2f7eef14f06aeedb5d0e3c14ed2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoDriver",
    jsii_struct_bases=[],
    name_mapping={
        "host_private_ip": "hostPrivateIp",
        "instance_id": "instanceId",
        "node_aws_attributes": "nodeAwsAttributes",
        "node_id": "nodeId",
        "private_ip": "privateIp",
        "public_dns": "publicDns",
        "start_timestamp": "startTimestamp",
    },
)
class DataDatabricksClusterClusterInfoDriver:
    def __init__(
        self,
        *,
        host_private_ip: typing.Optional[builtins.str] = None,
        instance_id: typing.Optional[builtins.str] = None,
        node_aws_attributes: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoDriverNodeAwsAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        node_id: typing.Optional[builtins.str] = None,
        private_ip: typing.Optional[builtins.str] = None,
        public_dns: typing.Optional[builtins.str] = None,
        start_timestamp: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param host_private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#host_private_ip DataDatabricksCluster#host_private_ip}.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_id DataDatabricksCluster#instance_id}.
        :param node_aws_attributes: node_aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_aws_attributes DataDatabricksCluster#node_aws_attributes}
        :param node_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_id DataDatabricksCluster#node_id}.
        :param private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#private_ip DataDatabricksCluster#private_ip}.
        :param public_dns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#public_dns DataDatabricksCluster#public_dns}.
        :param start_timestamp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#start_timestamp DataDatabricksCluster#start_timestamp}.
        '''
        if isinstance(node_aws_attributes, dict):
            node_aws_attributes = DataDatabricksClusterClusterInfoDriverNodeAwsAttributes(**node_aws_attributes)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba945cdb80dcfd9eefbab23cb273c6b2202336b1fc2ed61d3f31e93ee200ba56)
            check_type(argname="argument host_private_ip", value=host_private_ip, expected_type=type_hints["host_private_ip"])
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument node_aws_attributes", value=node_aws_attributes, expected_type=type_hints["node_aws_attributes"])
            check_type(argname="argument node_id", value=node_id, expected_type=type_hints["node_id"])
            check_type(argname="argument private_ip", value=private_ip, expected_type=type_hints["private_ip"])
            check_type(argname="argument public_dns", value=public_dns, expected_type=type_hints["public_dns"])
            check_type(argname="argument start_timestamp", value=start_timestamp, expected_type=type_hints["start_timestamp"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if host_private_ip is not None:
            self._values["host_private_ip"] = host_private_ip
        if instance_id is not None:
            self._values["instance_id"] = instance_id
        if node_aws_attributes is not None:
            self._values["node_aws_attributes"] = node_aws_attributes
        if node_id is not None:
            self._values["node_id"] = node_id
        if private_ip is not None:
            self._values["private_ip"] = private_ip
        if public_dns is not None:
            self._values["public_dns"] = public_dns
        if start_timestamp is not None:
            self._values["start_timestamp"] = start_timestamp

    @builtins.property
    def host_private_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#host_private_ip DataDatabricksCluster#host_private_ip}.'''
        result = self._values.get("host_private_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_id DataDatabricksCluster#instance_id}.'''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_aws_attributes(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoDriverNodeAwsAttributes"]:
        '''node_aws_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_aws_attributes DataDatabricksCluster#node_aws_attributes}
        '''
        result = self._values.get("node_aws_attributes")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoDriverNodeAwsAttributes"], result)

    @builtins.property
    def node_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_id DataDatabricksCluster#node_id}.'''
        result = self._values.get("node_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#private_ip DataDatabricksCluster#private_ip}.'''
        result = self._values.get("private_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_dns(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#public_dns DataDatabricksCluster#public_dns}.'''
        result = self._values.get("public_dns")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_timestamp(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#start_timestamp DataDatabricksCluster#start_timestamp}.'''
        result = self._values.get("start_timestamp")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoDriver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoDriverNodeAwsAttributes",
    jsii_struct_bases=[],
    name_mapping={"is_spot": "isSpot"},
)
class DataDatabricksClusterClusterInfoDriverNodeAwsAttributes:
    def __init__(
        self,
        *,
        is_spot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param is_spot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#is_spot DataDatabricksCluster#is_spot}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d02a39857fcca8e9f434fed94886dc65c4627d7cfa2008fb72dff0a1f0438d8f)
            check_type(argname="argument is_spot", value=is_spot, expected_type=type_hints["is_spot"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if is_spot is not None:
            self._values["is_spot"] = is_spot

    @builtins.property
    def is_spot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#is_spot DataDatabricksCluster#is_spot}.'''
        result = self._values.get("is_spot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoDriverNodeAwsAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoDriverNodeAwsAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoDriverNodeAwsAttributesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e4f95c12a5fb82e3d2a9908533f36c0cc6a951695cc6be0592f234eb48f5e1f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsSpot")
    def reset_is_spot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsSpot", []))

    @builtins.property
    @jsii.member(jsii_name="isSpotInput")
    def is_spot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "isSpotInput"))

    @builtins.property
    @jsii.member(jsii_name="isSpot")
    def is_spot(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "isSpot"))

    @is_spot.setter
    def is_spot(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89f88c64d3d302cdb175d5387179bc15015aba92d23fafe4e53631057e0e7061)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isSpot", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoDriverNodeAwsAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoDriverNodeAwsAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoDriverNodeAwsAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23ac5740c877c415e9e209fc6980fc105baca6a09eaaecb8f79d20e5d39cc7cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksClusterClusterInfoDriverOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoDriverOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75d1f2ab40327660157f1ca53ba1c7e7e104d4be183cb203bbb07bcdba4d0aa4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNodeAwsAttributes")
    def put_node_aws_attributes(
        self,
        *,
        is_spot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param is_spot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#is_spot DataDatabricksCluster#is_spot}.
        '''
        value = DataDatabricksClusterClusterInfoDriverNodeAwsAttributes(
            is_spot=is_spot
        )

        return typing.cast(None, jsii.invoke(self, "putNodeAwsAttributes", [value]))

    @jsii.member(jsii_name="resetHostPrivateIp")
    def reset_host_private_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPrivateIp", []))

    @jsii.member(jsii_name="resetInstanceId")
    def reset_instance_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceId", []))

    @jsii.member(jsii_name="resetNodeAwsAttributes")
    def reset_node_aws_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeAwsAttributes", []))

    @jsii.member(jsii_name="resetNodeId")
    def reset_node_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeId", []))

    @jsii.member(jsii_name="resetPrivateIp")
    def reset_private_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIp", []))

    @jsii.member(jsii_name="resetPublicDns")
    def reset_public_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicDns", []))

    @jsii.member(jsii_name="resetStartTimestamp")
    def reset_start_timestamp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTimestamp", []))

    @builtins.property
    @jsii.member(jsii_name="nodeAwsAttributes")
    def node_aws_attributes(
        self,
    ) -> DataDatabricksClusterClusterInfoDriverNodeAwsAttributesOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoDriverNodeAwsAttributesOutputReference, jsii.get(self, "nodeAwsAttributes"))

    @builtins.property
    @jsii.member(jsii_name="hostPrivateIpInput")
    def host_private_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostPrivateIpInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeAwsAttributesInput")
    def node_aws_attributes_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoDriverNodeAwsAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoDriverNodeAwsAttributes], jsii.get(self, "nodeAwsAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeIdInput")
    def node_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpInput")
    def private_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpInput"))

    @builtins.property
    @jsii.member(jsii_name="publicDnsInput")
    def public_dns_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicDnsInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimestampInput")
    def start_timestamp_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startTimestampInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPrivateIp")
    def host_private_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostPrivateIp"))

    @host_private_ip.setter
    def host_private_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6269da4c4e8e22c53c633e1a84ecc17989278e17f938d7dd78ecbc2c2791f50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostPrivateIp", value)

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e6217b4fdda4a43b9182bfae99be5e08ae3ca71be1bd7ca759cd699e0a012cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value)

    @builtins.property
    @jsii.member(jsii_name="nodeId")
    def node_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeId"))

    @node_id.setter
    def node_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95c666feaad9064f1b42d9eaab632213e471a7c9cc6d4ba73c2011829122799b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeId", value)

    @builtins.property
    @jsii.member(jsii_name="privateIp")
    def private_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIp"))

    @private_ip.setter
    def private_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5ce0b251e0f71bdb99b5e688cb7a64a5dd9f8a114eb5c5eddacd443f0a734cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIp", value)

    @builtins.property
    @jsii.member(jsii_name="publicDns")
    def public_dns(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicDns"))

    @public_dns.setter
    def public_dns(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b2e19bc978bdccbbbdc261896d8ed189b83773e03834ad8c27374e3255e3f7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicDns", value)

    @builtins.property
    @jsii.member(jsii_name="startTimestamp")
    def start_timestamp(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startTimestamp"))

    @start_timestamp.setter
    def start_timestamp(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__940f566898bc345cf8823d5d89706a421d05b7f883d747dfdd6df49a1a6569e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTimestamp", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataDatabricksClusterClusterInfoDriver]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoDriver], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoDriver],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3408ab9000ed503aaad0c3d9f036334817bd68d835ed4e7395878f1c61eaeef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoExecutors",
    jsii_struct_bases=[],
    name_mapping={
        "host_private_ip": "hostPrivateIp",
        "instance_id": "instanceId",
        "node_aws_attributes": "nodeAwsAttributes",
        "node_id": "nodeId",
        "private_ip": "privateIp",
        "public_dns": "publicDns",
        "start_timestamp": "startTimestamp",
    },
)
class DataDatabricksClusterClusterInfoExecutors:
    def __init__(
        self,
        *,
        host_private_ip: typing.Optional[builtins.str] = None,
        instance_id: typing.Optional[builtins.str] = None,
        node_aws_attributes: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        node_id: typing.Optional[builtins.str] = None,
        private_ip: typing.Optional[builtins.str] = None,
        public_dns: typing.Optional[builtins.str] = None,
        start_timestamp: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param host_private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#host_private_ip DataDatabricksCluster#host_private_ip}.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_id DataDatabricksCluster#instance_id}.
        :param node_aws_attributes: node_aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_aws_attributes DataDatabricksCluster#node_aws_attributes}
        :param node_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_id DataDatabricksCluster#node_id}.
        :param private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#private_ip DataDatabricksCluster#private_ip}.
        :param public_dns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#public_dns DataDatabricksCluster#public_dns}.
        :param start_timestamp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#start_timestamp DataDatabricksCluster#start_timestamp}.
        '''
        if isinstance(node_aws_attributes, dict):
            node_aws_attributes = DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes(**node_aws_attributes)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56efd4c4e105f2524c7572ea493a933476856da95ef8ad6affd3d077d281bed6)
            check_type(argname="argument host_private_ip", value=host_private_ip, expected_type=type_hints["host_private_ip"])
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument node_aws_attributes", value=node_aws_attributes, expected_type=type_hints["node_aws_attributes"])
            check_type(argname="argument node_id", value=node_id, expected_type=type_hints["node_id"])
            check_type(argname="argument private_ip", value=private_ip, expected_type=type_hints["private_ip"])
            check_type(argname="argument public_dns", value=public_dns, expected_type=type_hints["public_dns"])
            check_type(argname="argument start_timestamp", value=start_timestamp, expected_type=type_hints["start_timestamp"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if host_private_ip is not None:
            self._values["host_private_ip"] = host_private_ip
        if instance_id is not None:
            self._values["instance_id"] = instance_id
        if node_aws_attributes is not None:
            self._values["node_aws_attributes"] = node_aws_attributes
        if node_id is not None:
            self._values["node_id"] = node_id
        if private_ip is not None:
            self._values["private_ip"] = private_ip
        if public_dns is not None:
            self._values["public_dns"] = public_dns
        if start_timestamp is not None:
            self._values["start_timestamp"] = start_timestamp

    @builtins.property
    def host_private_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#host_private_ip DataDatabricksCluster#host_private_ip}.'''
        result = self._values.get("host_private_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_id DataDatabricksCluster#instance_id}.'''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_aws_attributes(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes"]:
        '''node_aws_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_aws_attributes DataDatabricksCluster#node_aws_attributes}
        '''
        result = self._values.get("node_aws_attributes")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes"], result)

    @builtins.property
    def node_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_id DataDatabricksCluster#node_id}.'''
        result = self._values.get("node_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#private_ip DataDatabricksCluster#private_ip}.'''
        result = self._values.get("private_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_dns(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#public_dns DataDatabricksCluster#public_dns}.'''
        result = self._values.get("public_dns")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_timestamp(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#start_timestamp DataDatabricksCluster#start_timestamp}.'''
        result = self._values.get("start_timestamp")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoExecutors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoExecutorsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoExecutorsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89ae0df44d453cdabce14936c61460213d097863f97d5c9eed6261aff75dc501)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDatabricksClusterClusterInfoExecutorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e57016b3f1efe7024856a66c4bf50714b1e4f08227c7371c6dc6532734d54577)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataDatabricksClusterClusterInfoExecutorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b46adb6d396f434af13485c528527327be502148bb1a7656de58d377607a63c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58506aed2551fffab49cbbe3d6cefe030e4b2c80ea9ddfecc9e38519dfda125b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dcf162b681a2d8f4bdbc9994a6a728fe4d7456b872b3f89722a5305f3947786)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksClusterClusterInfoExecutors]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksClusterClusterInfoExecutors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksClusterClusterInfoExecutors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a42cd687030d3d2aba16097689eac4308916566604f31171a537fe5af932e7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes",
    jsii_struct_bases=[],
    name_mapping={"is_spot": "isSpot"},
)
class DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes:
    def __init__(
        self,
        *,
        is_spot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param is_spot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#is_spot DataDatabricksCluster#is_spot}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__126f158d2851f755515aba5281a41b7316c8ee640d980fa2fce392c68304c2bf)
            check_type(argname="argument is_spot", value=is_spot, expected_type=type_hints["is_spot"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if is_spot is not None:
            self._values["is_spot"] = is_spot

    @builtins.property
    def is_spot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#is_spot DataDatabricksCluster#is_spot}.'''
        result = self._values.get("is_spot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a7534255031b0a290ea7fab12cc0c63ed8cfe34660f39b1ffb4ddbed619125e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsSpot")
    def reset_is_spot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsSpot", []))

    @builtins.property
    @jsii.member(jsii_name="isSpotInput")
    def is_spot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "isSpotInput"))

    @builtins.property
    @jsii.member(jsii_name="isSpot")
    def is_spot(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "isSpot"))

    @is_spot.setter
    def is_spot(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__008b1344f9184da4ac0503d8e1882c7703e741a3ade2e22f844c4a499d916283)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isSpot", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__932a0ff22a17ab7b2a60ab65207e328012ca69aea9d57d135b6d207a454b929f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksClusterClusterInfoExecutorsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoExecutorsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__556a7b9afe4f1c947a73ec4c2459f41a291efa104908026b913382850d1704ee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNodeAwsAttributes")
    def put_node_aws_attributes(
        self,
        *,
        is_spot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param is_spot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#is_spot DataDatabricksCluster#is_spot}.
        '''
        value = DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes(
            is_spot=is_spot
        )

        return typing.cast(None, jsii.invoke(self, "putNodeAwsAttributes", [value]))

    @jsii.member(jsii_name="resetHostPrivateIp")
    def reset_host_private_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPrivateIp", []))

    @jsii.member(jsii_name="resetInstanceId")
    def reset_instance_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceId", []))

    @jsii.member(jsii_name="resetNodeAwsAttributes")
    def reset_node_aws_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeAwsAttributes", []))

    @jsii.member(jsii_name="resetNodeId")
    def reset_node_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeId", []))

    @jsii.member(jsii_name="resetPrivateIp")
    def reset_private_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIp", []))

    @jsii.member(jsii_name="resetPublicDns")
    def reset_public_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicDns", []))

    @jsii.member(jsii_name="resetStartTimestamp")
    def reset_start_timestamp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTimestamp", []))

    @builtins.property
    @jsii.member(jsii_name="nodeAwsAttributes")
    def node_aws_attributes(
        self,
    ) -> DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributesOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributesOutputReference, jsii.get(self, "nodeAwsAttributes"))

    @builtins.property
    @jsii.member(jsii_name="hostPrivateIpInput")
    def host_private_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostPrivateIpInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeAwsAttributesInput")
    def node_aws_attributes_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes], jsii.get(self, "nodeAwsAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeIdInput")
    def node_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpInput")
    def private_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpInput"))

    @builtins.property
    @jsii.member(jsii_name="publicDnsInput")
    def public_dns_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicDnsInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimestampInput")
    def start_timestamp_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startTimestampInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPrivateIp")
    def host_private_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostPrivateIp"))

    @host_private_ip.setter
    def host_private_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41ddeb059395685fb39b73bf9be4e4691235c152089bee63aeb12cd429859703)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostPrivateIp", value)

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__387adf8266f292631fae4e2eaa13e7572b27bd402ac76e90345c4945ab61abe0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value)

    @builtins.property
    @jsii.member(jsii_name="nodeId")
    def node_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeId"))

    @node_id.setter
    def node_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b1798a914e13218deb01290ab183b20f2c919ec9f7e707d113e779f829160b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeId", value)

    @builtins.property
    @jsii.member(jsii_name="privateIp")
    def private_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIp"))

    @private_ip.setter
    def private_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e2ed538eaa9a517dcccbb14271d22daea95e362d17f2a27e5ed97a749a22c14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIp", value)

    @builtins.property
    @jsii.member(jsii_name="publicDns")
    def public_dns(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicDns"))

    @public_dns.setter
    def public_dns(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c02444a028233fabd1d4b93f7630827e014f4d7cffb263f7e52743f650927dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicDns", value)

    @builtins.property
    @jsii.member(jsii_name="startTimestamp")
    def start_timestamp(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startTimestamp"))

    @start_timestamp.setter
    def start_timestamp(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__195c3c3289a57b2fdebc7911ff0d731857b3665511a1994848a8ef91c34d58f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTimestamp", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataDatabricksClusterClusterInfoExecutors, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataDatabricksClusterClusterInfoExecutors, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoExecutors, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c8ac26df5386e8bef0385e4ce4d696e0c31995315370130ebb01e90b8d7f352)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoGcpAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "boot_disk_size": "bootDiskSize",
        "google_service_account": "googleServiceAccount",
        "use_preemptible_executors": "usePreemptibleExecutors",
        "zone_id": "zoneId",
    },
)
class DataDatabricksClusterClusterInfoGcpAttributes:
    def __init__(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        boot_disk_size: typing.Optional[jsii.Number] = None,
        google_service_account: typing.Optional[builtins.str] = None,
        use_preemptible_executors: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.
        :param boot_disk_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#boot_disk_size DataDatabricksCluster#boot_disk_size}.
        :param google_service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#google_service_account DataDatabricksCluster#google_service_account}.
        :param use_preemptible_executors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#use_preemptible_executors DataDatabricksCluster#use_preemptible_executors}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#zone_id DataDatabricksCluster#zone_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba2c03c51d70d98648a12cd093b81a8c1f6b5bab5ddbfd20e19fe056fac51dbf)
            check_type(argname="argument availability", value=availability, expected_type=type_hints["availability"])
            check_type(argname="argument boot_disk_size", value=boot_disk_size, expected_type=type_hints["boot_disk_size"])
            check_type(argname="argument google_service_account", value=google_service_account, expected_type=type_hints["google_service_account"])
            check_type(argname="argument use_preemptible_executors", value=use_preemptible_executors, expected_type=type_hints["use_preemptible_executors"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability is not None:
            self._values["availability"] = availability
        if boot_disk_size is not None:
            self._values["boot_disk_size"] = boot_disk_size
        if google_service_account is not None:
            self._values["google_service_account"] = google_service_account
        if use_preemptible_executors is not None:
            self._values["use_preemptible_executors"] = use_preemptible_executors
        if zone_id is not None:
            self._values["zone_id"] = zone_id

    @builtins.property
    def availability(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def boot_disk_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#boot_disk_size DataDatabricksCluster#boot_disk_size}.'''
        result = self._values.get("boot_disk_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def google_service_account(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#google_service_account DataDatabricksCluster#google_service_account}.'''
        result = self._values.get("google_service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_preemptible_executors(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#use_preemptible_executors DataDatabricksCluster#use_preemptible_executors}.'''
        result = self._values.get("use_preemptible_executors")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#zone_id DataDatabricksCluster#zone_id}.'''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoGcpAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoGcpAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoGcpAttributesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b2ef7bbcf01e0fa9e7a4511af4fbd0806b28d2dc94a3d0dee1685cc6c66ed98)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAvailability")
    def reset_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailability", []))

    @jsii.member(jsii_name="resetBootDiskSize")
    def reset_boot_disk_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskSize", []))

    @jsii.member(jsii_name="resetGoogleServiceAccount")
    def reset_google_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleServiceAccount", []))

    @jsii.member(jsii_name="resetUsePreemptibleExecutors")
    def reset_use_preemptible_executors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsePreemptibleExecutors", []))

    @jsii.member(jsii_name="resetZoneId")
    def reset_zone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneId", []))

    @builtins.property
    @jsii.member(jsii_name="availabilityInput")
    def availability_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskSizeInput")
    def boot_disk_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bootDiskSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="googleServiceAccountInput")
    def google_service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleServiceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="usePreemptibleExecutorsInput")
    def use_preemptible_executors_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "usePreemptibleExecutorsInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="availability")
    def availability(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availability"))

    @availability.setter
    def availability(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64c6d8c2e8f5944ec2ffd313e24c6ac60bed8d66342042fcd1f207053d404ccc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="bootDiskSize")
    def boot_disk_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bootDiskSize"))

    @boot_disk_size.setter
    def boot_disk_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c134581a3a1200e69dc7f9858891dbb5ca570a7b09fae372ad758f4b9ac965e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskSize", value)

    @builtins.property
    @jsii.member(jsii_name="googleServiceAccount")
    def google_service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "googleServiceAccount"))

    @google_service_account.setter
    def google_service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c3422fcab8c06581ca43819fb6317d826eec5c097e5190c408c307ba6470ccf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "googleServiceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="usePreemptibleExecutors")
    def use_preemptible_executors(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "usePreemptibleExecutors"))

    @use_preemptible_executors.setter
    def use_preemptible_executors(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__536df40dc7a7f333146091401e3896f5de1adb8f915014eb2ca75f99beb71dd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usePreemptibleExecutors", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec314f8536c8e261a5847643feb7068efdf02f47d765bba59959f8c13630bc62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoGcpAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoGcpAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoGcpAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf1be6000bbfc150c2cb868e7fcd1faca3145dfb601077bbdc99bee027ddb51a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScripts",
    jsii_struct_bases=[],
    name_mapping={
        "abfss": "abfss",
        "dbfs": "dbfs",
        "file": "file",
        "gcs": "gcs",
        "s3": "s3",
    },
)
class DataDatabricksClusterClusterInfoInitScripts:
    def __init__(
        self,
        *,
        abfss: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoInitScriptsAbfss", typing.Dict[builtins.str, typing.Any]]] = None,
        dbfs: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoInitScriptsDbfs", typing.Dict[builtins.str, typing.Any]]] = None,
        file: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoInitScriptsFile", typing.Dict[builtins.str, typing.Any]]] = None,
        gcs: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoInitScriptsGcs", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["DataDatabricksClusterClusterInfoInitScriptsS3", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param abfss: abfss block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#abfss DataDatabricksCluster#abfss}
        :param dbfs: dbfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#dbfs DataDatabricksCluster#dbfs}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#file DataDatabricksCluster#file}
        :param gcs: gcs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#gcs DataDatabricksCluster#gcs}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#s3 DataDatabricksCluster#s3}
        '''
        if isinstance(abfss, dict):
            abfss = DataDatabricksClusterClusterInfoInitScriptsAbfss(**abfss)
        if isinstance(dbfs, dict):
            dbfs = DataDatabricksClusterClusterInfoInitScriptsDbfs(**dbfs)
        if isinstance(file, dict):
            file = DataDatabricksClusterClusterInfoInitScriptsFile(**file)
        if isinstance(gcs, dict):
            gcs = DataDatabricksClusterClusterInfoInitScriptsGcs(**gcs)
        if isinstance(s3, dict):
            s3 = DataDatabricksClusterClusterInfoInitScriptsS3(**s3)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f2fda4455fb55433b211770e88c34ef7e5138c5aa4c96ca640cb26cd8902e53)
            check_type(argname="argument abfss", value=abfss, expected_type=type_hints["abfss"])
            check_type(argname="argument dbfs", value=dbfs, expected_type=type_hints["dbfs"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument gcs", value=gcs, expected_type=type_hints["gcs"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if abfss is not None:
            self._values["abfss"] = abfss
        if dbfs is not None:
            self._values["dbfs"] = dbfs
        if file is not None:
            self._values["file"] = file
        if gcs is not None:
            self._values["gcs"] = gcs
        if s3 is not None:
            self._values["s3"] = s3

    @builtins.property
    def abfss(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoInitScriptsAbfss"]:
        '''abfss block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#abfss DataDatabricksCluster#abfss}
        '''
        result = self._values.get("abfss")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoInitScriptsAbfss"], result)

    @builtins.property
    def dbfs(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoInitScriptsDbfs"]:
        '''dbfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#dbfs DataDatabricksCluster#dbfs}
        '''
        result = self._values.get("dbfs")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoInitScriptsDbfs"], result)

    @builtins.property
    def file(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoInitScriptsFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#file DataDatabricksCluster#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoInitScriptsFile"], result)

    @builtins.property
    def gcs(self) -> typing.Optional["DataDatabricksClusterClusterInfoInitScriptsGcs"]:
        '''gcs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#gcs DataDatabricksCluster#gcs}
        '''
        result = self._values.get("gcs")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoInitScriptsGcs"], result)

    @builtins.property
    def s3(self) -> typing.Optional["DataDatabricksClusterClusterInfoInitScriptsS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#s3 DataDatabricksCluster#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoInitScriptsS3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoInitScripts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsAbfss",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class DataDatabricksClusterClusterInfoInitScriptsAbfss:
    def __init__(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7377669a98248cd231d230670dd77d8343e541ee0bb7678707999e0c629e8d49)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.'''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoInitScriptsAbfss(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoInitScriptsAbfssOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsAbfssOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bf370a4dddb1d6fa8e0209dae625abd5846c3ff8eb3fb7bd00dbf0f08cc7431)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDestination")
    def reset_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestination", []))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58cfeef92efb26a30aba96e9200de8c69a0034c8290de7e542d8fa0e33c4f10e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoInitScriptsAbfss]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoInitScriptsAbfss], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoInitScriptsAbfss],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__600e3e5a8394425daa8943873527103778801f678a9bc0eb513ee66aee0399c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsDbfs",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class DataDatabricksClusterClusterInfoInitScriptsDbfs:
    def __init__(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be97984f7218421372715a6c88921fcd88c197aad27f1e58aa0c04f07cb5a7b5)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoInitScriptsDbfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoInitScriptsDbfsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsDbfsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb3594326c12186d9b535f2d6bcd8a690aff0fda57195663483cd28675671733)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__965923c2ca40eb3683580f86de52175264697361ab1f184f7714d33934ec93d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoInitScriptsDbfs]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoInitScriptsDbfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoInitScriptsDbfs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f441f986ebaeee59e3ac14ecc2bd5f30f9472460fb6a9dcdfd12aadb4585476)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsFile",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class DataDatabricksClusterClusterInfoInitScriptsFile:
    def __init__(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a03a60dd66b8c60cf2077f013899619885215515532eba5f1a13306817074326)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.'''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoInitScriptsFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoInitScriptsFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsFileOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eacbfe350fab8de6177db90a6d16b665886ab3003c9867919702fda213632506)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDestination")
    def reset_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestination", []))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62584ac48e40f905917bceb70dceb9cf45bc9ae4471ad95de420612ea0d4da98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoInitScriptsFile]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoInitScriptsFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoInitScriptsFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba0f9af0f1d3fbb8b64179dfa27855686fd9e53dfc91e4919173e7d11027ed5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsGcs",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class DataDatabricksClusterClusterInfoInitScriptsGcs:
    def __init__(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79616c591bbfcce6e0db8859cd3c5020406b5dafff576a1ba8cf70155796d8b8)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.'''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoInitScriptsGcs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoInitScriptsGcsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsGcsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37e315b926dea0dd4a99c5f649f07312fed0527aefca9040d70671d1c919753e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDestination")
    def reset_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestination", []))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8ce13203a859104b7ea76ff491859bc98965c2294c94f06169441ea7c9707ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoInitScriptsGcs]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoInitScriptsGcs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoInitScriptsGcs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70f6b1a59ea090d39952a8c34c846b05860268feaa3b709d6aac71373cc6fe14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksClusterClusterInfoInitScriptsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f109e758f9f3337d5e7809eac71f47cdb1527a69e48aa8975d134c28685c255d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDatabricksClusterClusterInfoInitScriptsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b230b8a9df1396495562a7c4d9f7d5fbfd1375b53e93fdee241da252452292bf)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataDatabricksClusterClusterInfoInitScriptsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84d7c2a7e7483da9f34d1d8d3aa201383194b1323ad9075a215e289eb74e827b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02db248d8a755da48a8b24d42bc9beeaa6c3517a49bff21df9fe93f8422dfca4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa84f5579716197cc6af834b6a18faa31764de81068b7ac5e380e70cdb8a6e46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksClusterClusterInfoInitScripts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksClusterClusterInfoInitScripts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksClusterClusterInfoInitScripts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13c6f62d6811d4515af5186f379beec2d3394a700ab213e03ccf814e739e4a67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksClusterClusterInfoInitScriptsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b9407e55882007ebf5e9592e44c3c8085848d88126ce55551166dca07ffde8f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAbfss")
    def put_abfss(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        '''
        value = DataDatabricksClusterClusterInfoInitScriptsAbfss(
            destination=destination
        )

        return typing.cast(None, jsii.invoke(self, "putAbfss", [value]))

    @jsii.member(jsii_name="putDbfs")
    def put_dbfs(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        '''
        value = DataDatabricksClusterClusterInfoInitScriptsDbfs(
            destination=destination
        )

        return typing.cast(None, jsii.invoke(self, "putDbfs", [value]))

    @jsii.member(jsii_name="putFile")
    def put_file(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        '''
        value = DataDatabricksClusterClusterInfoInitScriptsFile(
            destination=destination
        )

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putGcs")
    def put_gcs(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        '''
        value = DataDatabricksClusterClusterInfoInitScriptsGcs(destination=destination)

        return typing.cast(None, jsii.invoke(self, "putGcs", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        destination: builtins.str,
        canned_acl: typing.Optional[builtins.str] = None,
        enable_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encryption_type: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#canned_acl DataDatabricksCluster#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_encryption DataDatabricksCluster#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#encryption_type DataDatabricksCluster#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#endpoint DataDatabricksCluster#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#kms_key DataDatabricksCluster#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#region DataDatabricksCluster#region}.
        '''
        value = DataDatabricksClusterClusterInfoInitScriptsS3(
            destination=destination,
            canned_acl=canned_acl,
            enable_encryption=enable_encryption,
            encryption_type=encryption_type,
            endpoint=endpoint,
            kms_key=kms_key,
            region=region,
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="resetAbfss")
    def reset_abfss(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAbfss", []))

    @jsii.member(jsii_name="resetDbfs")
    def reset_dbfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbfs", []))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetGcs")
    def reset_gcs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcs", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @builtins.property
    @jsii.member(jsii_name="abfss")
    def abfss(self) -> DataDatabricksClusterClusterInfoInitScriptsAbfssOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoInitScriptsAbfssOutputReference, jsii.get(self, "abfss"))

    @builtins.property
    @jsii.member(jsii_name="dbfs")
    def dbfs(self) -> DataDatabricksClusterClusterInfoInitScriptsDbfsOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoInitScriptsDbfsOutputReference, jsii.get(self, "dbfs"))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> DataDatabricksClusterClusterInfoInitScriptsFileOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoInitScriptsFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="gcs")
    def gcs(self) -> DataDatabricksClusterClusterInfoInitScriptsGcsOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoInitScriptsGcsOutputReference, jsii.get(self, "gcs"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "DataDatabricksClusterClusterInfoInitScriptsS3OutputReference":
        return typing.cast("DataDatabricksClusterClusterInfoInitScriptsS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="abfssInput")
    def abfss_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoInitScriptsAbfss]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoInitScriptsAbfss], jsii.get(self, "abfssInput"))

    @builtins.property
    @jsii.member(jsii_name="dbfsInput")
    def dbfs_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoInitScriptsDbfs]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoInitScriptsDbfs], jsii.get(self, "dbfsInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoInitScriptsFile]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoInitScriptsFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="gcsInput")
    def gcs_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoInitScriptsGcs]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoInitScriptsGcs], jsii.get(self, "gcsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoInitScriptsS3"]:
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoInitScriptsS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataDatabricksClusterClusterInfoInitScripts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataDatabricksClusterClusterInfoInitScripts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoInitScripts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04b3bdb38afb5d5b1affad680e1239270d933832a8dc5a3bfad3b7e8354e3672)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsS3",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "canned_acl": "cannedAcl",
        "enable_encryption": "enableEncryption",
        "encryption_type": "encryptionType",
        "endpoint": "endpoint",
        "kms_key": "kmsKey",
        "region": "region",
    },
)
class DataDatabricksClusterClusterInfoInitScriptsS3:
    def __init__(
        self,
        *,
        destination: builtins.str,
        canned_acl: typing.Optional[builtins.str] = None,
        enable_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encryption_type: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#canned_acl DataDatabricksCluster#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_encryption DataDatabricksCluster#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#encryption_type DataDatabricksCluster#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#endpoint DataDatabricksCluster#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#kms_key DataDatabricksCluster#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#region DataDatabricksCluster#region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b451b4782f3f50fc8f564ef934f4cb840af23d06c8ead6d303a9820ccd689d7)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument canned_acl", value=canned_acl, expected_type=type_hints["canned_acl"])
            check_type(argname="argument enable_encryption", value=enable_encryption, expected_type=type_hints["enable_encryption"])
            check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
        }
        if canned_acl is not None:
            self._values["canned_acl"] = canned_acl
        if enable_encryption is not None:
            self._values["enable_encryption"] = enable_encryption
        if encryption_type is not None:
            self._values["encryption_type"] = encryption_type
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#destination DataDatabricksCluster#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def canned_acl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#canned_acl DataDatabricksCluster#canned_acl}.'''
        result = self._values.get("canned_acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#enable_encryption DataDatabricksCluster#enable_encryption}.'''
        result = self._values.get("enable_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encryption_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#encryption_type DataDatabricksCluster#encryption_type}.'''
        result = self._values.get("encryption_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#endpoint DataDatabricksCluster#endpoint}.'''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#kms_key DataDatabricksCluster#kms_key}.'''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#region DataDatabricksCluster#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoInitScriptsS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoInitScriptsS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoInitScriptsS3OutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8410f080d04d4d869e23ac4e3f44d2441ece6b2207f61adf91262bebb21cb0e4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCannedAcl")
    def reset_canned_acl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCannedAcl", []))

    @jsii.member(jsii_name="resetEnableEncryption")
    def reset_enable_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableEncryption", []))

    @jsii.member(jsii_name="resetEncryptionType")
    def reset_encryption_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionType", []))

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @jsii.member(jsii_name="resetKmsKey")
    def reset_kms_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKey", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @builtins.property
    @jsii.member(jsii_name="cannedAclInput")
    def canned_acl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cannedAclInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="enableEncryptionInput")
    def enable_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionTypeInput")
    def encryption_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyInput")
    def kms_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="cannedAcl")
    def canned_acl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cannedAcl"))

    @canned_acl.setter
    def canned_acl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fd255279abbcde7ef40ca2ddca55675442e1cf83b471581d98f4bedbe931a34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cannedAcl", value)

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d66353fe966001977ffa522e230db43da2f26d5210303c2aaa5ac9ef74a06308)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="enableEncryption")
    def enable_encryption(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableEncryption"))

    @enable_encryption.setter
    def enable_encryption(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16ea180e9f879597f7bcd450326f0297b698b1f46bfc0720a1bba91fed0bc273)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionType")
    def encryption_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionType"))

    @encryption_type.setter
    def encryption_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a259654148ae1c820b012ee931e7157b4f3be6e5a206c927d0db9400a35e052)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09be604796cbd591a0149665c7c2688f11c3cdb3aad82ed196e8cd96f7769600)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dd815bf83d85cd20cb080c0277ee1685a0ca67ae1cad3161efef3ae6e3ab004)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__851bb1c3f8a93800d5db5e2587e84eeb1e842fae74ac6794308aaad6dffe2ff9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoInitScriptsS3]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoInitScriptsS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoInitScriptsS3],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dc4c558106ea8f1c227d5dba38d240997a1d243f8fda4460e306b13d0685a3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksClusterClusterInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e41e69d1871a4fdfca29f1a8a2725db7b893a525f568ec15427d0009d9d0b17)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutoscale")
    def put_autoscale(
        self,
        *,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#max_workers DataDatabricksCluster#max_workers}.
        :param min_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#min_workers DataDatabricksCluster#min_workers}.
        '''
        value = DataDatabricksClusterClusterInfoAutoscale(
            max_workers=max_workers, min_workers=min_workers
        )

        return typing.cast(None, jsii.invoke(self, "putAutoscale", [value]))

    @jsii.member(jsii_name="putAwsAttributes")
    def put_aws_attributes(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        ebs_volume_count: typing.Optional[jsii.Number] = None,
        ebs_volume_size: typing.Optional[jsii.Number] = None,
        ebs_volume_type: typing.Optional[builtins.str] = None,
        first_on_demand: typing.Optional[jsii.Number] = None,
        instance_profile_arn: typing.Optional[builtins.str] = None,
        spot_bid_price_percent: typing.Optional[jsii.Number] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.
        :param ebs_volume_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_count DataDatabricksCluster#ebs_volume_count}.
        :param ebs_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_size DataDatabricksCluster#ebs_volume_size}.
        :param ebs_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#ebs_volume_type DataDatabricksCluster#ebs_volume_type}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#first_on_demand DataDatabricksCluster#first_on_demand}.
        :param instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_profile_arn DataDatabricksCluster#instance_profile_arn}.
        :param spot_bid_price_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spot_bid_price_percent DataDatabricksCluster#spot_bid_price_percent}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#zone_id DataDatabricksCluster#zone_id}.
        '''
        value = DataDatabricksClusterClusterInfoAwsAttributes(
            availability=availability,
            ebs_volume_count=ebs_volume_count,
            ebs_volume_size=ebs_volume_size,
            ebs_volume_type=ebs_volume_type,
            first_on_demand=first_on_demand,
            instance_profile_arn=instance_profile_arn,
            spot_bid_price_percent=spot_bid_price_percent,
            zone_id=zone_id,
        )

        return typing.cast(None, jsii.invoke(self, "putAwsAttributes", [value]))

    @jsii.member(jsii_name="putAzureAttributes")
    def put_azure_attributes(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        first_on_demand: typing.Optional[jsii.Number] = None,
        spot_bid_max_price: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#first_on_demand DataDatabricksCluster#first_on_demand}.
        :param spot_bid_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#spot_bid_max_price DataDatabricksCluster#spot_bid_max_price}.
        '''
        value = DataDatabricksClusterClusterInfoAzureAttributes(
            availability=availability,
            first_on_demand=first_on_demand,
            spot_bid_max_price=spot_bid_max_price,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureAttributes", [value]))

    @jsii.member(jsii_name="putClusterLogConf")
    def put_cluster_log_conf(
        self,
        *,
        dbfs: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoClusterLogConfDbfs, typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoClusterLogConfS3, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dbfs: dbfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#dbfs DataDatabricksCluster#dbfs}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#s3 DataDatabricksCluster#s3}
        '''
        value = DataDatabricksClusterClusterInfoClusterLogConf(dbfs=dbfs, s3=s3)

        return typing.cast(None, jsii.invoke(self, "putClusterLogConf", [value]))

    @jsii.member(jsii_name="putClusterLogStatus")
    def put_cluster_log_status(
        self,
        *,
        last_attempted: typing.Optional[jsii.Number] = None,
        last_exception: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param last_attempted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_attempted DataDatabricksCluster#last_attempted}.
        :param last_exception: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#last_exception DataDatabricksCluster#last_exception}.
        '''
        value = DataDatabricksClusterClusterInfoClusterLogStatus(
            last_attempted=last_attempted, last_exception=last_exception
        )

        return typing.cast(None, jsii.invoke(self, "putClusterLogStatus", [value]))

    @jsii.member(jsii_name="putDockerImage")
    def put_docker_image(
        self,
        *,
        url: builtins.str,
        basic_auth: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoDockerImageBasicAuth, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#url DataDatabricksCluster#url}.
        :param basic_auth: basic_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#basic_auth DataDatabricksCluster#basic_auth}
        '''
        value = DataDatabricksClusterClusterInfoDockerImage(
            url=url, basic_auth=basic_auth
        )

        return typing.cast(None, jsii.invoke(self, "putDockerImage", [value]))

    @jsii.member(jsii_name="putDriver")
    def put_driver(
        self,
        *,
        host_private_ip: typing.Optional[builtins.str] = None,
        instance_id: typing.Optional[builtins.str] = None,
        node_aws_attributes: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoDriverNodeAwsAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
        node_id: typing.Optional[builtins.str] = None,
        private_ip: typing.Optional[builtins.str] = None,
        public_dns: typing.Optional[builtins.str] = None,
        start_timestamp: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param host_private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#host_private_ip DataDatabricksCluster#host_private_ip}.
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#instance_id DataDatabricksCluster#instance_id}.
        :param node_aws_attributes: node_aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_aws_attributes DataDatabricksCluster#node_aws_attributes}
        :param node_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#node_id DataDatabricksCluster#node_id}.
        :param private_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#private_ip DataDatabricksCluster#private_ip}.
        :param public_dns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#public_dns DataDatabricksCluster#public_dns}.
        :param start_timestamp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#start_timestamp DataDatabricksCluster#start_timestamp}.
        '''
        value = DataDatabricksClusterClusterInfoDriver(
            host_private_ip=host_private_ip,
            instance_id=instance_id,
            node_aws_attributes=node_aws_attributes,
            node_id=node_id,
            private_ip=private_ip,
            public_dns=public_dns,
            start_timestamp=start_timestamp,
        )

        return typing.cast(None, jsii.invoke(self, "putDriver", [value]))

    @jsii.member(jsii_name="putExecutors")
    def put_executors(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksClusterClusterInfoExecutors, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e275d2e0126c10e109882a9b7f0c186162706b148d7d1580661abdd443d0669c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExecutors", [value]))

    @jsii.member(jsii_name="putGcpAttributes")
    def put_gcp_attributes(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        boot_disk_size: typing.Optional[jsii.Number] = None,
        google_service_account: typing.Optional[builtins.str] = None,
        use_preemptible_executors: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#availability DataDatabricksCluster#availability}.
        :param boot_disk_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#boot_disk_size DataDatabricksCluster#boot_disk_size}.
        :param google_service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#google_service_account DataDatabricksCluster#google_service_account}.
        :param use_preemptible_executors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#use_preemptible_executors DataDatabricksCluster#use_preemptible_executors}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#zone_id DataDatabricksCluster#zone_id}.
        '''
        value = DataDatabricksClusterClusterInfoGcpAttributes(
            availability=availability,
            boot_disk_size=boot_disk_size,
            google_service_account=google_service_account,
            use_preemptible_executors=use_preemptible_executors,
            zone_id=zone_id,
        )

        return typing.cast(None, jsii.invoke(self, "putGcpAttributes", [value]))

    @jsii.member(jsii_name="putInitScripts")
    def put_init_scripts(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksClusterClusterInfoInitScripts, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__501e51c92f6fa984891ab1c600485f18a229334fcaee3d3f9627141a622a10ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInitScripts", [value]))

    @jsii.member(jsii_name="putTerminationReason")
    def put_termination_reason(
        self,
        *,
        code: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#code DataDatabricksCluster#code}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#parameters DataDatabricksCluster#parameters}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#type DataDatabricksCluster#type}.
        '''
        value = DataDatabricksClusterClusterInfoTerminationReason(
            code=code, parameters=parameters, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putTerminationReason", [value]))

    @jsii.member(jsii_name="resetAutoscale")
    def reset_autoscale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscale", []))

    @jsii.member(jsii_name="resetAutoterminationMinutes")
    def reset_autotermination_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoterminationMinutes", []))

    @jsii.member(jsii_name="resetAwsAttributes")
    def reset_aws_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsAttributes", []))

    @jsii.member(jsii_name="resetAzureAttributes")
    def reset_azure_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureAttributes", []))

    @jsii.member(jsii_name="resetClusterCores")
    def reset_cluster_cores(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterCores", []))

    @jsii.member(jsii_name="resetClusterId")
    def reset_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterId", []))

    @jsii.member(jsii_name="resetClusterLogConf")
    def reset_cluster_log_conf(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterLogConf", []))

    @jsii.member(jsii_name="resetClusterLogStatus")
    def reset_cluster_log_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterLogStatus", []))

    @jsii.member(jsii_name="resetClusterMemoryMb")
    def reset_cluster_memory_mb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterMemoryMb", []))

    @jsii.member(jsii_name="resetClusterName")
    def reset_cluster_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterName", []))

    @jsii.member(jsii_name="resetClusterSource")
    def reset_cluster_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterSource", []))

    @jsii.member(jsii_name="resetCreatorUserName")
    def reset_creator_user_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreatorUserName", []))

    @jsii.member(jsii_name="resetCustomTags")
    def reset_custom_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomTags", []))

    @jsii.member(jsii_name="resetDataSecurityMode")
    def reset_data_security_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataSecurityMode", []))

    @jsii.member(jsii_name="resetDockerImage")
    def reset_docker_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerImage", []))

    @jsii.member(jsii_name="resetDriver")
    def reset_driver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriver", []))

    @jsii.member(jsii_name="resetDriverInstancePoolId")
    def reset_driver_instance_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverInstancePoolId", []))

    @jsii.member(jsii_name="resetDriverNodeTypeId")
    def reset_driver_node_type_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverNodeTypeId", []))

    @jsii.member(jsii_name="resetEnableElasticDisk")
    def reset_enable_elastic_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableElasticDisk", []))

    @jsii.member(jsii_name="resetEnableLocalDiskEncryption")
    def reset_enable_local_disk_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableLocalDiskEncryption", []))

    @jsii.member(jsii_name="resetExecutors")
    def reset_executors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutors", []))

    @jsii.member(jsii_name="resetGcpAttributes")
    def reset_gcp_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpAttributes", []))

    @jsii.member(jsii_name="resetInitScripts")
    def reset_init_scripts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitScripts", []))

    @jsii.member(jsii_name="resetInstancePoolId")
    def reset_instance_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancePoolId", []))

    @jsii.member(jsii_name="resetJdbcPort")
    def reset_jdbc_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJdbcPort", []))

    @jsii.member(jsii_name="resetLastActivityTime")
    def reset_last_activity_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastActivityTime", []))

    @jsii.member(jsii_name="resetLastStateLossTime")
    def reset_last_state_loss_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastStateLossTime", []))

    @jsii.member(jsii_name="resetNodeTypeId")
    def reset_node_type_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeTypeId", []))

    @jsii.member(jsii_name="resetNumWorkers")
    def reset_num_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumWorkers", []))

    @jsii.member(jsii_name="resetPolicyId")
    def reset_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyId", []))

    @jsii.member(jsii_name="resetRuntimeEngine")
    def reset_runtime_engine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimeEngine", []))

    @jsii.member(jsii_name="resetSingleUserName")
    def reset_single_user_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleUserName", []))

    @jsii.member(jsii_name="resetSparkConf")
    def reset_spark_conf(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkConf", []))

    @jsii.member(jsii_name="resetSparkContextId")
    def reset_spark_context_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkContextId", []))

    @jsii.member(jsii_name="resetSparkEnvVars")
    def reset_spark_env_vars(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkEnvVars", []))

    @jsii.member(jsii_name="resetSshPublicKeys")
    def reset_ssh_public_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshPublicKeys", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @jsii.member(jsii_name="resetStateMessage")
    def reset_state_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStateMessage", []))

    @jsii.member(jsii_name="resetTerminateTime")
    def reset_terminate_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminateTime", []))

    @jsii.member(jsii_name="resetTerminationReason")
    def reset_termination_reason(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminationReason", []))

    @builtins.property
    @jsii.member(jsii_name="autoscale")
    def autoscale(self) -> DataDatabricksClusterClusterInfoAutoscaleOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoAutoscaleOutputReference, jsii.get(self, "autoscale"))

    @builtins.property
    @jsii.member(jsii_name="awsAttributes")
    def aws_attributes(
        self,
    ) -> DataDatabricksClusterClusterInfoAwsAttributesOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoAwsAttributesOutputReference, jsii.get(self, "awsAttributes"))

    @builtins.property
    @jsii.member(jsii_name="azureAttributes")
    def azure_attributes(
        self,
    ) -> DataDatabricksClusterClusterInfoAzureAttributesOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoAzureAttributesOutputReference, jsii.get(self, "azureAttributes"))

    @builtins.property
    @jsii.member(jsii_name="clusterLogConf")
    def cluster_log_conf(
        self,
    ) -> DataDatabricksClusterClusterInfoClusterLogConfOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoClusterLogConfOutputReference, jsii.get(self, "clusterLogConf"))

    @builtins.property
    @jsii.member(jsii_name="clusterLogStatus")
    def cluster_log_status(
        self,
    ) -> DataDatabricksClusterClusterInfoClusterLogStatusOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoClusterLogStatusOutputReference, jsii.get(self, "clusterLogStatus"))

    @builtins.property
    @jsii.member(jsii_name="dockerImage")
    def docker_image(
        self,
    ) -> DataDatabricksClusterClusterInfoDockerImageOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoDockerImageOutputReference, jsii.get(self, "dockerImage"))

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> DataDatabricksClusterClusterInfoDriverOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoDriverOutputReference, jsii.get(self, "driver"))

    @builtins.property
    @jsii.member(jsii_name="executors")
    def executors(self) -> DataDatabricksClusterClusterInfoExecutorsList:
        return typing.cast(DataDatabricksClusterClusterInfoExecutorsList, jsii.get(self, "executors"))

    @builtins.property
    @jsii.member(jsii_name="gcpAttributes")
    def gcp_attributes(
        self,
    ) -> DataDatabricksClusterClusterInfoGcpAttributesOutputReference:
        return typing.cast(DataDatabricksClusterClusterInfoGcpAttributesOutputReference, jsii.get(self, "gcpAttributes"))

    @builtins.property
    @jsii.member(jsii_name="initScripts")
    def init_scripts(self) -> DataDatabricksClusterClusterInfoInitScriptsList:
        return typing.cast(DataDatabricksClusterClusterInfoInitScriptsList, jsii.get(self, "initScripts"))

    @builtins.property
    @jsii.member(jsii_name="terminationReason")
    def termination_reason(
        self,
    ) -> "DataDatabricksClusterClusterInfoTerminationReasonOutputReference":
        return typing.cast("DataDatabricksClusterClusterInfoTerminationReasonOutputReference", jsii.get(self, "terminationReason"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleInput")
    def autoscale_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoAutoscale]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoAutoscale], jsii.get(self, "autoscaleInput"))

    @builtins.property
    @jsii.member(jsii_name="autoterminationMinutesInput")
    def autotermination_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autoterminationMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="awsAttributesInput")
    def aws_attributes_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoAwsAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoAwsAttributes], jsii.get(self, "awsAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="azureAttributesInput")
    def azure_attributes_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoAzureAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoAzureAttributes], jsii.get(self, "azureAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterCoresInput")
    def cluster_cores_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "clusterCoresInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterLogConfInput")
    def cluster_log_conf_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoClusterLogConf]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoClusterLogConf], jsii.get(self, "clusterLogConfInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterLogStatusInput")
    def cluster_log_status_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoClusterLogStatus]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoClusterLogStatus], jsii.get(self, "clusterLogStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterMemoryMbInput")
    def cluster_memory_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "clusterMemoryMbInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterNameInput")
    def cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterSourceInput")
    def cluster_source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="creatorUserNameInput")
    def creator_user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "creatorUserNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customTagsInput")
    def custom_tags_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSecurityModeInput")
    def data_security_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSecurityModeInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTagsInput")
    def default_tags_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "defaultTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerImageInput")
    def docker_image_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoDockerImage]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoDockerImage], jsii.get(self, "dockerImageInput"))

    @builtins.property
    @jsii.member(jsii_name="driverInput")
    def driver_input(self) -> typing.Optional[DataDatabricksClusterClusterInfoDriver]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoDriver], jsii.get(self, "driverInput"))

    @builtins.property
    @jsii.member(jsii_name="driverInstancePoolIdInput")
    def driver_instance_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInstancePoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="driverNodeTypeIdInput")
    def driver_node_type_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverNodeTypeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="enableElasticDiskInput")
    def enable_elastic_disk_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableElasticDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="enableLocalDiskEncryptionInput")
    def enable_local_disk_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableLocalDiskEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="executorsInput")
    def executors_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksClusterClusterInfoExecutors]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksClusterClusterInfoExecutors]]], jsii.get(self, "executorsInput"))

    @builtins.property
    @jsii.member(jsii_name="gcpAttributesInput")
    def gcp_attributes_input(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoGcpAttributes]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoGcpAttributes], jsii.get(self, "gcpAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="initScriptsInput")
    def init_scripts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksClusterClusterInfoInitScripts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksClusterClusterInfoInitScripts]]], jsii.get(self, "initScriptsInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolIdInput")
    def instance_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instancePoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="jdbcPortInput")
    def jdbc_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "jdbcPortInput"))

    @builtins.property
    @jsii.member(jsii_name="lastActivityTimeInput")
    def last_activity_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lastActivityTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="lastStateLossTimeInput")
    def last_state_loss_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lastStateLossTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeTypeIdInput")
    def node_type_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeTypeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="numWorkersInput")
    def num_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="policyIdInput")
    def policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeEngineInput")
    def runtime_engine_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeEngineInput"))

    @builtins.property
    @jsii.member(jsii_name="singleUserNameInput")
    def single_user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "singleUserNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkConfInput")
    def spark_conf_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sparkConfInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkContextIdInput")
    def spark_context_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sparkContextIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkEnvVarsInput")
    def spark_env_vars_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sparkEnvVarsInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkVersionInput")
    def spark_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sparkVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeysInput")
    def ssh_public_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sshPublicKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="stateMessageInput")
    def state_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="terminateTimeInput")
    def terminate_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "terminateTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="terminationReasonInput")
    def termination_reason_input(
        self,
    ) -> typing.Optional["DataDatabricksClusterClusterInfoTerminationReason"]:
        return typing.cast(typing.Optional["DataDatabricksClusterClusterInfoTerminationReason"], jsii.get(self, "terminationReasonInput"))

    @builtins.property
    @jsii.member(jsii_name="autoterminationMinutes")
    def autotermination_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autoterminationMinutes"))

    @autotermination_minutes.setter
    def autotermination_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65d267c7aa4618874e3058a0669bdecbc9fbef1d7fd27a91a6bbf53ebce5654a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoterminationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="clusterCores")
    def cluster_cores(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "clusterCores"))

    @cluster_cores.setter
    def cluster_cores(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23fbb6506ac4b08e2b1001a19e1f7b1e3117fcd19a8cb80040c62834942c3a20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterCores", value)

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad3dba70766ab23c115cea87cdb8028bf4599bc8f3f7b81dc199fb62b1ee77ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="clusterMemoryMb")
    def cluster_memory_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "clusterMemoryMb"))

    @cluster_memory_mb.setter
    def cluster_memory_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9024919c59a95706eb27cb2edf93a3b51c0e588628d50bdcf9aaa845e7031cd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterMemoryMb", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad8917de4713abe1ca0211a753688d856d08e74650eb1a20f7882f21f0a6b263)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="clusterSource")
    def cluster_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterSource"))

    @cluster_source.setter
    def cluster_source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5560e38fd0ee898c1b7da55b51b915eca3364a069d2997aff3941e36afc94a76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterSource", value)

    @builtins.property
    @jsii.member(jsii_name="creatorUserName")
    def creator_user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creatorUserName"))

    @creator_user_name.setter
    def creator_user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae6de81f9a1a015ca237b396264c543f998078ce3beb4a06ae8820cef8eb7dbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creatorUserName", value)

    @builtins.property
    @jsii.member(jsii_name="customTags")
    def custom_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customTags"))

    @custom_tags.setter
    def custom_tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__939281136a03599aeeb96a2e5a750648af0cb859b747820a251f664c4b98f44d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customTags", value)

    @builtins.property
    @jsii.member(jsii_name="dataSecurityMode")
    def data_security_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSecurityMode"))

    @data_security_mode.setter
    def data_security_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a864936b156c5a96ff7c7a249648f9f19c2a7e14b25999e288ae1abe3026f6f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSecurityMode", value)

    @builtins.property
    @jsii.member(jsii_name="defaultTags")
    def default_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "defaultTags"))

    @default_tags.setter
    def default_tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03c68a6394024d635d8c9e27ec4569d59044c8d7c5e7708ff566a57f710b34e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTags", value)

    @builtins.property
    @jsii.member(jsii_name="driverInstancePoolId")
    def driver_instance_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driverInstancePoolId"))

    @driver_instance_pool_id.setter
    def driver_instance_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8c0d2fcb69e22129a0cb5579685664cff0b1702ffaea92bd785c41e3e0330cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverInstancePoolId", value)

    @builtins.property
    @jsii.member(jsii_name="driverNodeTypeId")
    def driver_node_type_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driverNodeTypeId"))

    @driver_node_type_id.setter
    def driver_node_type_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6ec5924a3362288d6d6619ab505130ecc0f70246de9eef2f8dd05320a074b0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverNodeTypeId", value)

    @builtins.property
    @jsii.member(jsii_name="enableElasticDisk")
    def enable_elastic_disk(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableElasticDisk"))

    @enable_elastic_disk.setter
    def enable_elastic_disk(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb04e08cf4977f79b73f75533a02248c55e809460afd824563cdd901281c466f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableElasticDisk", value)

    @builtins.property
    @jsii.member(jsii_name="enableLocalDiskEncryption")
    def enable_local_disk_encryption(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableLocalDiskEncryption"))

    @enable_local_disk_encryption.setter
    def enable_local_disk_encryption(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aec274539d01901565514c00f8051b58a5358f231de4ea96d522627786acecc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableLocalDiskEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="instancePoolId")
    def instance_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instancePoolId"))

    @instance_pool_id.setter
    def instance_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9db910bc9a465d4148ae55dfb280853531798dc9a6bacff4f518077b17d769c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instancePoolId", value)

    @builtins.property
    @jsii.member(jsii_name="jdbcPort")
    def jdbc_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "jdbcPort"))

    @jdbc_port.setter
    def jdbc_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab17b1c8ba17049fc665388b4105987aa12c23a252b5889aefd58c59fdcae7bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jdbcPort", value)

    @builtins.property
    @jsii.member(jsii_name="lastActivityTime")
    def last_activity_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lastActivityTime"))

    @last_activity_time.setter
    def last_activity_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ab84307e93ddd56059108657f730d8f708a49ce196ae2d2a57ffcc2283af3f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastActivityTime", value)

    @builtins.property
    @jsii.member(jsii_name="lastStateLossTime")
    def last_state_loss_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lastStateLossTime"))

    @last_state_loss_time.setter
    def last_state_loss_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59a8ab437663f050fd4f8e19323a9bcda3e5292b23ab199e6c828eeb36430f8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastStateLossTime", value)

    @builtins.property
    @jsii.member(jsii_name="nodeTypeId")
    def node_type_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeTypeId"))

    @node_type_id.setter
    def node_type_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__112b5ec27f4cfcc85cadaa3a8cb64ed39c8d5b637b0a4a81e3d0ddaea1fe12b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeTypeId", value)

    @builtins.property
    @jsii.member(jsii_name="numWorkers")
    def num_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numWorkers"))

    @num_workers.setter
    def num_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3112ba76c6f857748cb59e944acd6512efcda0d7942088ba640bbf7b4b55072)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyId"))

    @policy_id.setter
    def policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b93be6536d46527da1d420f2ee55c103b9d2fd36fe4d4f28ec2cb1db01d6d3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyId", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeEngine")
    def runtime_engine(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtimeEngine"))

    @runtime_engine.setter
    def runtime_engine(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b91e2f689105ee8f43661a681654db91f77524c97fb6503fbfdf7c8df1a03645)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeEngine", value)

    @builtins.property
    @jsii.member(jsii_name="singleUserName")
    def single_user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "singleUserName"))

    @single_user_name.setter
    def single_user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8545f416f44ccaa7d720acc248bb78b55a4b3733eceb8bc18d531c49d196430)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singleUserName", value)

    @builtins.property
    @jsii.member(jsii_name="sparkConf")
    def spark_conf(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sparkConf"))

    @spark_conf.setter
    def spark_conf(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b63a478f178e1a593d233a0d69b3de74e37dd49089a93370ab0f61b0fcf6563b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkConf", value)

    @builtins.property
    @jsii.member(jsii_name="sparkContextId")
    def spark_context_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sparkContextId"))

    @spark_context_id.setter
    def spark_context_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20b097e48b4ec4b79210f2dbc13adad0bae27215f154ae868280f647b8307ceb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkContextId", value)

    @builtins.property
    @jsii.member(jsii_name="sparkEnvVars")
    def spark_env_vars(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sparkEnvVars"))

    @spark_env_vars.setter
    def spark_env_vars(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98f75e28cfee35227add37e5bdba775c0075ee044ecaad0e822d8d0ae36f0cca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkEnvVars", value)

    @builtins.property
    @jsii.member(jsii_name="sparkVersion")
    def spark_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sparkVersion"))

    @spark_version.setter
    def spark_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c29c59f956839c25145822913b77825069bb02924eec652051fb4bdbfedf8c4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkVersion", value)

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeys")
    def ssh_public_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sshPublicKeys"))

    @ssh_public_keys.setter
    def ssh_public_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7087882a7261dcf5b23ee3005a69bc2347aeb5bbeda5bc91f4bb99a0a3b7e92a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPublicKeys", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3427bf46d5d988c265b9d6c73dcafc49588a8c25d2b9b28bdeff33bfee772ac8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__393c4198ec6f90a9237c53de104328f6008566d2b43e5befef097c19ccc29548)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="stateMessage")
    def state_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stateMessage"))

    @state_message.setter
    def state_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80a95099c6d634f959332e758b2a9f93a5e0986026a6eaf5a0fcad7de5536d9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateMessage", value)

    @builtins.property
    @jsii.member(jsii_name="terminateTime")
    def terminate_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "terminateTime"))

    @terminate_time.setter
    def terminate_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aaf2fb81169cf1a05635f045af091e0bcda9f73db95d1c1a23ee68a7cc2680f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terminateTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataDatabricksClusterClusterInfo]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b332bab1c15e177be17481722c38ef9c3eda80e9f8c025c9f6e4c09f08eded40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoTerminationReason",
    jsii_struct_bases=[],
    name_mapping={"code": "code", "parameters": "parameters", "type": "type"},
)
class DataDatabricksClusterClusterInfoTerminationReason:
    def __init__(
        self,
        *,
        code: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#code DataDatabricksCluster#code}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#parameters DataDatabricksCluster#parameters}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#type DataDatabricksCluster#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__948788c3d878fa52c616c2cb5ff30909bc3b8c169ad7c5c6ed9538bf8c56b94d)
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if code is not None:
            self._values["code"] = code
        if parameters is not None:
            self._values["parameters"] = parameters
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#code DataDatabricksCluster#code}.'''
        result = self._values.get("code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#parameters DataDatabricksCluster#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#type DataDatabricksCluster#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterClusterInfoTerminationReason(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksClusterClusterInfoTerminationReasonOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterClusterInfoTerminationReasonOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14408cfd61959624e645ec438a2e81f35362d23d8db5e2ae247bab800fe9f423)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCode")
    def reset_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCode", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="codeInput")
    def code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codeInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "code"))

    @code.setter
    def code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14bee2b3e7c3ee15e68ba3f90c99872bb209fbc66e120073b8d742b2850d365f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10e7603e4f2f52be9489298713ed5db9452fcc7e630143ea89468ec72bb88b22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8f67a5a6bb602f2050ebbb44bb4e417f9a3fadd24154f8d1bdbb25023033ac1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksClusterClusterInfoTerminationReason]:
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfoTerminationReason], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksClusterClusterInfoTerminationReason],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__742448ae8db46afc08e0ef81b1551e0af67538071b2cc0d3c29c089d2e2fb8cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksCluster.DataDatabricksClusterConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster_id": "clusterId",
        "cluster_info": "clusterInfo",
        "cluster_name": "clusterName",
        "id": "id",
    },
)
class DataDatabricksClusterConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        cluster_info: typing.Optional[typing.Union[DataDatabricksClusterClusterInfo, typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_id DataDatabricksCluster#cluster_id}.
        :param cluster_info: cluster_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_info DataDatabricksCluster#cluster_info}
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_name DataDatabricksCluster#cluster_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#id DataDatabricksCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cluster_info, dict):
            cluster_info = DataDatabricksClusterClusterInfo(**cluster_info)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c58d529727cec39a12f8ff1df4dfd671281ab07e46e96e721fe0a40d0872e33d)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument cluster_info", value=cluster_info, expected_type=type_hints["cluster_info"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if cluster_id is not None:
            self._values["cluster_id"] = cluster_id
        if cluster_info is not None:
            self._values["cluster_info"] = cluster_info
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_id DataDatabricksCluster#cluster_id}.'''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_info(self) -> typing.Optional[DataDatabricksClusterClusterInfo]:
        '''cluster_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_info DataDatabricksCluster#cluster_info}
        '''
        result = self._values.get("cluster_info")
        return typing.cast(typing.Optional[DataDatabricksClusterClusterInfo], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#cluster_name DataDatabricksCluster#cluster_name}.'''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/cluster#id DataDatabricksCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataDatabricksCluster",
    "DataDatabricksClusterClusterInfo",
    "DataDatabricksClusterClusterInfoAutoscale",
    "DataDatabricksClusterClusterInfoAutoscaleOutputReference",
    "DataDatabricksClusterClusterInfoAwsAttributes",
    "DataDatabricksClusterClusterInfoAwsAttributesOutputReference",
    "DataDatabricksClusterClusterInfoAzureAttributes",
    "DataDatabricksClusterClusterInfoAzureAttributesOutputReference",
    "DataDatabricksClusterClusterInfoClusterLogConf",
    "DataDatabricksClusterClusterInfoClusterLogConfDbfs",
    "DataDatabricksClusterClusterInfoClusterLogConfDbfsOutputReference",
    "DataDatabricksClusterClusterInfoClusterLogConfOutputReference",
    "DataDatabricksClusterClusterInfoClusterLogConfS3",
    "DataDatabricksClusterClusterInfoClusterLogConfS3OutputReference",
    "DataDatabricksClusterClusterInfoClusterLogStatus",
    "DataDatabricksClusterClusterInfoClusterLogStatusOutputReference",
    "DataDatabricksClusterClusterInfoDockerImage",
    "DataDatabricksClusterClusterInfoDockerImageBasicAuth",
    "DataDatabricksClusterClusterInfoDockerImageBasicAuthOutputReference",
    "DataDatabricksClusterClusterInfoDockerImageOutputReference",
    "DataDatabricksClusterClusterInfoDriver",
    "DataDatabricksClusterClusterInfoDriverNodeAwsAttributes",
    "DataDatabricksClusterClusterInfoDriverNodeAwsAttributesOutputReference",
    "DataDatabricksClusterClusterInfoDriverOutputReference",
    "DataDatabricksClusterClusterInfoExecutors",
    "DataDatabricksClusterClusterInfoExecutorsList",
    "DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes",
    "DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributesOutputReference",
    "DataDatabricksClusterClusterInfoExecutorsOutputReference",
    "DataDatabricksClusterClusterInfoGcpAttributes",
    "DataDatabricksClusterClusterInfoGcpAttributesOutputReference",
    "DataDatabricksClusterClusterInfoInitScripts",
    "DataDatabricksClusterClusterInfoInitScriptsAbfss",
    "DataDatabricksClusterClusterInfoInitScriptsAbfssOutputReference",
    "DataDatabricksClusterClusterInfoInitScriptsDbfs",
    "DataDatabricksClusterClusterInfoInitScriptsDbfsOutputReference",
    "DataDatabricksClusterClusterInfoInitScriptsFile",
    "DataDatabricksClusterClusterInfoInitScriptsFileOutputReference",
    "DataDatabricksClusterClusterInfoInitScriptsGcs",
    "DataDatabricksClusterClusterInfoInitScriptsGcsOutputReference",
    "DataDatabricksClusterClusterInfoInitScriptsList",
    "DataDatabricksClusterClusterInfoInitScriptsOutputReference",
    "DataDatabricksClusterClusterInfoInitScriptsS3",
    "DataDatabricksClusterClusterInfoInitScriptsS3OutputReference",
    "DataDatabricksClusterClusterInfoOutputReference",
    "DataDatabricksClusterClusterInfoTerminationReason",
    "DataDatabricksClusterClusterInfoTerminationReasonOutputReference",
    "DataDatabricksClusterConfig",
]

publication.publish()

def _typecheckingstub__f1c34b6757ec75a7e345694812782e8b53d0c659ffbbb23408d5fb560269d735(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    cluster_id: typing.Optional[builtins.str] = None,
    cluster_info: typing.Optional[typing.Union[DataDatabricksClusterClusterInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1362b5c144022c4061f55358a67328d0bfdb54fa18ca548a90a41457417ed814(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaac8b5d6ffc42289a6393bd5bb7aecf591a05d7fdabffed88a8e77014688a03(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__966dd3e8ead2ea020bea9709d896fa618505ab438e8c09f91c442f59713092b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__296ce555691258d87ac7958787edcb938924edb40d4f8f66eef6bb634906db09(
    *,
    default_tags: typing.Mapping[builtins.str, builtins.str],
    spark_version: builtins.str,
    state: builtins.str,
    autoscale: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoAutoscale, typing.Dict[builtins.str, typing.Any]]] = None,
    autotermination_minutes: typing.Optional[jsii.Number] = None,
    aws_attributes: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoAwsAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_attributes: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoAzureAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_cores: typing.Optional[jsii.Number] = None,
    cluster_id: typing.Optional[builtins.str] = None,
    cluster_log_conf: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoClusterLogConf, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_log_status: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoClusterLogStatus, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_memory_mb: typing.Optional[jsii.Number] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    cluster_source: typing.Optional[builtins.str] = None,
    creator_user_name: typing.Optional[builtins.str] = None,
    custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    data_security_mode: typing.Optional[builtins.str] = None,
    docker_image: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoDockerImage, typing.Dict[builtins.str, typing.Any]]] = None,
    driver: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoDriver, typing.Dict[builtins.str, typing.Any]]] = None,
    driver_instance_pool_id: typing.Optional[builtins.str] = None,
    driver_node_type_id: typing.Optional[builtins.str] = None,
    enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_local_disk_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    executors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksClusterClusterInfoExecutors, typing.Dict[builtins.str, typing.Any]]]]] = None,
    gcp_attributes: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoGcpAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    init_scripts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksClusterClusterInfoInitScripts, typing.Dict[builtins.str, typing.Any]]]]] = None,
    instance_pool_id: typing.Optional[builtins.str] = None,
    jdbc_port: typing.Optional[jsii.Number] = None,
    last_activity_time: typing.Optional[jsii.Number] = None,
    last_state_loss_time: typing.Optional[jsii.Number] = None,
    node_type_id: typing.Optional[builtins.str] = None,
    num_workers: typing.Optional[jsii.Number] = None,
    policy_id: typing.Optional[builtins.str] = None,
    runtime_engine: typing.Optional[builtins.str] = None,
    single_user_name: typing.Optional[builtins.str] = None,
    spark_conf: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    spark_context_id: typing.Optional[jsii.Number] = None,
    spark_env_vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    start_time: typing.Optional[jsii.Number] = None,
    state_message: typing.Optional[builtins.str] = None,
    terminate_time: typing.Optional[jsii.Number] = None,
    termination_reason: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoTerminationReason, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49a9c2ad50c160d7885fc28045c24ffa6f000e4ccb7f453c8360c7a3d77148c8(
    *,
    max_workers: typing.Optional[jsii.Number] = None,
    min_workers: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61a5c81af86f67b5c2927d3fa8ca85a14b8feb06e1b3597b657d85c6e5e7293c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__074118ac5a361f1e65608b670769f47864bacd1802100f5247c02d79679c5076(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f9523a52774ddd02d17b6f470d6f590fdc919820f956b2077fccc98011d6e62(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ceaa988b67b8b30e43067d9e427d6344f0506649836b3840a75953f3015bc60(
    value: typing.Optional[DataDatabricksClusterClusterInfoAutoscale],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e817bc42c3681c9e8a03b7ecbd8503f33cea3d3e6f0e84468c0aac93b4eaa57(
    *,
    availability: typing.Optional[builtins.str] = None,
    ebs_volume_count: typing.Optional[jsii.Number] = None,
    ebs_volume_size: typing.Optional[jsii.Number] = None,
    ebs_volume_type: typing.Optional[builtins.str] = None,
    first_on_demand: typing.Optional[jsii.Number] = None,
    instance_profile_arn: typing.Optional[builtins.str] = None,
    spot_bid_price_percent: typing.Optional[jsii.Number] = None,
    zone_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4962c90e92675d9b69d3d07780b1aa9353de6d9caeca25af34d73638cca4d8da(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90389a4992d69cce8807429e5298bc2c1cc1177f98116cb4ac91e6bd7ad39bf8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e463c10c4064d2a1cf2384b8bd86c677b3e44b47a5c38ff5d9d5da7a063d0ce(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a7c555fb9864e7b7ea2893ee8656bec28388e6efe8a644f8425e3b4295c878e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d79a78c6a83e18463cf1032a4c82918c1070118b6f25e7343cc13a495b1800c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd0066c7f5d2fceee518fe6986fcfc373b148dd31ad3ff7f979c63496af978c3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26b3a65bbd686c8664a67d9b401419d88c3c9d286d5a4ae2c9c0122cfa13b4d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a089a5e2a5f599ff3f3f89347470dbdb5a96138da0f250f7f3f9366dae03e74e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a568ac2785e081711a111a7c33daa49bf86ab50998bc46ac3d0d3375b24ed8ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d171c079811861faa12c6cc55b94c0f801309ac1b3dd004f872f295bdbcb705(
    value: typing.Optional[DataDatabricksClusterClusterInfoAwsAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efc875c53a47a7040774d946307573f621908820fb158100ba31419d34d18ee1(
    *,
    availability: typing.Optional[builtins.str] = None,
    first_on_demand: typing.Optional[jsii.Number] = None,
    spot_bid_max_price: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba9f238e842f58ba6614df8520f163e45873948a2ec8746392379f74946a3993(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__551e03eb74c653fe04aeedf2bba8986e0db20fa09b22ed7df3752c2697867bbc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8769f9cfdb32087c731dc2bf75087e8023b4869017034772937dc415dfc749a2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__585c0ce9ac5cd64a4008cd7efcc0435388b40630e746dcfb3987bc17b3ac310e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d64eace0e1c5d2053982513a78939185e0041d4492cfe4a8d0e430935f5b907(
    value: typing.Optional[DataDatabricksClusterClusterInfoAzureAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__308585a3320755d3d67595bee59528447495820e87ef84d56eabc9d8a2ddea58(
    *,
    dbfs: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoClusterLogConfDbfs, typing.Dict[builtins.str, typing.Any]]] = None,
    s3: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoClusterLogConfS3, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c778629d1c4e9c102b00bf38ac827799b2c6aaf332e02c4ee8a9c3f7b0444709(
    *,
    destination: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a085a9c7d70ba5e0cf9cab09b260b1e8d56d5c75182914a68c23350ad53e154(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37393d2882c51e19ab26cb34984551e11d6476a465ff79e20d91a404c288dc2d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42671a53bc53109241ab3115986b5503e4f5c46adb890b9ef1406c4c0997645c(
    value: typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfDbfs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caa4816ee34df49743bd9c60c38049bbe415e66512b96dd0f503fb3263385089(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c8b57b13973a8886694e958656298ae80a259caa9b53e6cba5b5b0734330653(
    value: typing.Optional[DataDatabricksClusterClusterInfoClusterLogConf],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33e2eae95f0f0da44c2e421afc22f20f1052b57fbf255bcacbd5b39c2f4250f3(
    *,
    destination: builtins.str,
    canned_acl: typing.Optional[builtins.str] = None,
    enable_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encryption_type: typing.Optional[builtins.str] = None,
    endpoint: typing.Optional[builtins.str] = None,
    kms_key: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__790db488da489570a2eb67666dadb7e463ea57ad7cd3efe097f3ff1e66b688cd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3213b9cdea742252fb689169b7d320ab637df403b49bb098421b0f2005a55cfb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6820c2064d82e918fdd458d95ef83e3cb9d1964115f7898a867720f501e7f66e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3d27d91fde45a20d321adfaf8d3d207d227bff609fce5f21e2a01e50d07d20c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0259bd6eb5c3c1197edc3dd47d99c8ef4c364f6f7cafc981eaca936ec7ec47c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0204aaed752737d1f1a04b88cfd8dff8e80757d245c9764ce081c78c3c79c7e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dd4adf364d758b69f2bd5d6c3cf3f6facdfc2217f45462917f6d873154eff8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f997e6ca3f20220100e1b301baf307cc60d5280f70adeb525e4ab01519850471(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecd84ac45c6f25991bd9e9499631527e6b653c2288d8ffc01ebdc0444f5e20b0(
    value: typing.Optional[DataDatabricksClusterClusterInfoClusterLogConfS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ff391eca99d5918bdc6c7c11a04dc394463f020e26749fcd5413125fe96e41a(
    *,
    last_attempted: typing.Optional[jsii.Number] = None,
    last_exception: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__085dc29d98a87251779c1e20fbff32d71c4cc041d89937b37d7a86e573308c5e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aa79b8140c59f273fded0557793db02805e10fb04f5d7a9fa6764b661c49d51(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c1dd3ca5c41cef546ae53ffa59ec1d0d5f7f8d54234094357db06abc68f99fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bb9f299d0656cd14dc8aab73fa96c932a3429e3551539379e2bc42aa2cb7f38(
    value: typing.Optional[DataDatabricksClusterClusterInfoClusterLogStatus],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c158ce94ca43385a0084cf6e326d51c915a2eccef4a366d1188c48937f779aa9(
    *,
    url: builtins.str,
    basic_auth: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoDockerImageBasicAuth, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf62467def032fea8f55c256492570831bbaf48f6254bb9643384c6e29f2e4e9(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0049d37fd051e7b304900466750303023a3f9d01f09ae85a7cebd42467047e1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc966efec25f2338418462de7de892c30f2326d9b67befd6136387269912dfb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad3538dd56aa772ee966f25abd298005ed2bcb91516245fd1a5b73eaf7ade85b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__281c56a91f9392b534ad7291a3ce9c107f355dcf591f262b316d3cc9391acaf4(
    value: typing.Optional[DataDatabricksClusterClusterInfoDockerImageBasicAuth],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f997dd0c9902453755c451dafe7a992a29255aa5b7f849a1d3764e8961f033f9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf2f929c18dd13260d2cdeba2194bbef063a5224798eb0582d31222b820fadf2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93272fa6d29f7ce25d5cd05cc5ea9fcac18dc2f7eef14f06aeedb5d0e3c14ed2(
    value: typing.Optional[DataDatabricksClusterClusterInfoDockerImage],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba945cdb80dcfd9eefbab23cb273c6b2202336b1fc2ed61d3f31e93ee200ba56(
    *,
    host_private_ip: typing.Optional[builtins.str] = None,
    instance_id: typing.Optional[builtins.str] = None,
    node_aws_attributes: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoDriverNodeAwsAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    node_id: typing.Optional[builtins.str] = None,
    private_ip: typing.Optional[builtins.str] = None,
    public_dns: typing.Optional[builtins.str] = None,
    start_timestamp: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d02a39857fcca8e9f434fed94886dc65c4627d7cfa2008fb72dff0a1f0438d8f(
    *,
    is_spot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e4f95c12a5fb82e3d2a9908533f36c0cc6a951695cc6be0592f234eb48f5e1f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89f88c64d3d302cdb175d5387179bc15015aba92d23fafe4e53631057e0e7061(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23ac5740c877c415e9e209fc6980fc105baca6a09eaaecb8f79d20e5d39cc7cb(
    value: typing.Optional[DataDatabricksClusterClusterInfoDriverNodeAwsAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75d1f2ab40327660157f1ca53ba1c7e7e104d4be183cb203bbb07bcdba4d0aa4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6269da4c4e8e22c53c633e1a84ecc17989278e17f938d7dd78ecbc2c2791f50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e6217b4fdda4a43b9182bfae99be5e08ae3ca71be1bd7ca759cd699e0a012cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95c666feaad9064f1b42d9eaab632213e471a7c9cc6d4ba73c2011829122799b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5ce0b251e0f71bdb99b5e688cb7a64a5dd9f8a114eb5c5eddacd443f0a734cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b2e19bc978bdccbbbdc261896d8ed189b83773e03834ad8c27374e3255e3f7a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__940f566898bc345cf8823d5d89706a421d05b7f883d747dfdd6df49a1a6569e4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3408ab9000ed503aaad0c3d9f036334817bd68d835ed4e7395878f1c61eaeef(
    value: typing.Optional[DataDatabricksClusterClusterInfoDriver],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56efd4c4e105f2524c7572ea493a933476856da95ef8ad6affd3d077d281bed6(
    *,
    host_private_ip: typing.Optional[builtins.str] = None,
    instance_id: typing.Optional[builtins.str] = None,
    node_aws_attributes: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    node_id: typing.Optional[builtins.str] = None,
    private_ip: typing.Optional[builtins.str] = None,
    public_dns: typing.Optional[builtins.str] = None,
    start_timestamp: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89ae0df44d453cdabce14936c61460213d097863f97d5c9eed6261aff75dc501(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e57016b3f1efe7024856a66c4bf50714b1e4f08227c7371c6dc6532734d54577(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b46adb6d396f434af13485c528527327be502148bb1a7656de58d377607a63c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58506aed2551fffab49cbbe3d6cefe030e4b2c80ea9ddfecc9e38519dfda125b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dcf162b681a2d8f4bdbc9994a6a728fe4d7456b872b3f89722a5305f3947786(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a42cd687030d3d2aba16097689eac4308916566604f31171a537fe5af932e7b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksClusterClusterInfoExecutors]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__126f158d2851f755515aba5281a41b7316c8ee640d980fa2fce392c68304c2bf(
    *,
    is_spot: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a7534255031b0a290ea7fab12cc0c63ed8cfe34660f39b1ffb4ddbed619125e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__008b1344f9184da4ac0503d8e1882c7703e741a3ade2e22f844c4a499d916283(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__932a0ff22a17ab7b2a60ab65207e328012ca69aea9d57d135b6d207a454b929f(
    value: typing.Optional[DataDatabricksClusterClusterInfoExecutorsNodeAwsAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__556a7b9afe4f1c947a73ec4c2459f41a291efa104908026b913382850d1704ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41ddeb059395685fb39b73bf9be4e4691235c152089bee63aeb12cd429859703(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__387adf8266f292631fae4e2eaa13e7572b27bd402ac76e90345c4945ab61abe0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b1798a914e13218deb01290ab183b20f2c919ec9f7e707d113e779f829160b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e2ed538eaa9a517dcccbb14271d22daea95e362d17f2a27e5ed97a749a22c14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c02444a028233fabd1d4b93f7630827e014f4d7cffb263f7e52743f650927dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__195c3c3289a57b2fdebc7911ff0d731857b3665511a1994848a8ef91c34d58f5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c8ac26df5386e8bef0385e4ce4d696e0c31995315370130ebb01e90b8d7f352(
    value: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoExecutors, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba2c03c51d70d98648a12cd093b81a8c1f6b5bab5ddbfd20e19fe056fac51dbf(
    *,
    availability: typing.Optional[builtins.str] = None,
    boot_disk_size: typing.Optional[jsii.Number] = None,
    google_service_account: typing.Optional[builtins.str] = None,
    use_preemptible_executors: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    zone_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b2ef7bbcf01e0fa9e7a4511af4fbd0806b28d2dc94a3d0dee1685cc6c66ed98(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64c6d8c2e8f5944ec2ffd313e24c6ac60bed8d66342042fcd1f207053d404ccc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c134581a3a1200e69dc7f9858891dbb5ca570a7b09fae372ad758f4b9ac965e6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c3422fcab8c06581ca43819fb6317d826eec5c097e5190c408c307ba6470ccf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__536df40dc7a7f333146091401e3896f5de1adb8f915014eb2ca75f99beb71dd6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec314f8536c8e261a5847643feb7068efdf02f47d765bba59959f8c13630bc62(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf1be6000bbfc150c2cb868e7fcd1faca3145dfb601077bbdc99bee027ddb51a(
    value: typing.Optional[DataDatabricksClusterClusterInfoGcpAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f2fda4455fb55433b211770e88c34ef7e5138c5aa4c96ca640cb26cd8902e53(
    *,
    abfss: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoInitScriptsAbfss, typing.Dict[builtins.str, typing.Any]]] = None,
    dbfs: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoInitScriptsDbfs, typing.Dict[builtins.str, typing.Any]]] = None,
    file: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoInitScriptsFile, typing.Dict[builtins.str, typing.Any]]] = None,
    gcs: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoInitScriptsGcs, typing.Dict[builtins.str, typing.Any]]] = None,
    s3: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoInitScriptsS3, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7377669a98248cd231d230670dd77d8343e541ee0bb7678707999e0c629e8d49(
    *,
    destination: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bf370a4dddb1d6fa8e0209dae625abd5846c3ff8eb3fb7bd00dbf0f08cc7431(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58cfeef92efb26a30aba96e9200de8c69a0034c8290de7e542d8fa0e33c4f10e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__600e3e5a8394425daa8943873527103778801f678a9bc0eb513ee66aee0399c1(
    value: typing.Optional[DataDatabricksClusterClusterInfoInitScriptsAbfss],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be97984f7218421372715a6c88921fcd88c197aad27f1e58aa0c04f07cb5a7b5(
    *,
    destination: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb3594326c12186d9b535f2d6bcd8a690aff0fda57195663483cd28675671733(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__965923c2ca40eb3683580f86de52175264697361ab1f184f7714d33934ec93d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f441f986ebaeee59e3ac14ecc2bd5f30f9472460fb6a9dcdfd12aadb4585476(
    value: typing.Optional[DataDatabricksClusterClusterInfoInitScriptsDbfs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a03a60dd66b8c60cf2077f013899619885215515532eba5f1a13306817074326(
    *,
    destination: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eacbfe350fab8de6177db90a6d16b665886ab3003c9867919702fda213632506(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62584ac48e40f905917bceb70dceb9cf45bc9ae4471ad95de420612ea0d4da98(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba0f9af0f1d3fbb8b64179dfa27855686fd9e53dfc91e4919173e7d11027ed5a(
    value: typing.Optional[DataDatabricksClusterClusterInfoInitScriptsFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79616c591bbfcce6e0db8859cd3c5020406b5dafff576a1ba8cf70155796d8b8(
    *,
    destination: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37e315b926dea0dd4a99c5f649f07312fed0527aefca9040d70671d1c919753e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8ce13203a859104b7ea76ff491859bc98965c2294c94f06169441ea7c9707ba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f6b1a59ea090d39952a8c34c846b05860268feaa3b709d6aac71373cc6fe14(
    value: typing.Optional[DataDatabricksClusterClusterInfoInitScriptsGcs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f109e758f9f3337d5e7809eac71f47cdb1527a69e48aa8975d134c28685c255d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b230b8a9df1396495562a7c4d9f7d5fbfd1375b53e93fdee241da252452292bf(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84d7c2a7e7483da9f34d1d8d3aa201383194b1323ad9075a215e289eb74e827b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02db248d8a755da48a8b24d42bc9beeaa6c3517a49bff21df9fe93f8422dfca4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa84f5579716197cc6af834b6a18faa31764de81068b7ac5e380e70cdb8a6e46(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13c6f62d6811d4515af5186f379beec2d3394a700ab213e03ccf814e739e4a67(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksClusterClusterInfoInitScripts]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b9407e55882007ebf5e9592e44c3c8085848d88126ce55551166dca07ffde8f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04b3bdb38afb5d5b1affad680e1239270d933832a8dc5a3bfad3b7e8354e3672(
    value: typing.Optional[typing.Union[DataDatabricksClusterClusterInfoInitScripts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b451b4782f3f50fc8f564ef934f4cb840af23d06c8ead6d303a9820ccd689d7(
    *,
    destination: builtins.str,
    canned_acl: typing.Optional[builtins.str] = None,
    enable_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encryption_type: typing.Optional[builtins.str] = None,
    endpoint: typing.Optional[builtins.str] = None,
    kms_key: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8410f080d04d4d869e23ac4e3f44d2441ece6b2207f61adf91262bebb21cb0e4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fd255279abbcde7ef40ca2ddca55675442e1cf83b471581d98f4bedbe931a34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d66353fe966001977ffa522e230db43da2f26d5210303c2aaa5ac9ef74a06308(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16ea180e9f879597f7bcd450326f0297b698b1f46bfc0720a1bba91fed0bc273(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a259654148ae1c820b012ee931e7157b4f3be6e5a206c927d0db9400a35e052(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09be604796cbd591a0149665c7c2688f11c3cdb3aad82ed196e8cd96f7769600(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dd815bf83d85cd20cb080c0277ee1685a0ca67ae1cad3161efef3ae6e3ab004(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__851bb1c3f8a93800d5db5e2587e84eeb1e842fae74ac6794308aaad6dffe2ff9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dc4c558106ea8f1c227d5dba38d240997a1d243f8fda4460e306b13d0685a3e(
    value: typing.Optional[DataDatabricksClusterClusterInfoInitScriptsS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e41e69d1871a4fdfca29f1a8a2725db7b893a525f568ec15427d0009d9d0b17(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e275d2e0126c10e109882a9b7f0c186162706b148d7d1580661abdd443d0669c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksClusterClusterInfoExecutors, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__501e51c92f6fa984891ab1c600485f18a229334fcaee3d3f9627141a622a10ed(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksClusterClusterInfoInitScripts, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65d267c7aa4618874e3058a0669bdecbc9fbef1d7fd27a91a6bbf53ebce5654a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23fbb6506ac4b08e2b1001a19e1f7b1e3117fcd19a8cb80040c62834942c3a20(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad3dba70766ab23c115cea87cdb8028bf4599bc8f3f7b81dc199fb62b1ee77ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9024919c59a95706eb27cb2edf93a3b51c0e588628d50bdcf9aaa845e7031cd6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad8917de4713abe1ca0211a753688d856d08e74650eb1a20f7882f21f0a6b263(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5560e38fd0ee898c1b7da55b51b915eca3364a069d2997aff3941e36afc94a76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae6de81f9a1a015ca237b396264c543f998078ce3beb4a06ae8820cef8eb7dbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__939281136a03599aeeb96a2e5a750648af0cb859b747820a251f664c4b98f44d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a864936b156c5a96ff7c7a249648f9f19c2a7e14b25999e288ae1abe3026f6f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03c68a6394024d635d8c9e27ec4569d59044c8d7c5e7708ff566a57f710b34e2(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8c0d2fcb69e22129a0cb5579685664cff0b1702ffaea92bd785c41e3e0330cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6ec5924a3362288d6d6619ab505130ecc0f70246de9eef2f8dd05320a074b0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb04e08cf4977f79b73f75533a02248c55e809460afd824563cdd901281c466f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aec274539d01901565514c00f8051b58a5358f231de4ea96d522627786acecc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9db910bc9a465d4148ae55dfb280853531798dc9a6bacff4f518077b17d769c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab17b1c8ba17049fc665388b4105987aa12c23a252b5889aefd58c59fdcae7bd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ab84307e93ddd56059108657f730d8f708a49ce196ae2d2a57ffcc2283af3f9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59a8ab437663f050fd4f8e19323a9bcda3e5292b23ab199e6c828eeb36430f8d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__112b5ec27f4cfcc85cadaa3a8cb64ed39c8d5b637b0a4a81e3d0ddaea1fe12b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3112ba76c6f857748cb59e944acd6512efcda0d7942088ba640bbf7b4b55072(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b93be6536d46527da1d420f2ee55c103b9d2fd36fe4d4f28ec2cb1db01d6d3d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b91e2f689105ee8f43661a681654db91f77524c97fb6503fbfdf7c8df1a03645(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8545f416f44ccaa7d720acc248bb78b55a4b3733eceb8bc18d531c49d196430(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b63a478f178e1a593d233a0d69b3de74e37dd49089a93370ab0f61b0fcf6563b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20b097e48b4ec4b79210f2dbc13adad0bae27215f154ae868280f647b8307ceb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98f75e28cfee35227add37e5bdba775c0075ee044ecaad0e822d8d0ae36f0cca(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c29c59f956839c25145822913b77825069bb02924eec652051fb4bdbfedf8c4a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7087882a7261dcf5b23ee3005a69bc2347aeb5bbeda5bc91f4bb99a0a3b7e92a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3427bf46d5d988c265b9d6c73dcafc49588a8c25d2b9b28bdeff33bfee772ac8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__393c4198ec6f90a9237c53de104328f6008566d2b43e5befef097c19ccc29548(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80a95099c6d634f959332e758b2a9f93a5e0986026a6eaf5a0fcad7de5536d9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aaf2fb81169cf1a05635f045af091e0bcda9f73db95d1c1a23ee68a7cc2680f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b332bab1c15e177be17481722c38ef9c3eda80e9f8c025c9f6e4c09f08eded40(
    value: typing.Optional[DataDatabricksClusterClusterInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__948788c3d878fa52c616c2cb5ff30909bc3b8c169ad7c5c6ed9538bf8c56b94d(
    *,
    code: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14408cfd61959624e645ec438a2e81f35362d23d8db5e2ae247bab800fe9f423(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14bee2b3e7c3ee15e68ba3f90c99872bb209fbc66e120073b8d742b2850d365f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10e7603e4f2f52be9489298713ed5db9452fcc7e630143ea89468ec72bb88b22(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8f67a5a6bb602f2050ebbb44bb4e417f9a3fadd24154f8d1bdbb25023033ac1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__742448ae8db46afc08e0ef81b1551e0af67538071b2cc0d3c29c089d2e2fb8cc(
    value: typing.Optional[DataDatabricksClusterClusterInfoTerminationReason],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c58d529727cec39a12f8ff1df4dfd671281ab07e46e96e721fe0a40d0872e33d(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cluster_id: typing.Optional[builtins.str] = None,
    cluster_info: typing.Optional[typing.Union[DataDatabricksClusterClusterInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
