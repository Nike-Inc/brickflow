'''
# `databricks_sql_alert`

Refer to the Terraform Registory for docs: [`databricks_sql_alert`](https://www.terraform.io/docs/providers/databricks/r/sql_alert).
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


class SqlAlert(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlAlert.SqlAlert",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert databricks_sql_alert}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        options: typing.Union["SqlAlertOptions", typing.Dict[builtins.str, typing.Any]],
        query_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        parent: typing.Optional[builtins.str] = None,
        rearm: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert databricks_sql_alert} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#name SqlAlert#name}.
        :param options: options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#options SqlAlert#options}
        :param query_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#query_id SqlAlert#query_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#id SqlAlert#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#parent SqlAlert#parent}.
        :param rearm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#rearm SqlAlert#rearm}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__634415514a44b117ba54df0acd3fd0bfa1b86531c6e003db7a5b4b9683d3c357)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SqlAlertConfig(
            name=name,
            options=options,
            query_id=query_id,
            id=id,
            parent=parent,
            rearm=rearm,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putOptions")
    def put_options(
        self,
        *,
        column: builtins.str,
        op: builtins.str,
        value: builtins.str,
        custom_body: typing.Optional[builtins.str] = None,
        custom_subject: typing.Optional[builtins.str] = None,
        muted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#column SqlAlert#column}.
        :param op: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#op SqlAlert#op}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#value SqlAlert#value}.
        :param custom_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#custom_body SqlAlert#custom_body}.
        :param custom_subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#custom_subject SqlAlert#custom_subject}.
        :param muted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#muted SqlAlert#muted}.
        '''
        value_ = SqlAlertOptions(
            column=column,
            op=op,
            value=value,
            custom_body=custom_body,
            custom_subject=custom_subject,
            muted=muted,
        )

        return typing.cast(None, jsii.invoke(self, "putOptions", [value_]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetParent")
    def reset_parent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParent", []))

    @jsii.member(jsii_name="resetRearm")
    def reset_rearm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRearm", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> "SqlAlertOptionsOutputReference":
        return typing.cast("SqlAlertOptionsOutputReference", jsii.get(self, "options"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(self) -> typing.Optional["SqlAlertOptions"]:
        return typing.cast(typing.Optional["SqlAlertOptions"], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="parentInput")
    def parent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentInput"))

    @builtins.property
    @jsii.member(jsii_name="queryIdInput")
    def query_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="rearmInput")
    def rearm_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rearmInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f0379d1cc48cdf7c58355498d45f41159a8c18640067cd4754af77b77a7bb3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a45d96374a89b26c0d3559d12f58c274f9eb88c06309958452aaae6c470ce3f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parent"))

    @parent.setter
    def parent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4c4ab61f5a391e585c4af010666ec366f392169548f68363b2318b9c8f94665)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parent", value)

    @builtins.property
    @jsii.member(jsii_name="queryId")
    def query_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryId"))

    @query_id.setter
    def query_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67dd37061e41371e3d24f30e875faa61d8cfe759472e55d480b54abd6b798fec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryId", value)

    @builtins.property
    @jsii.member(jsii_name="rearm")
    def rearm(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rearm"))

    @rearm.setter
    def rearm(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65705fc4b93f0d01e988d25547f168a618d8e1b6e8d202ae08eee0390d590413)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rearm", value)


@jsii.data_type(
    jsii_type="databricks.sqlAlert.SqlAlertConfig",
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
        "options": "options",
        "query_id": "queryId",
        "id": "id",
        "parent": "parent",
        "rearm": "rearm",
    },
)
class SqlAlertConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        options: typing.Union["SqlAlertOptions", typing.Dict[builtins.str, typing.Any]],
        query_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        parent: typing.Optional[builtins.str] = None,
        rearm: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#name SqlAlert#name}.
        :param options: options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#options SqlAlert#options}
        :param query_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#query_id SqlAlert#query_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#id SqlAlert#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#parent SqlAlert#parent}.
        :param rearm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#rearm SqlAlert#rearm}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(options, dict):
            options = SqlAlertOptions(**options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__233f97a866dceebe631f62ae2fd8ee58c1c0acddc96e2bb0a1ddef5ea6033db6)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument query_id", value=query_id, expected_type=type_hints["query_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument rearm", value=rearm, expected_type=type_hints["rearm"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "options": options,
            "query_id": query_id,
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
        if id is not None:
            self._values["id"] = id
        if parent is not None:
            self._values["parent"] = parent
        if rearm is not None:
            self._values["rearm"] = rearm

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#name SqlAlert#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def options(self) -> "SqlAlertOptions":
        '''options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#options SqlAlert#options}
        '''
        result = self._values.get("options")
        assert result is not None, "Required property 'options' is missing"
        return typing.cast("SqlAlertOptions", result)

    @builtins.property
    def query_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#query_id SqlAlert#query_id}.'''
        result = self._values.get("query_id")
        assert result is not None, "Required property 'query_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#id SqlAlert#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#parent SqlAlert#parent}.'''
        result = self._values.get("parent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rearm(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#rearm SqlAlert#rearm}.'''
        result = self._values.get("rearm")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlAlertConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.sqlAlert.SqlAlertOptions",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "op": "op",
        "value": "value",
        "custom_body": "customBody",
        "custom_subject": "customSubject",
        "muted": "muted",
    },
)
class SqlAlertOptions:
    def __init__(
        self,
        *,
        column: builtins.str,
        op: builtins.str,
        value: builtins.str,
        custom_body: typing.Optional[builtins.str] = None,
        custom_subject: typing.Optional[builtins.str] = None,
        muted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#column SqlAlert#column}.
        :param op: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#op SqlAlert#op}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#value SqlAlert#value}.
        :param custom_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#custom_body SqlAlert#custom_body}.
        :param custom_subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#custom_subject SqlAlert#custom_subject}.
        :param muted: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#muted SqlAlert#muted}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce20cc2a4a4a2ec925632604b9f9c7f19a8e666356aa725845d35a27d3d8cdab)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument op", value=op, expected_type=type_hints["op"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument custom_body", value=custom_body, expected_type=type_hints["custom_body"])
            check_type(argname="argument custom_subject", value=custom_subject, expected_type=type_hints["custom_subject"])
            check_type(argname="argument muted", value=muted, expected_type=type_hints["muted"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "column": column,
            "op": op,
            "value": value,
        }
        if custom_body is not None:
            self._values["custom_body"] = custom_body
        if custom_subject is not None:
            self._values["custom_subject"] = custom_subject
        if muted is not None:
            self._values["muted"] = muted

    @builtins.property
    def column(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#column SqlAlert#column}.'''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def op(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#op SqlAlert#op}.'''
        result = self._values.get("op")
        assert result is not None, "Required property 'op' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#value SqlAlert#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_body(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#custom_body SqlAlert#custom_body}.'''
        result = self._values.get("custom_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_subject(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#custom_subject SqlAlert#custom_subject}.'''
        result = self._values.get("custom_subject")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def muted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_alert#muted SqlAlert#muted}.'''
        result = self._values.get("muted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlAlertOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlAlertOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlAlert.SqlAlertOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__22870f40d2999d96ffd327f3f7e646f06bdf0769d7c2860e2fab4fe4e7dda0d6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCustomBody")
    def reset_custom_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomBody", []))

    @jsii.member(jsii_name="resetCustomSubject")
    def reset_custom_subject(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomSubject", []))

    @jsii.member(jsii_name="resetMuted")
    def reset_muted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMuted", []))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="customBodyInput")
    def custom_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="customSubjectInput")
    def custom_subject_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customSubjectInput"))

    @builtins.property
    @jsii.member(jsii_name="mutedInput")
    def muted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "mutedInput"))

    @builtins.property
    @jsii.member(jsii_name="opInput")
    def op_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "opInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "column"))

    @column.setter
    def column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d46b8995879b3af53e5e9794c1b53d214b4d9a0c60873f6188e46402416a2c0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="customBody")
    def custom_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customBody"))

    @custom_body.setter
    def custom_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1f64457a00adcca0638e6043c575139d2a18b7250c167b9e1d08fbfe0c3d506)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customBody", value)

    @builtins.property
    @jsii.member(jsii_name="customSubject")
    def custom_subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customSubject"))

    @custom_subject.setter
    def custom_subject(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd5de4ea2b8106c7c14456033867499cfa7476fa11a21ae400557e45ec5950ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customSubject", value)

    @builtins.property
    @jsii.member(jsii_name="muted")
    def muted(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "muted"))

    @muted.setter
    def muted(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__167e83e17c150e78f63ec26912d75866f37d5ecd1f3c9892f115867124c24c9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "muted", value)

    @builtins.property
    @jsii.member(jsii_name="op")
    def op(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "op"))

    @op.setter
    def op(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff04a0fc8701b8ec0dc2f318bdeadb89fcccc5dd48e4eef9ffd9512659a29115)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "op", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d80d2d374e111f7693f5a5862da1f7e385b817ecf9e8f1af9d78b96bd50ec29b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlAlertOptions]:
        return typing.cast(typing.Optional[SqlAlertOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlAlertOptions]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca372fcd7a1cbc9437edf626ee19e091a6dccff8541712da3fc2e43b26413af3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SqlAlert",
    "SqlAlertConfig",
    "SqlAlertOptions",
    "SqlAlertOptionsOutputReference",
]

publication.publish()

def _typecheckingstub__634415514a44b117ba54df0acd3fd0bfa1b86531c6e003db7a5b4b9683d3c357(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    options: typing.Union[SqlAlertOptions, typing.Dict[builtins.str, typing.Any]],
    query_id: builtins.str,
    id: typing.Optional[builtins.str] = None,
    parent: typing.Optional[builtins.str] = None,
    rearm: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__9f0379d1cc48cdf7c58355498d45f41159a8c18640067cd4754af77b77a7bb3b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a45d96374a89b26c0d3559d12f58c274f9eb88c06309958452aaae6c470ce3f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4c4ab61f5a391e585c4af010666ec366f392169548f68363b2318b9c8f94665(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67dd37061e41371e3d24f30e875faa61d8cfe759472e55d480b54abd6b798fec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65705fc4b93f0d01e988d25547f168a618d8e1b6e8d202ae08eee0390d590413(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__233f97a866dceebe631f62ae2fd8ee58c1c0acddc96e2bb0a1ddef5ea6033db6(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    options: typing.Union[SqlAlertOptions, typing.Dict[builtins.str, typing.Any]],
    query_id: builtins.str,
    id: typing.Optional[builtins.str] = None,
    parent: typing.Optional[builtins.str] = None,
    rearm: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce20cc2a4a4a2ec925632604b9f9c7f19a8e666356aa725845d35a27d3d8cdab(
    *,
    column: builtins.str,
    op: builtins.str,
    value: builtins.str,
    custom_body: typing.Optional[builtins.str] = None,
    custom_subject: typing.Optional[builtins.str] = None,
    muted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22870f40d2999d96ffd327f3f7e646f06bdf0769d7c2860e2fab4fe4e7dda0d6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d46b8995879b3af53e5e9794c1b53d214b4d9a0c60873f6188e46402416a2c0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1f64457a00adcca0638e6043c575139d2a18b7250c167b9e1d08fbfe0c3d506(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd5de4ea2b8106c7c14456033867499cfa7476fa11a21ae400557e45ec5950ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__167e83e17c150e78f63ec26912d75866f37d5ecd1f3c9892f115867124c24c9f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff04a0fc8701b8ec0dc2f318bdeadb89fcccc5dd48e4eef9ffd9512659a29115(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d80d2d374e111f7693f5a5862da1f7e385b817ecf9e8f1af9d78b96bd50ec29b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca372fcd7a1cbc9437edf626ee19e091a6dccff8541712da3fc2e43b26413af3(
    value: typing.Optional[SqlAlertOptions],
) -> None:
    """Type checking stubs"""
    pass
