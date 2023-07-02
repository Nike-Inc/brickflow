'''
# `databricks_azure_adls_gen2_mount`

Refer to the Terraform Registory for docs: [`databricks_azure_adls_gen2_mount`](https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount).
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


class AzureAdlsGen2Mount(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.azureAdlsGen2Mount.AzureAdlsGen2Mount",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount databricks_azure_adls_gen2_mount}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        client_id: builtins.str,
        client_secret_key: builtins.str,
        client_secret_scope: builtins.str,
        container_name: builtins.str,
        initialize_file_system: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        mount_name: builtins.str,
        storage_account_name: builtins.str,
        tenant_id: builtins.str,
        cluster_id: typing.Optional[builtins.str] = None,
        directory: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount databricks_azure_adls_gen2_mount} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#client_id AzureAdlsGen2Mount#client_id}.
        :param client_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#client_secret_key AzureAdlsGen2Mount#client_secret_key}.
        :param client_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#client_secret_scope AzureAdlsGen2Mount#client_secret_scope}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#container_name AzureAdlsGen2Mount#container_name}.
        :param initialize_file_system: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#initialize_file_system AzureAdlsGen2Mount#initialize_file_system}.
        :param mount_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#mount_name AzureAdlsGen2Mount#mount_name}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#storage_account_name AzureAdlsGen2Mount#storage_account_name}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#tenant_id AzureAdlsGen2Mount#tenant_id}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#cluster_id AzureAdlsGen2Mount#cluster_id}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#directory AzureAdlsGen2Mount#directory}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#id AzureAdlsGen2Mount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54c5873e29e4f762aab4a05b70a6f10dc58e1296de2d3ae1aa0bf6a7fd26b7e7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AzureAdlsGen2MountConfig(
            client_id=client_id,
            client_secret_key=client_secret_key,
            client_secret_scope=client_secret_scope,
            container_name=container_name,
            initialize_file_system=initialize_file_system,
            mount_name=mount_name,
            storage_account_name=storage_account_name,
            tenant_id=tenant_id,
            cluster_id=cluster_id,
            directory=directory,
            id=id,
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
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryInput")
    def directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initializeFileSystemInput")
    def initialize_file_system_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "initializeFileSystemInput"))

    @builtins.property
    @jsii.member(jsii_name="mountNameInput")
    def mount_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountNameInput")
    def storage_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountNameInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__b7a3fbcbb41f154c79134612b853ac88d72a032739b223afa1b386debbadf235)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretKey")
    def client_secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretKey"))

    @client_secret_key.setter
    def client_secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e998337694544fa9d7adb20ab864008ab527ec434993a5eb0a3783e02263b1e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretKey", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretScope")
    def client_secret_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretScope"))

    @client_secret_scope.setter
    def client_secret_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e543e57d1e4c0f24acd13f38b22123ebf8972680490308b1e7a9fa67b939ae65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretScope", value)

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4544df404ce7379b695c777779439e4784f24729ef8c55702ccda5595773b774)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cad2adeb75100568be39286f8b6f0fe027e37005e7a086b6264a60a265cc9b54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="directory")
    def directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directory"))

    @directory.setter
    def directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b92a2837f6911d31b4b6057024d286140fe18ba945ca9c7d6e36c7dd3bcf61b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directory", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9fcdb2c6ebd550ee59f7e30b82add4dabde8c1b9a6feafd5c6d96063d0926b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="initializeFileSystem")
    def initialize_file_system(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "initializeFileSystem"))

    @initialize_file_system.setter
    def initialize_file_system(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27f5ab3ce86b29cba1450fd88ec65da7ca17694b8392e1a1ff413dfbbc5b6b0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initializeFileSystem", value)

    @builtins.property
    @jsii.member(jsii_name="mountName")
    def mount_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountName"))

    @mount_name.setter
    def mount_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08f8001241f88e8fa3ad8233e7b74bd3492b0134074af526ba7920aa7618618f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountName", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountName")
    def storage_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountName"))

    @storage_account_name.setter
    def storage_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff51020a00b59aebb11c698c86585b1a1c78e33043c15b84eea7243dbf1bd78f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5d256b7eb039398e49f8e1f28a7987ffe707acc57c6eb3a1e7cfe4d92728b4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)


@jsii.data_type(
    jsii_type="databricks.azureAdlsGen2Mount.AzureAdlsGen2MountConfig",
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
        "container_name": "containerName",
        "initialize_file_system": "initializeFileSystem",
        "mount_name": "mountName",
        "storage_account_name": "storageAccountName",
        "tenant_id": "tenantId",
        "cluster_id": "clusterId",
        "directory": "directory",
        "id": "id",
    },
)
class AzureAdlsGen2MountConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        container_name: builtins.str,
        initialize_file_system: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        mount_name: builtins.str,
        storage_account_name: builtins.str,
        tenant_id: builtins.str,
        cluster_id: typing.Optional[builtins.str] = None,
        directory: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#client_id AzureAdlsGen2Mount#client_id}.
        :param client_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#client_secret_key AzureAdlsGen2Mount#client_secret_key}.
        :param client_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#client_secret_scope AzureAdlsGen2Mount#client_secret_scope}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#container_name AzureAdlsGen2Mount#container_name}.
        :param initialize_file_system: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#initialize_file_system AzureAdlsGen2Mount#initialize_file_system}.
        :param mount_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#mount_name AzureAdlsGen2Mount#mount_name}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#storage_account_name AzureAdlsGen2Mount#storage_account_name}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#tenant_id AzureAdlsGen2Mount#tenant_id}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#cluster_id AzureAdlsGen2Mount#cluster_id}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#directory AzureAdlsGen2Mount#directory}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#id AzureAdlsGen2Mount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9e020dc77f167c93fc538c479ad616cc829fe30289d63ffba33c1d4684de0cb)
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
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument initialize_file_system", value=initialize_file_system, expected_type=type_hints["initialize_file_system"])
            check_type(argname="argument mount_name", value=mount_name, expected_type=type_hints["mount_name"])
            check_type(argname="argument storage_account_name", value=storage_account_name, expected_type=type_hints["storage_account_name"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "client_secret_key": client_secret_key,
            "client_secret_scope": client_secret_scope,
            "container_name": container_name,
            "initialize_file_system": initialize_file_system,
            "mount_name": mount_name,
            "storage_account_name": storage_account_name,
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#client_id AzureAdlsGen2Mount#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#client_secret_key AzureAdlsGen2Mount#client_secret_key}.'''
        result = self._values.get("client_secret_key")
        assert result is not None, "Required property 'client_secret_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#client_secret_scope AzureAdlsGen2Mount#client_secret_scope}.'''
        result = self._values.get("client_secret_scope")
        assert result is not None, "Required property 'client_secret_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#container_name AzureAdlsGen2Mount#container_name}.'''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def initialize_file_system(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#initialize_file_system AzureAdlsGen2Mount#initialize_file_system}.'''
        result = self._values.get("initialize_file_system")
        assert result is not None, "Required property 'initialize_file_system' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def mount_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#mount_name AzureAdlsGen2Mount#mount_name}.'''
        result = self._values.get("mount_name")
        assert result is not None, "Required property 'mount_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#storage_account_name AzureAdlsGen2Mount#storage_account_name}.'''
        result = self._values.get("storage_account_name")
        assert result is not None, "Required property 'storage_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tenant_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#tenant_id AzureAdlsGen2Mount#tenant_id}.'''
        result = self._values.get("tenant_id")
        assert result is not None, "Required property 'tenant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#cluster_id AzureAdlsGen2Mount#cluster_id}.'''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#directory AzureAdlsGen2Mount#directory}.'''
        result = self._values.get("directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_adls_gen2_mount#id AzureAdlsGen2Mount#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzureAdlsGen2MountConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AzureAdlsGen2Mount",
    "AzureAdlsGen2MountConfig",
]

publication.publish()

def _typecheckingstub__54c5873e29e4f762aab4a05b70a6f10dc58e1296de2d3ae1aa0bf6a7fd26b7e7(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    client_id: builtins.str,
    client_secret_key: builtins.str,
    client_secret_scope: builtins.str,
    container_name: builtins.str,
    initialize_file_system: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    mount_name: builtins.str,
    storage_account_name: builtins.str,
    tenant_id: builtins.str,
    cluster_id: typing.Optional[builtins.str] = None,
    directory: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__b7a3fbcbb41f154c79134612b853ac88d72a032739b223afa1b386debbadf235(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e998337694544fa9d7adb20ab864008ab527ec434993a5eb0a3783e02263b1e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e543e57d1e4c0f24acd13f38b22123ebf8972680490308b1e7a9fa67b939ae65(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4544df404ce7379b695c777779439e4784f24729ef8c55702ccda5595773b774(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cad2adeb75100568be39286f8b6f0fe027e37005e7a086b6264a60a265cc9b54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b92a2837f6911d31b4b6057024d286140fe18ba945ca9c7d6e36c7dd3bcf61b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9fcdb2c6ebd550ee59f7e30b82add4dabde8c1b9a6feafd5c6d96063d0926b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27f5ab3ce86b29cba1450fd88ec65da7ca17694b8392e1a1ff413dfbbc5b6b0e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08f8001241f88e8fa3ad8233e7b74bd3492b0134074af526ba7920aa7618618f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff51020a00b59aebb11c698c86585b1a1c78e33043c15b84eea7243dbf1bd78f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5d256b7eb039398e49f8e1f28a7987ffe707acc57c6eb3a1e7cfe4d92728b4b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9e020dc77f167c93fc538c479ad616cc829fe30289d63ffba33c1d4684de0cb(
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
    container_name: builtins.str,
    initialize_file_system: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    mount_name: builtins.str,
    storage_account_name: builtins.str,
    tenant_id: builtins.str,
    cluster_id: typing.Optional[builtins.str] = None,
    directory: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
