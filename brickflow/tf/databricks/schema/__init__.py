'''
# `databricks_schema`

Refer to the Terraform Registory for docs: [`databricks_schema`](https://www.terraform.io/docs/providers/databricks/r/schema).
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


class Schema(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.schema.Schema",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/schema databricks_schema}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        catalog_name: builtins.str,
        name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        force_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        metastore_id: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        storage_root: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/schema databricks_schema} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param catalog_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#catalog_name Schema#catalog_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#name Schema#name}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#comment Schema#comment}.
        :param force_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#force_destroy Schema#force_destroy}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#id Schema#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metastore_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#metastore_id Schema#metastore_id}.
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#owner Schema#owner}.
        :param properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#properties Schema#properties}.
        :param storage_root: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#storage_root Schema#storage_root}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61039b80864716b52468d5bb091949fbe66ff816b1cdbe84268585ceb3b9e7b8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SchemaConfig(
            catalog_name=catalog_name,
            name=name,
            comment=comment,
            force_destroy=force_destroy,
            id=id,
            metastore_id=metastore_id,
            owner=owner,
            properties=properties,
            storage_root=storage_root,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetForceDestroy")
    def reset_force_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDestroy", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMetastoreId")
    def reset_metastore_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetastoreId", []))

    @jsii.member(jsii_name="resetOwner")
    def reset_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwner", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @jsii.member(jsii_name="resetStorageRoot")
    def reset_storage_root(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageRoot", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="catalogNameInput")
    def catalog_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogNameInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDestroyInput")
    def force_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metastoreIdInput")
    def metastore_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metastoreIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="storageRootInput")
    def storage_root_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageRootInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogName")
    def catalog_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogName"))

    @catalog_name.setter
    def catalog_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70d5f068158d517cbacf6fa521751d9fc4b92a23ad4ba6df925dc9050dec59f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogName", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__077fbcd0d2e1f5e9ba1885cea44d8815f161ac15efec6d099ed5a65312bf683b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="forceDestroy")
    def force_destroy(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forceDestroy"))

    @force_destroy.setter
    def force_destroy(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4824851b93bae6c6ff05cacb49ac4d540d01cc8dd7e11f64ff35515ba4b04392)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c9cbcc02b5623a951570841139b59a528fcb31fc178691457e59aef5d0c34ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="metastoreId")
    def metastore_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metastoreId"))

    @metastore_id.setter
    def metastore_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa4bfd440a8a6f3845ff0fa61b6989c7a632fd51c744da75e2685d50f920d0ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metastoreId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e2cfa0695477e379a983a509d0773fb38b9f048452ea2e4bf31f3ff34bee95f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9493c5c8479bc34e5e933234e8e5e58248387ac47991ee794444080757f40c75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58407bc82c7114b1ebeb9ff876e4a583bda35f02a97cfb839b2d527afe2ddf0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="storageRoot")
    def storage_root(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageRoot"))

    @storage_root.setter
    def storage_root(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ec275778621213f1eb47892b60748b81b9faa37249a36dffba1b529868f3ab2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageRoot", value)


@jsii.data_type(
    jsii_type="databricks.schema.SchemaConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "catalog_name": "catalogName",
        "name": "name",
        "comment": "comment",
        "force_destroy": "forceDestroy",
        "id": "id",
        "metastore_id": "metastoreId",
        "owner": "owner",
        "properties": "properties",
        "storage_root": "storageRoot",
    },
)
class SchemaConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        catalog_name: builtins.str,
        name: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        force_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        metastore_id: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        storage_root: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param catalog_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#catalog_name Schema#catalog_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#name Schema#name}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#comment Schema#comment}.
        :param force_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#force_destroy Schema#force_destroy}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#id Schema#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metastore_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#metastore_id Schema#metastore_id}.
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#owner Schema#owner}.
        :param properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#properties Schema#properties}.
        :param storage_root: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#storage_root Schema#storage_root}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b4308243b5e2537e93f0caab700ef317c94504fa8fe3f77a0728b2fba43bdb0)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument catalog_name", value=catalog_name, expected_type=type_hints["catalog_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument force_destroy", value=force_destroy, expected_type=type_hints["force_destroy"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument metastore_id", value=metastore_id, expected_type=type_hints["metastore_id"])
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument storage_root", value=storage_root, expected_type=type_hints["storage_root"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "catalog_name": catalog_name,
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
        if force_destroy is not None:
            self._values["force_destroy"] = force_destroy
        if id is not None:
            self._values["id"] = id
        if metastore_id is not None:
            self._values["metastore_id"] = metastore_id
        if owner is not None:
            self._values["owner"] = owner
        if properties is not None:
            self._values["properties"] = properties
        if storage_root is not None:
            self._values["storage_root"] = storage_root

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
    def catalog_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#catalog_name Schema#catalog_name}.'''
        result = self._values.get("catalog_name")
        assert result is not None, "Required property 'catalog_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#name Schema#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#comment Schema#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#force_destroy Schema#force_destroy}.'''
        result = self._values.get("force_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#id Schema#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metastore_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#metastore_id Schema#metastore_id}.'''
        result = self._values.get("metastore_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#owner Schema#owner}.'''
        result = self._values.get("owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#properties Schema#properties}.'''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def storage_root(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/schema#storage_root Schema#storage_root}.'''
        result = self._values.get("storage_root")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Schema",
    "SchemaConfig",
]

publication.publish()

def _typecheckingstub__61039b80864716b52468d5bb091949fbe66ff816b1cdbe84268585ceb3b9e7b8(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    catalog_name: builtins.str,
    name: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    force_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    metastore_id: typing.Optional[builtins.str] = None,
    owner: typing.Optional[builtins.str] = None,
    properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    storage_root: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__70d5f068158d517cbacf6fa521751d9fc4b92a23ad4ba6df925dc9050dec59f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__077fbcd0d2e1f5e9ba1885cea44d8815f161ac15efec6d099ed5a65312bf683b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4824851b93bae6c6ff05cacb49ac4d540d01cc8dd7e11f64ff35515ba4b04392(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c9cbcc02b5623a951570841139b59a528fcb31fc178691457e59aef5d0c34ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa4bfd440a8a6f3845ff0fa61b6989c7a632fd51c744da75e2685d50f920d0ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e2cfa0695477e379a983a509d0773fb38b9f048452ea2e4bf31f3ff34bee95f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9493c5c8479bc34e5e933234e8e5e58248387ac47991ee794444080757f40c75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58407bc82c7114b1ebeb9ff876e4a583bda35f02a97cfb839b2d527afe2ddf0e(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ec275778621213f1eb47892b60748b81b9faa37249a36dffba1b529868f3ab2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b4308243b5e2537e93f0caab700ef317c94504fa8fe3f77a0728b2fba43bdb0(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    catalog_name: builtins.str,
    name: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    force_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    metastore_id: typing.Optional[builtins.str] = None,
    owner: typing.Optional[builtins.str] = None,
    properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    storage_root: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
