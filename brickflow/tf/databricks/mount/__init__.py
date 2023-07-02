'''
# `databricks_mount`

Refer to the Terraform Registory for docs: [`databricks_mount`](https://www.terraform.io/docs/providers/databricks/r/mount).
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


class Mount(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mount.Mount",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/mount databricks_mount}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        abfs: typing.Optional[typing.Union["MountAbfs", typing.Dict[builtins.str, typing.Any]]] = None,
        adl: typing.Optional[typing.Union["MountAdl", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        encryption_type: typing.Optional[builtins.str] = None,
        extra_configs: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        gs: typing.Optional[typing.Union["MountGs", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        resource_id: typing.Optional[builtins.str] = None,
        s3: typing.Optional[typing.Union["MountS3", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["MountTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        uri: typing.Optional[builtins.str] = None,
        wasb: typing.Optional[typing.Union["MountWasb", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/mount databricks_mount} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param abfs: abfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#abfs Mount#abfs}
        :param adl: adl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#adl Mount#adl}
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#cluster_id Mount#cluster_id}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#encryption_type Mount#encryption_type}.
        :param extra_configs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#extra_configs Mount#extra_configs}.
        :param gs: gs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#gs Mount#gs}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#id Mount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#name Mount#name}.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#resource_id Mount#resource_id}.
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#s3 Mount#s3}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#timeouts Mount#timeouts}
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#uri Mount#uri}.
        :param wasb: wasb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#wasb Mount#wasb}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2439555499708318116951f69169d275c77e700790c18c929f2555910203d9ba)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MountConfig(
            abfs=abfs,
            adl=adl,
            cluster_id=cluster_id,
            encryption_type=encryption_type,
            extra_configs=extra_configs,
            gs=gs,
            id=id,
            name=name,
            resource_id=resource_id,
            s3=s3,
            timeouts=timeouts,
            uri=uri,
            wasb=wasb,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAbfs")
    def put_abfs(
        self,
        *,
        client_id: builtins.str,
        client_secret_key: builtins.str,
        client_secret_scope: builtins.str,
        initialize_file_system: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        container_name: typing.Optional[builtins.str] = None,
        directory: typing.Optional[builtins.str] = None,
        storage_account_name: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_id Mount#client_id}.
        :param client_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_key Mount#client_secret_key}.
        :param client_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_scope Mount#client_secret_scope}.
        :param initialize_file_system: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#initialize_file_system Mount#initialize_file_system}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#container_name Mount#container_name}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_account_name Mount#storage_account_name}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#tenant_id Mount#tenant_id}.
        '''
        value = MountAbfs(
            client_id=client_id,
            client_secret_key=client_secret_key,
            client_secret_scope=client_secret_scope,
            initialize_file_system=initialize_file_system,
            container_name=container_name,
            directory=directory,
            storage_account_name=storage_account_name,
            tenant_id=tenant_id,
        )

        return typing.cast(None, jsii.invoke(self, "putAbfs", [value]))

    @jsii.member(jsii_name="putAdl")
    def put_adl(
        self,
        *,
        client_id: builtins.str,
        client_secret_key: builtins.str,
        client_secret_scope: builtins.str,
        directory: typing.Optional[builtins.str] = None,
        spark_conf_prefix: typing.Optional[builtins.str] = None,
        storage_resource_name: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_id Mount#client_id}.
        :param client_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_key Mount#client_secret_key}.
        :param client_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_scope Mount#client_secret_scope}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.
        :param spark_conf_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#spark_conf_prefix Mount#spark_conf_prefix}.
        :param storage_resource_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_resource_name Mount#storage_resource_name}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#tenant_id Mount#tenant_id}.
        '''
        value = MountAdl(
            client_id=client_id,
            client_secret_key=client_secret_key,
            client_secret_scope=client_secret_scope,
            directory=directory,
            spark_conf_prefix=spark_conf_prefix,
            storage_resource_name=storage_resource_name,
            tenant_id=tenant_id,
        )

        return typing.cast(None, jsii.invoke(self, "putAdl", [value]))

    @jsii.member(jsii_name="putGs")
    def put_gs(
        self,
        *,
        bucket_name: builtins.str,
        service_account: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#bucket_name Mount#bucket_name}.
        :param service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#service_account Mount#service_account}.
        '''
        value = MountGs(bucket_name=bucket_name, service_account=service_account)

        return typing.cast(None, jsii.invoke(self, "putGs", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        bucket_name: builtins.str,
        instance_profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#bucket_name Mount#bucket_name}.
        :param instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#instance_profile Mount#instance_profile}.
        '''
        value = MountS3(bucket_name=bucket_name, instance_profile=instance_profile)

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#default Mount#default}.
        '''
        value = MountTimeouts(default=default)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWasb")
    def put_wasb(
        self,
        *,
        auth_type: builtins.str,
        token_secret_key: builtins.str,
        token_secret_scope: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        directory: typing.Optional[builtins.str] = None,
        storage_account_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#auth_type Mount#auth_type}.
        :param token_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#token_secret_key Mount#token_secret_key}.
        :param token_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#token_secret_scope Mount#token_secret_scope}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#container_name Mount#container_name}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_account_name Mount#storage_account_name}.
        '''
        value = MountWasb(
            auth_type=auth_type,
            token_secret_key=token_secret_key,
            token_secret_scope=token_secret_scope,
            container_name=container_name,
            directory=directory,
            storage_account_name=storage_account_name,
        )

        return typing.cast(None, jsii.invoke(self, "putWasb", [value]))

    @jsii.member(jsii_name="resetAbfs")
    def reset_abfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAbfs", []))

    @jsii.member(jsii_name="resetAdl")
    def reset_adl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdl", []))

    @jsii.member(jsii_name="resetClusterId")
    def reset_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterId", []))

    @jsii.member(jsii_name="resetEncryptionType")
    def reset_encryption_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionType", []))

    @jsii.member(jsii_name="resetExtraConfigs")
    def reset_extra_configs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraConfigs", []))

    @jsii.member(jsii_name="resetGs")
    def reset_gs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGs", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetResourceId")
    def reset_resource_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceId", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUri")
    def reset_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUri", []))

    @jsii.member(jsii_name="resetWasb")
    def reset_wasb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWasb", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="abfs")
    def abfs(self) -> "MountAbfsOutputReference":
        return typing.cast("MountAbfsOutputReference", jsii.get(self, "abfs"))

    @builtins.property
    @jsii.member(jsii_name="adl")
    def adl(self) -> "MountAdlOutputReference":
        return typing.cast("MountAdlOutputReference", jsii.get(self, "adl"))

    @builtins.property
    @jsii.member(jsii_name="gs")
    def gs(self) -> "MountGsOutputReference":
        return typing.cast("MountGsOutputReference", jsii.get(self, "gs"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "MountS3OutputReference":
        return typing.cast("MountS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MountTimeoutsOutputReference":
        return typing.cast("MountTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="wasb")
    def wasb(self) -> "MountWasbOutputReference":
        return typing.cast("MountWasbOutputReference", jsii.get(self, "wasb"))

    @builtins.property
    @jsii.member(jsii_name="abfsInput")
    def abfs_input(self) -> typing.Optional["MountAbfs"]:
        return typing.cast(typing.Optional["MountAbfs"], jsii.get(self, "abfsInput"))

    @builtins.property
    @jsii.member(jsii_name="adlInput")
    def adl_input(self) -> typing.Optional["MountAdl"]:
        return typing.cast(typing.Optional["MountAdl"], jsii.get(self, "adlInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionTypeInput")
    def encryption_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="extraConfigsInput")
    def extra_configs_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "extraConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="gsInput")
    def gs_input(self) -> typing.Optional["MountGs"]:
        return typing.cast(typing.Optional["MountGs"], jsii.get(self, "gsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceIdInput")
    def resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(self) -> typing.Optional["MountS3"]:
        return typing.cast(typing.Optional["MountS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MountTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MountTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="wasbInput")
    def wasb_input(self) -> typing.Optional["MountWasb"]:
        return typing.cast(typing.Optional["MountWasb"], jsii.get(self, "wasbInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__014eb78db2c5c4a674601be66c9104f419632f002374bf6f6668bfc092ee28dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionType")
    def encryption_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionType"))

    @encryption_type.setter
    def encryption_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3adb05c4e2e62dc888d6cb1cf427d0975a060e3721e2bb3474b8efe82fbe2bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="extraConfigs")
    def extra_configs(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "extraConfigs"))

    @extra_configs.setter
    def extra_configs(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1b66e56098ef836f16c532329cdf0c0493368fdcfe4e6bfc1c9d334a88970d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extraConfigs", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bf8e6d25ed9b1826c9eff102ee061a8a2fe968e80aca47e9f7e17bbbff4fb3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae1a7c936a4f8328d0fd641594cac2022c5ab94d11d343905a94385a54811d91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f7493171ca2cd4e71864353117a1642ade955cf822305a3cf11a9f18113b2e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55d370a81a5f1083128bce0415d296bba3bc1eadeeb74119c6a8ab3182658026)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)


@jsii.data_type(
    jsii_type="databricks.mount.MountAbfs",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret_key": "clientSecretKey",
        "client_secret_scope": "clientSecretScope",
        "initialize_file_system": "initializeFileSystem",
        "container_name": "containerName",
        "directory": "directory",
        "storage_account_name": "storageAccountName",
        "tenant_id": "tenantId",
    },
)
class MountAbfs:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret_key: builtins.str,
        client_secret_scope: builtins.str,
        initialize_file_system: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        container_name: typing.Optional[builtins.str] = None,
        directory: typing.Optional[builtins.str] = None,
        storage_account_name: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_id Mount#client_id}.
        :param client_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_key Mount#client_secret_key}.
        :param client_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_scope Mount#client_secret_scope}.
        :param initialize_file_system: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#initialize_file_system Mount#initialize_file_system}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#container_name Mount#container_name}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_account_name Mount#storage_account_name}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#tenant_id Mount#tenant_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f84003f14ada26fd1e1b880f36199ae29c5e11c0f2c73efe7fb044feba3e9bf3)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret_key", value=client_secret_key, expected_type=type_hints["client_secret_key"])
            check_type(argname="argument client_secret_scope", value=client_secret_scope, expected_type=type_hints["client_secret_scope"])
            check_type(argname="argument initialize_file_system", value=initialize_file_system, expected_type=type_hints["initialize_file_system"])
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
            check_type(argname="argument storage_account_name", value=storage_account_name, expected_type=type_hints["storage_account_name"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "client_secret_key": client_secret_key,
            "client_secret_scope": client_secret_scope,
            "initialize_file_system": initialize_file_system,
        }
        if container_name is not None:
            self._values["container_name"] = container_name
        if directory is not None:
            self._values["directory"] = directory
        if storage_account_name is not None:
            self._values["storage_account_name"] = storage_account_name
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_id Mount#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_key Mount#client_secret_key}.'''
        result = self._values.get("client_secret_key")
        assert result is not None, "Required property 'client_secret_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_scope Mount#client_secret_scope}.'''
        result = self._values.get("client_secret_scope")
        assert result is not None, "Required property 'client_secret_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def initialize_file_system(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#initialize_file_system Mount#initialize_file_system}.'''
        result = self._values.get("initialize_file_system")
        assert result is not None, "Required property 'initialize_file_system' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def container_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#container_name Mount#container_name}.'''
        result = self._values.get("container_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.'''
        result = self._values.get("directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_account_name Mount#storage_account_name}.'''
        result = self._values.get("storage_account_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#tenant_id Mount#tenant_id}.'''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountAbfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MountAbfsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mount.MountAbfsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8028fdfa1bd1045d860e75e233ca7e45a3800ac01666490edd82db471b9c6e10)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContainerName")
    def reset_container_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerName", []))

    @jsii.member(jsii_name="resetDirectory")
    def reset_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectory", []))

    @jsii.member(jsii_name="resetStorageAccountName")
    def reset_storage_account_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountName", []))

    @jsii.member(jsii_name="resetTenantId")
    def reset_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantId", []))

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
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryInput")
    def directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryInput"))

    @builtins.property
    @jsii.member(jsii_name="initializeFileSystemInput")
    def initialize_file_system_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "initializeFileSystemInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__3eb9be867946def2941b88d9e4b397c0433d745acd15049583b90eeff6995d52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretKey")
    def client_secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretKey"))

    @client_secret_key.setter
    def client_secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__491eb30281a52357d1ecc03df50ba639153c02216b9f90c1655edea1a5e0e281)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretKey", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretScope")
    def client_secret_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretScope"))

    @client_secret_scope.setter
    def client_secret_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73d7ffc5389242a6b7bc0b4e603e179f5d717797ca1860c086faac73d85aac2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretScope", value)

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90fb7e7e305cb404e4d46d180dea2d2af9dc9df31882d40de4012878d43e74b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="directory")
    def directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directory"))

    @directory.setter
    def directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddab2fabcd66269c1dbf4bad9e3daa05cba49cbf1dc4a4c4bae644dd6abf9633)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directory", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__1a052844c828dc9b02366299f880efd0f5e5943bbc1397b61aa9f693eac0b1d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initializeFileSystem", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountName")
    def storage_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountName"))

    @storage_account_name.setter
    def storage_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f42746c2f2ce54bcab509767ad28bb7b455bd39591faa3721ca254cec2f49c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da14049191bc2e992bfd1fd092200e43f0532f8b4c154fa7f9c57dac0af630f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MountAbfs]:
        return typing.cast(typing.Optional[MountAbfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MountAbfs]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__228f5bdcbed409fc5e19d5db58c31adabca9dc0d101bb0402fcec9d622340b44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.mount.MountAdl",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret_key": "clientSecretKey",
        "client_secret_scope": "clientSecretScope",
        "directory": "directory",
        "spark_conf_prefix": "sparkConfPrefix",
        "storage_resource_name": "storageResourceName",
        "tenant_id": "tenantId",
    },
)
class MountAdl:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret_key: builtins.str,
        client_secret_scope: builtins.str,
        directory: typing.Optional[builtins.str] = None,
        spark_conf_prefix: typing.Optional[builtins.str] = None,
        storage_resource_name: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_id Mount#client_id}.
        :param client_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_key Mount#client_secret_key}.
        :param client_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_scope Mount#client_secret_scope}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.
        :param spark_conf_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#spark_conf_prefix Mount#spark_conf_prefix}.
        :param storage_resource_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_resource_name Mount#storage_resource_name}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#tenant_id Mount#tenant_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d2dd15e6cd32c9d941afb76d17d000cbe12d5320737c094d8ca375e4a067c83)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret_key", value=client_secret_key, expected_type=type_hints["client_secret_key"])
            check_type(argname="argument client_secret_scope", value=client_secret_scope, expected_type=type_hints["client_secret_scope"])
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
            check_type(argname="argument spark_conf_prefix", value=spark_conf_prefix, expected_type=type_hints["spark_conf_prefix"])
            check_type(argname="argument storage_resource_name", value=storage_resource_name, expected_type=type_hints["storage_resource_name"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "client_secret_key": client_secret_key,
            "client_secret_scope": client_secret_scope,
        }
        if directory is not None:
            self._values["directory"] = directory
        if spark_conf_prefix is not None:
            self._values["spark_conf_prefix"] = spark_conf_prefix
        if storage_resource_name is not None:
            self._values["storage_resource_name"] = storage_resource_name
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_id Mount#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_key Mount#client_secret_key}.'''
        result = self._values.get("client_secret_key")
        assert result is not None, "Required property 'client_secret_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_scope Mount#client_secret_scope}.'''
        result = self._values.get("client_secret_scope")
        assert result is not None, "Required property 'client_secret_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def directory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.'''
        result = self._values.get("directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spark_conf_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#spark_conf_prefix Mount#spark_conf_prefix}.'''
        result = self._values.get("spark_conf_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_resource_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_resource_name Mount#storage_resource_name}.'''
        result = self._values.get("storage_resource_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#tenant_id Mount#tenant_id}.'''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountAdl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MountAdlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mount.MountAdlOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f4555265ac3b4a62d5c14f503959cd309856562a24d9ed4df38def9a1e3a8be)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDirectory")
    def reset_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectory", []))

    @jsii.member(jsii_name="resetSparkConfPrefix")
    def reset_spark_conf_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkConfPrefix", []))

    @jsii.member(jsii_name="resetStorageResourceName")
    def reset_storage_resource_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageResourceName", []))

    @jsii.member(jsii_name="resetTenantId")
    def reset_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantId", []))

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
    @jsii.member(jsii_name="directoryInput")
    def directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__0dd06285c55be460d4b72adec1e19c5aaf786745923336105a46d7c5b9171979)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretKey")
    def client_secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretKey"))

    @client_secret_key.setter
    def client_secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1140bef2a4e777c62de74b4fd2c434e5c3b3ffcb2e606d084271331cc89aeb5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretKey", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretScope")
    def client_secret_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretScope"))

    @client_secret_scope.setter
    def client_secret_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e99948cb3944a4d17c7afb1ff09e3bf1aa48ebd569df39d661b5278a18a95a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretScope", value)

    @builtins.property
    @jsii.member(jsii_name="directory")
    def directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directory"))

    @directory.setter
    def directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df621c227ca90a85b5e8c471e0247825b391abb521c2d95808e7ae4b7f5dc1dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directory", value)

    @builtins.property
    @jsii.member(jsii_name="sparkConfPrefix")
    def spark_conf_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sparkConfPrefix"))

    @spark_conf_prefix.setter
    def spark_conf_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37f017d42f0c6c7ef8087ee28c49b060ecce59e26049fe8462513073884bdb93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkConfPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="storageResourceName")
    def storage_resource_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageResourceName"))

    @storage_resource_name.setter
    def storage_resource_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7967aa76ff8ddd4882a189fec2127446faa475622cb362d74ec758384fcf42f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageResourceName", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7731fc4741aeb2bf02ef054db0ace741e71d9df995f40603878c89aeda0edbdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MountAdl]:
        return typing.cast(typing.Optional[MountAdl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MountAdl]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39c33c78617803fe9b3a5de504c13d4eb5bab48d1b522f160b7d8c1964be2761)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.mount.MountConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "abfs": "abfs",
        "adl": "adl",
        "cluster_id": "clusterId",
        "encryption_type": "encryptionType",
        "extra_configs": "extraConfigs",
        "gs": "gs",
        "id": "id",
        "name": "name",
        "resource_id": "resourceId",
        "s3": "s3",
        "timeouts": "timeouts",
        "uri": "uri",
        "wasb": "wasb",
    },
)
class MountConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        abfs: typing.Optional[typing.Union[MountAbfs, typing.Dict[builtins.str, typing.Any]]] = None,
        adl: typing.Optional[typing.Union[MountAdl, typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        encryption_type: typing.Optional[builtins.str] = None,
        extra_configs: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        gs: typing.Optional[typing.Union["MountGs", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        resource_id: typing.Optional[builtins.str] = None,
        s3: typing.Optional[typing.Union["MountS3", typing.Dict[builtins.str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["MountTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        uri: typing.Optional[builtins.str] = None,
        wasb: typing.Optional[typing.Union["MountWasb", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param abfs: abfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#abfs Mount#abfs}
        :param adl: adl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#adl Mount#adl}
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#cluster_id Mount#cluster_id}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#encryption_type Mount#encryption_type}.
        :param extra_configs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#extra_configs Mount#extra_configs}.
        :param gs: gs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#gs Mount#gs}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#id Mount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#name Mount#name}.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#resource_id Mount#resource_id}.
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#s3 Mount#s3}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#timeouts Mount#timeouts}
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#uri Mount#uri}.
        :param wasb: wasb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#wasb Mount#wasb}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(abfs, dict):
            abfs = MountAbfs(**abfs)
        if isinstance(adl, dict):
            adl = MountAdl(**adl)
        if isinstance(gs, dict):
            gs = MountGs(**gs)
        if isinstance(s3, dict):
            s3 = MountS3(**s3)
        if isinstance(timeouts, dict):
            timeouts = MountTimeouts(**timeouts)
        if isinstance(wasb, dict):
            wasb = MountWasb(**wasb)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aea21df40d7f4259bdbc8130c0427158da7d438ab37ac80c18edeec8b2f79506)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument abfs", value=abfs, expected_type=type_hints["abfs"])
            check_type(argname="argument adl", value=adl, expected_type=type_hints["adl"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
            check_type(argname="argument extra_configs", value=extra_configs, expected_type=type_hints["extra_configs"])
            check_type(argname="argument gs", value=gs, expected_type=type_hints["gs"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument wasb", value=wasb, expected_type=type_hints["wasb"])
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
        if abfs is not None:
            self._values["abfs"] = abfs
        if adl is not None:
            self._values["adl"] = adl
        if cluster_id is not None:
            self._values["cluster_id"] = cluster_id
        if encryption_type is not None:
            self._values["encryption_type"] = encryption_type
        if extra_configs is not None:
            self._values["extra_configs"] = extra_configs
        if gs is not None:
            self._values["gs"] = gs
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if resource_id is not None:
            self._values["resource_id"] = resource_id
        if s3 is not None:
            self._values["s3"] = s3
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if uri is not None:
            self._values["uri"] = uri
        if wasb is not None:
            self._values["wasb"] = wasb

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
    def abfs(self) -> typing.Optional[MountAbfs]:
        '''abfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#abfs Mount#abfs}
        '''
        result = self._values.get("abfs")
        return typing.cast(typing.Optional[MountAbfs], result)

    @builtins.property
    def adl(self) -> typing.Optional[MountAdl]:
        '''adl block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#adl Mount#adl}
        '''
        result = self._values.get("adl")
        return typing.cast(typing.Optional[MountAdl], result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#cluster_id Mount#cluster_id}.'''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#encryption_type Mount#encryption_type}.'''
        result = self._values.get("encryption_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extra_configs(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#extra_configs Mount#extra_configs}.'''
        result = self._values.get("extra_configs")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def gs(self) -> typing.Optional["MountGs"]:
        '''gs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#gs Mount#gs}
        '''
        result = self._values.get("gs")
        return typing.cast(typing.Optional["MountGs"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#id Mount#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#name Mount#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#resource_id Mount#resource_id}.'''
        result = self._values.get("resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3(self) -> typing.Optional["MountS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#s3 Mount#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["MountS3"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MountTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#timeouts Mount#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MountTimeouts"], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#uri Mount#uri}.'''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wasb(self) -> typing.Optional["MountWasb"]:
        '''wasb block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#wasb Mount#wasb}
        '''
        result = self._values.get("wasb")
        return typing.cast(typing.Optional["MountWasb"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.mount.MountGs",
    jsii_struct_bases=[],
    name_mapping={"bucket_name": "bucketName", "service_account": "serviceAccount"},
)
class MountGs:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        service_account: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#bucket_name Mount#bucket_name}.
        :param service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#service_account Mount#service_account}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2207919cdcb48eaf17e326ae32f5a3d5b64b373882a543c62160c00fc569f08a)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if service_account is not None:
            self._values["service_account"] = service_account

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#bucket_name Mount#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#service_account Mount#service_account}.'''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountGs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MountGsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mount.MountGsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__900e3eceaea6703b6ed008ad15a5e01f8abc5a2f087d49ebe0ab2e993802053f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetServiceAccount")
    def reset_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccount", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountInput")
    def service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e29d1a26b8cd6c278e9e1afc43db620acc2d1cf604380ea7c66e40e03f6528db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccount"))

    @service_account.setter
    def service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c3051eb1de0d52656cc7ab1f193362e4f63707215348bb5afaf5bde6b7c38c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MountGs]:
        return typing.cast(typing.Optional[MountGs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MountGs]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__226725e835ffee44ad93acdecbdeebad0664e3d2173e423d6cc09f7535792747)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.mount.MountS3",
    jsii_struct_bases=[],
    name_mapping={"bucket_name": "bucketName", "instance_profile": "instanceProfile"},
)
class MountS3:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        instance_profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#bucket_name Mount#bucket_name}.
        :param instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#instance_profile Mount#instance_profile}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4602237fa82742902bc760b25f2f16f0d4a8fed6f467c0218dd92a12324af44f)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument instance_profile", value=instance_profile, expected_type=type_hints["instance_profile"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if instance_profile is not None:
            self._values["instance_profile"] = instance_profile

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#bucket_name Mount#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_profile(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#instance_profile Mount#instance_profile}.'''
        result = self._values.get("instance_profile")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MountS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mount.MountS3OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb98b436dc6f30780e9d3dcd65bec55abf01b745b7f3d0f1bd39df633dd57221)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceProfile")
    def reset_instance_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceProfile", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceProfileInput")
    def instance_profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__760860f00399b847cdb5b7214f98ecfe95e15680d94c4ceb4bf15cec22c36e1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfile")
    def instance_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceProfile"))

    @instance_profile.setter
    def instance_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84e3769484cf4d95cd808da0af1f8d87daded2557f29df363103c64b148b775e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfile", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MountS3]:
        return typing.cast(typing.Optional[MountS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MountS3]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1228c37866665a645905b9556feafe0a6adb507fac92074c642b98ee56d82493)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.mount.MountTimeouts",
    jsii_struct_bases=[],
    name_mapping={"default": "default"},
)
class MountTimeouts:
    def __init__(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#default Mount#default}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ce8a1f5c3d64b99e0aaa1748044bd9c40e12de0689f1b6ebb77425f88f9d55b)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#default Mount#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MountTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mount.MountTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__68d8eef321dadfe46706918699e9b3e6bd085efb545150d620cf4f2736f3e980)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c43a48a36a554308ecde2bc0def22dc0b2d76e852e2e82132f2c3741cc44a80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MountTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MountTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MountTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__594425854892ee399017f42536ee9f963d238273bfa0da85eb65db5f13637397)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.mount.MountWasb",
    jsii_struct_bases=[],
    name_mapping={
        "auth_type": "authType",
        "token_secret_key": "tokenSecretKey",
        "token_secret_scope": "tokenSecretScope",
        "container_name": "containerName",
        "directory": "directory",
        "storage_account_name": "storageAccountName",
    },
)
class MountWasb:
    def __init__(
        self,
        *,
        auth_type: builtins.str,
        token_secret_key: builtins.str,
        token_secret_scope: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        directory: typing.Optional[builtins.str] = None,
        storage_account_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#auth_type Mount#auth_type}.
        :param token_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#token_secret_key Mount#token_secret_key}.
        :param token_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#token_secret_scope Mount#token_secret_scope}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#container_name Mount#container_name}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_account_name Mount#storage_account_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04393dbf8f8d5426d529c0f6a17fe9f585066a6c59d17492ee4ebebaef00057c)
            check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
            check_type(argname="argument token_secret_key", value=token_secret_key, expected_type=type_hints["token_secret_key"])
            check_type(argname="argument token_secret_scope", value=token_secret_scope, expected_type=type_hints["token_secret_scope"])
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
            check_type(argname="argument storage_account_name", value=storage_account_name, expected_type=type_hints["storage_account_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auth_type": auth_type,
            "token_secret_key": token_secret_key,
            "token_secret_scope": token_secret_scope,
        }
        if container_name is not None:
            self._values["container_name"] = container_name
        if directory is not None:
            self._values["directory"] = directory
        if storage_account_name is not None:
            self._values["storage_account_name"] = storage_account_name

    @builtins.property
    def auth_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#auth_type Mount#auth_type}.'''
        result = self._values.get("auth_type")
        assert result is not None, "Required property 'auth_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token_secret_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#token_secret_key Mount#token_secret_key}.'''
        result = self._values.get("token_secret_key")
        assert result is not None, "Required property 'token_secret_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token_secret_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#token_secret_scope Mount#token_secret_scope}.'''
        result = self._values.get("token_secret_scope")
        assert result is not None, "Required property 'token_secret_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#container_name Mount#container_name}.'''
        result = self._values.get("container_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.'''
        result = self._values.get("directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_account_name Mount#storage_account_name}.'''
        result = self._values.get("storage_account_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountWasb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MountWasbOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mount.MountWasbOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__98bd20d7504113aad82a52184b56b4f3a518ed8da280c18003cc2ab61a924b8b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContainerName")
    def reset_container_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerName", []))

    @jsii.member(jsii_name="resetDirectory")
    def reset_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectory", []))

    @jsii.member(jsii_name="resetStorageAccountName")
    def reset_storage_account_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountName", []))

    @builtins.property
    @jsii.member(jsii_name="authTypeInput")
    def auth_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryInput")
    def directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__9b3add4bcad2758823d890d50a31556f5bc4efb01f8788d3c0b8ab530b35bc18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authType", value)

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cebe803e15aad3ba2006afd103429a289511d990dde6a91a3c59904df652af4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="directory")
    def directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directory"))

    @directory.setter
    def directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce65031eb1cc5121e6e915a99d3cf44364a30d226ffa6cc7b263e0815b5b1f32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directory", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountName")
    def storage_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountName"))

    @storage_account_name.setter
    def storage_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60e4cf3f0f9797bebf25c44c7ce1adee3cc9fa9a731af5c9a210f288e56160de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="tokenSecretKey")
    def token_secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenSecretKey"))

    @token_secret_key.setter
    def token_secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cbcc6a7bbda8381f6ca189977e44775776e61c93be139e3b21e49632fc1c1c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenSecretKey", value)

    @builtins.property
    @jsii.member(jsii_name="tokenSecretScope")
    def token_secret_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenSecretScope"))

    @token_secret_scope.setter
    def token_secret_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__515c07306d18c61935c9cb69920bd1b7a077e72f4098c30ff392fb7d62b2c591)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenSecretScope", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MountWasb]:
        return typing.cast(typing.Optional[MountWasb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MountWasb]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b23269409afa972735934025db3c0ca61ac7582cd01d4e79ddc0db03d6b80cec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Mount",
    "MountAbfs",
    "MountAbfsOutputReference",
    "MountAdl",
    "MountAdlOutputReference",
    "MountConfig",
    "MountGs",
    "MountGsOutputReference",
    "MountS3",
    "MountS3OutputReference",
    "MountTimeouts",
    "MountTimeoutsOutputReference",
    "MountWasb",
    "MountWasbOutputReference",
]

publication.publish()

def _typecheckingstub__2439555499708318116951f69169d275c77e700790c18c929f2555910203d9ba(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    abfs: typing.Optional[typing.Union[MountAbfs, typing.Dict[builtins.str, typing.Any]]] = None,
    adl: typing.Optional[typing.Union[MountAdl, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_id: typing.Optional[builtins.str] = None,
    encryption_type: typing.Optional[builtins.str] = None,
    extra_configs: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    gs: typing.Optional[typing.Union[MountGs, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    resource_id: typing.Optional[builtins.str] = None,
    s3: typing.Optional[typing.Union[MountS3, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[MountTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    uri: typing.Optional[builtins.str] = None,
    wasb: typing.Optional[typing.Union[MountWasb, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__014eb78db2c5c4a674601be66c9104f419632f002374bf6f6668bfc092ee28dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3adb05c4e2e62dc888d6cb1cf427d0975a060e3721e2bb3474b8efe82fbe2bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1b66e56098ef836f16c532329cdf0c0493368fdcfe4e6bfc1c9d334a88970d2(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bf8e6d25ed9b1826c9eff102ee061a8a2fe968e80aca47e9f7e17bbbff4fb3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae1a7c936a4f8328d0fd641594cac2022c5ab94d11d343905a94385a54811d91(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f7493171ca2cd4e71864353117a1642ade955cf822305a3cf11a9f18113b2e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55d370a81a5f1083128bce0415d296bba3bc1eadeeb74119c6a8ab3182658026(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f84003f14ada26fd1e1b880f36199ae29c5e11c0f2c73efe7fb044feba3e9bf3(
    *,
    client_id: builtins.str,
    client_secret_key: builtins.str,
    client_secret_scope: builtins.str,
    initialize_file_system: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    container_name: typing.Optional[builtins.str] = None,
    directory: typing.Optional[builtins.str] = None,
    storage_account_name: typing.Optional[builtins.str] = None,
    tenant_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8028fdfa1bd1045d860e75e233ca7e45a3800ac01666490edd82db471b9c6e10(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3eb9be867946def2941b88d9e4b397c0433d745acd15049583b90eeff6995d52(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__491eb30281a52357d1ecc03df50ba639153c02216b9f90c1655edea1a5e0e281(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73d7ffc5389242a6b7bc0b4e603e179f5d717797ca1860c086faac73d85aac2e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90fb7e7e305cb404e4d46d180dea2d2af9dc9df31882d40de4012878d43e74b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddab2fabcd66269c1dbf4bad9e3daa05cba49cbf1dc4a4c4bae644dd6abf9633(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a052844c828dc9b02366299f880efd0f5e5943bbc1397b61aa9f693eac0b1d5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f42746c2f2ce54bcab509767ad28bb7b455bd39591faa3721ca254cec2f49c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da14049191bc2e992bfd1fd092200e43f0532f8b4c154fa7f9c57dac0af630f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__228f5bdcbed409fc5e19d5db58c31adabca9dc0d101bb0402fcec9d622340b44(
    value: typing.Optional[MountAbfs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d2dd15e6cd32c9d941afb76d17d000cbe12d5320737c094d8ca375e4a067c83(
    *,
    client_id: builtins.str,
    client_secret_key: builtins.str,
    client_secret_scope: builtins.str,
    directory: typing.Optional[builtins.str] = None,
    spark_conf_prefix: typing.Optional[builtins.str] = None,
    storage_resource_name: typing.Optional[builtins.str] = None,
    tenant_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4555265ac3b4a62d5c14f503959cd309856562a24d9ed4df38def9a1e3a8be(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dd06285c55be460d4b72adec1e19c5aaf786745923336105a46d7c5b9171979(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1140bef2a4e777c62de74b4fd2c434e5c3b3ffcb2e606d084271331cc89aeb5c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e99948cb3944a4d17c7afb1ff09e3bf1aa48ebd569df39d661b5278a18a95a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df621c227ca90a85b5e8c471e0247825b391abb521c2d95808e7ae4b7f5dc1dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37f017d42f0c6c7ef8087ee28c49b060ecce59e26049fe8462513073884bdb93(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7967aa76ff8ddd4882a189fec2127446faa475622cb362d74ec758384fcf42f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7731fc4741aeb2bf02ef054db0ace741e71d9df995f40603878c89aeda0edbdc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39c33c78617803fe9b3a5de504c13d4eb5bab48d1b522f160b7d8c1964be2761(
    value: typing.Optional[MountAdl],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aea21df40d7f4259bdbc8130c0427158da7d438ab37ac80c18edeec8b2f79506(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    abfs: typing.Optional[typing.Union[MountAbfs, typing.Dict[builtins.str, typing.Any]]] = None,
    adl: typing.Optional[typing.Union[MountAdl, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_id: typing.Optional[builtins.str] = None,
    encryption_type: typing.Optional[builtins.str] = None,
    extra_configs: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    gs: typing.Optional[typing.Union[MountGs, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    resource_id: typing.Optional[builtins.str] = None,
    s3: typing.Optional[typing.Union[MountS3, typing.Dict[builtins.str, typing.Any]]] = None,
    timeouts: typing.Optional[typing.Union[MountTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    uri: typing.Optional[builtins.str] = None,
    wasb: typing.Optional[typing.Union[MountWasb, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2207919cdcb48eaf17e326ae32f5a3d5b64b373882a543c62160c00fc569f08a(
    *,
    bucket_name: builtins.str,
    service_account: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__900e3eceaea6703b6ed008ad15a5e01f8abc5a2f087d49ebe0ab2e993802053f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e29d1a26b8cd6c278e9e1afc43db620acc2d1cf604380ea7c66e40e03f6528db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c3051eb1de0d52656cc7ab1f193362e4f63707215348bb5afaf5bde6b7c38c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__226725e835ffee44ad93acdecbdeebad0664e3d2173e423d6cc09f7535792747(
    value: typing.Optional[MountGs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4602237fa82742902bc760b25f2f16f0d4a8fed6f467c0218dd92a12324af44f(
    *,
    bucket_name: builtins.str,
    instance_profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb98b436dc6f30780e9d3dcd65bec55abf01b745b7f3d0f1bd39df633dd57221(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__760860f00399b847cdb5b7214f98ecfe95e15680d94c4ceb4bf15cec22c36e1d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84e3769484cf4d95cd808da0af1f8d87daded2557f29df363103c64b148b775e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1228c37866665a645905b9556feafe0a6adb507fac92074c642b98ee56d82493(
    value: typing.Optional[MountS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ce8a1f5c3d64b99e0aaa1748044bd9c40e12de0689f1b6ebb77425f88f9d55b(
    *,
    default: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68d8eef321dadfe46706918699e9b3e6bd085efb545150d620cf4f2736f3e980(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c43a48a36a554308ecde2bc0def22dc0b2d76e852e2e82132f2c3741cc44a80(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__594425854892ee399017f42536ee9f963d238273bfa0da85eb65db5f13637397(
    value: typing.Optional[typing.Union[MountTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04393dbf8f8d5426d529c0f6a17fe9f585066a6c59d17492ee4ebebaef00057c(
    *,
    auth_type: builtins.str,
    token_secret_key: builtins.str,
    token_secret_scope: builtins.str,
    container_name: typing.Optional[builtins.str] = None,
    directory: typing.Optional[builtins.str] = None,
    storage_account_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98bd20d7504113aad82a52184b56b4f3a518ed8da280c18003cc2ab61a924b8b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b3add4bcad2758823d890d50a31556f5bc4efb01f8788d3c0b8ab530b35bc18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cebe803e15aad3ba2006afd103429a289511d990dde6a91a3c59904df652af4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce65031eb1cc5121e6e915a99d3cf44364a30d226ffa6cc7b263e0815b5b1f32(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60e4cf3f0f9797bebf25c44c7ce1adee3cc9fa9a731af5c9a210f288e56160de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cbcc6a7bbda8381f6ca189977e44775776e61c93be139e3b21e49632fc1c1c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__515c07306d18c61935c9cb69920bd1b7a077e72f4098c30ff392fb7d62b2c591(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b23269409afa972735934025db3c0ca61ac7582cd01d4e79ddc0db03d6b80cec(
    value: typing.Optional[MountWasb],
) -> None:
    """Type checking stubs"""
    pass
