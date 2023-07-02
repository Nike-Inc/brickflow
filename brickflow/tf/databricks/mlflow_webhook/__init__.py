'''
# `databricks_mlflow_webhook`

Refer to the Terraform Registory for docs: [`databricks_mlflow_webhook`](https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook).
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


class MlflowWebhook(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mlflowWebhook.MlflowWebhook",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook databricks_mlflow_webhook}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        events: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        http_url_spec: typing.Optional[typing.Union["MlflowWebhookHttpUrlSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        job_spec: typing.Optional[typing.Union["MlflowWebhookJobSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        model_name: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook databricks_mlflow_webhook} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#events MlflowWebhook#events}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#description MlflowWebhook#description}.
        :param http_url_spec: http_url_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#http_url_spec MlflowWebhook#http_url_spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#id MlflowWebhook#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param job_spec: job_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#job_spec MlflowWebhook#job_spec}
        :param model_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#model_name MlflowWebhook#model_name}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#status MlflowWebhook#status}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c41d0c44add0fc705e1407b92054d126a7866b1208be1f9f96810a861f8f4317)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MlflowWebhookConfig(
            events=events,
            description=description,
            http_url_spec=http_url_spec,
            id=id,
            job_spec=job_spec,
            model_name=model_name,
            status=status,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putHttpUrlSpec")
    def put_http_url_spec(
        self,
        *,
        url: builtins.str,
        authorization: typing.Optional[builtins.str] = None,
        enable_ssl_verification: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#url MlflowWebhook#url}.
        :param authorization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#authorization MlflowWebhook#authorization}.
        :param enable_ssl_verification: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#enable_ssl_verification MlflowWebhook#enable_ssl_verification}.
        :param secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#secret MlflowWebhook#secret}.
        '''
        value = MlflowWebhookHttpUrlSpec(
            url=url,
            authorization=authorization,
            enable_ssl_verification=enable_ssl_verification,
            secret=secret,
        )

        return typing.cast(None, jsii.invoke(self, "putHttpUrlSpec", [value]))

    @jsii.member(jsii_name="putJobSpec")
    def put_job_spec(
        self,
        *,
        access_token: builtins.str,
        job_id: builtins.str,
        workspace_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#access_token MlflowWebhook#access_token}.
        :param job_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#job_id MlflowWebhook#job_id}.
        :param workspace_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#workspace_url MlflowWebhook#workspace_url}.
        '''
        value = MlflowWebhookJobSpec(
            access_token=access_token, job_id=job_id, workspace_url=workspace_url
        )

        return typing.cast(None, jsii.invoke(self, "putJobSpec", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetHttpUrlSpec")
    def reset_http_url_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpUrlSpec", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetJobSpec")
    def reset_job_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobSpec", []))

    @jsii.member(jsii_name="resetModelName")
    def reset_model_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModelName", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="httpUrlSpec")
    def http_url_spec(self) -> "MlflowWebhookHttpUrlSpecOutputReference":
        return typing.cast("MlflowWebhookHttpUrlSpecOutputReference", jsii.get(self, "httpUrlSpec"))

    @builtins.property
    @jsii.member(jsii_name="jobSpec")
    def job_spec(self) -> "MlflowWebhookJobSpecOutputReference":
        return typing.cast("MlflowWebhookJobSpecOutputReference", jsii.get(self, "jobSpec"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="eventsInput")
    def events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpUrlSpecInput")
    def http_url_spec_input(self) -> typing.Optional["MlflowWebhookHttpUrlSpec"]:
        return typing.cast(typing.Optional["MlflowWebhookHttpUrlSpec"], jsii.get(self, "httpUrlSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="jobSpecInput")
    def job_spec_input(self) -> typing.Optional["MlflowWebhookJobSpec"]:
        return typing.cast(typing.Optional["MlflowWebhookJobSpec"], jsii.get(self, "jobSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="modelNameInput")
    def model_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelNameInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02c87811bba8eee1d5b1b176ddad0c396a7d596f3f5c86cac1d65abbb5620f04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="events")
    def events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "events"))

    @events.setter
    def events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adb32c8fbe2212cbdf205a11497f49360c7bba4c48618e5c0fd08e7fc3c66705)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "events", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aea18514bd552d78b1cbd97ba69cf4926e27e8b792e9472d223e5c01d13e01e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="modelName")
    def model_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modelName"))

    @model_name.setter
    def model_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed13c321624e6d42859aa9128a8b67dffeaf7526da20411777d82b52d4678c63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelName", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5956ba59c59493018298ad86a0bec8a75d16b818d6c77ad0a00ae99f5da6215c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="databricks.mlflowWebhook.MlflowWebhookConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "events": "events",
        "description": "description",
        "http_url_spec": "httpUrlSpec",
        "id": "id",
        "job_spec": "jobSpec",
        "model_name": "modelName",
        "status": "status",
    },
)
class MlflowWebhookConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        events: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        http_url_spec: typing.Optional[typing.Union["MlflowWebhookHttpUrlSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        job_spec: typing.Optional[typing.Union["MlflowWebhookJobSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        model_name: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#events MlflowWebhook#events}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#description MlflowWebhook#description}.
        :param http_url_spec: http_url_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#http_url_spec MlflowWebhook#http_url_spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#id MlflowWebhook#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param job_spec: job_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#job_spec MlflowWebhook#job_spec}
        :param model_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#model_name MlflowWebhook#model_name}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#status MlflowWebhook#status}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(http_url_spec, dict):
            http_url_spec = MlflowWebhookHttpUrlSpec(**http_url_spec)
        if isinstance(job_spec, dict):
            job_spec = MlflowWebhookJobSpec(**job_spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f8decfd72606f106eaac8ca95b543919d0c55f5cb645395acade1868a68bae1)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument http_url_spec", value=http_url_spec, expected_type=type_hints["http_url_spec"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument job_spec", value=job_spec, expected_type=type_hints["job_spec"])
            check_type(argname="argument model_name", value=model_name, expected_type=type_hints["model_name"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "events": events,
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
        if http_url_spec is not None:
            self._values["http_url_spec"] = http_url_spec
        if id is not None:
            self._values["id"] = id
        if job_spec is not None:
            self._values["job_spec"] = job_spec
        if model_name is not None:
            self._values["model_name"] = model_name
        if status is not None:
            self._values["status"] = status

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
    def events(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#events MlflowWebhook#events}.'''
        result = self._values.get("events")
        assert result is not None, "Required property 'events' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#description MlflowWebhook#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_url_spec(self) -> typing.Optional["MlflowWebhookHttpUrlSpec"]:
        '''http_url_spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#http_url_spec MlflowWebhook#http_url_spec}
        '''
        result = self._values.get("http_url_spec")
        return typing.cast(typing.Optional["MlflowWebhookHttpUrlSpec"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#id MlflowWebhook#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_spec(self) -> typing.Optional["MlflowWebhookJobSpec"]:
        '''job_spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#job_spec MlflowWebhook#job_spec}
        '''
        result = self._values.get("job_spec")
        return typing.cast(typing.Optional["MlflowWebhookJobSpec"], result)

    @builtins.property
    def model_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#model_name MlflowWebhook#model_name}.'''
        result = self._values.get("model_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#status MlflowWebhook#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MlflowWebhookConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.mlflowWebhook.MlflowWebhookHttpUrlSpec",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "authorization": "authorization",
        "enable_ssl_verification": "enableSslVerification",
        "secret": "secret",
    },
)
class MlflowWebhookHttpUrlSpec:
    def __init__(
        self,
        *,
        url: builtins.str,
        authorization: typing.Optional[builtins.str] = None,
        enable_ssl_verification: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secret: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#url MlflowWebhook#url}.
        :param authorization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#authorization MlflowWebhook#authorization}.
        :param enable_ssl_verification: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#enable_ssl_verification MlflowWebhook#enable_ssl_verification}.
        :param secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#secret MlflowWebhook#secret}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eac6efa6979be7737d4f13638ccf46b89ae5381052cf984ba8f33d7f069ab6c7)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument authorization", value=authorization, expected_type=type_hints["authorization"])
            check_type(argname="argument enable_ssl_verification", value=enable_ssl_verification, expected_type=type_hints["enable_ssl_verification"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if authorization is not None:
            self._values["authorization"] = authorization
        if enable_ssl_verification is not None:
            self._values["enable_ssl_verification"] = enable_ssl_verification
        if secret is not None:
            self._values["secret"] = secret

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#url MlflowWebhook#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorization(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#authorization MlflowWebhook#authorization}.'''
        result = self._values.get("authorization")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_ssl_verification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#enable_ssl_verification MlflowWebhook#enable_ssl_verification}.'''
        result = self._values.get("enable_ssl_verification")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secret(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#secret MlflowWebhook#secret}.'''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MlflowWebhookHttpUrlSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MlflowWebhookHttpUrlSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mlflowWebhook.MlflowWebhookHttpUrlSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4963c63f25a6bbb538faf5d0db384896bd68bef5761adf0a80d4dc72b96f92e6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthorization")
    def reset_authorization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorization", []))

    @jsii.member(jsii_name="resetEnableSslVerification")
    def reset_enable_ssl_verification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableSslVerification", []))

    @jsii.member(jsii_name="resetSecret")
    def reset_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecret", []))

    @builtins.property
    @jsii.member(jsii_name="authorizationInput")
    def authorization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationInput"))

    @builtins.property
    @jsii.member(jsii_name="enableSslVerificationInput")
    def enable_ssl_verification_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableSslVerificationInput"))

    @builtins.property
    @jsii.member(jsii_name="secretInput")
    def secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="authorization")
    def authorization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorization"))

    @authorization.setter
    def authorization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9632a3dcaa8a858672bf44d63426855300ed4d5184ed9279c5ebb8378dbf5ff5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorization", value)

    @builtins.property
    @jsii.member(jsii_name="enableSslVerification")
    def enable_ssl_verification(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableSslVerification"))

    @enable_ssl_verification.setter
    def enable_ssl_verification(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d35a20435106f85eefa8ab7f109f8c7d86caadc84a08b7158f40adc335fa0c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSslVerification", value)

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secret"))

    @secret.setter
    def secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5c8cba7bd62dd1ddede6023767ec30c7769434c6297d8832a93540ca37edb14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secret", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c69fadb6a8debcff622ee0a47fdb2fabf9f2444305f07776859bd366783a7abd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MlflowWebhookHttpUrlSpec]:
        return typing.cast(typing.Optional[MlflowWebhookHttpUrlSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MlflowWebhookHttpUrlSpec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04f4dca9b3efa39d634529e4f435d736f2346502e59dae680d2f895c5ff0aa5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.mlflowWebhook.MlflowWebhookJobSpec",
    jsii_struct_bases=[],
    name_mapping={
        "access_token": "accessToken",
        "job_id": "jobId",
        "workspace_url": "workspaceUrl",
    },
)
class MlflowWebhookJobSpec:
    def __init__(
        self,
        *,
        access_token: builtins.str,
        job_id: builtins.str,
        workspace_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#access_token MlflowWebhook#access_token}.
        :param job_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#job_id MlflowWebhook#job_id}.
        :param workspace_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#workspace_url MlflowWebhook#workspace_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8da6fa55a604cc1f060c582b5f0e2774a36fd0d0bd0629fee7cfb7c6ae680978)
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument job_id", value=job_id, expected_type=type_hints["job_id"])
            check_type(argname="argument workspace_url", value=workspace_url, expected_type=type_hints["workspace_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_token": access_token,
            "job_id": job_id,
        }
        if workspace_url is not None:
            self._values["workspace_url"] = workspace_url

    @builtins.property
    def access_token(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#access_token MlflowWebhook#access_token}.'''
        result = self._values.get("access_token")
        assert result is not None, "Required property 'access_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def job_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#job_id MlflowWebhook#job_id}.'''
        result = self._values.get("job_id")
        assert result is not None, "Required property 'job_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mlflow_webhook#workspace_url MlflowWebhook#workspace_url}.'''
        result = self._values.get("workspace_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MlflowWebhookJobSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MlflowWebhookJobSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mlflowWebhook.MlflowWebhookJobSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3bc70d0f1b84bac22c1e5d1545871b91828b92d890a875a0c1347c9c347fe038)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetWorkspaceUrl")
    def reset_workspace_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceUrl", []))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="jobIdInput")
    def job_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobIdInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceUrlInput")
    def workspace_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workspaceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e5b777587db2e6547d3ee6a4fcfb4f90f22c27862d8420b3ea467ba57fccebe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="jobId")
    def job_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobId"))

    @job_id.setter
    def job_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e5952e96ff3552dc0c5f551d4d1900b0d6aacf42e3dc39edb304f629ad37bb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobId", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceUrl")
    def workspace_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceUrl"))

    @workspace_url.setter
    def workspace_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0cef7181e1f2cf5cf70f80ef222055be586845eecc09410f583491a58de940a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MlflowWebhookJobSpec]:
        return typing.cast(typing.Optional[MlflowWebhookJobSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MlflowWebhookJobSpec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ee678ac0977fade209fffde1096aa3a5fd04575b967d9262d6ecbc0289f1077)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MlflowWebhook",
    "MlflowWebhookConfig",
    "MlflowWebhookHttpUrlSpec",
    "MlflowWebhookHttpUrlSpecOutputReference",
    "MlflowWebhookJobSpec",
    "MlflowWebhookJobSpecOutputReference",
]

publication.publish()

def _typecheckingstub__c41d0c44add0fc705e1407b92054d126a7866b1208be1f9f96810a861f8f4317(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    events: typing.Sequence[builtins.str],
    description: typing.Optional[builtins.str] = None,
    http_url_spec: typing.Optional[typing.Union[MlflowWebhookHttpUrlSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    job_spec: typing.Optional[typing.Union[MlflowWebhookJobSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    model_name: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__02c87811bba8eee1d5b1b176ddad0c396a7d596f3f5c86cac1d65abbb5620f04(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adb32c8fbe2212cbdf205a11497f49360c7bba4c48618e5c0fd08e7fc3c66705(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aea18514bd552d78b1cbd97ba69cf4926e27e8b792e9472d223e5c01d13e01e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed13c321624e6d42859aa9128a8b67dffeaf7526da20411777d82b52d4678c63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5956ba59c59493018298ad86a0bec8a75d16b818d6c77ad0a00ae99f5da6215c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f8decfd72606f106eaac8ca95b543919d0c55f5cb645395acade1868a68bae1(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    events: typing.Sequence[builtins.str],
    description: typing.Optional[builtins.str] = None,
    http_url_spec: typing.Optional[typing.Union[MlflowWebhookHttpUrlSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    job_spec: typing.Optional[typing.Union[MlflowWebhookJobSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    model_name: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eac6efa6979be7737d4f13638ccf46b89ae5381052cf984ba8f33d7f069ab6c7(
    *,
    url: builtins.str,
    authorization: typing.Optional[builtins.str] = None,
    enable_ssl_verification: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secret: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4963c63f25a6bbb538faf5d0db384896bd68bef5761adf0a80d4dc72b96f92e6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9632a3dcaa8a858672bf44d63426855300ed4d5184ed9279c5ebb8378dbf5ff5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d35a20435106f85eefa8ab7f109f8c7d86caadc84a08b7158f40adc335fa0c3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5c8cba7bd62dd1ddede6023767ec30c7769434c6297d8832a93540ca37edb14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c69fadb6a8debcff622ee0a47fdb2fabf9f2444305f07776859bd366783a7abd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04f4dca9b3efa39d634529e4f435d736f2346502e59dae680d2f895c5ff0aa5f(
    value: typing.Optional[MlflowWebhookHttpUrlSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8da6fa55a604cc1f060c582b5f0e2774a36fd0d0bd0629fee7cfb7c6ae680978(
    *,
    access_token: builtins.str,
    job_id: builtins.str,
    workspace_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bc70d0f1b84bac22c1e5d1545871b91828b92d890a875a0c1347c9c347fe038(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e5b777587db2e6547d3ee6a4fcfb4f90f22c27862d8420b3ea467ba57fccebe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e5952e96ff3552dc0c5f551d4d1900b0d6aacf42e3dc39edb304f629ad37bb6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0cef7181e1f2cf5cf70f80ef222055be586845eecc09410f583491a58de940a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ee678ac0977fade209fffde1096aa3a5fd04575b967d9262d6ecbc0289f1077(
    value: typing.Optional[MlflowWebhookJobSpec],
) -> None:
    """Type checking stubs"""
    pass
