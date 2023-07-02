'''
# `databricks_sql_endpoint`

Refer to the Terraform Registory for docs: [`databricks_sql_endpoint`](https://www.terraform.io/docs/providers/databricks/r/sql_endpoint).
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


class SqlEndpoint(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlEndpoint.SqlEndpoint",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint databricks_sql_endpoint}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        cluster_size: builtins.str,
        name: builtins.str,
        auto_stop_mins: typing.Optional[jsii.Number] = None,
        channel: typing.Optional[typing.Union["SqlEndpointChannel", typing.Dict[builtins.str, typing.Any]]] = None,
        data_source_id: typing.Optional[builtins.str] = None,
        enable_photon: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_serverless_compute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        instance_profile_arn: typing.Optional[builtins.str] = None,
        jdbc_url: typing.Optional[builtins.str] = None,
        max_num_clusters: typing.Optional[jsii.Number] = None,
        min_num_clusters: typing.Optional[jsii.Number] = None,
        num_clusters: typing.Optional[jsii.Number] = None,
        odbc_params: typing.Optional[typing.Union["SqlEndpointOdbcParams", typing.Dict[builtins.str, typing.Any]]] = None,
        spot_instance_policy: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union["SqlEndpointTags", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["SqlEndpointTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        warehouse_type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint databricks_sql_endpoint} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#cluster_size SqlEndpoint#cluster_size}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#name SqlEndpoint#name}.
        :param auto_stop_mins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#auto_stop_mins SqlEndpoint#auto_stop_mins}.
        :param channel: channel block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#channel SqlEndpoint#channel}
        :param data_source_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#data_source_id SqlEndpoint#data_source_id}.
        :param enable_photon: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#enable_photon SqlEndpoint#enable_photon}.
        :param enable_serverless_compute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#enable_serverless_compute SqlEndpoint#enable_serverless_compute}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#id SqlEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#instance_profile_arn SqlEndpoint#instance_profile_arn}.
        :param jdbc_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#jdbc_url SqlEndpoint#jdbc_url}.
        :param max_num_clusters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#max_num_clusters SqlEndpoint#max_num_clusters}.
        :param min_num_clusters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#min_num_clusters SqlEndpoint#min_num_clusters}.
        :param num_clusters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#num_clusters SqlEndpoint#num_clusters}.
        :param odbc_params: odbc_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#odbc_params SqlEndpoint#odbc_params}
        :param spot_instance_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#spot_instance_policy SqlEndpoint#spot_instance_policy}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#state SqlEndpoint#state}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#tags SqlEndpoint#tags}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#timeouts SqlEndpoint#timeouts}
        :param warehouse_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#warehouse_type SqlEndpoint#warehouse_type}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7caa7af00225c33b8491b18acbe8a26970c3204571ebb8db4cceccff1ea05f2d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SqlEndpointConfig(
            cluster_size=cluster_size,
            name=name,
            auto_stop_mins=auto_stop_mins,
            channel=channel,
            data_source_id=data_source_id,
            enable_photon=enable_photon,
            enable_serverless_compute=enable_serverless_compute,
            id=id,
            instance_profile_arn=instance_profile_arn,
            jdbc_url=jdbc_url,
            max_num_clusters=max_num_clusters,
            min_num_clusters=min_num_clusters,
            num_clusters=num_clusters,
            odbc_params=odbc_params,
            spot_instance_policy=spot_instance_policy,
            state=state,
            tags=tags,
            timeouts=timeouts,
            warehouse_type=warehouse_type,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#name SqlEndpoint#name}.
        '''
        value = SqlEndpointChannel(name=name)

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
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#path SqlEndpoint#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#port SqlEndpoint#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#protocol SqlEndpoint#protocol}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#host SqlEndpoint#host}.
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#hostname SqlEndpoint#hostname}.
        '''
        value = SqlEndpointOdbcParams(
            path=path, port=port, protocol=protocol, host=host, hostname=hostname
        )

        return typing.cast(None, jsii.invoke(self, "putOdbcParams", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        *,
        custom_tags: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SqlEndpointTagsCustomTags", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param custom_tags: custom_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#custom_tags SqlEndpoint#custom_tags}
        '''
        value = SqlEndpointTags(custom_tags=custom_tags)

        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#create SqlEndpoint#create}.
        '''
        value = SqlEndpointTimeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAutoStopMins")
    def reset_auto_stop_mins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoStopMins", []))

    @jsii.member(jsii_name="resetChannel")
    def reset_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChannel", []))

    @jsii.member(jsii_name="resetDataSourceId")
    def reset_data_source_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataSourceId", []))

    @jsii.member(jsii_name="resetEnablePhoton")
    def reset_enable_photon(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablePhoton", []))

    @jsii.member(jsii_name="resetEnableServerlessCompute")
    def reset_enable_serverless_compute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableServerlessCompute", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWarehouseType")
    def reset_warehouse_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarehouseType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="channel")
    def channel(self) -> "SqlEndpointChannelOutputReference":
        return typing.cast("SqlEndpointChannelOutputReference", jsii.get(self, "channel"))

    @builtins.property
    @jsii.member(jsii_name="odbcParams")
    def odbc_params(self) -> "SqlEndpointOdbcParamsOutputReference":
        return typing.cast("SqlEndpointOdbcParamsOutputReference", jsii.get(self, "odbcParams"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "SqlEndpointTagsOutputReference":
        return typing.cast("SqlEndpointTagsOutputReference", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SqlEndpointTimeoutsOutputReference":
        return typing.cast("SqlEndpointTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="autoStopMinsInput")
    def auto_stop_mins_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autoStopMinsInput"))

    @builtins.property
    @jsii.member(jsii_name="channelInput")
    def channel_input(self) -> typing.Optional["SqlEndpointChannel"]:
        return typing.cast(typing.Optional["SqlEndpointChannel"], jsii.get(self, "channelInput"))

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
    def odbc_params_input(self) -> typing.Optional["SqlEndpointOdbcParams"]:
        return typing.cast(typing.Optional["SqlEndpointOdbcParams"], jsii.get(self, "odbcParamsInput"))

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
    def tags_input(self) -> typing.Optional["SqlEndpointTags"]:
        return typing.cast(typing.Optional["SqlEndpointTags"], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SqlEndpointTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SqlEndpointTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="warehouseTypeInput")
    def warehouse_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warehouseTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="autoStopMins")
    def auto_stop_mins(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autoStopMins"))

    @auto_stop_mins.setter
    def auto_stop_mins(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac0db9f33d19f39b30147c43cc37a1b1b575dde31629b7d904aab29311086ccf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoStopMins", value)

    @builtins.property
    @jsii.member(jsii_name="clusterSize")
    def cluster_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterSize"))

    @cluster_size.setter
    def cluster_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d5adbf3097313f031f4da348213d117dcbfd61f7e42841dbb8b2eb9f1a8703b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterSize", value)

    @builtins.property
    @jsii.member(jsii_name="dataSourceId")
    def data_source_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSourceId"))

    @data_source_id.setter
    def data_source_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3e990b67af063dae9af85181405b0a3f1ab64a07179793f880fe0a7799b7245)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b6585bc05b1bd264e3aec2e1feeeda785fe28571596c46fb66d029c0b2efd67b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f9a8690ba9ff3bced2c56867bc9732782223dec4d92ae40d7b70adba29c15a40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableServerlessCompute", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b968df8692cbdf0bbdb8f1831625982480c051093b92b0336114962758efdbdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfileArn")
    def instance_profile_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceProfileArn"))

    @instance_profile_arn.setter
    def instance_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f43e62b801eb93f60d3dd887393061c837e8e30bfc82af9547180fddfaf914f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="jdbcUrl")
    def jdbc_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jdbcUrl"))

    @jdbc_url.setter
    def jdbc_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__239367666d0b3d4d2adc2cf33af6dfbda42e5667a47cc9102c00cc9125f2a21f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jdbcUrl", value)

    @builtins.property
    @jsii.member(jsii_name="maxNumClusters")
    def max_num_clusters(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxNumClusters"))

    @max_num_clusters.setter
    def max_num_clusters(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c80a52f37436cc14cb5d76d5e1016d9f1f418a3500cfbcdd05b51927be938725)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxNumClusters", value)

    @builtins.property
    @jsii.member(jsii_name="minNumClusters")
    def min_num_clusters(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minNumClusters"))

    @min_num_clusters.setter
    def min_num_clusters(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9a2723ad717ee160ca9a402213ba10e51c2e5e784647da646a9c382178383da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minNumClusters", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01a0ad6f02f1be789d6e088c739d9f529640e5a5de65581fd69448c3ba8adaf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="numClusters")
    def num_clusters(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numClusters"))

    @num_clusters.setter
    def num_clusters(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03a5067d6b104c10830884d99cf516aea9157974dc32bb02cc2c9f3e9102823b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numClusters", value)

    @builtins.property
    @jsii.member(jsii_name="spotInstancePolicy")
    def spot_instance_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotInstancePolicy"))

    @spot_instance_policy.setter
    def spot_instance_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2de65f4ebcc362d5441ed0a75d6eebc6060f2128632666febc477d97fe1e785c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotInstancePolicy", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20f1f01ffc0b9d3f1b09052d3d24363f53818ae06c7d99a73d6dc366c5929974)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="warehouseType")
    def warehouse_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warehouseType"))

    @warehouse_type.setter
    def warehouse_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__723ff36197ed30322764f1f161d992d8a7a3033d7892971053ae75f584887236)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warehouseType", value)


@jsii.data_type(
    jsii_type="databricks.sqlEndpoint.SqlEndpointChannel",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class SqlEndpointChannel:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#name SqlEndpoint#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42062820b789425efa86ab1e93d73b585cb1f462b279dbdb0d51b55b6d24ce2b)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#name SqlEndpoint#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlEndpointChannel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlEndpointChannelOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlEndpoint.SqlEndpointChannelOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d41145b0e7dc64c885d7b77125e27edfda1f00dbbd1cd955d553f933bb1e40c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2434e511f239555acc3e30047b2e10bab8f40ed266f3be7bb8135eb8d1607926)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlEndpointChannel]:
        return typing.cast(typing.Optional[SqlEndpointChannel], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlEndpointChannel]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d79983f1b929cf13221c545d0503ae8702f7491e864e7b8da9af39dfab709a87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlEndpoint.SqlEndpointConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster_size": "clusterSize",
        "name": "name",
        "auto_stop_mins": "autoStopMins",
        "channel": "channel",
        "data_source_id": "dataSourceId",
        "enable_photon": "enablePhoton",
        "enable_serverless_compute": "enableServerlessCompute",
        "id": "id",
        "instance_profile_arn": "instanceProfileArn",
        "jdbc_url": "jdbcUrl",
        "max_num_clusters": "maxNumClusters",
        "min_num_clusters": "minNumClusters",
        "num_clusters": "numClusters",
        "odbc_params": "odbcParams",
        "spot_instance_policy": "spotInstancePolicy",
        "state": "state",
        "tags": "tags",
        "timeouts": "timeouts",
        "warehouse_type": "warehouseType",
    },
)
class SqlEndpointConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        cluster_size: builtins.str,
        name: builtins.str,
        auto_stop_mins: typing.Optional[jsii.Number] = None,
        channel: typing.Optional[typing.Union[SqlEndpointChannel, typing.Dict[builtins.str, typing.Any]]] = None,
        data_source_id: typing.Optional[builtins.str] = None,
        enable_photon: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_serverless_compute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        instance_profile_arn: typing.Optional[builtins.str] = None,
        jdbc_url: typing.Optional[builtins.str] = None,
        max_num_clusters: typing.Optional[jsii.Number] = None,
        min_num_clusters: typing.Optional[jsii.Number] = None,
        num_clusters: typing.Optional[jsii.Number] = None,
        odbc_params: typing.Optional[typing.Union["SqlEndpointOdbcParams", typing.Dict[builtins.str, typing.Any]]] = None,
        spot_instance_policy: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union["SqlEndpointTags", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["SqlEndpointTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        warehouse_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cluster_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#cluster_size SqlEndpoint#cluster_size}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#name SqlEndpoint#name}.
        :param auto_stop_mins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#auto_stop_mins SqlEndpoint#auto_stop_mins}.
        :param channel: channel block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#channel SqlEndpoint#channel}
        :param data_source_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#data_source_id SqlEndpoint#data_source_id}.
        :param enable_photon: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#enable_photon SqlEndpoint#enable_photon}.
        :param enable_serverless_compute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#enable_serverless_compute SqlEndpoint#enable_serverless_compute}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#id SqlEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#instance_profile_arn SqlEndpoint#instance_profile_arn}.
        :param jdbc_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#jdbc_url SqlEndpoint#jdbc_url}.
        :param max_num_clusters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#max_num_clusters SqlEndpoint#max_num_clusters}.
        :param min_num_clusters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#min_num_clusters SqlEndpoint#min_num_clusters}.
        :param num_clusters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#num_clusters SqlEndpoint#num_clusters}.
        :param odbc_params: odbc_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#odbc_params SqlEndpoint#odbc_params}
        :param spot_instance_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#spot_instance_policy SqlEndpoint#spot_instance_policy}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#state SqlEndpoint#state}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#tags SqlEndpoint#tags}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#timeouts SqlEndpoint#timeouts}
        :param warehouse_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#warehouse_type SqlEndpoint#warehouse_type}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(channel, dict):
            channel = SqlEndpointChannel(**channel)
        if isinstance(odbc_params, dict):
            odbc_params = SqlEndpointOdbcParams(**odbc_params)
        if isinstance(tags, dict):
            tags = SqlEndpointTags(**tags)
        if isinstance(timeouts, dict):
            timeouts = SqlEndpointTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0220363e72f7045b9da9ebabfdb585469fe248a3333069d27171f604f2ad33b0)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster_size", value=cluster_size, expected_type=type_hints["cluster_size"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument auto_stop_mins", value=auto_stop_mins, expected_type=type_hints["auto_stop_mins"])
            check_type(argname="argument channel", value=channel, expected_type=type_hints["channel"])
            check_type(argname="argument data_source_id", value=data_source_id, expected_type=type_hints["data_source_id"])
            check_type(argname="argument enable_photon", value=enable_photon, expected_type=type_hints["enable_photon"])
            check_type(argname="argument enable_serverless_compute", value=enable_serverless_compute, expected_type=type_hints["enable_serverless_compute"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_profile_arn", value=instance_profile_arn, expected_type=type_hints["instance_profile_arn"])
            check_type(argname="argument jdbc_url", value=jdbc_url, expected_type=type_hints["jdbc_url"])
            check_type(argname="argument max_num_clusters", value=max_num_clusters, expected_type=type_hints["max_num_clusters"])
            check_type(argname="argument min_num_clusters", value=min_num_clusters, expected_type=type_hints["min_num_clusters"])
            check_type(argname="argument num_clusters", value=num_clusters, expected_type=type_hints["num_clusters"])
            check_type(argname="argument odbc_params", value=odbc_params, expected_type=type_hints["odbc_params"])
            check_type(argname="argument spot_instance_policy", value=spot_instance_policy, expected_type=type_hints["spot_instance_policy"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument warehouse_type", value=warehouse_type, expected_type=type_hints["warehouse_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_size": cluster_size,
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
        if auto_stop_mins is not None:
            self._values["auto_stop_mins"] = auto_stop_mins
        if channel is not None:
            self._values["channel"] = channel
        if data_source_id is not None:
            self._values["data_source_id"] = data_source_id
        if enable_photon is not None:
            self._values["enable_photon"] = enable_photon
        if enable_serverless_compute is not None:
            self._values["enable_serverless_compute"] = enable_serverless_compute
        if id is not None:
            self._values["id"] = id
        if instance_profile_arn is not None:
            self._values["instance_profile_arn"] = instance_profile_arn
        if jdbc_url is not None:
            self._values["jdbc_url"] = jdbc_url
        if max_num_clusters is not None:
            self._values["max_num_clusters"] = max_num_clusters
        if min_num_clusters is not None:
            self._values["min_num_clusters"] = min_num_clusters
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
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if warehouse_type is not None:
            self._values["warehouse_type"] = warehouse_type

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
    def cluster_size(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#cluster_size SqlEndpoint#cluster_size}.'''
        result = self._values.get("cluster_size")
        assert result is not None, "Required property 'cluster_size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#name SqlEndpoint#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_stop_mins(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#auto_stop_mins SqlEndpoint#auto_stop_mins}.'''
        result = self._values.get("auto_stop_mins")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def channel(self) -> typing.Optional[SqlEndpointChannel]:
        '''channel block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#channel SqlEndpoint#channel}
        '''
        result = self._values.get("channel")
        return typing.cast(typing.Optional[SqlEndpointChannel], result)

    @builtins.property
    def data_source_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#data_source_id SqlEndpoint#data_source_id}.'''
        result = self._values.get("data_source_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_photon(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#enable_photon SqlEndpoint#enable_photon}.'''
        result = self._values.get("enable_photon")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_serverless_compute(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#enable_serverless_compute SqlEndpoint#enable_serverless_compute}.'''
        result = self._values.get("enable_serverless_compute")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#id SqlEndpoint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#instance_profile_arn SqlEndpoint#instance_profile_arn}.'''
        result = self._values.get("instance_profile_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jdbc_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#jdbc_url SqlEndpoint#jdbc_url}.'''
        result = self._values.get("jdbc_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_num_clusters(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#max_num_clusters SqlEndpoint#max_num_clusters}.'''
        result = self._values.get("max_num_clusters")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_num_clusters(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#min_num_clusters SqlEndpoint#min_num_clusters}.'''
        result = self._values.get("min_num_clusters")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def num_clusters(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#num_clusters SqlEndpoint#num_clusters}.'''
        result = self._values.get("num_clusters")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def odbc_params(self) -> typing.Optional["SqlEndpointOdbcParams"]:
        '''odbc_params block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#odbc_params SqlEndpoint#odbc_params}
        '''
        result = self._values.get("odbc_params")
        return typing.cast(typing.Optional["SqlEndpointOdbcParams"], result)

    @builtins.property
    def spot_instance_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#spot_instance_policy SqlEndpoint#spot_instance_policy}.'''
        result = self._values.get("spot_instance_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#state SqlEndpoint#state}.'''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional["SqlEndpointTags"]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#tags SqlEndpoint#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional["SqlEndpointTags"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SqlEndpointTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#timeouts SqlEndpoint#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SqlEndpointTimeouts"], result)

    @builtins.property
    def warehouse_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#warehouse_type SqlEndpoint#warehouse_type}.'''
        result = self._values.get("warehouse_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlEndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.sqlEndpoint.SqlEndpointOdbcParams",
    jsii_struct_bases=[],
    name_mapping={
        "path": "path",
        "port": "port",
        "protocol": "protocol",
        "host": "host",
        "hostname": "hostname",
    },
)
class SqlEndpointOdbcParams:
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
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#path SqlEndpoint#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#port SqlEndpoint#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#protocol SqlEndpoint#protocol}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#host SqlEndpoint#host}.
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#hostname SqlEndpoint#hostname}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d6016a18725c873516b3aeec02897d9685883911e2285d05cd845374cf32e4c)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#path SqlEndpoint#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#port SqlEndpoint#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#protocol SqlEndpoint#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#host SqlEndpoint#host}.'''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#hostname SqlEndpoint#hostname}.'''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlEndpointOdbcParams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlEndpointOdbcParamsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlEndpoint.SqlEndpointOdbcParamsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d576c9d4b25f59c7cab64204d40b78ab73bcb3389aaa876e41e11ef498a34e18)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5c32deb727bec34165ea3cdb403ea5ea0f16a14efb9dcea36245bdfcaa07277)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66fc0baf2f0469acf7a820cc1c93ff966a82c3cc0bb434feddcb3ac18cd78f0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c805b201426bc6446808e80128390dcc2bfba7449f2381a764dc64100cc9282)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7587ccc72bd20248f40cc6c29110833a61a0f545f1e653ac4837ff044c131b84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d22dea4a51868cda8c0a4c292f948b0d92672f9a7fe518374233fb1793a6bafc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlEndpointOdbcParams]:
        return typing.cast(typing.Optional[SqlEndpointOdbcParams], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlEndpointOdbcParams]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c980635f67b0eef21549d05807a8e425cc55a476964693149ec45deab7b41097)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlEndpoint.SqlEndpointTags",
    jsii_struct_bases=[],
    name_mapping={"custom_tags": "customTags"},
)
class SqlEndpointTags:
    def __init__(
        self,
        *,
        custom_tags: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SqlEndpointTagsCustomTags", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param custom_tags: custom_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#custom_tags SqlEndpoint#custom_tags}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09220a40407cd695935f63bf48a215157f624f06d7b9aff0f0a4bb49447d2dcd)
            check_type(argname="argument custom_tags", value=custom_tags, expected_type=type_hints["custom_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "custom_tags": custom_tags,
        }

    @builtins.property
    def custom_tags(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SqlEndpointTagsCustomTags"]]:
        '''custom_tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#custom_tags SqlEndpoint#custom_tags}
        '''
        result = self._values.get("custom_tags")
        assert result is not None, "Required property 'custom_tags' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SqlEndpointTagsCustomTags"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlEndpointTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.sqlEndpoint.SqlEndpointTagsCustomTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class SqlEndpointTagsCustomTags:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#key SqlEndpoint#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#value SqlEndpoint#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e386f0da5fd60c4fe7af8f59d5ff0d6c758e2ba450d2d5593a82199f2e16c71)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#key SqlEndpoint#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#value SqlEndpoint#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlEndpointTagsCustomTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlEndpointTagsCustomTagsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlEndpoint.SqlEndpointTagsCustomTagsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__71ffb22cb701e5f2a595721efab4848425594e3edecacc33721b03c679d8b6d6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SqlEndpointTagsCustomTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ed37dc4b8bbdd765afb3288eee095de32f60ab8b17a5143b7fe46be4724a993)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SqlEndpointTagsCustomTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75887f276bb7a66b19e34dbed886ca4c81e8e6ee3109ef87f04334afb34bb2d8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__423948efcba7b294e930904a927559867fbeb0fe994ddf65f3faf09dd297bba0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac571ccec8392b1f667dafd9046a4da3444b3645a58da2ba902d8fd79ca76183)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlEndpointTagsCustomTags]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlEndpointTagsCustomTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlEndpointTagsCustomTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ec111c9e43204b6cce2622d1ebef6a24ebd99393ee16e22f5b8c57234cd0b2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SqlEndpointTagsCustomTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlEndpoint.SqlEndpointTagsCustomTagsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d52fa098ba2bc0717e5baf71861f5403a97c596f21bc6aa83ca2ca9ecb518fdb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e26c982b5e72863d77f8e07ff91a0612760e81460ab4299df2995e708a0cee6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78b1570e880fafb295438cb5c555787d192dbdb9940457b44a5912d2cf304d6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SqlEndpointTagsCustomTags, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SqlEndpointTagsCustomTags, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SqlEndpointTagsCustomTags, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__713c4579e9f092bfb541411331eb7d291644f4a410ec7a8053f299feb235861a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SqlEndpointTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlEndpoint.SqlEndpointTagsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc5441cae71a5cbbd3522d95c913ee70d48d70ce2ae642df6daf955109d62643)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomTags")
    def put_custom_tags(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SqlEndpointTagsCustomTags, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2466a784b6428a30a3a381d120945452970980ea641302ab507cb15e9df2d2b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomTags", [value]))

    @builtins.property
    @jsii.member(jsii_name="customTags")
    def custom_tags(self) -> SqlEndpointTagsCustomTagsList:
        return typing.cast(SqlEndpointTagsCustomTagsList, jsii.get(self, "customTags"))

    @builtins.property
    @jsii.member(jsii_name="customTagsInput")
    def custom_tags_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlEndpointTagsCustomTags]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlEndpointTagsCustomTags]]], jsii.get(self, "customTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlEndpointTags]:
        return typing.cast(typing.Optional[SqlEndpointTags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlEndpointTags]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07adc3ad6461ba46a7aef774365f71dcc321a86806e1b63559c2d3f1f83ea606)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlEndpoint.SqlEndpointTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class SqlEndpointTimeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#create SqlEndpoint#create}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89a5bb2055e828c87a65b4028435c505787e15a047a26dc62d739102db9a3eeb)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_endpoint#create SqlEndpoint#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlEndpointTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlEndpointTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlEndpoint.SqlEndpointTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b34d8e11a59f5f671014ae1a6d745303012760bc5d4bd235785b8f605f081b27)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__397bdfc1fca6bb6e76b4e5212cf00b7dc07b4d04acc68c61cd57f94c3e377834)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SqlEndpointTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SqlEndpointTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SqlEndpointTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfb79a043e61b54afb7e357a9d8e86f5564cf1f59489be0144c13db4ef4f8eab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SqlEndpoint",
    "SqlEndpointChannel",
    "SqlEndpointChannelOutputReference",
    "SqlEndpointConfig",
    "SqlEndpointOdbcParams",
    "SqlEndpointOdbcParamsOutputReference",
    "SqlEndpointTags",
    "SqlEndpointTagsCustomTags",
    "SqlEndpointTagsCustomTagsList",
    "SqlEndpointTagsCustomTagsOutputReference",
    "SqlEndpointTagsOutputReference",
    "SqlEndpointTimeouts",
    "SqlEndpointTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__7caa7af00225c33b8491b18acbe8a26970c3204571ebb8db4cceccff1ea05f2d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    cluster_size: builtins.str,
    name: builtins.str,
    auto_stop_mins: typing.Optional[jsii.Number] = None,
    channel: typing.Optional[typing.Union[SqlEndpointChannel, typing.Dict[builtins.str, typing.Any]]] = None,
    data_source_id: typing.Optional[builtins.str] = None,
    enable_photon: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_serverless_compute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    instance_profile_arn: typing.Optional[builtins.str] = None,
    jdbc_url: typing.Optional[builtins.str] = None,
    max_num_clusters: typing.Optional[jsii.Number] = None,
    min_num_clusters: typing.Optional[jsii.Number] = None,
    num_clusters: typing.Optional[jsii.Number] = None,
    odbc_params: typing.Optional[typing.Union[SqlEndpointOdbcParams, typing.Dict[builtins.str, typing.Any]]] = None,
    spot_instance_policy: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Union[SqlEndpointTags, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[SqlEndpointTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    warehouse_type: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__ac0db9f33d19f39b30147c43cc37a1b1b575dde31629b7d904aab29311086ccf(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d5adbf3097313f031f4da348213d117dcbfd61f7e42841dbb8b2eb9f1a8703b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3e990b67af063dae9af85181405b0a3f1ab64a07179793f880fe0a7799b7245(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6585bc05b1bd264e3aec2e1feeeda785fe28571596c46fb66d029c0b2efd67b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9a8690ba9ff3bced2c56867bc9732782223dec4d92ae40d7b70adba29c15a40(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b968df8692cbdf0bbdb8f1831625982480c051093b92b0336114962758efdbdf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f43e62b801eb93f60d3dd887393061c837e8e30bfc82af9547180fddfaf914f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__239367666d0b3d4d2adc2cf33af6dfbda42e5667a47cc9102c00cc9125f2a21f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c80a52f37436cc14cb5d76d5e1016d9f1f418a3500cfbcdd05b51927be938725(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9a2723ad717ee160ca9a402213ba10e51c2e5e784647da646a9c382178383da(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01a0ad6f02f1be789d6e088c739d9f529640e5a5de65581fd69448c3ba8adaf4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03a5067d6b104c10830884d99cf516aea9157974dc32bb02cc2c9f3e9102823b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2de65f4ebcc362d5441ed0a75d6eebc6060f2128632666febc477d97fe1e785c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20f1f01ffc0b9d3f1b09052d3d24363f53818ae06c7d99a73d6dc366c5929974(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__723ff36197ed30322764f1f161d992d8a7a3033d7892971053ae75f584887236(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42062820b789425efa86ab1e93d73b585cb1f462b279dbdb0d51b55b6d24ce2b(
    *,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d41145b0e7dc64c885d7b77125e27edfda1f00dbbd1cd955d553f933bb1e40c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2434e511f239555acc3e30047b2e10bab8f40ed266f3be7bb8135eb8d1607926(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d79983f1b929cf13221c545d0503ae8702f7491e864e7b8da9af39dfab709a87(
    value: typing.Optional[SqlEndpointChannel],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0220363e72f7045b9da9ebabfdb585469fe248a3333069d27171f604f2ad33b0(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cluster_size: builtins.str,
    name: builtins.str,
    auto_stop_mins: typing.Optional[jsii.Number] = None,
    channel: typing.Optional[typing.Union[SqlEndpointChannel, typing.Dict[builtins.str, typing.Any]]] = None,
    data_source_id: typing.Optional[builtins.str] = None,
    enable_photon: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_serverless_compute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    instance_profile_arn: typing.Optional[builtins.str] = None,
    jdbc_url: typing.Optional[builtins.str] = None,
    max_num_clusters: typing.Optional[jsii.Number] = None,
    min_num_clusters: typing.Optional[jsii.Number] = None,
    num_clusters: typing.Optional[jsii.Number] = None,
    odbc_params: typing.Optional[typing.Union[SqlEndpointOdbcParams, typing.Dict[builtins.str, typing.Any]]] = None,
    spot_instance_policy: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Union[SqlEndpointTags, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[SqlEndpointTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    warehouse_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d6016a18725c873516b3aeec02897d9685883911e2285d05cd845374cf32e4c(
    *,
    path: builtins.str,
    port: jsii.Number,
    protocol: builtins.str,
    host: typing.Optional[builtins.str] = None,
    hostname: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d576c9d4b25f59c7cab64204d40b78ab73bcb3389aaa876e41e11ef498a34e18(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5c32deb727bec34165ea3cdb403ea5ea0f16a14efb9dcea36245bdfcaa07277(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66fc0baf2f0469acf7a820cc1c93ff966a82c3cc0bb434feddcb3ac18cd78f0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c805b201426bc6446808e80128390dcc2bfba7449f2381a764dc64100cc9282(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7587ccc72bd20248f40cc6c29110833a61a0f545f1e653ac4837ff044c131b84(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d22dea4a51868cda8c0a4c292f948b0d92672f9a7fe518374233fb1793a6bafc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c980635f67b0eef21549d05807a8e425cc55a476964693149ec45deab7b41097(
    value: typing.Optional[SqlEndpointOdbcParams],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09220a40407cd695935f63bf48a215157f624f06d7b9aff0f0a4bb49447d2dcd(
    *,
    custom_tags: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SqlEndpointTagsCustomTags, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e386f0da5fd60c4fe7af8f59d5ff0d6c758e2ba450d2d5593a82199f2e16c71(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71ffb22cb701e5f2a595721efab4848425594e3edecacc33721b03c679d8b6d6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ed37dc4b8bbdd765afb3288eee095de32f60ab8b17a5143b7fe46be4724a993(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75887f276bb7a66b19e34dbed886ca4c81e8e6ee3109ef87f04334afb34bb2d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__423948efcba7b294e930904a927559867fbeb0fe994ddf65f3faf09dd297bba0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac571ccec8392b1f667dafd9046a4da3444b3645a58da2ba902d8fd79ca76183(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ec111c9e43204b6cce2622d1ebef6a24ebd99393ee16e22f5b8c57234cd0b2e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlEndpointTagsCustomTags]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d52fa098ba2bc0717e5baf71861f5403a97c596f21bc6aa83ca2ca9ecb518fdb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e26c982b5e72863d77f8e07ff91a0612760e81460ab4299df2995e708a0cee6d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78b1570e880fafb295438cb5c555787d192dbdb9940457b44a5912d2cf304d6e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__713c4579e9f092bfb541411331eb7d291644f4a410ec7a8053f299feb235861a(
    value: typing.Optional[typing.Union[SqlEndpointTagsCustomTags, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc5441cae71a5cbbd3522d95c913ee70d48d70ce2ae642df6daf955109d62643(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2466a784b6428a30a3a381d120945452970980ea641302ab507cb15e9df2d2b5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SqlEndpointTagsCustomTags, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07adc3ad6461ba46a7aef774365f71dcc321a86806e1b63559c2d3f1f83ea606(
    value: typing.Optional[SqlEndpointTags],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89a5bb2055e828c87a65b4028435c505787e15a047a26dc62d739102db9a3eeb(
    *,
    create: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b34d8e11a59f5f671014ae1a6d745303012760bc5d4bd235785b8f605f081b27(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__397bdfc1fca6bb6e76b4e5212cf00b7dc07b4d04acc68c61cd57f94c3e377834(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfb79a043e61b54afb7e357a9d8e86f5564cf1f59489be0144c13db4ef4f8eab(
    value: typing.Optional[typing.Union[SqlEndpointTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
