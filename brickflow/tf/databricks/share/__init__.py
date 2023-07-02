'''
# `databricks_share`

Refer to the Terraform Registory for docs: [`databricks_share`](https://www.terraform.io/docs/providers/databricks/r/share).
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


class Share(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.share.Share",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/share databricks_share}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        created_at: typing.Optional[jsii.Number] = None,
        created_by: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        object: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ShareObject", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/share databricks_share} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#name Share#name}.
        :param created_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#created_at Share#created_at}.
        :param created_by: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#created_by Share#created_by}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#id Share#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param object: object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#object Share#object}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64dc31b5c3e5caaf441bf3a32e32982202f4da3606df8cae13ee778c74cb5a16)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ShareConfig(
            name=name,
            created_at=created_at,
            created_by=created_by,
            id=id,
            object=object,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putObject")
    def put_object(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ShareObject", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d0c17be4d111a2d74a21f237a08d9ae65f1cdd1d6bedfaf6a4c8c082247c5ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putObject", [value]))

    @jsii.member(jsii_name="resetCreatedAt")
    def reset_created_at(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreatedAt", []))

    @jsii.member(jsii_name="resetCreatedBy")
    def reset_created_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreatedBy", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetObject")
    def reset_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObject", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> "ShareObjectList":
        return typing.cast("ShareObjectList", jsii.get(self, "object"))

    @builtins.property
    @jsii.member(jsii_name="createdAtInput")
    def created_at_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "createdAtInput"))

    @builtins.property
    @jsii.member(jsii_name="createdByInput")
    def created_by_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createdByInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ShareObject"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ShareObject"]]], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "createdAt"))

    @created_at.setter
    def created_at(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ef5d0e8af1f5c0b42f973a3f82e7bef14616aac49397ba9df8b9578461cac29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createdAt", value)

    @builtins.property
    @jsii.member(jsii_name="createdBy")
    def created_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdBy"))

    @created_by.setter
    def created_by(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3725e683df9f3002145c6a56661f7fcee6b2d7922f771b2173ab8b09a9e019a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createdBy", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08922730d8e8c69d9c54791009147be466b66aa1308ff49d65b25cfc5da13b70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__534f9a5fd8e65a7f0463154a0b7c276700b58e99db3665d9deba2fa4c643c312)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="databricks.share.ShareConfig",
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
        "created_at": "createdAt",
        "created_by": "createdBy",
        "id": "id",
        "object": "object",
    },
)
class ShareConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        created_at: typing.Optional[jsii.Number] = None,
        created_by: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        object: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ShareObject", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#name Share#name}.
        :param created_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#created_at Share#created_at}.
        :param created_by: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#created_by Share#created_by}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#id Share#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param object: object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#object Share#object}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82ee147bff865a4517571eddf5e2ae2f7fa192ab94bc3512317df9b243bad826)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
            check_type(argname="argument created_by", value=created_by, expected_type=type_hints["created_by"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
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
        if created_at is not None:
            self._values["created_at"] = created_at
        if created_by is not None:
            self._values["created_by"] = created_by
        if id is not None:
            self._values["id"] = id
        if object is not None:
            self._values["object"] = object

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#name Share#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def created_at(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#created_at Share#created_at}.'''
        result = self._values.get("created_at")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def created_by(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#created_by Share#created_by}.'''
        result = self._values.get("created_by")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#id Share#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ShareObject"]]]:
        '''object block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#object Share#object}
        '''
        result = self._values.get("object")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ShareObject"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ShareConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.share.ShareObject",
    jsii_struct_bases=[],
    name_mapping={
        "data_object_type": "dataObjectType",
        "name": "name",
        "added_at": "addedAt",
        "added_by": "addedBy",
        "cdf_enabled": "cdfEnabled",
        "comment": "comment",
        "history_data_sharing_status": "historyDataSharingStatus",
        "partition": "partition",
        "shared_as": "sharedAs",
        "start_version": "startVersion",
        "status": "status",
    },
)
class ShareObject:
    def __init__(
        self,
        *,
        data_object_type: builtins.str,
        name: builtins.str,
        added_at: typing.Optional[jsii.Number] = None,
        added_by: typing.Optional[builtins.str] = None,
        cdf_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        comment: typing.Optional[builtins.str] = None,
        history_data_sharing_status: typing.Optional[builtins.str] = None,
        partition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ShareObjectPartition", typing.Dict[builtins.str, typing.Any]]]]] = None,
        shared_as: typing.Optional[builtins.str] = None,
        start_version: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param data_object_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#data_object_type Share#data_object_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#name Share#name}.
        :param added_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#added_at Share#added_at}.
        :param added_by: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#added_by Share#added_by}.
        :param cdf_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#cdf_enabled Share#cdf_enabled}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#comment Share#comment}.
        :param history_data_sharing_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#history_data_sharing_status Share#history_data_sharing_status}.
        :param partition: partition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#partition Share#partition}
        :param shared_as: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#shared_as Share#shared_as}.
        :param start_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#start_version Share#start_version}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#status Share#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90265af1d573c9b3ec2c2329e61cfbd25373c59c3f4646aa03180ec99ab7bcc3)
            check_type(argname="argument data_object_type", value=data_object_type, expected_type=type_hints["data_object_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument added_at", value=added_at, expected_type=type_hints["added_at"])
            check_type(argname="argument added_by", value=added_by, expected_type=type_hints["added_by"])
            check_type(argname="argument cdf_enabled", value=cdf_enabled, expected_type=type_hints["cdf_enabled"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument history_data_sharing_status", value=history_data_sharing_status, expected_type=type_hints["history_data_sharing_status"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument shared_as", value=shared_as, expected_type=type_hints["shared_as"])
            check_type(argname="argument start_version", value=start_version, expected_type=type_hints["start_version"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_object_type": data_object_type,
            "name": name,
        }
        if added_at is not None:
            self._values["added_at"] = added_at
        if added_by is not None:
            self._values["added_by"] = added_by
        if cdf_enabled is not None:
            self._values["cdf_enabled"] = cdf_enabled
        if comment is not None:
            self._values["comment"] = comment
        if history_data_sharing_status is not None:
            self._values["history_data_sharing_status"] = history_data_sharing_status
        if partition is not None:
            self._values["partition"] = partition
        if shared_as is not None:
            self._values["shared_as"] = shared_as
        if start_version is not None:
            self._values["start_version"] = start_version
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def data_object_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#data_object_type Share#data_object_type}.'''
        result = self._values.get("data_object_type")
        assert result is not None, "Required property 'data_object_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#name Share#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def added_at(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#added_at Share#added_at}.'''
        result = self._values.get("added_at")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def added_by(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#added_by Share#added_by}.'''
        result = self._values.get("added_by")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cdf_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#cdf_enabled Share#cdf_enabled}.'''
        result = self._values.get("cdf_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#comment Share#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def history_data_sharing_status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#history_data_sharing_status Share#history_data_sharing_status}.'''
        result = self._values.get("history_data_sharing_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ShareObjectPartition"]]]:
        '''partition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#partition Share#partition}
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ShareObjectPartition"]]], result)

    @builtins.property
    def shared_as(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#shared_as Share#shared_as}.'''
        result = self._values.get("shared_as")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_version(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#start_version Share#start_version}.'''
        result = self._values.get("start_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#status Share#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ShareObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ShareObjectList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.share.ShareObjectList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__079083b44c04bc5d1194046e8334307fb820ae9109ea98ec69dbb011bcc2ff20)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ShareObjectOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3a5b554dc79ec0ecae38a5b990e226bbe5065e0787343335a74eade2d705ba6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ShareObjectOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2554b8236b05696cc722ba3142115c67877a5717ce55b6819cde2b4195757f1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d8d81d29fb7f35ff7aa7fcc3a4875928b8a738991db271e445116db179841ee1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__77c90b0977c97c14a46626679228165f60745538f897d5e6c927a4eee798af39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ShareObject]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ShareObject]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ShareObject]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abe0878c08898dfcb7fed13691334d9d0d5f2a59ae716141d2d6358e8b109fce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ShareObjectOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.share.ShareObjectOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__253b108f73f04db773012abe4fa19cb38054738aaf21f7a393d7e69efb0f7621)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPartition")
    def put_partition(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ShareObjectPartition", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a4ed1e6f186a0a03e44b0e3ee71ee9d9d9b8ecb80c93cb2f7aa39e51b9b0d74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPartition", [value]))

    @jsii.member(jsii_name="resetAddedAt")
    def reset_added_at(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddedAt", []))

    @jsii.member(jsii_name="resetAddedBy")
    def reset_added_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddedBy", []))

    @jsii.member(jsii_name="resetCdfEnabled")
    def reset_cdf_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdfEnabled", []))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetHistoryDataSharingStatus")
    def reset_history_data_sharing_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHistoryDataSharingStatus", []))

    @jsii.member(jsii_name="resetPartition")
    def reset_partition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartition", []))

    @jsii.member(jsii_name="resetSharedAs")
    def reset_shared_as(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharedAs", []))

    @jsii.member(jsii_name="resetStartVersion")
    def reset_start_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartVersion", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> "ShareObjectPartitionList":
        return typing.cast("ShareObjectPartitionList", jsii.get(self, "partition"))

    @builtins.property
    @jsii.member(jsii_name="addedAtInput")
    def added_at_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "addedAtInput"))

    @builtins.property
    @jsii.member(jsii_name="addedByInput")
    def added_by_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addedByInput"))

    @builtins.property
    @jsii.member(jsii_name="cdfEnabledInput")
    def cdf_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "cdfEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="dataObjectTypeInput")
    def data_object_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataObjectTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="historyDataSharingStatusInput")
    def history_data_sharing_status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "historyDataSharingStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ShareObjectPartition"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ShareObjectPartition"]]], jsii.get(self, "partitionInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedAsInput")
    def shared_as_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sharedAsInput"))

    @builtins.property
    @jsii.member(jsii_name="startVersionInput")
    def start_version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="addedAt")
    def added_at(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "addedAt"))

    @added_at.setter
    def added_at(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5d7fb065cc68c043aa724166b6c2cdf680e8cad1fe71bbf985de611f16517e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addedAt", value)

    @builtins.property
    @jsii.member(jsii_name="addedBy")
    def added_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addedBy"))

    @added_by.setter
    def added_by(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baa479e78143c94b334bc84f719b4c693a3d779363b9a6c6e46b96dcabb9d049)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addedBy", value)

    @builtins.property
    @jsii.member(jsii_name="cdfEnabled")
    def cdf_enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "cdfEnabled"))

    @cdf_enabled.setter
    def cdf_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45bd119c70af397a3f519da9c1a4f3ad4eb3e88f53a53e6d25866030ea1e01c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdfEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9652db888f367bd2cc9334f52816daf09eb89a59985aa8bed0c2d3fbe1725bed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="dataObjectType")
    def data_object_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataObjectType"))

    @data_object_type.setter
    def data_object_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcfb919bbb356a88b48f3461a93c19e06aae76cf53c691f9a6af13b884fcaba4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataObjectType", value)

    @builtins.property
    @jsii.member(jsii_name="historyDataSharingStatus")
    def history_data_sharing_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "historyDataSharingStatus"))

    @history_data_sharing_status.setter
    def history_data_sharing_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0265dcf61789f2cdac175e215f54d88e2a69157919f6227aadc36c414bce53fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "historyDataSharingStatus", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__282eb429990fc46cb16a6d791766a0ebe88c48804df28202f9add32bdb965327)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sharedAs")
    def shared_as(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sharedAs"))

    @shared_as.setter
    def shared_as(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__170f4340fbabafe21244f9479bd42e59da0865bf44af3ee07fefe632e789ca5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedAs", value)

    @builtins.property
    @jsii.member(jsii_name="startVersion")
    def start_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startVersion"))

    @start_version.setter
    def start_version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8d749de208e069316a70dc730fcabed0bffb1b6be6079045f62ca8dc4185238)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startVersion", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e12f8c21c48f43d9e46b128eca7e78b968e0b15a294d944b3bbe9970cbb067c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ShareObject, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ShareObject, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ShareObject, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05ed646aa720b63c9e0c4db73ebb11e3540a13013bb3585d919bd212a4727715)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.share.ShareObjectPartition",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class ShareObjectPartition:
    def __init__(
        self,
        *,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ShareObjectPartitionValue", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#value Share#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3242caf8b9778e3403ee78e88046fad6790aa6f47ecc8491c7086ae6d0a16a81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ShareObjectPartitionValue"]]:
        '''value block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#value Share#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ShareObjectPartitionValue"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ShareObjectPartition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ShareObjectPartitionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.share.ShareObjectPartitionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a2f096cdc9c5f3cac147ee7cd8d977918d22074d9792bf1f9f96508e11b661b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ShareObjectPartitionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9725547a1637c2cf303354c75733e403d100f4c1b792948496fa300add8edfda)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ShareObjectPartitionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd3aaea361f77bb557088aa3b536584052550f1ecff1187d0a6f4373010b0ba1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ff38e3e9122ee0a31d0b23570d8ed5328392df4786f5a5b5af91f3d868a8caf2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__30a4705fcd71e3b02299cb2ccbaa13bb556c3e2b04b1df84cfb68314fe274214)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ShareObjectPartition]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ShareObjectPartition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ShareObjectPartition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__975f7fed022c5347578871deec8546fd73f159e04091582de9c66745c354a79e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ShareObjectPartitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.share.ShareObjectPartitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad194034e9043346ffe4db54a5a0945b302df49b27f4f3237f5305d3b6f347a9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putValue")
    def put_value(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ShareObjectPartitionValue", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7510e208260c913f763b36fbeb0f188b5fd8904f075dfb1ccb4823e1aa858722)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putValue", [value]))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> "ShareObjectPartitionValueList":
        return typing.cast("ShareObjectPartitionValueList", jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ShareObjectPartitionValue"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ShareObjectPartitionValue"]]], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ShareObjectPartition, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ShareObjectPartition, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ShareObjectPartition, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__581e33fc2bb061f6e641a51acfeaac4a4f59462ed82aa77edb003dd5eb335dfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.share.ShareObjectPartitionValue",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "op": "op",
        "recipient_property_key": "recipientPropertyKey",
        "value": "value",
    },
)
class ShareObjectPartitionValue:
    def __init__(
        self,
        *,
        name: builtins.str,
        op: builtins.str,
        recipient_property_key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#name Share#name}.
        :param op: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#op Share#op}.
        :param recipient_property_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#recipient_property_key Share#recipient_property_key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#value Share#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4c4fdd9843576f6ae97c90800c21716b540403bf38435011a57f231f6f3a56f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument op", value=op, expected_type=type_hints["op"])
            check_type(argname="argument recipient_property_key", value=recipient_property_key, expected_type=type_hints["recipient_property_key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "op": op,
        }
        if recipient_property_key is not None:
            self._values["recipient_property_key"] = recipient_property_key
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#name Share#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def op(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#op Share#op}.'''
        result = self._values.get("op")
        assert result is not None, "Required property 'op' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recipient_property_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#recipient_property_key Share#recipient_property_key}.'''
        result = self._values.get("recipient_property_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/share#value Share#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ShareObjectPartitionValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ShareObjectPartitionValueList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.share.ShareObjectPartitionValueList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__09fca9bf52dfd45e7a2a20b174d4dedbacef2366a1c9f694b545ca2a282a9f09)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ShareObjectPartitionValueOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34699fe43d79c71d0af6811048abe12c1f72c145e0cda6b843800ca17b159fad)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ShareObjectPartitionValueOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__112c9e19e146b8a381297d23267b3beed986776015cdff3943025e9e9ba49b42)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0782564c8980f4330efd6e464715fd919e4b3d99fa50fdebe9193cce6bf286d3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__24e922e1cc0072847469c86c53b29ef61a7e4111cf037c77b035c878078fe8b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ShareObjectPartitionValue]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ShareObjectPartitionValue]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ShareObjectPartitionValue]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0be0343bc9113aa57504c882637ea5d61f9e372b60d72a2a49bcd03e50544d53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ShareObjectPartitionValueOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.share.ShareObjectPartitionValueOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e03fdabf1be1e7e4461a087a176d60248fc9cc2f3eb7a9258dba0a037a1e2b93)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetRecipientPropertyKey")
    def reset_recipient_property_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecipientPropertyKey", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="opInput")
    def op_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "opInput"))

    @builtins.property
    @jsii.member(jsii_name="recipientPropertyKeyInput")
    def recipient_property_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recipientPropertyKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad30d131b6d6769341d8f25018d856732fce6ed13c83f1e30aa0d9b2c475338d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="op")
    def op(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "op"))

    @op.setter
    def op(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc698b43f97a10cf4f48c35870a8686597352b876499bdc6228cc403088dba32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "op", value)

    @builtins.property
    @jsii.member(jsii_name="recipientPropertyKey")
    def recipient_property_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recipientPropertyKey"))

    @recipient_property_key.setter
    def recipient_property_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffd8e3aeef24ffb1e02ef15c81720fcf2b7a4697cd3d871486be4805c27898c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recipientPropertyKey", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c7e34391cd839665e9662f61978d5cd99be5c15f1ad71eea4454b471e70aa5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ShareObjectPartitionValue, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ShareObjectPartitionValue, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ShareObjectPartitionValue, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9753e287ff20b4fa07c8f38207152da3febce7cb0f90dfbfb26345f798142466)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Share",
    "ShareConfig",
    "ShareObject",
    "ShareObjectList",
    "ShareObjectOutputReference",
    "ShareObjectPartition",
    "ShareObjectPartitionList",
    "ShareObjectPartitionOutputReference",
    "ShareObjectPartitionValue",
    "ShareObjectPartitionValueList",
    "ShareObjectPartitionValueOutputReference",
]

publication.publish()

def _typecheckingstub__64dc31b5c3e5caaf441bf3a32e32982202f4da3606df8cae13ee778c74cb5a16(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    created_at: typing.Optional[jsii.Number] = None,
    created_by: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    object: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ShareObject, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__5d0c17be4d111a2d74a21f237a08d9ae65f1cdd1d6bedfaf6a4c8c082247c5ef(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ShareObject, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ef5d0e8af1f5c0b42f973a3f82e7bef14616aac49397ba9df8b9578461cac29(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3725e683df9f3002145c6a56661f7fcee6b2d7922f771b2173ab8b09a9e019a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08922730d8e8c69d9c54791009147be466b66aa1308ff49d65b25cfc5da13b70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__534f9a5fd8e65a7f0463154a0b7c276700b58e99db3665d9deba2fa4c643c312(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82ee147bff865a4517571eddf5e2ae2f7fa192ab94bc3512317df9b243bad826(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    created_at: typing.Optional[jsii.Number] = None,
    created_by: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    object: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ShareObject, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90265af1d573c9b3ec2c2329e61cfbd25373c59c3f4646aa03180ec99ab7bcc3(
    *,
    data_object_type: builtins.str,
    name: builtins.str,
    added_at: typing.Optional[jsii.Number] = None,
    added_by: typing.Optional[builtins.str] = None,
    cdf_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    comment: typing.Optional[builtins.str] = None,
    history_data_sharing_status: typing.Optional[builtins.str] = None,
    partition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ShareObjectPartition, typing.Dict[builtins.str, typing.Any]]]]] = None,
    shared_as: typing.Optional[builtins.str] = None,
    start_version: typing.Optional[jsii.Number] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__079083b44c04bc5d1194046e8334307fb820ae9109ea98ec69dbb011bcc2ff20(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3a5b554dc79ec0ecae38a5b990e226bbe5065e0787343335a74eade2d705ba6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2554b8236b05696cc722ba3142115c67877a5717ce55b6819cde2b4195757f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8d81d29fb7f35ff7aa7fcc3a4875928b8a738991db271e445116db179841ee1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77c90b0977c97c14a46626679228165f60745538f897d5e6c927a4eee798af39(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abe0878c08898dfcb7fed13691334d9d0d5f2a59ae716141d2d6358e8b109fce(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ShareObject]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__253b108f73f04db773012abe4fa19cb38054738aaf21f7a393d7e69efb0f7621(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a4ed1e6f186a0a03e44b0e3ee71ee9d9d9b8ecb80c93cb2f7aa39e51b9b0d74(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ShareObjectPartition, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5d7fb065cc68c043aa724166b6c2cdf680e8cad1fe71bbf985de611f16517e6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baa479e78143c94b334bc84f719b4c693a3d779363b9a6c6e46b96dcabb9d049(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45bd119c70af397a3f519da9c1a4f3ad4eb3e88f53a53e6d25866030ea1e01c5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9652db888f367bd2cc9334f52816daf09eb89a59985aa8bed0c2d3fbe1725bed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcfb919bbb356a88b48f3461a93c19e06aae76cf53c691f9a6af13b884fcaba4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0265dcf61789f2cdac175e215f54d88e2a69157919f6227aadc36c414bce53fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__282eb429990fc46cb16a6d791766a0ebe88c48804df28202f9add32bdb965327(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__170f4340fbabafe21244f9479bd42e59da0865bf44af3ee07fefe632e789ca5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8d749de208e069316a70dc730fcabed0bffb1b6be6079045f62ca8dc4185238(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e12f8c21c48f43d9e46b128eca7e78b968e0b15a294d944b3bbe9970cbb067c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05ed646aa720b63c9e0c4db73ebb11e3540a13013bb3585d919bd212a4727715(
    value: typing.Optional[typing.Union[ShareObject, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3242caf8b9778e3403ee78e88046fad6790aa6f47ecc8491c7086ae6d0a16a81(
    *,
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ShareObjectPartitionValue, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a2f096cdc9c5f3cac147ee7cd8d977918d22074d9792bf1f9f96508e11b661b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9725547a1637c2cf303354c75733e403d100f4c1b792948496fa300add8edfda(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd3aaea361f77bb557088aa3b536584052550f1ecff1187d0a6f4373010b0ba1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff38e3e9122ee0a31d0b23570d8ed5328392df4786f5a5b5af91f3d868a8caf2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30a4705fcd71e3b02299cb2ccbaa13bb556c3e2b04b1df84cfb68314fe274214(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__975f7fed022c5347578871deec8546fd73f159e04091582de9c66745c354a79e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ShareObjectPartition]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad194034e9043346ffe4db54a5a0945b302df49b27f4f3237f5305d3b6f347a9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7510e208260c913f763b36fbeb0f188b5fd8904f075dfb1ccb4823e1aa858722(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ShareObjectPartitionValue, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__581e33fc2bb061f6e641a51acfeaac4a4f59462ed82aa77edb003dd5eb335dfe(
    value: typing.Optional[typing.Union[ShareObjectPartition, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4c4fdd9843576f6ae97c90800c21716b540403bf38435011a57f231f6f3a56f(
    *,
    name: builtins.str,
    op: builtins.str,
    recipient_property_key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09fca9bf52dfd45e7a2a20b174d4dedbacef2366a1c9f694b545ca2a282a9f09(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34699fe43d79c71d0af6811048abe12c1f72c145e0cda6b843800ca17b159fad(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__112c9e19e146b8a381297d23267b3beed986776015cdff3943025e9e9ba49b42(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0782564c8980f4330efd6e464715fd919e4b3d99fa50fdebe9193cce6bf286d3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24e922e1cc0072847469c86c53b29ef61a7e4111cf037c77b035c878078fe8b7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0be0343bc9113aa57504c882637ea5d61f9e372b60d72a2a49bcd03e50544d53(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ShareObjectPartitionValue]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e03fdabf1be1e7e4461a087a176d60248fc9cc2f3eb7a9258dba0a037a1e2b93(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad30d131b6d6769341d8f25018d856732fce6ed13c83f1e30aa0d9b2c475338d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc698b43f97a10cf4f48c35870a8686597352b876499bdc6228cc403088dba32(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffd8e3aeef24ffb1e02ef15c81720fcf2b7a4697cd3d871486be4805c27898c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c7e34391cd839665e9662f61978d5cd99be5c15f1ad71eea4454b471e70aa5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9753e287ff20b4fa07c8f38207152da3febce7cb0f90dfbfb26345f798142466(
    value: typing.Optional[typing.Union[ShareObjectPartitionValue, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
