'''
# `databricks_metastore_data_access`

Refer to the Terraform Registory for docs: [`databricks_metastore_data_access`](https://www.terraform.io/docs/providers/databricks/r/metastore_data_access).
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


class MetastoreDataAccess(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.metastoreDataAccess.MetastoreDataAccess",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access databricks_metastore_data_access}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        metastore_id: builtins.str,
        name: builtins.str,
        aws_iam_role: typing.Optional[typing.Union["MetastoreDataAccessAwsIamRole", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_managed_identity: typing.Optional[typing.Union["MetastoreDataAccessAzureManagedIdentity", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_service_principal: typing.Optional[typing.Union["MetastoreDataAccessAzureServicePrincipal", typing.Dict[builtins.str, typing.Any]]] = None,
        configuration_type: typing.Optional[builtins.str] = None,
        databricks_gcp_service_account: typing.Optional[typing.Union["MetastoreDataAccessDatabricksGcpServiceAccount", typing.Dict[builtins.str, typing.Any]]] = None,
        gcp_service_account_key: typing.Optional[typing.Union["MetastoreDataAccessGcpServiceAccountKey", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access databricks_metastore_data_access} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metastore_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#metastore_id MetastoreDataAccess#metastore_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#name MetastoreDataAccess#name}.
        :param aws_iam_role: aws_iam_role block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#aws_iam_role MetastoreDataAccess#aws_iam_role}
        :param azure_managed_identity: azure_managed_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#azure_managed_identity MetastoreDataAccess#azure_managed_identity}
        :param azure_service_principal: azure_service_principal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#azure_service_principal MetastoreDataAccess#azure_service_principal}
        :param configuration_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#configuration_type MetastoreDataAccess#configuration_type}.
        :param databricks_gcp_service_account: databricks_gcp_service_account block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#databricks_gcp_service_account MetastoreDataAccess#databricks_gcp_service_account}
        :param gcp_service_account_key: gcp_service_account_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#gcp_service_account_key MetastoreDataAccess#gcp_service_account_key}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#id MetastoreDataAccess#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#is_default MetastoreDataAccess#is_default}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00619eba18a2193a3ce821e95c31efe5a492fef13eb1eb3a2746deb4a2c87604)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MetastoreDataAccessConfig(
            metastore_id=metastore_id,
            name=name,
            aws_iam_role=aws_iam_role,
            azure_managed_identity=azure_managed_identity,
            azure_service_principal=azure_service_principal,
            configuration_type=configuration_type,
            databricks_gcp_service_account=databricks_gcp_service_account,
            gcp_service_account_key=gcp_service_account_key,
            id=id,
            is_default=is_default,
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
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#role_arn MetastoreDataAccess#role_arn}.
        '''
        value = MetastoreDataAccessAwsIamRole(role_arn=role_arn)

        return typing.cast(None, jsii.invoke(self, "putAwsIamRole", [value]))

    @jsii.member(jsii_name="putAzureManagedIdentity")
    def put_azure_managed_identity(self, *, access_connector_id: builtins.str) -> None:
        '''
        :param access_connector_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#access_connector_id MetastoreDataAccess#access_connector_id}.
        '''
        value = MetastoreDataAccessAzureManagedIdentity(
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
        :param application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#application_id MetastoreDataAccess#application_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#client_secret MetastoreDataAccess#client_secret}.
        :param directory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#directory_id MetastoreDataAccess#directory_id}.
        '''
        value = MetastoreDataAccessAzureServicePrincipal(
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
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#email MetastoreDataAccess#email}.
        '''
        value = MetastoreDataAccessDatabricksGcpServiceAccount(email=email)

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
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#email MetastoreDataAccess#email}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#private_key MetastoreDataAccess#private_key}.
        :param private_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#private_key_id MetastoreDataAccess#private_key_id}.
        '''
        value = MetastoreDataAccessGcpServiceAccountKey(
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

    @jsii.member(jsii_name="resetConfigurationType")
    def reset_configuration_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurationType", []))

    @jsii.member(jsii_name="resetDatabricksGcpServiceAccount")
    def reset_databricks_gcp_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabricksGcpServiceAccount", []))

    @jsii.member(jsii_name="resetGcpServiceAccountKey")
    def reset_gcp_service_account_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpServiceAccountKey", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsDefault")
    def reset_is_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsDefault", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="awsIamRole")
    def aws_iam_role(self) -> "MetastoreDataAccessAwsIamRoleOutputReference":
        return typing.cast("MetastoreDataAccessAwsIamRoleOutputReference", jsii.get(self, "awsIamRole"))

    @builtins.property
    @jsii.member(jsii_name="azureManagedIdentity")
    def azure_managed_identity(
        self,
    ) -> "MetastoreDataAccessAzureManagedIdentityOutputReference":
        return typing.cast("MetastoreDataAccessAzureManagedIdentityOutputReference", jsii.get(self, "azureManagedIdentity"))

    @builtins.property
    @jsii.member(jsii_name="azureServicePrincipal")
    def azure_service_principal(
        self,
    ) -> "MetastoreDataAccessAzureServicePrincipalOutputReference":
        return typing.cast("MetastoreDataAccessAzureServicePrincipalOutputReference", jsii.get(self, "azureServicePrincipal"))

    @builtins.property
    @jsii.member(jsii_name="databricksGcpServiceAccount")
    def databricks_gcp_service_account(
        self,
    ) -> "MetastoreDataAccessDatabricksGcpServiceAccountOutputReference":
        return typing.cast("MetastoreDataAccessDatabricksGcpServiceAccountOutputReference", jsii.get(self, "databricksGcpServiceAccount"))

    @builtins.property
    @jsii.member(jsii_name="gcpServiceAccountKey")
    def gcp_service_account_key(
        self,
    ) -> "MetastoreDataAccessGcpServiceAccountKeyOutputReference":
        return typing.cast("MetastoreDataAccessGcpServiceAccountKeyOutputReference", jsii.get(self, "gcpServiceAccountKey"))

    @builtins.property
    @jsii.member(jsii_name="awsIamRoleInput")
    def aws_iam_role_input(self) -> typing.Optional["MetastoreDataAccessAwsIamRole"]:
        return typing.cast(typing.Optional["MetastoreDataAccessAwsIamRole"], jsii.get(self, "awsIamRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="azureManagedIdentityInput")
    def azure_managed_identity_input(
        self,
    ) -> typing.Optional["MetastoreDataAccessAzureManagedIdentity"]:
        return typing.cast(typing.Optional["MetastoreDataAccessAzureManagedIdentity"], jsii.get(self, "azureManagedIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="azureServicePrincipalInput")
    def azure_service_principal_input(
        self,
    ) -> typing.Optional["MetastoreDataAccessAzureServicePrincipal"]:
        return typing.cast(typing.Optional["MetastoreDataAccessAzureServicePrincipal"], jsii.get(self, "azureServicePrincipalInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationTypeInput")
    def configuration_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="databricksGcpServiceAccountInput")
    def databricks_gcp_service_account_input(
        self,
    ) -> typing.Optional["MetastoreDataAccessDatabricksGcpServiceAccount"]:
        return typing.cast(typing.Optional["MetastoreDataAccessDatabricksGcpServiceAccount"], jsii.get(self, "databricksGcpServiceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="gcpServiceAccountKeyInput")
    def gcp_service_account_key_input(
        self,
    ) -> typing.Optional["MetastoreDataAccessGcpServiceAccountKey"]:
        return typing.cast(typing.Optional["MetastoreDataAccessGcpServiceAccountKey"], jsii.get(self, "gcpServiceAccountKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isDefaultInput")
    def is_default_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "isDefaultInput"))

    @builtins.property
    @jsii.member(jsii_name="metastoreIdInput")
    def metastore_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metastoreIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationType")
    def configuration_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configurationType"))

    @configuration_type.setter
    def configuration_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50eddf43ad439760cab3384c66bef8bcfebc661369aa396e7229ba78f9fb117b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5337bda326da7b1cc0fb840dc1ada6797d5c7a55d82a605b2f9da732e0ecee7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isDefault")
    def is_default(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "isDefault"))

    @is_default.setter
    def is_default(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c00e5195bd438e5f19053aca1753ec72aaa254d6dd9a2c0694fd2f0edb918a99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isDefault", value)

    @builtins.property
    @jsii.member(jsii_name="metastoreId")
    def metastore_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metastoreId"))

    @metastore_id.setter
    def metastore_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__263a596dfacbb359e85003d02946b0710a1738cfab84b5c0acc550791a4cdbe2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metastoreId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5707a13b4a27920defe7369a649da09111c755ecee4851348e9fba3671c29f45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="databricks.metastoreDataAccess.MetastoreDataAccessAwsIamRole",
    jsii_struct_bases=[],
    name_mapping={"role_arn": "roleArn"},
)
class MetastoreDataAccessAwsIamRole:
    def __init__(self, *, role_arn: builtins.str) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#role_arn MetastoreDataAccess#role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e22b1447167d2e7c8cff52ad148fab5a0a204c495168a5b27d3f4c83528a5d4f)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
        }

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#role_arn MetastoreDataAccess#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetastoreDataAccessAwsIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MetastoreDataAccessAwsIamRoleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.metastoreDataAccess.MetastoreDataAccessAwsIamRoleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__777b2c57ff3358ff1671179ab7f3230e2a725f31ef848180891d6ce8d83c3733)
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
            type_hints = typing.get_type_hints(_typecheckingstub__26893b262e96c4d612cb58499a4cd3e3b1dae29f9b1f3f4e0a0722117327f9b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MetastoreDataAccessAwsIamRole]:
        return typing.cast(typing.Optional[MetastoreDataAccessAwsIamRole], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MetastoreDataAccessAwsIamRole],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9529a9eb74452b0792ae99a4ed5ab95a09c25f7c0104a15920c46b8bfa058e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.metastoreDataAccess.MetastoreDataAccessAzureManagedIdentity",
    jsii_struct_bases=[],
    name_mapping={"access_connector_id": "accessConnectorId"},
)
class MetastoreDataAccessAzureManagedIdentity:
    def __init__(self, *, access_connector_id: builtins.str) -> None:
        '''
        :param access_connector_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#access_connector_id MetastoreDataAccess#access_connector_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f12cca1e2281ea9fff5589f860632ae37ed15ddc4ad3af79295e5cfe61d75d4d)
            check_type(argname="argument access_connector_id", value=access_connector_id, expected_type=type_hints["access_connector_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_connector_id": access_connector_id,
        }

    @builtins.property
    def access_connector_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#access_connector_id MetastoreDataAccess#access_connector_id}.'''
        result = self._values.get("access_connector_id")
        assert result is not None, "Required property 'access_connector_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetastoreDataAccessAzureManagedIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MetastoreDataAccessAzureManagedIdentityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.metastoreDataAccess.MetastoreDataAccessAzureManagedIdentityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dda36ba7af45592c5cd07911d6c024cec2cc7f18e1ab40faf57b5fa753a41d73)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4971028d7f8812d3ca056b835f560cc42d5fc1bbf4c4428047231a441ede6ddb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessConnectorId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MetastoreDataAccessAzureManagedIdentity]:
        return typing.cast(typing.Optional[MetastoreDataAccessAzureManagedIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MetastoreDataAccessAzureManagedIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee57ec32fd9b258b5c845068f4fe58b52b3b80ea008c5cf3e39b72307edd3be0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.metastoreDataAccess.MetastoreDataAccessAzureServicePrincipal",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "client_secret": "clientSecret",
        "directory_id": "directoryId",
    },
)
class MetastoreDataAccessAzureServicePrincipal:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        client_secret: builtins.str,
        directory_id: builtins.str,
    ) -> None:
        '''
        :param application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#application_id MetastoreDataAccess#application_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#client_secret MetastoreDataAccess#client_secret}.
        :param directory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#directory_id MetastoreDataAccess#directory_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f05b60d8f88a6410a5595ea352a56e1b8d1125ae9b17acb43ce910eebd9a511d)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#application_id MetastoreDataAccess#application_id}.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#client_secret MetastoreDataAccess#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def directory_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#directory_id MetastoreDataAccess#directory_id}.'''
        result = self._values.get("directory_id")
        assert result is not None, "Required property 'directory_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetastoreDataAccessAzureServicePrincipal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MetastoreDataAccessAzureServicePrincipalOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.metastoreDataAccess.MetastoreDataAccessAzureServicePrincipalOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d17537008c469b674a9b6878df81f9afe6dd3401e8669590549220fce1ccd7ad)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a77338ce72b38991b4b7f67bb8fe96b74b1f03ebda5e37c3c8fd31dba23bac5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60a33e69371ec34ba24fbb14a757ea9f4fe8806cab124fa084cef7226302a2f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="directoryId")
    def directory_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryId"))

    @directory_id.setter
    def directory_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__109ab5707028fd2f5df28fa8643cc2af9d7c9adfaebcf1f2338fc2cb21598a78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MetastoreDataAccessAzureServicePrincipal]:
        return typing.cast(typing.Optional[MetastoreDataAccessAzureServicePrincipal], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MetastoreDataAccessAzureServicePrincipal],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa9035a9d04464ac28108f1a98d340c83af86bb66f1f122d3e04f6b17461879d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.metastoreDataAccess.MetastoreDataAccessConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "metastore_id": "metastoreId",
        "name": "name",
        "aws_iam_role": "awsIamRole",
        "azure_managed_identity": "azureManagedIdentity",
        "azure_service_principal": "azureServicePrincipal",
        "configuration_type": "configurationType",
        "databricks_gcp_service_account": "databricksGcpServiceAccount",
        "gcp_service_account_key": "gcpServiceAccountKey",
        "id": "id",
        "is_default": "isDefault",
    },
)
class MetastoreDataAccessConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        metastore_id: builtins.str,
        name: builtins.str,
        aws_iam_role: typing.Optional[typing.Union[MetastoreDataAccessAwsIamRole, typing.Dict[builtins.str, typing.Any]]] = None,
        azure_managed_identity: typing.Optional[typing.Union[MetastoreDataAccessAzureManagedIdentity, typing.Dict[builtins.str, typing.Any]]] = None,
        azure_service_principal: typing.Optional[typing.Union[MetastoreDataAccessAzureServicePrincipal, typing.Dict[builtins.str, typing.Any]]] = None,
        configuration_type: typing.Optional[builtins.str] = None,
        databricks_gcp_service_account: typing.Optional[typing.Union["MetastoreDataAccessDatabricksGcpServiceAccount", typing.Dict[builtins.str, typing.Any]]] = None,
        gcp_service_account_key: typing.Optional[typing.Union["MetastoreDataAccessGcpServiceAccountKey", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metastore_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#metastore_id MetastoreDataAccess#metastore_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#name MetastoreDataAccess#name}.
        :param aws_iam_role: aws_iam_role block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#aws_iam_role MetastoreDataAccess#aws_iam_role}
        :param azure_managed_identity: azure_managed_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#azure_managed_identity MetastoreDataAccess#azure_managed_identity}
        :param azure_service_principal: azure_service_principal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#azure_service_principal MetastoreDataAccess#azure_service_principal}
        :param configuration_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#configuration_type MetastoreDataAccess#configuration_type}.
        :param databricks_gcp_service_account: databricks_gcp_service_account block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#databricks_gcp_service_account MetastoreDataAccess#databricks_gcp_service_account}
        :param gcp_service_account_key: gcp_service_account_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#gcp_service_account_key MetastoreDataAccess#gcp_service_account_key}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#id MetastoreDataAccess#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#is_default MetastoreDataAccess#is_default}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(aws_iam_role, dict):
            aws_iam_role = MetastoreDataAccessAwsIamRole(**aws_iam_role)
        if isinstance(azure_managed_identity, dict):
            azure_managed_identity = MetastoreDataAccessAzureManagedIdentity(**azure_managed_identity)
        if isinstance(azure_service_principal, dict):
            azure_service_principal = MetastoreDataAccessAzureServicePrincipal(**azure_service_principal)
        if isinstance(databricks_gcp_service_account, dict):
            databricks_gcp_service_account = MetastoreDataAccessDatabricksGcpServiceAccount(**databricks_gcp_service_account)
        if isinstance(gcp_service_account_key, dict):
            gcp_service_account_key = MetastoreDataAccessGcpServiceAccountKey(**gcp_service_account_key)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e319cec17b8a13eec7d178c0e24eaa89b0f56b1a4da9df07332bdf88dcff3642)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metastore_id", value=metastore_id, expected_type=type_hints["metastore_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument aws_iam_role", value=aws_iam_role, expected_type=type_hints["aws_iam_role"])
            check_type(argname="argument azure_managed_identity", value=azure_managed_identity, expected_type=type_hints["azure_managed_identity"])
            check_type(argname="argument azure_service_principal", value=azure_service_principal, expected_type=type_hints["azure_service_principal"])
            check_type(argname="argument configuration_type", value=configuration_type, expected_type=type_hints["configuration_type"])
            check_type(argname="argument databricks_gcp_service_account", value=databricks_gcp_service_account, expected_type=type_hints["databricks_gcp_service_account"])
            check_type(argname="argument gcp_service_account_key", value=gcp_service_account_key, expected_type=type_hints["gcp_service_account_key"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_default", value=is_default, expected_type=type_hints["is_default"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metastore_id": metastore_id,
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
        if configuration_type is not None:
            self._values["configuration_type"] = configuration_type
        if databricks_gcp_service_account is not None:
            self._values["databricks_gcp_service_account"] = databricks_gcp_service_account
        if gcp_service_account_key is not None:
            self._values["gcp_service_account_key"] = gcp_service_account_key
        if id is not None:
            self._values["id"] = id
        if is_default is not None:
            self._values["is_default"] = is_default

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
    def metastore_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#metastore_id MetastoreDataAccess#metastore_id}.'''
        result = self._values.get("metastore_id")
        assert result is not None, "Required property 'metastore_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#name MetastoreDataAccess#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_iam_role(self) -> typing.Optional[MetastoreDataAccessAwsIamRole]:
        '''aws_iam_role block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#aws_iam_role MetastoreDataAccess#aws_iam_role}
        '''
        result = self._values.get("aws_iam_role")
        return typing.cast(typing.Optional[MetastoreDataAccessAwsIamRole], result)

    @builtins.property
    def azure_managed_identity(
        self,
    ) -> typing.Optional[MetastoreDataAccessAzureManagedIdentity]:
        '''azure_managed_identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#azure_managed_identity MetastoreDataAccess#azure_managed_identity}
        '''
        result = self._values.get("azure_managed_identity")
        return typing.cast(typing.Optional[MetastoreDataAccessAzureManagedIdentity], result)

    @builtins.property
    def azure_service_principal(
        self,
    ) -> typing.Optional[MetastoreDataAccessAzureServicePrincipal]:
        '''azure_service_principal block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#azure_service_principal MetastoreDataAccess#azure_service_principal}
        '''
        result = self._values.get("azure_service_principal")
        return typing.cast(typing.Optional[MetastoreDataAccessAzureServicePrincipal], result)

    @builtins.property
    def configuration_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#configuration_type MetastoreDataAccess#configuration_type}.'''
        result = self._values.get("configuration_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def databricks_gcp_service_account(
        self,
    ) -> typing.Optional["MetastoreDataAccessDatabricksGcpServiceAccount"]:
        '''databricks_gcp_service_account block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#databricks_gcp_service_account MetastoreDataAccess#databricks_gcp_service_account}
        '''
        result = self._values.get("databricks_gcp_service_account")
        return typing.cast(typing.Optional["MetastoreDataAccessDatabricksGcpServiceAccount"], result)

    @builtins.property
    def gcp_service_account_key(
        self,
    ) -> typing.Optional["MetastoreDataAccessGcpServiceAccountKey"]:
        '''gcp_service_account_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#gcp_service_account_key MetastoreDataAccess#gcp_service_account_key}
        '''
        result = self._values.get("gcp_service_account_key")
        return typing.cast(typing.Optional["MetastoreDataAccessGcpServiceAccountKey"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#id MetastoreDataAccess#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_default(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#is_default MetastoreDataAccess#is_default}.'''
        result = self._values.get("is_default")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetastoreDataAccessConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.metastoreDataAccess.MetastoreDataAccessDatabricksGcpServiceAccount",
    jsii_struct_bases=[],
    name_mapping={"email": "email"},
)
class MetastoreDataAccessDatabricksGcpServiceAccount:
    def __init__(self, *, email: typing.Optional[builtins.str] = None) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#email MetastoreDataAccess#email}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__974b239ccb99dc09bfddb8c77d540e45ec7d4e9be6c9124554a44166544ab545)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if email is not None:
            self._values["email"] = email

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#email MetastoreDataAccess#email}.'''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetastoreDataAccessDatabricksGcpServiceAccount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MetastoreDataAccessDatabricksGcpServiceAccountOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.metastoreDataAccess.MetastoreDataAccessDatabricksGcpServiceAccountOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd55ba85cc9dd97dae08c4e1a9c0a2ade38b786bdfd0d87fbe1b3adab61f0650)
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
            type_hints = typing.get_type_hints(_typecheckingstub__444b91a6d6185bb597f513f568c7ab1622c5cc1527503ef98828f217920ffff4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MetastoreDataAccessDatabricksGcpServiceAccount]:
        return typing.cast(typing.Optional[MetastoreDataAccessDatabricksGcpServiceAccount], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MetastoreDataAccessDatabricksGcpServiceAccount],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b2ab416f038229d865f473cc720de0c8f80aa78c80f32a72a0338ee488dcdec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.metastoreDataAccess.MetastoreDataAccessGcpServiceAccountKey",
    jsii_struct_bases=[],
    name_mapping={
        "email": "email",
        "private_key": "privateKey",
        "private_key_id": "privateKeyId",
    },
)
class MetastoreDataAccessGcpServiceAccountKey:
    def __init__(
        self,
        *,
        email: builtins.str,
        private_key: builtins.str,
        private_key_id: builtins.str,
    ) -> None:
        '''
        :param email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#email MetastoreDataAccess#email}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#private_key MetastoreDataAccess#private_key}.
        :param private_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#private_key_id MetastoreDataAccess#private_key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99f993eb4d58a99b0d821e00638d0bde6af4f0573d1fae88d7c3267341cc545d)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#email MetastoreDataAccess#email}.'''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#private_key MetastoreDataAccess#private_key}.'''
        result = self._values.get("private_key")
        assert result is not None, "Required property 'private_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_key_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#private_key_id MetastoreDataAccess#private_key_id}.'''
        result = self._values.get("private_key_id")
        assert result is not None, "Required property 'private_key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetastoreDataAccessGcpServiceAccountKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MetastoreDataAccessGcpServiceAccountKeyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.metastoreDataAccess.MetastoreDataAccessGcpServiceAccountKeyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4ccaf07649331c0452dacd9bb2a7f38198b189e162d0f40622e7babd1d5c8c0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7eda7ad68c6fed07656b09ebdc4f90eed645ad17ba7330cec443b8288461028)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fe3f786618cef86d08a431cfd79175628c18756d46a5f871e74a0d9e3bb5553)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="privateKeyId")
    def private_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKeyId"))

    @private_key_id.setter
    def private_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c99facbaaa9b529d9064a2306625cc21b3e2821aa23eb6090121b8bc603ce5d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MetastoreDataAccessGcpServiceAccountKey]:
        return typing.cast(typing.Optional[MetastoreDataAccessGcpServiceAccountKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MetastoreDataAccessGcpServiceAccountKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__643562fad46533f6e656a9bde4e0d353dc2fb49adc93672c5cf1bbd480b5f57d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MetastoreDataAccess",
    "MetastoreDataAccessAwsIamRole",
    "MetastoreDataAccessAwsIamRoleOutputReference",
    "MetastoreDataAccessAzureManagedIdentity",
    "MetastoreDataAccessAzureManagedIdentityOutputReference",
    "MetastoreDataAccessAzureServicePrincipal",
    "MetastoreDataAccessAzureServicePrincipalOutputReference",
    "MetastoreDataAccessConfig",
    "MetastoreDataAccessDatabricksGcpServiceAccount",
    "MetastoreDataAccessDatabricksGcpServiceAccountOutputReference",
    "MetastoreDataAccessGcpServiceAccountKey",
    "MetastoreDataAccessGcpServiceAccountKeyOutputReference",
]

publication.publish()

def _typecheckingstub__00619eba18a2193a3ce821e95c31efe5a492fef13eb1eb3a2746deb4a2c87604(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    metastore_id: builtins.str,
    name: builtins.str,
    aws_iam_role: typing.Optional[typing.Union[MetastoreDataAccessAwsIamRole, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_managed_identity: typing.Optional[typing.Union[MetastoreDataAccessAzureManagedIdentity, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_service_principal: typing.Optional[typing.Union[MetastoreDataAccessAzureServicePrincipal, typing.Dict[builtins.str, typing.Any]]] = None,
    configuration_type: typing.Optional[builtins.str] = None,
    databricks_gcp_service_account: typing.Optional[typing.Union[MetastoreDataAccessDatabricksGcpServiceAccount, typing.Dict[builtins.str, typing.Any]]] = None,
    gcp_service_account_key: typing.Optional[typing.Union[MetastoreDataAccessGcpServiceAccountKey, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__50eddf43ad439760cab3384c66bef8bcfebc661369aa396e7229ba78f9fb117b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5337bda326da7b1cc0fb840dc1ada6797d5c7a55d82a605b2f9da732e0ecee7a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c00e5195bd438e5f19053aca1753ec72aaa254d6dd9a2c0694fd2f0edb918a99(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__263a596dfacbb359e85003d02946b0710a1738cfab84b5c0acc550791a4cdbe2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5707a13b4a27920defe7369a649da09111c755ecee4851348e9fba3671c29f45(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e22b1447167d2e7c8cff52ad148fab5a0a204c495168a5b27d3f4c83528a5d4f(
    *,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__777b2c57ff3358ff1671179ab7f3230e2a725f31ef848180891d6ce8d83c3733(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26893b262e96c4d612cb58499a4cd3e3b1dae29f9b1f3f4e0a0722117327f9b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9529a9eb74452b0792ae99a4ed5ab95a09c25f7c0104a15920c46b8bfa058e3(
    value: typing.Optional[MetastoreDataAccessAwsIamRole],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f12cca1e2281ea9fff5589f860632ae37ed15ddc4ad3af79295e5cfe61d75d4d(
    *,
    access_connector_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dda36ba7af45592c5cd07911d6c024cec2cc7f18e1ab40faf57b5fa753a41d73(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4971028d7f8812d3ca056b835f560cc42d5fc1bbf4c4428047231a441ede6ddb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee57ec32fd9b258b5c845068f4fe58b52b3b80ea008c5cf3e39b72307edd3be0(
    value: typing.Optional[MetastoreDataAccessAzureManagedIdentity],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f05b60d8f88a6410a5595ea352a56e1b8d1125ae9b17acb43ce910eebd9a511d(
    *,
    application_id: builtins.str,
    client_secret: builtins.str,
    directory_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d17537008c469b674a9b6878df81f9afe6dd3401e8669590549220fce1ccd7ad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a77338ce72b38991b4b7f67bb8fe96b74b1f03ebda5e37c3c8fd31dba23bac5c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60a33e69371ec34ba24fbb14a757ea9f4fe8806cab124fa084cef7226302a2f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__109ab5707028fd2f5df28fa8643cc2af9d7c9adfaebcf1f2338fc2cb21598a78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa9035a9d04464ac28108f1a98d340c83af86bb66f1f122d3e04f6b17461879d(
    value: typing.Optional[MetastoreDataAccessAzureServicePrincipal],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e319cec17b8a13eec7d178c0e24eaa89b0f56b1a4da9df07332bdf88dcff3642(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metastore_id: builtins.str,
    name: builtins.str,
    aws_iam_role: typing.Optional[typing.Union[MetastoreDataAccessAwsIamRole, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_managed_identity: typing.Optional[typing.Union[MetastoreDataAccessAzureManagedIdentity, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_service_principal: typing.Optional[typing.Union[MetastoreDataAccessAzureServicePrincipal, typing.Dict[builtins.str, typing.Any]]] = None,
    configuration_type: typing.Optional[builtins.str] = None,
    databricks_gcp_service_account: typing.Optional[typing.Union[MetastoreDataAccessDatabricksGcpServiceAccount, typing.Dict[builtins.str, typing.Any]]] = None,
    gcp_service_account_key: typing.Optional[typing.Union[MetastoreDataAccessGcpServiceAccountKey, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__974b239ccb99dc09bfddb8c77d540e45ec7d4e9be6c9124554a44166544ab545(
    *,
    email: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd55ba85cc9dd97dae08c4e1a9c0a2ade38b786bdfd0d87fbe1b3adab61f0650(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__444b91a6d6185bb597f513f568c7ab1622c5cc1527503ef98828f217920ffff4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b2ab416f038229d865f473cc720de0c8f80aa78c80f32a72a0338ee488dcdec(
    value: typing.Optional[MetastoreDataAccessDatabricksGcpServiceAccount],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99f993eb4d58a99b0d821e00638d0bde6af4f0573d1fae88d7c3267341cc545d(
    *,
    email: builtins.str,
    private_key: builtins.str,
    private_key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4ccaf07649331c0452dacd9bb2a7f38198b189e162d0f40622e7babd1d5c8c0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7eda7ad68c6fed07656b09ebdc4f90eed645ad17ba7330cec443b8288461028(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fe3f786618cef86d08a431cfd79175628c18756d46a5f871e74a0d9e3bb5553(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c99facbaaa9b529d9064a2306625cc21b3e2821aa23eb6090121b8bc603ce5d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__643562fad46533f6e656a9bde4e0d353dc2fb49adc93672c5cf1bbd480b5f57d(
    value: typing.Optional[MetastoreDataAccessGcpServiceAccountKey],
) -> None:
    """Type checking stubs"""
    pass
