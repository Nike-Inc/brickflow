'''
# `databricks_secret_scope`

Refer to the Terraform Registory for docs: [`databricks_secret_scope`](https://www.terraform.io/docs/providers/databricks/r/secret_scope).
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


class SecretScope(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.secretScope.SecretScope",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope databricks_secret_scope}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        backend_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_manage_principal: typing.Optional[builtins.str] = None,
        keyvault_metadata: typing.Optional[typing.Union["SecretScopeKeyvaultMetadata", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope databricks_secret_scope} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#name SecretScope#name}.
        :param backend_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#backend_type SecretScope#backend_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#id SecretScope#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_manage_principal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#initial_manage_principal SecretScope#initial_manage_principal}.
        :param keyvault_metadata: keyvault_metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#keyvault_metadata SecretScope#keyvault_metadata}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__790839b78cd316c76e3b134e1ce9a8cdc3523e7a2d0603811b44638bc05336c5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SecretScopeConfig(
            name=name,
            backend_type=backend_type,
            id=id,
            initial_manage_principal=initial_manage_principal,
            keyvault_metadata=keyvault_metadata,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putKeyvaultMetadata")
    def put_keyvault_metadata(
        self,
        *,
        dns_name: builtins.str,
        resource_id: builtins.str,
    ) -> None:
        '''
        :param dns_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#dns_name SecretScope#dns_name}.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#resource_id SecretScope#resource_id}.
        '''
        value = SecretScopeKeyvaultMetadata(dns_name=dns_name, resource_id=resource_id)

        return typing.cast(None, jsii.invoke(self, "putKeyvaultMetadata", [value]))

    @jsii.member(jsii_name="resetBackendType")
    def reset_backend_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendType", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInitialManagePrincipal")
    def reset_initial_manage_principal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialManagePrincipal", []))

    @jsii.member(jsii_name="resetKeyvaultMetadata")
    def reset_keyvault_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyvaultMetadata", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="keyvaultMetadata")
    def keyvault_metadata(self) -> "SecretScopeKeyvaultMetadataOutputReference":
        return typing.cast("SecretScopeKeyvaultMetadataOutputReference", jsii.get(self, "keyvaultMetadata"))

    @builtins.property
    @jsii.member(jsii_name="backendTypeInput")
    def backend_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initialManagePrincipalInput")
    def initial_manage_principal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "initialManagePrincipalInput"))

    @builtins.property
    @jsii.member(jsii_name="keyvaultMetadataInput")
    def keyvault_metadata_input(self) -> typing.Optional["SecretScopeKeyvaultMetadata"]:
        return typing.cast(typing.Optional["SecretScopeKeyvaultMetadata"], jsii.get(self, "keyvaultMetadataInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="backendType")
    def backend_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendType"))

    @backend_type.setter
    def backend_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__314e82ccf99e56be96c90ed30b2edb06da83ba0ed359b9b5ac061dfb7ccf6c32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__971f4e97cf2d71e5de4c797e87837259de3eca60e74ccf7c3f665109e3f56705)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="initialManagePrincipal")
    def initial_manage_principal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "initialManagePrincipal"))

    @initial_manage_principal.setter
    def initial_manage_principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__332dd502d2d9316d2e1cf8867a3446aabf4b3cbc2387c3c04a8c24963578d773)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialManagePrincipal", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cefd03d4ad66b18115e723fed15506a203e742edfaf3a2fb4fa250d98c942286)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="databricks.secretScope.SecretScopeConfig",
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
        "backend_type": "backendType",
        "id": "id",
        "initial_manage_principal": "initialManagePrincipal",
        "keyvault_metadata": "keyvaultMetadata",
    },
)
class SecretScopeConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        backend_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_manage_principal: typing.Optional[builtins.str] = None,
        keyvault_metadata: typing.Optional[typing.Union["SecretScopeKeyvaultMetadata", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#name SecretScope#name}.
        :param backend_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#backend_type SecretScope#backend_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#id SecretScope#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_manage_principal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#initial_manage_principal SecretScope#initial_manage_principal}.
        :param keyvault_metadata: keyvault_metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#keyvault_metadata SecretScope#keyvault_metadata}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(keyvault_metadata, dict):
            keyvault_metadata = SecretScopeKeyvaultMetadata(**keyvault_metadata)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e8b017d4b0c99bb3dc6ce47a54a55cbe48c77940da4598b7d91a2bc7f478d54)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument backend_type", value=backend_type, expected_type=type_hints["backend_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument initial_manage_principal", value=initial_manage_principal, expected_type=type_hints["initial_manage_principal"])
            check_type(argname="argument keyvault_metadata", value=keyvault_metadata, expected_type=type_hints["keyvault_metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
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
        if backend_type is not None:
            self._values["backend_type"] = backend_type
        if id is not None:
            self._values["id"] = id
        if initial_manage_principal is not None:
            self._values["initial_manage_principal"] = initial_manage_principal
        if keyvault_metadata is not None:
            self._values["keyvault_metadata"] = keyvault_metadata

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#name SecretScope#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backend_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#backend_type SecretScope#backend_type}.'''
        result = self._values.get("backend_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#id SecretScope#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_manage_principal(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#initial_manage_principal SecretScope#initial_manage_principal}.'''
        result = self._values.get("initial_manage_principal")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keyvault_metadata(self) -> typing.Optional["SecretScopeKeyvaultMetadata"]:
        '''keyvault_metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#keyvault_metadata SecretScope#keyvault_metadata}
        '''
        result = self._values.get("keyvault_metadata")
        return typing.cast(typing.Optional["SecretScopeKeyvaultMetadata"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretScopeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.secretScope.SecretScopeKeyvaultMetadata",
    jsii_struct_bases=[],
    name_mapping={"dns_name": "dnsName", "resource_id": "resourceId"},
)
class SecretScopeKeyvaultMetadata:
    def __init__(self, *, dns_name: builtins.str, resource_id: builtins.str) -> None:
        '''
        :param dns_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#dns_name SecretScope#dns_name}.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#resource_id SecretScope#resource_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58d24a8877f719cbcb75d16e17a88c122215fc542c5f9a6dfb19cb5bfbdf6fbc)
            check_type(argname="argument dns_name", value=dns_name, expected_type=type_hints["dns_name"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dns_name": dns_name,
            "resource_id": resource_id,
        }

    @builtins.property
    def dns_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#dns_name SecretScope#dns_name}.'''
        result = self._values.get("dns_name")
        assert result is not None, "Required property 'dns_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/secret_scope#resource_id SecretScope#resource_id}.'''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretScopeKeyvaultMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecretScopeKeyvaultMetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.secretScope.SecretScopeKeyvaultMetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1d0c7ba1072a1653fdc760ed2c926a130dfa27275ac4144ad2e63b61491802e4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dnsNameInput")
    def dns_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceIdInput")
    def resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @dns_name.setter
    def dns_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7356ea76f9dbda4ed24eb31aa0f94984a7dffd3305fd55777c363a906be7f3e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f8e5f0006cbab86330d60513c68605cc38a8ffa2657bbe415260571f3b8834d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SecretScopeKeyvaultMetadata]:
        return typing.cast(typing.Optional[SecretScopeKeyvaultMetadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SecretScopeKeyvaultMetadata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d23d7881edbc530f25e14e3d089ca20ed0b58bee769174a425f3544452d8d326)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SecretScope",
    "SecretScopeConfig",
    "SecretScopeKeyvaultMetadata",
    "SecretScopeKeyvaultMetadataOutputReference",
]

publication.publish()

def _typecheckingstub__790839b78cd316c76e3b134e1ce9a8cdc3523e7a2d0603811b44638bc05336c5(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    backend_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    initial_manage_principal: typing.Optional[builtins.str] = None,
    keyvault_metadata: typing.Optional[typing.Union[SecretScopeKeyvaultMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__314e82ccf99e56be96c90ed30b2edb06da83ba0ed359b9b5ac061dfb7ccf6c32(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__971f4e97cf2d71e5de4c797e87837259de3eca60e74ccf7c3f665109e3f56705(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__332dd502d2d9316d2e1cf8867a3446aabf4b3cbc2387c3c04a8c24963578d773(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cefd03d4ad66b18115e723fed15506a203e742edfaf3a2fb4fa250d98c942286(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e8b017d4b0c99bb3dc6ce47a54a55cbe48c77940da4598b7d91a2bc7f478d54(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    backend_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    initial_manage_principal: typing.Optional[builtins.str] = None,
    keyvault_metadata: typing.Optional[typing.Union[SecretScopeKeyvaultMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58d24a8877f719cbcb75d16e17a88c122215fc542c5f9a6dfb19cb5bfbdf6fbc(
    *,
    dns_name: builtins.str,
    resource_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d0c7ba1072a1653fdc760ed2c926a130dfa27275ac4144ad2e63b61491802e4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7356ea76f9dbda4ed24eb31aa0f94984a7dffd3305fd55777c363a906be7f3e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f8e5f0006cbab86330d60513c68605cc38a8ffa2657bbe415260571f3b8834d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d23d7881edbc530f25e14e3d089ca20ed0b58bee769174a425f3544452d8d326(
    value: typing.Optional[SecretScopeKeyvaultMetadata],
) -> None:
    """Type checking stubs"""
    pass
