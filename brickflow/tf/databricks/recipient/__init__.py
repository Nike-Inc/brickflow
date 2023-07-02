'''
# `databricks_recipient`

Refer to the Terraform Registory for docs: [`databricks_recipient`](https://www.terraform.io/docs/providers/databricks/r/recipient).
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


class Recipient(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.recipient.Recipient",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/recipient databricks_recipient}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        authentication_type: builtins.str,
        name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        data_recipient_global_metastore_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ip_access_list: typing.Optional[typing.Union["RecipientIpAccessList", typing.Dict[builtins.str, typing.Any]]] = None,
        sharing_code: typing.Optional[builtins.str] = None,
        tokens: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RecipientTokens", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/recipient databricks_recipient} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#authentication_type Recipient#authentication_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#name Recipient#name}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#comment Recipient#comment}.
        :param data_recipient_global_metastore_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#data_recipient_global_metastore_id Recipient#data_recipient_global_metastore_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#id Recipient#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_access_list: ip_access_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#ip_access_list Recipient#ip_access_list}
        :param sharing_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#sharing_code Recipient#sharing_code}.
        :param tokens: tokens block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#tokens Recipient#tokens}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5c114e51e6626404f210b9ed592f8911b08ee8ea29325acbd6e6b3c98c88fb8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RecipientConfig(
            authentication_type=authentication_type,
            name=name,
            comment=comment,
            data_recipient_global_metastore_id=data_recipient_global_metastore_id,
            id=id,
            ip_access_list=ip_access_list,
            sharing_code=sharing_code,
            tokens=tokens,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putIpAccessList")
    def put_ip_access_list(
        self,
        *,
        allowed_ip_addresses: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param allowed_ip_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#allowed_ip_addresses Recipient#allowed_ip_addresses}.
        '''
        value = RecipientIpAccessList(allowed_ip_addresses=allowed_ip_addresses)

        return typing.cast(None, jsii.invoke(self, "putIpAccessList", [value]))

    @jsii.member(jsii_name="putTokens")
    def put_tokens(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RecipientTokens", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c239c577caa562680ee0cb615271c17ac9557d7f706ede12166843b3c904647)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTokens", [value]))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetDataRecipientGlobalMetastoreId")
    def reset_data_recipient_global_metastore_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataRecipientGlobalMetastoreId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpAccessList")
    def reset_ip_access_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAccessList", []))

    @jsii.member(jsii_name="resetSharingCode")
    def reset_sharing_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharingCode", []))

    @jsii.member(jsii_name="resetTokens")
    def reset_tokens(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokens", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="ipAccessList")
    def ip_access_list(self) -> "RecipientIpAccessListOutputReference":
        return typing.cast("RecipientIpAccessListOutputReference", jsii.get(self, "ipAccessList"))

    @builtins.property
    @jsii.member(jsii_name="tokens")
    def tokens(self) -> "RecipientTokensList":
        return typing.cast("RecipientTokensList", jsii.get(self, "tokens"))

    @builtins.property
    @jsii.member(jsii_name="authenticationTypeInput")
    def authentication_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="dataRecipientGlobalMetastoreIdInput")
    def data_recipient_global_metastore_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataRecipientGlobalMetastoreIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAccessListInput")
    def ip_access_list_input(self) -> typing.Optional["RecipientIpAccessList"]:
        return typing.cast(typing.Optional["RecipientIpAccessList"], jsii.get(self, "ipAccessListInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sharingCodeInput")
    def sharing_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sharingCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="tokensInput")
    def tokens_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RecipientTokens"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RecipientTokens"]]], jsii.get(self, "tokensInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__453ac45f5c4cb4f2023c508d625c1099d6e6b0ab65fe47d31e7eba9412df8155)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12cf1713b111fe745f8169cd467b5f668d052e8d32f911c7a30afda92ca2d758)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="dataRecipientGlobalMetastoreId")
    def data_recipient_global_metastore_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataRecipientGlobalMetastoreId"))

    @data_recipient_global_metastore_id.setter
    def data_recipient_global_metastore_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad5159a60f38de7ed17fab197103818108002372eb8ad443a4cef8902a823524)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataRecipientGlobalMetastoreId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dcd29dea8d47deb9fb0172f1d852fc83ab0abf604911ff0dfa8b035e45b0ec2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9d96378bfa0bf190e1db0151eaec563d55112a9ae1d3bd286be9999b4fbfd28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sharingCode")
    def sharing_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sharingCode"))

    @sharing_code.setter
    def sharing_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c5b880ffcdce64b488092baebaed0a89799d68294246d4c89e82c21ee39e4b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharingCode", value)


@jsii.data_type(
    jsii_type="databricks.recipient.RecipientConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "authentication_type": "authenticationType",
        "name": "name",
        "comment": "comment",
        "data_recipient_global_metastore_id": "dataRecipientGlobalMetastoreId",
        "id": "id",
        "ip_access_list": "ipAccessList",
        "sharing_code": "sharingCode",
        "tokens": "tokens",
    },
)
class RecipientConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        authentication_type: builtins.str,
        name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        data_recipient_global_metastore_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ip_access_list: typing.Optional[typing.Union["RecipientIpAccessList", typing.Dict[builtins.str, typing.Any]]] = None,
        sharing_code: typing.Optional[builtins.str] = None,
        tokens: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RecipientTokens", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param authentication_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#authentication_type Recipient#authentication_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#name Recipient#name}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#comment Recipient#comment}.
        :param data_recipient_global_metastore_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#data_recipient_global_metastore_id Recipient#data_recipient_global_metastore_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#id Recipient#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_access_list: ip_access_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#ip_access_list Recipient#ip_access_list}
        :param sharing_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#sharing_code Recipient#sharing_code}.
        :param tokens: tokens block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#tokens Recipient#tokens}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(ip_access_list, dict):
            ip_access_list = RecipientIpAccessList(**ip_access_list)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cfe1ba0caf62223971cd79337da5d365fab84351006bc568defb3f5e67e841a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument data_recipient_global_metastore_id", value=data_recipient_global_metastore_id, expected_type=type_hints["data_recipient_global_metastore_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_access_list", value=ip_access_list, expected_type=type_hints["ip_access_list"])
            check_type(argname="argument sharing_code", value=sharing_code, expected_type=type_hints["sharing_code"])
            check_type(argname="argument tokens", value=tokens, expected_type=type_hints["tokens"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authentication_type": authentication_type,
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
        if comment is not None:
            self._values["comment"] = comment
        if data_recipient_global_metastore_id is not None:
            self._values["data_recipient_global_metastore_id"] = data_recipient_global_metastore_id
        if id is not None:
            self._values["id"] = id
        if ip_access_list is not None:
            self._values["ip_access_list"] = ip_access_list
        if sharing_code is not None:
            self._values["sharing_code"] = sharing_code
        if tokens is not None:
            self._values["tokens"] = tokens

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
    def authentication_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#authentication_type Recipient#authentication_type}.'''
        result = self._values.get("authentication_type")
        assert result is not None, "Required property 'authentication_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#name Recipient#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#comment Recipient#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_recipient_global_metastore_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#data_recipient_global_metastore_id Recipient#data_recipient_global_metastore_id}.'''
        result = self._values.get("data_recipient_global_metastore_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#id Recipient#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_access_list(self) -> typing.Optional["RecipientIpAccessList"]:
        '''ip_access_list block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#ip_access_list Recipient#ip_access_list}
        '''
        result = self._values.get("ip_access_list")
        return typing.cast(typing.Optional["RecipientIpAccessList"], result)

    @builtins.property
    def sharing_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#sharing_code Recipient#sharing_code}.'''
        result = self._values.get("sharing_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tokens(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RecipientTokens"]]]:
        '''tokens block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#tokens Recipient#tokens}
        '''
        result = self._values.get("tokens")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RecipientTokens"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecipientConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.recipient.RecipientIpAccessList",
    jsii_struct_bases=[],
    name_mapping={"allowed_ip_addresses": "allowedIpAddresses"},
)
class RecipientIpAccessList:
    def __init__(self, *, allowed_ip_addresses: typing.Sequence[builtins.str]) -> None:
        '''
        :param allowed_ip_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#allowed_ip_addresses Recipient#allowed_ip_addresses}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76717d68ab58c13f35e57bd673e3538a10bffffa54ed04b16d59fb0728019b95)
            check_type(argname="argument allowed_ip_addresses", value=allowed_ip_addresses, expected_type=type_hints["allowed_ip_addresses"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allowed_ip_addresses": allowed_ip_addresses,
        }

    @builtins.property
    def allowed_ip_addresses(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#allowed_ip_addresses Recipient#allowed_ip_addresses}.'''
        result = self._values.get("allowed_ip_addresses")
        assert result is not None, "Required property 'allowed_ip_addresses' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecipientIpAccessList(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RecipientIpAccessListOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.recipient.RecipientIpAccessListOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__19168ccc2012836cd3d727a3ff07453dad46cf199c39c509a98a82247e7f0d33)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="allowedIpAddressesInput")
    def allowed_ip_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedIpAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedIpAddresses")
    def allowed_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedIpAddresses"))

    @allowed_ip_addresses.setter
    def allowed_ip_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c96059b96dd8dc9e142a4c0abd12eedbf3baad46f6b5d288249afab38dfad60a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedIpAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RecipientIpAccessList]:
        return typing.cast(typing.Optional[RecipientIpAccessList], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RecipientIpAccessList]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcbf8ee494fba3ca5373c938d035082b5d49059d40e2f970c081fdcd4ea7ff82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.recipient.RecipientTokens",
    jsii_struct_bases=[],
    name_mapping={
        "activation_url": "activationUrl",
        "created_at": "createdAt",
        "created_by": "createdBy",
        "expiration_time": "expirationTime",
        "id": "id",
        "updated_at": "updatedAt",
        "updated_by": "updatedBy",
    },
)
class RecipientTokens:
    def __init__(
        self,
        *,
        activation_url: typing.Optional[builtins.str] = None,
        created_at: typing.Optional[jsii.Number] = None,
        created_by: typing.Optional[builtins.str] = None,
        expiration_time: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        updated_at: typing.Optional[jsii.Number] = None,
        updated_by: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param activation_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#activation_url Recipient#activation_url}.
        :param created_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#created_at Recipient#created_at}.
        :param created_by: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#created_by Recipient#created_by}.
        :param expiration_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#expiration_time Recipient#expiration_time}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#id Recipient#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param updated_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#updated_at Recipient#updated_at}.
        :param updated_by: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#updated_by Recipient#updated_by}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d1e25d5a6f8ddf7e2b0f7a3f807582abff178fdcc4ed8df2238ca3658e3ec7a)
            check_type(argname="argument activation_url", value=activation_url, expected_type=type_hints["activation_url"])
            check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
            check_type(argname="argument created_by", value=created_by, expected_type=type_hints["created_by"])
            check_type(argname="argument expiration_time", value=expiration_time, expected_type=type_hints["expiration_time"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument updated_at", value=updated_at, expected_type=type_hints["updated_at"])
            check_type(argname="argument updated_by", value=updated_by, expected_type=type_hints["updated_by"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if activation_url is not None:
            self._values["activation_url"] = activation_url
        if created_at is not None:
            self._values["created_at"] = created_at
        if created_by is not None:
            self._values["created_by"] = created_by
        if expiration_time is not None:
            self._values["expiration_time"] = expiration_time
        if id is not None:
            self._values["id"] = id
        if updated_at is not None:
            self._values["updated_at"] = updated_at
        if updated_by is not None:
            self._values["updated_by"] = updated_by

    @builtins.property
    def activation_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#activation_url Recipient#activation_url}.'''
        result = self._values.get("activation_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def created_at(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#created_at Recipient#created_at}.'''
        result = self._values.get("created_at")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def created_by(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#created_by Recipient#created_by}.'''
        result = self._values.get("created_by")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expiration_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#expiration_time Recipient#expiration_time}.'''
        result = self._values.get("expiration_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#id Recipient#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def updated_at(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#updated_at Recipient#updated_at}.'''
        result = self._values.get("updated_at")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def updated_by(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/recipient#updated_by Recipient#updated_by}.'''
        result = self._values.get("updated_by")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecipientTokens(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RecipientTokensList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.recipient.RecipientTokensList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d720e9e33ce38b8dd5a7d04e59fd95e1cfee5b62cf22a69330d6fdb1b108f129)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "RecipientTokensOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93ef757118c0209b8d658a0911dbdbd495b86cb4a9fe9b17f52a1d9102f501b7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RecipientTokensOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d1d444b12823aea1aec5ee32976a27f1a4557befd5d43197267ea94b1cbf457)
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
            type_hints = typing.get_type_hints(_typecheckingstub__91b86a489917c608f844bb4f036d836dd0ff88a997104f25fef70c5d393e00c5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ee6c11e86bb0c0bbd55ddf5838e200e9668f9ba2fbf4fa9cd551c8bb1f9b499d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RecipientTokens]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RecipientTokens]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RecipientTokens]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3506b522cacc4e3f36c23200330df08e8a4d2f1a95eead149b38e0baa005b4f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RecipientTokensOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.recipient.RecipientTokensOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__12c8ff266f201311649d20f22744ae8f6a8694e001099d35b89c0a2579a87b61)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetActivationUrl")
    def reset_activation_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivationUrl", []))

    @jsii.member(jsii_name="resetCreatedAt")
    def reset_created_at(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreatedAt", []))

    @jsii.member(jsii_name="resetCreatedBy")
    def reset_created_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreatedBy", []))

    @jsii.member(jsii_name="resetExpirationTime")
    def reset_expiration_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpirationTime", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetUpdatedAt")
    def reset_updated_at(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdatedAt", []))

    @jsii.member(jsii_name="resetUpdatedBy")
    def reset_updated_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdatedBy", []))

    @builtins.property
    @jsii.member(jsii_name="activationUrlInput")
    def activation_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activationUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="createdAtInput")
    def created_at_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "createdAtInput"))

    @builtins.property
    @jsii.member(jsii_name="createdByInput")
    def created_by_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createdByInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationTimeInput")
    def expiration_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expirationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="updatedAtInput")
    def updated_at_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "updatedAtInput"))

    @builtins.property
    @jsii.member(jsii_name="updatedByInput")
    def updated_by_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updatedByInput"))

    @builtins.property
    @jsii.member(jsii_name="activationUrl")
    def activation_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activationUrl"))

    @activation_url.setter
    def activation_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25dd94da88442f09dcd0fcb214175fc40ec2f78355ec6a56d4400c9648ee319e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activationUrl", value)

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "createdAt"))

    @created_at.setter
    def created_at(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae0801a49f49e089ccc7038de18ad4ab0c5f1302f89702572de0647a3c0fd675)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createdAt", value)

    @builtins.property
    @jsii.member(jsii_name="createdBy")
    def created_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdBy"))

    @created_by.setter
    def created_by(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d69c9e641563ede7a67b17dfb15bf59e389caf64e9b4bf43cf16a347162daf7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createdBy", value)

    @builtins.property
    @jsii.member(jsii_name="expirationTime")
    def expiration_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "expirationTime"))

    @expiration_time.setter
    def expiration_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a971f22e9ee754153f4dba1cd11e66614c21df0b57cbb21121a66f8940d5ba6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationTime", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecb18ac70485a04bcd56fdf47dcbcdba979a2f7f50d2dc2d787f567e907ce83e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "updatedAt"))

    @updated_at.setter
    def updated_at(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b23aad20e9306c174c8771580376675c37f588f8d0f382fc689335114da1769)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updatedAt", value)

    @builtins.property
    @jsii.member(jsii_name="updatedBy")
    def updated_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedBy"))

    @updated_by.setter
    def updated_by(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c1688449ad7582205269d2a6b38373a02cfa284dec0b5f5b3e66891acbc84f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updatedBy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RecipientTokens, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RecipientTokens, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RecipientTokens, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0582234928fab4e64d06eb5932edb8afc3edc8931144e9a5cddc5fbd674badf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Recipient",
    "RecipientConfig",
    "RecipientIpAccessList",
    "RecipientIpAccessListOutputReference",
    "RecipientTokens",
    "RecipientTokensList",
    "RecipientTokensOutputReference",
]

publication.publish()

def _typecheckingstub__f5c114e51e6626404f210b9ed592f8911b08ee8ea29325acbd6e6b3c98c88fb8(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    authentication_type: builtins.str,
    name: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    data_recipient_global_metastore_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ip_access_list: typing.Optional[typing.Union[RecipientIpAccessList, typing.Dict[builtins.str, typing.Any]]] = None,
    sharing_code: typing.Optional[builtins.str] = None,
    tokens: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RecipientTokens, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__7c239c577caa562680ee0cb615271c17ac9557d7f706ede12166843b3c904647(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RecipientTokens, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__453ac45f5c4cb4f2023c508d625c1099d6e6b0ab65fe47d31e7eba9412df8155(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12cf1713b111fe745f8169cd467b5f668d052e8d32f911c7a30afda92ca2d758(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad5159a60f38de7ed17fab197103818108002372eb8ad443a4cef8902a823524(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dcd29dea8d47deb9fb0172f1d852fc83ab0abf604911ff0dfa8b035e45b0ec2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9d96378bfa0bf190e1db0151eaec563d55112a9ae1d3bd286be9999b4fbfd28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c5b880ffcdce64b488092baebaed0a89799d68294246d4c89e82c21ee39e4b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cfe1ba0caf62223971cd79337da5d365fab84351006bc568defb3f5e67e841a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    authentication_type: builtins.str,
    name: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    data_recipient_global_metastore_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ip_access_list: typing.Optional[typing.Union[RecipientIpAccessList, typing.Dict[builtins.str, typing.Any]]] = None,
    sharing_code: typing.Optional[builtins.str] = None,
    tokens: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RecipientTokens, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76717d68ab58c13f35e57bd673e3538a10bffffa54ed04b16d59fb0728019b95(
    *,
    allowed_ip_addresses: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19168ccc2012836cd3d727a3ff07453dad46cf199c39c509a98a82247e7f0d33(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c96059b96dd8dc9e142a4c0abd12eedbf3baad46f6b5d288249afab38dfad60a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcbf8ee494fba3ca5373c938d035082b5d49059d40e2f970c081fdcd4ea7ff82(
    value: typing.Optional[RecipientIpAccessList],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d1e25d5a6f8ddf7e2b0f7a3f807582abff178fdcc4ed8df2238ca3658e3ec7a(
    *,
    activation_url: typing.Optional[builtins.str] = None,
    created_at: typing.Optional[jsii.Number] = None,
    created_by: typing.Optional[builtins.str] = None,
    expiration_time: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    updated_at: typing.Optional[jsii.Number] = None,
    updated_by: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d720e9e33ce38b8dd5a7d04e59fd95e1cfee5b62cf22a69330d6fdb1b108f129(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93ef757118c0209b8d658a0911dbdbd495b86cb4a9fe9b17f52a1d9102f501b7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d1d444b12823aea1aec5ee32976a27f1a4557befd5d43197267ea94b1cbf457(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91b86a489917c608f844bb4f036d836dd0ff88a997104f25fef70c5d393e00c5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee6c11e86bb0c0bbd55ddf5838e200e9668f9ba2fbf4fa9cd551c8bb1f9b499d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3506b522cacc4e3f36c23200330df08e8a4d2f1a95eead149b38e0baa005b4f1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RecipientTokens]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12c8ff266f201311649d20f22744ae8f6a8694e001099d35b89c0a2579a87b61(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25dd94da88442f09dcd0fcb214175fc40ec2f78355ec6a56d4400c9648ee319e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae0801a49f49e089ccc7038de18ad4ab0c5f1302f89702572de0647a3c0fd675(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d69c9e641563ede7a67b17dfb15bf59e389caf64e9b4bf43cf16a347162daf7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a971f22e9ee754153f4dba1cd11e66614c21df0b57cbb21121a66f8940d5ba6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecb18ac70485a04bcd56fdf47dcbcdba979a2f7f50d2dc2d787f567e907ce83e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b23aad20e9306c174c8771580376675c37f588f8d0f382fc689335114da1769(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c1688449ad7582205269d2a6b38373a02cfa284dec0b5f5b3e66891acbc84f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0582234928fab4e64d06eb5932edb8afc3edc8931144e9a5cddc5fbd674badf6(
    value: typing.Optional[typing.Union[RecipientTokens, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
