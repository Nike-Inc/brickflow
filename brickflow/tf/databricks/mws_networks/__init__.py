'''
# `databricks_mws_networks`

Refer to the Terraform Registory for docs: [`databricks_mws_networks`](https://www.terraform.io/docs/providers/databricks/r/mws_networks).
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


class MwsNetworks(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsNetworks.MwsNetworks",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks databricks_mws_networks}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        account_id: builtins.str,
        network_name: builtins.str,
        creation_time: typing.Optional[jsii.Number] = None,
        error_messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MwsNetworksErrorMessages", typing.Dict[builtins.str, typing.Any]]]]] = None,
        gcp_network_info: typing.Optional[typing.Union["MwsNetworksGcpNetworkInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        network_id: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc_endpoints: typing.Optional[typing.Union["MwsNetworksVpcEndpoints", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_id: typing.Optional[builtins.str] = None,
        vpc_status: typing.Optional[builtins.str] = None,
        workspace_id: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks databricks_mws_networks} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#account_id MwsNetworks#account_id}.
        :param network_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#network_name MwsNetworks#network_name}.
        :param creation_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#creation_time MwsNetworks#creation_time}.
        :param error_messages: error_messages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#error_messages MwsNetworks#error_messages}
        :param gcp_network_info: gcp_network_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#gcp_network_info MwsNetworks#gcp_network_info}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#id MwsNetworks#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#network_id MwsNetworks#network_id}.
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#security_group_ids MwsNetworks#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#subnet_ids MwsNetworks#subnet_ids}.
        :param vpc_endpoints: vpc_endpoints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_endpoints MwsNetworks#vpc_endpoints}
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_id MwsNetworks#vpc_id}.
        :param vpc_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_status MwsNetworks#vpc_status}.
        :param workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#workspace_id MwsNetworks#workspace_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7a4f31f87ce1e16a1f76cba4af70e85a10bc191b4b024ba42b4735dd5bbed07)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MwsNetworksConfig(
            account_id=account_id,
            network_name=network_name,
            creation_time=creation_time,
            error_messages=error_messages,
            gcp_network_info=gcp_network_info,
            id=id,
            network_id=network_id,
            security_group_ids=security_group_ids,
            subnet_ids=subnet_ids,
            vpc_endpoints=vpc_endpoints,
            vpc_id=vpc_id,
            vpc_status=vpc_status,
            workspace_id=workspace_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putErrorMessages")
    def put_error_messages(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MwsNetworksErrorMessages", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ebe8b4982e35bac7a5a00ffd465aae4fae947af5a92fa72029f8481e93c9b39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putErrorMessages", [value]))

    @jsii.member(jsii_name="putGcpNetworkInfo")
    def put_gcp_network_info(
        self,
        *,
        network_project_id: builtins.str,
        pod_ip_range_name: builtins.str,
        service_ip_range_name: builtins.str,
        subnet_id: builtins.str,
        subnet_region: builtins.str,
        vpc_id: builtins.str,
    ) -> None:
        '''
        :param network_project_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#network_project_id MwsNetworks#network_project_id}.
        :param pod_ip_range_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#pod_ip_range_name MwsNetworks#pod_ip_range_name}.
        :param service_ip_range_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#service_ip_range_name MwsNetworks#service_ip_range_name}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#subnet_id MwsNetworks#subnet_id}.
        :param subnet_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#subnet_region MwsNetworks#subnet_region}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_id MwsNetworks#vpc_id}.
        '''
        value = MwsNetworksGcpNetworkInfo(
            network_project_id=network_project_id,
            pod_ip_range_name=pod_ip_range_name,
            service_ip_range_name=service_ip_range_name,
            subnet_id=subnet_id,
            subnet_region=subnet_region,
            vpc_id=vpc_id,
        )

        return typing.cast(None, jsii.invoke(self, "putGcpNetworkInfo", [value]))

    @jsii.member(jsii_name="putVpcEndpoints")
    def put_vpc_endpoints(
        self,
        *,
        dataplane_relay: typing.Sequence[builtins.str],
        rest_api: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param dataplane_relay: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#dataplane_relay MwsNetworks#dataplane_relay}.
        :param rest_api: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#rest_api MwsNetworks#rest_api}.
        '''
        value = MwsNetworksVpcEndpoints(
            dataplane_relay=dataplane_relay, rest_api=rest_api
        )

        return typing.cast(None, jsii.invoke(self, "putVpcEndpoints", [value]))

    @jsii.member(jsii_name="resetCreationTime")
    def reset_creation_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreationTime", []))

    @jsii.member(jsii_name="resetErrorMessages")
    def reset_error_messages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorMessages", []))

    @jsii.member(jsii_name="resetGcpNetworkInfo")
    def reset_gcp_network_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpNetworkInfo", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNetworkId")
    def reset_network_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkId", []))

    @jsii.member(jsii_name="resetSecurityGroupIds")
    def reset_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroupIds", []))

    @jsii.member(jsii_name="resetSubnetIds")
    def reset_subnet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetIds", []))

    @jsii.member(jsii_name="resetVpcEndpoints")
    def reset_vpc_endpoints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcEndpoints", []))

    @jsii.member(jsii_name="resetVpcId")
    def reset_vpc_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcId", []))

    @jsii.member(jsii_name="resetVpcStatus")
    def reset_vpc_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcStatus", []))

    @jsii.member(jsii_name="resetWorkspaceId")
    def reset_workspace_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="errorMessages")
    def error_messages(self) -> "MwsNetworksErrorMessagesList":
        return typing.cast("MwsNetworksErrorMessagesList", jsii.get(self, "errorMessages"))

    @builtins.property
    @jsii.member(jsii_name="gcpNetworkInfo")
    def gcp_network_info(self) -> "MwsNetworksGcpNetworkInfoOutputReference":
        return typing.cast("MwsNetworksGcpNetworkInfoOutputReference", jsii.get(self, "gcpNetworkInfo"))

    @builtins.property
    @jsii.member(jsii_name="vpcEndpoints")
    def vpc_endpoints(self) -> "MwsNetworksVpcEndpointsOutputReference":
        return typing.cast("MwsNetworksVpcEndpointsOutputReference", jsii.get(self, "vpcEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="creationTimeInput")
    def creation_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "creationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="errorMessagesInput")
    def error_messages_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MwsNetworksErrorMessages"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MwsNetworksErrorMessages"]]], jsii.get(self, "errorMessagesInput"))

    @builtins.property
    @jsii.member(jsii_name="gcpNetworkInfoInput")
    def gcp_network_info_input(self) -> typing.Optional["MwsNetworksGcpNetworkInfo"]:
        return typing.cast(typing.Optional["MwsNetworksGcpNetworkInfo"], jsii.get(self, "gcpNetworkInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="networkIdInput")
    def network_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkIdInput"))

    @builtins.property
    @jsii.member(jsii_name="networkNameInput")
    def network_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkNameInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointsInput")
    def vpc_endpoints_input(self) -> typing.Optional["MwsNetworksVpcEndpoints"]:
        return typing.cast(typing.Optional["MwsNetworksVpcEndpoints"], jsii.get(self, "vpcEndpointsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcIdInput")
    def vpc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcStatusInput")
    def vpc_status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceIdInput")
    def workspace_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "workspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50c5289721b52dc88fa07eaa73326f74e52b792f8a532c3b7e0867ec87f8ba31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="creationTime")
    def creation_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "creationTime"))

    @creation_time.setter
    def creation_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42cbaedce6677f479da52942b0d9bdb60abafa3421aad41871d7ccc7e33af464)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creationTime", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8805acfda2d0c5d80d590a05dc2228325efb41eccd277378c7b83e940f37bc53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="networkId")
    def network_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkId"))

    @network_id.setter
    def network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7644ac076904a5d4f90123c98bbe4e30b1747c2d9fde358191f035aac98a7962)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkId", value)

    @builtins.property
    @jsii.member(jsii_name="networkName")
    def network_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkName"))

    @network_name.setter
    def network_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdd1ea1aebc8503c0f62e4fc7976fd6139a1acff3c72ad3416a9f27e8ce457d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkName", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84aaea7acc75e19805daed27902c47b69d748f21a9bf797628fae58218d746cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e119ad1ab20ca8c50c5e80dfa1a946c7394471030c87025dba9c1fa01431b17a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1569a15df5b5a1df6f754aa3fffa25af5daf29359b1cd08e638900a1c117495c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @builtins.property
    @jsii.member(jsii_name="vpcStatus")
    def vpc_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcStatus"))

    @vpc_status.setter
    def vpc_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f05a88f19f35e9d70b57d66e357f90fa8e7ec3c46c2f67a055a148c1a47fbae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcStatus", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceId")
    def workspace_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "workspaceId"))

    @workspace_id.setter
    def workspace_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__386e2928c95a2bd85ee81b36fb3d493178512f84953b8b21cfa10948e012293d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceId", value)


@jsii.data_type(
    jsii_type="databricks.mwsNetworks.MwsNetworksConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_id": "accountId",
        "network_name": "networkName",
        "creation_time": "creationTime",
        "error_messages": "errorMessages",
        "gcp_network_info": "gcpNetworkInfo",
        "id": "id",
        "network_id": "networkId",
        "security_group_ids": "securityGroupIds",
        "subnet_ids": "subnetIds",
        "vpc_endpoints": "vpcEndpoints",
        "vpc_id": "vpcId",
        "vpc_status": "vpcStatus",
        "workspace_id": "workspaceId",
    },
)
class MwsNetworksConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        account_id: builtins.str,
        network_name: builtins.str,
        creation_time: typing.Optional[jsii.Number] = None,
        error_messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MwsNetworksErrorMessages", typing.Dict[builtins.str, typing.Any]]]]] = None,
        gcp_network_info: typing.Optional[typing.Union["MwsNetworksGcpNetworkInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        network_id: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc_endpoints: typing.Optional[typing.Union["MwsNetworksVpcEndpoints", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_id: typing.Optional[builtins.str] = None,
        vpc_status: typing.Optional[builtins.str] = None,
        workspace_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#account_id MwsNetworks#account_id}.
        :param network_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#network_name MwsNetworks#network_name}.
        :param creation_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#creation_time MwsNetworks#creation_time}.
        :param error_messages: error_messages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#error_messages MwsNetworks#error_messages}
        :param gcp_network_info: gcp_network_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#gcp_network_info MwsNetworks#gcp_network_info}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#id MwsNetworks#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#network_id MwsNetworks#network_id}.
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#security_group_ids MwsNetworks#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#subnet_ids MwsNetworks#subnet_ids}.
        :param vpc_endpoints: vpc_endpoints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_endpoints MwsNetworks#vpc_endpoints}
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_id MwsNetworks#vpc_id}.
        :param vpc_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_status MwsNetworks#vpc_status}.
        :param workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#workspace_id MwsNetworks#workspace_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(gcp_network_info, dict):
            gcp_network_info = MwsNetworksGcpNetworkInfo(**gcp_network_info)
        if isinstance(vpc_endpoints, dict):
            vpc_endpoints = MwsNetworksVpcEndpoints(**vpc_endpoints)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__414b8cae24f4c7d9fd6f98fea18650d1647ee00ff9f4feed0e2f9af69a088436)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument network_name", value=network_name, expected_type=type_hints["network_name"])
            check_type(argname="argument creation_time", value=creation_time, expected_type=type_hints["creation_time"])
            check_type(argname="argument error_messages", value=error_messages, expected_type=type_hints["error_messages"])
            check_type(argname="argument gcp_network_info", value=gcp_network_info, expected_type=type_hints["gcp_network_info"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument network_id", value=network_id, expected_type=type_hints["network_id"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument vpc_endpoints", value=vpc_endpoints, expected_type=type_hints["vpc_endpoints"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument vpc_status", value=vpc_status, expected_type=type_hints["vpc_status"])
            check_type(argname="argument workspace_id", value=workspace_id, expected_type=type_hints["workspace_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
            "network_name": network_name,
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
        if creation_time is not None:
            self._values["creation_time"] = creation_time
        if error_messages is not None:
            self._values["error_messages"] = error_messages
        if gcp_network_info is not None:
            self._values["gcp_network_info"] = gcp_network_info
        if id is not None:
            self._values["id"] = id
        if network_id is not None:
            self._values["network_id"] = network_id
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
        if vpc_endpoints is not None:
            self._values["vpc_endpoints"] = vpc_endpoints
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id
        if vpc_status is not None:
            self._values["vpc_status"] = vpc_status
        if workspace_id is not None:
            self._values["workspace_id"] = workspace_id

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
    def account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#account_id MwsNetworks#account_id}.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#network_name MwsNetworks#network_name}.'''
        result = self._values.get("network_name")
        assert result is not None, "Required property 'network_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def creation_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#creation_time MwsNetworks#creation_time}.'''
        result = self._values.get("creation_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def error_messages(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MwsNetworksErrorMessages"]]]:
        '''error_messages block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#error_messages MwsNetworks#error_messages}
        '''
        result = self._values.get("error_messages")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MwsNetworksErrorMessages"]]], result)

    @builtins.property
    def gcp_network_info(self) -> typing.Optional["MwsNetworksGcpNetworkInfo"]:
        '''gcp_network_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#gcp_network_info MwsNetworks#gcp_network_info}
        '''
        result = self._values.get("gcp_network_info")
        return typing.cast(typing.Optional["MwsNetworksGcpNetworkInfo"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#id MwsNetworks#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#network_id MwsNetworks#network_id}.'''
        result = self._values.get("network_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#security_group_ids MwsNetworks#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#subnet_ids MwsNetworks#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def vpc_endpoints(self) -> typing.Optional["MwsNetworksVpcEndpoints"]:
        '''vpc_endpoints block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_endpoints MwsNetworks#vpc_endpoints}
        '''
        result = self._values.get("vpc_endpoints")
        return typing.cast(typing.Optional["MwsNetworksVpcEndpoints"], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_id MwsNetworks#vpc_id}.'''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_status MwsNetworks#vpc_status}.'''
        result = self._values.get("vpc_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workspace_id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#workspace_id MwsNetworks#workspace_id}.'''
        result = self._values.get("workspace_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsNetworksConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.mwsNetworks.MwsNetworksErrorMessages",
    jsii_struct_bases=[],
    name_mapping={"error_message": "errorMessage", "error_type": "errorType"},
)
class MwsNetworksErrorMessages:
    def __init__(
        self,
        *,
        error_message: typing.Optional[builtins.str] = None,
        error_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param error_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#error_message MwsNetworks#error_message}.
        :param error_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#error_type MwsNetworks#error_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc51e84f2879a9e1fd90666f8bc04c19c62a149c150887c5503ca9d43463f558)
            check_type(argname="argument error_message", value=error_message, expected_type=type_hints["error_message"])
            check_type(argname="argument error_type", value=error_type, expected_type=type_hints["error_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if error_message is not None:
            self._values["error_message"] = error_message
        if error_type is not None:
            self._values["error_type"] = error_type

    @builtins.property
    def error_message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#error_message MwsNetworks#error_message}.'''
        result = self._values.get("error_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#error_type MwsNetworks#error_type}.'''
        result = self._values.get("error_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsNetworksErrorMessages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsNetworksErrorMessagesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsNetworks.MwsNetworksErrorMessagesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d1631c4927d33791d517b0bc8e8aad3aa9022342c4a01221d2c6c02a23a0aee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MwsNetworksErrorMessagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1beae8e4cb8354cb06b176534b6d69fda44dd939fef0ddd66186fdcc73faea51)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MwsNetworksErrorMessagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ed2f83cca0c420cda938a9a851709777b07b31bad030c6c439cfaffbe31a622)
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
            type_hints = typing.get_type_hints(_typecheckingstub__15697f853800feb908008daca6cd87125b63588895f4325c1e1fa4aee0758ffc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__97082dd4a79971d4a30204efbdb6aff923d7e0f199409c3ad30f21e84f4b1e05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MwsNetworksErrorMessages]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MwsNetworksErrorMessages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MwsNetworksErrorMessages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cfd6a231bb0546183fafeeab793975b4040e96d5abf4b70e8f07110c1681122)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MwsNetworksErrorMessagesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsNetworks.MwsNetworksErrorMessagesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__502501c4da082083169ff51d1560138f638f51ea624aaaabe1016b522b02cd6f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetErrorMessage")
    def reset_error_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorMessage", []))

    @jsii.member(jsii_name="resetErrorType")
    def reset_error_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorType", []))

    @builtins.property
    @jsii.member(jsii_name="errorMessageInput")
    def error_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="errorTypeInput")
    def error_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="errorMessage")
    def error_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorMessage"))

    @error_message.setter
    def error_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfb17d632c660911374a904a666e73b7c1c4a915ea8dbf0445acf53ab0375c64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorMessage", value)

    @builtins.property
    @jsii.member(jsii_name="errorType")
    def error_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorType"))

    @error_type.setter
    def error_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce0cf4a4ec501f7716d8c5261d59f6efe0ef169c4430283d38e451b736ba9f10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MwsNetworksErrorMessages, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MwsNetworksErrorMessages, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MwsNetworksErrorMessages, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1c9213f0ab1042837f6bfd6fd37aaab3ed33f81c11cffba478228a6676da13e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.mwsNetworks.MwsNetworksGcpNetworkInfo",
    jsii_struct_bases=[],
    name_mapping={
        "network_project_id": "networkProjectId",
        "pod_ip_range_name": "podIpRangeName",
        "service_ip_range_name": "serviceIpRangeName",
        "subnet_id": "subnetId",
        "subnet_region": "subnetRegion",
        "vpc_id": "vpcId",
    },
)
class MwsNetworksGcpNetworkInfo:
    def __init__(
        self,
        *,
        network_project_id: builtins.str,
        pod_ip_range_name: builtins.str,
        service_ip_range_name: builtins.str,
        subnet_id: builtins.str,
        subnet_region: builtins.str,
        vpc_id: builtins.str,
    ) -> None:
        '''
        :param network_project_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#network_project_id MwsNetworks#network_project_id}.
        :param pod_ip_range_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#pod_ip_range_name MwsNetworks#pod_ip_range_name}.
        :param service_ip_range_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#service_ip_range_name MwsNetworks#service_ip_range_name}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#subnet_id MwsNetworks#subnet_id}.
        :param subnet_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#subnet_region MwsNetworks#subnet_region}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_id MwsNetworks#vpc_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdec507d37515c8d9053f5f7ea44be77c1745cfbaeb3eee64e6e67b6ae9fe265)
            check_type(argname="argument network_project_id", value=network_project_id, expected_type=type_hints["network_project_id"])
            check_type(argname="argument pod_ip_range_name", value=pod_ip_range_name, expected_type=type_hints["pod_ip_range_name"])
            check_type(argname="argument service_ip_range_name", value=service_ip_range_name, expected_type=type_hints["service_ip_range_name"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument subnet_region", value=subnet_region, expected_type=type_hints["subnet_region"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "network_project_id": network_project_id,
            "pod_ip_range_name": pod_ip_range_name,
            "service_ip_range_name": service_ip_range_name,
            "subnet_id": subnet_id,
            "subnet_region": subnet_region,
            "vpc_id": vpc_id,
        }

    @builtins.property
    def network_project_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#network_project_id MwsNetworks#network_project_id}.'''
        result = self._values.get("network_project_id")
        assert result is not None, "Required property 'network_project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pod_ip_range_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#pod_ip_range_name MwsNetworks#pod_ip_range_name}.'''
        result = self._values.get("pod_ip_range_name")
        assert result is not None, "Required property 'pod_ip_range_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_ip_range_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#service_ip_range_name MwsNetworks#service_ip_range_name}.'''
        result = self._values.get("service_ip_range_name")
        assert result is not None, "Required property 'service_ip_range_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#subnet_id MwsNetworks#subnet_id}.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#subnet_region MwsNetworks#subnet_region}.'''
        result = self._values.get("subnet_region")
        assert result is not None, "Required property 'subnet_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#vpc_id MwsNetworks#vpc_id}.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsNetworksGcpNetworkInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsNetworksGcpNetworkInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsNetworks.MwsNetworksGcpNetworkInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f180e768f3c97ed3aab325c204f8cfbe57cfda1dde724e3aa5f9838cb368a22)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="networkProjectIdInput")
    def network_project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkProjectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="podIpRangeNameInput")
    def pod_ip_range_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "podIpRangeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceIpRangeNameInput")
    def service_ip_range_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceIpRangeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetRegionInput")
    def subnet_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcIdInput")
    def vpc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcIdInput"))

    @builtins.property
    @jsii.member(jsii_name="networkProjectId")
    def network_project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkProjectId"))

    @network_project_id.setter
    def network_project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6c2ed60fd5d5d95bde2695bcf4a1b5de52effbced1dadc2a0b080086c1e0d82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkProjectId", value)

    @builtins.property
    @jsii.member(jsii_name="podIpRangeName")
    def pod_ip_range_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "podIpRangeName"))

    @pod_ip_range_name.setter
    def pod_ip_range_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c06bbbb3c0612d36cda59f74e87f7eb1a452fb0aac224093f97a8919e54a533)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "podIpRangeName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceIpRangeName")
    def service_ip_range_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceIpRangeName"))

    @service_ip_range_name.setter
    def service_ip_range_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb26d628024d4c113354d85b652fa0347f7c723dd08459595f6859d7a532c89c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceIpRangeName", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__520385a2a1741f748cd181abb2f0ca729a8c142dbbe7ff756851e31fbe3e7360)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="subnetRegion")
    def subnet_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetRegion"))

    @subnet_region.setter
    def subnet_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c848dc174d0630560aa9383fce8bb5ef7ebe803f21a9185aa172afe3aea09cf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetRegion", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6b837520e1c084adf85af048eb28bba2c651abb9109237c7baba89b8d24755d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwsNetworksGcpNetworkInfo]:
        return typing.cast(typing.Optional[MwsNetworksGcpNetworkInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MwsNetworksGcpNetworkInfo]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66d0d36bfede7f9f435117ce3b2db030b73448a3751132b104b8fcb214c58751)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.mwsNetworks.MwsNetworksVpcEndpoints",
    jsii_struct_bases=[],
    name_mapping={"dataplane_relay": "dataplaneRelay", "rest_api": "restApi"},
)
class MwsNetworksVpcEndpoints:
    def __init__(
        self,
        *,
        dataplane_relay: typing.Sequence[builtins.str],
        rest_api: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param dataplane_relay: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#dataplane_relay MwsNetworks#dataplane_relay}.
        :param rest_api: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#rest_api MwsNetworks#rest_api}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__061667d30730d41b1dd62991024aaf147e88d9c1968d978383a57abc9000a1ed)
            check_type(argname="argument dataplane_relay", value=dataplane_relay, expected_type=type_hints["dataplane_relay"])
            check_type(argname="argument rest_api", value=rest_api, expected_type=type_hints["rest_api"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataplane_relay": dataplane_relay,
            "rest_api": rest_api,
        }

    @builtins.property
    def dataplane_relay(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#dataplane_relay MwsNetworks#dataplane_relay}.'''
        result = self._values.get("dataplane_relay")
        assert result is not None, "Required property 'dataplane_relay' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def rest_api(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_networks#rest_api MwsNetworks#rest_api}.'''
        result = self._values.get("rest_api")
        assert result is not None, "Required property 'rest_api' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsNetworksVpcEndpoints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsNetworksVpcEndpointsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsNetworks.MwsNetworksVpcEndpointsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc3509c76bc3a3159fd96690163078fcd4a7f4e5fd18291c9116d65403f75cf1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dataplaneRelayInput")
    def dataplane_relay_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dataplaneRelayInput"))

    @builtins.property
    @jsii.member(jsii_name="restApiInput")
    def rest_api_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "restApiInput"))

    @builtins.property
    @jsii.member(jsii_name="dataplaneRelay")
    def dataplane_relay(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dataplaneRelay"))

    @dataplane_relay.setter
    def dataplane_relay(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__214848a6cd352e8fd5d0f470273f80ac4559ae636b898120116139f2bb52352a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataplaneRelay", value)

    @builtins.property
    @jsii.member(jsii_name="restApi")
    def rest_api(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "restApi"))

    @rest_api.setter
    def rest_api(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3b36b3551f33312a1f5d246e18978d3aefabcbecac69bafe5854f0245944db1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restApi", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwsNetworksVpcEndpoints]:
        return typing.cast(typing.Optional[MwsNetworksVpcEndpoints], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MwsNetworksVpcEndpoints]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23202bc92dfe27c602f3764b897dfc187af1c75dab0fc903c167c033cdd6768a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MwsNetworks",
    "MwsNetworksConfig",
    "MwsNetworksErrorMessages",
    "MwsNetworksErrorMessagesList",
    "MwsNetworksErrorMessagesOutputReference",
    "MwsNetworksGcpNetworkInfo",
    "MwsNetworksGcpNetworkInfoOutputReference",
    "MwsNetworksVpcEndpoints",
    "MwsNetworksVpcEndpointsOutputReference",
]

publication.publish()

def _typecheckingstub__a7a4f31f87ce1e16a1f76cba4af70e85a10bc191b4b024ba42b4735dd5bbed07(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    account_id: builtins.str,
    network_name: builtins.str,
    creation_time: typing.Optional[jsii.Number] = None,
    error_messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MwsNetworksErrorMessages, typing.Dict[builtins.str, typing.Any]]]]] = None,
    gcp_network_info: typing.Optional[typing.Union[MwsNetworksGcpNetworkInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    network_id: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    vpc_endpoints: typing.Optional[typing.Union[MwsNetworksVpcEndpoints, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_id: typing.Optional[builtins.str] = None,
    vpc_status: typing.Optional[builtins.str] = None,
    workspace_id: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__6ebe8b4982e35bac7a5a00ffd465aae4fae947af5a92fa72029f8481e93c9b39(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MwsNetworksErrorMessages, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50c5289721b52dc88fa07eaa73326f74e52b792f8a532c3b7e0867ec87f8ba31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42cbaedce6677f479da52942b0d9bdb60abafa3421aad41871d7ccc7e33af464(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8805acfda2d0c5d80d590a05dc2228325efb41eccd277378c7b83e940f37bc53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7644ac076904a5d4f90123c98bbe4e30b1747c2d9fde358191f035aac98a7962(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdd1ea1aebc8503c0f62e4fc7976fd6139a1acff3c72ad3416a9f27e8ce457d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84aaea7acc75e19805daed27902c47b69d748f21a9bf797628fae58218d746cc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e119ad1ab20ca8c50c5e80dfa1a946c7394471030c87025dba9c1fa01431b17a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1569a15df5b5a1df6f754aa3fffa25af5daf29359b1cd08e638900a1c117495c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f05a88f19f35e9d70b57d66e357f90fa8e7ec3c46c2f67a055a148c1a47fbae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__386e2928c95a2bd85ee81b36fb3d493178512f84953b8b21cfa10948e012293d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__414b8cae24f4c7d9fd6f98fea18650d1647ee00ff9f4feed0e2f9af69a088436(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    account_id: builtins.str,
    network_name: builtins.str,
    creation_time: typing.Optional[jsii.Number] = None,
    error_messages: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MwsNetworksErrorMessages, typing.Dict[builtins.str, typing.Any]]]]] = None,
    gcp_network_info: typing.Optional[typing.Union[MwsNetworksGcpNetworkInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    network_id: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    vpc_endpoints: typing.Optional[typing.Union[MwsNetworksVpcEndpoints, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_id: typing.Optional[builtins.str] = None,
    vpc_status: typing.Optional[builtins.str] = None,
    workspace_id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc51e84f2879a9e1fd90666f8bc04c19c62a149c150887c5503ca9d43463f558(
    *,
    error_message: typing.Optional[builtins.str] = None,
    error_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d1631c4927d33791d517b0bc8e8aad3aa9022342c4a01221d2c6c02a23a0aee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1beae8e4cb8354cb06b176534b6d69fda44dd939fef0ddd66186fdcc73faea51(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ed2f83cca0c420cda938a9a851709777b07b31bad030c6c439cfaffbe31a622(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15697f853800feb908008daca6cd87125b63588895f4325c1e1fa4aee0758ffc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97082dd4a79971d4a30204efbdb6aff923d7e0f199409c3ad30f21e84f4b1e05(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cfd6a231bb0546183fafeeab793975b4040e96d5abf4b70e8f07110c1681122(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MwsNetworksErrorMessages]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__502501c4da082083169ff51d1560138f638f51ea624aaaabe1016b522b02cd6f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfb17d632c660911374a904a666e73b7c1c4a915ea8dbf0445acf53ab0375c64(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce0cf4a4ec501f7716d8c5261d59f6efe0ef169c4430283d38e451b736ba9f10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1c9213f0ab1042837f6bfd6fd37aaab3ed33f81c11cffba478228a6676da13e(
    value: typing.Optional[typing.Union[MwsNetworksErrorMessages, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdec507d37515c8d9053f5f7ea44be77c1745cfbaeb3eee64e6e67b6ae9fe265(
    *,
    network_project_id: builtins.str,
    pod_ip_range_name: builtins.str,
    service_ip_range_name: builtins.str,
    subnet_id: builtins.str,
    subnet_region: builtins.str,
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f180e768f3c97ed3aab325c204f8cfbe57cfda1dde724e3aa5f9838cb368a22(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6c2ed60fd5d5d95bde2695bcf4a1b5de52effbced1dadc2a0b080086c1e0d82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c06bbbb3c0612d36cda59f74e87f7eb1a452fb0aac224093f97a8919e54a533(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb26d628024d4c113354d85b652fa0347f7c723dd08459595f6859d7a532c89c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__520385a2a1741f748cd181abb2f0ca729a8c142dbbe7ff756851e31fbe3e7360(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c848dc174d0630560aa9383fce8bb5ef7ebe803f21a9185aa172afe3aea09cf0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6b837520e1c084adf85af048eb28bba2c651abb9109237c7baba89b8d24755d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66d0d36bfede7f9f435117ce3b2db030b73448a3751132b104b8fcb214c58751(
    value: typing.Optional[MwsNetworksGcpNetworkInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__061667d30730d41b1dd62991024aaf147e88d9c1968d978383a57abc9000a1ed(
    *,
    dataplane_relay: typing.Sequence[builtins.str],
    rest_api: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc3509c76bc3a3159fd96690163078fcd4a7f4e5fd18291c9116d65403f75cf1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__214848a6cd352e8fd5d0f470273f80ac4559ae636b898120116139f2bb52352a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3b36b3551f33312a1f5d246e18978d3aefabcbecac69bafe5854f0245944db1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23202bc92dfe27c602f3764b897dfc187af1c75dab0fc903c167c033cdd6768a(
    value: typing.Optional[MwsNetworksVpcEndpoints],
) -> None:
    """Type checking stubs"""
    pass
