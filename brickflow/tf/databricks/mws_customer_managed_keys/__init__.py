'''
# `databricks_mws_customer_managed_keys`

Refer to the Terraform Registory for docs: [`databricks_mws_customer_managed_keys`](https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys).
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


class MwsCustomerManagedKeys(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsCustomerManagedKeys.MwsCustomerManagedKeys",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys databricks_mws_customer_managed_keys}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        account_id: builtins.str,
        use_cases: typing.Sequence[builtins.str],
        aws_key_info: typing.Optional[typing.Union["MwsCustomerManagedKeysAwsKeyInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        creation_time: typing.Optional[jsii.Number] = None,
        customer_managed_key_id: typing.Optional[builtins.str] = None,
        gcp_key_info: typing.Optional[typing.Union["MwsCustomerManagedKeysGcpKeyInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys databricks_mws_customer_managed_keys} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#account_id MwsCustomerManagedKeys#account_id}.
        :param use_cases: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#use_cases MwsCustomerManagedKeys#use_cases}.
        :param aws_key_info: aws_key_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#aws_key_info MwsCustomerManagedKeys#aws_key_info}
        :param creation_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#creation_time MwsCustomerManagedKeys#creation_time}.
        :param customer_managed_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#customer_managed_key_id MwsCustomerManagedKeys#customer_managed_key_id}.
        :param gcp_key_info: gcp_key_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#gcp_key_info MwsCustomerManagedKeys#gcp_key_info}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#id MwsCustomerManagedKeys#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18bf3ef8ef98d65250b7b66a8d075a46b615f16a125787a9b23ce1f5924361b0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MwsCustomerManagedKeysConfig(
            account_id=account_id,
            use_cases=use_cases,
            aws_key_info=aws_key_info,
            creation_time=creation_time,
            customer_managed_key_id=customer_managed_key_id,
            gcp_key_info=gcp_key_info,
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

    @jsii.member(jsii_name="putAwsKeyInfo")
    def put_aws_key_info(
        self,
        *,
        key_alias: builtins.str,
        key_arn: builtins.str,
        key_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_alias: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#key_alias MwsCustomerManagedKeys#key_alias}.
        :param key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#key_arn MwsCustomerManagedKeys#key_arn}.
        :param key_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#key_region MwsCustomerManagedKeys#key_region}.
        '''
        value = MwsCustomerManagedKeysAwsKeyInfo(
            key_alias=key_alias, key_arn=key_arn, key_region=key_region
        )

        return typing.cast(None, jsii.invoke(self, "putAwsKeyInfo", [value]))

    @jsii.member(jsii_name="putGcpKeyInfo")
    def put_gcp_key_info(self, *, kms_key_id: builtins.str) -> None:
        '''
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#kms_key_id MwsCustomerManagedKeys#kms_key_id}.
        '''
        value = MwsCustomerManagedKeysGcpKeyInfo(kms_key_id=kms_key_id)

        return typing.cast(None, jsii.invoke(self, "putGcpKeyInfo", [value]))

    @jsii.member(jsii_name="resetAwsKeyInfo")
    def reset_aws_key_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsKeyInfo", []))

    @jsii.member(jsii_name="resetCreationTime")
    def reset_creation_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreationTime", []))

    @jsii.member(jsii_name="resetCustomerManagedKeyId")
    def reset_customer_managed_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerManagedKeyId", []))

    @jsii.member(jsii_name="resetGcpKeyInfo")
    def reset_gcp_key_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpKeyInfo", []))

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
    @jsii.member(jsii_name="awsKeyInfo")
    def aws_key_info(self) -> "MwsCustomerManagedKeysAwsKeyInfoOutputReference":
        return typing.cast("MwsCustomerManagedKeysAwsKeyInfoOutputReference", jsii.get(self, "awsKeyInfo"))

    @builtins.property
    @jsii.member(jsii_name="gcpKeyInfo")
    def gcp_key_info(self) -> "MwsCustomerManagedKeysGcpKeyInfoOutputReference":
        return typing.cast("MwsCustomerManagedKeysGcpKeyInfoOutputReference", jsii.get(self, "gcpKeyInfo"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="awsKeyInfoInput")
    def aws_key_info_input(self) -> typing.Optional["MwsCustomerManagedKeysAwsKeyInfo"]:
        return typing.cast(typing.Optional["MwsCustomerManagedKeysAwsKeyInfo"], jsii.get(self, "awsKeyInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="creationTimeInput")
    def creation_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "creationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="customerManagedKeyIdInput")
    def customer_managed_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerManagedKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="gcpKeyInfoInput")
    def gcp_key_info_input(self) -> typing.Optional["MwsCustomerManagedKeysGcpKeyInfo"]:
        return typing.cast(typing.Optional["MwsCustomerManagedKeysGcpKeyInfo"], jsii.get(self, "gcpKeyInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="useCasesInput")
    def use_cases_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "useCasesInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb6e4993fbb1d5485178110b5c7d7e03f06c632f840ac69be9dd0208ca2e93cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="creationTime")
    def creation_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "creationTime"))

    @creation_time.setter
    def creation_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41858d3ee6a4e583a3ac851dc4bbb41fe898ff3c4eda004e5082c1a27f0703fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creationTime", value)

    @builtins.property
    @jsii.member(jsii_name="customerManagedKeyId")
    def customer_managed_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerManagedKeyId"))

    @customer_managed_key_id.setter
    def customer_managed_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65a46d9fcf398091c43317a89f5487e99a6ac4bf15390ba5b05ec0c61897ab75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerManagedKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d807216a4bc9104d3c7b82eb2fe7787ae74527033c5025126d13908378b97cca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="useCases")
    def use_cases(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "useCases"))

    @use_cases.setter
    def use_cases(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe6c30c120c5406b516da3b12711285c9b4d82a6d10666f78bee242ea8115657)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCases", value)


@jsii.data_type(
    jsii_type="databricks.mwsCustomerManagedKeys.MwsCustomerManagedKeysAwsKeyInfo",
    jsii_struct_bases=[],
    name_mapping={
        "key_alias": "keyAlias",
        "key_arn": "keyArn",
        "key_region": "keyRegion",
    },
)
class MwsCustomerManagedKeysAwsKeyInfo:
    def __init__(
        self,
        *,
        key_alias: builtins.str,
        key_arn: builtins.str,
        key_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_alias: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#key_alias MwsCustomerManagedKeys#key_alias}.
        :param key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#key_arn MwsCustomerManagedKeys#key_arn}.
        :param key_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#key_region MwsCustomerManagedKeys#key_region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23e55d4f6b798ab5830ad2061f53f107295c986fe8321e1e2bef27087367dda0)
            check_type(argname="argument key_alias", value=key_alias, expected_type=type_hints["key_alias"])
            check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
            check_type(argname="argument key_region", value=key_region, expected_type=type_hints["key_region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key_alias": key_alias,
            "key_arn": key_arn,
        }
        if key_region is not None:
            self._values["key_region"] = key_region

    @builtins.property
    def key_alias(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#key_alias MwsCustomerManagedKeys#key_alias}.'''
        result = self._values.get("key_alias")
        assert result is not None, "Required property 'key_alias' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#key_arn MwsCustomerManagedKeys#key_arn}.'''
        result = self._values.get("key_arn")
        assert result is not None, "Required property 'key_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#key_region MwsCustomerManagedKeys#key_region}.'''
        result = self._values.get("key_region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsCustomerManagedKeysAwsKeyInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsCustomerManagedKeysAwsKeyInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsCustomerManagedKeys.MwsCustomerManagedKeysAwsKeyInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f34b46bd82fbf7b42ae241d083cffd58c46e930916db55782174cb3475309c7a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKeyRegion")
    def reset_key_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyRegion", []))

    @builtins.property
    @jsii.member(jsii_name="keyAliasInput")
    def key_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="keyArnInput")
    def key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="keyRegionInput")
    def key_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="keyAlias")
    def key_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyAlias"))

    @key_alias.setter
    def key_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__508153dc9e12ad586eae3dd50ea8447ade09fbeb1293074c48ed95932bc20d41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyAlias", value)

    @builtins.property
    @jsii.member(jsii_name="keyArn")
    def key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyArn"))

    @key_arn.setter
    def key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7839c2878fdc0615d6334561bb7bb84dd1e2565fcc0613120f566dcd25ca3f64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyArn", value)

    @builtins.property
    @jsii.member(jsii_name="keyRegion")
    def key_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyRegion"))

    @key_region.setter
    def key_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__329594afc90978fc2999dc63c94617653f4e486573fdca93ad585cab2b362bce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyRegion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwsCustomerManagedKeysAwsKeyInfo]:
        return typing.cast(typing.Optional[MwsCustomerManagedKeysAwsKeyInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwsCustomerManagedKeysAwsKeyInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13495e0bcab567a14464d15eb4dd2cc4eab944dd23a6417e8a3de068fed8913f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.mwsCustomerManagedKeys.MwsCustomerManagedKeysConfig",
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
        "use_cases": "useCases",
        "aws_key_info": "awsKeyInfo",
        "creation_time": "creationTime",
        "customer_managed_key_id": "customerManagedKeyId",
        "gcp_key_info": "gcpKeyInfo",
        "id": "id",
    },
)
class MwsCustomerManagedKeysConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        use_cases: typing.Sequence[builtins.str],
        aws_key_info: typing.Optional[typing.Union[MwsCustomerManagedKeysAwsKeyInfo, typing.Dict[builtins.str, typing.Any]]] = None,
        creation_time: typing.Optional[jsii.Number] = None,
        customer_managed_key_id: typing.Optional[builtins.str] = None,
        gcp_key_info: typing.Optional[typing.Union["MwsCustomerManagedKeysGcpKeyInfo", typing.Dict[builtins.str, typing.Any]]] = None,
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
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#account_id MwsCustomerManagedKeys#account_id}.
        :param use_cases: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#use_cases MwsCustomerManagedKeys#use_cases}.
        :param aws_key_info: aws_key_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#aws_key_info MwsCustomerManagedKeys#aws_key_info}
        :param creation_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#creation_time MwsCustomerManagedKeys#creation_time}.
        :param customer_managed_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#customer_managed_key_id MwsCustomerManagedKeys#customer_managed_key_id}.
        :param gcp_key_info: gcp_key_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#gcp_key_info MwsCustomerManagedKeys#gcp_key_info}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#id MwsCustomerManagedKeys#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(aws_key_info, dict):
            aws_key_info = MwsCustomerManagedKeysAwsKeyInfo(**aws_key_info)
        if isinstance(gcp_key_info, dict):
            gcp_key_info = MwsCustomerManagedKeysGcpKeyInfo(**gcp_key_info)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65642c29e38c67a772e1a81da45c4621be59f1d44762cb7380431c064dc6d8ac)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument use_cases", value=use_cases, expected_type=type_hints["use_cases"])
            check_type(argname="argument aws_key_info", value=aws_key_info, expected_type=type_hints["aws_key_info"])
            check_type(argname="argument creation_time", value=creation_time, expected_type=type_hints["creation_time"])
            check_type(argname="argument customer_managed_key_id", value=customer_managed_key_id, expected_type=type_hints["customer_managed_key_id"])
            check_type(argname="argument gcp_key_info", value=gcp_key_info, expected_type=type_hints["gcp_key_info"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
            "use_cases": use_cases,
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
        if aws_key_info is not None:
            self._values["aws_key_info"] = aws_key_info
        if creation_time is not None:
            self._values["creation_time"] = creation_time
        if customer_managed_key_id is not None:
            self._values["customer_managed_key_id"] = customer_managed_key_id
        if gcp_key_info is not None:
            self._values["gcp_key_info"] = gcp_key_info
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
    def account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#account_id MwsCustomerManagedKeys#account_id}.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_cases(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#use_cases MwsCustomerManagedKeys#use_cases}.'''
        result = self._values.get("use_cases")
        assert result is not None, "Required property 'use_cases' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def aws_key_info(self) -> typing.Optional[MwsCustomerManagedKeysAwsKeyInfo]:
        '''aws_key_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#aws_key_info MwsCustomerManagedKeys#aws_key_info}
        '''
        result = self._values.get("aws_key_info")
        return typing.cast(typing.Optional[MwsCustomerManagedKeysAwsKeyInfo], result)

    @builtins.property
    def creation_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#creation_time MwsCustomerManagedKeys#creation_time}.'''
        result = self._values.get("creation_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def customer_managed_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#customer_managed_key_id MwsCustomerManagedKeys#customer_managed_key_id}.'''
        result = self._values.get("customer_managed_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gcp_key_info(self) -> typing.Optional["MwsCustomerManagedKeysGcpKeyInfo"]:
        '''gcp_key_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#gcp_key_info MwsCustomerManagedKeys#gcp_key_info}
        '''
        result = self._values.get("gcp_key_info")
        return typing.cast(typing.Optional["MwsCustomerManagedKeysGcpKeyInfo"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#id MwsCustomerManagedKeys#id}.

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
        return "MwsCustomerManagedKeysConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.mwsCustomerManagedKeys.MwsCustomerManagedKeysGcpKeyInfo",
    jsii_struct_bases=[],
    name_mapping={"kms_key_id": "kmsKeyId"},
)
class MwsCustomerManagedKeysGcpKeyInfo:
    def __init__(self, *, kms_key_id: builtins.str) -> None:
        '''
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#kms_key_id MwsCustomerManagedKeys#kms_key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce3da851d2ed2e626becd3c87f6d80b59ee057e84c75f0c8931aa77b73d7628b)
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kms_key_id": kms_key_id,
        }

    @builtins.property
    def kms_key_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_customer_managed_keys#kms_key_id MwsCustomerManagedKeys#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        assert result is not None, "Required property 'kms_key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsCustomerManagedKeysGcpKeyInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsCustomerManagedKeysGcpKeyInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsCustomerManagedKeys.MwsCustomerManagedKeysGcpKeyInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__935b0f54f3f28b41c8c483b85c4eb78e190a059168f5d134508017b2d8cfc1f0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d2597aa0df0cf052a16eef09aef83b1417964600a1533ddd6e77a5c6289392f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwsCustomerManagedKeysGcpKeyInfo]:
        return typing.cast(typing.Optional[MwsCustomerManagedKeysGcpKeyInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwsCustomerManagedKeysGcpKeyInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca5a7511bbb3f6cad3e55d5e4f1a3091cb39482b3fcac501974c15b34dfb5a31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MwsCustomerManagedKeys",
    "MwsCustomerManagedKeysAwsKeyInfo",
    "MwsCustomerManagedKeysAwsKeyInfoOutputReference",
    "MwsCustomerManagedKeysConfig",
    "MwsCustomerManagedKeysGcpKeyInfo",
    "MwsCustomerManagedKeysGcpKeyInfoOutputReference",
]

publication.publish()

def _typecheckingstub__18bf3ef8ef98d65250b7b66a8d075a46b615f16a125787a9b23ce1f5924361b0(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    account_id: builtins.str,
    use_cases: typing.Sequence[builtins.str],
    aws_key_info: typing.Optional[typing.Union[MwsCustomerManagedKeysAwsKeyInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    creation_time: typing.Optional[jsii.Number] = None,
    customer_managed_key_id: typing.Optional[builtins.str] = None,
    gcp_key_info: typing.Optional[typing.Union[MwsCustomerManagedKeysGcpKeyInfo, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__eb6e4993fbb1d5485178110b5c7d7e03f06c632f840ac69be9dd0208ca2e93cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41858d3ee6a4e583a3ac851dc4bbb41fe898ff3c4eda004e5082c1a27f0703fc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65a46d9fcf398091c43317a89f5487e99a6ac4bf15390ba5b05ec0c61897ab75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d807216a4bc9104d3c7b82eb2fe7787ae74527033c5025126d13908378b97cca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe6c30c120c5406b516da3b12711285c9b4d82a6d10666f78bee242ea8115657(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23e55d4f6b798ab5830ad2061f53f107295c986fe8321e1e2bef27087367dda0(
    *,
    key_alias: builtins.str,
    key_arn: builtins.str,
    key_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f34b46bd82fbf7b42ae241d083cffd58c46e930916db55782174cb3475309c7a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__508153dc9e12ad586eae3dd50ea8447ade09fbeb1293074c48ed95932bc20d41(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7839c2878fdc0615d6334561bb7bb84dd1e2565fcc0613120f566dcd25ca3f64(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__329594afc90978fc2999dc63c94617653f4e486573fdca93ad585cab2b362bce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13495e0bcab567a14464d15eb4dd2cc4eab944dd23a6417e8a3de068fed8913f(
    value: typing.Optional[MwsCustomerManagedKeysAwsKeyInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65642c29e38c67a772e1a81da45c4621be59f1d44762cb7380431c064dc6d8ac(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    account_id: builtins.str,
    use_cases: typing.Sequence[builtins.str],
    aws_key_info: typing.Optional[typing.Union[MwsCustomerManagedKeysAwsKeyInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    creation_time: typing.Optional[jsii.Number] = None,
    customer_managed_key_id: typing.Optional[builtins.str] = None,
    gcp_key_info: typing.Optional[typing.Union[MwsCustomerManagedKeysGcpKeyInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce3da851d2ed2e626becd3c87f6d80b59ee057e84c75f0c8931aa77b73d7628b(
    *,
    kms_key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__935b0f54f3f28b41c8c483b85c4eb78e190a059168f5d134508017b2d8cfc1f0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d2597aa0df0cf052a16eef09aef83b1417964600a1533ddd6e77a5c6289392f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca5a7511bbb3f6cad3e55d5e4f1a3091cb39482b3fcac501974c15b34dfb5a31(
    value: typing.Optional[MwsCustomerManagedKeysGcpKeyInfo],
) -> None:
    """Type checking stubs"""
    pass
