'''
# `databricks_storage_credential`

Refer to the Terraform Registory for docs: [`databricks_storage_credential`](https://www.terraform.io/docs/providers/databricks/r/storage_credential).
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


class StorageCredential(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.storageCredential.StorageCredential",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential databricks_storage_credential}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        aws_iam_role: typing.Optional[typing.Union["StorageCredentialAwsIamRole", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_managed_identity: typing.Optional[typing.Union["StorageCredentialAzureManagedIdentity", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_service_principal: typing.Optional[typing.Union["StorageCredentialAzureServicePrincipal", typing.Dict[builtins.str, typing.Any]]] = None,
        comment: typing.Optional[builtins.str] = None,
        databricks_gcp_service_account: typing.Optional[typing.Union["StorageCredentialDatabricksGcpServiceAccount", typing.Dict[builtins.str, typing.Any]]] = None,
        gcp_service_account_key: typing.Optional[typing.Union["StorageCredentialGcpServiceAccountKey", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        metastore_id: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential databricks_storage_credential} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#name StorageCredential#name}.
        :param aws_iam_role: aws_iam_role block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#aws_iam_role StorageCredential#aws_iam_role}
        :param azure_managed_identity: azure_managed_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#azure_managed_identity StorageCredential#azure_managed_identity}
        :param azure_service_principal: azure_service_principal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#azure_service_principal StorageCredential#azure_service_principal}
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#comment StorageCredential#comment}.
        :param databricks_gcp_service_account: databricks_gcp_service_account block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#databricks_gcp_service_account StorageCredential#databricks_gcp_service_account}
        :param gcp_service_account_key: gcp_service_account_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#gcp_service_account_key StorageCredential#gcp_service_account_key}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#id StorageCredential#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metastore_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#metastore_id StorageCredential#metastore_id}.
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#owner StorageCredential#owner}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cae7be342b20e51a499937993cb5957886bcf0a9775c8bb7c4b8650977735ee8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageCredentialConfig(
            name=name,
            aws_iam_role=aws_iam_role,
            azure_managed_identity=azure_managed_identity,
            azure_service_principal=azure_service_principal,
            comment=comment,
            databricks_gcp_service_account=databricks_gcp_service_account,
            gcp_service_account_key=gcp_service_account_key,
            id=id,
            metastore_id=metastore_id,
            owner=owner,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAwsIamRole")
    def put_aws_iam_role(self, *, role_arn: builtins.str) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#role_arn StorageCredential#role_arn}.
        '''
        value = StorageCredentialAwsIamRole(role_arn=role_arn)

        return typing.cast(None, jsii.invoke(self, "putAwsIamRole", [value]))

    @jsii.member(jsii_name="putAzureManagedIdentity")
    def put_azure_managed_identity(self, *, access_connector_id: builtins.str) -> None:
        '''
        :param access_connector_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#access_connector_id StorageCredential#access_connector_id}.
        '''
        value = StorageCredentialAzureManagedIdentity(
            access_connector_id=access_connector_id
        )

        return typing.cast(None, jsii.invoke(self, "putAzureManagedIdentity", [value]))

    @jsii.member(jsii_name="putAzureServicePrincipal")
    def put_azure_service_principal(
        self,
        *,
        application_id: builtins.str,
        client_secret: builtins.str,
        directory_id: builtins.str,
    ) -> None:
        '''
        :param application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#application_id StorageCredential#application_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#client_secret StorageCredential#client_secret}.
        :param directory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#directory_id StorageCredential#directory_id}.
        '''
        value = StorageCredentialAzureServicePrincipal(
            application_id=application_id,
            client_secret=client_secret,
            directory_id=directory_id,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureServicePrincipal", [value]))

    @jsii.member(jsii_name="putDatabricksGcpServiceAccount")
    def put_databricks_gcp_service_account(
        self,
        *,
        email: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#email StorageCredential#email}.
        '''
        value = StorageCredentialDatabricksGcpServiceAccount(email=email)

        return typing.cast(None, jsii.invoke(self, "putDatabricksGcpServiceAccount", [value]))

    @jsii.member(jsii_name="putGcpServiceAccountKey")
    def put_gcp_service_account_key(
        self,
        *,
        email: builtins.str,
        private_key: builtins.str,
        private_key_id: builtins.str,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#email StorageCredential#email}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#private_key StorageCredential#private_key}.
        :param private_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#private_key_id StorageCredential#private_key_id}.
        '''
        value = StorageCredentialGcpServiceAccountKey(
            email=email, private_key=private_key, private_key_id=private_key_id
        )

        return typing.cast(None, jsii.invoke(self, "putGcpServiceAccountKey", [value]))

    @jsii.member(jsii_name="resetAwsIamRole")
    def reset_aws_iam_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsIamRole", []))

    @jsii.member(jsii_name="resetAzureManagedIdentity")
    def reset_azure_managed_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureManagedIdentity", []))

    @jsii.member(jsii_name="resetAzureServicePrincipal")
    def reset_azure_service_principal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureServicePrincipal", []))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetDatabricksGcpServiceAccount")
    def reset_databricks_gcp_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabricksGcpServiceAccount", []))

    @jsii.member(jsii_name="resetGcpServiceAccountKey")
    def reset_gcp_service_account_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpServiceAccountKey", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMetastoreId")
    def reset_metastore_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetastoreId", []))

    @jsii.member(jsii_name="resetOwner")
    def reset_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwner", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="awsIamRole")
    def aws_iam_role(self) -> "StorageCredentialAwsIamRoleOutputReference":
        return typing.cast("StorageCredentialAwsIamRoleOutputReference", jsii.get(self, "awsIamRole"))

    @builtins.property
    @jsii.member(jsii_name="azureManagedIdentity")
    def azure_managed_identity(
        self,
    ) -> "StorageCredentialAzureManagedIdentityOutputReference":
        return typing.cast("StorageCredentialAzureManagedIdentityOutputReference", jsii.get(self, "azureManagedIdentity"))

    @builtins.property
    @jsii.member(jsii_name="azureServicePrincipal")
    def azure_service_principal(
        self,
    ) -> "StorageCredentialAzureServicePrincipalOutputReference":
        return typing.cast("StorageCredentialAzureServicePrincipalOutputReference", jsii.get(self, "azureServicePrincipal"))

    @builtins.property
    @jsii.member(jsii_name="databricksGcpServiceAccount")
    def databricks_gcp_service_account(
        self,
    ) -> "StorageCredentialDatabricksGcpServiceAccountOutputReference":
        return typing.cast("StorageCredentialDatabricksGcpServiceAccountOutputReference", jsii.get(self, "databricksGcpServiceAccount"))

    @builtins.property
    @jsii.member(jsii_name="gcpServiceAccountKey")
    def gcp_service_account_key(
        self,
    ) -> "StorageCredentialGcpServiceAccountKeyOutputReference":
        return typing.cast("StorageCredentialGcpServiceAccountKeyOutputReference", jsii.get(self, "gcpServiceAccountKey"))

    @builtins.property
    @jsii.member(jsii_name="awsIamRoleInput")
    def aws_iam_role_input(self) -> typing.Optional["StorageCredentialAwsIamRole"]:
        return typing.cast(typing.Optional["StorageCredentialAwsIamRole"], jsii.get(self, "awsIamRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="azureManagedIdentityInput")
    def azure_managed_identity_input(
        self,
    ) -> typing.Optional["StorageCredentialAzureManagedIdentity"]:
        return typing.cast(typing.Optional["StorageCredentialAzureManagedIdentity"], jsii.get(self, "azureManagedIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="azureServicePrincipalInput")
    def azure_service_principal_input(
        self,
    ) -> typing.Optional["StorageCredentialAzureServicePrincipal"]:
        return typing.cast(typing.Optional["StorageCredentialAzureServicePrincipal"], jsii.get(self, "azureServicePrincipalInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="databricksGcpServiceAccountInput")
    def databricks_gcp_service_account_input(
        self,
    ) -> typing.Optional["StorageCredentialDatabricksGcpServiceAccount"]:
        return typing.cast(typing.Optional["StorageCredentialDatabricksGcpServiceAccount"], jsii.get(self, "databricksGcpServiceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="gcpServiceAccountKeyInput")
    def gcp_service_account_key_input(
        self,
    ) -> typing.Optional["StorageCredentialGcpServiceAccountKey"]:
        return typing.cast(typing.Optional["StorageCredentialGcpServiceAccountKey"], jsii.get(self, "gcpServiceAccountKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metastoreIdInput")
    def metastore_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metastoreIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad715cb3a8db9fb83a8b58019c86b8400354156a6bd8bb70879d05b117312c24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e60ada9c5fc1253a3f02c85d8f4bbcedd3cc391e2a39f8c9758da6d8b34584b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="metastoreId")
    def metastore_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metastoreId"))

    @metastore_id.setter
    def metastore_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04f20d1e8c5308b848f2384e5b9e404a32cc42b90db949563d4e3b03695d69b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metastoreId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96365222c3aadbe22691c75f84eeeffacede2d7e6dcb93f64074ce5c4c64d6bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d0afe4b0bb91bee6284af91c598967eeef33b9e576c363725d03efb66314be3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)


@jsii.data_type(
    jsii_type="databricks.storageCredential.StorageCredentialAwsIamRole",
    jsii_struct_bases=[],
    name_mapping={"role_arn": "roleArn"},
)
class StorageCredentialAwsIamRole:
    def __init__(self, *, role_arn: builtins.str) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#role_arn StorageCredential#role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59bcbc9e3c3fc428c3051a9539759eff04a2041422fc34f5ee2c5f6a8e62ba0b)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
        }

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#role_arn StorageCredential#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCredentialAwsIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCredentialAwsIamRoleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.storageCredential.StorageCredentialAwsIamRoleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d59b9690d0d12d715b1c28cf6986c12cdac10010f95d383b9ad6e34b04ec2f9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a64b8000a46fd63794c26035bc8551c19412495fce8efe15a4ce76a8ccc91c1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageCredentialAwsIamRole]:
        return typing.cast(typing.Optional[StorageCredentialAwsIamRole], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageCredentialAwsIamRole],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec3ff9792823e83c44533f39d2a3cdfa19a241c55c7e419df5638dff07f4220b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.storageCredential.StorageCredentialAzureManagedIdentity",
    jsii_struct_bases=[],
    name_mapping={"access_connector_id": "accessConnectorId"},
)
class StorageCredentialAzureManagedIdentity:
    def __init__(self, *, access_connector_id: builtins.str) -> None:
        '''
        :param access_connector_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#access_connector_id StorageCredential#access_connector_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cda13050ac0d873dc7c39973c9782e58e7de8ce0ca58b7026bbca3b69e6418e)
            check_type(argname="argument access_connector_id", value=access_connector_id, expected_type=type_hints["access_connector_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_connector_id": access_connector_id,
        }

    @builtins.property
    def access_connector_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#access_connector_id StorageCredential#access_connector_id}.'''
        result = self._values.get("access_connector_id")
        assert result is not None, "Required property 'access_connector_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCredentialAzureManagedIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCredentialAzureManagedIdentityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.storageCredential.StorageCredentialAzureManagedIdentityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1d9b9ab1eabea5746495326cba099baefafe5a2d9017203011c8acc35c6b47a8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="accessConnectorIdInput")
    def access_connector_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessConnectorIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accessConnectorId")
    def access_connector_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessConnectorId"))

    @access_connector_id.setter
    def access_connector_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d1a603dd33c4f23ab3a9dc2559334fd6fbde41772bb9c2e0200a2eee6a119d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessConnectorId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageCredentialAzureManagedIdentity]:
        return typing.cast(typing.Optional[StorageCredentialAzureManagedIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageCredentialAzureManagedIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd0491d5e992f238e9f687486d8a2c9d0cbaac38840d53c98c2e3829db111182)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.storageCredential.StorageCredentialAzureServicePrincipal",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "client_secret": "clientSecret",
        "directory_id": "directoryId",
    },
)
class StorageCredentialAzureServicePrincipal:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        client_secret: builtins.str,
        directory_id: builtins.str,
    ) -> None:
        '''
        :param application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#application_id StorageCredential#application_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#client_secret StorageCredential#client_secret}.
        :param directory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#directory_id StorageCredential#directory_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ef1a2f1219e0a88155ed7f35576fc4464aa4794d8b38a03e311cafac475b962)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument directory_id", value=directory_id, expected_type=type_hints["directory_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "client_secret": client_secret,
            "directory_id": directory_id,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#application_id StorageCredential#application_id}.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#client_secret StorageCredential#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def directory_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#directory_id StorageCredential#directory_id}.'''
        result = self._values.get("directory_id")
        assert result is not None, "Required property 'directory_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCredentialAzureServicePrincipal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCredentialAzureServicePrincipalOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.storageCredential.StorageCredentialAzureServicePrincipalOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8142a6b9e2968aeee15ed4187aa65d604e48916754f78e7386996130524071e6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="applicationIdInput")
    def application_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryIdInput")
    def directory_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f641b4afdceeee4ccb834dd6e48c34ff0e2e5f55b28cc4b679952913ebf672c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__632e43c0877417625900a06fe1d8631ddd970d2a0cfd6dfafa5fe318f3a5b0b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="directoryId")
    def directory_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryId"))

    @directory_id.setter
    def directory_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3215047899e76f353ea90522f0fcc2592655a58ee04febe42c145d2ebedd7f1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageCredentialAzureServicePrincipal]:
        return typing.cast(typing.Optional[StorageCredentialAzureServicePrincipal], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageCredentialAzureServicePrincipal],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8e7062ed402d2c72ab4e42d934dab8f79f18efd969176e8ecc3862de29fa9ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.storageCredential.StorageCredentialConfig",
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
        "aws_iam_role": "awsIamRole",
        "azure_managed_identity": "azureManagedIdentity",
        "azure_service_principal": "azureServicePrincipal",
        "comment": "comment",
        "databricks_gcp_service_account": "databricksGcpServiceAccount",
        "gcp_service_account_key": "gcpServiceAccountKey",
        "id": "id",
        "metastore_id": "metastoreId",
        "owner": "owner",
    },
)
class StorageCredentialConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        aws_iam_role: typing.Optional[typing.Union[StorageCredentialAwsIamRole, typing.Dict[builtins.str, typing.Any]]] = None,
        azure_managed_identity: typing.Optional[typing.Union[StorageCredentialAzureManagedIdentity, typing.Dict[builtins.str, typing.Any]]] = None,
        azure_service_principal: typing.Optional[typing.Union[StorageCredentialAzureServicePrincipal, typing.Dict[builtins.str, typing.Any]]] = None,
        comment: typing.Optional[builtins.str] = None,
        databricks_gcp_service_account: typing.Optional[typing.Union["StorageCredentialDatabricksGcpServiceAccount", typing.Dict[builtins.str, typing.Any]]] = None,
        gcp_service_account_key: typing.Optional[typing.Union["StorageCredentialGcpServiceAccountKey", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        metastore_id: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#name StorageCredential#name}.
        :param aws_iam_role: aws_iam_role block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#aws_iam_role StorageCredential#aws_iam_role}
        :param azure_managed_identity: azure_managed_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#azure_managed_identity StorageCredential#azure_managed_identity}
        :param azure_service_principal: azure_service_principal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#azure_service_principal StorageCredential#azure_service_principal}
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#comment StorageCredential#comment}.
        :param databricks_gcp_service_account: databricks_gcp_service_account block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#databricks_gcp_service_account StorageCredential#databricks_gcp_service_account}
        :param gcp_service_account_key: gcp_service_account_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#gcp_service_account_key StorageCredential#gcp_service_account_key}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#id StorageCredential#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metastore_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#metastore_id StorageCredential#metastore_id}.
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#owner StorageCredential#owner}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(aws_iam_role, dict):
            aws_iam_role = StorageCredentialAwsIamRole(**aws_iam_role)
        if isinstance(azure_managed_identity, dict):
            azure_managed_identity = StorageCredentialAzureManagedIdentity(**azure_managed_identity)
        if isinstance(azure_service_principal, dict):
            azure_service_principal = StorageCredentialAzureServicePrincipal(**azure_service_principal)
        if isinstance(databricks_gcp_service_account, dict):
            databricks_gcp_service_account = StorageCredentialDatabricksGcpServiceAccount(**databricks_gcp_service_account)
        if isinstance(gcp_service_account_key, dict):
            gcp_service_account_key = StorageCredentialGcpServiceAccountKey(**gcp_service_account_key)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32b5ea82afc5f42c4fe9b1e7de86747b12de02dabda964a6858c6deedceef44b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument aws_iam_role", value=aws_iam_role, expected_type=type_hints["aws_iam_role"])
            check_type(argname="argument azure_managed_identity", value=azure_managed_identity, expected_type=type_hints["azure_managed_identity"])
            check_type(argname="argument azure_service_principal", value=azure_service_principal, expected_type=type_hints["azure_service_principal"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument databricks_gcp_service_account", value=databricks_gcp_service_account, expected_type=type_hints["databricks_gcp_service_account"])
            check_type(argname="argument gcp_service_account_key", value=gcp_service_account_key, expected_type=type_hints["gcp_service_account_key"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument metastore_id", value=metastore_id, expected_type=type_hints["metastore_id"])
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
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
        if aws_iam_role is not None:
            self._values["aws_iam_role"] = aws_iam_role
        if azure_managed_identity is not None:
            self._values["azure_managed_identity"] = azure_managed_identity
        if azure_service_principal is not None:
            self._values["azure_service_principal"] = azure_service_principal
        if comment is not None:
            self._values["comment"] = comment
        if databricks_gcp_service_account is not None:
            self._values["databricks_gcp_service_account"] = databricks_gcp_service_account
        if gcp_service_account_key is not None:
            self._values["gcp_service_account_key"] = gcp_service_account_key
        if id is not None:
            self._values["id"] = id
        if metastore_id is not None:
            self._values["metastore_id"] = metastore_id
        if owner is not None:
            self._values["owner"] = owner

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#name StorageCredential#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_iam_role(self) -> typing.Optional[StorageCredentialAwsIamRole]:
        '''aws_iam_role block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#aws_iam_role StorageCredential#aws_iam_role}
        '''
        result = self._values.get("aws_iam_role")
        return typing.cast(typing.Optional[StorageCredentialAwsIamRole], result)

    @builtins.property
    def azure_managed_identity(
        self,
    ) -> typing.Optional[StorageCredentialAzureManagedIdentity]:
        '''azure_managed_identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#azure_managed_identity StorageCredential#azure_managed_identity}
        '''
        result = self._values.get("azure_managed_identity")
        return typing.cast(typing.Optional[StorageCredentialAzureManagedIdentity], result)

    @builtins.property
    def azure_service_principal(
        self,
    ) -> typing.Optional[StorageCredentialAzureServicePrincipal]:
        '''azure_service_principal block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#azure_service_principal StorageCredential#azure_service_principal}
        '''
        result = self._values.get("azure_service_principal")
        return typing.cast(typing.Optional[StorageCredentialAzureServicePrincipal], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#comment StorageCredential#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def databricks_gcp_service_account(
        self,
    ) -> typing.Optional["StorageCredentialDatabricksGcpServiceAccount"]:
        '''databricks_gcp_service_account block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#databricks_gcp_service_account StorageCredential#databricks_gcp_service_account}
        '''
        result = self._values.get("databricks_gcp_service_account")
        return typing.cast(typing.Optional["StorageCredentialDatabricksGcpServiceAccount"], result)

    @builtins.property
    def gcp_service_account_key(
        self,
    ) -> typing.Optional["StorageCredentialGcpServiceAccountKey"]:
        '''gcp_service_account_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#gcp_service_account_key StorageCredential#gcp_service_account_key}
        '''
        result = self._values.get("gcp_service_account_key")
        return typing.cast(typing.Optional["StorageCredentialGcpServiceAccountKey"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#id StorageCredential#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metastore_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#metastore_id StorageCredential#metastore_id}.'''
        result = self._values.get("metastore_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#owner StorageCredential#owner}.'''
        result = self._values.get("owner")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCredentialConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.storageCredential.StorageCredentialDatabricksGcpServiceAccount",
    jsii_struct_bases=[],
    name_mapping={"email": "email"},
)
class StorageCredentialDatabricksGcpServiceAccount:
    def __init__(self, *, email: typing.Optional[builtins.str] = None) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#email StorageCredential#email}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3e6bb63b1654a615d1a14751942cccf5a5292477367540d61c17ee1b4428a0b)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if email is not None:
            self._values["email"] = email

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#email StorageCredential#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCredentialDatabricksGcpServiceAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCredentialDatabricksGcpServiceAccountOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.storageCredential.StorageCredentialDatabricksGcpServiceAccountOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a6dd4d330d9a7eea5c0f59ab558104607d241826be3272a938fbd835e27cbca)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75efa85635d27acf81513ddbe5cc114f0840047adc09eddf78e1cae3dfa6bc66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[StorageCredentialDatabricksGcpServiceAccount]:
        return typing.cast(typing.Optional[StorageCredentialDatabricksGcpServiceAccount], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageCredentialDatabricksGcpServiceAccount],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__594ab31312c8d13c61f4c2bc8e9e8c4e4f233721c3d025d55ecb524ed8108347)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.storageCredential.StorageCredentialGcpServiceAccountKey",
    jsii_struct_bases=[],
    name_mapping={
        "email": "email",
        "private_key": "privateKey",
        "private_key_id": "privateKeyId",
    },
)
class StorageCredentialGcpServiceAccountKey:
    def __init__(
        self,
        *,
        email: builtins.str,
        private_key: builtins.str,
        private_key_id: builtins.str,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#email StorageCredential#email}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#private_key StorageCredential#private_key}.
        :param private_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#private_key_id StorageCredential#private_key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c32419ec7219a62c630382690d3524621880445029c478159ad9945277a189d)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument private_key_id", value=private_key_id, expected_type=type_hints["private_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "email": email,
            "private_key": private_key,
            "private_key_id": private_key_id,
        }

    @builtins.property
    def email(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#email StorageCredential#email}.'''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#private_key StorageCredential#private_key}.'''
        result = self._values.get("private_key")
        assert result is not None, "Required property 'private_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_key_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/storage_credential#private_key_id StorageCredential#private_key_id}.'''
        result = self._values.get("private_key_id")
        assert result is not None, "Required property 'private_key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCredentialGcpServiceAccountKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCredentialGcpServiceAccountKeyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.storageCredential.StorageCredentialGcpServiceAccountKeyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ea796a89d3e16ded191f96c5de55b3a538e836961ecb62425832ff30555300d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyIdInput")
    def private_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyInput")
    def private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57458e085d167a18de25eab65bbb9f56c810d71d8848111c46d36eaafcd03687)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d506129c8bd1ef938172b58db6444a52cddc2e8800038a36336860fbd4caaeee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="privateKeyId")
    def private_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKeyId"))

    @private_key_id.setter
    def private_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86a7084dffb9e604c9bf7c2572c749addce57d413466105ae0e76e0f60fa5b09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageCredentialGcpServiceAccountKey]:
        return typing.cast(typing.Optional[StorageCredentialGcpServiceAccountKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[StorageCredentialGcpServiceAccountKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c46d658f8388f1aa781821398878517ef35d9506d146e539beb232b626574908)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StorageCredential",
    "StorageCredentialAwsIamRole",
    "StorageCredentialAwsIamRoleOutputReference",
    "StorageCredentialAzureManagedIdentity",
    "StorageCredentialAzureManagedIdentityOutputReference",
    "StorageCredentialAzureServicePrincipal",
    "StorageCredentialAzureServicePrincipalOutputReference",
    "StorageCredentialConfig",
    "StorageCredentialDatabricksGcpServiceAccount",
    "StorageCredentialDatabricksGcpServiceAccountOutputReference",
    "StorageCredentialGcpServiceAccountKey",
    "StorageCredentialGcpServiceAccountKeyOutputReference",
]

publication.publish()

def _typecheckingstub__cae7be342b20e51a499937993cb5957886bcf0a9775c8bb7c4b8650977735ee8(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    aws_iam_role: typing.Optional[typing.Union[StorageCredentialAwsIamRole, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_managed_identity: typing.Optional[typing.Union[StorageCredentialAzureManagedIdentity, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_service_principal: typing.Optional[typing.Union[StorageCredentialAzureServicePrincipal, typing.Dict[builtins.str, typing.Any]]] = None,
    comment: typing.Optional[builtins.str] = None,
    databricks_gcp_service_account: typing.Optional[typing.Union[StorageCredentialDatabricksGcpServiceAccount, typing.Dict[builtins.str, typing.Any]]] = None,
    gcp_service_account_key: typing.Optional[typing.Union[StorageCredentialGcpServiceAccountKey, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    metastore_id: typing.Optional[builtins.str] = None,
    owner: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__ad715cb3a8db9fb83a8b58019c86b8400354156a6bd8bb70879d05b117312c24(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e60ada9c5fc1253a3f02c85d8f4bbcedd3cc391e2a39f8c9758da6d8b34584b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04f20d1e8c5308b848f2384e5b9e404a32cc42b90db949563d4e3b03695d69b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96365222c3aadbe22691c75f84eeeffacede2d7e6dcb93f64074ce5c4c64d6bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d0afe4b0bb91bee6284af91c598967eeef33b9e576c363725d03efb66314be3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59bcbc9e3c3fc428c3051a9539759eff04a2041422fc34f5ee2c5f6a8e62ba0b(
    *,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d59b9690d0d12d715b1c28cf6986c12cdac10010f95d383b9ad6e34b04ec2f9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a64b8000a46fd63794c26035bc8551c19412495fce8efe15a4ce76a8ccc91c1d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec3ff9792823e83c44533f39d2a3cdfa19a241c55c7e419df5638dff07f4220b(
    value: typing.Optional[StorageCredentialAwsIamRole],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cda13050ac0d873dc7c39973c9782e58e7de8ce0ca58b7026bbca3b69e6418e(
    *,
    access_connector_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d9b9ab1eabea5746495326cba099baefafe5a2d9017203011c8acc35c6b47a8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d1a603dd33c4f23ab3a9dc2559334fd6fbde41772bb9c2e0200a2eee6a119d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd0491d5e992f238e9f687486d8a2c9d0cbaac38840d53c98c2e3829db111182(
    value: typing.Optional[StorageCredentialAzureManagedIdentity],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ef1a2f1219e0a88155ed7f35576fc4464aa4794d8b38a03e311cafac475b962(
    *,
    application_id: builtins.str,
    client_secret: builtins.str,
    directory_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8142a6b9e2968aeee15ed4187aa65d604e48916754f78e7386996130524071e6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f641b4afdceeee4ccb834dd6e48c34ff0e2e5f55b28cc4b679952913ebf672c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__632e43c0877417625900a06fe1d8631ddd970d2a0cfd6dfafa5fe318f3a5b0b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3215047899e76f353ea90522f0fcc2592655a58ee04febe42c145d2ebedd7f1a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8e7062ed402d2c72ab4e42d934dab8f79f18efd969176e8ecc3862de29fa9ab(
    value: typing.Optional[StorageCredentialAzureServicePrincipal],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b5ea82afc5f42c4fe9b1e7de86747b12de02dabda964a6858c6deedceef44b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    aws_iam_role: typing.Optional[typing.Union[StorageCredentialAwsIamRole, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_managed_identity: typing.Optional[typing.Union[StorageCredentialAzureManagedIdentity, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_service_principal: typing.Optional[typing.Union[StorageCredentialAzureServicePrincipal, typing.Dict[builtins.str, typing.Any]]] = None,
    comment: typing.Optional[builtins.str] = None,
    databricks_gcp_service_account: typing.Optional[typing.Union[StorageCredentialDatabricksGcpServiceAccount, typing.Dict[builtins.str, typing.Any]]] = None,
    gcp_service_account_key: typing.Optional[typing.Union[StorageCredentialGcpServiceAccountKey, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    metastore_id: typing.Optional[builtins.str] = None,
    owner: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3e6bb63b1654a615d1a14751942cccf5a5292477367540d61c17ee1b4428a0b(
    *,
    email: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a6dd4d330d9a7eea5c0f59ab558104607d241826be3272a938fbd835e27cbca(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75efa85635d27acf81513ddbe5cc114f0840047adc09eddf78e1cae3dfa6bc66(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__594ab31312c8d13c61f4c2bc8e9e8c4e4f233721c3d025d55ecb524ed8108347(
    value: typing.Optional[StorageCredentialDatabricksGcpServiceAccount],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c32419ec7219a62c630382690d3524621880445029c478159ad9945277a189d(
    *,
    email: builtins.str,
    private_key: builtins.str,
    private_key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ea796a89d3e16ded191f96c5de55b3a538e836961ecb62425832ff30555300d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57458e085d167a18de25eab65bbb9f56c810d71d8848111c46d36eaafcd03687(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d506129c8bd1ef938172b58db6444a52cddc2e8800038a36336860fbd4caaeee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86a7084dffb9e604c9bf7c2572c749addce57d413466105ae0e76e0f60fa5b09(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c46d658f8388f1aa781821398878517ef35d9506d146e539beb232b626574908(
    value: typing.Optional[StorageCredentialGcpServiceAccountKey],
) -> None:
    """Type checking stubs"""
    pass
