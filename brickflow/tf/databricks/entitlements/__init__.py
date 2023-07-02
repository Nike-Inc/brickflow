'''
# `databricks_entitlements`

Refer to the Terraform Registory for docs: [`databricks_entitlements`](https://www.terraform.io/docs/providers/databricks/r/entitlements).
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


class Entitlements(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.entitlements.Entitlements",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/entitlements databricks_entitlements}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        allow_cluster_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_instance_pool_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        databricks_sql_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        group_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        service_principal_id: typing.Optional[builtins.str] = None,
        user_id: typing.Optional[builtins.str] = None,
        workspace_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/entitlements databricks_entitlements} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param allow_cluster_create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#allow_cluster_create Entitlements#allow_cluster_create}.
        :param allow_instance_pool_create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#allow_instance_pool_create Entitlements#allow_instance_pool_create}.
        :param databricks_sql_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#databricks_sql_access Entitlements#databricks_sql_access}.
        :param group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#group_id Entitlements#group_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#id Entitlements#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param service_principal_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#service_principal_id Entitlements#service_principal_id}.
        :param user_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#user_id Entitlements#user_id}.
        :param workspace_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#workspace_access Entitlements#workspace_access}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3588839548dd642b3abca56327dff5bdf4f347367c5c3463af61a52d57b92462)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EntitlementsConfig(
            allow_cluster_create=allow_cluster_create,
            allow_instance_pool_create=allow_instance_pool_create,
            databricks_sql_access=databricks_sql_access,
            group_id=group_id,
            id=id,
            service_principal_id=service_principal_id,
            user_id=user_id,
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

    @jsii.member(jsii_name="resetDatabricksSqlAccess")
    def reset_databricks_sql_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabricksSqlAccess", []))

    @jsii.member(jsii_name="resetGroupId")
    def reset_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetServicePrincipalId")
    def reset_service_principal_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServicePrincipalId", []))

    @jsii.member(jsii_name="resetUserId")
    def reset_user_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserId", []))

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
    @jsii.member(jsii_name="databricksSqlAccessInput")
    def databricks_sql_access_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "databricksSqlAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="servicePrincipalIdInput")
    def service_principal_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicePrincipalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userIdInput")
    def user_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userIdInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__4de7ba3be85d74fd8c7a24f5e48e7b6f404d0a6b9095a85d8b36c91a424dbca5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1d99946f620c0a5e3920095e39afcc7c0bcf52540103162ccc2e24d834563bb0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f314c7e55367a2024dcd0af5487b941e296d2bb88e4fdf9253f233587ad199d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databricksSqlAccess", value)

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f8f81622e4e39345c31d70f8054c6d19def72f8c4dbf9f296cb3c410a280659)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0846d56425365e7769edc4435dea78c655bf27f5a4f2b44fa81be8004e07aae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="servicePrincipalId")
    def service_principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicePrincipalId"))

    @service_principal_id.setter
    def service_principal_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6aa87680c4541a60369f428d3d70438b3831119c7b29c0e009e2d28c6593a704)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicePrincipalId", value)

    @builtins.property
    @jsii.member(jsii_name="userId")
    def user_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userId"))

    @user_id.setter
    def user_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef17ca0f070c9acbe000cf65e1cd0c3bb2f68129f1c0de85ff2f2d6ad4265f6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userId", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__13ff9ef1d1d5927de26017b10d125e89bd9c9ef442be63c9e591ab8c32f8227e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceAccess", value)


@jsii.data_type(
    jsii_type="databricks.entitlements.EntitlementsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "allow_cluster_create": "allowClusterCreate",
        "allow_instance_pool_create": "allowInstancePoolCreate",
        "databricks_sql_access": "databricksSqlAccess",
        "group_id": "groupId",
        "id": "id",
        "service_principal_id": "servicePrincipalId",
        "user_id": "userId",
        "workspace_access": "workspaceAccess",
    },
)
class EntitlementsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        allow_cluster_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allow_instance_pool_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        databricks_sql_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        group_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        service_principal_id: typing.Optional[builtins.str] = None,
        user_id: typing.Optional[builtins.str] = None,
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
        :param allow_cluster_create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#allow_cluster_create Entitlements#allow_cluster_create}.
        :param allow_instance_pool_create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#allow_instance_pool_create Entitlements#allow_instance_pool_create}.
        :param databricks_sql_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#databricks_sql_access Entitlements#databricks_sql_access}.
        :param group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#group_id Entitlements#group_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#id Entitlements#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param service_principal_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#service_principal_id Entitlements#service_principal_id}.
        :param user_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#user_id Entitlements#user_id}.
        :param workspace_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#workspace_access Entitlements#workspace_access}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be89982d8d3ce089d453230b86ee64fd57d036c4fa43c54473f233007a3fb210)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument allow_cluster_create", value=allow_cluster_create, expected_type=type_hints["allow_cluster_create"])
            check_type(argname="argument allow_instance_pool_create", value=allow_instance_pool_create, expected_type=type_hints["allow_instance_pool_create"])
            check_type(argname="argument databricks_sql_access", value=databricks_sql_access, expected_type=type_hints["databricks_sql_access"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument service_principal_id", value=service_principal_id, expected_type=type_hints["service_principal_id"])
            check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
            check_type(argname="argument workspace_access", value=workspace_access, expected_type=type_hints["workspace_access"])
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
        if allow_cluster_create is not None:
            self._values["allow_cluster_create"] = allow_cluster_create
        if allow_instance_pool_create is not None:
            self._values["allow_instance_pool_create"] = allow_instance_pool_create
        if databricks_sql_access is not None:
            self._values["databricks_sql_access"] = databricks_sql_access
        if group_id is not None:
            self._values["group_id"] = group_id
        if id is not None:
            self._values["id"] = id
        if service_principal_id is not None:
            self._values["service_principal_id"] = service_principal_id
        if user_id is not None:
            self._values["user_id"] = user_id
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
    def allow_cluster_create(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#allow_cluster_create Entitlements#allow_cluster_create}.'''
        result = self._values.get("allow_cluster_create")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def allow_instance_pool_create(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#allow_instance_pool_create Entitlements#allow_instance_pool_create}.'''
        result = self._values.get("allow_instance_pool_create")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def databricks_sql_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#databricks_sql_access Entitlements#databricks_sql_access}.'''
        result = self._values.get("databricks_sql_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#group_id Entitlements#group_id}.'''
        result = self._values.get("group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#id Entitlements#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_principal_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#service_principal_id Entitlements#service_principal_id}.'''
        result = self._values.get("service_principal_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#user_id Entitlements#user_id}.'''
        result = self._values.get("user_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workspace_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/entitlements#workspace_access Entitlements#workspace_access}.'''
        result = self._values.get("workspace_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EntitlementsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Entitlements",
    "EntitlementsConfig",
]

publication.publish()

def _typecheckingstub__3588839548dd642b3abca56327dff5bdf4f347367c5c3463af61a52d57b92462(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    allow_cluster_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allow_instance_pool_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    databricks_sql_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    group_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    service_principal_id: typing.Optional[builtins.str] = None,
    user_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__4de7ba3be85d74fd8c7a24f5e48e7b6f404d0a6b9095a85d8b36c91a424dbca5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d99946f620c0a5e3920095e39afcc7c0bcf52540103162ccc2e24d834563bb0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f314c7e55367a2024dcd0af5487b941e296d2bb88e4fdf9253f233587ad199d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f8f81622e4e39345c31d70f8054c6d19def72f8c4dbf9f296cb3c410a280659(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0846d56425365e7769edc4435dea78c655bf27f5a4f2b44fa81be8004e07aae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aa87680c4541a60369f428d3d70438b3831119c7b29c0e009e2d28c6593a704(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef17ca0f070c9acbe000cf65e1cd0c3bb2f68129f1c0de85ff2f2d6ad4265f6d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13ff9ef1d1d5927de26017b10d125e89bd9c9ef442be63c9e591ab8c32f8227e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be89982d8d3ce089d453230b86ee64fd57d036c4fa43c54473f233007a3fb210(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    allow_cluster_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allow_instance_pool_create: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    databricks_sql_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    group_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    service_principal_id: typing.Optional[builtins.str] = None,
    user_id: typing.Optional[builtins.str] = None,
    workspace_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
