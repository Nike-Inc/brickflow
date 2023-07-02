'''
# `databricks_table`

Refer to the Terraform Registory for docs: [`databricks_table`](https://www.terraform.io/docs/providers/databricks/r/table).
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


class Table(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.table.Table",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/table databricks_table}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        catalog_name: builtins.str,
        column: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["TableColumn", typing.Dict[builtins.str, typing.Any]]]],
        data_source_format: builtins.str,
        name: builtins.str,
        schema_name: builtins.str,
        table_type: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        storage_credential_name: typing.Optional[builtins.str] = None,
        storage_location: typing.Optional[builtins.str] = None,
        view_definition: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/table databricks_table} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param catalog_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#catalog_name Table#catalog_name}.
        :param column: column block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#column Table#column}
        :param data_source_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#data_source_format Table#data_source_format}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#name Table#name}.
        :param schema_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#schema_name Table#schema_name}.
        :param table_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#table_type Table#table_type}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#comment Table#comment}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#id Table#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#owner Table#owner}.
        :param properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#properties Table#properties}.
        :param storage_credential_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#storage_credential_name Table#storage_credential_name}.
        :param storage_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#storage_location Table#storage_location}.
        :param view_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#view_definition Table#view_definition}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0e28d98f00e53d220de6b64dbce5c3e3b9936651c33037a54a97b66f76b1e56)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = TableConfig(
            catalog_name=catalog_name,
            column=column,
            data_source_format=data_source_format,
            name=name,
            schema_name=schema_name,
            table_type=table_type,
            comment=comment,
            id=id,
            owner=owner,
            properties=properties,
            storage_credential_name=storage_credential_name,
            storage_location=storage_location,
            view_definition=view_definition,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putColumn")
    def put_column(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["TableColumn", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08c49e98bbeaf84bae134f59c10b844cf7fde78a26a7f373355b96778863f2bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putColumn", [value]))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOwner")
    def reset_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwner", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @jsii.member(jsii_name="resetStorageCredentialName")
    def reset_storage_credential_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageCredentialName", []))

    @jsii.member(jsii_name="resetStorageLocation")
    def reset_storage_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageLocation", []))

    @jsii.member(jsii_name="resetViewDefinition")
    def reset_view_definition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetViewDefinition", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> "TableColumnList":
        return typing.cast("TableColumnList", jsii.get(self, "column"))

    @builtins.property
    @jsii.member(jsii_name="catalogNameInput")
    def catalog_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogNameInput"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TableColumn"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TableColumn"]]], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceFormatInput")
    def data_source_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSourceFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

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
    @jsii.member(jsii_name="schemaNameInput")
    def schema_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageCredentialNameInput")
    def storage_credential_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageCredentialNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageLocationInput")
    def storage_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="tableTypeInput")
    def table_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="viewDefinitionInput")
    def view_definition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "viewDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogName")
    def catalog_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalogName"))

    @catalog_name.setter
    def catalog_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62a1bbf4001a7da187cba674a75ecb1fad5f76cc53196ac60c1d7fb0467b7d5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalogName", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52f4ff39fd4c13f7b1c3dbae8d6d9a157a1a4f71845a001ef1016a43b318b247)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="dataSourceFormat")
    def data_source_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSourceFormat"))

    @data_source_format.setter
    def data_source_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f1a4fd0b4b2a3a2c211c3b95abbbddea2407dfb679b8f524e616efd54756cbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSourceFormat", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__642dd4d7ddeb67c2b0df646ec6309093633c1b9b775275784b5e25508bfe14cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02bfda71320823be8d5472b847de669d22db3624517c56d3c82d76568d300f65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__071ddd44b970d2387166b5716905f7e67137e72848152baeea92c9d82d03706d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26cf3f39db68f01483e27aad2fb224681666965f9900c0b2f182531002643644)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="schemaName")
    def schema_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaName"))

    @schema_name.setter
    def schema_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a81d0896e5c341617502ee288033698dd2dfeaff8b4ce41142ff349705da767f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaName", value)

    @builtins.property
    @jsii.member(jsii_name="storageCredentialName")
    def storage_credential_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageCredentialName"))

    @storage_credential_name.setter
    def storage_credential_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f024b55af0ae48399fd6cc4bed55661c078d1141126c0a7bba8d4c009ed74f29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageCredentialName", value)

    @builtins.property
    @jsii.member(jsii_name="storageLocation")
    def storage_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageLocation"))

    @storage_location.setter
    def storage_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e011aff1148e8f78062b7ff9bd0787299b1f3db0ea7156584674b605f440113)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageLocation", value)

    @builtins.property
    @jsii.member(jsii_name="tableType")
    def table_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableType"))

    @table_type.setter
    def table_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59cf5e41bd0e7f61f36b2a6df024f09a4b7becf20ffd0008eb0f43446dffb743)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableType", value)

    @builtins.property
    @jsii.member(jsii_name="viewDefinition")
    def view_definition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "viewDefinition"))

    @view_definition.setter
    def view_definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddb9e3bdb56011aa70f56eebb2d91ed85c4a0ef03c09b450c7bd45c8dafd4dba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "viewDefinition", value)


@jsii.data_type(
    jsii_type="databricks.table.TableColumn",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "position": "position",
        "type_name": "typeName",
        "type_text": "typeText",
        "comment": "comment",
        "nullable": "nullable",
        "partition_index": "partitionIndex",
        "type_interval_type": "typeIntervalType",
        "type_json": "typeJson",
        "type_precision": "typePrecision",
        "type_scale": "typeScale",
    },
)
class TableColumn:
    def __init__(
        self,
        *,
        name: builtins.str,
        position: jsii.Number,
        type_name: builtins.str,
        type_text: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        partition_index: typing.Optional[jsii.Number] = None,
        type_interval_type: typing.Optional[builtins.str] = None,
        type_json: typing.Optional[builtins.str] = None,
        type_precision: typing.Optional[jsii.Number] = None,
        type_scale: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#name Table#name}.
        :param position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#position Table#position}.
        :param type_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#type_name Table#type_name}.
        :param type_text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#type_text Table#type_text}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#comment Table#comment}.
        :param nullable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#nullable Table#nullable}.
        :param partition_index: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#partition_index Table#partition_index}.
        :param type_interval_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#type_interval_type Table#type_interval_type}.
        :param type_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#type_json Table#type_json}.
        :param type_precision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#type_precision Table#type_precision}.
        :param type_scale: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#type_scale Table#type_scale}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3461790eb11cc388c3e279ee66d918169172b44f38c165f3c867da8a8fc3a9e)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument position", value=position, expected_type=type_hints["position"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument type_text", value=type_text, expected_type=type_hints["type_text"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument nullable", value=nullable, expected_type=type_hints["nullable"])
            check_type(argname="argument partition_index", value=partition_index, expected_type=type_hints["partition_index"])
            check_type(argname="argument type_interval_type", value=type_interval_type, expected_type=type_hints["type_interval_type"])
            check_type(argname="argument type_json", value=type_json, expected_type=type_hints["type_json"])
            check_type(argname="argument type_precision", value=type_precision, expected_type=type_hints["type_precision"])
            check_type(argname="argument type_scale", value=type_scale, expected_type=type_hints["type_scale"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "position": position,
            "type_name": type_name,
            "type_text": type_text,
        }
        if comment is not None:
            self._values["comment"] = comment
        if nullable is not None:
            self._values["nullable"] = nullable
        if partition_index is not None:
            self._values["partition_index"] = partition_index
        if type_interval_type is not None:
            self._values["type_interval_type"] = type_interval_type
        if type_json is not None:
            self._values["type_json"] = type_json
        if type_precision is not None:
            self._values["type_precision"] = type_precision
        if type_scale is not None:
            self._values["type_scale"] = type_scale

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#name Table#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def position(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#position Table#position}.'''
        result = self._values.get("position")
        assert result is not None, "Required property 'position' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#type_name Table#type_name}.'''
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_text(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#type_text Table#type_text}.'''
        result = self._values.get("type_text")
        assert result is not None, "Required property 'type_text' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#comment Table#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nullable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#nullable Table#nullable}.'''
        result = self._values.get("nullable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def partition_index(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#partition_index Table#partition_index}.'''
        result = self._values.get("partition_index")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type_interval_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#type_interval_type Table#type_interval_type}.'''
        result = self._values.get("type_interval_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_json(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#type_json Table#type_json}.'''
        result = self._values.get("type_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_precision(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#type_precision Table#type_precision}.'''
        result = self._values.get("type_precision")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type_scale(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#type_scale Table#type_scale}.'''
        result = self._values.get("type_scale")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableColumn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TableColumnList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.table.TableColumnList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ebb9d3b6ea223488c6112cd6c577a4e0da3a528c3717380b1340d32971507b0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "TableColumnOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0f60d5076dfac5afa8c5174dc118b82964103bfc6926c00546e650534c316a3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("TableColumnOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92afc2a60521a8c7a3b7c10c33f94d42ebae8e2bb8ce63817b4bf8d159b62886)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bbdb7ff7087894421fbcdb35fac8d9233697d8edbbdc633320ca830ad545d4d5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__49ff3b7fb5a5e0e81d636b4ba087d32b7aecd6ffdaab571e9bb124518c3e854d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TableColumn]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TableColumn]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TableColumn]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe5472b70e0b15b0d84fbff075ffd763514708ee694bdee0e4440bcd5491873e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TableColumnOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.table.TableColumnOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e9e134b4386305a9cc51313e739cf588696703f3646e4d5a4e6778123aec9f5b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetNullable")
    def reset_nullable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNullable", []))

    @jsii.member(jsii_name="resetPartitionIndex")
    def reset_partition_index(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionIndex", []))

    @jsii.member(jsii_name="resetTypeIntervalType")
    def reset_type_interval_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeIntervalType", []))

    @jsii.member(jsii_name="resetTypeJson")
    def reset_type_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeJson", []))

    @jsii.member(jsii_name="resetTypePrecision")
    def reset_type_precision(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypePrecision", []))

    @jsii.member(jsii_name="resetTypeScale")
    def reset_type_scale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeScale", []))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nullableInput")
    def nullable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "nullableInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionIndexInput")
    def partition_index_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "partitionIndexInput"))

    @builtins.property
    @jsii.member(jsii_name="positionInput")
    def position_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "positionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeIntervalTypeInput")
    def type_interval_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeIntervalTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeJsonInput")
    def type_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="typeNameInput")
    def type_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="typePrecisionInput")
    def type_precision_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "typePrecisionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeScaleInput")
    def type_scale_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "typeScaleInput"))

    @builtins.property
    @jsii.member(jsii_name="typeTextInput")
    def type_text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeTextInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d8c016884d4dc97e6bb6f784c45eaf258ab0ce35ce80d6001c79130baf01144)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0423a812687723f5da4d4689b7e6fee6de0f79311ffb39238b00a3afeca46766)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nullable")
    def nullable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "nullable"))

    @nullable.setter
    def nullable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48960e6e90b8cdf84ff097aa6b563fa48634dd8d219accfb63ffe092ea40a0c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullable", value)

    @builtins.property
    @jsii.member(jsii_name="partitionIndex")
    def partition_index(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "partitionIndex"))

    @partition_index.setter
    def partition_index(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46b3116770fd9d7cbd39557fbd8135fac116442e96b2d13ec7d839fa688cf25f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionIndex", value)

    @builtins.property
    @jsii.member(jsii_name="position")
    def position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "position"))

    @position.setter
    def position(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ef6fc08d340b674ca53596934c0461b0259cc2721edc0787699c6ce38b6181b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "position", value)

    @builtins.property
    @jsii.member(jsii_name="typeIntervalType")
    def type_interval_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeIntervalType"))

    @type_interval_type.setter
    def type_interval_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__703820d8e02780ee27e5ea3cac42c023d778fc14e6513ad1908b09f811839f16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeIntervalType", value)

    @builtins.property
    @jsii.member(jsii_name="typeJson")
    def type_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeJson"))

    @type_json.setter
    def type_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95da2b754425f0a58243eee3c69cfb9eefde2583f2bf278553b191522061d2e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeJson", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca0974e9a77cee5140b4d5713d14f79dea9f611cca1688d01f3dfdf319650771)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="typePrecision")
    def type_precision(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "typePrecision"))

    @type_precision.setter
    def type_precision(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__884db221ea490730319b1123f11faab92d9022502a4f4fe42758dd958cdb0b2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typePrecision", value)

    @builtins.property
    @jsii.member(jsii_name="typeScale")
    def type_scale(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "typeScale"))

    @type_scale.setter
    def type_scale(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba47b1592f90e1012d44194b600b9c3eea73dd74a548d82294b4b231a61eb338)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeScale", value)

    @builtins.property
    @jsii.member(jsii_name="typeText")
    def type_text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeText"))

    @type_text.setter
    def type_text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d0bfb61d435f74d9c66a7d07fd93743d94b813dcd2c16f3eb2c9958f014252c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeText", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[TableColumn, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[TableColumn, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[TableColumn, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e604c08893dcb6067fad0ced919e647a9b8ae36418bdc4ce713d771d3ac8b17a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.table.TableConfig",
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
        "column": "column",
        "data_source_format": "dataSourceFormat",
        "name": "name",
        "schema_name": "schemaName",
        "table_type": "tableType",
        "comment": "comment",
        "id": "id",
        "owner": "owner",
        "properties": "properties",
        "storage_credential_name": "storageCredentialName",
        "storage_location": "storageLocation",
        "view_definition": "viewDefinition",
    },
)
class TableConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        column: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[TableColumn, typing.Dict[builtins.str, typing.Any]]]],
        data_source_format: builtins.str,
        name: builtins.str,
        schema_name: builtins.str,
        table_type: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        storage_credential_name: typing.Optional[builtins.str] = None,
        storage_location: typing.Optional[builtins.str] = None,
        view_definition: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param catalog_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#catalog_name Table#catalog_name}.
        :param column: column block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#column Table#column}
        :param data_source_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#data_source_format Table#data_source_format}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#name Table#name}.
        :param schema_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#schema_name Table#schema_name}.
        :param table_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#table_type Table#table_type}.
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#comment Table#comment}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#id Table#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#owner Table#owner}.
        :param properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#properties Table#properties}.
        :param storage_credential_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#storage_credential_name Table#storage_credential_name}.
        :param storage_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#storage_location Table#storage_location}.
        :param view_definition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#view_definition Table#view_definition}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62a6aad3035241e36de409b9d771d2b97726221e0685c8ab7f810a237d28a559)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument catalog_name", value=catalog_name, expected_type=type_hints["catalog_name"])
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument data_source_format", value=data_source_format, expected_type=type_hints["data_source_format"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
            check_type(argname="argument table_type", value=table_type, expected_type=type_hints["table_type"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument storage_credential_name", value=storage_credential_name, expected_type=type_hints["storage_credential_name"])
            check_type(argname="argument storage_location", value=storage_location, expected_type=type_hints["storage_location"])
            check_type(argname="argument view_definition", value=view_definition, expected_type=type_hints["view_definition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "catalog_name": catalog_name,
            "column": column,
            "data_source_format": data_source_format,
            "name": name,
            "schema_name": schema_name,
            "table_type": table_type,
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
        if id is not None:
            self._values["id"] = id
        if owner is not None:
            self._values["owner"] = owner
        if properties is not None:
            self._values["properties"] = properties
        if storage_credential_name is not None:
            self._values["storage_credential_name"] = storage_credential_name
        if storage_location is not None:
            self._values["storage_location"] = storage_location
        if view_definition is not None:
            self._values["view_definition"] = view_definition

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#catalog_name Table#catalog_name}.'''
        result = self._values.get("catalog_name")
        assert result is not None, "Required property 'catalog_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def column(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TableColumn]]:
        '''column block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#column Table#column}
        '''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TableColumn]], result)

    @builtins.property
    def data_source_format(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#data_source_format Table#data_source_format}.'''
        result = self._values.get("data_source_format")
        assert result is not None, "Required property 'data_source_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#name Table#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#schema_name Table#schema_name}.'''
        result = self._values.get("schema_name")
        assert result is not None, "Required property 'schema_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#table_type Table#table_type}.'''
        result = self._values.get("table_type")
        assert result is not None, "Required property 'table_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#comment Table#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#id Table#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#owner Table#owner}.'''
        result = self._values.get("owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#properties Table#properties}.'''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def storage_credential_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#storage_credential_name Table#storage_credential_name}.'''
        result = self._values.get("storage_credential_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#storage_location Table#storage_location}.'''
        result = self._values.get("storage_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def view_definition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/table#view_definition Table#view_definition}.'''
        result = self._values.get("view_definition")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Table",
    "TableColumn",
    "TableColumnList",
    "TableColumnOutputReference",
    "TableConfig",
]

publication.publish()

def _typecheckingstub__e0e28d98f00e53d220de6b64dbce5c3e3b9936651c33037a54a97b66f76b1e56(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    catalog_name: builtins.str,
    column: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[TableColumn, typing.Dict[builtins.str, typing.Any]]]],
    data_source_format: builtins.str,
    name: builtins.str,
    schema_name: builtins.str,
    table_type: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    owner: typing.Optional[builtins.str] = None,
    properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    storage_credential_name: typing.Optional[builtins.str] = None,
    storage_location: typing.Optional[builtins.str] = None,
    view_definition: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__08c49e98bbeaf84bae134f59c10b844cf7fde78a26a7f373355b96778863f2bc(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[TableColumn, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62a1bbf4001a7da187cba674a75ecb1fad5f76cc53196ac60c1d7fb0467b7d5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52f4ff39fd4c13f7b1c3dbae8d6d9a157a1a4f71845a001ef1016a43b318b247(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f1a4fd0b4b2a3a2c211c3b95abbbddea2407dfb679b8f524e616efd54756cbd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__642dd4d7ddeb67c2b0df646ec6309093633c1b9b775275784b5e25508bfe14cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02bfda71320823be8d5472b847de669d22db3624517c56d3c82d76568d300f65(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__071ddd44b970d2387166b5716905f7e67137e72848152baeea92c9d82d03706d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26cf3f39db68f01483e27aad2fb224681666965f9900c0b2f182531002643644(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a81d0896e5c341617502ee288033698dd2dfeaff8b4ce41142ff349705da767f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f024b55af0ae48399fd6cc4bed55661c078d1141126c0a7bba8d4c009ed74f29(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e011aff1148e8f78062b7ff9bd0787299b1f3db0ea7156584674b605f440113(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59cf5e41bd0e7f61f36b2a6df024f09a4b7becf20ffd0008eb0f43446dffb743(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddb9e3bdb56011aa70f56eebb2d91ed85c4a0ef03c09b450c7bd45c8dafd4dba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3461790eb11cc388c3e279ee66d918169172b44f38c165f3c867da8a8fc3a9e(
    *,
    name: builtins.str,
    position: jsii.Number,
    type_name: builtins.str,
    type_text: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    nullable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    partition_index: typing.Optional[jsii.Number] = None,
    type_interval_type: typing.Optional[builtins.str] = None,
    type_json: typing.Optional[builtins.str] = None,
    type_precision: typing.Optional[jsii.Number] = None,
    type_scale: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ebb9d3b6ea223488c6112cd6c577a4e0da3a528c3717380b1340d32971507b0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0f60d5076dfac5afa8c5174dc118b82964103bfc6926c00546e650534c316a3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92afc2a60521a8c7a3b7c10c33f94d42ebae8e2bb8ce63817b4bf8d159b62886(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbdb7ff7087894421fbcdb35fac8d9233697d8edbbdc633320ca830ad545d4d5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49ff3b7fb5a5e0e81d636b4ba087d32b7aecd6ffdaab571e9bb124518c3e854d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe5472b70e0b15b0d84fbff075ffd763514708ee694bdee0e4440bcd5491873e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TableColumn]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9e134b4386305a9cc51313e739cf588696703f3646e4d5a4e6778123aec9f5b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d8c016884d4dc97e6bb6f784c45eaf258ab0ce35ce80d6001c79130baf01144(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0423a812687723f5da4d4689b7e6fee6de0f79311ffb39238b00a3afeca46766(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48960e6e90b8cdf84ff097aa6b563fa48634dd8d219accfb63ffe092ea40a0c8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46b3116770fd9d7cbd39557fbd8135fac116442e96b2d13ec7d839fa688cf25f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ef6fc08d340b674ca53596934c0461b0259cc2721edc0787699c6ce38b6181b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__703820d8e02780ee27e5ea3cac42c023d778fc14e6513ad1908b09f811839f16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95da2b754425f0a58243eee3c69cfb9eefde2583f2bf278553b191522061d2e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca0974e9a77cee5140b4d5713d14f79dea9f611cca1688d01f3dfdf319650771(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__884db221ea490730319b1123f11faab92d9022502a4f4fe42758dd958cdb0b2a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba47b1592f90e1012d44194b600b9c3eea73dd74a548d82294b4b231a61eb338(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d0bfb61d435f74d9c66a7d07fd93743d94b813dcd2c16f3eb2c9958f014252c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e604c08893dcb6067fad0ced919e647a9b8ae36418bdc4ce713d771d3ac8b17a(
    value: typing.Optional[typing.Union[TableColumn, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62a6aad3035241e36de409b9d771d2b97726221e0685c8ab7f810a237d28a559(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    catalog_name: builtins.str,
    column: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[TableColumn, typing.Dict[builtins.str, typing.Any]]]],
    data_source_format: builtins.str,
    name: builtins.str,
    schema_name: builtins.str,
    table_type: builtins.str,
    comment: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    owner: typing.Optional[builtins.str] = None,
    properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    storage_credential_name: typing.Optional[builtins.str] = None,
    storage_location: typing.Optional[builtins.str] = None,
    view_definition: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
