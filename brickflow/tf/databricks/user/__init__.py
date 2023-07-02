'''
# `databricks_user`

Refer to the Terraform Registory for docs: [`databricks_user`](https://www.terraform.io/docs/providers/databricks/r/user).
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


class User(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.user.User",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/user databricks_user}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        user_name: builtins.str,
        active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_cluster_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_instance_pool_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        databricks_sql_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        display_name: typing.Optional[builtins.str] = None,
        external_id: typing.Optional[builtins.str] = None,
        force: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        force_delete_home_dir: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        force_delete_repos: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        home: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        repos: typing.Optional[builtins.str] = None,
        workspace_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/user databricks_user} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#user_name User#user_name}.
        :param active: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#active User#active}.
        :param allow_cluster_create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#allow_cluster_create User#allow_cluster_create}.
        :param allow_instance_pool_create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#allow_instance_pool_create User#allow_instance_pool_create}.
        :param databricks_sql_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#databricks_sql_access User#databricks_sql_access}.
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#display_name User#display_name}.
        :param external_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#external_id User#external_id}.
        :param force: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#force User#force}.
        :param force_delete_home_dir: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#force_delete_home_dir User#force_delete_home_dir}.
        :param force_delete_repos: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#force_delete_repos User#force_delete_repos}.
        :param home: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#home User#home}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#id User#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param repos: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#repos User#repos}.
        :param workspace_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#workspace_access User#workspace_access}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9363b9544469366bf5355d9740d3f5b1acef4611d2794269faab5cedcda48932)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = UserConfig(
            user_name=user_name,
            active=active,
            allow_cluster_create=allow_cluster_create,
            allow_instance_pool_create=allow_instance_pool_create,
            databricks_sql_access=databricks_sql_access,
            display_name=display_name,
            external_id=external_id,
            force=force,
            force_delete_home_dir=force_delete_home_dir,
            force_delete_repos=force_delete_repos,
            home=home,
            id=id,
            repos=repos,
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

    @jsii.member(jsii_name="resetActive")
    def reset_active(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActive", []))

    @jsii.member(jsii_name="resetAllowClusterCreate")
    def reset_allow_cluster_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowClusterCreate", []))

    @jsii.member(jsii_name="resetAllowInstancePoolCreate")
    def reset_allow_instance_pool_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowInstancePoolCreate", []))

    @jsii.member(jsii_name="resetDatabricksSqlAccess")
    def reset_databricks_sql_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabricksSqlAccess", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetExternalId")
    def reset_external_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalId", []))

    @jsii.member(jsii_name="resetForce")
    def reset_force(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForce", []))

    @jsii.member(jsii_name="resetForceDeleteHomeDir")
    def reset_force_delete_home_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDeleteHomeDir", []))

    @jsii.member(jsii_name="resetForceDeleteRepos")
    def reset_force_delete_repos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDeleteRepos", []))

    @jsii.member(jsii_name="resetHome")
    def reset_home(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHome", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRepos")
    def reset_repos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepos", []))

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
    @jsii.member(jsii_name="activeInput")
    def active_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "activeInput"))

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
    @jsii.member(jsii_name="forceDeleteHomeDirInput")
    def force_delete_home_dir_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceDeleteHomeDirInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDeleteReposInput")
    def force_delete_repos_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceDeleteReposInput"))

    @builtins.property
    @jsii.member(jsii_name="forceInput")
    def force_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceInput"))

    @builtins.property
    @jsii.member(jsii_name="homeInput")
    def home_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="reposInput")
    def repos_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "reposInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameInput")
    def user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userNameInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceAccessInput")
    def workspace_access_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "workspaceAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="active")
    def active(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "active"))

    @active.setter
    def active(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d9aac8be7697e097b795f8d1706570c15c8d4daee0e7b4045c5f39cb4d18696)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "active", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__35153470630bd60f52bc753b10fcc4d3ed707d0b29c9ea5f4ce783047c6fa8b5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b3e6e3643e260a19859bb9fe6296e487d2f4d65060a83fe048c527df1a2c4fc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowInstancePoolCreate", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__6842a40a73aa8b63fa9103ba7d3007db8c5ac36d4aa88f6c08738590ee5c38a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databricksSqlAccess", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c0ea75811b175e7608f716b4dd35eed0fb1d9011f8d1b9ecbcf71c61c19f8f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="externalId")
    def external_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalId"))

    @external_id.setter
    def external_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0237dad04d3e2af1ecdb95b081278d1c606b103c585df36c93678c1724dc7199)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalId", value)

    @builtins.property
    @jsii.member(jsii_name="force")
    def force(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "force"))

    @force.setter
    def force(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dfc3209732db852c18df7c85d2899415a80af21d3106d074ba7f575dab3757c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "force", value)

    @builtins.property
    @jsii.member(jsii_name="forceDeleteHomeDir")
    def force_delete_home_dir(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forceDeleteHomeDir"))

    @force_delete_home_dir.setter
    def force_delete_home_dir(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__073fb351327db6d3ae499969b7f9a5e84626a582ffa81aeedef371d0d68151d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDeleteHomeDir", value)

    @builtins.property
    @jsii.member(jsii_name="forceDeleteRepos")
    def force_delete_repos(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forceDeleteRepos"))

    @force_delete_repos.setter
    def force_delete_repos(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ae03d47b9a026bc69844f703f5092c30b596b783d5a72fb864c44e2d3fe3958)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDeleteRepos", value)

    @builtins.property
    @jsii.member(jsii_name="home")
    def home(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "home"))

    @home.setter
    def home(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4b8c8e95494adde0969414b281f83a29fcea6e2a01dc0f6ca04048c9656d454)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "home", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99af99c940bfe6df047a4232bc32349506810a5718084da1ebab4003b5da0db4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="repos")
    def repos(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repos"))

    @repos.setter
    def repos(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f86650417dfdab5e74cff33a4963197778d1f9c5fc800b7dcd5b4858ffe3f22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repos", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e09dda3eb7636ae68f419775b9a73ebc4f3015bd35e338c59f3e0179111b9e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__f7224291199422b594c5955f986f8efe203cac6a4ac7aaf09bf54e02bac66da2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceAccess", value)


@jsii.data_type(
    jsii_type="databricks.user.UserConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "user_name": "userName",
        "active": "active",
        "allow_cluster_create": "allowClusterCreate",
        "allow_instance_pool_create": "allowInstancePoolCreate",
        "databricks_sql_access": "databricksSqlAccess",
        "display_name": "displayName",
        "external_id": "externalId",
        "force": "force",
        "force_delete_home_dir": "forceDeleteHomeDir",
        "force_delete_repos": "forceDeleteRepos",
        "home": "home",
        "id": "id",
        "repos": "repos",
        "workspace_access": "workspaceAccess",
    },
)
class UserConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        user_name: builtins.str,
        active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_cluster_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_instance_pool_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        databricks_sql_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        display_name: typing.Optional[builtins.str] = None,
        external_id: typing.Optional[builtins.str] = None,
        force: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        force_delete_home_dir: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        force_delete_repos: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        home: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        repos: typing.Optional[builtins.str] = None,
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
        :param user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#user_name User#user_name}.
        :param active: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#active User#active}.
        :param allow_cluster_create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#allow_cluster_create User#allow_cluster_create}.
        :param allow_instance_pool_create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#allow_instance_pool_create User#allow_instance_pool_create}.
        :param databricks_sql_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#databricks_sql_access User#databricks_sql_access}.
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#display_name User#display_name}.
        :param external_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#external_id User#external_id}.
        :param force: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#force User#force}.
        :param force_delete_home_dir: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#force_delete_home_dir User#force_delete_home_dir}.
        :param force_delete_repos: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#force_delete_repos User#force_delete_repos}.
        :param home: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#home User#home}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#id User#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param repos: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#repos User#repos}.
        :param workspace_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#workspace_access User#workspace_access}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8be3231493c881db7da3b4c8fdad68fd0f7dbc4887d98884827adf9a5f5e4440)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument active", value=active, expected_type=type_hints["active"])
            check_type(argname="argument allow_cluster_create", value=allow_cluster_create, expected_type=type_hints["allow_cluster_create"])
            check_type(argname="argument allow_instance_pool_create", value=allow_instance_pool_create, expected_type=type_hints["allow_instance_pool_create"])
            check_type(argname="argument databricks_sql_access", value=databricks_sql_access, expected_type=type_hints["databricks_sql_access"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            check_type(argname="argument force", value=force, expected_type=type_hints["force"])
            check_type(argname="argument force_delete_home_dir", value=force_delete_home_dir, expected_type=type_hints["force_delete_home_dir"])
            check_type(argname="argument force_delete_repos", value=force_delete_repos, expected_type=type_hints["force_delete_repos"])
            check_type(argname="argument home", value=home, expected_type=type_hints["home"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument repos", value=repos, expected_type=type_hints["repos"])
            check_type(argname="argument workspace_access", value=workspace_access, expected_type=type_hints["workspace_access"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_name": user_name,
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
        if active is not None:
            self._values["active"] = active
        if allow_cluster_create is not None:
            self._values["allow_cluster_create"] = allow_cluster_create
        if allow_instance_pool_create is not None:
            self._values["allow_instance_pool_create"] = allow_instance_pool_create
        if databricks_sql_access is not None:
            self._values["databricks_sql_access"] = databricks_sql_access
        if display_name is not None:
            self._values["display_name"] = display_name
        if external_id is not None:
            self._values["external_id"] = external_id
        if force is not None:
            self._values["force"] = force
        if force_delete_home_dir is not None:
            self._values["force_delete_home_dir"] = force_delete_home_dir
        if force_delete_repos is not None:
            self._values["force_delete_repos"] = force_delete_repos
        if home is not None:
            self._values["home"] = home
        if id is not None:
            self._values["id"] = id
        if repos is not None:
            self._values["repos"] = repos
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
    def user_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#user_name User#user_name}.'''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#active User#active}.'''
        result = self._values.get("active")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def allow_cluster_create(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#allow_cluster_create User#allow_cluster_create}.'''
        result = self._values.get("allow_cluster_create")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def allow_instance_pool_create(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#allow_instance_pool_create User#allow_instance_pool_create}.'''
        result = self._values.get("allow_instance_pool_create")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def databricks_sql_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#databricks_sql_access User#databricks_sql_access}.'''
        result = self._values.get("databricks_sql_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#display_name User#display_name}.'''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#external_id User#external_id}.'''
        result = self._values.get("external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#force User#force}.'''
        result = self._values.get("force")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def force_delete_home_dir(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#force_delete_home_dir User#force_delete_home_dir}.'''
        result = self._values.get("force_delete_home_dir")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def force_delete_repos(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#force_delete_repos User#force_delete_repos}.'''
        result = self._values.get("force_delete_repos")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def home(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#home User#home}.'''
        result = self._values.get("home")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#id User#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repos(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#repos User#repos}.'''
        result = self._values.get("repos")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workspace_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/user#workspace_access User#workspace_access}.'''
        result = self._values.get("workspace_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "User",
    "UserConfig",
]

publication.publish()

def _typecheckingstub__9363b9544469366bf5355d9740d3f5b1acef4611d2794269faab5cedcda48932(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    user_name: builtins.str,
    active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allow_cluster_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allow_instance_pool_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    databricks_sql_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    display_name: typing.Optional[builtins.str] = None,
    external_id: typing.Optional[builtins.str] = None,
    force: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    force_delete_home_dir: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    force_delete_repos: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    home: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    repos: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__4d9aac8be7697e097b795f8d1706570c15c8d4daee0e7b4045c5f39cb4d18696(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35153470630bd60f52bc753b10fcc4d3ed707d0b29c9ea5f4ce783047c6fa8b5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3e6e3643e260a19859bb9fe6296e487d2f4d65060a83fe048c527df1a2c4fc0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6842a40a73aa8b63fa9103ba7d3007db8c5ac36d4aa88f6c08738590ee5c38a3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c0ea75811b175e7608f716b4dd35eed0fb1d9011f8d1b9ecbcf71c61c19f8f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0237dad04d3e2af1ecdb95b081278d1c606b103c585df36c93678c1724dc7199(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dfc3209732db852c18df7c85d2899415a80af21d3106d074ba7f575dab3757c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__073fb351327db6d3ae499969b7f9a5e84626a582ffa81aeedef371d0d68151d3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ae03d47b9a026bc69844f703f5092c30b596b783d5a72fb864c44e2d3fe3958(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4b8c8e95494adde0969414b281f83a29fcea6e2a01dc0f6ca04048c9656d454(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99af99c940bfe6df047a4232bc32349506810a5718084da1ebab4003b5da0db4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f86650417dfdab5e74cff33a4963197778d1f9c5fc800b7dcd5b4858ffe3f22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e09dda3eb7636ae68f419775b9a73ebc4f3015bd35e338c59f3e0179111b9e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7224291199422b594c5955f986f8efe203cac6a4ac7aaf09bf54e02bac66da2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8be3231493c881db7da3b4c8fdad68fd0f7dbc4887d98884827adf9a5f5e4440(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    user_name: builtins.str,
    active: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allow_cluster_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allow_instance_pool_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    databricks_sql_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    display_name: typing.Optional[builtins.str] = None,
    external_id: typing.Optional[builtins.str] = None,
    force: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    force_delete_home_dir: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    force_delete_repos: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    home: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    repos: typing.Optional[builtins.str] = None,
    workspace_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
