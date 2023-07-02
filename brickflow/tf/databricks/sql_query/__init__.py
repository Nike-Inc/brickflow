'''
# `databricks_sql_query`

Refer to the Terraform Registory for docs: [`databricks_sql_query`](https://www.terraform.io/docs/providers/databricks/r/sql_query).
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


class SqlQuery(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQuery",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/sql_query databricks_sql_query}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        data_source_id: builtins.str,
        name: builtins.str,
        query: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SqlQueryParameter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        parent: typing.Optional[builtins.str] = None,
        run_as_role: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union["SqlQuerySchedule", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/sql_query databricks_sql_query} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_source_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#data_source_id SqlQuery#data_source_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#name SqlQuery#name}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#query SqlQuery#query}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#description SqlQuery#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#id SqlQuery#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#parameter SqlQuery#parameter}
        :param parent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#parent SqlQuery#parent}.
        :param run_as_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#run_as_role SqlQuery#run_as_role}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#schedule SqlQuery#schedule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#tags SqlQuery#tags}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5048304b7db0e775e4f0e8161fa3cca352da818cb20821d62763511cbbf9fcea)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SqlQueryConfig(
            data_source_id=data_source_id,
            name=name,
            query=query,
            description=description,
            id=id,
            parameter=parameter,
            parent=parent,
            run_as_role=run_as_role,
            schedule=schedule,
            tags=tags,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putParameter")
    def put_parameter(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SqlQueryParameter", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9111d59c07c9d5941b9f8411a812c57b7af9551ee6e4e62a11602d488f0b79db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameter", [value]))

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(
        self,
        *,
        continuous: typing.Optional[typing.Union["SqlQueryScheduleContinuous", typing.Dict[builtins.str, typing.Any]]] = None,
        daily: typing.Optional[typing.Union["SqlQueryScheduleDaily", typing.Dict[builtins.str, typing.Any]]] = None,
        weekly: typing.Optional[typing.Union["SqlQueryScheduleWeekly", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param continuous: continuous block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#continuous SqlQuery#continuous}
        :param daily: daily block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#daily SqlQuery#daily}
        :param weekly: weekly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#weekly SqlQuery#weekly}
        '''
        value = SqlQuerySchedule(continuous=continuous, daily=daily, weekly=weekly)

        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @jsii.member(jsii_name="resetParent")
    def reset_parent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParent", []))

    @jsii.member(jsii_name="resetRunAsRole")
    def reset_run_as_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunAsRole", []))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(self) -> "SqlQueryParameterList":
        return typing.cast("SqlQueryParameterList", jsii.get(self, "parameter"))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> "SqlQueryScheduleOutputReference":
        return typing.cast("SqlQueryScheduleOutputReference", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceIdInput")
    def data_source_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SqlQueryParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SqlQueryParameter"]]], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="parentInput")
    def parent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="runAsRoleInput")
    def run_as_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runAsRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional["SqlQuerySchedule"]:
        return typing.cast(typing.Optional["SqlQuerySchedule"], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceId")
    def data_source_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSourceId"))

    @data_source_id.setter
    def data_source_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8f5f6aab48ed48226f42ebcdb27ca3701bfa8654ff293c393aa16a2bc5db1bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSourceId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fc459dbc58a29a6934114324dda457ebe39f833874569ad3b3bfeacb4a61891)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__741908d1a5b0f3e9cc12176a82620d9e6b0cb8df5f9849e27891665388481b28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a18916e62c842bcb72130a072bdfaaa4d8c7d08e4ca6fec1505568ee4d0ab276)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parent"))

    @parent.setter
    def parent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76e63f7f68cfbe8ea6f76104ee7d50be0b4d591742cb3e30a629be9ccbd7bbbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parent", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d769f6a1f7e4537581c496b37d603e1f82f0a5128e5ce6bcea5643edcd4b6183)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="runAsRole")
    def run_as_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runAsRole"))

    @run_as_role.setter
    def run_as_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b96d5f1ceb93e08af968c7e48a84c60ff3ba468bc2c0accb8e52f02c1d40346d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runAsRole", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed81771e47b5f80097e3d12b269f22b89e5d0d4a78b1075da335fc0ac2e29298)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_source_id": "dataSourceId",
        "name": "name",
        "query": "query",
        "description": "description",
        "id": "id",
        "parameter": "parameter",
        "parent": "parent",
        "run_as_role": "runAsRole",
        "schedule": "schedule",
        "tags": "tags",
    },
)
class SqlQueryConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        data_source_id: builtins.str,
        name: builtins.str,
        query: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SqlQueryParameter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        parent: typing.Optional[builtins.str] = None,
        run_as_role: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union["SqlQuerySchedule", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_source_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#data_source_id SqlQuery#data_source_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#name SqlQuery#name}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#query SqlQuery#query}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#description SqlQuery#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#id SqlQuery#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#parameter SqlQuery#parameter}
        :param parent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#parent SqlQuery#parent}.
        :param run_as_role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#run_as_role SqlQuery#run_as_role}.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#schedule SqlQuery#schedule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#tags SqlQuery#tags}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(schedule, dict):
            schedule = SqlQuerySchedule(**schedule)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c78c8e10068be6af9a9af7af59b3d2a77d1de2525dd4a372344e77737b6e2fb)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument data_source_id", value=data_source_id, expected_type=type_hints["data_source_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument run_as_role", value=run_as_role, expected_type=type_hints["run_as_role"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_source_id": data_source_id,
            "name": name,
            "query": query,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if parameter is not None:
            self._values["parameter"] = parameter
        if parent is not None:
            self._values["parent"] = parent
        if run_as_role is not None:
            self._values["run_as_role"] = run_as_role
        if schedule is not None:
            self._values["schedule"] = schedule
        if tags is not None:
            self._values["tags"] = tags

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
    def data_source_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#data_source_id SqlQuery#data_source_id}.'''
        result = self._values.get("data_source_id")
        assert result is not None, "Required property 'data_source_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#name SqlQuery#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#query SqlQuery#query}.'''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#description SqlQuery#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#id SqlQuery#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SqlQueryParameter"]]]:
        '''parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#parameter SqlQuery#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SqlQueryParameter"]]], result)

    @builtins.property
    def parent(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#parent SqlQuery#parent}.'''
        result = self._values.get("parent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def run_as_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#run_as_role SqlQuery#run_as_role}.'''
        result = self._values.get("run_as_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule(self) -> typing.Optional["SqlQuerySchedule"]:
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#schedule SqlQuery#schedule}
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional["SqlQuerySchedule"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#tags SqlQuery#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryParameter",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "date": "date",
        "date_range": "dateRange",
        "datetime": "datetime",
        "datetime_range": "datetimeRange",
        "datetimesec": "datetimesec",
        "datetimesec_range": "datetimesecRange",
        "enum": "enum",
        "number": "number",
        "query": "query",
        "text": "text",
        "title": "title",
    },
)
class SqlQueryParameter:
    def __init__(
        self,
        *,
        name: builtins.str,
        date: typing.Optional[typing.Union["SqlQueryParameterDate", typing.Dict[builtins.str, typing.Any]]] = None,
        date_range: typing.Optional[typing.Union["SqlQueryParameterDateRange", typing.Dict[builtins.str, typing.Any]]] = None,
        datetime: typing.Optional[typing.Union["SqlQueryParameterDatetime", typing.Dict[builtins.str, typing.Any]]] = None,
        datetime_range: typing.Optional[typing.Union["SqlQueryParameterDatetimeRange", typing.Dict[builtins.str, typing.Any]]] = None,
        datetimesec: typing.Optional[typing.Union["SqlQueryParameterDatetimesec", typing.Dict[builtins.str, typing.Any]]] = None,
        datetimesec_range: typing.Optional[typing.Union["SqlQueryParameterDatetimesecRange", typing.Dict[builtins.str, typing.Any]]] = None,
        enum: typing.Optional[typing.Union["SqlQueryParameterEnum", typing.Dict[builtins.str, typing.Any]]] = None,
        number: typing.Optional[typing.Union["SqlQueryParameterNumber", typing.Dict[builtins.str, typing.Any]]] = None,
        query: typing.Optional[typing.Union["SqlQueryParameterQuery", typing.Dict[builtins.str, typing.Any]]] = None,
        text: typing.Optional[typing.Union["SqlQueryParameterText", typing.Dict[builtins.str, typing.Any]]] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#name SqlQuery#name}.
        :param date: date block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#date SqlQuery#date}
        :param date_range: date_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#date_range SqlQuery#date_range}
        :param datetime: datetime block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#datetime SqlQuery#datetime}
        :param datetime_range: datetime_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#datetime_range SqlQuery#datetime_range}
        :param datetimesec: datetimesec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#datetimesec SqlQuery#datetimesec}
        :param datetimesec_range: datetimesec_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#datetimesec_range SqlQuery#datetimesec_range}
        :param enum: enum block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#enum SqlQuery#enum}
        :param number: number block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#number SqlQuery#number}
        :param query: query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#query SqlQuery#query}
        :param text: text block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#text SqlQuery#text}
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#title SqlQuery#title}.
        '''
        if isinstance(date, dict):
            date = SqlQueryParameterDate(**date)
        if isinstance(date_range, dict):
            date_range = SqlQueryParameterDateRange(**date_range)
        if isinstance(datetime, dict):
            datetime = SqlQueryParameterDatetime(**datetime)
        if isinstance(datetime_range, dict):
            datetime_range = SqlQueryParameterDatetimeRange(**datetime_range)
        if isinstance(datetimesec, dict):
            datetimesec = SqlQueryParameterDatetimesec(**datetimesec)
        if isinstance(datetimesec_range, dict):
            datetimesec_range = SqlQueryParameterDatetimesecRange(**datetimesec_range)
        if isinstance(enum, dict):
            enum = SqlQueryParameterEnum(**enum)
        if isinstance(number, dict):
            number = SqlQueryParameterNumber(**number)
        if isinstance(query, dict):
            query = SqlQueryParameterQuery(**query)
        if isinstance(text, dict):
            text = SqlQueryParameterText(**text)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a0b7813a7d790f4136f838141f5388989a4774e74407b829cc81dcae2b24bd6)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument date", value=date, expected_type=type_hints["date"])
            check_type(argname="argument date_range", value=date_range, expected_type=type_hints["date_range"])
            check_type(argname="argument datetime", value=datetime, expected_type=type_hints["datetime"])
            check_type(argname="argument datetime_range", value=datetime_range, expected_type=type_hints["datetime_range"])
            check_type(argname="argument datetimesec", value=datetimesec, expected_type=type_hints["datetimesec"])
            check_type(argname="argument datetimesec_range", value=datetimesec_range, expected_type=type_hints["datetimesec_range"])
            check_type(argname="argument enum", value=enum, expected_type=type_hints["enum"])
            check_type(argname="argument number", value=number, expected_type=type_hints["number"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if date is not None:
            self._values["date"] = date
        if date_range is not None:
            self._values["date_range"] = date_range
        if datetime is not None:
            self._values["datetime"] = datetime
        if datetime_range is not None:
            self._values["datetime_range"] = datetime_range
        if datetimesec is not None:
            self._values["datetimesec"] = datetimesec
        if datetimesec_range is not None:
            self._values["datetimesec_range"] = datetimesec_range
        if enum is not None:
            self._values["enum"] = enum
        if number is not None:
            self._values["number"] = number
        if query is not None:
            self._values["query"] = query
        if text is not None:
            self._values["text"] = text
        if title is not None:
            self._values["title"] = title

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#name SqlQuery#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def date(self) -> typing.Optional["SqlQueryParameterDate"]:
        '''date block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#date SqlQuery#date}
        '''
        result = self._values.get("date")
        return typing.cast(typing.Optional["SqlQueryParameterDate"], result)

    @builtins.property
    def date_range(self) -> typing.Optional["SqlQueryParameterDateRange"]:
        '''date_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#date_range SqlQuery#date_range}
        '''
        result = self._values.get("date_range")
        return typing.cast(typing.Optional["SqlQueryParameterDateRange"], result)

    @builtins.property
    def datetime(self) -> typing.Optional["SqlQueryParameterDatetime"]:
        '''datetime block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#datetime SqlQuery#datetime}
        '''
        result = self._values.get("datetime")
        return typing.cast(typing.Optional["SqlQueryParameterDatetime"], result)

    @builtins.property
    def datetime_range(self) -> typing.Optional["SqlQueryParameterDatetimeRange"]:
        '''datetime_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#datetime_range SqlQuery#datetime_range}
        '''
        result = self._values.get("datetime_range")
        return typing.cast(typing.Optional["SqlQueryParameterDatetimeRange"], result)

    @builtins.property
    def datetimesec(self) -> typing.Optional["SqlQueryParameterDatetimesec"]:
        '''datetimesec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#datetimesec SqlQuery#datetimesec}
        '''
        result = self._values.get("datetimesec")
        return typing.cast(typing.Optional["SqlQueryParameterDatetimesec"], result)

    @builtins.property
    def datetimesec_range(self) -> typing.Optional["SqlQueryParameterDatetimesecRange"]:
        '''datetimesec_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#datetimesec_range SqlQuery#datetimesec_range}
        '''
        result = self._values.get("datetimesec_range")
        return typing.cast(typing.Optional["SqlQueryParameterDatetimesecRange"], result)

    @builtins.property
    def enum(self) -> typing.Optional["SqlQueryParameterEnum"]:
        '''enum block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#enum SqlQuery#enum}
        '''
        result = self._values.get("enum")
        return typing.cast(typing.Optional["SqlQueryParameterEnum"], result)

    @builtins.property
    def number(self) -> typing.Optional["SqlQueryParameterNumber"]:
        '''number block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#number SqlQuery#number}
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional["SqlQueryParameterNumber"], result)

    @builtins.property
    def query(self) -> typing.Optional["SqlQueryParameterQuery"]:
        '''query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#query SqlQuery#query}
        '''
        result = self._values.get("query")
        return typing.cast(typing.Optional["SqlQueryParameterQuery"], result)

    @builtins.property
    def text(self) -> typing.Optional["SqlQueryParameterText"]:
        '''text block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#text SqlQuery#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional["SqlQueryParameterText"], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#title SqlQuery#title}.'''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryParameterDate",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class SqlQueryParameterDate:
    def __init__(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca5e16a1f32adf552a88ee913bb2dd7c3eae264f105d77ef768af0a79146c878)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterDate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterDateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryParameterDateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__33dcc146d942573fd37f0c12b41ad8d58a459f206c1ae4c4a4525aadbfa986cc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f75f158a4e5b2d97882e2293a1c644cc0927e286064da2931e81c7cd204e164)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterDate]:
        return typing.cast(typing.Optional[SqlQueryParameterDate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQueryParameterDate]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ca1ae3a9a8ebdef21a234475bf9f1b5c906083e38abf3d69501366042eea009)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryParameterDateRange",
    jsii_struct_bases=[],
    name_mapping={"range": "range", "value": "value"},
)
class SqlQueryParameterDateRange:
    def __init__(
        self,
        *,
        range: typing.Optional[typing.Union["SqlQueryParameterDateRangeRange", typing.Dict[builtins.str, typing.Any]]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#range SqlQuery#range}
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        if isinstance(range, dict):
            range = SqlQueryParameterDateRangeRange(**range)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6aba251e2c9f46e8c7f567cf4890223328a6b1dec48fe605450410932e82950)
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if range is not None:
            self._values["range"] = range
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def range(self) -> typing.Optional["SqlQueryParameterDateRangeRange"]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#range SqlQuery#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional["SqlQueryParameterDateRangeRange"], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterDateRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterDateRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryParameterDateRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__06d33f75360eba954d0d1d34684f2fbd927a6855fd3e3e8be22808122b849e4c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(self, *, end: builtins.str, start: builtins.str) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#end SqlQuery#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#start SqlQuery#start}.
        '''
        value = SqlQueryParameterDateRangeRange(end=end, start=start)

        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "SqlQueryParameterDateRangeRangeOutputReference":
        return typing.cast("SqlQueryParameterDateRangeRangeOutputReference", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(self) -> typing.Optional["SqlQueryParameterDateRangeRange"]:
        return typing.cast(typing.Optional["SqlQueryParameterDateRangeRange"], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24ebbb67ea694ac48249ef1fe7212f773e4bc270cca907bc167546adcddcee7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterDateRange]:
        return typing.cast(typing.Optional[SqlQueryParameterDateRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlQueryParameterDateRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae925dadbcbc0a06ca0ac7821306f8dcee2bcd6747fba47904edb94e24e2834f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryParameterDateRangeRange",
    jsii_struct_bases=[],
    name_mapping={"end": "end", "start": "start"},
)
class SqlQueryParameterDateRangeRange:
    def __init__(self, *, end: builtins.str, start: builtins.str) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#end SqlQuery#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#start SqlQuery#start}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8697c2f0343cdff058601303594f941de349c15574b64b9cf007bdb9cbc7990d)
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "end": end,
            "start": start,
        }

    @builtins.property
    def end(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#end SqlQuery#end}.'''
        result = self._values.get("end")
        assert result is not None, "Required property 'end' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def start(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#start SqlQuery#start}.'''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterDateRangeRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterDateRangeRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryParameterDateRangeRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8fe8d4eb0d9f7291f3f51e6a857bf5b2fd89d311f4139f8c0bc118231a23b43f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endInput")
    def end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "end"))

    @end.setter
    def end(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16698838cae795aac758d14ee6e1aa64893209d49de99ce5e75acd3bc3106000)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "start"))

    @start.setter
    def start(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27857db834cfe6251d60cdbcbf9a29608865493b544aee8f837d842774fd6d38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterDateRangeRange]:
        return typing.cast(typing.Optional[SqlQueryParameterDateRangeRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlQueryParameterDateRangeRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad7d5287b82bc044593c59b20d5f75df655713b19924d0e7685ebeafc3268df5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryParameterDatetime",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class SqlQueryParameterDatetime:
    def __init__(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd66c816f3c1558a0d0717d816c71d3f87ce292fc00df0dfa4b164134b0997b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterDatetime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterDatetimeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryParameterDatetimeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b33645a092cfbb722bd0c1deb0416060684809f453c08454add7278eb1b942a0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e13c64d9024006550415b6761a4edf5923567c3571f83648e0f7bd65222f69c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterDatetime]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQueryParameterDatetime]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a69525046759542a4b6438482a7bbfdbd241e65f6de52946deae767d3a4c5220)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryParameterDatetimeRange",
    jsii_struct_bases=[],
    name_mapping={"range": "range", "value": "value"},
)
class SqlQueryParameterDatetimeRange:
    def __init__(
        self,
        *,
        range: typing.Optional[typing.Union["SqlQueryParameterDatetimeRangeRange", typing.Dict[builtins.str, typing.Any]]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#range SqlQuery#range}
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        if isinstance(range, dict):
            range = SqlQueryParameterDatetimeRangeRange(**range)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed07840685ae9d7a5cb86e90417e5ed480e2904f6ed6688d5e43eb3e5a90c1ed)
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if range is not None:
            self._values["range"] = range
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def range(self) -> typing.Optional["SqlQueryParameterDatetimeRangeRange"]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#range SqlQuery#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional["SqlQueryParameterDatetimeRangeRange"], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterDatetimeRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterDatetimeRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryParameterDatetimeRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ec96223936c810eea8c2335964a1174bd03c13019e76ab04e147e7a61eafb5a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(self, *, end: builtins.str, start: builtins.str) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#end SqlQuery#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#start SqlQuery#start}.
        '''
        value = SqlQueryParameterDatetimeRangeRange(end=end, start=start)

        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "SqlQueryParameterDatetimeRangeRangeOutputReference":
        return typing.cast("SqlQueryParameterDatetimeRangeRangeOutputReference", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(self) -> typing.Optional["SqlQueryParameterDatetimeRangeRange"]:
        return typing.cast(typing.Optional["SqlQueryParameterDatetimeRangeRange"], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db3ea3430bb906c9a791d512da10b651d0eb41a014d80d57991c4465b50813d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterDatetimeRange]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetimeRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlQueryParameterDatetimeRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9c2c66f2ac207085785300f2b339adfe2ef9c5ac8bd7623aa31e1de968c9c21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryParameterDatetimeRangeRange",
    jsii_struct_bases=[],
    name_mapping={"end": "end", "start": "start"},
)
class SqlQueryParameterDatetimeRangeRange:
    def __init__(self, *, end: builtins.str, start: builtins.str) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#end SqlQuery#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#start SqlQuery#start}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f395b9278422880d001a70ee786160379316013415bd1ef49aeaffe065425d89)
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "end": end,
            "start": start,
        }

    @builtins.property
    def end(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#end SqlQuery#end}.'''
        result = self._values.get("end")
        assert result is not None, "Required property 'end' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def start(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#start SqlQuery#start}.'''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterDatetimeRangeRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterDatetimeRangeRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryParameterDatetimeRangeRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__31a04ffa2e80a0730edb74313b28b3be5b91d15fee091d0f10591a42397facc7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endInput")
    def end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "end"))

    @end.setter
    def end(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f9837d18695e6315e593765b0468cfb10fc252e05de5562d86b34e9de1a7750)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "start"))

    @start.setter
    def start(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8823a4212862892abba8150849244156ade2801e5ae31cc148989de3121c5fe7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterDatetimeRangeRange]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetimeRangeRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlQueryParameterDatetimeRangeRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6d05773ec5cec2d960a1446907be164a577b92b1f0d418dae66def4176a820a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryParameterDatetimesec",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class SqlQueryParameterDatetimesec:
    def __init__(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92be823e2ae56b9d2a05c513dd29c5364d1ccb74887dc089524211977ceb81ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterDatetimesec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterDatetimesecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryParameterDatetimesecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__446612324a849a4f8084404df4d5efefd04c1fdd9835e07667030738bfe2fcdb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18b4680c55208358753e3ca2ef00735aeee6e543a1dcb5ad8414e4cf4d694f38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterDatetimesec]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetimesec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlQueryParameterDatetimesec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3090a5944ac75376eb9bc94c021162d16aa935de8ef30271240a8d9db315a2a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryParameterDatetimesecRange",
    jsii_struct_bases=[],
    name_mapping={"range": "range", "value": "value"},
)
class SqlQueryParameterDatetimesecRange:
    def __init__(
        self,
        *,
        range: typing.Optional[typing.Union["SqlQueryParameterDatetimesecRangeRange", typing.Dict[builtins.str, typing.Any]]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#range SqlQuery#range}
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        if isinstance(range, dict):
            range = SqlQueryParameterDatetimesecRangeRange(**range)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee38a8ed3b2968fb9387dff05486f06ac792f803843d3d655aa3482c39d765ea)
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if range is not None:
            self._values["range"] = range
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def range(self) -> typing.Optional["SqlQueryParameterDatetimesecRangeRange"]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#range SqlQuery#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional["SqlQueryParameterDatetimesecRangeRange"], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterDatetimesecRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterDatetimesecRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryParameterDatetimesecRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec63078ea19aeb5d79267b932d37e3e1a985294f928f235c849df56c5650d629)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(self, *, end: builtins.str, start: builtins.str) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#end SqlQuery#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#start SqlQuery#start}.
        '''
        value = SqlQueryParameterDatetimesecRangeRange(end=end, start=start)

        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "SqlQueryParameterDatetimesecRangeRangeOutputReference":
        return typing.cast("SqlQueryParameterDatetimesecRangeRangeOutputReference", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(self) -> typing.Optional["SqlQueryParameterDatetimesecRangeRange"]:
        return typing.cast(typing.Optional["SqlQueryParameterDatetimesecRangeRange"], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77c9fac0089266c4674ab528c5e840b226371564e6a359af1e0e106988548571)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterDatetimesecRange]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetimesecRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlQueryParameterDatetimesecRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6b38a8a47fab504053b439652092d7d06709e991314c762402dd0fe46d3ada2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryParameterDatetimesecRangeRange",
    jsii_struct_bases=[],
    name_mapping={"end": "end", "start": "start"},
)
class SqlQueryParameterDatetimesecRangeRange:
    def __init__(self, *, end: builtins.str, start: builtins.str) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#end SqlQuery#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#start SqlQuery#start}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1215ce01f13e8c7b671035455d485506481f75c09c944037f3c600ffbc7db9c6)
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "end": end,
            "start": start,
        }

    @builtins.property
    def end(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#end SqlQuery#end}.'''
        result = self._values.get("end")
        assert result is not None, "Required property 'end' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def start(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#start SqlQuery#start}.'''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterDatetimesecRangeRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterDatetimesecRangeRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryParameterDatetimesecRangeRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__168ed7096bb5107cfaf2cd48c8db6470f6ee0145547a0c21be26fec14ffdea30)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endInput")
    def end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "end"))

    @end.setter
    def end(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffa9d0e237c06d5c2a57f8bb73ec3d5333ee27a4d2ff29803661ee1ccccd2916)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "start"))

    @start.setter
    def start(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f139f2822a0faf6c6eb134cc6da1ab9bfcce50c08d8dda3370022b5cb8ac15b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterDatetimesecRangeRange]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetimesecRangeRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlQueryParameterDatetimesecRangeRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff3f7464de25a3faf188799a0dea6089e48a6c1c8f71c378db32d5e7f6ff263a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryParameterEnum",
    jsii_struct_bases=[],
    name_mapping={
        "options": "options",
        "multiple": "multiple",
        "value": "value",
        "values": "values",
    },
)
class SqlQueryParameterEnum:
    def __init__(
        self,
        *,
        options: typing.Sequence[builtins.str],
        multiple: typing.Optional[typing.Union["SqlQueryParameterEnumMultiple", typing.Dict[builtins.str, typing.Any]]] = None,
        value: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#options SqlQuery#options}.
        :param multiple: multiple block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#multiple SqlQuery#multiple}
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#values SqlQuery#values}.
        '''
        if isinstance(multiple, dict):
            multiple = SqlQueryParameterEnumMultiple(**multiple)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53bcbccefc239f31c076143b21392267da548e3008137a317e4166d24942f83c)
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument multiple", value=multiple, expected_type=type_hints["multiple"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "options": options,
        }
        if multiple is not None:
            self._values["multiple"] = multiple
        if value is not None:
            self._values["value"] = value
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def options(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#options SqlQuery#options}.'''
        result = self._values.get("options")
        assert result is not None, "Required property 'options' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def multiple(self) -> typing.Optional["SqlQueryParameterEnumMultiple"]:
        '''multiple block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#multiple SqlQuery#multiple}
        '''
        result = self._values.get("multiple")
        return typing.cast(typing.Optional["SqlQueryParameterEnumMultiple"], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#values SqlQuery#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterEnum(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryParameterEnumMultiple",
    jsii_struct_bases=[],
    name_mapping={"prefix": "prefix", "separator": "separator", "suffix": "suffix"},
)
class SqlQueryParameterEnumMultiple:
    def __init__(
        self,
        *,
        prefix: builtins.str,
        separator: builtins.str,
        suffix: builtins.str,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#prefix SqlQuery#prefix}.
        :param separator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#separator SqlQuery#separator}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#suffix SqlQuery#suffix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6155389546d6426cf71db0c4f02adc20f3a4d3035991db094bb07d6844ac24c)
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument separator", value=separator, expected_type=type_hints["separator"])
            check_type(argname="argument suffix", value=suffix, expected_type=type_hints["suffix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "prefix": prefix,
            "separator": separator,
            "suffix": suffix,
        }

    @builtins.property
    def prefix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#prefix SqlQuery#prefix}.'''
        result = self._values.get("prefix")
        assert result is not None, "Required property 'prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def separator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#separator SqlQuery#separator}.'''
        result = self._values.get("separator")
        assert result is not None, "Required property 'separator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def suffix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#suffix SqlQuery#suffix}.'''
        result = self._values.get("suffix")
        assert result is not None, "Required property 'suffix' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterEnumMultiple(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterEnumMultipleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryParameterEnumMultipleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__acbc6ac055d15c33340ea8f03e390d4fec07c6025ee3e6f8374099a1e1444b89)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="separatorInput")
    def separator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "separatorInput"))

    @builtins.property
    @jsii.member(jsii_name="suffixInput")
    def suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "suffixInput"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__027f6bf1d4e35066b57ebab7ae94d0c062d97b9827c77c776bc2068d853ddc00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="separator")
    def separator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "separator"))

    @separator.setter
    def separator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01fc38f84adbdbc18852b29b25658642080d32848882f208e4807fd87fb1c001)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "separator", value)

    @builtins.property
    @jsii.member(jsii_name="suffix")
    def suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suffix"))

    @suffix.setter
    def suffix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7bd5adcc084131031812d0a7aa916f896020fce51eab8abaf6f200e70e70e17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suffix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterEnumMultiple]:
        return typing.cast(typing.Optional[SqlQueryParameterEnumMultiple], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlQueryParameterEnumMultiple],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e0fbf100c524ce5d8a825e8f65662bb1f3cafae2deb7ba93e38ee7eb41d67e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SqlQueryParameterEnumOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryParameterEnumOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__62f118eb3a2e8c27fb06ea7183e504ca5bce21fc59b9ac5034c8f3f33ecabd40)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMultiple")
    def put_multiple(
        self,
        *,
        prefix: builtins.str,
        separator: builtins.str,
        suffix: builtins.str,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#prefix SqlQuery#prefix}.
        :param separator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#separator SqlQuery#separator}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#suffix SqlQuery#suffix}.
        '''
        value = SqlQueryParameterEnumMultiple(
            prefix=prefix, separator=separator, suffix=suffix
        )

        return typing.cast(None, jsii.invoke(self, "putMultiple", [value]))

    @jsii.member(jsii_name="resetMultiple")
    def reset_multiple(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMultiple", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="multiple")
    def multiple(self) -> SqlQueryParameterEnumMultipleOutputReference:
        return typing.cast(SqlQueryParameterEnumMultipleOutputReference, jsii.get(self, "multiple"))

    @builtins.property
    @jsii.member(jsii_name="multipleInput")
    def multiple_input(self) -> typing.Optional[SqlQueryParameterEnumMultiple]:
        return typing.cast(typing.Optional[SqlQueryParameterEnumMultiple], jsii.get(self, "multipleInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb73bb63a96ba60f2f8d72096fa75546b76d268a05362b0cf3e871e01471eba4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42595538d01721f62066e93699c22c5f0c36fd549bba71b793b48fc9f027369b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b25dd8db0abe08fb10a91b01cf94e644763f21e39dc879b32a1e5ae3a1f45a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterEnum]:
        return typing.cast(typing.Optional[SqlQueryParameterEnum], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQueryParameterEnum]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76e607aa04098a8f507adc0b85332acadd9ebe026cb1555bc72d085473ef99f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SqlQueryParameterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryParameterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f137bf4be6b51f7df2e770c252f036eae9d420438315503e61dca5d48bd5c4b6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SqlQueryParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__739d9993c230d4ff95497110469208cc910d1731eb2343d0e8f43881b72009eb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SqlQueryParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27ada4ca9ebde30fdd2115ae45776f65a0c41fd9646c14eae2ca9b69bed1e9e6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4686d42fd613bf9f51dfa1bcc7b364bdd1e374e137d7b4c5cde9d9d5e1072c9f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef50554f13ad099b2573e701a6678e7b96450bc07939c79dd81e128d51caab30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlQueryParameter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlQueryParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlQueryParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__298ff8c40e462b8c7751dd32d865fb81f679c059eec9f65250892f339c56d0e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryParameterNumber",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class SqlQueryParameterNumber:
    def __init__(self, *, value: jsii.Number) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3397a19b52245f3d2aa64bea55ed39705431b937a1bd810d3a6591abae0b3d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterNumber(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterNumberOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryParameterNumberOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b13cc11452962378db122862d28d99641716be80c416c808b9e1b5807a05c469)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f13aafa83bb5e45e7ca5bce4ddf8bec784db3c707bcdbaa1afbaa153958673f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterNumber]:
        return typing.cast(typing.Optional[SqlQueryParameterNumber], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQueryParameterNumber]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60147bff570773764a6d8e513d451bce08aeea85934b232ba46f34c9bf77675f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SqlQueryParameterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryParameterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2cde4d53dcf81393977dad89cf6a2d388af7939bd870657304cc3b093d3c3e1b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDate")
    def put_date(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        value_ = SqlQueryParameterDate(value=value)

        return typing.cast(None, jsii.invoke(self, "putDate", [value_]))

    @jsii.member(jsii_name="putDateRange")
    def put_date_range(
        self,
        *,
        range: typing.Optional[typing.Union[SqlQueryParameterDateRangeRange, typing.Dict[builtins.str, typing.Any]]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#range SqlQuery#range}
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        value_ = SqlQueryParameterDateRange(range=range, value=value)

        return typing.cast(None, jsii.invoke(self, "putDateRange", [value_]))

    @jsii.member(jsii_name="putDatetime")
    def put_datetime(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        value_ = SqlQueryParameterDatetime(value=value)

        return typing.cast(None, jsii.invoke(self, "putDatetime", [value_]))

    @jsii.member(jsii_name="putDatetimeRange")
    def put_datetime_range(
        self,
        *,
        range: typing.Optional[typing.Union[SqlQueryParameterDatetimeRangeRange, typing.Dict[builtins.str, typing.Any]]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#range SqlQuery#range}
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        value_ = SqlQueryParameterDatetimeRange(range=range, value=value)

        return typing.cast(None, jsii.invoke(self, "putDatetimeRange", [value_]))

    @jsii.member(jsii_name="putDatetimesec")
    def put_datetimesec(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        value_ = SqlQueryParameterDatetimesec(value=value)

        return typing.cast(None, jsii.invoke(self, "putDatetimesec", [value_]))

    @jsii.member(jsii_name="putDatetimesecRange")
    def put_datetimesec_range(
        self,
        *,
        range: typing.Optional[typing.Union[SqlQueryParameterDatetimesecRangeRange, typing.Dict[builtins.str, typing.Any]]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#range SqlQuery#range}
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        value_ = SqlQueryParameterDatetimesecRange(range=range, value=value)

        return typing.cast(None, jsii.invoke(self, "putDatetimesecRange", [value_]))

    @jsii.member(jsii_name="putEnum")
    def put_enum(
        self,
        *,
        options: typing.Sequence[builtins.str],
        multiple: typing.Optional[typing.Union[SqlQueryParameterEnumMultiple, typing.Dict[builtins.str, typing.Any]]] = None,
        value: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#options SqlQuery#options}.
        :param multiple: multiple block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#multiple SqlQuery#multiple}
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#values SqlQuery#values}.
        '''
        value_ = SqlQueryParameterEnum(
            options=options, multiple=multiple, value=value, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putEnum", [value_]))

    @jsii.member(jsii_name="putNumber")
    def put_number(self, *, value: jsii.Number) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        value_ = SqlQueryParameterNumber(value=value)

        return typing.cast(None, jsii.invoke(self, "putNumber", [value_]))

    @jsii.member(jsii_name="putQuery")
    def put_query(
        self,
        *,
        query_id: builtins.str,
        multiple: typing.Optional[typing.Union["SqlQueryParameterQueryMultiple", typing.Dict[builtins.str, typing.Any]]] = None,
        value: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param query_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#query_id SqlQuery#query_id}.
        :param multiple: multiple block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#multiple SqlQuery#multiple}
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#values SqlQuery#values}.
        '''
        value_ = SqlQueryParameterQuery(
            query_id=query_id, multiple=multiple, value=value, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putQuery", [value_]))

    @jsii.member(jsii_name="putText")
    def put_text(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        value_ = SqlQueryParameterText(value=value)

        return typing.cast(None, jsii.invoke(self, "putText", [value_]))

    @jsii.member(jsii_name="resetDate")
    def reset_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDate", []))

    @jsii.member(jsii_name="resetDateRange")
    def reset_date_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDateRange", []))

    @jsii.member(jsii_name="resetDatetime")
    def reset_datetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatetime", []))

    @jsii.member(jsii_name="resetDatetimeRange")
    def reset_datetime_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatetimeRange", []))

    @jsii.member(jsii_name="resetDatetimesec")
    def reset_datetimesec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatetimesec", []))

    @jsii.member(jsii_name="resetDatetimesecRange")
    def reset_datetimesec_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatetimesecRange", []))

    @jsii.member(jsii_name="resetEnum")
    def reset_enum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnum", []))

    @jsii.member(jsii_name="resetNumber")
    def reset_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumber", []))

    @jsii.member(jsii_name="resetQuery")
    def reset_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuery", []))

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @builtins.property
    @jsii.member(jsii_name="date")
    def date(self) -> SqlQueryParameterDateOutputReference:
        return typing.cast(SqlQueryParameterDateOutputReference, jsii.get(self, "date"))

    @builtins.property
    @jsii.member(jsii_name="dateRange")
    def date_range(self) -> SqlQueryParameterDateRangeOutputReference:
        return typing.cast(SqlQueryParameterDateRangeOutputReference, jsii.get(self, "dateRange"))

    @builtins.property
    @jsii.member(jsii_name="datetime")
    def datetime(self) -> SqlQueryParameterDatetimeOutputReference:
        return typing.cast(SqlQueryParameterDatetimeOutputReference, jsii.get(self, "datetime"))

    @builtins.property
    @jsii.member(jsii_name="datetimeRange")
    def datetime_range(self) -> SqlQueryParameterDatetimeRangeOutputReference:
        return typing.cast(SqlQueryParameterDatetimeRangeOutputReference, jsii.get(self, "datetimeRange"))

    @builtins.property
    @jsii.member(jsii_name="datetimesec")
    def datetimesec(self) -> SqlQueryParameterDatetimesecOutputReference:
        return typing.cast(SqlQueryParameterDatetimesecOutputReference, jsii.get(self, "datetimesec"))

    @builtins.property
    @jsii.member(jsii_name="datetimesecRange")
    def datetimesec_range(self) -> SqlQueryParameterDatetimesecRangeOutputReference:
        return typing.cast(SqlQueryParameterDatetimesecRangeOutputReference, jsii.get(self, "datetimesecRange"))

    @builtins.property
    @jsii.member(jsii_name="enum")
    def enum(self) -> SqlQueryParameterEnumOutputReference:
        return typing.cast(SqlQueryParameterEnumOutputReference, jsii.get(self, "enum"))

    @builtins.property
    @jsii.member(jsii_name="number")
    def number(self) -> SqlQueryParameterNumberOutputReference:
        return typing.cast(SqlQueryParameterNumberOutputReference, jsii.get(self, "number"))

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> "SqlQueryParameterQueryOutputReference":
        return typing.cast("SqlQueryParameterQueryOutputReference", jsii.get(self, "query"))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> "SqlQueryParameterTextOutputReference":
        return typing.cast("SqlQueryParameterTextOutputReference", jsii.get(self, "text"))

    @builtins.property
    @jsii.member(jsii_name="dateInput")
    def date_input(self) -> typing.Optional[SqlQueryParameterDate]:
        return typing.cast(typing.Optional[SqlQueryParameterDate], jsii.get(self, "dateInput"))

    @builtins.property
    @jsii.member(jsii_name="dateRangeInput")
    def date_range_input(self) -> typing.Optional[SqlQueryParameterDateRange]:
        return typing.cast(typing.Optional[SqlQueryParameterDateRange], jsii.get(self, "dateRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="datetimeInput")
    def datetime_input(self) -> typing.Optional[SqlQueryParameterDatetime]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetime], jsii.get(self, "datetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="datetimeRangeInput")
    def datetime_range_input(self) -> typing.Optional[SqlQueryParameterDatetimeRange]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetimeRange], jsii.get(self, "datetimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="datetimesecInput")
    def datetimesec_input(self) -> typing.Optional[SqlQueryParameterDatetimesec]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetimesec], jsii.get(self, "datetimesecInput"))

    @builtins.property
    @jsii.member(jsii_name="datetimesecRangeInput")
    def datetimesec_range_input(
        self,
    ) -> typing.Optional[SqlQueryParameterDatetimesecRange]:
        return typing.cast(typing.Optional[SqlQueryParameterDatetimesecRange], jsii.get(self, "datetimesecRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="enumInput")
    def enum_input(self) -> typing.Optional[SqlQueryParameterEnum]:
        return typing.cast(typing.Optional[SqlQueryParameterEnum], jsii.get(self, "enumInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="numberInput")
    def number_input(self) -> typing.Optional[SqlQueryParameterNumber]:
        return typing.cast(typing.Optional[SqlQueryParameterNumber], jsii.get(self, "numberInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional["SqlQueryParameterQuery"]:
        return typing.cast(typing.Optional["SqlQueryParameterQuery"], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional["SqlQueryParameterText"]:
        return typing.cast(typing.Optional["SqlQueryParameterText"], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da61f0bac16848301b3cceb4fb857e495ffbc1bb982044f3be5ee9b12d2d00d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77f4dd7475f347006696175b59f2ecd6260bb53d7e093d72a5dd7f8830554f18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SqlQueryParameter, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SqlQueryParameter, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SqlQueryParameter, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4a909b32ff5c8a19d1505853f3200e5d88e14b56677d44332ef5a928cbf28cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryParameterQuery",
    jsii_struct_bases=[],
    name_mapping={
        "query_id": "queryId",
        "multiple": "multiple",
        "value": "value",
        "values": "values",
    },
)
class SqlQueryParameterQuery:
    def __init__(
        self,
        *,
        query_id: builtins.str,
        multiple: typing.Optional[typing.Union["SqlQueryParameterQueryMultiple", typing.Dict[builtins.str, typing.Any]]] = None,
        value: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param query_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#query_id SqlQuery#query_id}.
        :param multiple: multiple block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#multiple SqlQuery#multiple}
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#values SqlQuery#values}.
        '''
        if isinstance(multiple, dict):
            multiple = SqlQueryParameterQueryMultiple(**multiple)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94d43b884f5329fe19b8db6e8a08436958fbf96d2c64c475c4cb95eaa7836cb0)
            check_type(argname="argument query_id", value=query_id, expected_type=type_hints["query_id"])
            check_type(argname="argument multiple", value=multiple, expected_type=type_hints["multiple"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "query_id": query_id,
        }
        if multiple is not None:
            self._values["multiple"] = multiple
        if value is not None:
            self._values["value"] = value
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def query_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#query_id SqlQuery#query_id}.'''
        result = self._values.get("query_id")
        assert result is not None, "Required property 'query_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def multiple(self) -> typing.Optional["SqlQueryParameterQueryMultiple"]:
        '''multiple block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#multiple SqlQuery#multiple}
        '''
        result = self._values.get("multiple")
        return typing.cast(typing.Optional["SqlQueryParameterQueryMultiple"], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#values SqlQuery#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryParameterQueryMultiple",
    jsii_struct_bases=[],
    name_mapping={"prefix": "prefix", "separator": "separator", "suffix": "suffix"},
)
class SqlQueryParameterQueryMultiple:
    def __init__(
        self,
        *,
        prefix: builtins.str,
        separator: builtins.str,
        suffix: builtins.str,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#prefix SqlQuery#prefix}.
        :param separator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#separator SqlQuery#separator}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#suffix SqlQuery#suffix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8a12ccf4018885e7922a798c1d6c60d12857e0fab607f958b4958a0accd3214)
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument separator", value=separator, expected_type=type_hints["separator"])
            check_type(argname="argument suffix", value=suffix, expected_type=type_hints["suffix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "prefix": prefix,
            "separator": separator,
            "suffix": suffix,
        }

    @builtins.property
    def prefix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#prefix SqlQuery#prefix}.'''
        result = self._values.get("prefix")
        assert result is not None, "Required property 'prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def separator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#separator SqlQuery#separator}.'''
        result = self._values.get("separator")
        assert result is not None, "Required property 'separator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def suffix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#suffix SqlQuery#suffix}.'''
        result = self._values.get("suffix")
        assert result is not None, "Required property 'suffix' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterQueryMultiple(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterQueryMultipleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryParameterQueryMultipleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1096c4326762eab2939265c6c27f20719ae66de7bfde028b862c7897a55ffb41)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="separatorInput")
    def separator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "separatorInput"))

    @builtins.property
    @jsii.member(jsii_name="suffixInput")
    def suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "suffixInput"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bafe9ddcc4a6a32e5f0d53b4dd9bd6d4c2780b49ab042fa8928c44b5c2771cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="separator")
    def separator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "separator"))

    @separator.setter
    def separator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__401df0d3353753817dd905152f5672952c59ef5114f215f2e699f7ae4b56cfa8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "separator", value)

    @builtins.property
    @jsii.member(jsii_name="suffix")
    def suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suffix"))

    @suffix.setter
    def suffix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea4f2b013598d144fbfbc234a11a2cc2ad63a6f1eed024b31f3f17717b8a1585)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suffix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterQueryMultiple]:
        return typing.cast(typing.Optional[SqlQueryParameterQueryMultiple], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlQueryParameterQueryMultiple],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29c00b333239c5963ffccd6fc1091f2278921fcbb37cbd109298b4e53e962cf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SqlQueryParameterQueryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryParameterQueryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ad9515c5558c3fec634ce5ac1b65fab4d48ddffc74706e5a3559dfed60b0de2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMultiple")
    def put_multiple(
        self,
        *,
        prefix: builtins.str,
        separator: builtins.str,
        suffix: builtins.str,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#prefix SqlQuery#prefix}.
        :param separator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#separator SqlQuery#separator}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#suffix SqlQuery#suffix}.
        '''
        value = SqlQueryParameterQueryMultiple(
            prefix=prefix, separator=separator, suffix=suffix
        )

        return typing.cast(None, jsii.invoke(self, "putMultiple", [value]))

    @jsii.member(jsii_name="resetMultiple")
    def reset_multiple(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMultiple", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="multiple")
    def multiple(self) -> SqlQueryParameterQueryMultipleOutputReference:
        return typing.cast(SqlQueryParameterQueryMultipleOutputReference, jsii.get(self, "multiple"))

    @builtins.property
    @jsii.member(jsii_name="multipleInput")
    def multiple_input(self) -> typing.Optional[SqlQueryParameterQueryMultiple]:
        return typing.cast(typing.Optional[SqlQueryParameterQueryMultiple], jsii.get(self, "multipleInput"))

    @builtins.property
    @jsii.member(jsii_name="queryIdInput")
    def query_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="queryId")
    def query_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryId"))

    @query_id.setter
    def query_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fe3d7c2a2f73b6a33d994d37977275ec42df67366e39330ee5a10b80d044168)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryId", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22f2a8bdcfd5468440099c3e3bcf0114411fcaaee36a60101decc2345e3bfd2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__272aef5cfc66d12d600fd90594af11b0775022e88ddef9cf153dc49eac92d0d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterQuery]:
        return typing.cast(typing.Optional[SqlQueryParameterQuery], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQueryParameterQuery]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed3eb48fb928fbd96ad7391c61f3602850049b37125d0125101ec0fdec5db1a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryParameterText",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class SqlQueryParameterText:
    def __init__(self, *, value: builtins.str) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1573699cbfe711be2426bd27d100630b2b3878c61d1275a1a4500e2bb61f423b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#value SqlQuery#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryParameterText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryParameterTextOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryParameterTextOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0771f66374e2ee9efcf8d466322f9dec002cc48f81cdc5f47ca43f0d73c4959f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8687da1884923af0345bb5c79092f6fe4f782ab9d442078a47ef94d6d7296f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryParameterText]:
        return typing.cast(typing.Optional[SqlQueryParameterText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQueryParameterText]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__030bdf8695af99d9a2e12cdcf279372d08479ad4f3e9aa9ec5daf2474e98dac9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQuerySchedule",
    jsii_struct_bases=[],
    name_mapping={"continuous": "continuous", "daily": "daily", "weekly": "weekly"},
)
class SqlQuerySchedule:
    def __init__(
        self,
        *,
        continuous: typing.Optional[typing.Union["SqlQueryScheduleContinuous", typing.Dict[builtins.str, typing.Any]]] = None,
        daily: typing.Optional[typing.Union["SqlQueryScheduleDaily", typing.Dict[builtins.str, typing.Any]]] = None,
        weekly: typing.Optional[typing.Union["SqlQueryScheduleWeekly", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param continuous: continuous block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#continuous SqlQuery#continuous}
        :param daily: daily block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#daily SqlQuery#daily}
        :param weekly: weekly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#weekly SqlQuery#weekly}
        '''
        if isinstance(continuous, dict):
            continuous = SqlQueryScheduleContinuous(**continuous)
        if isinstance(daily, dict):
            daily = SqlQueryScheduleDaily(**daily)
        if isinstance(weekly, dict):
            weekly = SqlQueryScheduleWeekly(**weekly)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d0da63288d692f5f93dde90c8a27b592f966e427d8197b1a94c59110e7dd030)
            check_type(argname="argument continuous", value=continuous, expected_type=type_hints["continuous"])
            check_type(argname="argument daily", value=daily, expected_type=type_hints["daily"])
            check_type(argname="argument weekly", value=weekly, expected_type=type_hints["weekly"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if continuous is not None:
            self._values["continuous"] = continuous
        if daily is not None:
            self._values["daily"] = daily
        if weekly is not None:
            self._values["weekly"] = weekly

    @builtins.property
    def continuous(self) -> typing.Optional["SqlQueryScheduleContinuous"]:
        '''continuous block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#continuous SqlQuery#continuous}
        '''
        result = self._values.get("continuous")
        return typing.cast(typing.Optional["SqlQueryScheduleContinuous"], result)

    @builtins.property
    def daily(self) -> typing.Optional["SqlQueryScheduleDaily"]:
        '''daily block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#daily SqlQuery#daily}
        '''
        result = self._values.get("daily")
        return typing.cast(typing.Optional["SqlQueryScheduleDaily"], result)

    @builtins.property
    def weekly(self) -> typing.Optional["SqlQueryScheduleWeekly"]:
        '''weekly block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#weekly SqlQuery#weekly}
        '''
        result = self._values.get("weekly")
        return typing.cast(typing.Optional["SqlQueryScheduleWeekly"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQuerySchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryScheduleContinuous",
    jsii_struct_bases=[],
    name_mapping={"interval_seconds": "intervalSeconds", "until_date": "untilDate"},
)
class SqlQueryScheduleContinuous:
    def __init__(
        self,
        *,
        interval_seconds: jsii.Number,
        until_date: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param interval_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_seconds SqlQuery#interval_seconds}.
        :param until_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9793ed7595943b239246ae398021ab4582bc0075de3f6d8ed55df63ea1c9d7f1)
            check_type(argname="argument interval_seconds", value=interval_seconds, expected_type=type_hints["interval_seconds"])
            check_type(argname="argument until_date", value=until_date, expected_type=type_hints["until_date"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "interval_seconds": interval_seconds,
        }
        if until_date is not None:
            self._values["until_date"] = until_date

    @builtins.property
    def interval_seconds(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_seconds SqlQuery#interval_seconds}.'''
        result = self._values.get("interval_seconds")
        assert result is not None, "Required property 'interval_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def until_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.'''
        result = self._values.get("until_date")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryScheduleContinuous(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryScheduleContinuousOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryScheduleContinuousOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c1eab6fb5f010cd90ed57c4358530598e7bf6e0c78499603d545d5f34a1e2591)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUntilDate")
    def reset_until_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUntilDate", []))

    @builtins.property
    @jsii.member(jsii_name="intervalSecondsInput")
    def interval_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="untilDateInput")
    def until_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "untilDateInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalSeconds")
    def interval_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalSeconds"))

    @interval_seconds.setter
    def interval_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9baa0664e5d7553d61560aefdc39cf5873a31a0051a448d17f498874ed146fb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="untilDate")
    def until_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "untilDate"))

    @until_date.setter
    def until_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eac2112fc3ac6343dc88c5cb4dd9fbb6910191e2b0b0451252b95af5a62c262)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "untilDate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryScheduleContinuous]:
        return typing.cast(typing.Optional[SqlQueryScheduleContinuous], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SqlQueryScheduleContinuous],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9bc774247ae315f2a699261422dc575d520a9ad5e67134b2b77bded052afa66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryScheduleDaily",
    jsii_struct_bases=[],
    name_mapping={
        "interval_days": "intervalDays",
        "time_of_day": "timeOfDay",
        "until_date": "untilDate",
    },
)
class SqlQueryScheduleDaily:
    def __init__(
        self,
        *,
        interval_days: jsii.Number,
        time_of_day: builtins.str,
        until_date: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param interval_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_days SqlQuery#interval_days}.
        :param time_of_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#time_of_day SqlQuery#time_of_day}.
        :param until_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__915bf772fc3c46cb7235ddfec359e3961af5d0ca8e2dd8b908ecb2240f7dfdf9)
            check_type(argname="argument interval_days", value=interval_days, expected_type=type_hints["interval_days"])
            check_type(argname="argument time_of_day", value=time_of_day, expected_type=type_hints["time_of_day"])
            check_type(argname="argument until_date", value=until_date, expected_type=type_hints["until_date"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "interval_days": interval_days,
            "time_of_day": time_of_day,
        }
        if until_date is not None:
            self._values["until_date"] = until_date

    @builtins.property
    def interval_days(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_days SqlQuery#interval_days}.'''
        result = self._values.get("interval_days")
        assert result is not None, "Required property 'interval_days' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def time_of_day(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#time_of_day SqlQuery#time_of_day}.'''
        result = self._values.get("time_of_day")
        assert result is not None, "Required property 'time_of_day' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def until_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.'''
        result = self._values.get("until_date")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryScheduleDaily(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryScheduleDailyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryScheduleDailyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e89b1062b6236ba6ca9724dd74f9c30c4c77abce71e5109f51d93c3d0af63e0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUntilDate")
    def reset_until_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUntilDate", []))

    @builtins.property
    @jsii.member(jsii_name="intervalDaysInput")
    def interval_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="timeOfDayInput")
    def time_of_day_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeOfDayInput"))

    @builtins.property
    @jsii.member(jsii_name="untilDateInput")
    def until_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "untilDateInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalDays")
    def interval_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalDays"))

    @interval_days.setter
    def interval_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ca0fa80d9f77a98d6d40831d8875819a74764afac4997c8cb9aed918fae057c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalDays", value)

    @builtins.property
    @jsii.member(jsii_name="timeOfDay")
    def time_of_day(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeOfDay"))

    @time_of_day.setter
    def time_of_day(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63ce59c23f6cde551e6848edfd4aaa794363ae0ef414fd1b80caf1a024743c8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeOfDay", value)

    @builtins.property
    @jsii.member(jsii_name="untilDate")
    def until_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "untilDate"))

    @until_date.setter
    def until_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aadc4d811945a2b4c0a8e280d8a08f608ddc88ee78d2ced9ce397c298ee736b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "untilDate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryScheduleDaily]:
        return typing.cast(typing.Optional[SqlQueryScheduleDaily], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQueryScheduleDaily]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68ed74de60436bb8afc3f49f9dc5da0e14463249f819ab6e380018b680fc21b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SqlQueryScheduleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryScheduleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e639ff4efe07ea9931ad0d9a9a8136302d8c8438193e522f96bde16d9dec40e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putContinuous")
    def put_continuous(
        self,
        *,
        interval_seconds: jsii.Number,
        until_date: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param interval_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_seconds SqlQuery#interval_seconds}.
        :param until_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.
        '''
        value = SqlQueryScheduleContinuous(
            interval_seconds=interval_seconds, until_date=until_date
        )

        return typing.cast(None, jsii.invoke(self, "putContinuous", [value]))

    @jsii.member(jsii_name="putDaily")
    def put_daily(
        self,
        *,
        interval_days: jsii.Number,
        time_of_day: builtins.str,
        until_date: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param interval_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_days SqlQuery#interval_days}.
        :param time_of_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#time_of_day SqlQuery#time_of_day}.
        :param until_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.
        '''
        value = SqlQueryScheduleDaily(
            interval_days=interval_days, time_of_day=time_of_day, until_date=until_date
        )

        return typing.cast(None, jsii.invoke(self, "putDaily", [value]))

    @jsii.member(jsii_name="putWeekly")
    def put_weekly(
        self,
        *,
        day_of_week: builtins.str,
        interval_weeks: jsii.Number,
        time_of_day: builtins.str,
        until_date: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param day_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#day_of_week SqlQuery#day_of_week}.
        :param interval_weeks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_weeks SqlQuery#interval_weeks}.
        :param time_of_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#time_of_day SqlQuery#time_of_day}.
        :param until_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.
        '''
        value = SqlQueryScheduleWeekly(
            day_of_week=day_of_week,
            interval_weeks=interval_weeks,
            time_of_day=time_of_day,
            until_date=until_date,
        )

        return typing.cast(None, jsii.invoke(self, "putWeekly", [value]))

    @jsii.member(jsii_name="resetContinuous")
    def reset_continuous(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContinuous", []))

    @jsii.member(jsii_name="resetDaily")
    def reset_daily(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDaily", []))

    @jsii.member(jsii_name="resetWeekly")
    def reset_weekly(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeekly", []))

    @builtins.property
    @jsii.member(jsii_name="continuous")
    def continuous(self) -> SqlQueryScheduleContinuousOutputReference:
        return typing.cast(SqlQueryScheduleContinuousOutputReference, jsii.get(self, "continuous"))

    @builtins.property
    @jsii.member(jsii_name="daily")
    def daily(self) -> SqlQueryScheduleDailyOutputReference:
        return typing.cast(SqlQueryScheduleDailyOutputReference, jsii.get(self, "daily"))

    @builtins.property
    @jsii.member(jsii_name="weekly")
    def weekly(self) -> "SqlQueryScheduleWeeklyOutputReference":
        return typing.cast("SqlQueryScheduleWeeklyOutputReference", jsii.get(self, "weekly"))

    @builtins.property
    @jsii.member(jsii_name="continuousInput")
    def continuous_input(self) -> typing.Optional[SqlQueryScheduleContinuous]:
        return typing.cast(typing.Optional[SqlQueryScheduleContinuous], jsii.get(self, "continuousInput"))

    @builtins.property
    @jsii.member(jsii_name="dailyInput")
    def daily_input(self) -> typing.Optional[SqlQueryScheduleDaily]:
        return typing.cast(typing.Optional[SqlQueryScheduleDaily], jsii.get(self, "dailyInput"))

    @builtins.property
    @jsii.member(jsii_name="weeklyInput")
    def weekly_input(self) -> typing.Optional["SqlQueryScheduleWeekly"]:
        return typing.cast(typing.Optional["SqlQueryScheduleWeekly"], jsii.get(self, "weeklyInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQuerySchedule]:
        return typing.cast(typing.Optional[SqlQuerySchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQuerySchedule]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ae3bcca35e85afd04003075cd1bff9c76c30e2f48927801c0d4939b5415154c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlQuery.SqlQueryScheduleWeekly",
    jsii_struct_bases=[],
    name_mapping={
        "day_of_week": "dayOfWeek",
        "interval_weeks": "intervalWeeks",
        "time_of_day": "timeOfDay",
        "until_date": "untilDate",
    },
)
class SqlQueryScheduleWeekly:
    def __init__(
        self,
        *,
        day_of_week: builtins.str,
        interval_weeks: jsii.Number,
        time_of_day: builtins.str,
        until_date: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param day_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#day_of_week SqlQuery#day_of_week}.
        :param interval_weeks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_weeks SqlQuery#interval_weeks}.
        :param time_of_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#time_of_day SqlQuery#time_of_day}.
        :param until_date: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b59fbee5dfa53edfc797e8ffc9659a94df64174be6e5e7e6f6b8c30fea1224df)
            check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
            check_type(argname="argument interval_weeks", value=interval_weeks, expected_type=type_hints["interval_weeks"])
            check_type(argname="argument time_of_day", value=time_of_day, expected_type=type_hints["time_of_day"])
            check_type(argname="argument until_date", value=until_date, expected_type=type_hints["until_date"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "day_of_week": day_of_week,
            "interval_weeks": interval_weeks,
            "time_of_day": time_of_day,
        }
        if until_date is not None:
            self._values["until_date"] = until_date

    @builtins.property
    def day_of_week(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#day_of_week SqlQuery#day_of_week}.'''
        result = self._values.get("day_of_week")
        assert result is not None, "Required property 'day_of_week' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def interval_weeks(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#interval_weeks SqlQuery#interval_weeks}.'''
        result = self._values.get("interval_weeks")
        assert result is not None, "Required property 'interval_weeks' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def time_of_day(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#time_of_day SqlQuery#time_of_day}.'''
        result = self._values.get("time_of_day")
        assert result is not None, "Required property 'time_of_day' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def until_date(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_query#until_date SqlQuery#until_date}.'''
        result = self._values.get("until_date")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlQueryScheduleWeekly(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlQueryScheduleWeeklyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlQuery.SqlQueryScheduleWeeklyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c5848ac372b5a252250da719b99c59767dc429201a1eb241e10db15ff9bca5a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUntilDate")
    def reset_until_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUntilDate", []))

    @builtins.property
    @jsii.member(jsii_name="dayOfWeekInput")
    def day_of_week_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalWeeksInput")
    def interval_weeks_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalWeeksInput"))

    @builtins.property
    @jsii.member(jsii_name="timeOfDayInput")
    def time_of_day_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeOfDayInput"))

    @builtins.property
    @jsii.member(jsii_name="untilDateInput")
    def until_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "untilDateInput"))

    @builtins.property
    @jsii.member(jsii_name="dayOfWeek")
    def day_of_week(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayOfWeek"))

    @day_of_week.setter
    def day_of_week(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f88c2e2d24c47744bdebe9619e327b705251001e6b963a6193d1f0d8bfe8ea39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfWeek", value)

    @builtins.property
    @jsii.member(jsii_name="intervalWeeks")
    def interval_weeks(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalWeeks"))

    @interval_weeks.setter
    def interval_weeks(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a9b2dac9545a1e51b67db4ebeeabe6b62285231a695b211f14a69d0eb594ae1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalWeeks", value)

    @builtins.property
    @jsii.member(jsii_name="timeOfDay")
    def time_of_day(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeOfDay"))

    @time_of_day.setter
    def time_of_day(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adc03cb8d73259fc66b8988f21d0058857ea65354adb136fcfcf03ff65a8dbd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeOfDay", value)

    @builtins.property
    @jsii.member(jsii_name="untilDate")
    def until_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "untilDate"))

    @until_date.setter
    def until_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e776d31e5dae854ae614f311b3b1b30c4f0b738aaef1837cbbcbfbd8570db8dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "untilDate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlQueryScheduleWeekly]:
        return typing.cast(typing.Optional[SqlQueryScheduleWeekly], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlQueryScheduleWeekly]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5616489962796cf37067ef57aa0cd68834023e0b3002e65c6ab39cbbe326f6f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SqlQuery",
    "SqlQueryConfig",
    "SqlQueryParameter",
    "SqlQueryParameterDate",
    "SqlQueryParameterDateOutputReference",
    "SqlQueryParameterDateRange",
    "SqlQueryParameterDateRangeOutputReference",
    "SqlQueryParameterDateRangeRange",
    "SqlQueryParameterDateRangeRangeOutputReference",
    "SqlQueryParameterDatetime",
    "SqlQueryParameterDatetimeOutputReference",
    "SqlQueryParameterDatetimeRange",
    "SqlQueryParameterDatetimeRangeOutputReference",
    "SqlQueryParameterDatetimeRangeRange",
    "SqlQueryParameterDatetimeRangeRangeOutputReference",
    "SqlQueryParameterDatetimesec",
    "SqlQueryParameterDatetimesecOutputReference",
    "SqlQueryParameterDatetimesecRange",
    "SqlQueryParameterDatetimesecRangeOutputReference",
    "SqlQueryParameterDatetimesecRangeRange",
    "SqlQueryParameterDatetimesecRangeRangeOutputReference",
    "SqlQueryParameterEnum",
    "SqlQueryParameterEnumMultiple",
    "SqlQueryParameterEnumMultipleOutputReference",
    "SqlQueryParameterEnumOutputReference",
    "SqlQueryParameterList",
    "SqlQueryParameterNumber",
    "SqlQueryParameterNumberOutputReference",
    "SqlQueryParameterOutputReference",
    "SqlQueryParameterQuery",
    "SqlQueryParameterQueryMultiple",
    "SqlQueryParameterQueryMultipleOutputReference",
    "SqlQueryParameterQueryOutputReference",
    "SqlQueryParameterText",
    "SqlQueryParameterTextOutputReference",
    "SqlQuerySchedule",
    "SqlQueryScheduleContinuous",
    "SqlQueryScheduleContinuousOutputReference",
    "SqlQueryScheduleDaily",
    "SqlQueryScheduleDailyOutputReference",
    "SqlQueryScheduleOutputReference",
    "SqlQueryScheduleWeekly",
    "SqlQueryScheduleWeeklyOutputReference",
]

publication.publish()

def _typecheckingstub__5048304b7db0e775e4f0e8161fa3cca352da818cb20821d62763511cbbf9fcea(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    data_source_id: builtins.str,
    name: builtins.str,
    query: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SqlQueryParameter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    parent: typing.Optional[builtins.str] = None,
    run_as_role: typing.Optional[builtins.str] = None,
    schedule: typing.Optional[typing.Union[SqlQuerySchedule, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__9111d59c07c9d5941b9f8411a812c57b7af9551ee6e4e62a11602d488f0b79db(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SqlQueryParameter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8f5f6aab48ed48226f42ebcdb27ca3701bfa8654ff293c393aa16a2bc5db1bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fc459dbc58a29a6934114324dda457ebe39f833874569ad3b3bfeacb4a61891(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__741908d1a5b0f3e9cc12176a82620d9e6b0cb8df5f9849e27891665388481b28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a18916e62c842bcb72130a072bdfaaa4d8c7d08e4ca6fec1505568ee4d0ab276(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76e63f7f68cfbe8ea6f76104ee7d50be0b4d591742cb3e30a629be9ccbd7bbbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d769f6a1f7e4537581c496b37d603e1f82f0a5128e5ce6bcea5643edcd4b6183(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b96d5f1ceb93e08af968c7e48a84c60ff3ba468bc2c0accb8e52f02c1d40346d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed81771e47b5f80097e3d12b269f22b89e5d0d4a78b1075da335fc0ac2e29298(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c78c8e10068be6af9a9af7af59b3d2a77d1de2525dd4a372344e77737b6e2fb(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    data_source_id: builtins.str,
    name: builtins.str,
    query: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SqlQueryParameter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    parent: typing.Optional[builtins.str] = None,
    run_as_role: typing.Optional[builtins.str] = None,
    schedule: typing.Optional[typing.Union[SqlQuerySchedule, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a0b7813a7d790f4136f838141f5388989a4774e74407b829cc81dcae2b24bd6(
    *,
    name: builtins.str,
    date: typing.Optional[typing.Union[SqlQueryParameterDate, typing.Dict[builtins.str, typing.Any]]] = None,
    date_range: typing.Optional[typing.Union[SqlQueryParameterDateRange, typing.Dict[builtins.str, typing.Any]]] = None,
    datetime: typing.Optional[typing.Union[SqlQueryParameterDatetime, typing.Dict[builtins.str, typing.Any]]] = None,
    datetime_range: typing.Optional[typing.Union[SqlQueryParameterDatetimeRange, typing.Dict[builtins.str, typing.Any]]] = None,
    datetimesec: typing.Optional[typing.Union[SqlQueryParameterDatetimesec, typing.Dict[builtins.str, typing.Any]]] = None,
    datetimesec_range: typing.Optional[typing.Union[SqlQueryParameterDatetimesecRange, typing.Dict[builtins.str, typing.Any]]] = None,
    enum: typing.Optional[typing.Union[SqlQueryParameterEnum, typing.Dict[builtins.str, typing.Any]]] = None,
    number: typing.Optional[typing.Union[SqlQueryParameterNumber, typing.Dict[builtins.str, typing.Any]]] = None,
    query: typing.Optional[typing.Union[SqlQueryParameterQuery, typing.Dict[builtins.str, typing.Any]]] = None,
    text: typing.Optional[typing.Union[SqlQueryParameterText, typing.Dict[builtins.str, typing.Any]]] = None,
    title: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca5e16a1f32adf552a88ee913bb2dd7c3eae264f105d77ef768af0a79146c878(
    *,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33dcc146d942573fd37f0c12b41ad8d58a459f206c1ae4c4a4525aadbfa986cc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f75f158a4e5b2d97882e2293a1c644cc0927e286064da2931e81c7cd204e164(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ca1ae3a9a8ebdef21a234475bf9f1b5c906083e38abf3d69501366042eea009(
    value: typing.Optional[SqlQueryParameterDate],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6aba251e2c9f46e8c7f567cf4890223328a6b1dec48fe605450410932e82950(
    *,
    range: typing.Optional[typing.Union[SqlQueryParameterDateRangeRange, typing.Dict[builtins.str, typing.Any]]] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06d33f75360eba954d0d1d34684f2fbd927a6855fd3e3e8be22808122b849e4c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24ebbb67ea694ac48249ef1fe7212f773e4bc270cca907bc167546adcddcee7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae925dadbcbc0a06ca0ac7821306f8dcee2bcd6747fba47904edb94e24e2834f(
    value: typing.Optional[SqlQueryParameterDateRange],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8697c2f0343cdff058601303594f941de349c15574b64b9cf007bdb9cbc7990d(
    *,
    end: builtins.str,
    start: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fe8d4eb0d9f7291f3f51e6a857bf5b2fd89d311f4139f8c0bc118231a23b43f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16698838cae795aac758d14ee6e1aa64893209d49de99ce5e75acd3bc3106000(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27857db834cfe6251d60cdbcbf9a29608865493b544aee8f837d842774fd6d38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad7d5287b82bc044593c59b20d5f75df655713b19924d0e7685ebeafc3268df5(
    value: typing.Optional[SqlQueryParameterDateRangeRange],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd66c816f3c1558a0d0717d816c71d3f87ce292fc00df0dfa4b164134b0997b5(
    *,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b33645a092cfbb722bd0c1deb0416060684809f453c08454add7278eb1b942a0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e13c64d9024006550415b6761a4edf5923567c3571f83648e0f7bd65222f69c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a69525046759542a4b6438482a7bbfdbd241e65f6de52946deae767d3a4c5220(
    value: typing.Optional[SqlQueryParameterDatetime],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed07840685ae9d7a5cb86e90417e5ed480e2904f6ed6688d5e43eb3e5a90c1ed(
    *,
    range: typing.Optional[typing.Union[SqlQueryParameterDatetimeRangeRange, typing.Dict[builtins.str, typing.Any]]] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ec96223936c810eea8c2335964a1174bd03c13019e76ab04e147e7a61eafb5a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db3ea3430bb906c9a791d512da10b651d0eb41a014d80d57991c4465b50813d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9c2c66f2ac207085785300f2b339adfe2ef9c5ac8bd7623aa31e1de968c9c21(
    value: typing.Optional[SqlQueryParameterDatetimeRange],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f395b9278422880d001a70ee786160379316013415bd1ef49aeaffe065425d89(
    *,
    end: builtins.str,
    start: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31a04ffa2e80a0730edb74313b28b3be5b91d15fee091d0f10591a42397facc7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f9837d18695e6315e593765b0468cfb10fc252e05de5562d86b34e9de1a7750(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8823a4212862892abba8150849244156ade2801e5ae31cc148989de3121c5fe7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6d05773ec5cec2d960a1446907be164a577b92b1f0d418dae66def4176a820a(
    value: typing.Optional[SqlQueryParameterDatetimeRangeRange],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92be823e2ae56b9d2a05c513dd29c5364d1ccb74887dc089524211977ceb81ea(
    *,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__446612324a849a4f8084404df4d5efefd04c1fdd9835e07667030738bfe2fcdb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18b4680c55208358753e3ca2ef00735aeee6e543a1dcb5ad8414e4cf4d694f38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3090a5944ac75376eb9bc94c021162d16aa935de8ef30271240a8d9db315a2a3(
    value: typing.Optional[SqlQueryParameterDatetimesec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee38a8ed3b2968fb9387dff05486f06ac792f803843d3d655aa3482c39d765ea(
    *,
    range: typing.Optional[typing.Union[SqlQueryParameterDatetimesecRangeRange, typing.Dict[builtins.str, typing.Any]]] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec63078ea19aeb5d79267b932d37e3e1a985294f928f235c849df56c5650d629(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77c9fac0089266c4674ab528c5e840b226371564e6a359af1e0e106988548571(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6b38a8a47fab504053b439652092d7d06709e991314c762402dd0fe46d3ada2(
    value: typing.Optional[SqlQueryParameterDatetimesecRange],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1215ce01f13e8c7b671035455d485506481f75c09c944037f3c600ffbc7db9c6(
    *,
    end: builtins.str,
    start: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__168ed7096bb5107cfaf2cd48c8db6470f6ee0145547a0c21be26fec14ffdea30(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffa9d0e237c06d5c2a57f8bb73ec3d5333ee27a4d2ff29803661ee1ccccd2916(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f139f2822a0faf6c6eb134cc6da1ab9bfcce50c08d8dda3370022b5cb8ac15b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff3f7464de25a3faf188799a0dea6089e48a6c1c8f71c378db32d5e7f6ff263a(
    value: typing.Optional[SqlQueryParameterDatetimesecRangeRange],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53bcbccefc239f31c076143b21392267da548e3008137a317e4166d24942f83c(
    *,
    options: typing.Sequence[builtins.str],
    multiple: typing.Optional[typing.Union[SqlQueryParameterEnumMultiple, typing.Dict[builtins.str, typing.Any]]] = None,
    value: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6155389546d6426cf71db0c4f02adc20f3a4d3035991db094bb07d6844ac24c(
    *,
    prefix: builtins.str,
    separator: builtins.str,
    suffix: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acbc6ac055d15c33340ea8f03e390d4fec07c6025ee3e6f8374099a1e1444b89(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__027f6bf1d4e35066b57ebab7ae94d0c062d97b9827c77c776bc2068d853ddc00(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01fc38f84adbdbc18852b29b25658642080d32848882f208e4807fd87fb1c001(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7bd5adcc084131031812d0a7aa916f896020fce51eab8abaf6f200e70e70e17(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e0fbf100c524ce5d8a825e8f65662bb1f3cafae2deb7ba93e38ee7eb41d67e9(
    value: typing.Optional[SqlQueryParameterEnumMultiple],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62f118eb3a2e8c27fb06ea7183e504ca5bce21fc59b9ac5034c8f3f33ecabd40(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb73bb63a96ba60f2f8d72096fa75546b76d268a05362b0cf3e871e01471eba4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42595538d01721f62066e93699c22c5f0c36fd549bba71b793b48fc9f027369b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b25dd8db0abe08fb10a91b01cf94e644763f21e39dc879b32a1e5ae3a1f45a8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76e607aa04098a8f507adc0b85332acadd9ebe026cb1555bc72d085473ef99f1(
    value: typing.Optional[SqlQueryParameterEnum],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f137bf4be6b51f7df2e770c252f036eae9d420438315503e61dca5d48bd5c4b6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__739d9993c230d4ff95497110469208cc910d1731eb2343d0e8f43881b72009eb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27ada4ca9ebde30fdd2115ae45776f65a0c41fd9646c14eae2ca9b69bed1e9e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4686d42fd613bf9f51dfa1bcc7b364bdd1e374e137d7b4c5cde9d9d5e1072c9f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef50554f13ad099b2573e701a6678e7b96450bc07939c79dd81e128d51caab30(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__298ff8c40e462b8c7751dd32d865fb81f679c059eec9f65250892f339c56d0e0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlQueryParameter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3397a19b52245f3d2aa64bea55ed39705431b937a1bd810d3a6591abae0b3d7(
    *,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b13cc11452962378db122862d28d99641716be80c416c808b9e1b5807a05c469(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f13aafa83bb5e45e7ca5bce4ddf8bec784db3c707bcdbaa1afbaa153958673f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60147bff570773764a6d8e513d451bce08aeea85934b232ba46f34c9bf77675f(
    value: typing.Optional[SqlQueryParameterNumber],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cde4d53dcf81393977dad89cf6a2d388af7939bd870657304cc3b093d3c3e1b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da61f0bac16848301b3cceb4fb857e495ffbc1bb982044f3be5ee9b12d2d00d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77f4dd7475f347006696175b59f2ecd6260bb53d7e093d72a5dd7f8830554f18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4a909b32ff5c8a19d1505853f3200e5d88e14b56677d44332ef5a928cbf28cb(
    value: typing.Optional[typing.Union[SqlQueryParameter, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94d43b884f5329fe19b8db6e8a08436958fbf96d2c64c475c4cb95eaa7836cb0(
    *,
    query_id: builtins.str,
    multiple: typing.Optional[typing.Union[SqlQueryParameterQueryMultiple, typing.Dict[builtins.str, typing.Any]]] = None,
    value: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8a12ccf4018885e7922a798c1d6c60d12857e0fab607f958b4958a0accd3214(
    *,
    prefix: builtins.str,
    separator: builtins.str,
    suffix: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1096c4326762eab2939265c6c27f20719ae66de7bfde028b862c7897a55ffb41(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bafe9ddcc4a6a32e5f0d53b4dd9bd6d4c2780b49ab042fa8928c44b5c2771cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__401df0d3353753817dd905152f5672952c59ef5114f215f2e699f7ae4b56cfa8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea4f2b013598d144fbfbc234a11a2cc2ad63a6f1eed024b31f3f17717b8a1585(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29c00b333239c5963ffccd6fc1091f2278921fcbb37cbd109298b4e53e962cf1(
    value: typing.Optional[SqlQueryParameterQueryMultiple],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ad9515c5558c3fec634ce5ac1b65fab4d48ddffc74706e5a3559dfed60b0de2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fe3d7c2a2f73b6a33d994d37977275ec42df67366e39330ee5a10b80d044168(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22f2a8bdcfd5468440099c3e3bcf0114411fcaaee36a60101decc2345e3bfd2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__272aef5cfc66d12d600fd90594af11b0775022e88ddef9cf153dc49eac92d0d8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed3eb48fb928fbd96ad7391c61f3602850049b37125d0125101ec0fdec5db1a4(
    value: typing.Optional[SqlQueryParameterQuery],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1573699cbfe711be2426bd27d100630b2b3878c61d1275a1a4500e2bb61f423b(
    *,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0771f66374e2ee9efcf8d466322f9dec002cc48f81cdc5f47ca43f0d73c4959f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8687da1884923af0345bb5c79092f6fe4f782ab9d442078a47ef94d6d7296f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__030bdf8695af99d9a2e12cdcf279372d08479ad4f3e9aa9ec5daf2474e98dac9(
    value: typing.Optional[SqlQueryParameterText],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d0da63288d692f5f93dde90c8a27b592f966e427d8197b1a94c59110e7dd030(
    *,
    continuous: typing.Optional[typing.Union[SqlQueryScheduleContinuous, typing.Dict[builtins.str, typing.Any]]] = None,
    daily: typing.Optional[typing.Union[SqlQueryScheduleDaily, typing.Dict[builtins.str, typing.Any]]] = None,
    weekly: typing.Optional[typing.Union[SqlQueryScheduleWeekly, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9793ed7595943b239246ae398021ab4582bc0075de3f6d8ed55df63ea1c9d7f1(
    *,
    interval_seconds: jsii.Number,
    until_date: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1eab6fb5f010cd90ed57c4358530598e7bf6e0c78499603d545d5f34a1e2591(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9baa0664e5d7553d61560aefdc39cf5873a31a0051a448d17f498874ed146fb8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eac2112fc3ac6343dc88c5cb4dd9fbb6910191e2b0b0451252b95af5a62c262(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9bc774247ae315f2a699261422dc575d520a9ad5e67134b2b77bded052afa66(
    value: typing.Optional[SqlQueryScheduleContinuous],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__915bf772fc3c46cb7235ddfec359e3961af5d0ca8e2dd8b908ecb2240f7dfdf9(
    *,
    interval_days: jsii.Number,
    time_of_day: builtins.str,
    until_date: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e89b1062b6236ba6ca9724dd74f9c30c4c77abce71e5109f51d93c3d0af63e0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ca0fa80d9f77a98d6d40831d8875819a74764afac4997c8cb9aed918fae057c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63ce59c23f6cde551e6848edfd4aaa794363ae0ef414fd1b80caf1a024743c8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aadc4d811945a2b4c0a8e280d8a08f608ddc88ee78d2ced9ce397c298ee736b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68ed74de60436bb8afc3f49f9dc5da0e14463249f819ab6e380018b680fc21b7(
    value: typing.Optional[SqlQueryScheduleDaily],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e639ff4efe07ea9931ad0d9a9a8136302d8c8438193e522f96bde16d9dec40e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ae3bcca35e85afd04003075cd1bff9c76c30e2f48927801c0d4939b5415154c(
    value: typing.Optional[SqlQuerySchedule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b59fbee5dfa53edfc797e8ffc9659a94df64174be6e5e7e6f6b8c30fea1224df(
    *,
    day_of_week: builtins.str,
    interval_weeks: jsii.Number,
    time_of_day: builtins.str,
    until_date: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c5848ac372b5a252250da719b99c59767dc429201a1eb241e10db15ff9bca5a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f88c2e2d24c47744bdebe9619e327b705251001e6b963a6193d1f0d8bfe8ea39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a9b2dac9545a1e51b67db4ebeeabe6b62285231a695b211f14a69d0eb594ae1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adc03cb8d73259fc66b8988f21d0058857ea65354adb136fcfcf03ff65a8dbd5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e776d31e5dae854ae614f311b3b1b30c4f0b738aaef1837cbbcbfbd8570db8dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5616489962796cf37067ef57aa0cd68834023e0b3002e65c6ab39cbbe326f6f7(
    value: typing.Optional[SqlQueryScheduleWeekly],
) -> None:
    """Type checking stubs"""
    pass
