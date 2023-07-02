'''
# `databricks_sql_permissions`

Refer to the Terraform Registory for docs: [`databricks_sql_permissions`](https://www.terraform.io/docs/providers/databricks/r/sql_permissions).
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


class SqlPermissions(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlPermissions.SqlPermissions",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions databricks_sql_permissions}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        anonymous_function: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        any_file: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        catalog: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        database: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        privilege_assignments: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SqlPermissionsPrivilegeAssignments", typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions databricks_sql_permissions} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param anonymous_function: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#anonymous_function SqlPermissions#anonymous_function}.
        :param any_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#any_file SqlPermissions#any_file}.
        :param catalog: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#catalog SqlPermissions#catalog}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#cluster_id SqlPermissions#cluster_id}.
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#database SqlPermissions#database}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#id SqlPermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param privilege_assignments: privilege_assignments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#privilege_assignments SqlPermissions#privilege_assignments}
        :param table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#table SqlPermissions#table}.
        :param view: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#view SqlPermissions#view}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9878fa3cbce81a3b24111a6cfb85d56e9ad9a95270583a4e5b1c3738ec04662)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SqlPermissionsConfig(
            anonymous_function=anonymous_function,
            any_file=any_file,
            catalog=catalog,
            cluster_id=cluster_id,
            database=database,
            id=id,
            privilege_assignments=privilege_assignments,
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

    @jsii.member(jsii_name="putPrivilegeAssignments")
    def put_privilege_assignments(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SqlPermissionsPrivilegeAssignments", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74ed6fd965b5cb3df116c6deeefe474f5a029eaff5e847f99ed1de6c8f711dab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPrivilegeAssignments", [value]))

    @jsii.member(jsii_name="resetAnonymousFunction")
    def reset_anonymous_function(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnonymousFunction", []))

    @jsii.member(jsii_name="resetAnyFile")
    def reset_any_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnyFile", []))

    @jsii.member(jsii_name="resetCatalog")
    def reset_catalog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalog", []))

    @jsii.member(jsii_name="resetClusterId")
    def reset_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterId", []))

    @jsii.member(jsii_name="resetDatabase")
    def reset_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabase", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPrivilegeAssignments")
    def reset_privilege_assignments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivilegeAssignments", []))

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
    @jsii.member(jsii_name="privilegeAssignments")
    def privilege_assignments(self) -> "SqlPermissionsPrivilegeAssignmentsList":
        return typing.cast("SqlPermissionsPrivilegeAssignmentsList", jsii.get(self, "privilegeAssignments"))

    @builtins.property
    @jsii.member(jsii_name="anonymousFunctionInput")
    def anonymous_function_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "anonymousFunctionInput"))

    @builtins.property
    @jsii.member(jsii_name="anyFileInput")
    def any_file_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "anyFileInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogInput")
    def catalog_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "catalogInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegeAssignmentsInput")
    def privilege_assignments_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SqlPermissionsPrivilegeAssignments"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SqlPermissionsPrivilegeAssignments"]]], jsii.get(self, "privilegeAssignmentsInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="viewInput")
    def view_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "viewInput"))

    @builtins.property
    @jsii.member(jsii_name="anonymousFunction")
    def anonymous_function(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "anonymousFunction"))

    @anonymous_function.setter
    def anonymous_function(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d3faf2b8571d735be97587197b8aa9a223f791d0936f605146f0466f71d7f53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anonymousFunction", value)

    @builtins.property
    @jsii.member(jsii_name="anyFile")
    def any_file(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "anyFile"))

    @any_file.setter
    def any_file(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c070a391daf9de4806b32f1ca3a340fb8978a9a07035fdb4918b4a8e1ab897f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anyFile", value)

    @builtins.property
    @jsii.member(jsii_name="catalog")
    def catalog(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "catalog"))

    @catalog.setter
    def catalog(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__696af9d4e9f35fde32930494ac1e272a29dadc5a781db1525ad213cb58f3bda6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalog", value)

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a343f41086a417a46cf04dc6a1c3ab2e56f17b49047293ca7d2d81d69a3db4f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f73eee5018133d8ede096880551b358f3226c46dfd3b3212189f6d996fee47d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03150d4d3d11ca02e3a5ace944f2ceb33efc99ad49a1f031906ca050e137c69f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "table"))

    @table.setter
    def table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2fce152fb4e9faa3c5b4e9c1394cfc72147f5473799d090ece399fd7209e12c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="view")
    def view(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "view"))

    @view.setter
    def view(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00aef68e0e51a916fb481f706e035d2715e50c6a351d41f9535fb6f72efa40b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "view", value)


@jsii.data_type(
    jsii_type="databricks.sqlPermissions.SqlPermissionsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "anonymous_function": "anonymousFunction",
        "any_file": "anyFile",
        "catalog": "catalog",
        "cluster_id": "clusterId",
        "database": "database",
        "id": "id",
        "privilege_assignments": "privilegeAssignments",
        "table": "table",
        "view": "view",
    },
)
class SqlPermissionsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        anonymous_function: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        any_file: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        catalog: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        database: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        privilege_assignments: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SqlPermissionsPrivilegeAssignments", typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        :param anonymous_function: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#anonymous_function SqlPermissions#anonymous_function}.
        :param any_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#any_file SqlPermissions#any_file}.
        :param catalog: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#catalog SqlPermissions#catalog}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#cluster_id SqlPermissions#cluster_id}.
        :param database: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#database SqlPermissions#database}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#id SqlPermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param privilege_assignments: privilege_assignments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#privilege_assignments SqlPermissions#privilege_assignments}
        :param table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#table SqlPermissions#table}.
        :param view: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#view SqlPermissions#view}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5d2c153e55a8502c1065e3132433d5bf4887060563a16635531c920eca24c59)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument anonymous_function", value=anonymous_function, expected_type=type_hints["anonymous_function"])
            check_type(argname="argument any_file", value=any_file, expected_type=type_hints["any_file"])
            check_type(argname="argument catalog", value=catalog, expected_type=type_hints["catalog"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument privilege_assignments", value=privilege_assignments, expected_type=type_hints["privilege_assignments"])
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument view", value=view, expected_type=type_hints["view"])
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
        if anonymous_function is not None:
            self._values["anonymous_function"] = anonymous_function
        if any_file is not None:
            self._values["any_file"] = any_file
        if catalog is not None:
            self._values["catalog"] = catalog
        if cluster_id is not None:
            self._values["cluster_id"] = cluster_id
        if database is not None:
            self._values["database"] = database
        if id is not None:
            self._values["id"] = id
        if privilege_assignments is not None:
            self._values["privilege_assignments"] = privilege_assignments
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
    def anonymous_function(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#anonymous_function SqlPermissions#anonymous_function}.'''
        result = self._values.get("anonymous_function")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def any_file(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#any_file SqlPermissions#any_file}.'''
        result = self._values.get("any_file")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def catalog(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#catalog SqlPermissions#catalog}.'''
        result = self._values.get("catalog")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#cluster_id SqlPermissions#cluster_id}.'''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#database SqlPermissions#database}.'''
        result = self._values.get("database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#id SqlPermissions#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def privilege_assignments(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SqlPermissionsPrivilegeAssignments"]]]:
        '''privilege_assignments block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#privilege_assignments SqlPermissions#privilege_assignments}
        '''
        result = self._values.get("privilege_assignments")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SqlPermissionsPrivilegeAssignments"]]], result)

    @builtins.property
    def table(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#table SqlPermissions#table}.'''
        result = self._values.get("table")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def view(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#view SqlPermissions#view}.'''
        result = self._values.get("view")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlPermissionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.sqlPermissions.SqlPermissionsPrivilegeAssignments",
    jsii_struct_bases=[],
    name_mapping={"principal": "principal", "privileges": "privileges"},
)
class SqlPermissionsPrivilegeAssignments:
    def __init__(
        self,
        *,
        principal: builtins.str,
        privileges: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param principal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#principal SqlPermissions#principal}.
        :param privileges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#privileges SqlPermissions#privileges}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c12043d2295d4617bba89727634d13a3c0ceaafe0b049343d381e7edf9d9606)
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument privileges", value=privileges, expected_type=type_hints["privileges"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "principal": principal,
            "privileges": privileges,
        }

    @builtins.property
    def principal(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#principal SqlPermissions#principal}.'''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def privileges(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_permissions#privileges SqlPermissions#privileges}.'''
        result = self._values.get("privileges")
        assert result is not None, "Required property 'privileges' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlPermissionsPrivilegeAssignments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlPermissionsPrivilegeAssignmentsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlPermissions.SqlPermissionsPrivilegeAssignmentsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__024c58eddd1cc683f23956bfcfe9282cdcddd8dc2ace434d93698ad103361d66)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SqlPermissionsPrivilegeAssignmentsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4027e197edba540d9946e24f06bf44b3ee87bccdae14b5b7b41b15ad79fb7da5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SqlPermissionsPrivilegeAssignmentsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b17f126177a4d67594673fa3374b0cb0735a1b21cf80c6ff2adbef40e6a9c0cb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ce9117a6287ce47c77a78f37393b1da7d035f874367d3fe3367975fa54bd0cb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b54aded6f8ff530c86d5945d54a3d0beba6e48ea3464740e919c4dd5f4386e87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlPermissionsPrivilegeAssignments]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlPermissionsPrivilegeAssignments]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlPermissionsPrivilegeAssignments]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99cb22b00de8b94f92c495533d1d744029d1afd79c12b4f96983e0d02218a4ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SqlPermissionsPrivilegeAssignmentsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlPermissions.SqlPermissionsPrivilegeAssignmentsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2a2eddd1683e3705719de4b4e744834f2f39d513892c6d3512c07a179871f361)
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
            type_hints = typing.get_type_hints(_typecheckingstub__74d578e0746db431393c09e101afadb8babcf6098585a7b925926b453856a5b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value)

    @builtins.property
    @jsii.member(jsii_name="privileges")
    def privileges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "privileges"))

    @privileges.setter
    def privileges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e2def720f4d28830d7daf3bc145ad3f38a8324a7589cdc3d78494b029400149)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privileges", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SqlPermissionsPrivilegeAssignments, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SqlPermissionsPrivilegeAssignments, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SqlPermissionsPrivilegeAssignments, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bb93042f605072e4c988f5f3be55b577183e4829af8ee321bd6cfcd352b987f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SqlPermissions",
    "SqlPermissionsConfig",
    "SqlPermissionsPrivilegeAssignments",
    "SqlPermissionsPrivilegeAssignmentsList",
    "SqlPermissionsPrivilegeAssignmentsOutputReference",
]

publication.publish()

def _typecheckingstub__c9878fa3cbce81a3b24111a6cfb85d56e9ad9a95270583a4e5b1c3738ec04662(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    anonymous_function: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    any_file: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    catalog: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cluster_id: typing.Optional[builtins.str] = None,
    database: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    privilege_assignments: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SqlPermissionsPrivilegeAssignments, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__74ed6fd965b5cb3df116c6deeefe474f5a029eaff5e847f99ed1de6c8f711dab(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SqlPermissionsPrivilegeAssignments, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d3faf2b8571d735be97587197b8aa9a223f791d0936f605146f0466f71d7f53(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c070a391daf9de4806b32f1ca3a340fb8978a9a07035fdb4918b4a8e1ab897f2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__696af9d4e9f35fde32930494ac1e272a29dadc5a781db1525ad213cb58f3bda6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a343f41086a417a46cf04dc6a1c3ab2e56f17b49047293ca7d2d81d69a3db4f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f73eee5018133d8ede096880551b358f3226c46dfd3b3212189f6d996fee47d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03150d4d3d11ca02e3a5ace944f2ceb33efc99ad49a1f031906ca050e137c69f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2fce152fb4e9faa3c5b4e9c1394cfc72147f5473799d090ece399fd7209e12c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00aef68e0e51a916fb481f706e035d2715e50c6a351d41f9535fb6f72efa40b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5d2c153e55a8502c1065e3132433d5bf4887060563a16635531c920eca24c59(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    anonymous_function: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    any_file: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    catalog: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cluster_id: typing.Optional[builtins.str] = None,
    database: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    privilege_assignments: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SqlPermissionsPrivilegeAssignments, typing.Dict[builtins.str, typing.Any]]]]] = None,
    table: typing.Optional[builtins.str] = None,
    view: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c12043d2295d4617bba89727634d13a3c0ceaafe0b049343d381e7edf9d9606(
    *,
    principal: builtins.str,
    privileges: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__024c58eddd1cc683f23956bfcfe9282cdcddd8dc2ace434d93698ad103361d66(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4027e197edba540d9946e24f06bf44b3ee87bccdae14b5b7b41b15ad79fb7da5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b17f126177a4d67594673fa3374b0cb0735a1b21cf80c6ff2adbef40e6a9c0cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ce9117a6287ce47c77a78f37393b1da7d035f874367d3fe3367975fa54bd0cb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b54aded6f8ff530c86d5945d54a3d0beba6e48ea3464740e919c4dd5f4386e87(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99cb22b00de8b94f92c495533d1d744029d1afd79c12b4f96983e0d02218a4ec(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlPermissionsPrivilegeAssignments]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a2eddd1683e3705719de4b4e744834f2f39d513892c6d3512c07a179871f361(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74d578e0746db431393c09e101afadb8babcf6098585a7b925926b453856a5b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e2def720f4d28830d7daf3bc145ad3f38a8324a7589cdc3d78494b029400149(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bb93042f605072e4c988f5f3be55b577183e4829af8ee321bd6cfcd352b987f(
    value: typing.Optional[typing.Union[SqlPermissionsPrivilegeAssignments, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
