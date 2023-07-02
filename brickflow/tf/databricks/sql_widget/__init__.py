'''
# `databricks_sql_widget`

Refer to the Terraform Registory for docs: [`databricks_sql_widget`](https://www.terraform.io/docs/providers/databricks/r/sql_widget).
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


class SqlWidget(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlWidget.SqlWidget",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget databricks_sql_widget}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        dashboard_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SqlWidgetParameter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        position: typing.Optional[typing.Union["SqlWidgetPosition", typing.Dict[builtins.str, typing.Any]]] = None,
        text: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        visualization_id: typing.Optional[builtins.str] = None,
        widget_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget databricks_sql_widget} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param dashboard_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#dashboard_id SqlWidget#dashboard_id}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#description SqlWidget#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#id SqlWidget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#parameter SqlWidget#parameter}
        :param position: position block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#position SqlWidget#position}
        :param text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#text SqlWidget#text}.
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#title SqlWidget#title}.
        :param visualization_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#visualization_id SqlWidget#visualization_id}.
        :param widget_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#widget_id SqlWidget#widget_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__634a5c0a590ef3f859c6f78779eeb0be65988682b599081be88d68815db9fe5e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SqlWidgetConfig(
            dashboard_id=dashboard_id,
            description=description,
            id=id,
            parameter=parameter,
            position=position,
            text=text,
            title=title,
            visualization_id=visualization_id,
            widget_id=widget_id,
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
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SqlWidgetParameter", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c99b2df570f377ed76595ed50e342a808b4e651c6b8665a210a4672db9c4fb83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameter", [value]))

    @jsii.member(jsii_name="putPosition")
    def put_position(
        self,
        *,
        size_x: jsii.Number,
        size_y: jsii.Number,
        auto_height: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        pos_x: typing.Optional[jsii.Number] = None,
        pos_y: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param size_x: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#size_x SqlWidget#size_x}.
        :param size_y: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#size_y SqlWidget#size_y}.
        :param auto_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#auto_height SqlWidget#auto_height}.
        :param pos_x: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#pos_x SqlWidget#pos_x}.
        :param pos_y: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#pos_y SqlWidget#pos_y}.
        '''
        value = SqlWidgetPosition(
            size_x=size_x,
            size_y=size_y,
            auto_height=auto_height,
            pos_x=pos_x,
            pos_y=pos_y,
        )

        return typing.cast(None, jsii.invoke(self, "putPosition", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @jsii.member(jsii_name="resetPosition")
    def reset_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPosition", []))

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @jsii.member(jsii_name="resetVisualizationId")
    def reset_visualization_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVisualizationId", []))

    @jsii.member(jsii_name="resetWidgetId")
    def reset_widget_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidgetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(self) -> "SqlWidgetParameterList":
        return typing.cast("SqlWidgetParameterList", jsii.get(self, "parameter"))

    @builtins.property
    @jsii.member(jsii_name="position")
    def position(self) -> "SqlWidgetPositionOutputReference":
        return typing.cast("SqlWidgetPositionOutputReference", jsii.get(self, "position"))

    @builtins.property
    @jsii.member(jsii_name="dashboardIdInput")
    def dashboard_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dashboardIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SqlWidgetParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SqlWidgetParameter"]]], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="positionInput")
    def position_input(self) -> typing.Optional["SqlWidgetPosition"]:
        return typing.cast(typing.Optional["SqlWidgetPosition"], jsii.get(self, "positionInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="visualizationIdInput")
    def visualization_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "visualizationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="widgetIdInput")
    def widget_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "widgetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="dashboardId")
    def dashboard_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dashboardId"))

    @dashboard_id.setter
    def dashboard_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b471c739e77430effb27c12a51cb4726d403a1d64f75225cb3e0fdc4c1c13f7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashboardId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe6e12a32eb56692f74e00df00558c98533f884bc227218fe34ab2c58e87ba20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a36384eebbfbb4ea6a9e900e077d7e8786e28e1109f24129c19064a31ae340fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "text"))

    @text.setter
    def text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95b9e421f35ded6629d53a3e0128200bd746486e9decb8b9a5c0d6e022de37fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d80b870ab904d915b01a16d02f37f4732847e4b54adf0cbbec86fb761e530b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="visualizationId")
    def visualization_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "visualizationId"))

    @visualization_id.setter
    def visualization_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2260e2717a8e8895c9786f2d41f2116beed852c0bae132f4a734788bc5dfb264)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visualizationId", value)

    @builtins.property
    @jsii.member(jsii_name="widgetId")
    def widget_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "widgetId"))

    @widget_id.setter
    def widget_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__369f183ced1074b9e5b191cf903f8bce1359107866b5ce3b17b19a4ebcd06ebd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "widgetId", value)


@jsii.data_type(
    jsii_type="databricks.sqlWidget.SqlWidgetConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "dashboard_id": "dashboardId",
        "description": "description",
        "id": "id",
        "parameter": "parameter",
        "position": "position",
        "text": "text",
        "title": "title",
        "visualization_id": "visualizationId",
        "widget_id": "widgetId",
    },
)
class SqlWidgetConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        dashboard_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SqlWidgetParameter", typing.Dict[builtins.str, typing.Any]]]]] = None,
        position: typing.Optional[typing.Union["SqlWidgetPosition", typing.Dict[builtins.str, typing.Any]]] = None,
        text: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        visualization_id: typing.Optional[builtins.str] = None,
        widget_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param dashboard_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#dashboard_id SqlWidget#dashboard_id}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#description SqlWidget#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#id SqlWidget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#parameter SqlWidget#parameter}
        :param position: position block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#position SqlWidget#position}
        :param text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#text SqlWidget#text}.
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#title SqlWidget#title}.
        :param visualization_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#visualization_id SqlWidget#visualization_id}.
        :param widget_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#widget_id SqlWidget#widget_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(position, dict):
            position = SqlWidgetPosition(**position)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0128bcf6018ffc54dfafbee6f86b2a7c8fe9ccf4d658e6a5f1826c8db02f61a9)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument dashboard_id", value=dashboard_id, expected_type=type_hints["dashboard_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
            check_type(argname="argument position", value=position, expected_type=type_hints["position"])
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument visualization_id", value=visualization_id, expected_type=type_hints["visualization_id"])
            check_type(argname="argument widget_id", value=widget_id, expected_type=type_hints["widget_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dashboard_id": dashboard_id,
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
        if position is not None:
            self._values["position"] = position
        if text is not None:
            self._values["text"] = text
        if title is not None:
            self._values["title"] = title
        if visualization_id is not None:
            self._values["visualization_id"] = visualization_id
        if widget_id is not None:
            self._values["widget_id"] = widget_id

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
    def dashboard_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#dashboard_id SqlWidget#dashboard_id}.'''
        result = self._values.get("dashboard_id")
        assert result is not None, "Required property 'dashboard_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#description SqlWidget#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#id SqlWidget#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SqlWidgetParameter"]]]:
        '''parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#parameter SqlWidget#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SqlWidgetParameter"]]], result)

    @builtins.property
    def position(self) -> typing.Optional["SqlWidgetPosition"]:
        '''position block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#position SqlWidget#position}
        '''
        result = self._values.get("position")
        return typing.cast(typing.Optional["SqlWidgetPosition"], result)

    @builtins.property
    def text(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#text SqlWidget#text}.'''
        result = self._values.get("text")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#title SqlWidget#title}.'''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def visualization_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#visualization_id SqlWidget#visualization_id}.'''
        result = self._values.get("visualization_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def widget_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#widget_id SqlWidget#widget_id}.'''
        result = self._values.get("widget_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlWidgetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.sqlWidget.SqlWidgetParameter",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "map_to": "mapTo",
        "title": "title",
        "value": "value",
        "values": "values",
    },
)
class SqlWidgetParameter:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        map_to: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#name SqlWidget#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#type SqlWidget#type}.
        :param map_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#map_to SqlWidget#map_to}.
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#title SqlWidget#title}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#value SqlWidget#value}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#values SqlWidget#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c3bafa801a37e8f75039317cb805d9829b8e15e309a7a4ae94d031f993716ee)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument map_to", value=map_to, expected_type=type_hints["map_to"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if map_to is not None:
            self._values["map_to"] = map_to
        if title is not None:
            self._values["title"] = title
        if value is not None:
            self._values["value"] = value
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#name SqlWidget#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#type SqlWidget#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def map_to(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#map_to SqlWidget#map_to}.'''
        result = self._values.get("map_to")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#title SqlWidget#title}.'''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#value SqlWidget#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#values SqlWidget#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlWidgetParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlWidgetParameterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlWidget.SqlWidgetParameterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3345f00d1e103351cc4400ef7c94af82bc0e3a2fb9bf01998c55d85f47b5bf13)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SqlWidgetParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e54ea6cb6c45eb39cb14e42da96a3ed98dac058aeffecd98956a15f181db321)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SqlWidgetParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b59f6852a6155b64f56f2b2389e69af0e42180857a87ea4941cf1176b0855116)
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
            type_hints = typing.get_type_hints(_typecheckingstub__43ff325ac298835b60df15172b83a80b176f050711405b4a629e5f03dbd107d1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a239963d32a8a2f7c198fc722d3f87b23cabfa638d6d0b7eff53ccdaf1eb2c4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlWidgetParameter]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlWidgetParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlWidgetParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a41c6d407c52345ac34b760a11d724d0ff2e0cab54c80f115583f730c13c9ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SqlWidgetParameterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlWidget.SqlWidgetParameterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__de75daff78b770243b273c2b22a449ac463ebd7943983b1bcdc89eed7241f627)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMapTo")
    def reset_map_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMapTo", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="mapToInput")
    def map_to_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mapToInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="mapTo")
    def map_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mapTo"))

    @map_to.setter
    def map_to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37e368a7824e30470efd2a25dba88349bd16f93a1ace387ff5a8e5c7cfb73f69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mapTo", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b040f15d7895db69400557a1c91514cffba8cb29c1c4154baabc8d17212e81ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4114551644acb1bbdcc40c2c667132c4d0d1ae5b439d4618d901ac26c35ae619)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cf46a995141e72e97dba9a5b9d3eabdc79aacd4d2a368ea9f084b33a1c8617e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f74f00c18f483a9c4a3ddeb26acc3f034b2fe2e455db5f1e43f6620ab80066a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59d73d2c75010acbb29c2bea56123b95007763f2060272a7fe2cbc74a1d94dde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SqlWidgetParameter, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SqlWidgetParameter, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SqlWidgetParameter, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2284a1b866d09e7f45fa80443d271d7ecee5931006a47bd766c81dd15ed1f0fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.sqlWidget.SqlWidgetPosition",
    jsii_struct_bases=[],
    name_mapping={
        "size_x": "sizeX",
        "size_y": "sizeY",
        "auto_height": "autoHeight",
        "pos_x": "posX",
        "pos_y": "posY",
    },
)
class SqlWidgetPosition:
    def __init__(
        self,
        *,
        size_x: jsii.Number,
        size_y: jsii.Number,
        auto_height: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        pos_x: typing.Optional[jsii.Number] = None,
        pos_y: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param size_x: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#size_x SqlWidget#size_x}.
        :param size_y: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#size_y SqlWidget#size_y}.
        :param auto_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#auto_height SqlWidget#auto_height}.
        :param pos_x: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#pos_x SqlWidget#pos_x}.
        :param pos_y: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#pos_y SqlWidget#pos_y}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82a0cf6fe4f13eaa14bf5b6122be95d88a7a16a29d5b05202b9e5776ed48956d)
            check_type(argname="argument size_x", value=size_x, expected_type=type_hints["size_x"])
            check_type(argname="argument size_y", value=size_y, expected_type=type_hints["size_y"])
            check_type(argname="argument auto_height", value=auto_height, expected_type=type_hints["auto_height"])
            check_type(argname="argument pos_x", value=pos_x, expected_type=type_hints["pos_x"])
            check_type(argname="argument pos_y", value=pos_y, expected_type=type_hints["pos_y"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "size_x": size_x,
            "size_y": size_y,
        }
        if auto_height is not None:
            self._values["auto_height"] = auto_height
        if pos_x is not None:
            self._values["pos_x"] = pos_x
        if pos_y is not None:
            self._values["pos_y"] = pos_y

    @builtins.property
    def size_x(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#size_x SqlWidget#size_x}.'''
        result = self._values.get("size_x")
        assert result is not None, "Required property 'size_x' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def size_y(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#size_y SqlWidget#size_y}.'''
        result = self._values.get("size_y")
        assert result is not None, "Required property 'size_y' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def auto_height(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#auto_height SqlWidget#auto_height}.'''
        result = self._values.get("auto_height")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def pos_x(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#pos_x SqlWidget#pos_x}.'''
        result = self._values.get("pos_x")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pos_y(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#pos_y SqlWidget#pos_y}.'''
        result = self._values.get("pos_y")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlWidgetPosition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlWidgetPositionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlWidget.SqlWidgetPositionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8802068968ef82ee4f4560c24a5e570a1296a6524499891dfbd8c87f8f51d805)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAutoHeight")
    def reset_auto_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoHeight", []))

    @jsii.member(jsii_name="resetPosX")
    def reset_pos_x(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPosX", []))

    @jsii.member(jsii_name="resetPosY")
    def reset_pos_y(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPosY", []))

    @builtins.property
    @jsii.member(jsii_name="autoHeightInput")
    def auto_height_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoHeightInput"))

    @builtins.property
    @jsii.member(jsii_name="posXInput")
    def pos_x_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "posXInput"))

    @builtins.property
    @jsii.member(jsii_name="posYInput")
    def pos_y_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "posYInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeXInput")
    def size_x_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeXInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeYInput")
    def size_y_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeYInput"))

    @builtins.property
    @jsii.member(jsii_name="autoHeight")
    def auto_height(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoHeight"))

    @auto_height.setter
    def auto_height(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9450858ccfece16bd9020221fead80ce6ec9f7afcb2c74dced3af182041f6448)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoHeight", value)

    @builtins.property
    @jsii.member(jsii_name="posX")
    def pos_x(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "posX"))

    @pos_x.setter
    def pos_x(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58d95895eac4b06a667af29c2c65cdd142c71ce25c5bdc7e7900ecd4dac6eb39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "posX", value)

    @builtins.property
    @jsii.member(jsii_name="posY")
    def pos_y(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "posY"))

    @pos_y.setter
    def pos_y(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dc516979d20c5871559f354fcc8ba0fe5e8356099163253bba4b911b1e08911)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "posY", value)

    @builtins.property
    @jsii.member(jsii_name="sizeX")
    def size_x(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeX"))

    @size_x.setter
    def size_x(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6388da4c5c26e1f74823bb39625d0bd16d20f153b2dd4c5dcddb00be8f061bca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeX", value)

    @builtins.property
    @jsii.member(jsii_name="sizeY")
    def size_y(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeY"))

    @size_y.setter
    def size_y(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9c192165953368064ab44e97627721a5de37a248fcfa9ca9d23f147ec2a1d7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeY", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlWidgetPosition]:
        return typing.cast(typing.Optional[SqlWidgetPosition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlWidgetPosition]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d102ebffc3072ed7b03feae8e4e4cc0a7a576f22e4d22e584fb60b1b29be7972)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SqlWidget",
    "SqlWidgetConfig",
    "SqlWidgetParameter",
    "SqlWidgetParameterList",
    "SqlWidgetParameterOutputReference",
    "SqlWidgetPosition",
    "SqlWidgetPositionOutputReference",
]

publication.publish()

def _typecheckingstub__634a5c0a590ef3f859c6f78779eeb0be65988682b599081be88d68815db9fe5e(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    dashboard_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SqlWidgetParameter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    position: typing.Optional[typing.Union[SqlWidgetPosition, typing.Dict[builtins.str, typing.Any]]] = None,
    text: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    visualization_id: typing.Optional[builtins.str] = None,
    widget_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__c99b2df570f377ed76595ed50e342a808b4e651c6b8665a210a4672db9c4fb83(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SqlWidgetParameter, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b471c739e77430effb27c12a51cb4726d403a1d64f75225cb3e0fdc4c1c13f7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe6e12a32eb56692f74e00df00558c98533f884bc227218fe34ab2c58e87ba20(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a36384eebbfbb4ea6a9e900e077d7e8786e28e1109f24129c19064a31ae340fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95b9e421f35ded6629d53a3e0128200bd746486e9decb8b9a5c0d6e022de37fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d80b870ab904d915b01a16d02f37f4732847e4b54adf0cbbec86fb761e530b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2260e2717a8e8895c9786f2d41f2116beed852c0bae132f4a734788bc5dfb264(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__369f183ced1074b9e5b191cf903f8bce1359107866b5ce3b17b19a4ebcd06ebd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0128bcf6018ffc54dfafbee6f86b2a7c8fe9ccf4d658e6a5f1826c8db02f61a9(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    dashboard_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    parameter: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SqlWidgetParameter, typing.Dict[builtins.str, typing.Any]]]]] = None,
    position: typing.Optional[typing.Union[SqlWidgetPosition, typing.Dict[builtins.str, typing.Any]]] = None,
    text: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    visualization_id: typing.Optional[builtins.str] = None,
    widget_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c3bafa801a37e8f75039317cb805d9829b8e15e309a7a4ae94d031f993716ee(
    *,
    name: builtins.str,
    type: builtins.str,
    map_to: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3345f00d1e103351cc4400ef7c94af82bc0e3a2fb9bf01998c55d85f47b5bf13(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e54ea6cb6c45eb39cb14e42da96a3ed98dac058aeffecd98956a15f181db321(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b59f6852a6155b64f56f2b2389e69af0e42180857a87ea4941cf1176b0855116(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43ff325ac298835b60df15172b83a80b176f050711405b4a629e5f03dbd107d1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a239963d32a8a2f7c198fc722d3f87b23cabfa638d6d0b7eff53ccdaf1eb2c4a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a41c6d407c52345ac34b760a11d724d0ff2e0cab54c80f115583f730c13c9ba(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SqlWidgetParameter]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de75daff78b770243b273c2b22a449ac463ebd7943983b1bcdc89eed7241f627(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37e368a7824e30470efd2a25dba88349bd16f93a1ace387ff5a8e5c7cfb73f69(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b040f15d7895db69400557a1c91514cffba8cb29c1c4154baabc8d17212e81ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4114551644acb1bbdcc40c2c667132c4d0d1ae5b439d4618d901ac26c35ae619(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cf46a995141e72e97dba9a5b9d3eabdc79aacd4d2a368ea9f084b33a1c8617e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f74f00c18f483a9c4a3ddeb26acc3f034b2fe2e455db5f1e43f6620ab80066a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59d73d2c75010acbb29c2bea56123b95007763f2060272a7fe2cbc74a1d94dde(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2284a1b866d09e7f45fa80443d271d7ecee5931006a47bd766c81dd15ed1f0fc(
    value: typing.Optional[typing.Union[SqlWidgetParameter, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82a0cf6fe4f13eaa14bf5b6122be95d88a7a16a29d5b05202b9e5776ed48956d(
    *,
    size_x: jsii.Number,
    size_y: jsii.Number,
    auto_height: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    pos_x: typing.Optional[jsii.Number] = None,
    pos_y: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8802068968ef82ee4f4560c24a5e570a1296a6524499891dfbd8c87f8f51d805(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9450858ccfece16bd9020221fead80ce6ec9f7afcb2c74dced3af182041f6448(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58d95895eac4b06a667af29c2c65cdd142c71ce25c5bdc7e7900ecd4dac6eb39(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dc516979d20c5871559f354fcc8ba0fe5e8356099163253bba4b911b1e08911(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6388da4c5c26e1f74823bb39625d0bd16d20f153b2dd4c5dcddb00be8f061bca(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9c192165953368064ab44e97627721a5de37a248fcfa9ca9d23f147ec2a1d7f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d102ebffc3072ed7b03feae8e4e4cc0a7a576f22e4d22e584fb60b1b29be7972(
    value: typing.Optional[SqlWidgetPosition],
) -> None:
    """Type checking stubs"""
    pass
