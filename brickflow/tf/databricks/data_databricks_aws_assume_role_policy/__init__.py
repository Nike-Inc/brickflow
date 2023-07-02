'''
# `data_databricks_aws_assume_role_policy`

Refer to the Terraform Registory for docs: [`data_databricks_aws_assume_role_policy`](https://www.terraform.io/docs/providers/databricks/d/aws_assume_role_policy).
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


class DataDatabricksAwsAssumeRolePolicy(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksAwsAssumeRolePolicy.DataDatabricksAwsAssumeRolePolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/d/aws_assume_role_policy databricks_aws_assume_role_policy}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        external_id: builtins.str,
        databricks_account_id: typing.Optional[builtins.str] = None,
        for_log_delivery: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/d/aws_assume_role_policy databricks_aws_assume_role_policy} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param external_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/aws_assume_role_policy#external_id DataDatabricksAwsAssumeRolePolicy#external_id}.
        :param databricks_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/aws_assume_role_policy#databricks_account_id DataDatabricksAwsAssumeRolePolicy#databricks_account_id}.
        :param for_log_delivery: Grant AssumeRole to Databricks SaasUsageDeliveryRole instead of root account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/aws_assume_role_policy#for_log_delivery DataDatabricksAwsAssumeRolePolicy#for_log_delivery}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/aws_assume_role_policy#id DataDatabricksAwsAssumeRolePolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a53cc6c90938ef6fce79998e6baa26f9b335f20e71a505fac9c36ac0ecc831ec)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataDatabricksAwsAssumeRolePolicyConfig(
            external_id=external_id,
            databricks_account_id=databricks_account_id,
            for_log_delivery=for_log_delivery,
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

    @jsii.member(jsii_name="resetDatabricksAccountId")
    def reset_databricks_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabricksAccountId", []))

    @jsii.member(jsii_name="resetForLogDelivery")
    def reset_for_log_delivery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForLogDelivery", []))

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
    @jsii.member(jsii_name="json")
    def json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "json"))

    @builtins.property
    @jsii.member(jsii_name="databricksAccountIdInput")
    def databricks_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databricksAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="externalIdInput")
    def external_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="forLogDeliveryInput")
    def for_log_delivery_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forLogDeliveryInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="databricksAccountId")
    def databricks_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databricksAccountId"))

    @databricks_account_id.setter
    def databricks_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7afd731df083614541136aaf9860c0cccae06fac14645660055735603790f7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databricksAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="externalId")
    def external_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalId"))

    @external_id.setter
    def external_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3208bd55f2ee1494eab00306dc188ea2985ffda4507a5fc086246b78dccee6bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalId", value)

    @builtins.property
    @jsii.member(jsii_name="forLogDelivery")
    def for_log_delivery(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forLogDelivery"))

    @for_log_delivery.setter
    def for_log_delivery(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e4f3cd940ca97fb666cc0612433950d4a7326d485d1b3cd73150fa3bdf5adfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forLogDelivery", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ec5570e259ae645ad6947b4420a27daccfc6cd43778db3daf92fd014fa07e4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksAwsAssumeRolePolicy.DataDatabricksAwsAssumeRolePolicyConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "external_id": "externalId",
        "databricks_account_id": "databricksAccountId",
        "for_log_delivery": "forLogDelivery",
        "id": "id",
    },
)
class DataDatabricksAwsAssumeRolePolicyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        external_id: builtins.str,
        databricks_account_id: typing.Optional[builtins.str] = None,
        for_log_delivery: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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
        :param external_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/aws_assume_role_policy#external_id DataDatabricksAwsAssumeRolePolicy#external_id}.
        :param databricks_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/aws_assume_role_policy#databricks_account_id DataDatabricksAwsAssumeRolePolicy#databricks_account_id}.
        :param for_log_delivery: Grant AssumeRole to Databricks SaasUsageDeliveryRole instead of root account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/aws_assume_role_policy#for_log_delivery DataDatabricksAwsAssumeRolePolicy#for_log_delivery}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/aws_assume_role_policy#id DataDatabricksAwsAssumeRolePolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4a8201323341fe419ea2d043f26a1804f46e3bb06669174b83fac95f93977af)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            check_type(argname="argument databricks_account_id", value=databricks_account_id, expected_type=type_hints["databricks_account_id"])
            check_type(argname="argument for_log_delivery", value=for_log_delivery, expected_type=type_hints["for_log_delivery"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "external_id": external_id,
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
        if databricks_account_id is not None:
            self._values["databricks_account_id"] = databricks_account_id
        if for_log_delivery is not None:
            self._values["for_log_delivery"] = for_log_delivery
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
    def external_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/aws_assume_role_policy#external_id DataDatabricksAwsAssumeRolePolicy#external_id}.'''
        result = self._values.get("external_id")
        assert result is not None, "Required property 'external_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def databricks_account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/aws_assume_role_policy#databricks_account_id DataDatabricksAwsAssumeRolePolicy#databricks_account_id}.'''
        result = self._values.get("databricks_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def for_log_delivery(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Grant AssumeRole to Databricks SaasUsageDeliveryRole instead of root account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/aws_assume_role_policy#for_log_delivery DataDatabricksAwsAssumeRolePolicy#for_log_delivery}
        '''
        result = self._values.get("for_log_delivery")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/aws_assume_role_policy#id DataDatabricksAwsAssumeRolePolicy#id}.

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
        return "DataDatabricksAwsAssumeRolePolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataDatabricksAwsAssumeRolePolicy",
    "DataDatabricksAwsAssumeRolePolicyConfig",
]

publication.publish()

def _typecheckingstub__a53cc6c90938ef6fce79998e6baa26f9b335f20e71a505fac9c36ac0ecc831ec(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    external_id: builtins.str,
    databricks_account_id: typing.Optional[builtins.str] = None,
    for_log_delivery: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__c7afd731df083614541136aaf9860c0cccae06fac14645660055735603790f7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3208bd55f2ee1494eab00306dc188ea2985ffda4507a5fc086246b78dccee6bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e4f3cd940ca97fb666cc0612433950d4a7326d485d1b3cd73150fa3bdf5adfd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ec5570e259ae645ad6947b4420a27daccfc6cd43778db3daf92fd014fa07e4a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4a8201323341fe419ea2d043f26a1804f46e3bb06669174b83fac95f93977af(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    external_id: builtins.str,
    databricks_account_id: typing.Optional[builtins.str] = None,
    for_log_delivery: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
