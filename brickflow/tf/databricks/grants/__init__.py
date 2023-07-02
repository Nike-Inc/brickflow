'''
# `databricks_grants`

Refer to the Terraform Registory for docs: [`databricks_grants`](https://www.terraform.io/docs/providers/databricks/r/grants).
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


class Grants(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.grants.Grants",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/grants databricks_grants}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        grant: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GrantsGrant", typing.Dict[builtins.str, typing.Any]]]],
        catalog: typing.Optional[builtins.str] = None,
        external_location: typing.Optional[builtins.str] = None,
        function: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        materialized_view: typing.Optional[builtins.str] = None,
        metastore: typing.Optional[builtins.str] = None,
        schema: typing.Optional[builtins.str] = None,
        share: typing.Optional[builtins.str] = None,
        storage_credential: typing.Optional[builtins.str] = None,
        table: typing.Optional[builtins.str] = None,
        view: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/grants databricks_grants} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param grant: grant block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#grant Grants#grant}
        :param catalog: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#catalog Grants#catalog}.
        :param external_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#external_location Grants#external_location}.
        :param function: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#function Grants#function}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#id Grants#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param materialized_view: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#materialized_view Grants#materialized_view}.
        :param metastore: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#metastore Grants#metastore}.
        :param schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#schema Grants#schema}.
        :param share: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#share Grants#share}.
        :param storage_credential: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#storage_credential Grants#storage_credential}.
        :param table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#table Grants#table}.
        :param view: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#view Grants#view}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__389d32d028f2c39e21416df4471f06ef9efe8920da3bc732e08095aa5f1fecd3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GrantsConfig(
            grant=grant,
            catalog=catalog,
            external_location=external_location,
            function=function,
            id=id,
            materialized_view=materialized_view,
            metastore=metastore,
            schema=schema,
            share=share,
            storage_credential=storage_credential,
            table=table,
            view=view,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putGrant")
    def put_grant(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GrantsGrant", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b8873ff2e6e5acf56481a975b85912cd5b7eefc726e9289874f41dbe386709e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGrant", [value]))

    @jsii.member(jsii_name="resetCatalog")
    def reset_catalog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalog", []))

    @jsii.member(jsii_name="resetExternalLocation")
    def reset_external_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalLocation", []))

    @jsii.member(jsii_name="resetFunction")
    def reset_function(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunction", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaterializedView")
    def reset_materialized_view(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaterializedView", []))

    @jsii.member(jsii_name="resetMetastore")
    def reset_metastore(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetastore", []))

    @jsii.member(jsii_name="resetSchema")
    def reset_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchema", []))

    @jsii.member(jsii_name="resetShare")
    def reset_share(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShare", []))

    @jsii.member(jsii_name="resetStorageCredential")
    def reset_storage_credential(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageCredential", []))

    @jsii.member(jsii_name="resetTable")
    def reset_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTable", []))

    @jsii.member(jsii_name="resetView")
    def reset_view(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetView", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="grant")
    def grant(self) -> "GrantsGrantList":
        return typing.cast("GrantsGrantList", jsii.get(self, "grant"))

    @builtins.property
    @jsii.member(jsii_name="catalogInput")
    def catalog_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogInput"))

    @builtins.property
    @jsii.member(jsii_name="externalLocationInput")
    def external_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="functionInput")
    def function_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionInput"))

    @builtins.property
    @jsii.member(jsii_name="grantInput")
    def grant_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GrantsGrant"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GrantsGrant"]]], jsii.get(self, "grantInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="materializedViewInput")
    def materialized_view_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "materializedViewInput"))

    @builtins.property
    @jsii.member(jsii_name="metastoreInput")
    def metastore_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metastoreInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="shareInput")
    def share_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shareInput"))

    @builtins.property
    @jsii.member(jsii_name="storageCredentialInput")
    def storage_credential_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageCredentialInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="viewInput")
    def view_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "viewInput"))

    @builtins.property
    @jsii.member(jsii_name="catalog")
    def catalog(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalog"))

    @catalog.setter
    def catalog(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51d5fd36fe41a639fb34f8a909e4de0ac4a4be5e0b7565ba0e831a2d264d1e11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalog", value)

    @builtins.property
    @jsii.member(jsii_name="externalLocation")
    def external_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalLocation"))

    @external_location.setter
    def external_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc87cb5c48e13aca1928819de4351894eb9b59a2fc2ae4c577725100b81f0d79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalLocation", value)

    @builtins.property
    @jsii.member(jsii_name="function")
    def function(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "function"))

    @function.setter
    def function(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8135f9344e4bbccc897a42fa4a0ea166d90e407eebc71dadfebf129aa7a4743)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "function", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d36bad57565217436eaa4e4457ce41d05b04299a2d1c2062e46989fa647dd308)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="materializedView")
    def materialized_view(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "materializedView"))

    @materialized_view.setter
    def materialized_view(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96f6a792be175e4b3601739eeb975e09911630a486f42238b8441d5cd1de1f86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "materializedView", value)

    @builtins.property
    @jsii.member(jsii_name="metastore")
    def metastore(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metastore"))

    @metastore.setter
    def metastore(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c90a3c35685640088266d9b36bfdbe81f4088c7b804d433abc33a8203512f695)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metastore", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5afed6810208bbe96ad722b133f4e8c7397231e920050ead4cffa729c0b75ee3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="share")
    def share(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "share"))

    @share.setter
    def share(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77792382d580e00dace39aa9ac6f93d5eabcd95c70b1f17ddbb978babd465692)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "share", value)

    @builtins.property
    @jsii.member(jsii_name="storageCredential")
    def storage_credential(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageCredential"))

    @storage_credential.setter
    def storage_credential(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__079f4398e307797d18575fa5b6f774b93022f3c30d4e2177f3bc501b0c4d87c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageCredential", value)

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "table"))

    @table.setter
    def table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__911538ec08ec6399dbd4b080bd011b26ab58dcd849cd15f15ec2b89a21549aae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="view")
    def view(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "view"))

    @view.setter
    def view(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7e1664517ff6de23a56627788b8d98d60171de1d05d006a4ec49b4676b9fc08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "view", value)


@jsii.data_type(
    jsii_type="databricks.grants.GrantsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "grant": "grant",
        "catalog": "catalog",
        "external_location": "externalLocation",
        "function": "function",
        "id": "id",
        "materialized_view": "materializedView",
        "metastore": "metastore",
        "schema": "schema",
        "share": "share",
        "storage_credential": "storageCredential",
        "table": "table",
        "view": "view",
    },
)
class GrantsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        grant: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["GrantsGrant", typing.Dict[builtins.str, typing.Any]]]],
        catalog: typing.Optional[builtins.str] = None,
        external_location: typing.Optional[builtins.str] = None,
        function: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        materialized_view: typing.Optional[builtins.str] = None,
        metastore: typing.Optional[builtins.str] = None,
        schema: typing.Optional[builtins.str] = None,
        share: typing.Optional[builtins.str] = None,
        storage_credential: typing.Optional[builtins.str] = None,
        table: typing.Optional[builtins.str] = None,
        view: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param grant: grant block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#grant Grants#grant}
        :param catalog: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#catalog Grants#catalog}.
        :param external_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#external_location Grants#external_location}.
        :param function: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#function Grants#function}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#id Grants#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param materialized_view: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#materialized_view Grants#materialized_view}.
        :param metastore: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#metastore Grants#metastore}.
        :param schema: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#schema Grants#schema}.
        :param share: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#share Grants#share}.
        :param storage_credential: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#storage_credential Grants#storage_credential}.
        :param table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#table Grants#table}.
        :param view: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#view Grants#view}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f8d98cb184de65aa9c2b0f0476eed2a98966c2f3928a47ad1cfb0d59748e6d7)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument grant", value=grant, expected_type=type_hints["grant"])
            check_type(argname="argument catalog", value=catalog, expected_type=type_hints["catalog"])
            check_type(argname="argument external_location", value=external_location, expected_type=type_hints["external_location"])
            check_type(argname="argument function", value=function, expected_type=type_hints["function"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument materialized_view", value=materialized_view, expected_type=type_hints["materialized_view"])
            check_type(argname="argument metastore", value=metastore, expected_type=type_hints["metastore"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument share", value=share, expected_type=type_hints["share"])
            check_type(argname="argument storage_credential", value=storage_credential, expected_type=type_hints["storage_credential"])
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument view", value=view, expected_type=type_hints["view"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "grant": grant,
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
        if catalog is not None:
            self._values["catalog"] = catalog
        if external_location is not None:
            self._values["external_location"] = external_location
        if function is not None:
            self._values["function"] = function
        if id is not None:
            self._values["id"] = id
        if materialized_view is not None:
            self._values["materialized_view"] = materialized_view
        if metastore is not None:
            self._values["metastore"] = metastore
        if schema is not None:
            self._values["schema"] = schema
        if share is not None:
            self._values["share"] = share
        if storage_credential is not None:
            self._values["storage_credential"] = storage_credential
        if table is not None:
            self._values["table"] = table
        if view is not None:
            self._values["view"] = view

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
    def grant(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GrantsGrant"]]:
        '''grant block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#grant Grants#grant}
        '''
        result = self._values.get("grant")
        assert result is not None, "Required property 'grant' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["GrantsGrant"]], result)

    @builtins.property
    def catalog(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#catalog Grants#catalog}.'''
        result = self._values.get("catalog")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#external_location Grants#external_location}.'''
        result = self._values.get("external_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def function(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#function Grants#function}.'''
        result = self._values.get("function")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#id Grants#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def materialized_view(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#materialized_view Grants#materialized_view}.'''
        result = self._values.get("materialized_view")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metastore(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#metastore Grants#metastore}.'''
        result = self._values.get("metastore")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#schema Grants#schema}.'''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def share(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#share Grants#share}.'''
        result = self._values.get("share")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_credential(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#storage_credential Grants#storage_credential}.'''
        result = self._values.get("storage_credential")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def table(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#table Grants#table}.'''
        result = self._values.get("table")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def view(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#view Grants#view}.'''
        result = self._values.get("view")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.grants.GrantsGrant",
    jsii_struct_bases=[],
    name_mapping={"principal": "principal", "privileges": "privileges"},
)
class GrantsGrant:
    def __init__(
        self,
        *,
        principal: builtins.str,
        privileges: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param principal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#principal Grants#principal}.
        :param privileges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#privileges Grants#privileges}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90dac6cd5a8f30ec6575148d247d88dea9c274d3ba34d7affe05a040a60b9fe7)
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument privileges", value=privileges, expected_type=type_hints["privileges"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "principal": principal,
            "privileges": privileges,
        }

    @builtins.property
    def principal(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#principal Grants#principal}.'''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def privileges(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/grants#privileges Grants#privileges}.'''
        result = self._values.get("privileges")
        assert result is not None, "Required property 'privileges' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantsGrant(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GrantsGrantList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.grants.GrantsGrantList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__73a54897298b3ec5c7391e1bdc6669b2a836c3d364ec844c61b1d99d7bd0dbe9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GrantsGrantOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7033ad0748653867a07185d4fb254b63bfd968936ae757b4b7934d434feee730)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GrantsGrantOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6053db7b06c0c76f06d4f7c3aad636f40715c26a1e807fac2b5abe6a30dcbc0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a774ae16dfa71108ff650e184051b2309b9d2adc045122d0c204f6e15dac51a2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__85fc53853581596303eb87f6dca719bdf716441d13e1213e09593242317e52ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GrantsGrant]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GrantsGrant]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GrantsGrant]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71a2e0804928f72e8431e4752b3807bcf4c4fbe52960b96c5988e3b2ebc6e744)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GrantsGrantOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.grants.GrantsGrantOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8301b3829633755df461a81b8647954224e0ef90e5911233ddf718147bd7797f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="principalInput")
    def principal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegesInput")
    def privileges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "privilegesInput"))

    @builtins.property
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principal"))

    @principal.setter
    def principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61df643904a533c7c7255ea240295d60513fdb78a74d81313478ca2b0245cc67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value)

    @builtins.property
    @jsii.member(jsii_name="privileges")
    def privileges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "privileges"))

    @privileges.setter
    def privileges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1ac4f7612e636f25a0ea125d981520d1b53690ea7c2d02d079994dc8dbd55d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privileges", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GrantsGrant, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GrantsGrant, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GrantsGrant, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20fea54d7252fee69eb6b21a8a10664c71ddb2d53661c20b9f4e806cf1a6798c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Grants",
    "GrantsConfig",
    "GrantsGrant",
    "GrantsGrantList",
    "GrantsGrantOutputReference",
]

publication.publish()

def _typecheckingstub__389d32d028f2c39e21416df4471f06ef9efe8920da3bc732e08095aa5f1fecd3(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    grant: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GrantsGrant, typing.Dict[builtins.str, typing.Any]]]],
    catalog: typing.Optional[builtins.str] = None,
    external_location: typing.Optional[builtins.str] = None,
    function: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    materialized_view: typing.Optional[builtins.str] = None,
    metastore: typing.Optional[builtins.str] = None,
    schema: typing.Optional[builtins.str] = None,
    share: typing.Optional[builtins.str] = None,
    storage_credential: typing.Optional[builtins.str] = None,
    table: typing.Optional[builtins.str] = None,
    view: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__6b8873ff2e6e5acf56481a975b85912cd5b7eefc726e9289874f41dbe386709e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GrantsGrant, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51d5fd36fe41a639fb34f8a909e4de0ac4a4be5e0b7565ba0e831a2d264d1e11(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc87cb5c48e13aca1928819de4351894eb9b59a2fc2ae4c577725100b81f0d79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8135f9344e4bbccc897a42fa4a0ea166d90e407eebc71dadfebf129aa7a4743(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d36bad57565217436eaa4e4457ce41d05b04299a2d1c2062e46989fa647dd308(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96f6a792be175e4b3601739eeb975e09911630a486f42238b8441d5cd1de1f86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c90a3c35685640088266d9b36bfdbe81f4088c7b804d433abc33a8203512f695(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5afed6810208bbe96ad722b133f4e8c7397231e920050ead4cffa729c0b75ee3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77792382d580e00dace39aa9ac6f93d5eabcd95c70b1f17ddbb978babd465692(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__079f4398e307797d18575fa5b6f774b93022f3c30d4e2177f3bc501b0c4d87c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__911538ec08ec6399dbd4b080bd011b26ab58dcd849cd15f15ec2b89a21549aae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7e1664517ff6de23a56627788b8d98d60171de1d05d006a4ec49b4676b9fc08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f8d98cb184de65aa9c2b0f0476eed2a98966c2f3928a47ad1cfb0d59748e6d7(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    grant: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[GrantsGrant, typing.Dict[builtins.str, typing.Any]]]],
    catalog: typing.Optional[builtins.str] = None,
    external_location: typing.Optional[builtins.str] = None,
    function: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    materialized_view: typing.Optional[builtins.str] = None,
    metastore: typing.Optional[builtins.str] = None,
    schema: typing.Optional[builtins.str] = None,
    share: typing.Optional[builtins.str] = None,
    storage_credential: typing.Optional[builtins.str] = None,
    table: typing.Optional[builtins.str] = None,
    view: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90dac6cd5a8f30ec6575148d247d88dea9c274d3ba34d7affe05a040a60b9fe7(
    *,
    principal: builtins.str,
    privileges: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73a54897298b3ec5c7391e1bdc6669b2a836c3d364ec844c61b1d99d7bd0dbe9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7033ad0748653867a07185d4fb254b63bfd968936ae757b4b7934d434feee730(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6053db7b06c0c76f06d4f7c3aad636f40715c26a1e807fac2b5abe6a30dcbc0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a774ae16dfa71108ff650e184051b2309b9d2adc045122d0c204f6e15dac51a2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85fc53853581596303eb87f6dca719bdf716441d13e1213e09593242317e52ae(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71a2e0804928f72e8431e4752b3807bcf4c4fbe52960b96c5988e3b2ebc6e744(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[GrantsGrant]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8301b3829633755df461a81b8647954224e0ef90e5911233ddf718147bd7797f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61df643904a533c7c7255ea240295d60513fdb78a74d81313478ca2b0245cc67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1ac4f7612e636f25a0ea125d981520d1b53690ea7c2d02d079994dc8dbd55d5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20fea54d7252fee69eb6b21a8a10664c71ddb2d53661c20b9f4e806cf1a6798c(
    value: typing.Optional[typing.Union[GrantsGrant, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
