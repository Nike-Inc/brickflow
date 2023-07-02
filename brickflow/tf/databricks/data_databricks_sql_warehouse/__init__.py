'''
# `data_databricks_sql_warehouse`

Refer to the Terraform Registory for docs: [`data_databricks_sql_warehouse`](https://www.terraform.io/docs/providers/databricks/d/sql_warehouse).
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


class DataDatabricksSqlWarehouse(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksSqlWarehouse.DataDatabricksSqlWarehouse",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse databricks_sql_warehouse}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        id: builtins.str,
        auto_stop_mins: typing.Optional[jsii.Number] = None,
        channel: typing.Optional[typing.Union["DataDatabricksSqlWarehouseChannel", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_size: typing.Optional[builtins.str] = None,
        data_source_id: typing.Optional[builtins.str] = None,
        enable_photon: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_serverless_compute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        instance_profile_arn: typing.Optional[builtins.str] = None,
        jdbc_url: typing.Optional[builtins.str] = None,
        max_num_clusters: typing.Optional[jsii.Number] = None,
        min_num_clusters: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        num_clusters: typing.Optional[jsii.Number] = None,
        odbc_params: typing.Optional[typing.Union["DataDatabricksSqlWarehouseOdbcParams", typing.Dict[builtins.str, typing.Any]]] = None,
        spot_instance_policy: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union["DataDatabricksSqlWarehouseTags", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse databricks_sql_warehouse} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#id DataDatabricksSqlWarehouse#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param auto_stop_mins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#auto_stop_mins DataDatabricksSqlWarehouse#auto_stop_mins}.
        :param channel: channel block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#channel DataDatabricksSqlWarehouse#channel}
        :param cluster_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#cluster_size DataDatabricksSqlWarehouse#cluster_size}.
        :param data_source_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#data_source_id DataDatabricksSqlWarehouse#data_source_id}.
        :param enable_photon: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#enable_photon DataDatabricksSqlWarehouse#enable_photon}.
        :param enable_serverless_compute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#enable_serverless_compute DataDatabricksSqlWarehouse#enable_serverless_compute}.
        :param instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#instance_profile_arn DataDatabricksSqlWarehouse#instance_profile_arn}.
        :param jdbc_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#jdbc_url DataDatabricksSqlWarehouse#jdbc_url}.
        :param max_num_clusters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#max_num_clusters DataDatabricksSqlWarehouse#max_num_clusters}.
        :param min_num_clusters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#min_num_clusters DataDatabricksSqlWarehouse#min_num_clusters}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#name DataDatabricksSqlWarehouse#name}.
        :param num_clusters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#num_clusters DataDatabricksSqlWarehouse#num_clusters}.
        :param odbc_params: odbc_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#odbc_params DataDatabricksSqlWarehouse#odbc_params}
        :param spot_instance_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#spot_instance_policy DataDatabricksSqlWarehouse#spot_instance_policy}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#state DataDatabricksSqlWarehouse#state}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#tags DataDatabricksSqlWarehouse#tags}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75c99fe2f944de95e49e5e1859f9575289a7996aecdc17caec92a9fcbae1d8aa)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataDatabricksSqlWarehouseConfig(
            id=id,
            auto_stop_mins=auto_stop_mins,
            channel=channel,
            cluster_size=cluster_size,
            data_source_id=data_source_id,
            enable_photon=enable_photon,
            enable_serverless_compute=enable_serverless_compute,
            instance_profile_arn=instance_profile_arn,
            jdbc_url=jdbc_url,
            max_num_clusters=max_num_clusters,
            min_num_clusters=min_num_clusters,
            name=name,
            num_clusters=num_clusters,
            odbc_params=odbc_params,
            spot_instance_policy=spot_instance_policy,
            state=state,
            tags=tags,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putChannel")
    def put_channel(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#name DataDatabricksSqlWarehouse#name}.
        '''
        value = DataDatabricksSqlWarehouseChannel(name=name)

        return typing.cast(None, jsii.invoke(self, "putChannel", [value]))

    @jsii.member(jsii_name="putOdbcParams")
    def put_odbc_params(
        self,
        *,
        path: builtins.str,
        port: jsii.Number,
        protocol: builtins.str,
        host: typing.Optional[builtins.str] = None,
        hostname: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#path DataDatabricksSqlWarehouse#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#port DataDatabricksSqlWarehouse#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#protocol DataDatabricksSqlWarehouse#protocol}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#host DataDatabricksSqlWarehouse#host}.
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#hostname DataDatabricksSqlWarehouse#hostname}.
        '''
        value = DataDatabricksSqlWarehouseOdbcParams(
            path=path, port=port, protocol=protocol, host=host, hostname=hostname
        )

        return typing.cast(None, jsii.invoke(self, "putOdbcParams", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        *,
        custom_tags: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksSqlWarehouseTagsCustomTags", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param custom_tags: custom_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#custom_tags DataDatabricksSqlWarehouse#custom_tags}
        '''
        value = DataDatabricksSqlWarehouseTags(custom_tags=custom_tags)

        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetAutoStopMins")
    def reset_auto_stop_mins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoStopMins", []))

    @jsii.member(jsii_name="resetChannel")
    def reset_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChannel", []))

    @jsii.member(jsii_name="resetClusterSize")
    def reset_cluster_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterSize", []))

    @jsii.member(jsii_name="resetDataSourceId")
    def reset_data_source_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataSourceId", []))

    @jsii.member(jsii_name="resetEnablePhoton")
    def reset_enable_photon(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablePhoton", []))

    @jsii.member(jsii_name="resetEnableServerlessCompute")
    def reset_enable_serverless_compute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableServerlessCompute", []))

    @jsii.member(jsii_name="resetInstanceProfileArn")
    def reset_instance_profile_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceProfileArn", []))

    @jsii.member(jsii_name="resetJdbcUrl")
    def reset_jdbc_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJdbcUrl", []))

    @jsii.member(jsii_name="resetMaxNumClusters")
    def reset_max_num_clusters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxNumClusters", []))

    @jsii.member(jsii_name="resetMinNumClusters")
    def reset_min_num_clusters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinNumClusters", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNumClusters")
    def reset_num_clusters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumClusters", []))

    @jsii.member(jsii_name="resetOdbcParams")
    def reset_odbc_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOdbcParams", []))

    @jsii.member(jsii_name="resetSpotInstancePolicy")
    def reset_spot_instance_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotInstancePolicy", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="channel")
    def channel(self) -> "DataDatabricksSqlWarehouseChannelOutputReference":
        return typing.cast("DataDatabricksSqlWarehouseChannelOutputReference", jsii.get(self, "channel"))

    @builtins.property
    @jsii.member(jsii_name="odbcParams")
    def odbc_params(self) -> "DataDatabricksSqlWarehouseOdbcParamsOutputReference":
        return typing.cast("DataDatabricksSqlWarehouseOdbcParamsOutputReference", jsii.get(self, "odbcParams"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "DataDatabricksSqlWarehouseTagsOutputReference":
        return typing.cast("DataDatabricksSqlWarehouseTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="autoStopMinsInput")
    def auto_stop_mins_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autoStopMinsInput"))

    @builtins.property
    @jsii.member(jsii_name="channelInput")
    def channel_input(self) -> typing.Optional["DataDatabricksSqlWarehouseChannel"]:
        return typing.cast(typing.Optional["DataDatabricksSqlWarehouseChannel"], jsii.get(self, "channelInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterSizeInput")
    def cluster_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceIdInput")
    def data_source_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="enablePhotonInput")
    def enable_photon_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enablePhotonInput"))

    @builtins.property
    @jsii.member(jsii_name="enableServerlessComputeInput")
    def enable_serverless_compute_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableServerlessComputeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceProfileArnInput")
    def instance_profile_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceProfileArnInput"))

    @builtins.property
    @jsii.member(jsii_name="jdbcUrlInput")
    def jdbc_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jdbcUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="maxNumClustersInput")
    def max_num_clusters_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxNumClustersInput"))

    @builtins.property
    @jsii.member(jsii_name="minNumClustersInput")
    def min_num_clusters_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minNumClustersInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="numClustersInput")
    def num_clusters_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numClustersInput"))

    @builtins.property
    @jsii.member(jsii_name="odbcParamsInput")
    def odbc_params_input(
        self,
    ) -> typing.Optional["DataDatabricksSqlWarehouseOdbcParams"]:
        return typing.cast(typing.Optional["DataDatabricksSqlWarehouseOdbcParams"], jsii.get(self, "odbcParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="spotInstancePolicyInput")
    def spot_instance_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spotInstancePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional["DataDatabricksSqlWarehouseTags"]:
        return typing.cast(typing.Optional["DataDatabricksSqlWarehouseTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoStopMins")
    def auto_stop_mins(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autoStopMins"))

    @auto_stop_mins.setter
    def auto_stop_mins(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d31419fab62847b3ca98f91e4a4fdec5e9c405173299477580ca6ee0fce9e93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoStopMins", value)

    @builtins.property
    @jsii.member(jsii_name="clusterSize")
    def cluster_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterSize"))

    @cluster_size.setter
    def cluster_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__669953b61623fc4680a59361f736f6911b638b34777c1adfec81a3462561b563)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterSize", value)

    @builtins.property
    @jsii.member(jsii_name="dataSourceId")
    def data_source_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSourceId"))

    @data_source_id.setter
    def data_source_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52648d5d047380e8f746f3c1f666562d59a5615fc28edd1fdf271ed8fc228646)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSourceId", value)

    @builtins.property
    @jsii.member(jsii_name="enablePhoton")
    def enable_photon(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enablePhoton"))

    @enable_photon.setter
    def enable_photon(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a24577774b63e963942a867449aa4d0691cd3f3c5228a8c5f4c7ea7a7c95fb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePhoton", value)

    @builtins.property
    @jsii.member(jsii_name="enableServerlessCompute")
    def enable_serverless_compute(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableServerlessCompute"))

    @enable_serverless_compute.setter
    def enable_serverless_compute(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7e9b650227c1422a83bee496fcc42af00e9043a0062c63bae9fafa82be7b437)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableServerlessCompute", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7e171c39cc6dda4e8a85dc03bd63fa17bea5503955435e94df31e2cc16c9d3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfileArn")
    def instance_profile_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceProfileArn"))

    @instance_profile_arn.setter
    def instance_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adc19dc9bd0dd7ba5b20f6cc0d77cc1f8b1469d711a6991e1dac745c8df95bc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="jdbcUrl")
    def jdbc_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jdbcUrl"))

    @jdbc_url.setter
    def jdbc_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7725d6a390c78403aadb20b05518e7842ad869c2b1e2e47099c72215d4daae5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jdbcUrl", value)

    @builtins.property
    @jsii.member(jsii_name="maxNumClusters")
    def max_num_clusters(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxNumClusters"))

    @max_num_clusters.setter
    def max_num_clusters(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67c8db8a8926b1cdde12a20d26cf8ad78ffb46c8a7cb43dec65dd94a4b820931)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxNumClusters", value)

    @builtins.property
    @jsii.member(jsii_name="minNumClusters")
    def min_num_clusters(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minNumClusters"))

    @min_num_clusters.setter
    def min_num_clusters(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0749482c6adbf1b01de082b5d15cbbc6218b386cf22bd832e6bd5789d302ad6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minNumClusters", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5385e5e31dff3362e240cdfc7916a32749eaa2894b67d74a5fd0adb1fdc4b8c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="numClusters")
    def num_clusters(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numClusters"))

    @num_clusters.setter
    def num_clusters(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c03ef9db17d3c26c142b7998863c2d95144ae8735e2e02c0bf6d9e37b2ec5d6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numClusters", value)

    @builtins.property
    @jsii.member(jsii_name="spotInstancePolicy")
    def spot_instance_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotInstancePolicy"))

    @spot_instance_policy.setter
    def spot_instance_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f6b6ef7718e78739e72a01c207465d7b0bb10a1b6ad7e76d90653f66d3d6f56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotInstancePolicy", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__345e69737159184fb13dd974268ddbcad61126422e41ae6bc32a5a226201929d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksSqlWarehouse.DataDatabricksSqlWarehouseChannel",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class DataDatabricksSqlWarehouseChannel:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#name DataDatabricksSqlWarehouse#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__237cbf54b853e2f48549b11dd05026367716c1e6909b86a82fc244d45bd559c3)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#name DataDatabricksSqlWarehouse#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksSqlWarehouseChannel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksSqlWarehouseChannelOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksSqlWarehouse.DataDatabricksSqlWarehouseChannelOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__60f36b07f83c571eb172ae981cfe1eb53eef37e8cd4a06fd66999b87ec6d1098)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53231eae5a767d1de3ff5c41f663e49702b443d0b3415e3dac7f6bc8940a6519)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataDatabricksSqlWarehouseChannel]:
        return typing.cast(typing.Optional[DataDatabricksSqlWarehouseChannel], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksSqlWarehouseChannel],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b76a6a112ff86fe4964a5a54626dedd906a7967e9ec076de281d3c155fdaec0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksSqlWarehouse.DataDatabricksSqlWarehouseConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "id": "id",
        "auto_stop_mins": "autoStopMins",
        "channel": "channel",
        "cluster_size": "clusterSize",
        "data_source_id": "dataSourceId",
        "enable_photon": "enablePhoton",
        "enable_serverless_compute": "enableServerlessCompute",
        "instance_profile_arn": "instanceProfileArn",
        "jdbc_url": "jdbcUrl",
        "max_num_clusters": "maxNumClusters",
        "min_num_clusters": "minNumClusters",
        "name": "name",
        "num_clusters": "numClusters",
        "odbc_params": "odbcParams",
        "spot_instance_policy": "spotInstancePolicy",
        "state": "state",
        "tags": "tags",
    },
)
class DataDatabricksSqlWarehouseConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        id: builtins.str,
        auto_stop_mins: typing.Optional[jsii.Number] = None,
        channel: typing.Optional[typing.Union[DataDatabricksSqlWarehouseChannel, typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_size: typing.Optional[builtins.str] = None,
        data_source_id: typing.Optional[builtins.str] = None,
        enable_photon: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_serverless_compute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        instance_profile_arn: typing.Optional[builtins.str] = None,
        jdbc_url: typing.Optional[builtins.str] = None,
        max_num_clusters: typing.Optional[jsii.Number] = None,
        min_num_clusters: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        num_clusters: typing.Optional[jsii.Number] = None,
        odbc_params: typing.Optional[typing.Union["DataDatabricksSqlWarehouseOdbcParams", typing.Dict[builtins.str, typing.Any]]] = None,
        spot_instance_policy: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union["DataDatabricksSqlWarehouseTags", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#id DataDatabricksSqlWarehouse#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param auto_stop_mins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#auto_stop_mins DataDatabricksSqlWarehouse#auto_stop_mins}.
        :param channel: channel block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#channel DataDatabricksSqlWarehouse#channel}
        :param cluster_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#cluster_size DataDatabricksSqlWarehouse#cluster_size}.
        :param data_source_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#data_source_id DataDatabricksSqlWarehouse#data_source_id}.
        :param enable_photon: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#enable_photon DataDatabricksSqlWarehouse#enable_photon}.
        :param enable_serverless_compute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#enable_serverless_compute DataDatabricksSqlWarehouse#enable_serverless_compute}.
        :param instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#instance_profile_arn DataDatabricksSqlWarehouse#instance_profile_arn}.
        :param jdbc_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#jdbc_url DataDatabricksSqlWarehouse#jdbc_url}.
        :param max_num_clusters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#max_num_clusters DataDatabricksSqlWarehouse#max_num_clusters}.
        :param min_num_clusters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#min_num_clusters DataDatabricksSqlWarehouse#min_num_clusters}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#name DataDatabricksSqlWarehouse#name}.
        :param num_clusters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#num_clusters DataDatabricksSqlWarehouse#num_clusters}.
        :param odbc_params: odbc_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#odbc_params DataDatabricksSqlWarehouse#odbc_params}
        :param spot_instance_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#spot_instance_policy DataDatabricksSqlWarehouse#spot_instance_policy}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#state DataDatabricksSqlWarehouse#state}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#tags DataDatabricksSqlWarehouse#tags}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(channel, dict):
            channel = DataDatabricksSqlWarehouseChannel(**channel)
        if isinstance(odbc_params, dict):
            odbc_params = DataDatabricksSqlWarehouseOdbcParams(**odbc_params)
        if isinstance(tags, dict):
            tags = DataDatabricksSqlWarehouseTags(**tags)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__334d6fff894ce4a90d5bd53054792068ad1414ae5e8500f56e41377a2053283b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument auto_stop_mins", value=auto_stop_mins, expected_type=type_hints["auto_stop_mins"])
            check_type(argname="argument channel", value=channel, expected_type=type_hints["channel"])
            check_type(argname="argument cluster_size", value=cluster_size, expected_type=type_hints["cluster_size"])
            check_type(argname="argument data_source_id", value=data_source_id, expected_type=type_hints["data_source_id"])
            check_type(argname="argument enable_photon", value=enable_photon, expected_type=type_hints["enable_photon"])
            check_type(argname="argument enable_serverless_compute", value=enable_serverless_compute, expected_type=type_hints["enable_serverless_compute"])
            check_type(argname="argument instance_profile_arn", value=instance_profile_arn, expected_type=type_hints["instance_profile_arn"])
            check_type(argname="argument jdbc_url", value=jdbc_url, expected_type=type_hints["jdbc_url"])
            check_type(argname="argument max_num_clusters", value=max_num_clusters, expected_type=type_hints["max_num_clusters"])
            check_type(argname="argument min_num_clusters", value=min_num_clusters, expected_type=type_hints["min_num_clusters"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument num_clusters", value=num_clusters, expected_type=type_hints["num_clusters"])
            check_type(argname="argument odbc_params", value=odbc_params, expected_type=type_hints["odbc_params"])
            check_type(argname="argument spot_instance_policy", value=spot_instance_policy, expected_type=type_hints["spot_instance_policy"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
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
        if auto_stop_mins is not None:
            self._values["auto_stop_mins"] = auto_stop_mins
        if channel is not None:
            self._values["channel"] = channel
        if cluster_size is not None:
            self._values["cluster_size"] = cluster_size
        if data_source_id is not None:
            self._values["data_source_id"] = data_source_id
        if enable_photon is not None:
            self._values["enable_photon"] = enable_photon
        if enable_serverless_compute is not None:
            self._values["enable_serverless_compute"] = enable_serverless_compute
        if instance_profile_arn is not None:
            self._values["instance_profile_arn"] = instance_profile_arn
        if jdbc_url is not None:
            self._values["jdbc_url"] = jdbc_url
        if max_num_clusters is not None:
            self._values["max_num_clusters"] = max_num_clusters
        if min_num_clusters is not None:
            self._values["min_num_clusters"] = min_num_clusters
        if name is not None:
            self._values["name"] = name
        if num_clusters is not None:
            self._values["num_clusters"] = num_clusters
        if odbc_params is not None:
            self._values["odbc_params"] = odbc_params
        if spot_instance_policy is not None:
            self._values["spot_instance_policy"] = spot_instance_policy
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags

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
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#id DataDatabricksSqlWarehouse#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_stop_mins(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#auto_stop_mins DataDatabricksSqlWarehouse#auto_stop_mins}.'''
        result = self._values.get("auto_stop_mins")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def channel(self) -> typing.Optional[DataDatabricksSqlWarehouseChannel]:
        '''channel block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#channel DataDatabricksSqlWarehouse#channel}
        '''
        result = self._values.get("channel")
        return typing.cast(typing.Optional[DataDatabricksSqlWarehouseChannel], result)

    @builtins.property
    def cluster_size(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#cluster_size DataDatabricksSqlWarehouse#cluster_size}.'''
        result = self._values.get("cluster_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_source_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#data_source_id DataDatabricksSqlWarehouse#data_source_id}.'''
        result = self._values.get("data_source_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_photon(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#enable_photon DataDatabricksSqlWarehouse#enable_photon}.'''
        result = self._values.get("enable_photon")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_serverless_compute(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#enable_serverless_compute DataDatabricksSqlWarehouse#enable_serverless_compute}.'''
        result = self._values.get("enable_serverless_compute")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#instance_profile_arn DataDatabricksSqlWarehouse#instance_profile_arn}.'''
        result = self._values.get("instance_profile_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jdbc_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#jdbc_url DataDatabricksSqlWarehouse#jdbc_url}.'''
        result = self._values.get("jdbc_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_num_clusters(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#max_num_clusters DataDatabricksSqlWarehouse#max_num_clusters}.'''
        result = self._values.get("max_num_clusters")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_num_clusters(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#min_num_clusters DataDatabricksSqlWarehouse#min_num_clusters}.'''
        result = self._values.get("min_num_clusters")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#name DataDatabricksSqlWarehouse#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_clusters(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#num_clusters DataDatabricksSqlWarehouse#num_clusters}.'''
        result = self._values.get("num_clusters")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def odbc_params(self) -> typing.Optional["DataDatabricksSqlWarehouseOdbcParams"]:
        '''odbc_params block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#odbc_params DataDatabricksSqlWarehouse#odbc_params}
        '''
        result = self._values.get("odbc_params")
        return typing.cast(typing.Optional["DataDatabricksSqlWarehouseOdbcParams"], result)

    @builtins.property
    def spot_instance_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#spot_instance_policy DataDatabricksSqlWarehouse#spot_instance_policy}.'''
        result = self._values.get("spot_instance_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#state DataDatabricksSqlWarehouse#state}.'''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional["DataDatabricksSqlWarehouseTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#tags DataDatabricksSqlWarehouse#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["DataDatabricksSqlWarehouseTags"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksSqlWarehouseConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.dataDatabricksSqlWarehouse.DataDatabricksSqlWarehouseOdbcParams",
    jsii_struct_bases=[],
    name_mapping={
        "path": "path",
        "port": "port",
        "protocol": "protocol",
        "host": "host",
        "hostname": "hostname",
    },
)
class DataDatabricksSqlWarehouseOdbcParams:
    def __init__(
        self,
        *,
        path: builtins.str,
        port: jsii.Number,
        protocol: builtins.str,
        host: typing.Optional[builtins.str] = None,
        hostname: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#path DataDatabricksSqlWarehouse#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#port DataDatabricksSqlWarehouse#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#protocol DataDatabricksSqlWarehouse#protocol}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#host DataDatabricksSqlWarehouse#host}.
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#hostname DataDatabricksSqlWarehouse#hostname}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fba4640feb1646afb5a2d559ef9c8d7bd49a281607064127769e2ca4aa19b07)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path": path,
            "port": port,
            "protocol": protocol,
        }
        if host is not None:
            self._values["host"] = host
        if hostname is not None:
            self._values["hostname"] = hostname

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#path DataDatabricksSqlWarehouse#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#port DataDatabricksSqlWarehouse#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#protocol DataDatabricksSqlWarehouse#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#host DataDatabricksSqlWarehouse#host}.'''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#hostname DataDatabricksSqlWarehouse#hostname}.'''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksSqlWarehouseOdbcParams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksSqlWarehouseOdbcParamsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksSqlWarehouse.DataDatabricksSqlWarehouseOdbcParamsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f4ce13116e8fb0560a99c28374717acf70b70af83eb0c939bdeb7f1d54fc026)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e4e638a2f3435b586f3daf168e68f4d5f74154a66adddc3efde2ed923dfb1b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84285b497c3c3d2d23ee043534028b8a999b1d534b8b5ad341c009f8a205f32f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47d104f43a0c9955ad87f70fb059fc02a08424579335ee4a2cbbb2117447c24c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb27602db8847e79e05600abea25212e8bcc410db5bd553d943b63b74f44219b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79c53aba1947ed3f59d829abb707fc5a90839b958ed645ff6ef2f73e8506188c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataDatabricksSqlWarehouseOdbcParams]:
        return typing.cast(typing.Optional[DataDatabricksSqlWarehouseOdbcParams], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksSqlWarehouseOdbcParams],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2423c59e1081bf18f84c0bfddf9a08a3afa4b9086090e11d847794a20869ef58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksSqlWarehouse.DataDatabricksSqlWarehouseTags",
    jsii_struct_bases=[],
    name_mapping={"custom_tags": "customTags"},
)
class DataDatabricksSqlWarehouseTags:
    def __init__(
        self,
        *,
        custom_tags: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksSqlWarehouseTagsCustomTags", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param custom_tags: custom_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#custom_tags DataDatabricksSqlWarehouse#custom_tags}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43ebcef35775128b31ee6b1b0018ea7408daea1a373ba8d8bcd18b2224bf35cc)
            check_type(argname="argument custom_tags", value=custom_tags, expected_type=type_hints["custom_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "custom_tags": custom_tags,
        }

    @builtins.property
    def custom_tags(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksSqlWarehouseTagsCustomTags"]]:
        '''custom_tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#custom_tags DataDatabricksSqlWarehouse#custom_tags}
        '''
        result = self._values.get("custom_tags")
        assert result is not None, "Required property 'custom_tags' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksSqlWarehouseTagsCustomTags"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksSqlWarehouseTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.dataDatabricksSqlWarehouse.DataDatabricksSqlWarehouseTagsCustomTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class DataDatabricksSqlWarehouseTagsCustomTags:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#key DataDatabricksSqlWarehouse#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#value DataDatabricksSqlWarehouse#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__005ec4813de0a9d8fd274a5e76586566c010a0439a946b594c978aa72bdf552b)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#key DataDatabricksSqlWarehouse#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/sql_warehouse#value DataDatabricksSqlWarehouse#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksSqlWarehouseTagsCustomTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksSqlWarehouseTagsCustomTagsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksSqlWarehouse.DataDatabricksSqlWarehouseTagsCustomTagsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__105d8ecbe70a42869361f065f86826158f2797bb6214da92f80ec6f0108b4bb3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDatabricksSqlWarehouseTagsCustomTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e4ab22913f7a52d551862ba9a2885148882cb479fcab512cb8fd9db4d8d5a65)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataDatabricksSqlWarehouseTagsCustomTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f33cd8ca34d638543f60722f02ce2c324c8789e2fa0cfba7bb56f49cb997177)
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
            type_hints = typing.get_type_hints(_typecheckingstub__be7b74ea805d50e3807e88dd55b096ea97566609c17ede6d0fecd73c491ff294)
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
            type_hints = typing.get_type_hints(_typecheckingstub__91dd3571d63126fe8e5b96b2bb789a879ec87ecab219814fcb5e30ca2037b9ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksSqlWarehouseTagsCustomTags]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksSqlWarehouseTagsCustomTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksSqlWarehouseTagsCustomTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e74b455d2a3c842d1ee7f4e64f08fc5f3bea31c7511a3c4af1c2658f9d118abd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksSqlWarehouseTagsCustomTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksSqlWarehouse.DataDatabricksSqlWarehouseTagsCustomTagsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f55862801974452d3199ccec7a74f2f6630df0d26b37f21df97db9a4794491a9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8801a02cc0e710c3df34f6beee0baa96476c5f53d505379fb1561d7fc756d9af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b523719db7f747534ebf24aef8b2f8cebabeae6a563ad58366f4f29f5b2f093)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataDatabricksSqlWarehouseTagsCustomTags, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataDatabricksSqlWarehouseTagsCustomTags, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataDatabricksSqlWarehouseTagsCustomTags, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f7868924900b5e6f3eedacebcd13553411c6dc1ed358d9c909fa2c34dd0db6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksSqlWarehouseTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksSqlWarehouse.DataDatabricksSqlWarehouseTagsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d0a2eca6b9b46dcc503c291b305920b635c716ab72cab6f133ff7876feba11c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomTags")
    def put_custom_tags(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksSqlWarehouseTagsCustomTags, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05714b74cb0c9795e46239eb2dd00db827b43328e064e82ff52a1b4150a72182)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomTags", [value]))

    @builtins.property
    @jsii.member(jsii_name="customTags")
    def custom_tags(self) -> DataDatabricksSqlWarehouseTagsCustomTagsList:
        return typing.cast(DataDatabricksSqlWarehouseTagsCustomTagsList, jsii.get(self, "customTags"))

    @builtins.property
    @jsii.member(jsii_name="customTagsInput")
    def custom_tags_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksSqlWarehouseTagsCustomTags]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksSqlWarehouseTagsCustomTags]]], jsii.get(self, "customTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataDatabricksSqlWarehouseTags]:
        return typing.cast(typing.Optional[DataDatabricksSqlWarehouseTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataDatabricksSqlWarehouseTags],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f78c1162666a4589e7a55cd6edef4d122f3ad8fe1ac861bcfbf5eaa673fcee1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataDatabricksSqlWarehouse",
    "DataDatabricksSqlWarehouseChannel",
    "DataDatabricksSqlWarehouseChannelOutputReference",
    "DataDatabricksSqlWarehouseConfig",
    "DataDatabricksSqlWarehouseOdbcParams",
    "DataDatabricksSqlWarehouseOdbcParamsOutputReference",
    "DataDatabricksSqlWarehouseTags",
    "DataDatabricksSqlWarehouseTagsCustomTags",
    "DataDatabricksSqlWarehouseTagsCustomTagsList",
    "DataDatabricksSqlWarehouseTagsCustomTagsOutputReference",
    "DataDatabricksSqlWarehouseTagsOutputReference",
]

publication.publish()

def _typecheckingstub__75c99fe2f944de95e49e5e1859f9575289a7996aecdc17caec92a9fcbae1d8aa(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    id: builtins.str,
    auto_stop_mins: typing.Optional[jsii.Number] = None,
    channel: typing.Optional[typing.Union[DataDatabricksSqlWarehouseChannel, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_size: typing.Optional[builtins.str] = None,
    data_source_id: typing.Optional[builtins.str] = None,
    enable_photon: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_serverless_compute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    instance_profile_arn: typing.Optional[builtins.str] = None,
    jdbc_url: typing.Optional[builtins.str] = None,
    max_num_clusters: typing.Optional[jsii.Number] = None,
    min_num_clusters: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    num_clusters: typing.Optional[jsii.Number] = None,
    odbc_params: typing.Optional[typing.Union[DataDatabricksSqlWarehouseOdbcParams, typing.Dict[builtins.str, typing.Any]]] = None,
    spot_instance_policy: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Union[DataDatabricksSqlWarehouseTags, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__5d31419fab62847b3ca98f91e4a4fdec5e9c405173299477580ca6ee0fce9e93(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__669953b61623fc4680a59361f736f6911b638b34777c1adfec81a3462561b563(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52648d5d047380e8f746f3c1f666562d59a5615fc28edd1fdf271ed8fc228646(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a24577774b63e963942a867449aa4d0691cd3f3c5228a8c5f4c7ea7a7c95fb9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7e9b650227c1422a83bee496fcc42af00e9043a0062c63bae9fafa82be7b437(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7e171c39cc6dda4e8a85dc03bd63fa17bea5503955435e94df31e2cc16c9d3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adc19dc9bd0dd7ba5b20f6cc0d77cc1f8b1469d711a6991e1dac745c8df95bc3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7725d6a390c78403aadb20b05518e7842ad869c2b1e2e47099c72215d4daae5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67c8db8a8926b1cdde12a20d26cf8ad78ffb46c8a7cb43dec65dd94a4b820931(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0749482c6adbf1b01de082b5d15cbbc6218b386cf22bd832e6bd5789d302ad6e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5385e5e31dff3362e240cdfc7916a32749eaa2894b67d74a5fd0adb1fdc4b8c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c03ef9db17d3c26c142b7998863c2d95144ae8735e2e02c0bf6d9e37b2ec5d6d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f6b6ef7718e78739e72a01c207465d7b0bb10a1b6ad7e76d90653f66d3d6f56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__345e69737159184fb13dd974268ddbcad61126422e41ae6bc32a5a226201929d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__237cbf54b853e2f48549b11dd05026367716c1e6909b86a82fc244d45bd559c3(
    *,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60f36b07f83c571eb172ae981cfe1eb53eef37e8cd4a06fd66999b87ec6d1098(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53231eae5a767d1de3ff5c41f663e49702b443d0b3415e3dac7f6bc8940a6519(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b76a6a112ff86fe4964a5a54626dedd906a7967e9ec076de281d3c155fdaec0e(
    value: typing.Optional[DataDatabricksSqlWarehouseChannel],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__334d6fff894ce4a90d5bd53054792068ad1414ae5e8500f56e41377a2053283b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: builtins.str,
    auto_stop_mins: typing.Optional[jsii.Number] = None,
    channel: typing.Optional[typing.Union[DataDatabricksSqlWarehouseChannel, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_size: typing.Optional[builtins.str] = None,
    data_source_id: typing.Optional[builtins.str] = None,
    enable_photon: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_serverless_compute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    instance_profile_arn: typing.Optional[builtins.str] = None,
    jdbc_url: typing.Optional[builtins.str] = None,
    max_num_clusters: typing.Optional[jsii.Number] = None,
    min_num_clusters: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    num_clusters: typing.Optional[jsii.Number] = None,
    odbc_params: typing.Optional[typing.Union[DataDatabricksSqlWarehouseOdbcParams, typing.Dict[builtins.str, typing.Any]]] = None,
    spot_instance_policy: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Union[DataDatabricksSqlWarehouseTags, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fba4640feb1646afb5a2d559ef9c8d7bd49a281607064127769e2ca4aa19b07(
    *,
    path: builtins.str,
    port: jsii.Number,
    protocol: builtins.str,
    host: typing.Optional[builtins.str] = None,
    hostname: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f4ce13116e8fb0560a99c28374717acf70b70af83eb0c939bdeb7f1d54fc026(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e4e638a2f3435b586f3daf168e68f4d5f74154a66adddc3efde2ed923dfb1b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84285b497c3c3d2d23ee043534028b8a999b1d534b8b5ad341c009f8a205f32f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47d104f43a0c9955ad87f70fb059fc02a08424579335ee4a2cbbb2117447c24c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb27602db8847e79e05600abea25212e8bcc410db5bd553d943b63b74f44219b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79c53aba1947ed3f59d829abb707fc5a90839b958ed645ff6ef2f73e8506188c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2423c59e1081bf18f84c0bfddf9a08a3afa4b9086090e11d847794a20869ef58(
    value: typing.Optional[DataDatabricksSqlWarehouseOdbcParams],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43ebcef35775128b31ee6b1b0018ea7408daea1a373ba8d8bcd18b2224bf35cc(
    *,
    custom_tags: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksSqlWarehouseTagsCustomTags, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__005ec4813de0a9d8fd274a5e76586566c010a0439a946b594c978aa72bdf552b(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__105d8ecbe70a42869361f065f86826158f2797bb6214da92f80ec6f0108b4bb3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e4ab22913f7a52d551862ba9a2885148882cb479fcab512cb8fd9db4d8d5a65(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f33cd8ca34d638543f60722f02ce2c324c8789e2fa0cfba7bb56f49cb997177(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be7b74ea805d50e3807e88dd55b096ea97566609c17ede6d0fecd73c491ff294(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91dd3571d63126fe8e5b96b2bb789a879ec87ecab219814fcb5e30ca2037b9ea(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e74b455d2a3c842d1ee7f4e64f08fc5f3bea31c7511a3c4af1c2658f9d118abd(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksSqlWarehouseTagsCustomTags]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f55862801974452d3199ccec7a74f2f6630df0d26b37f21df97db9a4794491a9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8801a02cc0e710c3df34f6beee0baa96476c5f53d505379fb1561d7fc756d9af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b523719db7f747534ebf24aef8b2f8cebabeae6a563ad58366f4f29f5b2f093(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f7868924900b5e6f3eedacebcd13553411c6dc1ed358d9c909fa2c34dd0db6d(
    value: typing.Optional[typing.Union[DataDatabricksSqlWarehouseTagsCustomTags, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d0a2eca6b9b46dcc503c291b305920b635c716ab72cab6f133ff7876feba11c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05714b74cb0c9795e46239eb2dd00db827b43328e064e82ff52a1b4150a72182(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksSqlWarehouseTagsCustomTags, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f78c1162666a4589e7a55cd6edef4d122f3ad8fe1ac861bcfbf5eaa673fcee1(
    value: typing.Optional[DataDatabricksSqlWarehouseTags],
) -> None:
    """Type checking stubs"""
    pass
