'''
# `databricks_metastore`

Refer to the Terraform Registory for docs: [`databricks_metastore`](https://www.terraform.io/docs/providers/databricks/r/metastore).
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


class Metastore(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.metastore.Metastore",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/metastore databricks_metastore}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        storage_root: builtins.str,
        cloud: typing.Optional[builtins.str] = None,
        created_at: typing.Optional[jsii.Number] = None,
        created_by: typing.Optional[builtins.str] = None,
        default_data_access_config_id: typing.Optional[builtins.str] = None,
        delta_sharing_organization_name: typing.Optional[builtins.str] = None,
        delta_sharing_recipient_token_lifetime_in_seconds: typing.Optional[jsii.Number] = None,
        delta_sharing_scope: typing.Optional[builtins.str] = None,
        force_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        global_metastore_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        updated_at: typing.Optional[jsii.Number] = None,
        updated_by: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/metastore databricks_metastore} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#name Metastore#name}.
        :param storage_root: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#storage_root Metastore#storage_root}.
        :param cloud: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#cloud Metastore#cloud}.
        :param created_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#created_at Metastore#created_at}.
        :param created_by: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#created_by Metastore#created_by}.
        :param default_data_access_config_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#default_data_access_config_id Metastore#default_data_access_config_id}.
        :param delta_sharing_organization_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#delta_sharing_organization_name Metastore#delta_sharing_organization_name}.
        :param delta_sharing_recipient_token_lifetime_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#delta_sharing_recipient_token_lifetime_in_seconds Metastore#delta_sharing_recipient_token_lifetime_in_seconds}.
        :param delta_sharing_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#delta_sharing_scope Metastore#delta_sharing_scope}.
        :param force_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#force_destroy Metastore#force_destroy}.
        :param global_metastore_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#global_metastore_id Metastore#global_metastore_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#id Metastore#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#owner Metastore#owner}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#region Metastore#region}.
        :param updated_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#updated_at Metastore#updated_at}.
        :param updated_by: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#updated_by Metastore#updated_by}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5224edebdb4ee7243f8c635d3d8c38e15c5f4c0abd1515a48cf43863b57574c3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MetastoreConfig(
            name=name,
            storage_root=storage_root,
            cloud=cloud,
            created_at=created_at,
            created_by=created_by,
            default_data_access_config_id=default_data_access_config_id,
            delta_sharing_organization_name=delta_sharing_organization_name,
            delta_sharing_recipient_token_lifetime_in_seconds=delta_sharing_recipient_token_lifetime_in_seconds,
            delta_sharing_scope=delta_sharing_scope,
            force_destroy=force_destroy,
            global_metastore_id=global_metastore_id,
            id=id,
            owner=owner,
            region=region,
            updated_at=updated_at,
            updated_by=updated_by,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCloud")
    def reset_cloud(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloud", []))

    @jsii.member(jsii_name="resetCreatedAt")
    def reset_created_at(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreatedAt", []))

    @jsii.member(jsii_name="resetCreatedBy")
    def reset_created_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreatedBy", []))

    @jsii.member(jsii_name="resetDefaultDataAccessConfigId")
    def reset_default_data_access_config_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultDataAccessConfigId", []))

    @jsii.member(jsii_name="resetDeltaSharingOrganizationName")
    def reset_delta_sharing_organization_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeltaSharingOrganizationName", []))

    @jsii.member(jsii_name="resetDeltaSharingRecipientTokenLifetimeInSeconds")
    def reset_delta_sharing_recipient_token_lifetime_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeltaSharingRecipientTokenLifetimeInSeconds", []))

    @jsii.member(jsii_name="resetDeltaSharingScope")
    def reset_delta_sharing_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeltaSharingScope", []))

    @jsii.member(jsii_name="resetForceDestroy")
    def reset_force_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDestroy", []))

    @jsii.member(jsii_name="resetGlobalMetastoreId")
    def reset_global_metastore_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlobalMetastoreId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOwner")
    def reset_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwner", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetUpdatedAt")
    def reset_updated_at(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdatedAt", []))

    @jsii.member(jsii_name="resetUpdatedBy")
    def reset_updated_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdatedBy", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="cloudInput")
    def cloud_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudInput"))

    @builtins.property
    @jsii.member(jsii_name="createdAtInput")
    def created_at_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "createdAtInput"))

    @builtins.property
    @jsii.member(jsii_name="createdByInput")
    def created_by_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createdByInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultDataAccessConfigIdInput")
    def default_data_access_config_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultDataAccessConfigIdInput"))

    @builtins.property
    @jsii.member(jsii_name="deltaSharingOrganizationNameInput")
    def delta_sharing_organization_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deltaSharingOrganizationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deltaSharingRecipientTokenLifetimeInSecondsInput")
    def delta_sharing_recipient_token_lifetime_in_seconds_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deltaSharingRecipientTokenLifetimeInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="deltaSharingScopeInput")
    def delta_sharing_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deltaSharingScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDestroyInput")
    def force_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="globalMetastoreIdInput")
    def global_metastore_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "globalMetastoreIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="storageRootInput")
    def storage_root_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageRootInput"))

    @builtins.property
    @jsii.member(jsii_name="updatedAtInput")
    def updated_at_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "updatedAtInput"))

    @builtins.property
    @jsii.member(jsii_name="updatedByInput")
    def updated_by_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updatedByInput"))

    @builtins.property
    @jsii.member(jsii_name="cloud")
    def cloud(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloud"))

    @cloud.setter
    def cloud(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__257574bffb262cdfbe18225cc92dd37e08dc7f570123f8b500b1175ac736b8a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloud", value)

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "createdAt"))

    @created_at.setter
    def created_at(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7295848c7443dd85b7380198f3cd8e9aaa7d955117ce66d6511226f164ea4f87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createdAt", value)

    @builtins.property
    @jsii.member(jsii_name="createdBy")
    def created_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdBy"))

    @created_by.setter
    def created_by(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de26e07608635cdd200a31eaa9f25382f4128a5c4992e9be95491ee79fc1d135)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createdBy", value)

    @builtins.property
    @jsii.member(jsii_name="defaultDataAccessConfigId")
    def default_data_access_config_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultDataAccessConfigId"))

    @default_data_access_config_id.setter
    def default_data_access_config_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2fa503b497f0e5b5134121e227b92e81d7ffda31f3bcb02d8567fa50cde69ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultDataAccessConfigId", value)

    @builtins.property
    @jsii.member(jsii_name="deltaSharingOrganizationName")
    def delta_sharing_organization_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deltaSharingOrganizationName"))

    @delta_sharing_organization_name.setter
    def delta_sharing_organization_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c32cf049dbdbf407a181488b527b8510d1ab626df69e5dd4ccd43e0778499bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deltaSharingOrganizationName", value)

    @builtins.property
    @jsii.member(jsii_name="deltaSharingRecipientTokenLifetimeInSeconds")
    def delta_sharing_recipient_token_lifetime_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deltaSharingRecipientTokenLifetimeInSeconds"))

    @delta_sharing_recipient_token_lifetime_in_seconds.setter
    def delta_sharing_recipient_token_lifetime_in_seconds(
        self,
        value: jsii.Number,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c27fe107ffe8beb251e6ed1eb81e697001939b3ff10831c51ec0a04349cee4e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deltaSharingRecipientTokenLifetimeInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="deltaSharingScope")
    def delta_sharing_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deltaSharingScope"))

    @delta_sharing_scope.setter
    def delta_sharing_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d35a56c46e48fa568b4011bcb48832a6becc11fcc5bed324533ba9e6ccfd843)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deltaSharingScope", value)

    @builtins.property
    @jsii.member(jsii_name="forceDestroy")
    def force_destroy(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forceDestroy"))

    @force_destroy.setter
    def force_destroy(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f5a64276236cd68def84bbb4ebd3665c2d7a15ca108d975d0a7a74ef53979d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="globalMetastoreId")
    def global_metastore_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "globalMetastoreId"))

    @global_metastore_id.setter
    def global_metastore_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e6294920d3ff3f90b557ff34e35a42cee71535a2fcadc877475ba40581061bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalMetastoreId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49fb0ed9bb3cda794d66cea20841a4d9d93594c9ae5d13a8115e31e3f4020040)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0dd7add61ef2d015cbf90d30c0f7f5638c75161ae8372b1c38582b03a9a1ead)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cd30f9dbb9069c5bfbe18385a14191230564a270dbe6dfd213eddcd8174b451)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dcee31e137ec89291fd8352841f26cfbed7983d3545f86e0f15a0a41f3a1552)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="storageRoot")
    def storage_root(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageRoot"))

    @storage_root.setter
    def storage_root(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__583e981ed7b112019381c934e78481dd59245e4956aa6ec039f6af12d7e08688)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageRoot", value)

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "updatedAt"))

    @updated_at.setter
    def updated_at(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3da4a8b43b25cea51c230a6aa7e2a1b2111917130084a3662f2f524a03eb7d01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updatedAt", value)

    @builtins.property
    @jsii.member(jsii_name="updatedBy")
    def updated_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedBy"))

    @updated_by.setter
    def updated_by(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b389f2d7816fd9f0788a0388eb9094285fbdf66fe89f11f9eb7464d0edca1d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updatedBy", value)


@jsii.data_type(
    jsii_type="databricks.metastore.MetastoreConfig",
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
        "storage_root": "storageRoot",
        "cloud": "cloud",
        "created_at": "createdAt",
        "created_by": "createdBy",
        "default_data_access_config_id": "defaultDataAccessConfigId",
        "delta_sharing_organization_name": "deltaSharingOrganizationName",
        "delta_sharing_recipient_token_lifetime_in_seconds": "deltaSharingRecipientTokenLifetimeInSeconds",
        "delta_sharing_scope": "deltaSharingScope",
        "force_destroy": "forceDestroy",
        "global_metastore_id": "globalMetastoreId",
        "id": "id",
        "owner": "owner",
        "region": "region",
        "updated_at": "updatedAt",
        "updated_by": "updatedBy",
    },
)
class MetastoreConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        storage_root: builtins.str,
        cloud: typing.Optional[builtins.str] = None,
        created_at: typing.Optional[jsii.Number] = None,
        created_by: typing.Optional[builtins.str] = None,
        default_data_access_config_id: typing.Optional[builtins.str] = None,
        delta_sharing_organization_name: typing.Optional[builtins.str] = None,
        delta_sharing_recipient_token_lifetime_in_seconds: typing.Optional[jsii.Number] = None,
        delta_sharing_scope: typing.Optional[builtins.str] = None,
        force_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        global_metastore_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        updated_at: typing.Optional[jsii.Number] = None,
        updated_by: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#name Metastore#name}.
        :param storage_root: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#storage_root Metastore#storage_root}.
        :param cloud: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#cloud Metastore#cloud}.
        :param created_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#created_at Metastore#created_at}.
        :param created_by: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#created_by Metastore#created_by}.
        :param default_data_access_config_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#default_data_access_config_id Metastore#default_data_access_config_id}.
        :param delta_sharing_organization_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#delta_sharing_organization_name Metastore#delta_sharing_organization_name}.
        :param delta_sharing_recipient_token_lifetime_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#delta_sharing_recipient_token_lifetime_in_seconds Metastore#delta_sharing_recipient_token_lifetime_in_seconds}.
        :param delta_sharing_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#delta_sharing_scope Metastore#delta_sharing_scope}.
        :param force_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#force_destroy Metastore#force_destroy}.
        :param global_metastore_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#global_metastore_id Metastore#global_metastore_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#id Metastore#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#owner Metastore#owner}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#region Metastore#region}.
        :param updated_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#updated_at Metastore#updated_at}.
        :param updated_by: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#updated_by Metastore#updated_by}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ee7ea8ee65d1802661e6814b188b4445c6cf73c9f38df70a5e71aff2d4180a8)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument storage_root", value=storage_root, expected_type=type_hints["storage_root"])
            check_type(argname="argument cloud", value=cloud, expected_type=type_hints["cloud"])
            check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
            check_type(argname="argument created_by", value=created_by, expected_type=type_hints["created_by"])
            check_type(argname="argument default_data_access_config_id", value=default_data_access_config_id, expected_type=type_hints["default_data_access_config_id"])
            check_type(argname="argument delta_sharing_organization_name", value=delta_sharing_organization_name, expected_type=type_hints["delta_sharing_organization_name"])
            check_type(argname="argument delta_sharing_recipient_token_lifetime_in_seconds", value=delta_sharing_recipient_token_lifetime_in_seconds, expected_type=type_hints["delta_sharing_recipient_token_lifetime_in_seconds"])
            check_type(argname="argument delta_sharing_scope", value=delta_sharing_scope, expected_type=type_hints["delta_sharing_scope"])
            check_type(argname="argument force_destroy", value=force_destroy, expected_type=type_hints["force_destroy"])
            check_type(argname="argument global_metastore_id", value=global_metastore_id, expected_type=type_hints["global_metastore_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument updated_at", value=updated_at, expected_type=type_hints["updated_at"])
            check_type(argname="argument updated_by", value=updated_by, expected_type=type_hints["updated_by"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "storage_root": storage_root,
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
        if cloud is not None:
            self._values["cloud"] = cloud
        if created_at is not None:
            self._values["created_at"] = created_at
        if created_by is not None:
            self._values["created_by"] = created_by
        if default_data_access_config_id is not None:
            self._values["default_data_access_config_id"] = default_data_access_config_id
        if delta_sharing_organization_name is not None:
            self._values["delta_sharing_organization_name"] = delta_sharing_organization_name
        if delta_sharing_recipient_token_lifetime_in_seconds is not None:
            self._values["delta_sharing_recipient_token_lifetime_in_seconds"] = delta_sharing_recipient_token_lifetime_in_seconds
        if delta_sharing_scope is not None:
            self._values["delta_sharing_scope"] = delta_sharing_scope
        if force_destroy is not None:
            self._values["force_destroy"] = force_destroy
        if global_metastore_id is not None:
            self._values["global_metastore_id"] = global_metastore_id
        if id is not None:
            self._values["id"] = id
        if owner is not None:
            self._values["owner"] = owner
        if region is not None:
            self._values["region"] = region
        if updated_at is not None:
            self._values["updated_at"] = updated_at
        if updated_by is not None:
            self._values["updated_by"] = updated_by

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#name Metastore#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_root(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#storage_root Metastore#storage_root}.'''
        result = self._values.get("storage_root")
        assert result is not None, "Required property 'storage_root' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloud(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#cloud Metastore#cloud}.'''
        result = self._values.get("cloud")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def created_at(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#created_at Metastore#created_at}.'''
        result = self._values.get("created_at")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def created_by(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#created_by Metastore#created_by}.'''
        result = self._values.get("created_by")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_data_access_config_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#default_data_access_config_id Metastore#default_data_access_config_id}.'''
        result = self._values.get("default_data_access_config_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delta_sharing_organization_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#delta_sharing_organization_name Metastore#delta_sharing_organization_name}.'''
        result = self._values.get("delta_sharing_organization_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delta_sharing_recipient_token_lifetime_in_seconds(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#delta_sharing_recipient_token_lifetime_in_seconds Metastore#delta_sharing_recipient_token_lifetime_in_seconds}.'''
        result = self._values.get("delta_sharing_recipient_token_lifetime_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def delta_sharing_scope(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#delta_sharing_scope Metastore#delta_sharing_scope}.'''
        result = self._values.get("delta_sharing_scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#force_destroy Metastore#force_destroy}.'''
        result = self._values.get("force_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def global_metastore_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#global_metastore_id Metastore#global_metastore_id}.'''
        result = self._values.get("global_metastore_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#id Metastore#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#owner Metastore#owner}.'''
        result = self._values.get("owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#region Metastore#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def updated_at(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#updated_at Metastore#updated_at}.'''
        result = self._values.get("updated_at")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def updated_by(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore#updated_by Metastore#updated_by}.'''
        result = self._values.get("updated_by")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetastoreConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Metastore",
    "MetastoreConfig",
]

publication.publish()

def _typecheckingstub__5224edebdb4ee7243f8c635d3d8c38e15c5f4c0abd1515a48cf43863b57574c3(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    storage_root: builtins.str,
    cloud: typing.Optional[builtins.str] = None,
    created_at: typing.Optional[jsii.Number] = None,
    created_by: typing.Optional[builtins.str] = None,
    default_data_access_config_id: typing.Optional[builtins.str] = None,
    delta_sharing_organization_name: typing.Optional[builtins.str] = None,
    delta_sharing_recipient_token_lifetime_in_seconds: typing.Optional[jsii.Number] = None,
    delta_sharing_scope: typing.Optional[builtins.str] = None,
    force_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    global_metastore_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    owner: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    updated_at: typing.Optional[jsii.Number] = None,
    updated_by: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__257574bffb262cdfbe18225cc92dd37e08dc7f570123f8b500b1175ac736b8a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7295848c7443dd85b7380198f3cd8e9aaa7d955117ce66d6511226f164ea4f87(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de26e07608635cdd200a31eaa9f25382f4128a5c4992e9be95491ee79fc1d135(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2fa503b497f0e5b5134121e227b92e81d7ffda31f3bcb02d8567fa50cde69ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c32cf049dbdbf407a181488b527b8510d1ab626df69e5dd4ccd43e0778499bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c27fe107ffe8beb251e6ed1eb81e697001939b3ff10831c51ec0a04349cee4e1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d35a56c46e48fa568b4011bcb48832a6becc11fcc5bed324533ba9e6ccfd843(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f5a64276236cd68def84bbb4ebd3665c2d7a15ca108d975d0a7a74ef53979d0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e6294920d3ff3f90b557ff34e35a42cee71535a2fcadc877475ba40581061bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49fb0ed9bb3cda794d66cea20841a4d9d93594c9ae5d13a8115e31e3f4020040(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0dd7add61ef2d015cbf90d30c0f7f5638c75161ae8372b1c38582b03a9a1ead(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cd30f9dbb9069c5bfbe18385a14191230564a270dbe6dfd213eddcd8174b451(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dcee31e137ec89291fd8352841f26cfbed7983d3545f86e0f15a0a41f3a1552(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__583e981ed7b112019381c934e78481dd59245e4956aa6ec039f6af12d7e08688(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3da4a8b43b25cea51c230a6aa7e2a1b2111917130084a3662f2f524a03eb7d01(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b389f2d7816fd9f0788a0388eb9094285fbdf66fe89f11f9eb7464d0edca1d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ee7ea8ee65d1802661e6814b188b4445c6cf73c9f38df70a5e71aff2d4180a8(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    storage_root: builtins.str,
    cloud: typing.Optional[builtins.str] = None,
    created_at: typing.Optional[jsii.Number] = None,
    created_by: typing.Optional[builtins.str] = None,
    default_data_access_config_id: typing.Optional[builtins.str] = None,
    delta_sharing_organization_name: typing.Optional[builtins.str] = None,
    delta_sharing_recipient_token_lifetime_in_seconds: typing.Optional[jsii.Number] = None,
    delta_sharing_scope: typing.Optional[builtins.str] = None,
    force_destroy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    global_metastore_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    owner: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    updated_at: typing.Optional[jsii.Number] = None,
    updated_by: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
