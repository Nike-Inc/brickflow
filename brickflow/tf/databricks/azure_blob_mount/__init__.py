'''
# `databricks_azure_blob_mount`

Refer to the Terraform Registory for docs: [`databricks_azure_blob_mount`](https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount).
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


class AzureBlobMount(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.azureBlobMount.AzureBlobMount",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount databricks_azure_blob_mount}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        auth_type: builtins.str,
        container_name: builtins.str,
        mount_name: builtins.str,
        storage_account_name: builtins.str,
        token_secret_key: builtins.str,
        token_secret_scope: builtins.str,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount databricks_azure_blob_mount} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#auth_type AzureBlobMount#auth_type}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#container_name AzureBlobMount#container_name}.
        :param mount_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#mount_name AzureBlobMount#mount_name}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#storage_account_name AzureBlobMount#storage_account_name}.
        :param token_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#token_secret_key AzureBlobMount#token_secret_key}.
        :param token_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#token_secret_scope AzureBlobMount#token_secret_scope}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#cluster_id AzureBlobMount#cluster_id}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#directory AzureBlobMount#directory}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#id AzureBlobMount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04fdc78e99155387e79742cc6079b7d254071bbb76008bb2fcac7a5580f09dbf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AzureBlobMountConfig(
            auth_type=auth_type,
            container_name=container_name,
            mount_name=mount_name,
            storage_account_name=storage_account_name,
            token_secret_key=token_secret_key,
            token_secret_scope=token_secret_scope,
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
    @jsii.member(jsii_name="authTypeInput")
    def auth_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTypeInput"))

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
    @jsii.member(jsii_name="mountNameInput")
    def mount_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountNameInput")
    def storage_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenSecretKeyInput")
    def token_secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenSecretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenSecretScopeInput")
    def token_secret_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenSecretScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authType"))

    @auth_type.setter
    def auth_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6d5f188607600a311a9f7273e0e364eca522c99e3490e1e1a57f758963d1d6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authType", value)

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca8951ea475607b60eff61038a5b5ee08bd2f868366150338ef00a7d0fb83db8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91fb010388e0258530a6b60d27b3d97dede5521a1bd3fa9fd286c3459c6a08c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="directory")
    def directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directory"))

    @directory.setter
    def directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ac6bde53baffea928be80fa91e0aff66e4f92405683511828baeba48a0a3891)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directory", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e3f3e4f5747ab3d3712f8fe8fa3a0215c18010ce4b5dc2a71c829fd81211e05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mountName")
    def mount_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountName"))

    @mount_name.setter
    def mount_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8107b668b2a92657b49a12810a83e0f24fb343eb172d050f1b1c986f2dcd46ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountName", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountName")
    def storage_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountName"))

    @storage_account_name.setter
    def storage_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbab1703b4b65d3bf3e71eb83ba96a4269ed4727e981e2f91a134e612d134da2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="tokenSecretKey")
    def token_secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenSecretKey"))

    @token_secret_key.setter
    def token_secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bfc8aac9610df77279d78fbc02f9c20421124427da7e1b573a7a4ea68907b2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenSecretKey", value)

    @builtins.property
    @jsii.member(jsii_name="tokenSecretScope")
    def token_secret_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenSecretScope"))

    @token_secret_scope.setter
    def token_secret_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7af65eb666502bb7b4090bc8a9ed8b2f34120d464e60495d00dd80cd09713eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenSecretScope", value)


@jsii.data_type(
    jsii_type="databricks.azureBlobMount.AzureBlobMountConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "auth_type": "authType",
        "container_name": "containerName",
        "mount_name": "mountName",
        "storage_account_name": "storageAccountName",
        "token_secret_key": "tokenSecretKey",
        "token_secret_scope": "tokenSecretScope",
        "cluster_id": "clusterId",
        "directory": "directory",
        "id": "id",
    },
)
class AzureBlobMountConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        auth_type: builtins.str,
        container_name: builtins.str,
        mount_name: builtins.str,
        storage_account_name: builtins.str,
        token_secret_key: builtins.str,
        token_secret_scope: builtins.str,
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
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#auth_type AzureBlobMount#auth_type}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#container_name AzureBlobMount#container_name}.
        :param mount_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#mount_name AzureBlobMount#mount_name}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#storage_account_name AzureBlobMount#storage_account_name}.
        :param token_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#token_secret_key AzureBlobMount#token_secret_key}.
        :param token_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#token_secret_scope AzureBlobMount#token_secret_scope}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#cluster_id AzureBlobMount#cluster_id}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#directory AzureBlobMount#directory}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#id AzureBlobMount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3c39cd05aeb3da18f594d3ba1e39310f4e51310fdf7d057955a922b1c4a8462)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument mount_name", value=mount_name, expected_type=type_hints["mount_name"])
            check_type(argname="argument storage_account_name", value=storage_account_name, expected_type=type_hints["storage_account_name"])
            check_type(argname="argument token_secret_key", value=token_secret_key, expected_type=type_hints["token_secret_key"])
            check_type(argname="argument token_secret_scope", value=token_secret_scope, expected_type=type_hints["token_secret_scope"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auth_type": auth_type,
            "container_name": container_name,
            "mount_name": mount_name,
            "storage_account_name": storage_account_name,
            "token_secret_key": token_secret_key,
            "token_secret_scope": token_secret_scope,
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
    def auth_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#auth_type AzureBlobMount#auth_type}.'''
        result = self._values.get("auth_type")
        assert result is not None, "Required property 'auth_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#container_name AzureBlobMount#container_name}.'''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mount_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#mount_name AzureBlobMount#mount_name}.'''
        result = self._values.get("mount_name")
        assert result is not None, "Required property 'mount_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#storage_account_name AzureBlobMount#storage_account_name}.'''
        result = self._values.get("storage_account_name")
        assert result is not None, "Required property 'storage_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token_secret_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#token_secret_key AzureBlobMount#token_secret_key}.'''
        result = self._values.get("token_secret_key")
        assert result is not None, "Required property 'token_secret_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token_secret_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#token_secret_scope AzureBlobMount#token_secret_scope}.'''
        result = self._values.get("token_secret_scope")
        assert result is not None, "Required property 'token_secret_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#cluster_id AzureBlobMount#cluster_id}.'''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#directory AzureBlobMount#directory}.'''
        result = self._values.get("directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/azure_blob_mount#id AzureBlobMount#id}.

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
        return "AzureBlobMountConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AzureBlobMount",
    "AzureBlobMountConfig",
]

publication.publish()

def _typecheckingstub__04fdc78e99155387e79742cc6079b7d254071bbb76008bb2fcac7a5580f09dbf(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    auth_type: builtins.str,
    container_name: builtins.str,
    mount_name: builtins.str,
    storage_account_name: builtins.str,
    token_secret_key: builtins.str,
    token_secret_scope: builtins.str,
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

def _typecheckingstub__f6d5f188607600a311a9f7273e0e364eca522c99e3490e1e1a57f758963d1d6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca8951ea475607b60eff61038a5b5ee08bd2f868366150338ef00a7d0fb83db8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91fb010388e0258530a6b60d27b3d97dede5521a1bd3fa9fd286c3459c6a08c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ac6bde53baffea928be80fa91e0aff66e4f92405683511828baeba48a0a3891(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e3f3e4f5747ab3d3712f8fe8fa3a0215c18010ce4b5dc2a71c829fd81211e05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8107b668b2a92657b49a12810a83e0f24fb343eb172d050f1b1c986f2dcd46ba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbab1703b4b65d3bf3e71eb83ba96a4269ed4727e981e2f91a134e612d134da2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bfc8aac9610df77279d78fbc02f9c20421124427da7e1b573a7a4ea68907b2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7af65eb666502bb7b4090bc8a9ed8b2f34120d464e60495d00dd80cd09713eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3c39cd05aeb3da18f594d3ba1e39310f4e51310fdf7d057955a922b1c4a8462(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    auth_type: builtins.str,
    container_name: builtins.str,
    mount_name: builtins.str,
    storage_account_name: builtins.str,
    token_secret_key: builtins.str,
    token_secret_scope: builtins.str,
    cluster_id: typing.Optional[builtins.str] = None,
    directory: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
