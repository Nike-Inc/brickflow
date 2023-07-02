'''
# `databricks_mws_vpc_endpoint`

Refer to the Terraform Registory for docs: [`databricks_mws_vpc_endpoint`](https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint).
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


class MwsVpcEndpoint(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsVpcEndpoint.MwsVpcEndpoint",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint databricks_mws_vpc_endpoint}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        vpc_endpoint_name: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        aws_account_id: typing.Optional[builtins.str] = None,
        aws_endpoint_service_id: typing.Optional[builtins.str] = None,
        aws_vpc_endpoint_id: typing.Optional[builtins.str] = None,
        gcp_vpc_endpoint_info: typing.Optional[typing.Union["MwsVpcEndpointGcpVpcEndpointInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        use_case: typing.Optional[builtins.str] = None,
        vpc_endpoint_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint databricks_mws_vpc_endpoint} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param vpc_endpoint_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#vpc_endpoint_name MwsVpcEndpoint#vpc_endpoint_name}.
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#account_id MwsVpcEndpoint#account_id}.
        :param aws_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#aws_account_id MwsVpcEndpoint#aws_account_id}.
        :param aws_endpoint_service_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#aws_endpoint_service_id MwsVpcEndpoint#aws_endpoint_service_id}.
        :param aws_vpc_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#aws_vpc_endpoint_id MwsVpcEndpoint#aws_vpc_endpoint_id}.
        :param gcp_vpc_endpoint_info: gcp_vpc_endpoint_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#gcp_vpc_endpoint_info MwsVpcEndpoint#gcp_vpc_endpoint_info}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#id MwsVpcEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#region MwsVpcEndpoint#region}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#state MwsVpcEndpoint#state}.
        :param use_case: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#use_case MwsVpcEndpoint#use_case}.
        :param vpc_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#vpc_endpoint_id MwsVpcEndpoint#vpc_endpoint_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60551eba903930df02e3cc3c6b05334e1a40d5bc4dd1e602ecefd7b2da5ee127)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MwsVpcEndpointConfig(
            vpc_endpoint_name=vpc_endpoint_name,
            account_id=account_id,
            aws_account_id=aws_account_id,
            aws_endpoint_service_id=aws_endpoint_service_id,
            aws_vpc_endpoint_id=aws_vpc_endpoint_id,
            gcp_vpc_endpoint_info=gcp_vpc_endpoint_info,
            id=id,
            region=region,
            state=state,
            use_case=use_case,
            vpc_endpoint_id=vpc_endpoint_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putGcpVpcEndpointInfo")
    def put_gcp_vpc_endpoint_info(
        self,
        *,
        endpoint_region: builtins.str,
        project_id: builtins.str,
        psc_endpoint_name: builtins.str,
        psc_connection_id: typing.Optional[builtins.str] = None,
        service_attachment_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#endpoint_region MwsVpcEndpoint#endpoint_region}.
        :param project_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#project_id MwsVpcEndpoint#project_id}.
        :param psc_endpoint_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#psc_endpoint_name MwsVpcEndpoint#psc_endpoint_name}.
        :param psc_connection_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#psc_connection_id MwsVpcEndpoint#psc_connection_id}.
        :param service_attachment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#service_attachment_id MwsVpcEndpoint#service_attachment_id}.
        '''
        value = MwsVpcEndpointGcpVpcEndpointInfo(
            endpoint_region=endpoint_region,
            project_id=project_id,
            psc_endpoint_name=psc_endpoint_name,
            psc_connection_id=psc_connection_id,
            service_attachment_id=service_attachment_id,
        )

        return typing.cast(None, jsii.invoke(self, "putGcpVpcEndpointInfo", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetAwsAccountId")
    def reset_aws_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsAccountId", []))

    @jsii.member(jsii_name="resetAwsEndpointServiceId")
    def reset_aws_endpoint_service_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsEndpointServiceId", []))

    @jsii.member(jsii_name="resetAwsVpcEndpointId")
    def reset_aws_vpc_endpoint_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsVpcEndpointId", []))

    @jsii.member(jsii_name="resetGcpVpcEndpointInfo")
    def reset_gcp_vpc_endpoint_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpVpcEndpointInfo", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @jsii.member(jsii_name="resetUseCase")
    def reset_use_case(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCase", []))

    @jsii.member(jsii_name="resetVpcEndpointId")
    def reset_vpc_endpoint_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcEndpointId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="gcpVpcEndpointInfo")
    def gcp_vpc_endpoint_info(
        self,
    ) -> "MwsVpcEndpointGcpVpcEndpointInfoOutputReference":
        return typing.cast("MwsVpcEndpointGcpVpcEndpointInfoOutputReference", jsii.get(self, "gcpVpcEndpointInfo"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="awsAccountIdInput")
    def aws_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="awsEndpointServiceIdInput")
    def aws_endpoint_service_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsEndpointServiceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="awsVpcEndpointIdInput")
    def aws_vpc_endpoint_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsVpcEndpointIdInput"))

    @builtins.property
    @jsii.member(jsii_name="gcpVpcEndpointInfoInput")
    def gcp_vpc_endpoint_info_input(
        self,
    ) -> typing.Optional["MwsVpcEndpointGcpVpcEndpointInfo"]:
        return typing.cast(typing.Optional["MwsVpcEndpointGcpVpcEndpointInfo"], jsii.get(self, "gcpVpcEndpointInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="useCaseInput")
    def use_case_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "useCaseInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointIdInput")
    def vpc_endpoint_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcEndpointIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointNameInput")
    def vpc_endpoint_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcEndpointNameInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5372c8fe455c9c0b9d17a8713361536efb1c2f79ff6dd9fe2aa6a5f151794096)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsAccountId"))

    @aws_account_id.setter
    def aws_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32da69f8967ca401be2a976258577991512bdd74493d93dca9826c3a368cd8f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="awsEndpointServiceId")
    def aws_endpoint_service_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsEndpointServiceId"))

    @aws_endpoint_service_id.setter
    def aws_endpoint_service_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4982baf06585d921e0114c988b3f124ea4014d491ab46f6653b807271e38185)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsEndpointServiceId", value)

    @builtins.property
    @jsii.member(jsii_name="awsVpcEndpointId")
    def aws_vpc_endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsVpcEndpointId"))

    @aws_vpc_endpoint_id.setter
    def aws_vpc_endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40409ca4c8f30653e8fcb0b39a4a97ef0b814f09fc8f2d258b3b2dcfb58832ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsVpcEndpointId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a424d15c8428ac7ed3a09ca8dc0005cd5336e018a0699d17ec331e2c9a5174ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9308a1a8d89da661e659ef89725d976c335a830f1dd33e418571cffb73c5a125)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f122d1144321e84064e588458f406a5977961234c5061eedf3fb160370f92873)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="useCase")
    def use_case(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "useCase"))

    @use_case.setter
    def use_case(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cb678c75c8dafdf7c9e22dcd4fed94420a3c894a35577ad23831c33d79b588f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCase", value)

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointId")
    def vpc_endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcEndpointId"))

    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dac6feba96f1054aaa7a1a97782b9540c4499a191747f2276b1f253075c4229)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcEndpointId", value)

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointName")
    def vpc_endpoint_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcEndpointName"))

    @vpc_endpoint_name.setter
    def vpc_endpoint_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35f640aed0a0bd598089f544c70b225130e7fb9487efe0171e860363c2bca5a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcEndpointName", value)


@jsii.data_type(
    jsii_type="databricks.mwsVpcEndpoint.MwsVpcEndpointConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "vpc_endpoint_name": "vpcEndpointName",
        "account_id": "accountId",
        "aws_account_id": "awsAccountId",
        "aws_endpoint_service_id": "awsEndpointServiceId",
        "aws_vpc_endpoint_id": "awsVpcEndpointId",
        "gcp_vpc_endpoint_info": "gcpVpcEndpointInfo",
        "id": "id",
        "region": "region",
        "state": "state",
        "use_case": "useCase",
        "vpc_endpoint_id": "vpcEndpointId",
    },
)
class MwsVpcEndpointConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        vpc_endpoint_name: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        aws_account_id: typing.Optional[builtins.str] = None,
        aws_endpoint_service_id: typing.Optional[builtins.str] = None,
        aws_vpc_endpoint_id: typing.Optional[builtins.str] = None,
        gcp_vpc_endpoint_info: typing.Optional[typing.Union["MwsVpcEndpointGcpVpcEndpointInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        use_case: typing.Optional[builtins.str] = None,
        vpc_endpoint_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param vpc_endpoint_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#vpc_endpoint_name MwsVpcEndpoint#vpc_endpoint_name}.
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#account_id MwsVpcEndpoint#account_id}.
        :param aws_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#aws_account_id MwsVpcEndpoint#aws_account_id}.
        :param aws_endpoint_service_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#aws_endpoint_service_id MwsVpcEndpoint#aws_endpoint_service_id}.
        :param aws_vpc_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#aws_vpc_endpoint_id MwsVpcEndpoint#aws_vpc_endpoint_id}.
        :param gcp_vpc_endpoint_info: gcp_vpc_endpoint_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#gcp_vpc_endpoint_info MwsVpcEndpoint#gcp_vpc_endpoint_info}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#id MwsVpcEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#region MwsVpcEndpoint#region}.
        :param state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#state MwsVpcEndpoint#state}.
        :param use_case: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#use_case MwsVpcEndpoint#use_case}.
        :param vpc_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#vpc_endpoint_id MwsVpcEndpoint#vpc_endpoint_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(gcp_vpc_endpoint_info, dict):
            gcp_vpc_endpoint_info = MwsVpcEndpointGcpVpcEndpointInfo(**gcp_vpc_endpoint_info)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da4bac7f1bd0fe248d227d508590515194fb1064160ec963ea3007225f59c0ff)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument vpc_endpoint_name", value=vpc_endpoint_name, expected_type=type_hints["vpc_endpoint_name"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument aws_endpoint_service_id", value=aws_endpoint_service_id, expected_type=type_hints["aws_endpoint_service_id"])
            check_type(argname="argument aws_vpc_endpoint_id", value=aws_vpc_endpoint_id, expected_type=type_hints["aws_vpc_endpoint_id"])
            check_type(argname="argument gcp_vpc_endpoint_info", value=gcp_vpc_endpoint_info, expected_type=type_hints["gcp_vpc_endpoint_info"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument use_case", value=use_case, expected_type=type_hints["use_case"])
            check_type(argname="argument vpc_endpoint_id", value=vpc_endpoint_id, expected_type=type_hints["vpc_endpoint_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc_endpoint_name": vpc_endpoint_name,
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
        if account_id is not None:
            self._values["account_id"] = account_id
        if aws_account_id is not None:
            self._values["aws_account_id"] = aws_account_id
        if aws_endpoint_service_id is not None:
            self._values["aws_endpoint_service_id"] = aws_endpoint_service_id
        if aws_vpc_endpoint_id is not None:
            self._values["aws_vpc_endpoint_id"] = aws_vpc_endpoint_id
        if gcp_vpc_endpoint_info is not None:
            self._values["gcp_vpc_endpoint_info"] = gcp_vpc_endpoint_info
        if id is not None:
            self._values["id"] = id
        if region is not None:
            self._values["region"] = region
        if state is not None:
            self._values["state"] = state
        if use_case is not None:
            self._values["use_case"] = use_case
        if vpc_endpoint_id is not None:
            self._values["vpc_endpoint_id"] = vpc_endpoint_id

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
    def vpc_endpoint_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#vpc_endpoint_name MwsVpcEndpoint#vpc_endpoint_name}.'''
        result = self._values.get("vpc_endpoint_name")
        assert result is not None, "Required property 'vpc_endpoint_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#account_id MwsVpcEndpoint#account_id}.'''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#aws_account_id MwsVpcEndpoint#aws_account_id}.'''
        result = self._values.get("aws_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_endpoint_service_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#aws_endpoint_service_id MwsVpcEndpoint#aws_endpoint_service_id}.'''
        result = self._values.get("aws_endpoint_service_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_vpc_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#aws_vpc_endpoint_id MwsVpcEndpoint#aws_vpc_endpoint_id}.'''
        result = self._values.get("aws_vpc_endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gcp_vpc_endpoint_info(
        self,
    ) -> typing.Optional["MwsVpcEndpointGcpVpcEndpointInfo"]:
        '''gcp_vpc_endpoint_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#gcp_vpc_endpoint_info MwsVpcEndpoint#gcp_vpc_endpoint_info}
        '''
        result = self._values.get("gcp_vpc_endpoint_info")
        return typing.cast(typing.Optional["MwsVpcEndpointGcpVpcEndpointInfo"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#id MwsVpcEndpoint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#region MwsVpcEndpoint#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#state MwsVpcEndpoint#state}.'''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_case(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#use_case MwsVpcEndpoint#use_case}.'''
        result = self._values.get("use_case")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#vpc_endpoint_id MwsVpcEndpoint#vpc_endpoint_id}.'''
        result = self._values.get("vpc_endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsVpcEndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.mwsVpcEndpoint.MwsVpcEndpointGcpVpcEndpointInfo",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_region": "endpointRegion",
        "project_id": "projectId",
        "psc_endpoint_name": "pscEndpointName",
        "psc_connection_id": "pscConnectionId",
        "service_attachment_id": "serviceAttachmentId",
    },
)
class MwsVpcEndpointGcpVpcEndpointInfo:
    def __init__(
        self,
        *,
        endpoint_region: builtins.str,
        project_id: builtins.str,
        psc_endpoint_name: builtins.str,
        psc_connection_id: typing.Optional[builtins.str] = None,
        service_attachment_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param endpoint_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#endpoint_region MwsVpcEndpoint#endpoint_region}.
        :param project_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#project_id MwsVpcEndpoint#project_id}.
        :param psc_endpoint_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#psc_endpoint_name MwsVpcEndpoint#psc_endpoint_name}.
        :param psc_connection_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#psc_connection_id MwsVpcEndpoint#psc_connection_id}.
        :param service_attachment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#service_attachment_id MwsVpcEndpoint#service_attachment_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a8af8f399958e934524df2b81f7c8a9402905c26653b329ac5e0f91ec697d45)
            check_type(argname="argument endpoint_region", value=endpoint_region, expected_type=type_hints["endpoint_region"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument psc_endpoint_name", value=psc_endpoint_name, expected_type=type_hints["psc_endpoint_name"])
            check_type(argname="argument psc_connection_id", value=psc_connection_id, expected_type=type_hints["psc_connection_id"])
            check_type(argname="argument service_attachment_id", value=service_attachment_id, expected_type=type_hints["service_attachment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_region": endpoint_region,
            "project_id": project_id,
            "psc_endpoint_name": psc_endpoint_name,
        }
        if psc_connection_id is not None:
            self._values["psc_connection_id"] = psc_connection_id
        if service_attachment_id is not None:
            self._values["service_attachment_id"] = service_attachment_id

    @builtins.property
    def endpoint_region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#endpoint_region MwsVpcEndpoint#endpoint_region}.'''
        result = self._values.get("endpoint_region")
        assert result is not None, "Required property 'endpoint_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#project_id MwsVpcEndpoint#project_id}.'''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def psc_endpoint_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#psc_endpoint_name MwsVpcEndpoint#psc_endpoint_name}.'''
        result = self._values.get("psc_endpoint_name")
        assert result is not None, "Required property 'psc_endpoint_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def psc_connection_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#psc_connection_id MwsVpcEndpoint#psc_connection_id}.'''
        result = self._values.get("psc_connection_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_attachment_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_vpc_endpoint#service_attachment_id MwsVpcEndpoint#service_attachment_id}.'''
        result = self._values.get("service_attachment_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsVpcEndpointGcpVpcEndpointInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsVpcEndpointGcpVpcEndpointInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsVpcEndpoint.MwsVpcEndpointGcpVpcEndpointInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__891906f473561f418e3211efe853ef3eb01530d75bcacd4d920adcc16cdef5df)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPscConnectionId")
    def reset_psc_connection_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPscConnectionId", []))

    @jsii.member(jsii_name="resetServiceAttachmentId")
    def reset_service_attachment_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAttachmentId", []))

    @builtins.property
    @jsii.member(jsii_name="endpointRegionInput")
    def endpoint_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="pscConnectionIdInput")
    def psc_connection_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pscConnectionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="pscEndpointNameInput")
    def psc_endpoint_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pscEndpointNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAttachmentIdInput")
    def service_attachment_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAttachmentIdInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointRegion")
    def endpoint_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointRegion"))

    @endpoint_region.setter
    def endpoint_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__942a9d7e6dbf043f5aed0a15ebc153d2b34b7486a18ad5e2e25546cf683fa0c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointRegion", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74a33498a410769b5feb4929d46d2e3b646dfe1bc8f28b54dc22445e4c3344c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="pscConnectionId")
    def psc_connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pscConnectionId"))

    @psc_connection_id.setter
    def psc_connection_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80d0cd6b606d7589b182bcfce25cffeda37c7ce000fa012747491f4b52d33bb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pscConnectionId", value)

    @builtins.property
    @jsii.member(jsii_name="pscEndpointName")
    def psc_endpoint_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pscEndpointName"))

    @psc_endpoint_name.setter
    def psc_endpoint_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb17d0d6f50f85fdbfd1d515a42d966aeec41edb2fb0dd0fe245630e77bc0782)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pscEndpointName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAttachmentId")
    def service_attachment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAttachmentId"))

    @service_attachment_id.setter
    def service_attachment_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee9763fc3deed042229daa10471e9267d12190f9fa8dc5f596d8b1da70a3d818)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAttachmentId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwsVpcEndpointGcpVpcEndpointInfo]:
        return typing.cast(typing.Optional[MwsVpcEndpointGcpVpcEndpointInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwsVpcEndpointGcpVpcEndpointInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2dce673a92cbde9ba81cabf2c97b26bdfa227048d95b2388e6cf3187553a01b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MwsVpcEndpoint",
    "MwsVpcEndpointConfig",
    "MwsVpcEndpointGcpVpcEndpointInfo",
    "MwsVpcEndpointGcpVpcEndpointInfoOutputReference",
]

publication.publish()

def _typecheckingstub__60551eba903930df02e3cc3c6b05334e1a40d5bc4dd1e602ecefd7b2da5ee127(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    vpc_endpoint_name: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    aws_account_id: typing.Optional[builtins.str] = None,
    aws_endpoint_service_id: typing.Optional[builtins.str] = None,
    aws_vpc_endpoint_id: typing.Optional[builtins.str] = None,
    gcp_vpc_endpoint_info: typing.Optional[typing.Union[MwsVpcEndpointGcpVpcEndpointInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    use_case: typing.Optional[builtins.str] = None,
    vpc_endpoint_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__5372c8fe455c9c0b9d17a8713361536efb1c2f79ff6dd9fe2aa6a5f151794096(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32da69f8967ca401be2a976258577991512bdd74493d93dca9826c3a368cd8f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4982baf06585d921e0114c988b3f124ea4014d491ab46f6653b807271e38185(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40409ca4c8f30653e8fcb0b39a4a97ef0b814f09fc8f2d258b3b2dcfb58832ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a424d15c8428ac7ed3a09ca8dc0005cd5336e018a0699d17ec331e2c9a5174ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9308a1a8d89da661e659ef89725d976c335a830f1dd33e418571cffb73c5a125(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f122d1144321e84064e588458f406a5977961234c5061eedf3fb160370f92873(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cb678c75c8dafdf7c9e22dcd4fed94420a3c894a35577ad23831c33d79b588f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dac6feba96f1054aaa7a1a97782b9540c4499a191747f2276b1f253075c4229(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35f640aed0a0bd598089f544c70b225130e7fb9487efe0171e860363c2bca5a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da4bac7f1bd0fe248d227d508590515194fb1064160ec963ea3007225f59c0ff(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    vpc_endpoint_name: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    aws_account_id: typing.Optional[builtins.str] = None,
    aws_endpoint_service_id: typing.Optional[builtins.str] = None,
    aws_vpc_endpoint_id: typing.Optional[builtins.str] = None,
    gcp_vpc_endpoint_info: typing.Optional[typing.Union[MwsVpcEndpointGcpVpcEndpointInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    use_case: typing.Optional[builtins.str] = None,
    vpc_endpoint_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a8af8f399958e934524df2b81f7c8a9402905c26653b329ac5e0f91ec697d45(
    *,
    endpoint_region: builtins.str,
    project_id: builtins.str,
    psc_endpoint_name: builtins.str,
    psc_connection_id: typing.Optional[builtins.str] = None,
    service_attachment_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__891906f473561f418e3211efe853ef3eb01530d75bcacd4d920adcc16cdef5df(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__942a9d7e6dbf043f5aed0a15ebc153d2b34b7486a18ad5e2e25546cf683fa0c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74a33498a410769b5feb4929d46d2e3b646dfe1bc8f28b54dc22445e4c3344c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80d0cd6b606d7589b182bcfce25cffeda37c7ce000fa012747491f4b52d33bb7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb17d0d6f50f85fdbfd1d515a42d966aeec41edb2fb0dd0fe245630e77bc0782(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee9763fc3deed042229daa10471e9267d12190f9fa8dc5f596d8b1da70a3d818(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2dce673a92cbde9ba81cabf2c97b26bdfa227048d95b2388e6cf3187553a01b(
    value: typing.Optional[MwsVpcEndpointGcpVpcEndpointInfo],
) -> None:
    """Type checking stubs"""
    pass
