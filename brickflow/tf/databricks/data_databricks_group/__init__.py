'''
# `data_databricks_group`

Refer to the Terraform Registory for docs: [`data_databricks_group`](https://www.terraform.io/docs/providers/databricks/d/group).
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


class DataDatabricksGroup(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksGroup.DataDatabricksGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/d/group databricks_group}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        display_name: builtins.str,
        allow_cluster_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_instance_pool_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        child_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        databricks_sql_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        external_id: typing.Optional[builtins.str] = None,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        instance_profiles: typing.Optional[typing.Sequence[builtins.str]] = None,
        members: typing.Optional[typing.Sequence[builtins.str]] = None,
        recursive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        service_principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        users: typing.Optional[typing.Sequence[builtins.str]] = None,
        workspace_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/d/group databricks_group} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#display_name DataDatabricksGroup#display_name}.
        :param allow_cluster_create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#allow_cluster_create DataDatabricksGroup#allow_cluster_create}.
        :param allow_instance_pool_create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#allow_instance_pool_create DataDatabricksGroup#allow_instance_pool_create}.
        :param child_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#child_groups DataDatabricksGroup#child_groups}.
        :param databricks_sql_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#databricks_sql_access DataDatabricksGroup#databricks_sql_access}.
        :param external_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#external_id DataDatabricksGroup#external_id}.
        :param groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#groups DataDatabricksGroup#groups}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#id DataDatabricksGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_profiles: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#instance_profiles DataDatabricksGroup#instance_profiles}.
        :param members: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#members DataDatabricksGroup#members}.
        :param recursive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#recursive DataDatabricksGroup#recursive}.
        :param service_principals: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#service_principals DataDatabricksGroup#service_principals}.
        :param users: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#users DataDatabricksGroup#users}.
        :param workspace_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#workspace_access DataDatabricksGroup#workspace_access}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e8b622da612e0c5e0620219bb6e93da91aca908317d5dbcd863d5ee53bc78c5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataDatabricksGroupConfig(
            display_name=display_name,
            allow_cluster_create=allow_cluster_create,
            allow_instance_pool_create=allow_instance_pool_create,
            child_groups=child_groups,
            databricks_sql_access=databricks_sql_access,
            external_id=external_id,
            groups=groups,
            id=id,
            instance_profiles=instance_profiles,
            members=members,
            recursive=recursive,
            service_principals=service_principals,
            users=users,
            workspace_access=workspace_access,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAllowClusterCreate")
    def reset_allow_cluster_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowClusterCreate", []))

    @jsii.member(jsii_name="resetAllowInstancePoolCreate")
    def reset_allow_instance_pool_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowInstancePoolCreate", []))

    @jsii.member(jsii_name="resetChildGroups")
    def reset_child_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChildGroups", []))

    @jsii.member(jsii_name="resetDatabricksSqlAccess")
    def reset_databricks_sql_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabricksSqlAccess", []))

    @jsii.member(jsii_name="resetExternalId")
    def reset_external_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalId", []))

    @jsii.member(jsii_name="resetGroups")
    def reset_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroups", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstanceProfiles")
    def reset_instance_profiles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceProfiles", []))

    @jsii.member(jsii_name="resetMembers")
    def reset_members(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMembers", []))

    @jsii.member(jsii_name="resetRecursive")
    def reset_recursive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecursive", []))

    @jsii.member(jsii_name="resetServicePrincipals")
    def reset_service_principals(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServicePrincipals", []))

    @jsii.member(jsii_name="resetUsers")
    def reset_users(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsers", []))

    @jsii.member(jsii_name="resetWorkspaceAccess")
    def reset_workspace_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceAccess", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="allowClusterCreateInput")
    def allow_cluster_create_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowClusterCreateInput"))

    @builtins.property
    @jsii.member(jsii_name="allowInstancePoolCreateInput")
    def allow_instance_pool_create_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowInstancePoolCreateInput"))

    @builtins.property
    @jsii.member(jsii_name="childGroupsInput")
    def child_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "childGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="databricksSqlAccessInput")
    def databricks_sql_access_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "databricksSqlAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="externalIdInput")
    def external_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="groupsInput")
    def groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceProfilesInput")
    def instance_profiles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instanceProfilesInput"))

    @builtins.property
    @jsii.member(jsii_name="membersInput")
    def members_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "membersInput"))

    @builtins.property
    @jsii.member(jsii_name="recursiveInput")
    def recursive_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "recursiveInput"))

    @builtins.property
    @jsii.member(jsii_name="servicePrincipalsInput")
    def service_principals_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "servicePrincipalsInput"))

    @builtins.property
    @jsii.member(jsii_name="usersInput")
    def users_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "usersInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceAccessInput")
    def workspace_access_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "workspaceAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="allowClusterCreate")
    def allow_cluster_create(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowClusterCreate"))

    @allow_cluster_create.setter
    def allow_cluster_create(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5580f257d28561bec0aa650c76cf916133745568b2b3b18ab58fcf6dcdf04730)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowClusterCreate", value)

    @builtins.property
    @jsii.member(jsii_name="allowInstancePoolCreate")
    def allow_instance_pool_create(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowInstancePoolCreate"))

    @allow_instance_pool_create.setter
    def allow_instance_pool_create(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6318320a3230f9e8c291718d9305710e4dddc3fc6936e656aae425da0fe5326)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowInstancePoolCreate", value)

    @builtins.property
    @jsii.member(jsii_name="childGroups")
    def child_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "childGroups"))

    @child_groups.setter
    def child_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baa11086865af666cd03c1f19c7d157d821eed549699ea8a29c05c4697c5883b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "childGroups", value)

    @builtins.property
    @jsii.member(jsii_name="databricksSqlAccess")
    def databricks_sql_access(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "databricksSqlAccess"))

    @databricks_sql_access.setter
    def databricks_sql_access(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__860c20feb53b7061db095d3d45928f40bfb555493e2a2252de91f42bf9924d68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databricksSqlAccess", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08e67957df8a0e42a7b2b9f551a2093a49f76628767d4a4a8bd55753d08733ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="externalId")
    def external_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalId"))

    @external_id.setter
    def external_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f7774dd43f501c0f3fd0ae7c21b4929e50f5733bb99ec8adc080626401bf5ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalId", value)

    @builtins.property
    @jsii.member(jsii_name="groups")
    def groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groups"))

    @groups.setter
    def groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c13b4f006c83c4584bd3cea88a7e5ad262329df4f33adbcaf24d0b07004cbeb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groups", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6574367056278d19927ba2430e228c8ac49afc01ad723dbf7a8eb3db030ccb2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfiles")
    def instance_profiles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceProfiles"))

    @instance_profiles.setter
    def instance_profiles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc20aba2cbcf688275d1f26bec6e68975062e96e3a4375f7e294d3532d655781)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfiles", value)

    @builtins.property
    @jsii.member(jsii_name="members")
    def members(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "members"))

    @members.setter
    def members(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0d52eec13d630ece6426dbdf84472823a3b0acdac647cd6e4ea0153c1b50ac8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "members", value)

    @builtins.property
    @jsii.member(jsii_name="recursive")
    def recursive(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "recursive"))

    @recursive.setter
    def recursive(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__227dec19a292a515a6a3548bd4cc1be48e994f0df4c6894ff975b70d1d874a72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recursive", value)

    @builtins.property
    @jsii.member(jsii_name="servicePrincipals")
    def service_principals(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "servicePrincipals"))

    @service_principals.setter
    def service_principals(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f583629f276b1ce7f77c891aa81d33c27b40202d7aee87cd612f6d22d5ebcd9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicePrincipals", value)

    @builtins.property
    @jsii.member(jsii_name="users")
    def users(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "users"))

    @users.setter
    def users(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__051a5a8cc299f23ef83cab54bcf6fa7ba5450afbe14fc5bbe1f3c4b21f0ca0f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "users", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceAccess")
    def workspace_access(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "workspaceAccess"))

    @workspace_access.setter
    def workspace_access(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d228b879962a6eed4f1c0ac2642e7ba1b6267fbbcee79fbe8a2bb002c820c04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceAccess", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksGroup.DataDatabricksGroupConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "display_name": "displayName",
        "allow_cluster_create": "allowClusterCreate",
        "allow_instance_pool_create": "allowInstancePoolCreate",
        "child_groups": "childGroups",
        "databricks_sql_access": "databricksSqlAccess",
        "external_id": "externalId",
        "groups": "groups",
        "id": "id",
        "instance_profiles": "instanceProfiles",
        "members": "members",
        "recursive": "recursive",
        "service_principals": "servicePrincipals",
        "users": "users",
        "workspace_access": "workspaceAccess",
    },
)
class DataDatabricksGroupConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        display_name: builtins.str,
        allow_cluster_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_instance_pool_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        child_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        databricks_sql_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        external_id: typing.Optional[builtins.str] = None,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        instance_profiles: typing.Optional[typing.Sequence[builtins.str]] = None,
        members: typing.Optional[typing.Sequence[builtins.str]] = None,
        recursive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        service_principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        users: typing.Optional[typing.Sequence[builtins.str]] = None,
        workspace_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#display_name DataDatabricksGroup#display_name}.
        :param allow_cluster_create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#allow_cluster_create DataDatabricksGroup#allow_cluster_create}.
        :param allow_instance_pool_create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#allow_instance_pool_create DataDatabricksGroup#allow_instance_pool_create}.
        :param child_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#child_groups DataDatabricksGroup#child_groups}.
        :param databricks_sql_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#databricks_sql_access DataDatabricksGroup#databricks_sql_access}.
        :param external_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#external_id DataDatabricksGroup#external_id}.
        :param groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#groups DataDatabricksGroup#groups}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#id DataDatabricksGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_profiles: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#instance_profiles DataDatabricksGroup#instance_profiles}.
        :param members: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#members DataDatabricksGroup#members}.
        :param recursive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#recursive DataDatabricksGroup#recursive}.
        :param service_principals: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#service_principals DataDatabricksGroup#service_principals}.
        :param users: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#users DataDatabricksGroup#users}.
        :param workspace_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#workspace_access DataDatabricksGroup#workspace_access}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5fa3cad342e8f651cc65118405e3075757f03bdd456a7517a7e8883b4b58858)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument allow_cluster_create", value=allow_cluster_create, expected_type=type_hints["allow_cluster_create"])
            check_type(argname="argument allow_instance_pool_create", value=allow_instance_pool_create, expected_type=type_hints["allow_instance_pool_create"])
            check_type(argname="argument child_groups", value=child_groups, expected_type=type_hints["child_groups"])
            check_type(argname="argument databricks_sql_access", value=databricks_sql_access, expected_type=type_hints["databricks_sql_access"])
            check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_profiles", value=instance_profiles, expected_type=type_hints["instance_profiles"])
            check_type(argname="argument members", value=members, expected_type=type_hints["members"])
            check_type(argname="argument recursive", value=recursive, expected_type=type_hints["recursive"])
            check_type(argname="argument service_principals", value=service_principals, expected_type=type_hints["service_principals"])
            check_type(argname="argument users", value=users, expected_type=type_hints["users"])
            check_type(argname="argument workspace_access", value=workspace_access, expected_type=type_hints["workspace_access"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "display_name": display_name,
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
        if allow_cluster_create is not None:
            self._values["allow_cluster_create"] = allow_cluster_create
        if allow_instance_pool_create is not None:
            self._values["allow_instance_pool_create"] = allow_instance_pool_create
        if child_groups is not None:
            self._values["child_groups"] = child_groups
        if databricks_sql_access is not None:
            self._values["databricks_sql_access"] = databricks_sql_access
        if external_id is not None:
            self._values["external_id"] = external_id
        if groups is not None:
            self._values["groups"] = groups
        if id is not None:
            self._values["id"] = id
        if instance_profiles is not None:
            self._values["instance_profiles"] = instance_profiles
        if members is not None:
            self._values["members"] = members
        if recursive is not None:
            self._values["recursive"] = recursive
        if service_principals is not None:
            self._values["service_principals"] = service_principals
        if users is not None:
            self._values["users"] = users
        if workspace_access is not None:
            self._values["workspace_access"] = workspace_access

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
    def display_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#display_name DataDatabricksGroup#display_name}.'''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_cluster_create(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#allow_cluster_create DataDatabricksGroup#allow_cluster_create}.'''
        result = self._values.get("allow_cluster_create")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def allow_instance_pool_create(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#allow_instance_pool_create DataDatabricksGroup#allow_instance_pool_create}.'''
        result = self._values.get("allow_instance_pool_create")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def child_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#child_groups DataDatabricksGroup#child_groups}.'''
        result = self._values.get("child_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def databricks_sql_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#databricks_sql_access DataDatabricksGroup#databricks_sql_access}.'''
        result = self._values.get("databricks_sql_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def external_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#external_id DataDatabricksGroup#external_id}.'''
        result = self._values.get("external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#groups DataDatabricksGroup#groups}.'''
        result = self._values.get("groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#id DataDatabricksGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_profiles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#instance_profiles DataDatabricksGroup#instance_profiles}.'''
        result = self._values.get("instance_profiles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def members(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#members DataDatabricksGroup#members}.'''
        result = self._values.get("members")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def recursive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#recursive DataDatabricksGroup#recursive}.'''
        result = self._values.get("recursive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def service_principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#service_principals DataDatabricksGroup#service_principals}.'''
        result = self._values.get("service_principals")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def users(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#users DataDatabricksGroup#users}.'''
        result = self._values.get("users")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def workspace_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/group#workspace_access DataDatabricksGroup#workspace_access}.'''
        result = self._values.get("workspace_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataDatabricksGroup",
    "DataDatabricksGroupConfig",
]

publication.publish()

def _typecheckingstub__9e8b622da612e0c5e0620219bb6e93da91aca908317d5dbcd863d5ee53bc78c5(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    display_name: builtins.str,
    allow_cluster_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allow_instance_pool_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    child_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    databricks_sql_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    external_id: typing.Optional[builtins.str] = None,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    instance_profiles: typing.Optional[typing.Sequence[builtins.str]] = None,
    members: typing.Optional[typing.Sequence[builtins.str]] = None,
    recursive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    service_principals: typing.Optional[typing.Sequence[builtins.str]] = None,
    users: typing.Optional[typing.Sequence[builtins.str]] = None,
    workspace_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__5580f257d28561bec0aa650c76cf916133745568b2b3b18ab58fcf6dcdf04730(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6318320a3230f9e8c291718d9305710e4dddc3fc6936e656aae425da0fe5326(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baa11086865af666cd03c1f19c7d157d821eed549699ea8a29c05c4697c5883b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__860c20feb53b7061db095d3d45928f40bfb555493e2a2252de91f42bf9924d68(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08e67957df8a0e42a7b2b9f551a2093a49f76628767d4a4a8bd55753d08733ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f7774dd43f501c0f3fd0ae7c21b4929e50f5733bb99ec8adc080626401bf5ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c13b4f006c83c4584bd3cea88a7e5ad262329df4f33adbcaf24d0b07004cbeb9(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6574367056278d19927ba2430e228c8ac49afc01ad723dbf7a8eb3db030ccb2e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc20aba2cbcf688275d1f26bec6e68975062e96e3a4375f7e294d3532d655781(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0d52eec13d630ece6426dbdf84472823a3b0acdac647cd6e4ea0153c1b50ac8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__227dec19a292a515a6a3548bd4cc1be48e994f0df4c6894ff975b70d1d874a72(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f583629f276b1ce7f77c891aa81d33c27b40202d7aee87cd612f6d22d5ebcd9c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__051a5a8cc299f23ef83cab54bcf6fa7ba5450afbe14fc5bbe1f3c4b21f0ca0f0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d228b879962a6eed4f1c0ac2642e7ba1b6267fbbcee79fbe8a2bb002c820c04(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5fa3cad342e8f651cc65118405e3075757f03bdd456a7517a7e8883b4b58858(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    display_name: builtins.str,
    allow_cluster_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allow_instance_pool_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    child_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    databricks_sql_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    external_id: typing.Optional[builtins.str] = None,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    instance_profiles: typing.Optional[typing.Sequence[builtins.str]] = None,
    members: typing.Optional[typing.Sequence[builtins.str]] = None,
    recursive: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    service_principals: typing.Optional[typing.Sequence[builtins.str]] = None,
    users: typing.Optional[typing.Sequence[builtins.str]] = None,
    workspace_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
