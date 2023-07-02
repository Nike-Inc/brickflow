'''
# `databricks_mlflow_experiment`

Refer to the Terraform Registory for docs: [`databricks_mlflow_experiment`](https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment).
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


class MlflowExperiment(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mlflowExperiment.MlflowExperiment",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment databricks_mlflow_experiment}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        artifact_location: typing.Optional[builtins.str] = None,
        creation_time: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        experiment_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        last_update_time: typing.Optional[jsii.Number] = None,
        lifecycle_stage: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MlflowExperimentTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment databricks_mlflow_experiment} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#name MlflowExperiment#name}.
        :param artifact_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#artifact_location MlflowExperiment#artifact_location}.
        :param creation_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#creation_time MlflowExperiment#creation_time}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#description MlflowExperiment#description}.
        :param experiment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#experiment_id MlflowExperiment#experiment_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#id MlflowExperiment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param last_update_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#last_update_time MlflowExperiment#last_update_time}.
        :param lifecycle_stage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#lifecycle_stage MlflowExperiment#lifecycle_stage}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#timeouts MlflowExperiment#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c1847b5964484159ee9908ca977c8aeb8c67a707ed26d0ce2e1f375572845db)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MlflowExperimentConfig(
            name=name,
            artifact_location=artifact_location,
            creation_time=creation_time,
            description=description,
            experiment_id=experiment_id,
            id=id,
            last_update_time=last_update_time,
            lifecycle_stage=lifecycle_stage,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self) -> None:
        value = MlflowExperimentTimeouts()

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetArtifactLocation")
    def reset_artifact_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArtifactLocation", []))

    @jsii.member(jsii_name="resetCreationTime")
    def reset_creation_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreationTime", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExperimentId")
    def reset_experiment_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExperimentId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLastUpdateTime")
    def reset_last_update_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastUpdateTime", []))

    @jsii.member(jsii_name="resetLifecycleStage")
    def reset_lifecycle_stage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleStage", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MlflowExperimentTimeoutsOutputReference":
        return typing.cast("MlflowExperimentTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="artifactLocationInput")
    def artifact_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="creationTimeInput")
    def creation_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "creationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="experimentIdInput")
    def experiment_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "experimentIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdateTimeInput")
    def last_update_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lastUpdateTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleStageInput")
    def lifecycle_stage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleStageInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MlflowExperimentTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MlflowExperimentTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactLocation")
    def artifact_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactLocation"))

    @artifact_location.setter
    def artifact_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbdb31634026507cc7988ffb5e104c42ebd54d9a931d403dbe620b35faeb6f04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactLocation", value)

    @builtins.property
    @jsii.member(jsii_name="creationTime")
    def creation_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "creationTime"))

    @creation_time.setter
    def creation_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaf5402ec9356aa49928105160f2f2660509b9fc093f31d894ffa71e6afd50c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creationTime", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e753c880c1acc8fd6d76bc3abbd54553ae895b25271023ee9d2b8f8a0c3667f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="experimentId")
    def experiment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "experimentId"))

    @experiment_id.setter
    def experiment_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab868d402e255d6eec25f2eed09f386895f2d7efb9a008dc7af64a9f83578bfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "experimentId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__224ee63795129ba552708d07d2cf1ba7531a0c597409f04c6737fa500606f2c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="lastUpdateTime")
    def last_update_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lastUpdateTime"))

    @last_update_time.setter
    def last_update_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6f4241f1c68020a446b5fd452b227d8bcb001b1289fc5f3f4e2c39a6da74cc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastUpdateTime", value)

    @builtins.property
    @jsii.member(jsii_name="lifecycleStage")
    def lifecycle_stage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleStage"))

    @lifecycle_stage.setter
    def lifecycle_stage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c1bb8e024ce874431584a2e7564775b6e91268145b896fcfcd4385f1033a45b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleStage", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d882c0ae031bc1aadf4b0f31b348cdaa3bfb1968054f5c05e8f85b0d82f06b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="databricks.mlflowExperiment.MlflowExperimentConfig",
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
        "artifact_location": "artifactLocation",
        "creation_time": "creationTime",
        "description": "description",
        "experiment_id": "experimentId",
        "id": "id",
        "last_update_time": "lastUpdateTime",
        "lifecycle_stage": "lifecycleStage",
        "timeouts": "timeouts",
    },
)
class MlflowExperimentConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        artifact_location: typing.Optional[builtins.str] = None,
        creation_time: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        experiment_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        last_update_time: typing.Optional[jsii.Number] = None,
        lifecycle_stage: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MlflowExperimentTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#name MlflowExperiment#name}.
        :param artifact_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#artifact_location MlflowExperiment#artifact_location}.
        :param creation_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#creation_time MlflowExperiment#creation_time}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#description MlflowExperiment#description}.
        :param experiment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#experiment_id MlflowExperiment#experiment_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#id MlflowExperiment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param last_update_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#last_update_time MlflowExperiment#last_update_time}.
        :param lifecycle_stage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#lifecycle_stage MlflowExperiment#lifecycle_stage}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#timeouts MlflowExperiment#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = MlflowExperimentTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6569e5a232e74593e9aca308b325d5a9290b215dafcbeb97899c10ff7653a0d8)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument artifact_location", value=artifact_location, expected_type=type_hints["artifact_location"])
            check_type(argname="argument creation_time", value=creation_time, expected_type=type_hints["creation_time"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument experiment_id", value=experiment_id, expected_type=type_hints["experiment_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument last_update_time", value=last_update_time, expected_type=type_hints["last_update_time"])
            check_type(argname="argument lifecycle_stage", value=lifecycle_stage, expected_type=type_hints["lifecycle_stage"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
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
        if artifact_location is not None:
            self._values["artifact_location"] = artifact_location
        if creation_time is not None:
            self._values["creation_time"] = creation_time
        if description is not None:
            self._values["description"] = description
        if experiment_id is not None:
            self._values["experiment_id"] = experiment_id
        if id is not None:
            self._values["id"] = id
        if last_update_time is not None:
            self._values["last_update_time"] = last_update_time
        if lifecycle_stage is not None:
            self._values["lifecycle_stage"] = lifecycle_stage
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#name MlflowExperiment#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def artifact_location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#artifact_location MlflowExperiment#artifact_location}.'''
        result = self._values.get("artifact_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def creation_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#creation_time MlflowExperiment#creation_time}.'''
        result = self._values.get("creation_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#description MlflowExperiment#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def experiment_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#experiment_id MlflowExperiment#experiment_id}.'''
        result = self._values.get("experiment_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#id MlflowExperiment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_update_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#last_update_time MlflowExperiment#last_update_time}.'''
        result = self._values.get("last_update_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lifecycle_stage(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#lifecycle_stage MlflowExperiment#lifecycle_stage}.'''
        result = self._values.get("lifecycle_stage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MlflowExperimentTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_experiment#timeouts MlflowExperiment#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MlflowExperimentTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MlflowExperimentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.mlflowExperiment.MlflowExperimentTimeouts",
    jsii_struct_bases=[],
    name_mapping={},
)
class MlflowExperimentTimeouts:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MlflowExperimentTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MlflowExperimentTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mlflowExperiment.MlflowExperimentTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ebc502c7ab0af4381295c20dd77de8c2f5c4e129f9f486bc361ddb28b32100b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MlflowExperimentTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MlflowExperimentTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MlflowExperimentTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22c607fd94b00434eda08662bba9e3034b01e37aa382c8b92756162d9f2d3ff6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MlflowExperiment",
    "MlflowExperimentConfig",
    "MlflowExperimentTimeouts",
    "MlflowExperimentTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__4c1847b5964484159ee9908ca977c8aeb8c67a707ed26d0ce2e1f375572845db(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    artifact_location: typing.Optional[builtins.str] = None,
    creation_time: typing.Optional[jsii.Number] = None,
    description: typing.Optional[builtins.str] = None,
    experiment_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    last_update_time: typing.Optional[jsii.Number] = None,
    lifecycle_stage: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[MlflowExperimentTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__bbdb31634026507cc7988ffb5e104c42ebd54d9a931d403dbe620b35faeb6f04(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaf5402ec9356aa49928105160f2f2660509b9fc093f31d894ffa71e6afd50c2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e753c880c1acc8fd6d76bc3abbd54553ae895b25271023ee9d2b8f8a0c3667f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab868d402e255d6eec25f2eed09f386895f2d7efb9a008dc7af64a9f83578bfc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__224ee63795129ba552708d07d2cf1ba7531a0c597409f04c6737fa500606f2c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6f4241f1c68020a446b5fd452b227d8bcb001b1289fc5f3f4e2c39a6da74cc6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c1bb8e024ce874431584a2e7564775b6e91268145b896fcfcd4385f1033a45b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d882c0ae031bc1aadf4b0f31b348cdaa3bfb1968054f5c05e8f85b0d82f06b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6569e5a232e74593e9aca308b325d5a9290b215dafcbeb97899c10ff7653a0d8(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    artifact_location: typing.Optional[builtins.str] = None,
    creation_time: typing.Optional[jsii.Number] = None,
    description: typing.Optional[builtins.str] = None,
    experiment_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    last_update_time: typing.Optional[jsii.Number] = None,
    lifecycle_stage: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[MlflowExperimentTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ebc502c7ab0af4381295c20dd77de8c2f5c4e129f9f486bc361ddb28b32100b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22c607fd94b00434eda08662bba9e3034b01e37aa382c8b92756162d9f2d3ff6(
    value: typing.Optional[typing.Union[MlflowExperimentTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
