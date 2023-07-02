'''
# `data_databricks_share`

Refer to the Terraform Registory for docs: [`data_databricks_share`](https://www.terraform.io/docs/providers/databricks/d/share).
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


class DataDatabricksShare(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksShare.DataDatabricksShare",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/d/share databricks_share}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        created_at: typing.Optional[jsii.Number] = None,
        created_by: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        object: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksShareObject", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/d/share databricks_share} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param created_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#created_at DataDatabricksShare#created_at}.
        :param created_by: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#created_by DataDatabricksShare#created_by}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#id DataDatabricksShare#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#name DataDatabricksShare#name}.
        :param object: object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#object DataDatabricksShare#object}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97201639fbba9d17978a271d8fa98e4ff011b64fcdd86301dbe17a54074e5ecb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataDatabricksShareConfig(
            created_at=created_at,
            created_by=created_by,
            id=id,
            name=name,
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
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksShareObject", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfce56214ebfe769c610ae57b649aaf3f7adb680a9658e8e331c5670299768cf)
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

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

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
    def object(self) -> "DataDatabricksShareObjectList":
        return typing.cast("DataDatabricksShareObjectList", jsii.get(self, "object"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksShareObject"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksShareObject"]]], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "createdAt"))

    @created_at.setter
    def created_at(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f97249349d653784e22cbd5125667592f235da245f93ab2a5d00ae622fc21b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createdAt", value)

    @builtins.property
    @jsii.member(jsii_name="createdBy")
    def created_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdBy"))

    @created_by.setter
    def created_by(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b67b49ed9f3fa55d469e190329a7da440f0f56aa9830b1814b960f06ab2b8b89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createdBy", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__025c411c1c1525bd22729a9b174e6408f18731881796f3fe7e10d2f32e737928)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__581651731b1964a6ec7cc1a2302b0fe6110fc7b6f3039ba0e0e84da971df8753)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksShare.DataDatabricksShareConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "created_at": "createdAt",
        "created_by": "createdBy",
        "id": "id",
        "name": "name",
        "object": "object",
    },
)
class DataDatabricksShareConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        created_at: typing.Optional[jsii.Number] = None,
        created_by: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        object: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksShareObject", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param created_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#created_at DataDatabricksShare#created_at}.
        :param created_by: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#created_by DataDatabricksShare#created_by}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#id DataDatabricksShare#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#name DataDatabricksShare#name}.
        :param object: object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#object DataDatabricksShare#object}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4b2c5924ccd7840bc2a69963671b9e4c34f8da5716a005dcf6f49ff42462ecc)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
            check_type(argname="argument created_by", value=created_by, expected_type=type_hints["created_by"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
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
        if created_at is not None:
            self._values["created_at"] = created_at
        if created_by is not None:
            self._values["created_by"] = created_by
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
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
    def created_at(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#created_at DataDatabricksShare#created_at}.'''
        result = self._values.get("created_at")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def created_by(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#created_by DataDatabricksShare#created_by}.'''
        result = self._values.get("created_by")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#id DataDatabricksShare#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#name DataDatabricksShare#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksShareObject"]]]:
        '''object block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#object DataDatabricksShare#object}
        '''
        result = self._values.get("object")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksShareObject"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksShareConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.dataDatabricksShare.DataDatabricksShareObject",
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
class DataDatabricksShareObject:
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
        partition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksShareObjectPartition", typing.Dict[builtins.str, typing.Any]]]]] = None,
        shared_as: typing.Optional[builtins.str] = None,
        start_version: typing.Optional[jsii.Number] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param data_object_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#data_object_type DataDatabricksShare#data_object_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#name DataDatabricksShare#name}.
        :param added_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#added_at DataDatabricksShare#added_at}.
        :param added_by: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#added_by DataDatabricksShare#added_by}.
        :param cdf_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#cdf_enabled DataDatabricksShare#cdf_enabled}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#comment DataDatabricksShare#comment}.
        :param history_data_sharing_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#history_data_sharing_status DataDatabricksShare#history_data_sharing_status}.
        :param partition: partition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#partition DataDatabricksShare#partition}
        :param shared_as: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#shared_as DataDatabricksShare#shared_as}.
        :param start_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#start_version DataDatabricksShare#start_version}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#status DataDatabricksShare#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f91529bbea0507690e63c469eabb56392465f8f0f56b293453142cef30851f02)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#data_object_type DataDatabricksShare#data_object_type}.'''
        result = self._values.get("data_object_type")
        assert result is not None, "Required property 'data_object_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#name DataDatabricksShare#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def added_at(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#added_at DataDatabricksShare#added_at}.'''
        result = self._values.get("added_at")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def added_by(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#added_by DataDatabricksShare#added_by}.'''
        result = self._values.get("added_by")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cdf_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#cdf_enabled DataDatabricksShare#cdf_enabled}.'''
        result = self._values.get("cdf_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#comment DataDatabricksShare#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def history_data_sharing_status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#history_data_sharing_status DataDatabricksShare#history_data_sharing_status}.'''
        result = self._values.get("history_data_sharing_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksShareObjectPartition"]]]:
        '''partition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#partition DataDatabricksShare#partition}
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksShareObjectPartition"]]], result)

    @builtins.property
    def shared_as(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#shared_as DataDatabricksShare#shared_as}.'''
        result = self._values.get("shared_as")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_version(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#start_version DataDatabricksShare#start_version}.'''
        result = self._values.get("start_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#status DataDatabricksShare#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksShareObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksShareObjectList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksShare.DataDatabricksShareObjectList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__07e05a79c9a044e4fccaa174ebf2d40b1945cb5edfa68c566c4f30b8e6027738)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataDatabricksShareObjectOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__667ff6fdbb158b0eef99df507d400ba88523d136fec29f87070ef435958257d4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataDatabricksShareObjectOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bdd49edb97de8e7862086bf386756990d20ca5d0706c3f074ae2c64a9895ac6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4969ce055300e2f575ceb89c143ee711869aba04a7b4b2294b18c9018ce1e1b6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f59b1b9bfd80cafb38123b258f90c003d5eb38b676474c6c94372793881ed68b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksShareObject]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksShareObject]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksShareObject]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3758fc47d153cc7bc46cabbbfd3389c1bbe4282ceb16580b7a7052a4891ead85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksShareObjectOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksShare.DataDatabricksShareObjectOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c4a277758d73eba3d97be3e1c66613758d5deddb5a105bdab72ab32c4e2ab1a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPartition")
    def put_partition(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksShareObjectPartition", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63d3987235bcd7315ebb98d3f558c04d2e9a8ee36ad0b550fb9d00d9989aa6ce)
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
    def partition(self) -> "DataDatabricksShareObjectPartitionList":
        return typing.cast("DataDatabricksShareObjectPartitionList", jsii.get(self, "partition"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksShareObjectPartition"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksShareObjectPartition"]]], jsii.get(self, "partitionInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__f0ff7e25a51bc5ea38b3668b366ee350d5241f9db4e3cfd86d127a610f13c5ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addedAt", value)

    @builtins.property
    @jsii.member(jsii_name="addedBy")
    def added_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "addedBy"))

    @added_by.setter
    def added_by(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efa00062d4c6c421c5ed1067e2e2e65d450e82cc46bf3f0cee64924abba96ee6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1d48fd26de9dd3157c7ba1d102fba45418aedd994cc63e1408c5f84b0fa6a4c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdfEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71696061ab64512d30d128c95c6f287e4361434446d7a875f65a1ca8124ec53c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="dataObjectType")
    def data_object_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataObjectType"))

    @data_object_type.setter
    def data_object_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1528ea4af4edc29ed8343317fa0a22a4f2c20027c74edf3f730f4ff5e2c35716)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataObjectType", value)

    @builtins.property
    @jsii.member(jsii_name="historyDataSharingStatus")
    def history_data_sharing_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "historyDataSharingStatus"))

    @history_data_sharing_status.setter
    def history_data_sharing_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a2c73304c5f708f49df830e0f10c6fedae288191d7d5849406891491abf18e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "historyDataSharingStatus", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73d5d56ebf01623cb280fd0ee23bed78ac1423f053e99606e7cbeaa9043df09d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sharedAs")
    def shared_as(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sharedAs"))

    @shared_as.setter
    def shared_as(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3439a0fa0edeaeb84d71f6b1c0988778f9b93aaeb4f67ef099ef3787dd929e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedAs", value)

    @builtins.property
    @jsii.member(jsii_name="startVersion")
    def start_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startVersion"))

    @start_version.setter
    def start_version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fac7259bfad64c23bb479d6a4f38efa7dfcc8a448d743b63ecf572e45b617a96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startVersion", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ae628dfdb30568937c19eb1dbf2a7df864320eb603cdf031eed4035866e8e58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataDatabricksShareObject, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataDatabricksShareObject, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataDatabricksShareObject, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d629e3d3c1b6e297a341eb59e9452c2e4be3feb41861f5e639f60f5891fe97f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksShare.DataDatabricksShareObjectPartition",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class DataDatabricksShareObjectPartition:
    def __init__(
        self,
        *,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksShareObjectPartitionValue", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#value DataDatabricksShare#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4e151e3293cc197bd1c217444f4a4567b09ed2cc9b729e0fc289ef54323cede)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksShareObjectPartitionValue"]]:
        '''value block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#value DataDatabricksShare#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksShareObjectPartitionValue"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksShareObjectPartition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksShareObjectPartitionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksShare.DataDatabricksShareObjectPartitionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e3c186ebf6accd72ff33106aba5d59bcecd72eb9b7c6fd3e49a9ec7115adcee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDatabricksShareObjectPartitionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a83d0a20841bfd48bf91be0beaa481848f9b3ae1ef595ef0f55fed40b887d91f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataDatabricksShareObjectPartitionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf7022be0f1a8f89949268b56b08a756f535f1628668377181a073e30ee7027c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b47bdf2eda40be57c52f1537e375de3ac48c47d6055442d67c34293fd906b27f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__acf8ecdd5dc4f58f1f2f3cd85ab70bc80a2f71c70405cb8fcdae0b82a4432919)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksShareObjectPartition]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksShareObjectPartition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksShareObjectPartition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__114c9091792344f8da5b357b97af387489daf7cfc5012544932d18ab001e9cd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksShareObjectPartitionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksShare.DataDatabricksShareObjectPartitionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5dd254aa67968886a3f69c6ed306ebde5e7a89865b2f99e88523ace3f507d811)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putValue")
    def put_value(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataDatabricksShareObjectPartitionValue", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e73ff64f6157528069ba9c75718ae79e68064065cd7db485d3441220f5695c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putValue", [value]))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> "DataDatabricksShareObjectPartitionValueList":
        return typing.cast("DataDatabricksShareObjectPartitionValueList", jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksShareObjectPartitionValue"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataDatabricksShareObjectPartitionValue"]]], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataDatabricksShareObjectPartition, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataDatabricksShareObjectPartition, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataDatabricksShareObjectPartition, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9aa23d8a1d674a95535e7bfd178840fd0f5249e1164aab2881e1239240931bd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksShare.DataDatabricksShareObjectPartitionValue",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "op": "op",
        "recipient_property_key": "recipientPropertyKey",
        "value": "value",
    },
)
class DataDatabricksShareObjectPartitionValue:
    def __init__(
        self,
        *,
        name: builtins.str,
        op: builtins.str,
        recipient_property_key: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#name DataDatabricksShare#name}.
        :param op: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#op DataDatabricksShare#op}.
        :param recipient_property_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#recipient_property_key DataDatabricksShare#recipient_property_key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#value DataDatabricksShare#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8ba3b8398ae4be17fefaf39a268a1d6a85b143cf22cdf4f4ff74c75a466f225)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#name DataDatabricksShare#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def op(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#op DataDatabricksShare#op}.'''
        result = self._values.get("op")
        assert result is not None, "Required property 'op' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recipient_property_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#recipient_property_key DataDatabricksShare#recipient_property_key}.'''
        result = self._values.get("recipient_property_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/share#value DataDatabricksShare#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksShareObjectPartitionValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataDatabricksShareObjectPartitionValueList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksShare.DataDatabricksShareObjectPartitionValueList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad37ebee3b648c4d3db195cd8a2d1ee3f54e606f204f37231cb7fefb33d21ec1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataDatabricksShareObjectPartitionValueOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__803d443c33d6b6f333a35a98ce32f72755c29074cd57eb763aa0d9fcd501b983)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataDatabricksShareObjectPartitionValueOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddb501c2f739d8d3fdb504919f136d910f0c1276a3ac3d11531cd000347ad1b0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b954bd48c193c8ee585bbb0bb98917f7585d6ccd8085f487fd20dd3799230e75)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d80b43b7e7dc23219166c870e13062d718840bb1ae01af38ae8888d13ce947ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksShareObjectPartitionValue]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksShareObjectPartitionValue]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksShareObjectPartitionValue]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5985250c649dc1bdf3bb32655c130b6185a9f69c6c717be8a6a482e65b5ad760)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataDatabricksShareObjectPartitionValueOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksShare.DataDatabricksShareObjectPartitionValueOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e739389003b88dcc72024a0caacec68bba3702f046b2dfc3dc41ef9b54dc9b34)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ffa8ef130435bda7394690f35d345f6940955415aa9d42bf943db0d1129542c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="op")
    def op(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "op"))

    @op.setter
    def op(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f14bb1622fa37903e0be35abb21b0b2c3018884c6b3118f1ad56daa2a03e32f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "op", value)

    @builtins.property
    @jsii.member(jsii_name="recipientPropertyKey")
    def recipient_property_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recipientPropertyKey"))

    @recipient_property_key.setter
    def recipient_property_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bcee2e0cab7c48540d4c4378087ca59d2d0615ac6b8266c7c5d93291833dcab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recipientPropertyKey", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78fa16f739b03c9cf6f8919de80620b4e2c9261271c2ce12088dc45463713fb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataDatabricksShareObjectPartitionValue, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataDatabricksShareObjectPartitionValue, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataDatabricksShareObjectPartitionValue, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2e3418f856afd1247970102ef10105eb2df8b4be4f7d8ff528bf3a7e548b783)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataDatabricksShare",
    "DataDatabricksShareConfig",
    "DataDatabricksShareObject",
    "DataDatabricksShareObjectList",
    "DataDatabricksShareObjectOutputReference",
    "DataDatabricksShareObjectPartition",
    "DataDatabricksShareObjectPartitionList",
    "DataDatabricksShareObjectPartitionOutputReference",
    "DataDatabricksShareObjectPartitionValue",
    "DataDatabricksShareObjectPartitionValueList",
    "DataDatabricksShareObjectPartitionValueOutputReference",
]

publication.publish()

def _typecheckingstub__97201639fbba9d17978a271d8fa98e4ff011b64fcdd86301dbe17a54074e5ecb(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    created_at: typing.Optional[jsii.Number] = None,
    created_by: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    object: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksShareObject, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__cfce56214ebfe769c610ae57b649aaf3f7adb680a9658e8e331c5670299768cf(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksShareObject, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f97249349d653784e22cbd5125667592f235da245f93ab2a5d00ae622fc21b4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b67b49ed9f3fa55d469e190329a7da440f0f56aa9830b1814b960f06ab2b8b89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__025c411c1c1525bd22729a9b174e6408f18731881796f3fe7e10d2f32e737928(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__581651731b1964a6ec7cc1a2302b0fe6110fc7b6f3039ba0e0e84da971df8753(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4b2c5924ccd7840bc2a69963671b9e4c34f8da5716a005dcf6f49ff42462ecc(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    created_at: typing.Optional[jsii.Number] = None,
    created_by: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    object: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksShareObject, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f91529bbea0507690e63c469eabb56392465f8f0f56b293453142cef30851f02(
    *,
    data_object_type: builtins.str,
    name: builtins.str,
    added_at: typing.Optional[jsii.Number] = None,
    added_by: typing.Optional[builtins.str] = None,
    cdf_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    comment: typing.Optional[builtins.str] = None,
    history_data_sharing_status: typing.Optional[builtins.str] = None,
    partition: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksShareObjectPartition, typing.Dict[builtins.str, typing.Any]]]]] = None,
    shared_as: typing.Optional[builtins.str] = None,
    start_version: typing.Optional[jsii.Number] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07e05a79c9a044e4fccaa174ebf2d40b1945cb5edfa68c566c4f30b8e6027738(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__667ff6fdbb158b0eef99df507d400ba88523d136fec29f87070ef435958257d4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bdd49edb97de8e7862086bf386756990d20ca5d0706c3f074ae2c64a9895ac6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4969ce055300e2f575ceb89c143ee711869aba04a7b4b2294b18c9018ce1e1b6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f59b1b9bfd80cafb38123b258f90c003d5eb38b676474c6c94372793881ed68b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3758fc47d153cc7bc46cabbbfd3389c1bbe4282ceb16580b7a7052a4891ead85(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksShareObject]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c4a277758d73eba3d97be3e1c66613758d5deddb5a105bdab72ab32c4e2ab1a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63d3987235bcd7315ebb98d3f558c04d2e9a8ee36ad0b550fb9d00d9989aa6ce(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksShareObjectPartition, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0ff7e25a51bc5ea38b3668b366ee350d5241f9db4e3cfd86d127a610f13c5ab(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efa00062d4c6c421c5ed1067e2e2e65d450e82cc46bf3f0cee64924abba96ee6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d48fd26de9dd3157c7ba1d102fba45418aedd994cc63e1408c5f84b0fa6a4c9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71696061ab64512d30d128c95c6f287e4361434446d7a875f65a1ca8124ec53c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1528ea4af4edc29ed8343317fa0a22a4f2c20027c74edf3f730f4ff5e2c35716(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a2c73304c5f708f49df830e0f10c6fedae288191d7d5849406891491abf18e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73d5d56ebf01623cb280fd0ee23bed78ac1423f053e99606e7cbeaa9043df09d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3439a0fa0edeaeb84d71f6b1c0988778f9b93aaeb4f67ef099ef3787dd929e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fac7259bfad64c23bb479d6a4f38efa7dfcc8a448d743b63ecf572e45b617a96(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ae628dfdb30568937c19eb1dbf2a7df864320eb603cdf031eed4035866e8e58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d629e3d3c1b6e297a341eb59e9452c2e4be3feb41861f5e639f60f5891fe97f4(
    value: typing.Optional[typing.Union[DataDatabricksShareObject, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4e151e3293cc197bd1c217444f4a4567b09ed2cc9b729e0fc289ef54323cede(
    *,
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksShareObjectPartitionValue, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e3c186ebf6accd72ff33106aba5d59bcecd72eb9b7c6fd3e49a9ec7115adcee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a83d0a20841bfd48bf91be0beaa481848f9b3ae1ef595ef0f55fed40b887d91f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf7022be0f1a8f89949268b56b08a756f535f1628668377181a073e30ee7027c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b47bdf2eda40be57c52f1537e375de3ac48c47d6055442d67c34293fd906b27f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acf8ecdd5dc4f58f1f2f3cd85ab70bc80a2f71c70405cb8fcdae0b82a4432919(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__114c9091792344f8da5b357b97af387489daf7cfc5012544932d18ab001e9cd7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksShareObjectPartition]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dd254aa67968886a3f69c6ed306ebde5e7a89865b2f99e88523ace3f507d811(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e73ff64f6157528069ba9c75718ae79e68064065cd7db485d3441220f5695c0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataDatabricksShareObjectPartitionValue, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9aa23d8a1d674a95535e7bfd178840fd0f5249e1164aab2881e1239240931bd8(
    value: typing.Optional[typing.Union[DataDatabricksShareObjectPartition, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8ba3b8398ae4be17fefaf39a268a1d6a85b143cf22cdf4f4ff74c75a466f225(
    *,
    name: builtins.str,
    op: builtins.str,
    recipient_property_key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad37ebee3b648c4d3db195cd8a2d1ee3f54e606f204f37231cb7fefb33d21ec1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__803d443c33d6b6f333a35a98ce32f72755c29074cd57eb763aa0d9fcd501b983(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddb501c2f739d8d3fdb504919f136d910f0c1276a3ac3d11531cd000347ad1b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b954bd48c193c8ee585bbb0bb98917f7585d6ccd8085f487fd20dd3799230e75(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d80b43b7e7dc23219166c870e13062d718840bb1ae01af38ae8888d13ce947ea(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5985250c649dc1bdf3bb32655c130b6185a9f69c6c717be8a6a482e65b5ad760(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataDatabricksShareObjectPartitionValue]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e739389003b88dcc72024a0caacec68bba3702f046b2dfc3dc41ef9b54dc9b34(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffa8ef130435bda7394690f35d345f6940955415aa9d42bf943db0d1129542c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f14bb1622fa37903e0be35abb21b0b2c3018884c6b3118f1ad56daa2a03e32f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bcee2e0cab7c48540d4c4378087ca59d2d0615ac6b8266c7c5d93291833dcab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78fa16f739b03c9cf6f8919de80620b4e2c9261271c2ce12088dc45463713fb9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2e3418f856afd1247970102ef10105eb2df8b4be4f7d8ff528bf3a7e548b783(
    value: typing.Optional[typing.Union[DataDatabricksShareObjectPartitionValue, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
