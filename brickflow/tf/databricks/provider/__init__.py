'''
# `provider`

Refer to the Terraform Registory for docs: [`databricks`](https://www.terraform.io/docs/providers/databricks).
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


class DatabricksProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.provider.DatabricksProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks databricks}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        account_id: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        auth_type: typing.Optional[builtins.str] = None,
        azure_client_id: typing.Optional[builtins.str] = None,
        azure_client_secret: typing.Optional[builtins.str] = None,
        azure_environment: typing.Optional[builtins.str] = None,
        azure_login_app_id: typing.Optional[builtins.str] = None,
        azure_tenant_id: typing.Optional[builtins.str] = None,
        azure_use_msi: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        azure_workspace_resource_id: typing.Optional[builtins.str] = None,
        bricks_cli_path: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        config_file: typing.Optional[builtins.str] = None,
        debug_headers: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        debug_truncate_bytes: typing.Optional[jsii.Number] = None,
        google_credentials: typing.Optional[builtins.str] = None,
        google_service_account: typing.Optional[builtins.str] = None,
        host: typing.Optional[builtins.str] = None,
        http_timeout_seconds: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        rate_limit: typing.Optional[jsii.Number] = None,
        retry_timeout_seconds: typing.Optional[jsii.Number] = None,
        skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        token: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks databricks} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#account_id DatabricksProvider#account_id}.
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#alias DatabricksProvider#alias}
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#auth_type DatabricksProvider#auth_type}.
        :param azure_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_client_id DatabricksProvider#azure_client_id}.
        :param azure_client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_client_secret DatabricksProvider#azure_client_secret}.
        :param azure_environment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_environment DatabricksProvider#azure_environment}.
        :param azure_login_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_login_app_id DatabricksProvider#azure_login_app_id}.
        :param azure_tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_tenant_id DatabricksProvider#azure_tenant_id}.
        :param azure_use_msi: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_use_msi DatabricksProvider#azure_use_msi}.
        :param azure_workspace_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_workspace_resource_id DatabricksProvider#azure_workspace_resource_id}.
        :param bricks_cli_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#bricks_cli_path DatabricksProvider#bricks_cli_path}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#client_id DatabricksProvider#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#client_secret DatabricksProvider#client_secret}.
        :param config_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#config_file DatabricksProvider#config_file}.
        :param debug_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#debug_headers DatabricksProvider#debug_headers}.
        :param debug_truncate_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#debug_truncate_bytes DatabricksProvider#debug_truncate_bytes}.
        :param google_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#google_credentials DatabricksProvider#google_credentials}.
        :param google_service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#google_service_account DatabricksProvider#google_service_account}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#host DatabricksProvider#host}.
        :param http_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#http_timeout_seconds DatabricksProvider#http_timeout_seconds}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#password DatabricksProvider#password}.
        :param profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#profile DatabricksProvider#profile}.
        :param rate_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#rate_limit DatabricksProvider#rate_limit}.
        :param retry_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#retry_timeout_seconds DatabricksProvider#retry_timeout_seconds}.
        :param skip_verify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#skip_verify DatabricksProvider#skip_verify}.
        :param token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#token DatabricksProvider#token}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#username DatabricksProvider#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__083fa990793980cc648331b1283a7a29e2cac0c0a6717a4d7bac2f31b229c795)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DatabricksProviderConfig(
            account_id=account_id,
            alias=alias,
            auth_type=auth_type,
            azure_client_id=azure_client_id,
            azure_client_secret=azure_client_secret,
            azure_environment=azure_environment,
            azure_login_app_id=azure_login_app_id,
            azure_tenant_id=azure_tenant_id,
            azure_use_msi=azure_use_msi,
            azure_workspace_resource_id=azure_workspace_resource_id,
            bricks_cli_path=bricks_cli_path,
            client_id=client_id,
            client_secret=client_secret,
            config_file=config_file,
            debug_headers=debug_headers,
            debug_truncate_bytes=debug_truncate_bytes,
            google_credentials=google_credentials,
            google_service_account=google_service_account,
            host=host,
            http_timeout_seconds=http_timeout_seconds,
            password=password,
            profile=profile,
            rate_limit=rate_limit,
            retry_timeout_seconds=retry_timeout_seconds,
            skip_verify=skip_verify,
            token=token,
            username=username,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetAuthType")
    def reset_auth_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthType", []))

    @jsii.member(jsii_name="resetAzureClientId")
    def reset_azure_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureClientId", []))

    @jsii.member(jsii_name="resetAzureClientSecret")
    def reset_azure_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureClientSecret", []))

    @jsii.member(jsii_name="resetAzureEnvironment")
    def reset_azure_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureEnvironment", []))

    @jsii.member(jsii_name="resetAzureLoginAppId")
    def reset_azure_login_app_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureLoginAppId", []))

    @jsii.member(jsii_name="resetAzureTenantId")
    def reset_azure_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureTenantId", []))

    @jsii.member(jsii_name="resetAzureUseMsi")
    def reset_azure_use_msi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureUseMsi", []))

    @jsii.member(jsii_name="resetAzureWorkspaceResourceId")
    def reset_azure_workspace_resource_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureWorkspaceResourceId", []))

    @jsii.member(jsii_name="resetBricksCliPath")
    def reset_bricks_cli_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBricksCliPath", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetConfigFile")
    def reset_config_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigFile", []))

    @jsii.member(jsii_name="resetDebugHeaders")
    def reset_debug_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDebugHeaders", []))

    @jsii.member(jsii_name="resetDebugTruncateBytes")
    def reset_debug_truncate_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDebugTruncateBytes", []))

    @jsii.member(jsii_name="resetGoogleCredentials")
    def reset_google_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleCredentials", []))

    @jsii.member(jsii_name="resetGoogleServiceAccount")
    def reset_google_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleServiceAccount", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetHttpTimeoutSeconds")
    def reset_http_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpTimeoutSeconds", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetProfile")
    def reset_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProfile", []))

    @jsii.member(jsii_name="resetRateLimit")
    def reset_rate_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRateLimit", []))

    @jsii.member(jsii_name="resetRetryTimeoutSeconds")
    def reset_retry_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryTimeoutSeconds", []))

    @jsii.member(jsii_name="resetSkipVerify")
    def reset_skip_verify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipVerify", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="authTypeInput")
    def auth_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="azureClientIdInput")
    def azure_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="azureClientSecretInput")
    def azure_client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureClientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="azureEnvironmentInput")
    def azure_environment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureEnvironmentInput"))

    @builtins.property
    @jsii.member(jsii_name="azureLoginAppIdInput")
    def azure_login_app_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureLoginAppIdInput"))

    @builtins.property
    @jsii.member(jsii_name="azureTenantIdInput")
    def azure_tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureTenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="azureUseMsiInput")
    def azure_use_msi_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "azureUseMsiInput"))

    @builtins.property
    @jsii.member(jsii_name="azureWorkspaceResourceIdInput")
    def azure_workspace_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureWorkspaceResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="bricksCliPathInput")
    def bricks_cli_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bricksCliPathInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="configFileInput")
    def config_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configFileInput"))

    @builtins.property
    @jsii.member(jsii_name="debugHeadersInput")
    def debug_headers_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "debugHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="debugTruncateBytesInput")
    def debug_truncate_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "debugTruncateBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="googleCredentialsInput")
    def google_credentials_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="googleServiceAccountInput")
    def google_service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleServiceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="httpTimeoutSecondsInput")
    def http_timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpTimeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="profileInput")
    def profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileInput"))

    @builtins.property
    @jsii.member(jsii_name="rateLimitInput")
    def rate_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rateLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="retryTimeoutSecondsInput")
    def retry_timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryTimeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="skipVerifyInput")
    def skip_verify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "skipVerifyInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0329bfcb2b563a8b8c5dfa91c434d56bc3c2e4d0a2209b67afd9c5ae06af57ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e0dcb257ce07366581d6a739d83fd865d740443a15dfca3b46d05f622b683d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authType"))

    @auth_type.setter
    def auth_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7f97da7f04432a0688a8950c7fd2972667ed2182db3adba8b67d69d5b60d576)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authType", value)

    @builtins.property
    @jsii.member(jsii_name="azureClientId")
    def azure_client_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureClientId"))

    @azure_client_id.setter
    def azure_client_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__894c091ac78062c258fbf239edb2a784c82f5fc1014b210df1d6f907580646a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureClientId", value)

    @builtins.property
    @jsii.member(jsii_name="azureClientSecret")
    def azure_client_secret(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureClientSecret"))

    @azure_client_secret.setter
    def azure_client_secret(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85249a5b362c06f4559c32bc5c5d9766ad69ba8ca04c99ec14117cbb7bec7254)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureClientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="azureEnvironment")
    def azure_environment(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureEnvironment"))

    @azure_environment.setter
    def azure_environment(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c653756a0ca66c847f06be8617f48c4ec86580dc216bd94680acb60e2519d81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureEnvironment", value)

    @builtins.property
    @jsii.member(jsii_name="azureLoginAppId")
    def azure_login_app_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureLoginAppId"))

    @azure_login_app_id.setter
    def azure_login_app_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2736c5fda7196459b013162c40b54d88192283311793666f9c68754ca20f2bf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureLoginAppId", value)

    @builtins.property
    @jsii.member(jsii_name="azureTenantId")
    def azure_tenant_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureTenantId"))

    @azure_tenant_id.setter
    def azure_tenant_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__354949fb6fbc98136876b8e9e41c41d95ee55c4ea4963cc7029faf3216290453)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureTenantId", value)

    @builtins.property
    @jsii.member(jsii_name="azureUseMsi")
    def azure_use_msi(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "azureUseMsi"))

    @azure_use_msi.setter
    def azure_use_msi(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9056a273af10a9820c458de8b056bd9220949b8dcd489e3c680170b745430ce5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureUseMsi", value)

    @builtins.property
    @jsii.member(jsii_name="azureWorkspaceResourceId")
    def azure_workspace_resource_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureWorkspaceResourceId"))

    @azure_workspace_resource_id.setter
    def azure_workspace_resource_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a67bdefd20eefc9d7df72b32b01611bf7042314c91615fcb742754f9746f60f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureWorkspaceResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="bricksCliPath")
    def bricks_cli_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bricksCliPath"))

    @bricks_cli_path.setter
    def bricks_cli_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fecb9143cc110eb151d4af17dfb98d6657f804f464f4ed0ce1be6522f8471877)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bricksCliPath", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0946ba91334eb522f25176954b69da5d49ebb6afc2fd35f2da209aed6ff5ff6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78b0d3c88775f0f1e4d1c662de822d900bd3747ebf3ce166b220e21372417737)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="configFile")
    def config_file(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configFile"))

    @config_file.setter
    def config_file(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be9e771e38913b43fe56b98733472dac36f1b5a00ba58f52e08294390ef050be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configFile", value)

    @builtins.property
    @jsii.member(jsii_name="debugHeaders")
    def debug_headers(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "debugHeaders"))

    @debug_headers.setter
    def debug_headers(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b28185d55380756ebfbaf395df863664436f44a7029c9f4ec8634a6009d6e13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "debugHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="debugTruncateBytes")
    def debug_truncate_bytes(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "debugTruncateBytes"))

    @debug_truncate_bytes.setter
    def debug_truncate_bytes(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eca6e2d35037ae01b92ffc8c380b24f76a2741e82dee8caefaa077c83c2183f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "debugTruncateBytes", value)

    @builtins.property
    @jsii.member(jsii_name="googleCredentials")
    def google_credentials(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleCredentials"))

    @google_credentials.setter
    def google_credentials(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9de17842af0680b7b0ca360aec73a6a01ff5b58c5b47e342af143dfdaa9bef86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "googleCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="googleServiceAccount")
    def google_service_account(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleServiceAccount"))

    @google_service_account.setter
    def google_service_account(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6c0a83d63a75488a0f671106a5a3f969c6160ca815bf7d123135637447fcb6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "googleServiceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "host"))

    @host.setter
    def host(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__365eefc31aab1dc47a2c5ac3ae7a66b1c17d39c1006aed20494c3a1e0f14159c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="httpTimeoutSeconds")
    def http_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpTimeoutSeconds"))

    @http_timeout_seconds.setter
    def http_timeout_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d49db9d2d2afd13d52c4691c2c1cebfe5d718c9007d20b55e514f5c0b91da80d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ce05e2ae9a44506052d126e7860f4017c9a7bcc4327fec685beb353b98afb32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="profile")
    def profile(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profile"))

    @profile.setter
    def profile(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__def0a013395a291a4eb4182e05b09a79905bf8808e24c4fbae895105f0aecb49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profile", value)

    @builtins.property
    @jsii.member(jsii_name="rateLimit")
    def rate_limit(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rateLimit"))

    @rate_limit.setter
    def rate_limit(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6bba2d1938a583ca20e489cd964c87e4a308695c2f5bb904acc5fc386547f63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rateLimit", value)

    @builtins.property
    @jsii.member(jsii_name="retryTimeoutSeconds")
    def retry_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryTimeoutSeconds"))

    @retry_timeout_seconds.setter
    def retry_timeout_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dca9848e68211f9c3cc191fcaf8cd573b0b3375f1f4f39fc4ce3baebe98f2c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="skipVerify")
    def skip_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "skipVerify"))

    @skip_verify.setter
    def skip_verify(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cd38022f87f43d702cc136d622b6aee0a957bc20945604d08a07ddee8ae5d59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipVerify", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c46aa3ce47f904cc93335f1c48a790ab1ce1f16f0212e557d6a518c884b6f9be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "username"))

    @username.setter
    def username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f73df2faa6116afa856891f0459fefb42f3fdb4bc4f751b0724a71d677fc69a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="databricks.provider.DatabricksProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "alias": "alias",
        "auth_type": "authType",
        "azure_client_id": "azureClientId",
        "azure_client_secret": "azureClientSecret",
        "azure_environment": "azureEnvironment",
        "azure_login_app_id": "azureLoginAppId",
        "azure_tenant_id": "azureTenantId",
        "azure_use_msi": "azureUseMsi",
        "azure_workspace_resource_id": "azureWorkspaceResourceId",
        "bricks_cli_path": "bricksCliPath",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "config_file": "configFile",
        "debug_headers": "debugHeaders",
        "debug_truncate_bytes": "debugTruncateBytes",
        "google_credentials": "googleCredentials",
        "google_service_account": "googleServiceAccount",
        "host": "host",
        "http_timeout_seconds": "httpTimeoutSeconds",
        "password": "password",
        "profile": "profile",
        "rate_limit": "rateLimit",
        "retry_timeout_seconds": "retryTimeoutSeconds",
        "skip_verify": "skipVerify",
        "token": "token",
        "username": "username",
    },
)
class DatabricksProviderConfig:
    def __init__(
        self,
        *,
        account_id: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        auth_type: typing.Optional[builtins.str] = None,
        azure_client_id: typing.Optional[builtins.str] = None,
        azure_client_secret: typing.Optional[builtins.str] = None,
        azure_environment: typing.Optional[builtins.str] = None,
        azure_login_app_id: typing.Optional[builtins.str] = None,
        azure_tenant_id: typing.Optional[builtins.str] = None,
        azure_use_msi: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        azure_workspace_resource_id: typing.Optional[builtins.str] = None,
        bricks_cli_path: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        config_file: typing.Optional[builtins.str] = None,
        debug_headers: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        debug_truncate_bytes: typing.Optional[jsii.Number] = None,
        google_credentials: typing.Optional[builtins.str] = None,
        google_service_account: typing.Optional[builtins.str] = None,
        host: typing.Optional[builtins.str] = None,
        http_timeout_seconds: typing.Optional[jsii.Number] = None,
        password: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        rate_limit: typing.Optional[jsii.Number] = None,
        retry_timeout_seconds: typing.Optional[jsii.Number] = None,
        skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        token: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#account_id DatabricksProvider#account_id}.
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#alias DatabricksProvider#alias}
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#auth_type DatabricksProvider#auth_type}.
        :param azure_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_client_id DatabricksProvider#azure_client_id}.
        :param azure_client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_client_secret DatabricksProvider#azure_client_secret}.
        :param azure_environment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_environment DatabricksProvider#azure_environment}.
        :param azure_login_app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_login_app_id DatabricksProvider#azure_login_app_id}.
        :param azure_tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_tenant_id DatabricksProvider#azure_tenant_id}.
        :param azure_use_msi: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_use_msi DatabricksProvider#azure_use_msi}.
        :param azure_workspace_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_workspace_resource_id DatabricksProvider#azure_workspace_resource_id}.
        :param bricks_cli_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#bricks_cli_path DatabricksProvider#bricks_cli_path}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#client_id DatabricksProvider#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#client_secret DatabricksProvider#client_secret}.
        :param config_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#config_file DatabricksProvider#config_file}.
        :param debug_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#debug_headers DatabricksProvider#debug_headers}.
        :param debug_truncate_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#debug_truncate_bytes DatabricksProvider#debug_truncate_bytes}.
        :param google_credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#google_credentials DatabricksProvider#google_credentials}.
        :param google_service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#google_service_account DatabricksProvider#google_service_account}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#host DatabricksProvider#host}.
        :param http_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#http_timeout_seconds DatabricksProvider#http_timeout_seconds}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#password DatabricksProvider#password}.
        :param profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#profile DatabricksProvider#profile}.
        :param rate_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#rate_limit DatabricksProvider#rate_limit}.
        :param retry_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#retry_timeout_seconds DatabricksProvider#retry_timeout_seconds}.
        :param skip_verify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#skip_verify DatabricksProvider#skip_verify}.
        :param token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#token DatabricksProvider#token}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#username DatabricksProvider#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ec2c76424c723bb935fab26c44a7b770c62ae8b45336bf38fcba397253d8cb5)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
            check_type(argname="argument azure_client_id", value=azure_client_id, expected_type=type_hints["azure_client_id"])
            check_type(argname="argument azure_client_secret", value=azure_client_secret, expected_type=type_hints["azure_client_secret"])
            check_type(argname="argument azure_environment", value=azure_environment, expected_type=type_hints["azure_environment"])
            check_type(argname="argument azure_login_app_id", value=azure_login_app_id, expected_type=type_hints["azure_login_app_id"])
            check_type(argname="argument azure_tenant_id", value=azure_tenant_id, expected_type=type_hints["azure_tenant_id"])
            check_type(argname="argument azure_use_msi", value=azure_use_msi, expected_type=type_hints["azure_use_msi"])
            check_type(argname="argument azure_workspace_resource_id", value=azure_workspace_resource_id, expected_type=type_hints["azure_workspace_resource_id"])
            check_type(argname="argument bricks_cli_path", value=bricks_cli_path, expected_type=type_hints["bricks_cli_path"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument config_file", value=config_file, expected_type=type_hints["config_file"])
            check_type(argname="argument debug_headers", value=debug_headers, expected_type=type_hints["debug_headers"])
            check_type(argname="argument debug_truncate_bytes", value=debug_truncate_bytes, expected_type=type_hints["debug_truncate_bytes"])
            check_type(argname="argument google_credentials", value=google_credentials, expected_type=type_hints["google_credentials"])
            check_type(argname="argument google_service_account", value=google_service_account, expected_type=type_hints["google_service_account"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument http_timeout_seconds", value=http_timeout_seconds, expected_type=type_hints["http_timeout_seconds"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument rate_limit", value=rate_limit, expected_type=type_hints["rate_limit"])
            check_type(argname="argument retry_timeout_seconds", value=retry_timeout_seconds, expected_type=type_hints["retry_timeout_seconds"])
            check_type(argname="argument skip_verify", value=skip_verify, expected_type=type_hints["skip_verify"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account_id is not None:
            self._values["account_id"] = account_id
        if alias is not None:
            self._values["alias"] = alias
        if auth_type is not None:
            self._values["auth_type"] = auth_type
        if azure_client_id is not None:
            self._values["azure_client_id"] = azure_client_id
        if azure_client_secret is not None:
            self._values["azure_client_secret"] = azure_client_secret
        if azure_environment is not None:
            self._values["azure_environment"] = azure_environment
        if azure_login_app_id is not None:
            self._values["azure_login_app_id"] = azure_login_app_id
        if azure_tenant_id is not None:
            self._values["azure_tenant_id"] = azure_tenant_id
        if azure_use_msi is not None:
            self._values["azure_use_msi"] = azure_use_msi
        if azure_workspace_resource_id is not None:
            self._values["azure_workspace_resource_id"] = azure_workspace_resource_id
        if bricks_cli_path is not None:
            self._values["bricks_cli_path"] = bricks_cli_path
        if client_id is not None:
            self._values["client_id"] = client_id
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if config_file is not None:
            self._values["config_file"] = config_file
        if debug_headers is not None:
            self._values["debug_headers"] = debug_headers
        if debug_truncate_bytes is not None:
            self._values["debug_truncate_bytes"] = debug_truncate_bytes
        if google_credentials is not None:
            self._values["google_credentials"] = google_credentials
        if google_service_account is not None:
            self._values["google_service_account"] = google_service_account
        if host is not None:
            self._values["host"] = host
        if http_timeout_seconds is not None:
            self._values["http_timeout_seconds"] = http_timeout_seconds
        if password is not None:
            self._values["password"] = password
        if profile is not None:
            self._values["profile"] = profile
        if rate_limit is not None:
            self._values["rate_limit"] = rate_limit
        if retry_timeout_seconds is not None:
            self._values["retry_timeout_seconds"] = retry_timeout_seconds
        if skip_verify is not None:
            self._values["skip_verify"] = skip_verify
        if token is not None:
            self._values["token"] = token
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#account_id DatabricksProvider#account_id}.'''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#alias DatabricksProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#auth_type DatabricksProvider#auth_type}.'''
        result = self._values.get("auth_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_client_id DatabricksProvider#azure_client_id}.'''
        result = self._values.get("azure_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_client_secret(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_client_secret DatabricksProvider#azure_client_secret}.'''
        result = self._values.get("azure_client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_environment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_environment DatabricksProvider#azure_environment}.'''
        result = self._values.get("azure_environment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_login_app_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_login_app_id DatabricksProvider#azure_login_app_id}.'''
        result = self._values.get("azure_login_app_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_tenant_id DatabricksProvider#azure_tenant_id}.'''
        result = self._values.get("azure_tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azure_use_msi(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_use_msi DatabricksProvider#azure_use_msi}.'''
        result = self._values.get("azure_use_msi")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def azure_workspace_resource_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#azure_workspace_resource_id DatabricksProvider#azure_workspace_resource_id}.'''
        result = self._values.get("azure_workspace_resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bricks_cli_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#bricks_cli_path DatabricksProvider#bricks_cli_path}.'''
        result = self._values.get("bricks_cli_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#client_id DatabricksProvider#client_id}.'''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#client_secret DatabricksProvider#client_secret}.'''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_file(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#config_file DatabricksProvider#config_file}.'''
        result = self._values.get("config_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def debug_headers(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#debug_headers DatabricksProvider#debug_headers}.'''
        result = self._values.get("debug_headers")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def debug_truncate_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#debug_truncate_bytes DatabricksProvider#debug_truncate_bytes}.'''
        result = self._values.get("debug_truncate_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def google_credentials(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#google_credentials DatabricksProvider#google_credentials}.'''
        result = self._values.get("google_credentials")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def google_service_account(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#google_service_account DatabricksProvider#google_service_account}.'''
        result = self._values.get("google_service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#host DatabricksProvider#host}.'''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#http_timeout_seconds DatabricksProvider#http_timeout_seconds}.'''
        result = self._values.get("http_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#password DatabricksProvider#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#profile DatabricksProvider#profile}.'''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rate_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#rate_limit DatabricksProvider#rate_limit}.'''
        result = self._values.get("rate_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retry_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#retry_timeout_seconds DatabricksProvider#retry_timeout_seconds}.'''
        result = self._values.get("retry_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def skip_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#skip_verify DatabricksProvider#skip_verify}.'''
        result = self._values.get("skip_verify")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#token DatabricksProvider#token}.'''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks#username DatabricksProvider#username}.'''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabricksProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DatabricksProvider",
    "DatabricksProviderConfig",
]

publication.publish()

def _typecheckingstub__083fa990793980cc648331b1283a7a29e2cac0c0a6717a4d7bac2f31b229c795(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account_id: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    auth_type: typing.Optional[builtins.str] = None,
    azure_client_id: typing.Optional[builtins.str] = None,
    azure_client_secret: typing.Optional[builtins.str] = None,
    azure_environment: typing.Optional[builtins.str] = None,
    azure_login_app_id: typing.Optional[builtins.str] = None,
    azure_tenant_id: typing.Optional[builtins.str] = None,
    azure_use_msi: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    azure_workspace_resource_id: typing.Optional[builtins.str] = None,
    bricks_cli_path: typing.Optional[builtins.str] = None,
    client_id: typing.Optional[builtins.str] = None,
    client_secret: typing.Optional[builtins.str] = None,
    config_file: typing.Optional[builtins.str] = None,
    debug_headers: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    debug_truncate_bytes: typing.Optional[jsii.Number] = None,
    google_credentials: typing.Optional[builtins.str] = None,
    google_service_account: typing.Optional[builtins.str] = None,
    host: typing.Optional[builtins.str] = None,
    http_timeout_seconds: typing.Optional[jsii.Number] = None,
    password: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    rate_limit: typing.Optional[jsii.Number] = None,
    retry_timeout_seconds: typing.Optional[jsii.Number] = None,
    skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    token: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0329bfcb2b563a8b8c5dfa91c434d56bc3c2e4d0a2209b67afd9c5ae06af57ba(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e0dcb257ce07366581d6a739d83fd865d740443a15dfca3b46d05f622b683d1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7f97da7f04432a0688a8950c7fd2972667ed2182db3adba8b67d69d5b60d576(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__894c091ac78062c258fbf239edb2a784c82f5fc1014b210df1d6f907580646a7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85249a5b362c06f4559c32bc5c5d9766ad69ba8ca04c99ec14117cbb7bec7254(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c653756a0ca66c847f06be8617f48c4ec86580dc216bd94680acb60e2519d81(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2736c5fda7196459b013162c40b54d88192283311793666f9c68754ca20f2bf6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__354949fb6fbc98136876b8e9e41c41d95ee55c4ea4963cc7029faf3216290453(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9056a273af10a9820c458de8b056bd9220949b8dcd489e3c680170b745430ce5(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a67bdefd20eefc9d7df72b32b01611bf7042314c91615fcb742754f9746f60f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fecb9143cc110eb151d4af17dfb98d6657f804f464f4ed0ce1be6522f8471877(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0946ba91334eb522f25176954b69da5d49ebb6afc2fd35f2da209aed6ff5ff6c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78b0d3c88775f0f1e4d1c662de822d900bd3747ebf3ce166b220e21372417737(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be9e771e38913b43fe56b98733472dac36f1b5a00ba58f52e08294390ef050be(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b28185d55380756ebfbaf395df863664436f44a7029c9f4ec8634a6009d6e13(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eca6e2d35037ae01b92ffc8c380b24f76a2741e82dee8caefaa077c83c2183f8(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9de17842af0680b7b0ca360aec73a6a01ff5b58c5b47e342af143dfdaa9bef86(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6c0a83d63a75488a0f671106a5a3f969c6160ca815bf7d123135637447fcb6c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__365eefc31aab1dc47a2c5ac3ae7a66b1c17d39c1006aed20494c3a1e0f14159c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d49db9d2d2afd13d52c4691c2c1cebfe5d718c9007d20b55e514f5c0b91da80d(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ce05e2ae9a44506052d126e7860f4017c9a7bcc4327fec685beb353b98afb32(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__def0a013395a291a4eb4182e05b09a79905bf8808e24c4fbae895105f0aecb49(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6bba2d1938a583ca20e489cd964c87e4a308695c2f5bb904acc5fc386547f63(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dca9848e68211f9c3cc191fcaf8cd573b0b3375f1f4f39fc4ce3baebe98f2c3(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cd38022f87f43d702cc136d622b6aee0a957bc20945604d08a07ddee8ae5d59(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c46aa3ce47f904cc93335f1c48a790ab1ce1f16f0212e557d6a518c884b6f9be(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f73df2faa6116afa856891f0459fefb42f3fdb4bc4f751b0724a71d677fc69a2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ec2c76424c723bb935fab26c44a7b770c62ae8b45336bf38fcba397253d8cb5(
    *,
    account_id: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    auth_type: typing.Optional[builtins.str] = None,
    azure_client_id: typing.Optional[builtins.str] = None,
    azure_client_secret: typing.Optional[builtins.str] = None,
    azure_environment: typing.Optional[builtins.str] = None,
    azure_login_app_id: typing.Optional[builtins.str] = None,
    azure_tenant_id: typing.Optional[builtins.str] = None,
    azure_use_msi: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    azure_workspace_resource_id: typing.Optional[builtins.str] = None,
    bricks_cli_path: typing.Optional[builtins.str] = None,
    client_id: typing.Optional[builtins.str] = None,
    client_secret: typing.Optional[builtins.str] = None,
    config_file: typing.Optional[builtins.str] = None,
    debug_headers: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    debug_truncate_bytes: typing.Optional[jsii.Number] = None,
    google_credentials: typing.Optional[builtins.str] = None,
    google_service_account: typing.Optional[builtins.str] = None,
    host: typing.Optional[builtins.str] = None,
    http_timeout_seconds: typing.Optional[jsii.Number] = None,
    password: typing.Optional[builtins.str] = None,
    profile: typing.Optional[builtins.str] = None,
    rate_limit: typing.Optional[jsii.Number] = None,
    retry_timeout_seconds: typing.Optional[jsii.Number] = None,
    skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    token: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
