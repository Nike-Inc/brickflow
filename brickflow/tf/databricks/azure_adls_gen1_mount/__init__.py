'''
# `databricks_azure_adls_gen1_mount`

Refer to the Terraform Registory for docs: [`databricks_azure_adls_gen1_mount`](https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount).
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


class AzureAdlsGen1Mount(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.azureAdlsGen1Mount.AzureAdlsGen1Mount",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount databricks_azure_adls_gen1_mount}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        client_id: builtins.str,
        client_secret_key: builtins.str,
        client_secret_scope: builtins.str,
        mount_name: builtins.str,
        storage_resource_name: builtins.str,
        tenant_id: builtins.str,
        cluster_id: typing.Optional[builtins.str] = None,
        directory: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        spark_conf_prefix: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount databricks_azure_adls_gen1_mount} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#client_id AzureAdlsGen1Mount#client_id}.
        :param client_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#client_secret_key AzureAdlsGen1Mount#client_secret_key}.
        :param client_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#client_secret_scope AzureAdlsGen1Mount#client_secret_scope}.
        :param mount_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#mount_name AzureAdlsGen1Mount#mount_name}.
        :param storage_resource_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#storage_resource_name AzureAdlsGen1Mount#storage_resource_name}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#tenant_id AzureAdlsGen1Mount#tenant_id}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#cluster_id AzureAdlsGen1Mount#cluster_id}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#directory AzureAdlsGen1Mount#directory}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#id AzureAdlsGen1Mount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param spark_conf_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#spark_conf_prefix AzureAdlsGen1Mount#spark_conf_prefix}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82e44be891054dbc0f7fd2e348e028d28af2f0ced4b3764dac6a3f5cf4462044)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AzureAdlsGen1MountConfig(
            client_id=client_id,
            client_secret_key=client_secret_key,
            client_secret_scope=client_secret_scope,
            mount_name=mount_name,
            storage_resource_name=storage_resource_name,
            tenant_id=tenant_id,
            cluster_id=cluster_id,
            directory=directory,
            id=id,
            spark_conf_prefix=spark_conf_prefix,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetClusterId")
    def reset_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterId", []))

    @jsii.member(jsii_name="resetDirectory")
    def reset_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectory", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSparkConfPrefix")
    def reset_spark_conf_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkConfPrefix", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretKeyInput")
    def client_secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretScopeInput")
    def client_secret_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryInput")
    def directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mountNameInput")
    def mount_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkConfPrefixInput")
    def spark_conf_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sparkConfPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="storageResourceNameInput")
    def storage_resource_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageResourceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07d59b6cdf68b90566335b099409812c1404969d2a5ea5f237dbf530ac13f335)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretKey")
    def client_secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretKey"))

    @client_secret_key.setter
    def client_secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9764b9cf7cc094ba2417271d819917674c55abf42eadebc79bb4242e2bb2af62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretKey", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretScope")
    def client_secret_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretScope"))

    @client_secret_scope.setter
    def client_secret_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62afa251be2a39d58d35e02c9c2633d7b1f57228e29c82f5b27f21bbedfdb8db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretScope", value)

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cd1b14e3b13e23d6e1f901966a796fb73aeaa8395581543fc9e3168c131dbea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="directory")
    def directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directory"))

    @directory.setter
    def directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a755df424737437a77b6490f11f731d50dcae7bfebaa944d501e830679f23dd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directory", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ea65543aa6e09504ab3be2f7c37607e8ed71a0ac24cac8de01cfc0e20689fd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mountName")
    def mount_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountName"))

    @mount_name.setter
    def mount_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d1040c1b5c4fbdbc31254e4c25e0ae2d6560f274d4fe93bd8a31445016bb548)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountName", value)

    @builtins.property
    @jsii.member(jsii_name="sparkConfPrefix")
    def spark_conf_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sparkConfPrefix"))

    @spark_conf_prefix.setter
    def spark_conf_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e2204389d4fa8ae5ed09339262fc372b840bf29b195d7c6ef1b05645c03fdf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkConfPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="storageResourceName")
    def storage_resource_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageResourceName"))

    @storage_resource_name.setter
    def storage_resource_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6633d97e8f240bdc047755ed1d00f6ca738c4c75ee6df9b85d37f31a22e75eb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageResourceName", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc1224f071bf72170cd3930aee2603dd6847df29b2c01e7229bd6b21b30cbfb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)


@jsii.data_type(
    jsii_type="databricks.azureAdlsGen1Mount.AzureAdlsGen1MountConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "client_id": "clientId",
        "client_secret_key": "clientSecretKey",
        "client_secret_scope": "clientSecretScope",
        "mount_name": "mountName",
        "storage_resource_name": "storageResourceName",
        "tenant_id": "tenantId",
        "cluster_id": "clusterId",
        "directory": "directory",
        "id": "id",
        "spark_conf_prefix": "sparkConfPrefix",
    },
)
class AzureAdlsGen1MountConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        client_id: builtins.str,
        client_secret_key: builtins.str,
        client_secret_scope: builtins.str,
        mount_name: builtins.str,
        storage_resource_name: builtins.str,
        tenant_id: builtins.str,
        cluster_id: typing.Optional[builtins.str] = None,
        directory: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        spark_conf_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#client_id AzureAdlsGen1Mount#client_id}.
        :param client_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#client_secret_key AzureAdlsGen1Mount#client_secret_key}.
        :param client_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#client_secret_scope AzureAdlsGen1Mount#client_secret_scope}.
        :param mount_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#mount_name AzureAdlsGen1Mount#mount_name}.
        :param storage_resource_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#storage_resource_name AzureAdlsGen1Mount#storage_resource_name}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#tenant_id AzureAdlsGen1Mount#tenant_id}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#cluster_id AzureAdlsGen1Mount#cluster_id}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#directory AzureAdlsGen1Mount#directory}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#id AzureAdlsGen1Mount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param spark_conf_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#spark_conf_prefix AzureAdlsGen1Mount#spark_conf_prefix}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e5fefa5c1c9ae699ff03b8f4c72b0c4f9d30ad4665428d7cb18e860bdcd8385)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret_key", value=client_secret_key, expected_type=type_hints["client_secret_key"])
            check_type(argname="argument client_secret_scope", value=client_secret_scope, expected_type=type_hints["client_secret_scope"])
            check_type(argname="argument mount_name", value=mount_name, expected_type=type_hints["mount_name"])
            check_type(argname="argument storage_resource_name", value=storage_resource_name, expected_type=type_hints["storage_resource_name"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument spark_conf_prefix", value=spark_conf_prefix, expected_type=type_hints["spark_conf_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "client_secret_key": client_secret_key,
            "client_secret_scope": client_secret_scope,
            "mount_name": mount_name,
            "storage_resource_name": storage_resource_name,
            "tenant_id": tenant_id,
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
        if cluster_id is not None:
            self._values["cluster_id"] = cluster_id
        if directory is not None:
            self._values["directory"] = directory
        if id is not None:
            self._values["id"] = id
        if spark_conf_prefix is not None:
            self._values["spark_conf_prefix"] = spark_conf_prefix

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
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#client_id AzureAdlsGen1Mount#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#client_secret_key AzureAdlsGen1Mount#client_secret_key}.'''
        result = self._values.get("client_secret_key")
        assert result is not None, "Required property 'client_secret_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#client_secret_scope AzureAdlsGen1Mount#client_secret_scope}.'''
        result = self._values.get("client_secret_scope")
        assert result is not None, "Required property 'client_secret_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mount_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#mount_name AzureAdlsGen1Mount#mount_name}.'''
        result = self._values.get("mount_name")
        assert result is not None, "Required property 'mount_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_resource_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#storage_resource_name AzureAdlsGen1Mount#storage_resource_name}.'''
        result = self._values.get("storage_resource_name")
        assert result is not None, "Required property 'storage_resource_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tenant_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#tenant_id AzureAdlsGen1Mount#tenant_id}.'''
        result = self._values.get("tenant_id")
        assert result is not None, "Required property 'tenant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#cluster_id AzureAdlsGen1Mount#cluster_id}.'''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#directory AzureAdlsGen1Mount#directory}.'''
        result = self._values.get("directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#id AzureAdlsGen1Mount#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spark_conf_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen1_mount#spark_conf_prefix AzureAdlsGen1Mount#spark_conf_prefix}.'''
        result = self._values.get("spark_conf_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzureAdlsGen1MountConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AzureAdlsGen1Mount",
    "AzureAdlsGen1MountConfig",
]

publication.publish()

def _typecheckingstub__82e44be891054dbc0f7fd2e348e028d28af2f0ced4b3764dac6a3f5cf4462044(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    client_id: builtins.str,
    client_secret_key: builtins.str,
    client_secret_scope: builtins.str,
    mount_name: builtins.str,
    storage_resource_name: builtins.str,
    tenant_id: builtins.str,
    cluster_id: typing.Optional[builtins.str] = None,
    directory: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    spark_conf_prefix: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__07d59b6cdf68b90566335b099409812c1404969d2a5ea5f237dbf530ac13f335(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9764b9cf7cc094ba2417271d819917674c55abf42eadebc79bb4242e2bb2af62(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62afa251be2a39d58d35e02c9c2633d7b1f57228e29c82f5b27f21bbedfdb8db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cd1b14e3b13e23d6e1f901966a796fb73aeaa8395581543fc9e3168c131dbea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a755df424737437a77b6490f11f731d50dcae7bfebaa944d501e830679f23dd0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ea65543aa6e09504ab3be2f7c37607e8ed71a0ac24cac8de01cfc0e20689fd9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d1040c1b5c4fbdbc31254e4c25e0ae2d6560f274d4fe93bd8a31445016bb548(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e2204389d4fa8ae5ed09339262fc372b840bf29b195d7c6ef1b05645c03fdf9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6633d97e8f240bdc047755ed1d00f6ca738c4c75ee6df9b85d37f31a22e75eb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc1224f071bf72170cd3930aee2603dd6847df29b2c01e7229bd6b21b30cbfb4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e5fefa5c1c9ae699ff03b8f4c72b0c4f9d30ad4665428d7cb18e860bdcd8385(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    client_id: builtins.str,
    client_secret_key: builtins.str,
    client_secret_scope: builtins.str,
    mount_name: builtins.str,
    storage_resource_name: builtins.str,
    tenant_id: builtins.str,
    cluster_id: typing.Optional[builtins.str] = None,
    directory: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    spark_conf_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
