'''
# `data_databricks_instance_pool`

Refer to the Terraform Registory for docs: [`data_databricks_instance_pool`](https://www.terraform.io/docs/providers/databricks/d/instance_pool).
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


class DataDatabricksInstancePool(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePool",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool databricks_instance_pool}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        pool_info: typing.Optional[typing.Union["DataDatabricksInstancePoolPoolInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool databricks_instance_pool} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#name DataDatabricksInstancePool#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#id DataDatabricksInstancePool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param pool_info: pool_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#pool_info DataDatabricksInstancePool#pool_info}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f7ca568f8f220243c16aeb14de0cde47815b31f062b1efd4ca3b2a6a9d57364)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataDatabricksInstancePoolConfig(
            name=name,
            id=id,
            pool_info=pool_info,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putPoolInfo")
    def put_pool_info(
        self,
        *,
        idle_instance_autotermination_minutes: jsii.Number,
        instance_pool_name: builtins.str,
        aws_attributes: typing.Optional[typing.Union["DataDatabricksInstancePoolPoolInfoAwsAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_attributes: typing.Optional[typing.Union["DataDatabricksInstancePoolPoolInfoAzureAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        disk_spec: typing.Optional[typing.Union["DataDatabricksInstancePoolPoolInfoDiskSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        gcp_attributes: typing.Optional[typing.Union["DataDatabricksInstancePoolPoolInfoGcpAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        instance_pool_fleet_attributes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        instance_pool_id: typing.Optional[builtins.str] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_idle_instances: typing.Optional[jsii.Number] = None,
        node_type_id: typing.Optional[builtins.str] = None,
        preloaded_docker_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksInstancePoolPoolInfoPreloadedDockerImage", typing.Dict[builtins.str, typing.Any]]]]] = None,
        preloaded_spark_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        state: typing.Optional[builtins.str] = None,
        stats: typing.Optional[typing.Union["DataDatabricksInstancePoolPoolInfoStats", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle_instance_autotermination_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#idle_instance_autotermination_minutes DataDatabricksInstancePool#idle_instance_autotermination_minutes}.
        :param instance_pool_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#instance_pool_name DataDatabricksInstancePool#instance_pool_name}.
        :param aws_attributes: aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#aws_attributes DataDatabricksInstancePool#aws_attributes}
        :param azure_attributes: azure_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#azure_attributes DataDatabricksInstancePool#azure_attributes}
        :param custom_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#custom_tags DataDatabricksInstancePool#custom_tags}.
        :param default_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#default_tags DataDatabricksInstancePool#default_tags}.
        :param disk_spec: disk_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#disk_spec DataDatabricksInstancePool#disk_spec}
        :param enable_elastic_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#enable_elastic_disk DataDatabricksInstancePool#enable_elastic_disk}.
        :param gcp_attributes: gcp_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#gcp_attributes DataDatabricksInstancePool#gcp_attributes}
        :param instance_pool_fleet_attributes: instance_pool_fleet_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#instance_pool_fleet_attributes DataDatabricksInstancePool#instance_pool_fleet_attributes}
        :param instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#instance_pool_id DataDatabricksInstancePool#instance_pool_id}.
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#max_capacity DataDatabricksInstancePool#max_capacity}.
        :param min_idle_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#min_idle_instances DataDatabricksInstancePool#min_idle_instances}.
        :param node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#node_type_id DataDatabricksInstancePool#node_type_id}.
        :param preloaded_docker_image: preloaded_docker_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#preloaded_docker_image DataDatabricksInstancePool#preloaded_docker_image}
        :param preloaded_spark_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#preloaded_spark_versions DataDatabricksInstancePool#preloaded_spark_versions}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#state DataDatabricksInstancePool#state}.
        :param stats: stats block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#stats DataDatabricksInstancePool#stats}
        '''
        value = DataDatabricksInstancePoolPoolInfo(
            idle_instance_autotermination_minutes=idle_instance_autotermination_minutes,
            instance_pool_name=instance_pool_name,
            aws_attributes=aws_attributes,
            azure_attributes=azure_attributes,
            custom_tags=custom_tags,
            default_tags=default_tags,
            disk_spec=disk_spec,
            enable_elastic_disk=enable_elastic_disk,
            gcp_attributes=gcp_attributes,
            instance_pool_fleet_attributes=instance_pool_fleet_attributes,
            instance_pool_id=instance_pool_id,
            max_capacity=max_capacity,
            min_idle_instances=min_idle_instances,
            node_type_id=node_type_id,
            preloaded_docker_image=preloaded_docker_image,
            preloaded_spark_versions=preloaded_spark_versions,
            state=state,
            stats=stats,
        )

        return typing.cast(None, jsii.invoke(self, "putPoolInfo", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPoolInfo")
    def reset_pool_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPoolInfo", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="poolInfo")
    def pool_info(self) -> "DataDatabricksInstancePoolPoolInfoOutputReference":
        return typing.cast("DataDatabricksInstancePoolPoolInfoOutputReference", jsii.get(self, "poolInfo"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="poolInfoInput")
    def pool_info_input(self) -> typing.Optional["DataDatabricksInstancePoolPoolInfo"]:
        return typing.cast(typing.Optional["DataDatabricksInstancePoolPoolInfo"], jsii.get(self, "poolInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c455a8dd3f665aba3e3e1767da747b4eda08baee8371161a2834bc23d6bd6a1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3ba8889bad0c36cfcbe350abedc7de9335881010dfb45989b7c3dc65d756abd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "id": "id",
        "pool_info": "poolInfo",
    },
)
class DataDatabricksInstancePoolConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        pool_info: typing.Optional[typing.Union["DataDatabricksInstancePoolPoolInfo", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#name DataDatabricksInstancePool#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#id DataDatabricksInstancePool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param pool_info: pool_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#pool_info DataDatabricksInstancePool#pool_info}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(pool_info, dict):
            pool_info = DataDatabricksInstancePoolPoolInfo(**pool_info)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3c11edb7e13c303a17566e0055db01202cae4a7aa9de0285ddae7a187fa0741)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument pool_info", value=pool_info, expected_type=type_hints["pool_info"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
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
        if id is not None:
            self._values["id"] = id
        if pool_info is not None:
            self._values["pool_info"] = pool_info

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#name DataDatabricksInstancePool#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#id DataDatabricksInstancePool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pool_info(self) -> typing.Optional["DataDatabricksInstancePoolPoolInfo"]:
        '''pool_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#pool_info DataDatabricksInstancePool#pool_info}
        '''
        result = self._values.get("pool_info")
        return typing.cast(typing.Optional["DataDatabricksInstancePoolPoolInfo"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksInstancePoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfo",
    jsii_struct_bases=[],
    name_mapping={
        "idle_instance_autotermination_minutes": "idleInstanceAutoterminationMinutes",
        "instance_pool_name": "instancePoolName",
        "aws_attributes": "awsAttributes",
        "azure_attributes": "azureAttributes",
        "custom_tags": "customTags",
        "default_tags": "defaultTags",
        "disk_spec": "diskSpec",
        "enable_elastic_disk": "enableElasticDisk",
        "gcp_attributes": "gcpAttributes",
        "instance_pool_fleet_attributes": "instancePoolFleetAttributes",
        "instance_pool_id": "instancePoolId",
        "max_capacity": "maxCapacity",
        "min_idle_instances": "minIdleInstances",
        "node_type_id": "nodeTypeId",
        "preloaded_docker_image": "preloadedDockerImage",
        "preloaded_spark_versions": "preloadedSparkVersions",
        "state": "state",
        "stats": "stats",
    },
)
class DataDatabricksInstancePoolPoolInfo:
    def __init__(
        self,
        *,
        idle_instance_autotermination_minutes: jsii.Number,
        instance_pool_name: builtins.str,
        aws_attributes: typing.Optional[typing.Union["DataDatabricksInstancePoolPoolInfoAwsAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_attributes: typing.Optional[typing.Union["DataDatabricksInstancePoolPoolInfoAzureAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        disk_spec: typing.Optional[typing.Union["DataDatabricksInstancePoolPoolInfoDiskSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        gcp_attributes: typing.Optional[typing.Union["DataDatabricksInstancePoolPoolInfoGcpAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        instance_pool_fleet_attributes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        instance_pool_id: typing.Optional[builtins.str] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_idle_instances: typing.Optional[jsii.Number] = None,
        node_type_id: typing.Optional[builtins.str] = None,
        preloaded_docker_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksInstancePoolPoolInfoPreloadedDockerImage", typing.Dict[builtins.str, typing.Any]]]]] = None,
        preloaded_spark_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        state: typing.Optional[builtins.str] = None,
        stats: typing.Optional[typing.Union["DataDatabricksInstancePoolPoolInfoStats", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle_instance_autotermination_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#idle_instance_autotermination_minutes DataDatabricksInstancePool#idle_instance_autotermination_minutes}.
        :param instance_pool_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#instance_pool_name DataDatabricksInstancePool#instance_pool_name}.
        :param aws_attributes: aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#aws_attributes DataDatabricksInstancePool#aws_attributes}
        :param azure_attributes: azure_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#azure_attributes DataDatabricksInstancePool#azure_attributes}
        :param custom_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#custom_tags DataDatabricksInstancePool#custom_tags}.
        :param default_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#default_tags DataDatabricksInstancePool#default_tags}.
        :param disk_spec: disk_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#disk_spec DataDatabricksInstancePool#disk_spec}
        :param enable_elastic_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#enable_elastic_disk DataDatabricksInstancePool#enable_elastic_disk}.
        :param gcp_attributes: gcp_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#gcp_attributes DataDatabricksInstancePool#gcp_attributes}
        :param instance_pool_fleet_attributes: instance_pool_fleet_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#instance_pool_fleet_attributes DataDatabricksInstancePool#instance_pool_fleet_attributes}
        :param instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#instance_pool_id DataDatabricksInstancePool#instance_pool_id}.
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#max_capacity DataDatabricksInstancePool#max_capacity}.
        :param min_idle_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#min_idle_instances DataDatabricksInstancePool#min_idle_instances}.
        :param node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#node_type_id DataDatabricksInstancePool#node_type_id}.
        :param preloaded_docker_image: preloaded_docker_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#preloaded_docker_image DataDatabricksInstancePool#preloaded_docker_image}
        :param preloaded_spark_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#preloaded_spark_versions DataDatabricksInstancePool#preloaded_spark_versions}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#state DataDatabricksInstancePool#state}.
        :param stats: stats block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#stats DataDatabricksInstancePool#stats}
        '''
        if isinstance(aws_attributes, dict):
            aws_attributes = DataDatabricksInstancePoolPoolInfoAwsAttributes(**aws_attributes)
        if isinstance(azure_attributes, dict):
            azure_attributes = DataDatabricksInstancePoolPoolInfoAzureAttributes(**azure_attributes)
        if isinstance(disk_spec, dict):
            disk_spec = DataDatabricksInstancePoolPoolInfoDiskSpec(**disk_spec)
        if isinstance(gcp_attributes, dict):
            gcp_attributes = DataDatabricksInstancePoolPoolInfoGcpAttributes(**gcp_attributes)
        if isinstance(stats, dict):
            stats = DataDatabricksInstancePoolPoolInfoStats(**stats)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71aa1a3e37cc283977885db4ce62f72bb1eea5a1758193d1a9a350c88d7997c6)
            check_type(argname="argument idle_instance_autotermination_minutes", value=idle_instance_autotermination_minutes, expected_type=type_hints["idle_instance_autotermination_minutes"])
            check_type(argname="argument instance_pool_name", value=instance_pool_name, expected_type=type_hints["instance_pool_name"])
            check_type(argname="argument aws_attributes", value=aws_attributes, expected_type=type_hints["aws_attributes"])
            check_type(argname="argument azure_attributes", value=azure_attributes, expected_type=type_hints["azure_attributes"])
            check_type(argname="argument custom_tags", value=custom_tags, expected_type=type_hints["custom_tags"])
            check_type(argname="argument default_tags", value=default_tags, expected_type=type_hints["default_tags"])
            check_type(argname="argument disk_spec", value=disk_spec, expected_type=type_hints["disk_spec"])
            check_type(argname="argument enable_elastic_disk", value=enable_elastic_disk, expected_type=type_hints["enable_elastic_disk"])
            check_type(argname="argument gcp_attributes", value=gcp_attributes, expected_type=type_hints["gcp_attributes"])
            check_type(argname="argument instance_pool_fleet_attributes", value=instance_pool_fleet_attributes, expected_type=type_hints["instance_pool_fleet_attributes"])
            check_type(argname="argument instance_pool_id", value=instance_pool_id, expected_type=type_hints["instance_pool_id"])
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument min_idle_instances", value=min_idle_instances, expected_type=type_hints["min_idle_instances"])
            check_type(argname="argument node_type_id", value=node_type_id, expected_type=type_hints["node_type_id"])
            check_type(argname="argument preloaded_docker_image", value=preloaded_docker_image, expected_type=type_hints["preloaded_docker_image"])
            check_type(argname="argument preloaded_spark_versions", value=preloaded_spark_versions, expected_type=type_hints["preloaded_spark_versions"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument stats", value=stats, expected_type=type_hints["stats"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "idle_instance_autotermination_minutes": idle_instance_autotermination_minutes,
            "instance_pool_name": instance_pool_name,
        }
        if aws_attributes is not None:
            self._values["aws_attributes"] = aws_attributes
        if azure_attributes is not None:
            self._values["azure_attributes"] = azure_attributes
        if custom_tags is not None:
            self._values["custom_tags"] = custom_tags
        if default_tags is not None:
            self._values["default_tags"] = default_tags
        if disk_spec is not None:
            self._values["disk_spec"] = disk_spec
        if enable_elastic_disk is not None:
            self._values["enable_elastic_disk"] = enable_elastic_disk
        if gcp_attributes is not None:
            self._values["gcp_attributes"] = gcp_attributes
        if instance_pool_fleet_attributes is not None:
            self._values["instance_pool_fleet_attributes"] = instance_pool_fleet_attributes
        if instance_pool_id is not None:
            self._values["instance_pool_id"] = instance_pool_id
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity
        if min_idle_instances is not None:
            self._values["min_idle_instances"] = min_idle_instances
        if node_type_id is not None:
            self._values["node_type_id"] = node_type_id
        if preloaded_docker_image is not None:
            self._values["preloaded_docker_image"] = preloaded_docker_image
        if preloaded_spark_versions is not None:
            self._values["preloaded_spark_versions"] = preloaded_spark_versions
        if state is not None:
            self._values["state"] = state
        if stats is not None:
            self._values["stats"] = stats

    @builtins.property
    def idle_instance_autotermination_minutes(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#idle_instance_autotermination_minutes DataDatabricksInstancePool#idle_instance_autotermination_minutes}.'''
        result = self._values.get("idle_instance_autotermination_minutes")
        assert result is not None, "Required property 'idle_instance_autotermination_minutes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def instance_pool_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#instance_pool_name DataDatabricksInstancePool#instance_pool_name}.'''
        result = self._values.get("instance_pool_name")
        assert result is not None, "Required property 'instance_pool_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_attributes(
        self,
    ) -> typing.Optional["DataDatabricksInstancePoolPoolInfoAwsAttributes"]:
        '''aws_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#aws_attributes DataDatabricksInstancePool#aws_attributes}
        '''
        result = self._values.get("aws_attributes")
        return typing.cast(typing.Optional["DataDatabricksInstancePoolPoolInfoAwsAttributes"], result)

    @builtins.property
    def azure_attributes(
        self,
    ) -> typing.Optional["DataDatabricksInstancePoolPoolInfoAzureAttributes"]:
        '''azure_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#azure_attributes DataDatabricksInstancePool#azure_attributes}
        '''
        result = self._values.get("azure_attributes")
        return typing.cast(typing.Optional["DataDatabricksInstancePoolPoolInfoAzureAttributes"], result)

    @builtins.property
    def custom_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#custom_tags DataDatabricksInstancePool#custom_tags}.'''
        result = self._values.get("custom_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def default_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#default_tags DataDatabricksInstancePool#default_tags}.'''
        result = self._values.get("default_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def disk_spec(
        self,
    ) -> typing.Optional["DataDatabricksInstancePoolPoolInfoDiskSpec"]:
        '''disk_spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#disk_spec DataDatabricksInstancePool#disk_spec}
        '''
        result = self._values.get("disk_spec")
        return typing.cast(typing.Optional["DataDatabricksInstancePoolPoolInfoDiskSpec"], result)

    @builtins.property
    def enable_elastic_disk(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#enable_elastic_disk DataDatabricksInstancePool#enable_elastic_disk}.'''
        result = self._values.get("enable_elastic_disk")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def gcp_attributes(
        self,
    ) -> typing.Optional["DataDatabricksInstancePoolPoolInfoGcpAttributes"]:
        '''gcp_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#gcp_attributes DataDatabricksInstancePool#gcp_attributes}
        '''
        result = self._values.get("gcp_attributes")
        return typing.cast(typing.Optional["DataDatabricksInstancePoolPoolInfoGcpAttributes"], result)

    @builtins.property
    def instance_pool_fleet_attributes(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes"]]]:
        '''instance_pool_fleet_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#instance_pool_fleet_attributes DataDatabricksInstancePool#instance_pool_fleet_attributes}
        '''
        result = self._values.get("instance_pool_fleet_attributes")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes"]]], result)

    @builtins.property
    def instance_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#instance_pool_id DataDatabricksInstancePool#instance_pool_id}.'''
        result = self._values.get("instance_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#max_capacity DataDatabricksInstancePool#max_capacity}.'''
        result = self._values.get("max_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_idle_instances(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#min_idle_instances DataDatabricksInstancePool#min_idle_instances}.'''
        result = self._values.get("min_idle_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def node_type_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#node_type_id DataDatabricksInstancePool#node_type_id}.'''
        result = self._values.get("node_type_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preloaded_docker_image(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksInstancePoolPoolInfoPreloadedDockerImage"]]]:
        '''preloaded_docker_image block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#preloaded_docker_image DataDatabricksInstancePool#preloaded_docker_image}
        '''
        result = self._values.get("preloaded_docker_image")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksInstancePoolPoolInfoPreloadedDockerImage"]]], result)

    @builtins.property
    def preloaded_spark_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#preloaded_spark_versions DataDatabricksInstancePool#preloaded_spark_versions}.'''
        result = self._values.get("preloaded_spark_versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#state DataDatabricksInstancePool#state}.'''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stats(self) -> typing.Optional["DataDatabricksInstancePoolPoolInfoStats"]:
        '''stats block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#stats DataDatabricksInstancePool#stats}
        '''
        result = self._values.get("stats")
        return typing.cast(typing.Optional["DataDatabricksInstancePoolPoolInfoStats"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksInstancePoolPoolInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoAwsAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "spot_bid_price_percent": "spotBidPricePercent",
        "zone_id": "zoneId",
    },
)
class DataDatabricksInstancePoolPoolInfoAwsAttributes:
    def __init__(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        spot_bid_price_percent: typing.Optional[jsii.Number] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#availability DataDatabricksInstancePool#availability}.
        :param spot_bid_price_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#spot_bid_price_percent DataDatabricksInstancePool#spot_bid_price_percent}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#zone_id DataDatabricksInstancePool#zone_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e04f0f2bd5cfbcf69cebf7ac4c551c549fcf4cd90f912d9c5646c5f7ea215d88)
            check_type(argname="argument availability", value=availability, expected_type=type_hints["availability"])
            check_type(argname="argument spot_bid_price_percent", value=spot_bid_price_percent, expected_type=type_hints["spot_bid_price_percent"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability is not None:
            self._values["availability"] = availability
        if spot_bid_price_percent is not None:
            self._values["spot_bid_price_percent"] = spot_bid_price_percent
        if zone_id is not None:
            self._values["zone_id"] = zone_id

    @builtins.property
    def availability(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#availability DataDatabricksInstancePool#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_bid_price_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#spot_bid_price_percent DataDatabricksInstancePool#spot_bid_price_percent}.'''
        result = self._values.get("spot_bid_price_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#zone_id DataDatabricksInstancePool#zone_id}.'''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksInstancePoolPoolInfoAwsAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksInstancePoolPoolInfoAwsAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoAwsAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e4198a332b9101ba6701f88e4938cb729a00f683734a7e3e35a74fab8206103a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAvailability")
    def reset_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailability", []))

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
            type_hints = typing.get_type_hints(_typecheckingstub__2de8358c1fb2a97729a6145ddb1d4df852787b1d97954fed8030324fa229a993)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="spotBidPricePercent")
    def spot_bid_price_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotBidPricePercent"))

    @spot_bid_price_percent.setter
    def spot_bid_price_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87869fb319047e2b38de86c43ba0f2818baa82fed4f1525558cc71139cc3855e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotBidPricePercent", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f4daa1cfd78ef5f4e27d1879d7a5739ca9ed1ca6ecee216f89b75a777723360)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksInstancePoolPoolInfoAwsAttributes]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfoAwsAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksInstancePoolPoolInfoAwsAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e31055d1db1843401f6c6bff580f0d904ee96555efaff2bbad025aaf85d830f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoAzureAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "spot_bid_max_price": "spotBidMaxPrice",
    },
)
class DataDatabricksInstancePoolPoolInfoAzureAttributes:
    def __init__(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        spot_bid_max_price: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#availability DataDatabricksInstancePool#availability}.
        :param spot_bid_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#spot_bid_max_price DataDatabricksInstancePool#spot_bid_max_price}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d9f6bdb745b11f0069815f2a5dc2cbc433a50d352bebdcf8df8fd385b286249)
            check_type(argname="argument availability", value=availability, expected_type=type_hints["availability"])
            check_type(argname="argument spot_bid_max_price", value=spot_bid_max_price, expected_type=type_hints["spot_bid_max_price"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability is not None:
            self._values["availability"] = availability
        if spot_bid_max_price is not None:
            self._values["spot_bid_max_price"] = spot_bid_max_price

    @builtins.property
    def availability(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#availability DataDatabricksInstancePool#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_bid_max_price(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#spot_bid_max_price DataDatabricksInstancePool#spot_bid_max_price}.'''
        result = self._values.get("spot_bid_max_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksInstancePoolPoolInfoAzureAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksInstancePoolPoolInfoAzureAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoAzureAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__18344d7b95740e7bbf418001550bc9249fe0d330664aaf4c589e3a7bcb2a6df1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAvailability")
    def reset_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailability", []))

    @jsii.member(jsii_name="resetSpotBidMaxPrice")
    def reset_spot_bid_max_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotBidMaxPrice", []))

    @builtins.property
    @jsii.member(jsii_name="availabilityInput")
    def availability_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__2f0aad6032cf82a3252d905c4248b01c4cf0e32c221054a5cdbd4d39eff7cba8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="spotBidMaxPrice")
    def spot_bid_max_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotBidMaxPrice"))

    @spot_bid_max_price.setter
    def spot_bid_max_price(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a018858c6735bd386db1c7abebc9117c3fbb19eac6aa45de4722f95f30ace7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotBidMaxPrice", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksInstancePoolPoolInfoAzureAttributes]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfoAzureAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksInstancePoolPoolInfoAzureAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d932934b031b445d7095904f26374f3bdf22ae9dc9a2d5cfbb37547d4fb44e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoDiskSpec",
    jsii_struct_bases=[],
    name_mapping={
        "disk_count": "diskCount",
        "disk_size": "diskSize",
        "disk_type": "diskType",
    },
)
class DataDatabricksInstancePoolPoolInfoDiskSpec:
    def __init__(
        self,
        *,
        disk_count: typing.Optional[jsii.Number] = None,
        disk_size: typing.Optional[jsii.Number] = None,
        disk_type: typing.Optional[typing.Union["DataDatabricksInstancePoolPoolInfoDiskSpecDiskType", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param disk_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#disk_count DataDatabricksInstancePool#disk_count}.
        :param disk_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#disk_size DataDatabricksInstancePool#disk_size}.
        :param disk_type: disk_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#disk_type DataDatabricksInstancePool#disk_type}
        '''
        if isinstance(disk_type, dict):
            disk_type = DataDatabricksInstancePoolPoolInfoDiskSpecDiskType(**disk_type)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70f2325d622a653edd475f455bf1f47841d14201d1588c3b3dd6d3011825d783)
            check_type(argname="argument disk_count", value=disk_count, expected_type=type_hints["disk_count"])
            check_type(argname="argument disk_size", value=disk_size, expected_type=type_hints["disk_size"])
            check_type(argname="argument disk_type", value=disk_type, expected_type=type_hints["disk_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if disk_count is not None:
            self._values["disk_count"] = disk_count
        if disk_size is not None:
            self._values["disk_size"] = disk_size
        if disk_type is not None:
            self._values["disk_type"] = disk_type

    @builtins.property
    def disk_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#disk_count DataDatabricksInstancePool#disk_count}.'''
        result = self._values.get("disk_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#disk_size DataDatabricksInstancePool#disk_size}.'''
        result = self._values.get("disk_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_type(
        self,
    ) -> typing.Optional["DataDatabricksInstancePoolPoolInfoDiskSpecDiskType"]:
        '''disk_type block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#disk_type DataDatabricksInstancePool#disk_type}
        '''
        result = self._values.get("disk_type")
        return typing.cast(typing.Optional["DataDatabricksInstancePoolPoolInfoDiskSpecDiskType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksInstancePoolPoolInfoDiskSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoDiskSpecDiskType",
    jsii_struct_bases=[],
    name_mapping={
        "azure_disk_volume_type": "azureDiskVolumeType",
        "ebs_volume_type": "ebsVolumeType",
    },
)
class DataDatabricksInstancePoolPoolInfoDiskSpecDiskType:
    def __init__(
        self,
        *,
        azure_disk_volume_type: typing.Optional[builtins.str] = None,
        ebs_volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param azure_disk_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#azure_disk_volume_type DataDatabricksInstancePool#azure_disk_volume_type}.
        :param ebs_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#ebs_volume_type DataDatabricksInstancePool#ebs_volume_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fdd6861484b029a1bc96919f2aabb661294292fb795d2a67423ee549a249fb8)
            check_type(argname="argument azure_disk_volume_type", value=azure_disk_volume_type, expected_type=type_hints["azure_disk_volume_type"])
            check_type(argname="argument ebs_volume_type", value=ebs_volume_type, expected_type=type_hints["ebs_volume_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if azure_disk_volume_type is not None:
            self._values["azure_disk_volume_type"] = azure_disk_volume_type
        if ebs_volume_type is not None:
            self._values["ebs_volume_type"] = ebs_volume_type

    @builtins.property
    def azure_disk_volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#azure_disk_volume_type DataDatabricksInstancePool#azure_disk_volume_type}.'''
        result = self._values.get("azure_disk_volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#ebs_volume_type DataDatabricksInstancePool#ebs_volume_type}.'''
        result = self._values.get("ebs_volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksInstancePoolPoolInfoDiskSpecDiskType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksInstancePoolPoolInfoDiskSpecDiskTypeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoDiskSpecDiskTypeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__232a16dfb9d2ab1fd50bcf929688e4886adaebc5552a68e1d7652a9ee380fcca)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAzureDiskVolumeType")
    def reset_azure_disk_volume_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureDiskVolumeType", []))

    @jsii.member(jsii_name="resetEbsVolumeType")
    def reset_ebs_volume_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsVolumeType", []))

    @builtins.property
    @jsii.member(jsii_name="azureDiskVolumeTypeInput")
    def azure_disk_volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureDiskVolumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeTypeInput")
    def ebs_volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ebsVolumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="azureDiskVolumeType")
    def azure_disk_volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureDiskVolumeType"))

    @azure_disk_volume_type.setter
    def azure_disk_volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23324ca2554d1b492064958a9a2d8f866588448219fc505f0eda6239b888a9dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureDiskVolumeType", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeType")
    def ebs_volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ebsVolumeType"))

    @ebs_volume_type.setter
    def ebs_volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1752e5d59c27ac77303406a41cdaa617f1bbc5950f7ca426f25ae23702e9b1b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksInstancePoolPoolInfoDiskSpecDiskType]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfoDiskSpecDiskType], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksInstancePoolPoolInfoDiskSpecDiskType],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33113ff6e03d1a7c8301e75299f8d71d1933c189bbb86fa273eeff7832bdc0e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksInstancePoolPoolInfoDiskSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoDiskSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__667ecc016d979d2f6bfc547cc44cb75c755f8f25f8bf4835b247db80ee354249)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDiskType")
    def put_disk_type(
        self,
        *,
        azure_disk_volume_type: typing.Optional[builtins.str] = None,
        ebs_volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param azure_disk_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#azure_disk_volume_type DataDatabricksInstancePool#azure_disk_volume_type}.
        :param ebs_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#ebs_volume_type DataDatabricksInstancePool#ebs_volume_type}.
        '''
        value = DataDatabricksInstancePoolPoolInfoDiskSpecDiskType(
            azure_disk_volume_type=azure_disk_volume_type,
            ebs_volume_type=ebs_volume_type,
        )

        return typing.cast(None, jsii.invoke(self, "putDiskType", [value]))

    @jsii.member(jsii_name="resetDiskCount")
    def reset_disk_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskCount", []))

    @jsii.member(jsii_name="resetDiskSize")
    def reset_disk_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSize", []))

    @jsii.member(jsii_name="resetDiskType")
    def reset_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskType", []))

    @builtins.property
    @jsii.member(jsii_name="diskType")
    def disk_type(
        self,
    ) -> DataDatabricksInstancePoolPoolInfoDiskSpecDiskTypeOutputReference:
        return typing.cast(DataDatabricksInstancePoolPoolInfoDiskSpecDiskTypeOutputReference, jsii.get(self, "diskType"))

    @builtins.property
    @jsii.member(jsii_name="diskCountInput")
    def disk_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskCountInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeInput")
    def disk_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="diskTypeInput")
    def disk_type_input(
        self,
    ) -> typing.Optional[DataDatabricksInstancePoolPoolInfoDiskSpecDiskType]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfoDiskSpecDiskType], jsii.get(self, "diskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="diskCount")
    def disk_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskCount"))

    @disk_count.setter
    def disk_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ac1286af20e21efbfe480f45bab80f3d55e70962fa47605b00aa8f4985d41f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskCount", value)

    @builtins.property
    @jsii.member(jsii_name="diskSize")
    def disk_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSize"))

    @disk_size.setter
    def disk_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30716ef81730a97f9010d39e5a06becc9f25b6f3afc40fc1e1c7c348f7073758)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSize", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksInstancePoolPoolInfoDiskSpec]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfoDiskSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksInstancePoolPoolInfoDiskSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf17cc6f45b37910f35e4c9b443c00815050059a7b2edaa84962e9373e8d9a79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoGcpAttributes",
    jsii_struct_bases=[],
    name_mapping={"gcp_availability": "gcpAvailability"},
)
class DataDatabricksInstancePoolPoolInfoGcpAttributes:
    def __init__(
        self,
        *,
        gcp_availability: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param gcp_availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#gcp_availability DataDatabricksInstancePool#gcp_availability}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__657f2beedae41b091551464288db80baa2d0d9add00e89b3ca4670bd878c9faa)
            check_type(argname="argument gcp_availability", value=gcp_availability, expected_type=type_hints["gcp_availability"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if gcp_availability is not None:
            self._values["gcp_availability"] = gcp_availability

    @builtins.property
    def gcp_availability(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#gcp_availability DataDatabricksInstancePool#gcp_availability}.'''
        result = self._values.get("gcp_availability")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksInstancePoolPoolInfoGcpAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksInstancePoolPoolInfoGcpAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoGcpAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__07806c4de054d36bc01e4eb6a68e256c145bbf30c5c4f106e4f7e182597e1c5e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGcpAvailability")
    def reset_gcp_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpAvailability", []))

    @builtins.property
    @jsii.member(jsii_name="gcpAvailabilityInput")
    def gcp_availability_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gcpAvailabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="gcpAvailability")
    def gcp_availability(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gcpAvailability"))

    @gcp_availability.setter
    def gcp_availability(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__069500366f86a92c85c4de2b56a68a6fdc7ca8d0d609ef90813123c3835f0fa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gcpAvailability", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksInstancePoolPoolInfoGcpAttributes]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfoGcpAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksInstancePoolPoolInfoGcpAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2253174fc6800cf3cc086a6595edbaab8471bfefab4a2d35c0ec0fdc57490b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "launch_template_override": "launchTemplateOverride",
        "fleet_on_demand_option": "fleetOnDemandOption",
        "fleet_spot_option": "fleetSpotOption",
    },
)
class DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes:
    def __init__(
        self,
        *,
        launch_template_override: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride", typing.Dict[builtins.str, typing.Any]]]],
        fleet_on_demand_option: typing.Optional[typing.Union["DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOption", typing.Dict[builtins.str, typing.Any]]] = None,
        fleet_spot_option: typing.Optional[typing.Union["DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOption", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param launch_template_override: launch_template_override block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#launch_template_override DataDatabricksInstancePool#launch_template_override}
        :param fleet_on_demand_option: fleet_on_demand_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#fleet_on_demand_option DataDatabricksInstancePool#fleet_on_demand_option}
        :param fleet_spot_option: fleet_spot_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#fleet_spot_option DataDatabricksInstancePool#fleet_spot_option}
        '''
        if isinstance(fleet_on_demand_option, dict):
            fleet_on_demand_option = DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOption(**fleet_on_demand_option)
        if isinstance(fleet_spot_option, dict):
            fleet_spot_option = DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOption(**fleet_spot_option)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2c76a641e0630c03a24648969f1d24b079b2c50b68ea5f4f85d8b1e134f3f93)
            check_type(argname="argument launch_template_override", value=launch_template_override, expected_type=type_hints["launch_template_override"])
            check_type(argname="argument fleet_on_demand_option", value=fleet_on_demand_option, expected_type=type_hints["fleet_on_demand_option"])
            check_type(argname="argument fleet_spot_option", value=fleet_spot_option, expected_type=type_hints["fleet_spot_option"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "launch_template_override": launch_template_override,
        }
        if fleet_on_demand_option is not None:
            self._values["fleet_on_demand_option"] = fleet_on_demand_option
        if fleet_spot_option is not None:
            self._values["fleet_spot_option"] = fleet_spot_option

    @builtins.property
    def launch_template_override(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride"]]:
        '''launch_template_override block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#launch_template_override DataDatabricksInstancePool#launch_template_override}
        '''
        result = self._values.get("launch_template_override")
        assert result is not None, "Required property 'launch_template_override' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride"]], result)

    @builtins.property
    def fleet_on_demand_option(
        self,
    ) -> typing.Optional["DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOption"]:
        '''fleet_on_demand_option block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#fleet_on_demand_option DataDatabricksInstancePool#fleet_on_demand_option}
        '''
        result = self._values.get("fleet_on_demand_option")
        return typing.cast(typing.Optional["DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOption"], result)

    @builtins.property
    def fleet_spot_option(
        self,
    ) -> typing.Optional["DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOption"]:
        '''fleet_spot_option block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#fleet_spot_option DataDatabricksInstancePool#fleet_spot_option}
        '''
        result = self._values.get("fleet_spot_option")
        return typing.cast(typing.Optional["DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOption"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOption",
    jsii_struct_bases=[],
    name_mapping={
        "allocation_strategy": "allocationStrategy",
        "instance_pools_to_use_count": "instancePoolsToUseCount",
    },
)
class DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOption:
    def __init__(
        self,
        *,
        allocation_strategy: builtins.str,
        instance_pools_to_use_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#allocation_strategy DataDatabricksInstancePool#allocation_strategy}.
        :param instance_pools_to_use_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#instance_pools_to_use_count DataDatabricksInstancePool#instance_pools_to_use_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff28981cd21add80e072ef24a952db575893b2929a8110daa54588ba3c63b798)
            check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
            check_type(argname="argument instance_pools_to_use_count", value=instance_pools_to_use_count, expected_type=type_hints["instance_pools_to_use_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allocation_strategy": allocation_strategy,
        }
        if instance_pools_to_use_count is not None:
            self._values["instance_pools_to_use_count"] = instance_pools_to_use_count

    @builtins.property
    def allocation_strategy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#allocation_strategy DataDatabricksInstancePool#allocation_strategy}.'''
        result = self._values.get("allocation_strategy")
        assert result is not None, "Required property 'allocation_strategy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_pools_to_use_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#instance_pools_to_use_count DataDatabricksInstancePool#instance_pools_to_use_count}.'''
        result = self._values.get("instance_pools_to_use_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e25546780e7308c5b73451f984ccc8fcedca972e248ed458a91dfb7521472e78)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstancePoolsToUseCount")
    def reset_instance_pools_to_use_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancePoolsToUseCount", []))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategyInput")
    def allocation_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolsToUseCountInput")
    def instance_pools_to_use_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instancePoolsToUseCountInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategy")
    def allocation_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allocationStrategy"))

    @allocation_strategy.setter
    def allocation_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f33e758df9ad07d1d7be0931f6062c2b99e614293b6af24773cdb10808da3bfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="instancePoolsToUseCount")
    def instance_pools_to_use_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instancePoolsToUseCount"))

    @instance_pools_to_use_count.setter
    def instance_pools_to_use_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5733977065b9726d80e48cdb35eb22ef353d4faf1d4c90778fb0c18b643c609d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instancePoolsToUseCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOption]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ca2e4333dbee896a7d7975e7130a8ce71156d255e3343c9c55c6b217a1d2ac4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOption",
    jsii_struct_bases=[],
    name_mapping={
        "allocation_strategy": "allocationStrategy",
        "instance_pools_to_use_count": "instancePoolsToUseCount",
    },
)
class DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOption:
    def __init__(
        self,
        *,
        allocation_strategy: builtins.str,
        instance_pools_to_use_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#allocation_strategy DataDatabricksInstancePool#allocation_strategy}.
        :param instance_pools_to_use_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#instance_pools_to_use_count DataDatabricksInstancePool#instance_pools_to_use_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6250b06901ae61e86fd97ddd5a1c6b5e3f7a38704b3d3fa651e3cc1c683f149)
            check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
            check_type(argname="argument instance_pools_to_use_count", value=instance_pools_to_use_count, expected_type=type_hints["instance_pools_to_use_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allocation_strategy": allocation_strategy,
        }
        if instance_pools_to_use_count is not None:
            self._values["instance_pools_to_use_count"] = instance_pools_to_use_count

    @builtins.property
    def allocation_strategy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#allocation_strategy DataDatabricksInstancePool#allocation_strategy}.'''
        result = self._values.get("allocation_strategy")
        assert result is not None, "Required property 'allocation_strategy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_pools_to_use_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#instance_pools_to_use_count DataDatabricksInstancePool#instance_pools_to_use_count}.'''
        result = self._values.get("instance_pools_to_use_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e6e54e56fe8360c34d4d84bff172380f455fa61c3798d2a0e854292b33bd9eb9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstancePoolsToUseCount")
    def reset_instance_pools_to_use_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancePoolsToUseCount", []))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategyInput")
    def allocation_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolsToUseCountInput")
    def instance_pools_to_use_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instancePoolsToUseCountInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategy")
    def allocation_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allocationStrategy"))

    @allocation_strategy.setter
    def allocation_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfd26ceec344d7d215e0fcb44e221b8b814ef6d637e93aded2c7d6b7150a0fd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="instancePoolsToUseCount")
    def instance_pools_to_use_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instancePoolsToUseCount"))

    @instance_pools_to_use_count.setter
    def instance_pools_to_use_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__474920365bd7556349189a402d54a0073e3be86453ceebf9c72cd86d6c5a4886)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instancePoolsToUseCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOption]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e09baf8e03f7e02782a2e9adedc2027433e4148fc645d0d3d2eda7b3643daecf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zone": "availabilityZone",
        "instance_type": "instanceType",
    },
)
class DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride:
    def __init__(
        self,
        *,
        availability_zone: builtins.str,
        instance_type: builtins.str,
    ) -> None:
        '''
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#availability_zone DataDatabricksInstancePool#availability_zone}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#instance_type DataDatabricksInstancePool#instance_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1bd66f64fdb45d81658ebb20fc83cedc6ef00b6ae3e2bdb7af8ff2b4da11925)
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "availability_zone": availability_zone,
            "instance_type": instance_type,
        }

    @builtins.property
    def availability_zone(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#availability_zone DataDatabricksInstancePool#availability_zone}.'''
        result = self._values.get("availability_zone")
        assert result is not None, "Required property 'availability_zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#instance_type DataDatabricksInstancePool#instance_type}.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverrideList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverrideList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f8ecc89a1c147020932b44086541c083797fa2615d4410052b566e35239a9523)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverrideOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30c6f4ba8dd74302ec8104b84deef1d2b637371e82b9246ced9ede442c5733ba)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverrideOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9c0e5262c93219c6ca7a019281673838e5e7592db3c8cd0754cc4635ee89acb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__977c320ae6920a20c8380833b2f19a5eb4b4cf22d8d21deba357c8764397b60d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8cdba2db31270a08dce2d677333ddf5214fb22b2a4d09cf363d63eb4b4904fe7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9e60acd4f0e548e8c514f08d373f66ab75ffc0b27d0ddd21eb6d00dc0ea64af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverrideOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverrideOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__894df49c6dfc9a37014982fdc931fa6e3ed53d7488d455e9232ba5452f59f472)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneInput")
    def availability_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c28d6bade305dba7fd996ef353b729d86658637b0c486da1996946bc79eff968)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40ceefe079b24261928224ef62baca482854766da4cbef8280513410589aa043)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51ac1097061b9a6cb48a2230886c7dd35e04dd217e859d567420a9130bd32ecd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d29c0afcc8725f72c08389fc98adedddf5af0c56e88ed6a3d2ab8d47aa83baa0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c42cd2072033f047a9bcddc371a2b5fd9c731f419a3a2b443734e54564a4ecd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5a30b6baa46b89c233a7c82c9a676f183d23a1f89b0740d7861e2208239e1a4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__21e20f2d20083c956f6ab5744543529a100d4548999cf465775865d441bc7c5d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9011b0f76b510b23208f9c4f74f172db426082036c866e25ce8e40f4ca530413)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f544dae4d0ba0a4dcbae6e103ca3cb7c43d8d1d795acfb01c66373aeb665ce6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__11a27f6cb7a3e3a050697b4b903f06e3d3c711aa8fe913959591fec326c0a593)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFleetOnDemandOption")
    def put_fleet_on_demand_option(
        self,
        *,
        allocation_strategy: builtins.str,
        instance_pools_to_use_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#allocation_strategy DataDatabricksInstancePool#allocation_strategy}.
        :param instance_pools_to_use_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#instance_pools_to_use_count DataDatabricksInstancePool#instance_pools_to_use_count}.
        '''
        value = DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOption(
            allocation_strategy=allocation_strategy,
            instance_pools_to_use_count=instance_pools_to_use_count,
        )

        return typing.cast(None, jsii.invoke(self, "putFleetOnDemandOption", [value]))

    @jsii.member(jsii_name="putFleetSpotOption")
    def put_fleet_spot_option(
        self,
        *,
        allocation_strategy: builtins.str,
        instance_pools_to_use_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#allocation_strategy DataDatabricksInstancePool#allocation_strategy}.
        :param instance_pools_to_use_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#instance_pools_to_use_count DataDatabricksInstancePool#instance_pools_to_use_count}.
        '''
        value = DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOption(
            allocation_strategy=allocation_strategy,
            instance_pools_to_use_count=instance_pools_to_use_count,
        )

        return typing.cast(None, jsii.invoke(self, "putFleetSpotOption", [value]))

    @jsii.member(jsii_name="putLaunchTemplateOverride")
    def put_launch_template_override(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88d9b0737ecc7351d81da3de96810b8275401906fb007b70a8e4355e6af761e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLaunchTemplateOverride", [value]))

    @jsii.member(jsii_name="resetFleetOnDemandOption")
    def reset_fleet_on_demand_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFleetOnDemandOption", []))

    @jsii.member(jsii_name="resetFleetSpotOption")
    def reset_fleet_spot_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFleetSpotOption", []))

    @builtins.property
    @jsii.member(jsii_name="fleetOnDemandOption")
    def fleet_on_demand_option(
        self,
    ) -> DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOptionOutputReference:
        return typing.cast(DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOptionOutputReference, jsii.get(self, "fleetOnDemandOption"))

    @builtins.property
    @jsii.member(jsii_name="fleetSpotOption")
    def fleet_spot_option(
        self,
    ) -> DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOptionOutputReference:
        return typing.cast(DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOptionOutputReference, jsii.get(self, "fleetSpotOption"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateOverride")
    def launch_template_override(
        self,
    ) -> DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverrideList:
        return typing.cast(DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverrideList, jsii.get(self, "launchTemplateOverride"))

    @builtins.property
    @jsii.member(jsii_name="fleetOnDemandOptionInput")
    def fleet_on_demand_option_input(
        self,
    ) -> typing.Optional[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOption]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOption], jsii.get(self, "fleetOnDemandOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="fleetSpotOptionInput")
    def fleet_spot_option_input(
        self,
    ) -> typing.Optional[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOption]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOption], jsii.get(self, "fleetSpotOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateOverrideInput")
    def launch_template_override_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride]]], jsii.get(self, "launchTemplateOverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a875bcc1168e14ebdd862a4c1b0c7f79a9285450e289d193f5e72eb986efcd57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksInstancePoolPoolInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7e1ea6bbc4aaf27bd60355b4ef9b0585d82e24e6cf4a9193781f92569e98a86)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAwsAttributes")
    def put_aws_attributes(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        spot_bid_price_percent: typing.Optional[jsii.Number] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#availability DataDatabricksInstancePool#availability}.
        :param spot_bid_price_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#spot_bid_price_percent DataDatabricksInstancePool#spot_bid_price_percent}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#zone_id DataDatabricksInstancePool#zone_id}.
        '''
        value = DataDatabricksInstancePoolPoolInfoAwsAttributes(
            availability=availability,
            spot_bid_price_percent=spot_bid_price_percent,
            zone_id=zone_id,
        )

        return typing.cast(None, jsii.invoke(self, "putAwsAttributes", [value]))

    @jsii.member(jsii_name="putAzureAttributes")
    def put_azure_attributes(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        spot_bid_max_price: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#availability DataDatabricksInstancePool#availability}.
        :param spot_bid_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#spot_bid_max_price DataDatabricksInstancePool#spot_bid_max_price}.
        '''
        value = DataDatabricksInstancePoolPoolInfoAzureAttributes(
            availability=availability, spot_bid_max_price=spot_bid_max_price
        )

        return typing.cast(None, jsii.invoke(self, "putAzureAttributes", [value]))

    @jsii.member(jsii_name="putDiskSpec")
    def put_disk_spec(
        self,
        *,
        disk_count: typing.Optional[jsii.Number] = None,
        disk_size: typing.Optional[jsii.Number] = None,
        disk_type: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoDiskSpecDiskType, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param disk_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#disk_count DataDatabricksInstancePool#disk_count}.
        :param disk_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#disk_size DataDatabricksInstancePool#disk_size}.
        :param disk_type: disk_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#disk_type DataDatabricksInstancePool#disk_type}
        '''
        value = DataDatabricksInstancePoolPoolInfoDiskSpec(
            disk_count=disk_count, disk_size=disk_size, disk_type=disk_type
        )

        return typing.cast(None, jsii.invoke(self, "putDiskSpec", [value]))

    @jsii.member(jsii_name="putGcpAttributes")
    def put_gcp_attributes(
        self,
        *,
        gcp_availability: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param gcp_availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#gcp_availability DataDatabricksInstancePool#gcp_availability}.
        '''
        value = DataDatabricksInstancePoolPoolInfoGcpAttributes(
            gcp_availability=gcp_availability
        )

        return typing.cast(None, jsii.invoke(self, "putGcpAttributes", [value]))

    @jsii.member(jsii_name="putInstancePoolFleetAttributes")
    def put_instance_pool_fleet_attributes(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__353a2f4c65f7c5c5f6feecc11fe14904d9a17af15125625b61f4d23d6120a39b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInstancePoolFleetAttributes", [value]))

    @jsii.member(jsii_name="putPreloadedDockerImage")
    def put_preloaded_docker_image(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksInstancePoolPoolInfoPreloadedDockerImage", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6596fdeb8509e2ca413ea8698d81f2b807dcc819934a2821985af1791b876ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPreloadedDockerImage", [value]))

    @jsii.member(jsii_name="putStats")
    def put_stats(
        self,
        *,
        idle_count: typing.Optional[jsii.Number] = None,
        pending_idle_count: typing.Optional[jsii.Number] = None,
        pending_used_count: typing.Optional[jsii.Number] = None,
        used_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param idle_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#idle_count DataDatabricksInstancePool#idle_count}.
        :param pending_idle_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#pending_idle_count DataDatabricksInstancePool#pending_idle_count}.
        :param pending_used_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#pending_used_count DataDatabricksInstancePool#pending_used_count}.
        :param used_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#used_count DataDatabricksInstancePool#used_count}.
        '''
        value = DataDatabricksInstancePoolPoolInfoStats(
            idle_count=idle_count,
            pending_idle_count=pending_idle_count,
            pending_used_count=pending_used_count,
            used_count=used_count,
        )

        return typing.cast(None, jsii.invoke(self, "putStats", [value]))

    @jsii.member(jsii_name="resetAwsAttributes")
    def reset_aws_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsAttributes", []))

    @jsii.member(jsii_name="resetAzureAttributes")
    def reset_azure_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureAttributes", []))

    @jsii.member(jsii_name="resetCustomTags")
    def reset_custom_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomTags", []))

    @jsii.member(jsii_name="resetDefaultTags")
    def reset_default_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTags", []))

    @jsii.member(jsii_name="resetDiskSpec")
    def reset_disk_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSpec", []))

    @jsii.member(jsii_name="resetEnableElasticDisk")
    def reset_enable_elastic_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableElasticDisk", []))

    @jsii.member(jsii_name="resetGcpAttributes")
    def reset_gcp_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpAttributes", []))

    @jsii.member(jsii_name="resetInstancePoolFleetAttributes")
    def reset_instance_pool_fleet_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancePoolFleetAttributes", []))

    @jsii.member(jsii_name="resetInstancePoolId")
    def reset_instance_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancePoolId", []))

    @jsii.member(jsii_name="resetMaxCapacity")
    def reset_max_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxCapacity", []))

    @jsii.member(jsii_name="resetMinIdleInstances")
    def reset_min_idle_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinIdleInstances", []))

    @jsii.member(jsii_name="resetNodeTypeId")
    def reset_node_type_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeTypeId", []))

    @jsii.member(jsii_name="resetPreloadedDockerImage")
    def reset_preloaded_docker_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreloadedDockerImage", []))

    @jsii.member(jsii_name="resetPreloadedSparkVersions")
    def reset_preloaded_spark_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreloadedSparkVersions", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @jsii.member(jsii_name="resetStats")
    def reset_stats(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStats", []))

    @builtins.property
    @jsii.member(jsii_name="awsAttributes")
    def aws_attributes(
        self,
    ) -> DataDatabricksInstancePoolPoolInfoAwsAttributesOutputReference:
        return typing.cast(DataDatabricksInstancePoolPoolInfoAwsAttributesOutputReference, jsii.get(self, "awsAttributes"))

    @builtins.property
    @jsii.member(jsii_name="azureAttributes")
    def azure_attributes(
        self,
    ) -> DataDatabricksInstancePoolPoolInfoAzureAttributesOutputReference:
        return typing.cast(DataDatabricksInstancePoolPoolInfoAzureAttributesOutputReference, jsii.get(self, "azureAttributes"))

    @builtins.property
    @jsii.member(jsii_name="diskSpec")
    def disk_spec(self) -> DataDatabricksInstancePoolPoolInfoDiskSpecOutputReference:
        return typing.cast(DataDatabricksInstancePoolPoolInfoDiskSpecOutputReference, jsii.get(self, "diskSpec"))

    @builtins.property
    @jsii.member(jsii_name="gcpAttributes")
    def gcp_attributes(
        self,
    ) -> DataDatabricksInstancePoolPoolInfoGcpAttributesOutputReference:
        return typing.cast(DataDatabricksInstancePoolPoolInfoGcpAttributesOutputReference, jsii.get(self, "gcpAttributes"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolFleetAttributes")
    def instance_pool_fleet_attributes(
        self,
    ) -> DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesList:
        return typing.cast(DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesList, jsii.get(self, "instancePoolFleetAttributes"))

    @builtins.property
    @jsii.member(jsii_name="preloadedDockerImage")
    def preloaded_docker_image(
        self,
    ) -> "DataDatabricksInstancePoolPoolInfoPreloadedDockerImageList":
        return typing.cast("DataDatabricksInstancePoolPoolInfoPreloadedDockerImageList", jsii.get(self, "preloadedDockerImage"))

    @builtins.property
    @jsii.member(jsii_name="stats")
    def stats(self) -> "DataDatabricksInstancePoolPoolInfoStatsOutputReference":
        return typing.cast("DataDatabricksInstancePoolPoolInfoStatsOutputReference", jsii.get(self, "stats"))

    @builtins.property
    @jsii.member(jsii_name="awsAttributesInput")
    def aws_attributes_input(
        self,
    ) -> typing.Optional[DataDatabricksInstancePoolPoolInfoAwsAttributes]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfoAwsAttributes], jsii.get(self, "awsAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="azureAttributesInput")
    def azure_attributes_input(
        self,
    ) -> typing.Optional[DataDatabricksInstancePoolPoolInfoAzureAttributes]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfoAzureAttributes], jsii.get(self, "azureAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="customTagsInput")
    def custom_tags_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTagsInput")
    def default_tags_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "defaultTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSpecInput")
    def disk_spec_input(
        self,
    ) -> typing.Optional[DataDatabricksInstancePoolPoolInfoDiskSpec]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfoDiskSpec], jsii.get(self, "diskSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="enableElasticDiskInput")
    def enable_elastic_disk_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableElasticDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="gcpAttributesInput")
    def gcp_attributes_input(
        self,
    ) -> typing.Optional[DataDatabricksInstancePoolPoolInfoGcpAttributes]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfoGcpAttributes], jsii.get(self, "gcpAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="idleInstanceAutoterminationMinutesInput")
    def idle_instance_autotermination_minutes_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleInstanceAutoterminationMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolFleetAttributesInput")
    def instance_pool_fleet_attributes_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes]]], jsii.get(self, "instancePoolFleetAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolIdInput")
    def instance_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instancePoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolNameInput")
    def instance_pool_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instancePoolNameInput"))

    @builtins.property
    @jsii.member(jsii_name="maxCapacityInput")
    def max_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="minIdleInstancesInput")
    def min_idle_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minIdleInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeTypeIdInput")
    def node_type_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeTypeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="preloadedDockerImageInput")
    def preloaded_docker_image_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksInstancePoolPoolInfoPreloadedDockerImage"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksInstancePoolPoolInfoPreloadedDockerImage"]]], jsii.get(self, "preloadedDockerImageInput"))

    @builtins.property
    @jsii.member(jsii_name="preloadedSparkVersionsInput")
    def preloaded_spark_versions_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "preloadedSparkVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="statsInput")
    def stats_input(self) -> typing.Optional["DataDatabricksInstancePoolPoolInfoStats"]:
        return typing.cast(typing.Optional["DataDatabricksInstancePoolPoolInfoStats"], jsii.get(self, "statsInput"))

    @builtins.property
    @jsii.member(jsii_name="customTags")
    def custom_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customTags"))

    @custom_tags.setter
    def custom_tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b9cc0604ab17c37b10ff9f9a51ee6f17a8ff47250f951350dfde801fd401973)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customTags", value)

    @builtins.property
    @jsii.member(jsii_name="defaultTags")
    def default_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "defaultTags"))

    @default_tags.setter
    def default_tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c89b47075d1c15bcdb22478c4fcc1e98638e1d90c3dbfb2e5639e8a24b521c9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTags", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__227160cda55e8a20652d5c447d1f487c56321b9e6391ed50758e5695c061f9d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableElasticDisk", value)

    @builtins.property
    @jsii.member(jsii_name="idleInstanceAutoterminationMinutes")
    def idle_instance_autotermination_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleInstanceAutoterminationMinutes"))

    @idle_instance_autotermination_minutes.setter
    def idle_instance_autotermination_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d97c3f0dc9709556edb2e9f178186ebba1ca5bd1648d08eb221d99910f44848)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleInstanceAutoterminationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="instancePoolId")
    def instance_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instancePoolId"))

    @instance_pool_id.setter
    def instance_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47cb61f8705a3261522d9f404fc6ba456dc7005e8e41c4dde4368d0cc7706a0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instancePoolId", value)

    @builtins.property
    @jsii.member(jsii_name="instancePoolName")
    def instance_pool_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instancePoolName"))

    @instance_pool_name.setter
    def instance_pool_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aabb06e204b18c7ff68daa0c193263be4115f3066ec19d6264ba98a74d55e949)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instancePoolName", value)

    @builtins.property
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxCapacity"))

    @max_capacity.setter
    def max_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f474d10ff11f2c1bfcb95ec8841e93e5c3074bc6b2ac01ac63fca87102b096e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="minIdleInstances")
    def min_idle_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minIdleInstances"))

    @min_idle_instances.setter
    def min_idle_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f2705c847622bb740a0d5914c7280d49c193cfd7061b2c6f8a266671b201dc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minIdleInstances", value)

    @builtins.property
    @jsii.member(jsii_name="nodeTypeId")
    def node_type_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeTypeId"))

    @node_type_id.setter
    def node_type_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49bfd2d769e935966296e5b794d0933b0fe2273ece6902ccb96ce82e59bea175)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeTypeId", value)

    @builtins.property
    @jsii.member(jsii_name="preloadedSparkVersions")
    def preloaded_spark_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "preloadedSparkVersions"))

    @preloaded_spark_versions.setter
    def preloaded_spark_versions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__537d0dbcb877a0a71eb05b4c987f457c83e3873db9b6d89080878c94e3c0d302)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preloadedSparkVersions", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07125fbdd08f86e595dfa080e5ed08fa752f696f6362f2f748321ec82d102cd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataDatabricksInstancePoolPoolInfo]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksInstancePoolPoolInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d69dff752e30ed458f3d9b6371dbaed25ab5b4a84a715e6e043083b101c142e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoPreloadedDockerImage",
    jsii_struct_bases=[],
    name_mapping={"url": "url", "basic_auth": "basicAuth"},
)
class DataDatabricksInstancePoolPoolInfoPreloadedDockerImage:
    def __init__(
        self,
        *,
        url: builtins.str,
        basic_auth: typing.Optional[typing.Union["DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuth", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#url DataDatabricksInstancePool#url}.
        :param basic_auth: basic_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#basic_auth DataDatabricksInstancePool#basic_auth}
        '''
        if isinstance(basic_auth, dict):
            basic_auth = DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuth(**basic_auth)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f940949a973f103d18afc8b9f8dcf78bdf489f72c795fe762dad80f63b5e7daa)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument basic_auth", value=basic_auth, expected_type=type_hints["basic_auth"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if basic_auth is not None:
            self._values["basic_auth"] = basic_auth

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#url DataDatabricksInstancePool#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def basic_auth(
        self,
    ) -> typing.Optional["DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuth"]:
        '''basic_auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#basic_auth DataDatabricksInstancePool#basic_auth}
        '''
        result = self._values.get("basic_auth")
        return typing.cast(typing.Optional["DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuth"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksInstancePoolPoolInfoPreloadedDockerImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuth",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuth:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#password DataDatabricksInstancePool#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#username DataDatabricksInstancePool#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2868bfd5ef3b4c38fa3d543682138c2fb4377fa0700172ec17a60f7aa20f4950)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#password DataDatabricksInstancePool#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#username DataDatabricksInstancePool#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuthOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuthOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2755bc649c70aa671dcd0d278c87a4b8d87330a28222ecde50e3826cd871b76)
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
            type_hints = typing.get_type_hints(_typecheckingstub__29456e320015607331818bea359924a29955b166e3eec3e80389ca4fd0c2abfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74c5cbc2e7ac9924a50058a9a8272fcb79e563b08c25676015bd104586141eca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuth]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50f95da479545fa8957b14b56162164e722d306c57b03321722ed9842f11aa1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksInstancePoolPoolInfoPreloadedDockerImageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoPreloadedDockerImageList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7903798074e396660677a59c450cded0fdd08a0614da8b2d883826b4e58cbb3f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDatabricksInstancePoolPoolInfoPreloadedDockerImageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23bc4db57f8747d89c72d23333eb6a2b1f733c437f8b0579ea1517634c974dbf)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataDatabricksInstancePoolPoolInfoPreloadedDockerImageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f446a9dd33d8c25fae775a50c352753f63377c87662544296df898cce7fab2a5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9d69dbab621d5cca460e8628c39ecaa2876cc9c4ac8a0d5ffe73b6e05043ff8f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__36e9c457542bee236cfabe1578e450182f2fd4e9fd42ac5dc2a9476432e56621)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksInstancePoolPoolInfoPreloadedDockerImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksInstancePoolPoolInfoPreloadedDockerImage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksInstancePoolPoolInfoPreloadedDockerImage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d5f6b0baa40f2ca4a7e74208aded6c8ba2111972af8e370ac6dce1d0d1f7d7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksInstancePoolPoolInfoPreloadedDockerImageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoPreloadedDockerImageOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f24309d12a2973eff9961d4ffdb07319e9c654f0952ddf45ae90c19e2dc4415)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putBasicAuth")
    def put_basic_auth(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#password DataDatabricksInstancePool#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#username DataDatabricksInstancePool#username}.
        '''
        value = DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuth(
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
    ) -> DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuthOutputReference:
        return typing.cast(DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuthOutputReference, jsii.get(self, "basicAuth"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthInput")
    def basic_auth_input(
        self,
    ) -> typing.Optional[DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuth]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuth], jsii.get(self, "basicAuthInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__41b54ac8c02d71c9e1ce3edb10ac02c5598cae8e39ba309146a868c0aee4c7a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoPreloadedDockerImage, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoPreloadedDockerImage, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoPreloadedDockerImage, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e011c0888c0831c908c8da8246bb5ac955d52405413f4275cea7f5a0d395f06e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoStats",
    jsii_struct_bases=[],
    name_mapping={
        "idle_count": "idleCount",
        "pending_idle_count": "pendingIdleCount",
        "pending_used_count": "pendingUsedCount",
        "used_count": "usedCount",
    },
)
class DataDatabricksInstancePoolPoolInfoStats:
    def __init__(
        self,
        *,
        idle_count: typing.Optional[jsii.Number] = None,
        pending_idle_count: typing.Optional[jsii.Number] = None,
        pending_used_count: typing.Optional[jsii.Number] = None,
        used_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param idle_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#idle_count DataDatabricksInstancePool#idle_count}.
        :param pending_idle_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#pending_idle_count DataDatabricksInstancePool#pending_idle_count}.
        :param pending_used_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#pending_used_count DataDatabricksInstancePool#pending_used_count}.
        :param used_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#used_count DataDatabricksInstancePool#used_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__004cfd317646d9481542df5a5e3d569563ae933f89412e51cd5a31017f653566)
            check_type(argname="argument idle_count", value=idle_count, expected_type=type_hints["idle_count"])
            check_type(argname="argument pending_idle_count", value=pending_idle_count, expected_type=type_hints["pending_idle_count"])
            check_type(argname="argument pending_used_count", value=pending_used_count, expected_type=type_hints["pending_used_count"])
            check_type(argname="argument used_count", value=used_count, expected_type=type_hints["used_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle_count is not None:
            self._values["idle_count"] = idle_count
        if pending_idle_count is not None:
            self._values["pending_idle_count"] = pending_idle_count
        if pending_used_count is not None:
            self._values["pending_used_count"] = pending_used_count
        if used_count is not None:
            self._values["used_count"] = used_count

    @builtins.property
    def idle_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#idle_count DataDatabricksInstancePool#idle_count}.'''
        result = self._values.get("idle_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pending_idle_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#pending_idle_count DataDatabricksInstancePool#pending_idle_count}.'''
        result = self._values.get("pending_idle_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pending_used_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#pending_used_count DataDatabricksInstancePool#pending_used_count}.'''
        result = self._values.get("pending_used_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def used_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/instance_pool#used_count DataDatabricksInstancePool#used_count}.'''
        result = self._values.get("used_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksInstancePoolPoolInfoStats(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksInstancePoolPoolInfoStatsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksInstancePool.DataDatabricksInstancePoolPoolInfoStatsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__99fd0204a0a5898e07bc8b2cf86a854991ed1743dda3ed91ab1cdd0e5233c725)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdleCount")
    def reset_idle_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleCount", []))

    @jsii.member(jsii_name="resetPendingIdleCount")
    def reset_pending_idle_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPendingIdleCount", []))

    @jsii.member(jsii_name="resetPendingUsedCount")
    def reset_pending_used_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPendingUsedCount", []))

    @jsii.member(jsii_name="resetUsedCount")
    def reset_used_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsedCount", []))

    @builtins.property
    @jsii.member(jsii_name="idleCountInput")
    def idle_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleCountInput"))

    @builtins.property
    @jsii.member(jsii_name="pendingIdleCountInput")
    def pending_idle_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "pendingIdleCountInput"))

    @builtins.property
    @jsii.member(jsii_name="pendingUsedCountInput")
    def pending_used_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "pendingUsedCountInput"))

    @builtins.property
    @jsii.member(jsii_name="usedCountInput")
    def used_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "usedCountInput"))

    @builtins.property
    @jsii.member(jsii_name="idleCount")
    def idle_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleCount"))

    @idle_count.setter
    def idle_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dca5c51c5e2ac258d8bb8aa9c4819858aa3d38cc547d6c7ff88d3703e3a49173)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleCount", value)

    @builtins.property
    @jsii.member(jsii_name="pendingIdleCount")
    def pending_idle_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "pendingIdleCount"))

    @pending_idle_count.setter
    def pending_idle_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef9160cdeadd2c36e3241a96bb3da38b96c85092fa87f3a475b72d7b2c7aa301)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pendingIdleCount", value)

    @builtins.property
    @jsii.member(jsii_name="pendingUsedCount")
    def pending_used_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "pendingUsedCount"))

    @pending_used_count.setter
    def pending_used_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7733a801ef14ff41b9e23670eacb201ffef75426e8467f0fc22be07f5c758e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pendingUsedCount", value)

    @builtins.property
    @jsii.member(jsii_name="usedCount")
    def used_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "usedCount"))

    @used_count.setter
    def used_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4636a04bd5a290af34fa5cb356b9e9f5a2ba273c2fd4adf000c4bddb7dd3354d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usedCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataDatabricksInstancePoolPoolInfoStats]:
        return typing.cast(typing.Optional[DataDatabricksInstancePoolPoolInfoStats], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksInstancePoolPoolInfoStats],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5673ee306d2723d9fdfddba581e83efd127919e79a3acb527aaf930333a378e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataDatabricksInstancePool",
    "DataDatabricksInstancePoolConfig",
    "DataDatabricksInstancePoolPoolInfo",
    "DataDatabricksInstancePoolPoolInfoAwsAttributes",
    "DataDatabricksInstancePoolPoolInfoAwsAttributesOutputReference",
    "DataDatabricksInstancePoolPoolInfoAzureAttributes",
    "DataDatabricksInstancePoolPoolInfoAzureAttributesOutputReference",
    "DataDatabricksInstancePoolPoolInfoDiskSpec",
    "DataDatabricksInstancePoolPoolInfoDiskSpecDiskType",
    "DataDatabricksInstancePoolPoolInfoDiskSpecDiskTypeOutputReference",
    "DataDatabricksInstancePoolPoolInfoDiskSpecOutputReference",
    "DataDatabricksInstancePoolPoolInfoGcpAttributes",
    "DataDatabricksInstancePoolPoolInfoGcpAttributesOutputReference",
    "DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes",
    "DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOption",
    "DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOptionOutputReference",
    "DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOption",
    "DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOptionOutputReference",
    "DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride",
    "DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverrideList",
    "DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverrideOutputReference",
    "DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesList",
    "DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesOutputReference",
    "DataDatabricksInstancePoolPoolInfoOutputReference",
    "DataDatabricksInstancePoolPoolInfoPreloadedDockerImage",
    "DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuth",
    "DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuthOutputReference",
    "DataDatabricksInstancePoolPoolInfoPreloadedDockerImageList",
    "DataDatabricksInstancePoolPoolInfoPreloadedDockerImageOutputReference",
    "DataDatabricksInstancePoolPoolInfoStats",
    "DataDatabricksInstancePoolPoolInfoStatsOutputReference",
]

publication.publish()

def _typecheckingstub__9f7ca568f8f220243c16aeb14de0cde47815b31f062b1efd4ca3b2a6a9d57364(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    pool_info: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfo, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__c455a8dd3f665aba3e3e1767da747b4eda08baee8371161a2834bc23d6bd6a1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3ba8889bad0c36cfcbe350abedc7de9335881010dfb45989b7c3dc65d756abd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3c11edb7e13c303a17566e0055db01202cae4a7aa9de0285ddae7a187fa0741(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    pool_info: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfo, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71aa1a3e37cc283977885db4ce62f72bb1eea5a1758193d1a9a350c88d7997c6(
    *,
    idle_instance_autotermination_minutes: jsii.Number,
    instance_pool_name: builtins.str,
    aws_attributes: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoAwsAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_attributes: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoAzureAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    default_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    disk_spec: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoDiskSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    gcp_attributes: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoGcpAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    instance_pool_fleet_attributes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes, typing.Dict[builtins.str, typing.Any]]]]] = None,
    instance_pool_id: typing.Optional[builtins.str] = None,
    max_capacity: typing.Optional[jsii.Number] = None,
    min_idle_instances: typing.Optional[jsii.Number] = None,
    node_type_id: typing.Optional[builtins.str] = None,
    preloaded_docker_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksInstancePoolPoolInfoPreloadedDockerImage, typing.Dict[builtins.str, typing.Any]]]]] = None,
    preloaded_spark_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    state: typing.Optional[builtins.str] = None,
    stats: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoStats, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e04f0f2bd5cfbcf69cebf7ac4c551c549fcf4cd90f912d9c5646c5f7ea215d88(
    *,
    availability: typing.Optional[builtins.str] = None,
    spot_bid_price_percent: typing.Optional[jsii.Number] = None,
    zone_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4198a332b9101ba6701f88e4938cb729a00f683734a7e3e35a74fab8206103a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2de8358c1fb2a97729a6145ddb1d4df852787b1d97954fed8030324fa229a993(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87869fb319047e2b38de86c43ba0f2818baa82fed4f1525558cc71139cc3855e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f4daa1cfd78ef5f4e27d1879d7a5739ca9ed1ca6ecee216f89b75a777723360(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e31055d1db1843401f6c6bff580f0d904ee96555efaff2bbad025aaf85d830f2(
    value: typing.Optional[DataDatabricksInstancePoolPoolInfoAwsAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d9f6bdb745b11f0069815f2a5dc2cbc433a50d352bebdcf8df8fd385b286249(
    *,
    availability: typing.Optional[builtins.str] = None,
    spot_bid_max_price: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18344d7b95740e7bbf418001550bc9249fe0d330664aaf4c589e3a7bcb2a6df1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f0aad6032cf82a3252d905c4248b01c4cf0e32c221054a5cdbd4d39eff7cba8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a018858c6735bd386db1c7abebc9117c3fbb19eac6aa45de4722f95f30ace7f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d932934b031b445d7095904f26374f3bdf22ae9dc9a2d5cfbb37547d4fb44e3(
    value: typing.Optional[DataDatabricksInstancePoolPoolInfoAzureAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f2325d622a653edd475f455bf1f47841d14201d1588c3b3dd6d3011825d783(
    *,
    disk_count: typing.Optional[jsii.Number] = None,
    disk_size: typing.Optional[jsii.Number] = None,
    disk_type: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoDiskSpecDiskType, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fdd6861484b029a1bc96919f2aabb661294292fb795d2a67423ee549a249fb8(
    *,
    azure_disk_volume_type: typing.Optional[builtins.str] = None,
    ebs_volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__232a16dfb9d2ab1fd50bcf929688e4886adaebc5552a68e1d7652a9ee380fcca(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23324ca2554d1b492064958a9a2d8f866588448219fc505f0eda6239b888a9dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1752e5d59c27ac77303406a41cdaa617f1bbc5950f7ca426f25ae23702e9b1b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33113ff6e03d1a7c8301e75299f8d71d1933c189bbb86fa273eeff7832bdc0e8(
    value: typing.Optional[DataDatabricksInstancePoolPoolInfoDiskSpecDiskType],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__667ecc016d979d2f6bfc547cc44cb75c755f8f25f8bf4835b247db80ee354249(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ac1286af20e21efbfe480f45bab80f3d55e70962fa47605b00aa8f4985d41f6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30716ef81730a97f9010d39e5a06becc9f25b6f3afc40fc1e1c7c348f7073758(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf17cc6f45b37910f35e4c9b443c00815050059a7b2edaa84962e9373e8d9a79(
    value: typing.Optional[DataDatabricksInstancePoolPoolInfoDiskSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__657f2beedae41b091551464288db80baa2d0d9add00e89b3ca4670bd878c9faa(
    *,
    gcp_availability: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07806c4de054d36bc01e4eb6a68e256c145bbf30c5c4f106e4f7e182597e1c5e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__069500366f86a92c85c4de2b56a68a6fdc7ca8d0d609ef90813123c3835f0fa3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2253174fc6800cf3cc086a6595edbaab8471bfefab4a2d35c0ec0fdc57490b1(
    value: typing.Optional[DataDatabricksInstancePoolPoolInfoGcpAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2c76a641e0630c03a24648969f1d24b079b2c50b68ea5f4f85d8b1e134f3f93(
    *,
    launch_template_override: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride, typing.Dict[builtins.str, typing.Any]]]],
    fleet_on_demand_option: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOption, typing.Dict[builtins.str, typing.Any]]] = None,
    fleet_spot_option: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOption, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff28981cd21add80e072ef24a952db575893b2929a8110daa54588ba3c63b798(
    *,
    allocation_strategy: builtins.str,
    instance_pools_to_use_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e25546780e7308c5b73451f984ccc8fcedca972e248ed458a91dfb7521472e78(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f33e758df9ad07d1d7be0931f6062c2b99e614293b6af24773cdb10808da3bfa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5733977065b9726d80e48cdb35eb22ef353d4faf1d4c90778fb0c18b643c609d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca2e4333dbee896a7d7975e7130a8ce71156d255e3343c9c55c6b217a1d2ac4(
    value: typing.Optional[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetOnDemandOption],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6250b06901ae61e86fd97ddd5a1c6b5e3f7a38704b3d3fa651e3cc1c683f149(
    *,
    allocation_strategy: builtins.str,
    instance_pools_to_use_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6e54e56fe8360c34d4d84bff172380f455fa61c3798d2a0e854292b33bd9eb9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfd26ceec344d7d215e0fcb44e221b8b814ef6d637e93aded2c7d6b7150a0fd5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__474920365bd7556349189a402d54a0073e3be86453ceebf9c72cd86d6c5a4886(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e09baf8e03f7e02782a2e9adedc2027433e4148fc645d0d3d2eda7b3643daecf(
    value: typing.Optional[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesFleetSpotOption],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1bd66f64fdb45d81658ebb20fc83cedc6ef00b6ae3e2bdb7af8ff2b4da11925(
    *,
    availability_zone: builtins.str,
    instance_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8ecc89a1c147020932b44086541c083797fa2615d4410052b566e35239a9523(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30c6f4ba8dd74302ec8104b84deef1d2b637371e82b9246ced9ede442c5733ba(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9c0e5262c93219c6ca7a019281673838e5e7592db3c8cd0754cc4635ee89acb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__977c320ae6920a20c8380833b2f19a5eb4b4cf22d8d21deba357c8764397b60d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cdba2db31270a08dce2d677333ddf5214fb22b2a4d09cf363d63eb4b4904fe7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9e60acd4f0e548e8c514f08d373f66ab75ffc0b27d0ddd21eb6d00dc0ea64af(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__894df49c6dfc9a37014982fdc931fa6e3ed53d7488d455e9232ba5452f59f472(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c28d6bade305dba7fd996ef353b729d86658637b0c486da1996946bc79eff968(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40ceefe079b24261928224ef62baca482854766da4cbef8280513410589aa043(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51ac1097061b9a6cb48a2230886c7dd35e04dd217e859d567420a9130bd32ecd(
    value: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d29c0afcc8725f72c08389fc98adedddf5af0c56e88ed6a3d2ab8d47aa83baa0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c42cd2072033f047a9bcddc371a2b5fd9c731f419a3a2b443734e54564a4ecd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5a30b6baa46b89c233a7c82c9a676f183d23a1f89b0740d7861e2208239e1a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21e20f2d20083c956f6ab5744543529a100d4548999cf465775865d441bc7c5d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9011b0f76b510b23208f9c4f74f172db426082036c866e25ce8e40f4ca530413(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f544dae4d0ba0a4dcbae6e103ca3cb7c43d8d1d795acfb01c66373aeb665ce6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11a27f6cb7a3e3a050697b4b903f06e3d3c711aa8fe913959591fec326c0a593(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88d9b0737ecc7351d81da3de96810b8275401906fb007b70a8e4355e6af761e8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributesLaunchTemplateOverride, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a875bcc1168e14ebdd862a4c1b0c7f79a9285450e289d193f5e72eb986efcd57(
    value: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7e1ea6bbc4aaf27bd60355b4ef9b0585d82e24e6cf4a9193781f92569e98a86(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__353a2f4c65f7c5c5f6feecc11fe14904d9a17af15125625b61f4d23d6120a39b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksInstancePoolPoolInfoInstancePoolFleetAttributes, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6596fdeb8509e2ca413ea8698d81f2b807dcc819934a2821985af1791b876ec(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksInstancePoolPoolInfoPreloadedDockerImage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b9cc0604ab17c37b10ff9f9a51ee6f17a8ff47250f951350dfde801fd401973(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c89b47075d1c15bcdb22478c4fcc1e98638e1d90c3dbfb2e5639e8a24b521c9c(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__227160cda55e8a20652d5c447d1f487c56321b9e6391ed50758e5695c061f9d7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d97c3f0dc9709556edb2e9f178186ebba1ca5bd1648d08eb221d99910f44848(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47cb61f8705a3261522d9f404fc6ba456dc7005e8e41c4dde4368d0cc7706a0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aabb06e204b18c7ff68daa0c193263be4115f3066ec19d6264ba98a74d55e949(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f474d10ff11f2c1bfcb95ec8841e93e5c3074bc6b2ac01ac63fca87102b096e0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f2705c847622bb740a0d5914c7280d49c193cfd7061b2c6f8a266671b201dc6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49bfd2d769e935966296e5b794d0933b0fe2273ece6902ccb96ce82e59bea175(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__537d0dbcb877a0a71eb05b4c987f457c83e3873db9b6d89080878c94e3c0d302(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07125fbdd08f86e595dfa080e5ed08fa752f696f6362f2f748321ec82d102cd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d69dff752e30ed458f3d9b6371dbaed25ab5b4a84a715e6e043083b101c142e4(
    value: typing.Optional[DataDatabricksInstancePoolPoolInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f940949a973f103d18afc8b9f8dcf78bdf489f72c795fe762dad80f63b5e7daa(
    *,
    url: builtins.str,
    basic_auth: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuth, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2868bfd5ef3b4c38fa3d543682138c2fb4377fa0700172ec17a60f7aa20f4950(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2755bc649c70aa671dcd0d278c87a4b8d87330a28222ecde50e3826cd871b76(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29456e320015607331818bea359924a29955b166e3eec3e80389ca4fd0c2abfe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74c5cbc2e7ac9924a50058a9a8272fcb79e563b08c25676015bd104586141eca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50f95da479545fa8957b14b56162164e722d306c57b03321722ed9842f11aa1d(
    value: typing.Optional[DataDatabricksInstancePoolPoolInfoPreloadedDockerImageBasicAuth],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7903798074e396660677a59c450cded0fdd08a0614da8b2d883826b4e58cbb3f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23bc4db57f8747d89c72d23333eb6a2b1f733c437f8b0579ea1517634c974dbf(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f446a9dd33d8c25fae775a50c352753f63377c87662544296df898cce7fab2a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d69dbab621d5cca460e8628c39ecaa2876cc9c4ac8a0d5ffe73b6e05043ff8f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36e9c457542bee236cfabe1578e450182f2fd4e9fd42ac5dc2a9476432e56621(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d5f6b0baa40f2ca4a7e74208aded6c8ba2111972af8e370ac6dce1d0d1f7d7e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksInstancePoolPoolInfoPreloadedDockerImage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f24309d12a2973eff9961d4ffdb07319e9c654f0952ddf45ae90c19e2dc4415(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41b54ac8c02d71c9e1ce3edb10ac02c5598cae8e39ba309146a868c0aee4c7a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e011c0888c0831c908c8da8246bb5ac955d52405413f4275cea7f5a0d395f06e(
    value: typing.Optional[typing.Union[DataDatabricksInstancePoolPoolInfoPreloadedDockerImage, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__004cfd317646d9481542df5a5e3d569563ae933f89412e51cd5a31017f653566(
    *,
    idle_count: typing.Optional[jsii.Number] = None,
    pending_idle_count: typing.Optional[jsii.Number] = None,
    pending_used_count: typing.Optional[jsii.Number] = None,
    used_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99fd0204a0a5898e07bc8b2cf86a854991ed1743dda3ed91ab1cdd0e5233c725(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dca5c51c5e2ac258d8bb8aa9c4819858aa3d38cc547d6c7ff88d3703e3a49173(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef9160cdeadd2c36e3241a96bb3da38b96c85092fa87f3a475b72d7b2c7aa301(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7733a801ef14ff41b9e23670eacb201ffef75426e8467f0fc22be07f5c758e8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4636a04bd5a290af34fa5cb356b9e9f5a2ba273c2fd4adf000c4bddb7dd3354d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5673ee306d2723d9fdfddba581e83efd127919e79a3acb527aaf930333a378e(
    value: typing.Optional[DataDatabricksInstancePoolPoolInfoStats],
) -> None:
    """Type checking stubs"""
    pass
