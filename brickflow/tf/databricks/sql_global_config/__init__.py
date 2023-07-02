'''
# `databricks_sql_global_config`

Refer to the Terraform Registory for docs: [`databricks_sql_global_config`](https://www.terraform.io/docs/providers/databricks/r/sql_global_config).
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


class SqlGlobalConfig(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.sqlGlobalConfig.SqlGlobalConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config databricks_sql_global_config}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        data_access_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        enable_serverless_compute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        instance_profile_arn: typing.Optional[builtins.str] = None,
        security_policy: typing.Optional[builtins.str] = None,
        sql_config_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config databricks_sql_global_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_access_config: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#data_access_config SqlGlobalConfig#data_access_config}.
        :param enable_serverless_compute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#enable_serverless_compute SqlGlobalConfig#enable_serverless_compute}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#id SqlGlobalConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#instance_profile_arn SqlGlobalConfig#instance_profile_arn}.
        :param security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#security_policy SqlGlobalConfig#security_policy}.
        :param sql_config_params: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#sql_config_params SqlGlobalConfig#sql_config_params}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c32db073f290473869e8872cb307d68ff48ac9d3d7081937e623192186e16050)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SqlGlobalConfigConfig(
            data_access_config=data_access_config,
            enable_serverless_compute=enable_serverless_compute,
            id=id,
            instance_profile_arn=instance_profile_arn,
            security_policy=security_policy,
            sql_config_params=sql_config_params,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDataAccessConfig")
    def reset_data_access_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataAccessConfig", []))

    @jsii.member(jsii_name="resetEnableServerlessCompute")
    def reset_enable_serverless_compute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableServerlessCompute", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstanceProfileArn")
    def reset_instance_profile_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceProfileArn", []))

    @jsii.member(jsii_name="resetSecurityPolicy")
    def reset_security_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityPolicy", []))

    @jsii.member(jsii_name="resetSqlConfigParams")
    def reset_sql_config_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlConfigParams", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="dataAccessConfigInput")
    def data_access_config_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dataAccessConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="enableServerlessComputeInput")
    def enable_serverless_compute_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableServerlessComputeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceProfileArnInput")
    def instance_profile_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceProfileArnInput"))

    @builtins.property
    @jsii.member(jsii_name="securityPolicyInput")
    def security_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlConfigParamsInput")
    def sql_config_params_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sqlConfigParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataAccessConfig")
    def data_access_config(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "dataAccessConfig"))

    @data_access_config.setter
    def data_access_config(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__715d21f567c93780567d0f71b263be99efe90c0ec4807235d29e1bc0e4810051)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataAccessConfig", value)

    @builtins.property
    @jsii.member(jsii_name="enableServerlessCompute")
    def enable_serverless_compute(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableServerlessCompute"))

    @enable_serverless_compute.setter
    def enable_serverless_compute(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49349b771e494cff0bc4ba9620c10e35076880daaa19f908bd34a6105a13dba0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableServerlessCompute", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__390c56d04a36ab017bd91d75c993d11ac6f7f47c161adde7cec95d255ec1c23b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfileArn")
    def instance_profile_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceProfileArn"))

    @instance_profile_arn.setter
    def instance_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7029fac2e7f5324d103056428621d014ef4a089a06913a8fad51aaf76d1ba9df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="securityPolicy")
    def security_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityPolicy"))

    @security_policy.setter
    def security_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2bab47b471399f7ab736c293e13ec6e8e73590892caf53002548ef66f71b083)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="sqlConfigParams")
    def sql_config_params(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sqlConfigParams"))

    @sql_config_params.setter
    def sql_config_params(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f428206fdad866657ab6cf8c55602793d096409e8be85dfa534d27016770f5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlConfigParams", value)


@jsii.data_type(
    jsii_type="databricks.sqlGlobalConfig.SqlGlobalConfigConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_access_config": "dataAccessConfig",
        "enable_serverless_compute": "enableServerlessCompute",
        "id": "id",
        "instance_profile_arn": "instanceProfileArn",
        "security_policy": "securityPolicy",
        "sql_config_params": "sqlConfigParams",
    },
)
class SqlGlobalConfigConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        data_access_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        enable_serverless_compute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        instance_profile_arn: typing.Optional[builtins.str] = None,
        security_policy: typing.Optional[builtins.str] = None,
        sql_config_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_access_config: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#data_access_config SqlGlobalConfig#data_access_config}.
        :param enable_serverless_compute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#enable_serverless_compute SqlGlobalConfig#enable_serverless_compute}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#id SqlGlobalConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#instance_profile_arn SqlGlobalConfig#instance_profile_arn}.
        :param security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#security_policy SqlGlobalConfig#security_policy}.
        :param sql_config_params: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#sql_config_params SqlGlobalConfig#sql_config_params}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba55b9c9700775f7418dd4a04dfcc658b690bdc7310f94335d9014798f6b28f7)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument data_access_config", value=data_access_config, expected_type=type_hints["data_access_config"])
            check_type(argname="argument enable_serverless_compute", value=enable_serverless_compute, expected_type=type_hints["enable_serverless_compute"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_profile_arn", value=instance_profile_arn, expected_type=type_hints["instance_profile_arn"])
            check_type(argname="argument security_policy", value=security_policy, expected_type=type_hints["security_policy"])
            check_type(argname="argument sql_config_params", value=sql_config_params, expected_type=type_hints["sql_config_params"])
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
        if data_access_config is not None:
            self._values["data_access_config"] = data_access_config
        if enable_serverless_compute is not None:
            self._values["enable_serverless_compute"] = enable_serverless_compute
        if id is not None:
            self._values["id"] = id
        if instance_profile_arn is not None:
            self._values["instance_profile_arn"] = instance_profile_arn
        if security_policy is not None:
            self._values["security_policy"] = security_policy
        if sql_config_params is not None:
            self._values["sql_config_params"] = sql_config_params

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
    def data_access_config(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#data_access_config SqlGlobalConfig#data_access_config}.'''
        result = self._values.get("data_access_config")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def enable_serverless_compute(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#enable_serverless_compute SqlGlobalConfig#enable_serverless_compute}.'''
        result = self._values.get("enable_serverless_compute")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#id SqlGlobalConfig#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#instance_profile_arn SqlGlobalConfig#instance_profile_arn}.'''
        result = self._values.get("instance_profile_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#security_policy SqlGlobalConfig#security_policy}.'''
        result = self._values.get("security_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sql_config_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_global_config#sql_config_params SqlGlobalConfig#sql_config_params}.'''
        result = self._values.get("sql_config_params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlGlobalConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SqlGlobalConfig",
    "SqlGlobalConfigConfig",
]

publication.publish()

def _typecheckingstub__c32db073f290473869e8872cb307d68ff48ac9d3d7081937e623192186e16050(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    data_access_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    enable_serverless_compute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    instance_profile_arn: typing.Optional[builtins.str] = None,
    security_policy: typing.Optional[builtins.str] = None,
    sql_config_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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

def _typecheckingstub__715d21f567c93780567d0f71b263be99efe90c0ec4807235d29e1bc0e4810051(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49349b771e494cff0bc4ba9620c10e35076880daaa19f908bd34a6105a13dba0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__390c56d04a36ab017bd91d75c993d11ac6f7f47c161adde7cec95d255ec1c23b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7029fac2e7f5324d103056428621d014ef4a089a06913a8fad51aaf76d1ba9df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2bab47b471399f7ab736c293e13ec6e8e73590892caf53002548ef66f71b083(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f428206fdad866657ab6cf8c55602793d096409e8be85dfa534d27016770f5e(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba55b9c9700775f7418dd4a04dfcc658b690bdc7310f94335d9014798f6b28f7(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    data_access_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    enable_serverless_compute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    instance_profile_arn: typing.Optional[builtins.str] = None,
    security_policy: typing.Optional[builtins.str] = None,
    sql_config_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
