'''
# `databricks_model_serving`

Refer to the Terraform Registory for docs: [`databricks_model_serving`](https://www.terraform.io/docs/providers/databricks/r/model_serving).
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


class ModelServing(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.modelServing.ModelServing",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/model_serving databricks_model_serving}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        config: typing.Union["ModelServingConfigA", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ModelServingTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/model_serving databricks_model_serving} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#config ModelServing#config}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#name ModelServing#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#id ModelServing#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#timeouts ModelServing#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b47a6a89f9b83085463270361bcfc2458747135ff6702149246e95053120452c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config_ = ModelServingConfig(
            config=config,
            name=name,
            id=id,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config_])

    @jsii.member(jsii_name="putConfig")
    def put_config(
        self,
        *,
        served_models: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ModelServingConfigServedModels", typing.Dict[builtins.str, typing.Any]]]],
        traffic_config: typing.Optional[typing.Union["ModelServingConfigTrafficConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param served_models: served_models block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#served_models ModelServing#served_models}
        :param traffic_config: traffic_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#traffic_config ModelServing#traffic_config}
        '''
        value = ModelServingConfigA(
            served_models=served_models, traffic_config=traffic_config
        )

        return typing.cast(None, jsii.invoke(self, "putConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#create ModelServing#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#update ModelServing#update}.
        '''
        value = ModelServingTimeouts(create=create, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(self) -> "ModelServingConfigAOutputReference":
        return typing.cast("ModelServingConfigAOutputReference", jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ModelServingTimeoutsOutputReference":
        return typing.cast("ModelServingTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="configInput")
    def config_input(self) -> typing.Optional["ModelServingConfigA"]:
        return typing.cast(typing.Optional["ModelServingConfigA"], jsii.get(self, "configInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ModelServingTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ModelServingTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f20c974cb2062333306e049b07f1b451a63080d8bbdd579a6410233fcf09245)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d76ef75f8a0e4c82c844fe5d274af400a844dd17b750d57e1be441f1e15dbe9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="databricks.modelServing.ModelServingConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "config": "config",
        "name": "name",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class ModelServingConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        config: typing.Union["ModelServingConfigA", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ModelServingTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#config ModelServing#config}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#name ModelServing#name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#id ModelServing#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#timeouts ModelServing#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(config, dict):
            config = ModelServingConfigA(**config)
        if isinstance(timeouts, dict):
            timeouts = ModelServingTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5c8cfc13641feebcca8f29d9f631c847d84148be5c7e21156003173def1343c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config": config,
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
        if id is not None:
            self._values["id"] = id
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def config(self) -> "ModelServingConfigA":
        '''config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#config ModelServing#config}
        '''
        result = self._values.get("config")
        assert result is not None, "Required property 'config' is missing"
        return typing.cast("ModelServingConfigA", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#name ModelServing#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#id ModelServing#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ModelServingTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#timeouts ModelServing#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ModelServingTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelServingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.modelServing.ModelServingConfigA",
    jsii_struct_bases=[],
    name_mapping={"served_models": "servedModels", "traffic_config": "trafficConfig"},
)
class ModelServingConfigA:
    def __init__(
        self,
        *,
        served_models: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ModelServingConfigServedModels", typing.Dict[builtins.str, typing.Any]]]],
        traffic_config: typing.Optional[typing.Union["ModelServingConfigTrafficConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param served_models: served_models block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#served_models ModelServing#served_models}
        :param traffic_config: traffic_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#traffic_config ModelServing#traffic_config}
        '''
        if isinstance(traffic_config, dict):
            traffic_config = ModelServingConfigTrafficConfig(**traffic_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dfa9a6198699272f07bb9a634a2fdf6610b49c3052670f1785805c8331e8990)
            check_type(argname="argument served_models", value=served_models, expected_type=type_hints["served_models"])
            check_type(argname="argument traffic_config", value=traffic_config, expected_type=type_hints["traffic_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "served_models": served_models,
        }
        if traffic_config is not None:
            self._values["traffic_config"] = traffic_config

    @builtins.property
    def served_models(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ModelServingConfigServedModels"]]:
        '''served_models block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#served_models ModelServing#served_models}
        '''
        result = self._values.get("served_models")
        assert result is not None, "Required property 'served_models' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ModelServingConfigServedModels"]], result)

    @builtins.property
    def traffic_config(self) -> typing.Optional["ModelServingConfigTrafficConfig"]:
        '''traffic_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#traffic_config ModelServing#traffic_config}
        '''
        result = self._values.get("traffic_config")
        return typing.cast(typing.Optional["ModelServingConfigTrafficConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelServingConfigA(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ModelServingConfigAOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.modelServing.ModelServingConfigAOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a30c2b64961e0dcd3ab48a4f9a9d239f7d2eb4daea8f8debe1b61d2351996930)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putServedModels")
    def put_served_models(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ModelServingConfigServedModels", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89b966b3f70cc1a972031beeae508a75d951aa1ec171e7074709d06c36d1d1c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putServedModels", [value]))

    @jsii.member(jsii_name="putTrafficConfig")
    def put_traffic_config(
        self,
        *,
        routes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ModelServingConfigTrafficConfigRoutes", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param routes: routes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#routes ModelServing#routes}
        '''
        value = ModelServingConfigTrafficConfig(routes=routes)

        return typing.cast(None, jsii.invoke(self, "putTrafficConfig", [value]))

    @jsii.member(jsii_name="resetTrafficConfig")
    def reset_traffic_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrafficConfig", []))

    @builtins.property
    @jsii.member(jsii_name="servedModels")
    def served_models(self) -> "ModelServingConfigServedModelsList":
        return typing.cast("ModelServingConfigServedModelsList", jsii.get(self, "servedModels"))

    @builtins.property
    @jsii.member(jsii_name="trafficConfig")
    def traffic_config(self) -> "ModelServingConfigTrafficConfigOutputReference":
        return typing.cast("ModelServingConfigTrafficConfigOutputReference", jsii.get(self, "trafficConfig"))

    @builtins.property
    @jsii.member(jsii_name="servedModelsInput")
    def served_models_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ModelServingConfigServedModels"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ModelServingConfigServedModels"]]], jsii.get(self, "servedModelsInput"))

    @builtins.property
    @jsii.member(jsii_name="trafficConfigInput")
    def traffic_config_input(
        self,
    ) -> typing.Optional["ModelServingConfigTrafficConfig"]:
        return typing.cast(typing.Optional["ModelServingConfigTrafficConfig"], jsii.get(self, "trafficConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ModelServingConfigA]:
        return typing.cast(typing.Optional[ModelServingConfigA], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ModelServingConfigA]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__130f2a2f57b7e82249c3fca199199e75f69bed922a6aeb51d4ec7fda3f4370d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.modelServing.ModelServingConfigServedModels",
    jsii_struct_bases=[],
    name_mapping={
        "model_name": "modelName",
        "model_version": "modelVersion",
        "workload_size": "workloadSize",
        "name": "name",
        "scale_to_zero_enabled": "scaleToZeroEnabled",
    },
)
class ModelServingConfigServedModels:
    def __init__(
        self,
        *,
        model_name: builtins.str,
        model_version: builtins.str,
        workload_size: builtins.str,
        name: typing.Optional[builtins.str] = None,
        scale_to_zero_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param model_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#model_name ModelServing#model_name}.
        :param model_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#model_version ModelServing#model_version}.
        :param workload_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#workload_size ModelServing#workload_size}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#name ModelServing#name}.
        :param scale_to_zero_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#scale_to_zero_enabled ModelServing#scale_to_zero_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec1b8450de4be843325b6bf4f4ffe3f1eab613e77647906eb281219f52a8ac8f)
            check_type(argname="argument model_name", value=model_name, expected_type=type_hints["model_name"])
            check_type(argname="argument model_version", value=model_version, expected_type=type_hints["model_version"])
            check_type(argname="argument workload_size", value=workload_size, expected_type=type_hints["workload_size"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument scale_to_zero_enabled", value=scale_to_zero_enabled, expected_type=type_hints["scale_to_zero_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "model_name": model_name,
            "model_version": model_version,
            "workload_size": workload_size,
        }
        if name is not None:
            self._values["name"] = name
        if scale_to_zero_enabled is not None:
            self._values["scale_to_zero_enabled"] = scale_to_zero_enabled

    @builtins.property
    def model_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#model_name ModelServing#model_name}.'''
        result = self._values.get("model_name")
        assert result is not None, "Required property 'model_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def model_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#model_version ModelServing#model_version}.'''
        result = self._values.get("model_version")
        assert result is not None, "Required property 'model_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workload_size(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#workload_size ModelServing#workload_size}.'''
        result = self._values.get("workload_size")
        assert result is not None, "Required property 'workload_size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#name ModelServing#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_to_zero_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#scale_to_zero_enabled ModelServing#scale_to_zero_enabled}.'''
        result = self._values.get("scale_to_zero_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelServingConfigServedModels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ModelServingConfigServedModelsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.modelServing.ModelServingConfigServedModelsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4a911391eea313ddf7ab13fdcea88899b3394474655ade4915f97aee49171fad)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ModelServingConfigServedModelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fb64a48c2efed0a7aa94fb7139a408db9dd02df7aba3828527065247eab5225)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ModelServingConfigServedModelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8382ba57e30b7daaa79ab20cda96462ea517176d17a3f3ee005315e7bf23c135)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f1468260c114e50d4e57b5889823b5c3edd18a4173e93e6a1a5ec1d3211a8fe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dcec82990424e69e2043447a0949eab561684d224c1067ad8e14e45c42ace628)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ModelServingConfigServedModels]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ModelServingConfigServedModels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ModelServingConfigServedModels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43788d13a917348bb02a435a921cbb27a7a97348ee4e2ab4ea44a7d9c148a965)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ModelServingConfigServedModelsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.modelServing.ModelServingConfigServedModelsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8403e485ec8341c80585b63dd1491c69249e2e1b1bce5d3ab9c7a67d01d0d0ba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetScaleToZeroEnabled")
    def reset_scale_to_zero_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleToZeroEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="modelNameInput")
    def model_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelNameInput"))

    @builtins.property
    @jsii.member(jsii_name="modelVersionInput")
    def model_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleToZeroEnabledInput")
    def scale_to_zero_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "scaleToZeroEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="workloadSizeInput")
    def workload_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workloadSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="modelName")
    def model_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modelName"))

    @model_name.setter
    def model_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89dd18b2e739ecb7d750d26fe1ea62859f40ace6038e4e55c0b61a39e8ebe8b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelName", value)

    @builtins.property
    @jsii.member(jsii_name="modelVersion")
    def model_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modelVersion"))

    @model_version.setter
    def model_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8180236dd0f503956242977abafac10c94ab94745e7737774533fb6c9f40e948)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelVersion", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae27f6793d90f0cc4b4b5e7b1b88a944b40e46a84cd017ec360719cd20d242f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="scaleToZeroEnabled")
    def scale_to_zero_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "scaleToZeroEnabled"))

    @scale_to_zero_enabled.setter
    def scale_to_zero_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d12f2d2c9428ca9606e470f4851248d6749ab6f9d805d846a46eb53385b356ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleToZeroEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="workloadSize")
    def workload_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workloadSize"))

    @workload_size.setter
    def workload_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acb3005319449bda2b01b898c371177564796090b7027b37062348bb3b047429)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workloadSize", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ModelServingConfigServedModels, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ModelServingConfigServedModels, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ModelServingConfigServedModels, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79c5b6bf8b8dca07ccef925d852468bca1dd630946d69ea9dfea65388e0d04dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.modelServing.ModelServingConfigTrafficConfig",
    jsii_struct_bases=[],
    name_mapping={"routes": "routes"},
)
class ModelServingConfigTrafficConfig:
    def __init__(
        self,
        *,
        routes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ModelServingConfigTrafficConfigRoutes", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param routes: routes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#routes ModelServing#routes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bb8284d2aa77f4b0a3ab91f032b6f64956e07a55061b441e20ad958c60494a2)
            check_type(argname="argument routes", value=routes, expected_type=type_hints["routes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if routes is not None:
            self._values["routes"] = routes

    @builtins.property
    def routes(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ModelServingConfigTrafficConfigRoutes"]]]:
        '''routes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#routes ModelServing#routes}
        '''
        result = self._values.get("routes")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ModelServingConfigTrafficConfigRoutes"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelServingConfigTrafficConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ModelServingConfigTrafficConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.modelServing.ModelServingConfigTrafficConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__77e00eddfcde822ce54e891c00d799c279f118067a5a26fb9b5a9ff9c02c7f74)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRoutes")
    def put_routes(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ModelServingConfigTrafficConfigRoutes", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40f894c6be361ea32d3b2957dab2d16b4606a6c6cb67e4b51415d0b0d600acd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRoutes", [value]))

    @jsii.member(jsii_name="resetRoutes")
    def reset_routes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoutes", []))

    @builtins.property
    @jsii.member(jsii_name="routes")
    def routes(self) -> "ModelServingConfigTrafficConfigRoutesList":
        return typing.cast("ModelServingConfigTrafficConfigRoutesList", jsii.get(self, "routes"))

    @builtins.property
    @jsii.member(jsii_name="routesInput")
    def routes_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ModelServingConfigTrafficConfigRoutes"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ModelServingConfigTrafficConfigRoutes"]]], jsii.get(self, "routesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ModelServingConfigTrafficConfig]:
        return typing.cast(typing.Optional[ModelServingConfigTrafficConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ModelServingConfigTrafficConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1af95663e159ca118b245b762a884ca73873506d446984fcfcd4839b47d862dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.modelServing.ModelServingConfigTrafficConfigRoutes",
    jsii_struct_bases=[],
    name_mapping={
        "served_model_name": "servedModelName",
        "traffic_percentage": "trafficPercentage",
    },
)
class ModelServingConfigTrafficConfigRoutes:
    def __init__(
        self,
        *,
        served_model_name: builtins.str,
        traffic_percentage: jsii.Number,
    ) -> None:
        '''
        :param served_model_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#served_model_name ModelServing#served_model_name}.
        :param traffic_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#traffic_percentage ModelServing#traffic_percentage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__722ce6488dba44982ed611c59f7c8c95ffa4b122c378522c2fed6eefa1c9f99d)
            check_type(argname="argument served_model_name", value=served_model_name, expected_type=type_hints["served_model_name"])
            check_type(argname="argument traffic_percentage", value=traffic_percentage, expected_type=type_hints["traffic_percentage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "served_model_name": served_model_name,
            "traffic_percentage": traffic_percentage,
        }

    @builtins.property
    def served_model_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#served_model_name ModelServing#served_model_name}.'''
        result = self._values.get("served_model_name")
        assert result is not None, "Required property 'served_model_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def traffic_percentage(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#traffic_percentage ModelServing#traffic_percentage}.'''
        result = self._values.get("traffic_percentage")
        assert result is not None, "Required property 'traffic_percentage' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelServingConfigTrafficConfigRoutes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ModelServingConfigTrafficConfigRoutesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.modelServing.ModelServingConfigTrafficConfigRoutesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b521ca8f432e327f0c05caa8663b39f9a4367afa5873f7c887541b697f45e182)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ModelServingConfigTrafficConfigRoutesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9066f99ba9364d5f15f6c1e1b647d7e6433224e9802f13bf7a3fab7b728bf01c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ModelServingConfigTrafficConfigRoutesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de3b26312a06a60e3a2aa60447dde1c09c4df3dcbd6188a1a87db13bed0cddd6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb1adc7ec47286f84c09751b3782d9db284ab5511d78857cb968b300b575f17c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__af10cc5bf71bb8461b673d3e3a9d857904f8eeb1790f465977394ab71e9a03cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ModelServingConfigTrafficConfigRoutes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ModelServingConfigTrafficConfigRoutes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ModelServingConfigTrafficConfigRoutes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f653293721aa86d8b113bb2441700c7c5482e661a05e90ddb64f29795dad193e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ModelServingConfigTrafficConfigRoutesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.modelServing.ModelServingConfigTrafficConfigRoutesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__49970dd8e992880d5442a681098dca90de764a6ba747f960be77344b963cca3e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="servedModelNameInput")
    def served_model_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servedModelNameInput"))

    @builtins.property
    @jsii.member(jsii_name="trafficPercentageInput")
    def traffic_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "trafficPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="servedModelName")
    def served_model_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servedModelName"))

    @served_model_name.setter
    def served_model_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d2e730143916ca7927472617d73801c2bb5536aaca5b4f223582ef68b95e2c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servedModelName", value)

    @builtins.property
    @jsii.member(jsii_name="trafficPercentage")
    def traffic_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "trafficPercentage"))

    @traffic_percentage.setter
    def traffic_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0758e6efb2a3af50d818117fbd87cf2a88e92c7f5a9cf4e6bc3a973b4210ce3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trafficPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ModelServingConfigTrafficConfigRoutes, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ModelServingConfigTrafficConfigRoutes, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ModelServingConfigTrafficConfigRoutes, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__851fccbf31222ff234c218e15fa523f91713460abb6ebde8281f77c85d7cf759)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.modelServing.ModelServingTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "update": "update"},
)
class ModelServingTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#create ModelServing#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#update ModelServing#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__057c10a6dfc0d2819641a75ad70ed5176d43ff29e2f7273915abfc328f56b851)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#create ModelServing#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/model_serving#update ModelServing#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelServingTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ModelServingTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.modelServing.ModelServingTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd69edf29ba24f65b074f1432957bc71a33c9152384308aba575faf8f5878289)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72607f704713f6097c8e3e0ad32a9354500a5f4a9eba00ff867fac0140aa11a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37e367300ea4c3899c8900b0ee8c249fc49fcdaf73617eef811dda42200d689b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ModelServingTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ModelServingTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ModelServingTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9a7375937a5cfc5af9e9176e12da16b10773d6511dd973c70ded628dd3cbb77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ModelServing",
    "ModelServingConfig",
    "ModelServingConfigA",
    "ModelServingConfigAOutputReference",
    "ModelServingConfigServedModels",
    "ModelServingConfigServedModelsList",
    "ModelServingConfigServedModelsOutputReference",
    "ModelServingConfigTrafficConfig",
    "ModelServingConfigTrafficConfigOutputReference",
    "ModelServingConfigTrafficConfigRoutes",
    "ModelServingConfigTrafficConfigRoutesList",
    "ModelServingConfigTrafficConfigRoutesOutputReference",
    "ModelServingTimeouts",
    "ModelServingTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__b47a6a89f9b83085463270361bcfc2458747135ff6702149246e95053120452c(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    config: typing.Union[ModelServingConfigA, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[ModelServingTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__9f20c974cb2062333306e049b07f1b451a63080d8bbdd579a6410233fcf09245(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d76ef75f8a0e4c82c844fe5d274af400a844dd17b750d57e1be441f1e15dbe9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5c8cfc13641feebcca8f29d9f631c847d84148be5c7e21156003173def1343c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    config: typing.Union[ModelServingConfigA, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[ModelServingTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dfa9a6198699272f07bb9a634a2fdf6610b49c3052670f1785805c8331e8990(
    *,
    served_models: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ModelServingConfigServedModels, typing.Dict[builtins.str, typing.Any]]]],
    traffic_config: typing.Optional[typing.Union[ModelServingConfigTrafficConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a30c2b64961e0dcd3ab48a4f9a9d239f7d2eb4daea8f8debe1b61d2351996930(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89b966b3f70cc1a972031beeae508a75d951aa1ec171e7074709d06c36d1d1c4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ModelServingConfigServedModels, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__130f2a2f57b7e82249c3fca199199e75f69bed922a6aeb51d4ec7fda3f4370d4(
    value: typing.Optional[ModelServingConfigA],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec1b8450de4be843325b6bf4f4ffe3f1eab613e77647906eb281219f52a8ac8f(
    *,
    model_name: builtins.str,
    model_version: builtins.str,
    workload_size: builtins.str,
    name: typing.Optional[builtins.str] = None,
    scale_to_zero_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a911391eea313ddf7ab13fdcea88899b3394474655ade4915f97aee49171fad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fb64a48c2efed0a7aa94fb7139a408db9dd02df7aba3828527065247eab5225(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8382ba57e30b7daaa79ab20cda96462ea517176d17a3f3ee005315e7bf23c135(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f1468260c114e50d4e57b5889823b5c3edd18a4173e93e6a1a5ec1d3211a8fe(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcec82990424e69e2043447a0949eab561684d224c1067ad8e14e45c42ace628(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43788d13a917348bb02a435a921cbb27a7a97348ee4e2ab4ea44a7d9c148a965(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ModelServingConfigServedModels]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8403e485ec8341c80585b63dd1491c69249e2e1b1bce5d3ab9c7a67d01d0d0ba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89dd18b2e739ecb7d750d26fe1ea62859f40ace6038e4e55c0b61a39e8ebe8b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8180236dd0f503956242977abafac10c94ab94745e7737774533fb6c9f40e948(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae27f6793d90f0cc4b4b5e7b1b88a944b40e46a84cd017ec360719cd20d242f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d12f2d2c9428ca9606e470f4851248d6749ab6f9d805d846a46eb53385b356ba(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acb3005319449bda2b01b898c371177564796090b7027b37062348bb3b047429(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79c5b6bf8b8dca07ccef925d852468bca1dd630946d69ea9dfea65388e0d04dc(
    value: typing.Optional[typing.Union[ModelServingConfigServedModels, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bb8284d2aa77f4b0a3ab91f032b6f64956e07a55061b441e20ad958c60494a2(
    *,
    routes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ModelServingConfigTrafficConfigRoutes, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77e00eddfcde822ce54e891c00d799c279f118067a5a26fb9b5a9ff9c02c7f74(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40f894c6be361ea32d3b2957dab2d16b4606a6c6cb67e4b51415d0b0d600acd1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ModelServingConfigTrafficConfigRoutes, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1af95663e159ca118b245b762a884ca73873506d446984fcfcd4839b47d862dd(
    value: typing.Optional[ModelServingConfigTrafficConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__722ce6488dba44982ed611c59f7c8c95ffa4b122c378522c2fed6eefa1c9f99d(
    *,
    served_model_name: builtins.str,
    traffic_percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b521ca8f432e327f0c05caa8663b39f9a4367afa5873f7c887541b697f45e182(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9066f99ba9364d5f15f6c1e1b647d7e6433224e9802f13bf7a3fab7b728bf01c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de3b26312a06a60e3a2aa60447dde1c09c4df3dcbd6188a1a87db13bed0cddd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb1adc7ec47286f84c09751b3782d9db284ab5511d78857cb968b300b575f17c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af10cc5bf71bb8461b673d3e3a9d857904f8eeb1790f465977394ab71e9a03cc(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f653293721aa86d8b113bb2441700c7c5482e661a05e90ddb64f29795dad193e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ModelServingConfigTrafficConfigRoutes]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49970dd8e992880d5442a681098dca90de764a6ba747f960be77344b963cca3e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d2e730143916ca7927472617d73801c2bb5536aaca5b4f223582ef68b95e2c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0758e6efb2a3af50d818117fbd87cf2a88e92c7f5a9cf4e6bc3a973b4210ce3f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__851fccbf31222ff234c218e15fa523f91713460abb6ebde8281f77c85d7cf759(
    value: typing.Optional[typing.Union[ModelServingConfigTrafficConfigRoutes, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__057c10a6dfc0d2819641a75ad70ed5176d43ff29e2f7273915abfc328f56b851(
    *,
    create: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd69edf29ba24f65b074f1432957bc71a33c9152384308aba575faf8f5878289(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72607f704713f6097c8e3e0ad32a9354500a5f4a9eba00ff867fac0140aa11a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37e367300ea4c3899c8900b0ee8c249fc49fcdaf73617eef811dda42200d689b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9a7375937a5cfc5af9e9176e12da16b10773d6511dd973c70ded628dd3cbb77(
    value: typing.Optional[typing.Union[ModelServingTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
