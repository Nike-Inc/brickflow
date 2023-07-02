'''
# `databricks_mws_workspaces`

Refer to the Terraform Registory for docs: [`databricks_mws_workspaces`](https://www.terraform.io/docs/providers/databricks/r/mws_workspaces).
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


class MwsWorkspaces(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsWorkspaces.MwsWorkspaces",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces databricks_mws_workspaces}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        account_id: builtins.str,
        workspace_name: builtins.str,
        aws_region: typing.Optional[builtins.str] = None,
        cloud: typing.Optional[builtins.str] = None,
        cloud_resource_container: typing.Optional[typing.Union["MwsWorkspacesCloudResourceContainer", typing.Dict[builtins.str, typing.Any]]] = None,
        creation_time: typing.Optional[jsii.Number] = None,
        credentials_id: typing.Optional[builtins.str] = None,
        customer_managed_key_id: typing.Optional[builtins.str] = None,
        deployment_name: typing.Optional[builtins.str] = None,
        external_customer_info: typing.Optional[typing.Union["MwsWorkspacesExternalCustomerInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        gcp_managed_network_config: typing.Optional[typing.Union["MwsWorkspacesGcpManagedNetworkConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        gke_config: typing.Optional[typing.Union["MwsWorkspacesGkeConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        is_no_public_ip_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        managed_services_customer_managed_key_id: typing.Optional[builtins.str] = None,
        network_id: typing.Optional[builtins.str] = None,
        pricing_tier: typing.Optional[builtins.str] = None,
        private_access_settings_id: typing.Optional[builtins.str] = None,
        storage_configuration_id: typing.Optional[builtins.str] = None,
        storage_customer_managed_key_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MwsWorkspacesTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        token: typing.Optional[typing.Union["MwsWorkspacesToken", typing.Dict[builtins.str, typing.Any]]] = None,
        workspace_id: typing.Optional[jsii.Number] = None,
        workspace_status: typing.Optional[builtins.str] = None,
        workspace_status_message: typing.Optional[builtins.str] = None,
        workspace_url: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces databricks_mws_workspaces} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#account_id MwsWorkspaces#account_id}.
        :param workspace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_name MwsWorkspaces#workspace_name}.
        :param aws_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#aws_region MwsWorkspaces#aws_region}.
        :param cloud: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#cloud MwsWorkspaces#cloud}.
        :param cloud_resource_container: cloud_resource_container block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#cloud_resource_container MwsWorkspaces#cloud_resource_container}
        :param creation_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#creation_time MwsWorkspaces#creation_time}.
        :param credentials_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#credentials_id MwsWorkspaces#credentials_id}.
        :param customer_managed_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#customer_managed_key_id MwsWorkspaces#customer_managed_key_id}.
        :param deployment_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#deployment_name MwsWorkspaces#deployment_name}.
        :param external_customer_info: external_customer_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#external_customer_info MwsWorkspaces#external_customer_info}
        :param gcp_managed_network_config: gcp_managed_network_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gcp_managed_network_config MwsWorkspaces#gcp_managed_network_config}
        :param gke_config: gke_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_config MwsWorkspaces#gke_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#id MwsWorkspaces#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_no_public_ip_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#is_no_public_ip_enabled MwsWorkspaces#is_no_public_ip_enabled}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#location MwsWorkspaces#location}.
        :param managed_services_customer_managed_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#managed_services_customer_managed_key_id MwsWorkspaces#managed_services_customer_managed_key_id}.
        :param network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#network_id MwsWorkspaces#network_id}.
        :param pricing_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#pricing_tier MwsWorkspaces#pricing_tier}.
        :param private_access_settings_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#private_access_settings_id MwsWorkspaces#private_access_settings_id}.
        :param storage_configuration_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#storage_configuration_id MwsWorkspaces#storage_configuration_id}.
        :param storage_customer_managed_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#storage_customer_managed_key_id MwsWorkspaces#storage_customer_managed_key_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#timeouts MwsWorkspaces#timeouts}
        :param token: token block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token MwsWorkspaces#token}
        :param workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_id MwsWorkspaces#workspace_id}.
        :param workspace_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_status MwsWorkspaces#workspace_status}.
        :param workspace_status_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_status_message MwsWorkspaces#workspace_status_message}.
        :param workspace_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_url MwsWorkspaces#workspace_url}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0706cd5c9907c8b2f0d0dc4529ff6077959730ca71d7c750bdcbe6b9d0a904a9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MwsWorkspacesConfig(
            account_id=account_id,
            workspace_name=workspace_name,
            aws_region=aws_region,
            cloud=cloud,
            cloud_resource_container=cloud_resource_container,
            creation_time=creation_time,
            credentials_id=credentials_id,
            customer_managed_key_id=customer_managed_key_id,
            deployment_name=deployment_name,
            external_customer_info=external_customer_info,
            gcp_managed_network_config=gcp_managed_network_config,
            gke_config=gke_config,
            id=id,
            is_no_public_ip_enabled=is_no_public_ip_enabled,
            location=location,
            managed_services_customer_managed_key_id=managed_services_customer_managed_key_id,
            network_id=network_id,
            pricing_tier=pricing_tier,
            private_access_settings_id=private_access_settings_id,
            storage_configuration_id=storage_configuration_id,
            storage_customer_managed_key_id=storage_customer_managed_key_id,
            timeouts=timeouts,
            token=token,
            workspace_id=workspace_id,
            workspace_status=workspace_status,
            workspace_status_message=workspace_status_message,
            workspace_url=workspace_url,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCloudResourceContainer")
    def put_cloud_resource_container(
        self,
        *,
        gcp: typing.Union["MwsWorkspacesCloudResourceContainerGcp", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param gcp: gcp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gcp MwsWorkspaces#gcp}
        '''
        value = MwsWorkspacesCloudResourceContainer(gcp=gcp)

        return typing.cast(None, jsii.invoke(self, "putCloudResourceContainer", [value]))

    @jsii.member(jsii_name="putExternalCustomerInfo")
    def put_external_customer_info(
        self,
        *,
        authoritative_user_email: builtins.str,
        authoritative_user_full_name: builtins.str,
        customer_name: builtins.str,
    ) -> None:
        '''
        :param authoritative_user_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#authoritative_user_email MwsWorkspaces#authoritative_user_email}.
        :param authoritative_user_full_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#authoritative_user_full_name MwsWorkspaces#authoritative_user_full_name}.
        :param customer_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#customer_name MwsWorkspaces#customer_name}.
        '''
        value = MwsWorkspacesExternalCustomerInfo(
            authoritative_user_email=authoritative_user_email,
            authoritative_user_full_name=authoritative_user_full_name,
            customer_name=customer_name,
        )

        return typing.cast(None, jsii.invoke(self, "putExternalCustomerInfo", [value]))

    @jsii.member(jsii_name="putGcpManagedNetworkConfig")
    def put_gcp_managed_network_config(
        self,
        *,
        gke_cluster_pod_ip_range: builtins.str,
        gke_cluster_service_ip_range: builtins.str,
        subnet_cidr: builtins.str,
    ) -> None:
        '''
        :param gke_cluster_pod_ip_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_cluster_pod_ip_range MwsWorkspaces#gke_cluster_pod_ip_range}.
        :param gke_cluster_service_ip_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_cluster_service_ip_range MwsWorkspaces#gke_cluster_service_ip_range}.
        :param subnet_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#subnet_cidr MwsWorkspaces#subnet_cidr}.
        '''
        value = MwsWorkspacesGcpManagedNetworkConfig(
            gke_cluster_pod_ip_range=gke_cluster_pod_ip_range,
            gke_cluster_service_ip_range=gke_cluster_service_ip_range,
            subnet_cidr=subnet_cidr,
        )

        return typing.cast(None, jsii.invoke(self, "putGcpManagedNetworkConfig", [value]))

    @jsii.member(jsii_name="putGkeConfig")
    def put_gke_config(
        self,
        *,
        connectivity_type: builtins.str,
        master_ip_range: builtins.str,
    ) -> None:
        '''
        :param connectivity_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#connectivity_type MwsWorkspaces#connectivity_type}.
        :param master_ip_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#master_ip_range MwsWorkspaces#master_ip_range}.
        '''
        value = MwsWorkspacesGkeConfig(
            connectivity_type=connectivity_type, master_ip_range=master_ip_range
        )

        return typing.cast(None, jsii.invoke(self, "putGkeConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#create MwsWorkspaces#create}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#read MwsWorkspaces#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#update MwsWorkspaces#update}.
        '''
        value = MwsWorkspacesTimeouts(create=create, read=read, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putToken")
    def put_token(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        lifetime_seconds: typing.Optional[jsii.Number] = None,
        token_id: typing.Optional[builtins.str] = None,
        token_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#comment MwsWorkspaces#comment}.
        :param lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#lifetime_seconds MwsWorkspaces#lifetime_seconds}.
        :param token_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token_id MwsWorkspaces#token_id}.
        :param token_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token_value MwsWorkspaces#token_value}.
        '''
        value = MwsWorkspacesToken(
            comment=comment,
            lifetime_seconds=lifetime_seconds,
            token_id=token_id,
            token_value=token_value,
        )

        return typing.cast(None, jsii.invoke(self, "putToken", [value]))

    @jsii.member(jsii_name="resetAwsRegion")
    def reset_aws_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegion", []))

    @jsii.member(jsii_name="resetCloud")
    def reset_cloud(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloud", []))

    @jsii.member(jsii_name="resetCloudResourceContainer")
    def reset_cloud_resource_container(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudResourceContainer", []))

    @jsii.member(jsii_name="resetCreationTime")
    def reset_creation_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreationTime", []))

    @jsii.member(jsii_name="resetCredentialsId")
    def reset_credentials_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentialsId", []))

    @jsii.member(jsii_name="resetCustomerManagedKeyId")
    def reset_customer_managed_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerManagedKeyId", []))

    @jsii.member(jsii_name="resetDeploymentName")
    def reset_deployment_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentName", []))

    @jsii.member(jsii_name="resetExternalCustomerInfo")
    def reset_external_customer_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalCustomerInfo", []))

    @jsii.member(jsii_name="resetGcpManagedNetworkConfig")
    def reset_gcp_managed_network_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpManagedNetworkConfig", []))

    @jsii.member(jsii_name="resetGkeConfig")
    def reset_gke_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGkeConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsNoPublicIpEnabled")
    def reset_is_no_public_ip_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsNoPublicIpEnabled", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetManagedServicesCustomerManagedKeyId")
    def reset_managed_services_customer_managed_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedServicesCustomerManagedKeyId", []))

    @jsii.member(jsii_name="resetNetworkId")
    def reset_network_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkId", []))

    @jsii.member(jsii_name="resetPricingTier")
    def reset_pricing_tier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPricingTier", []))

    @jsii.member(jsii_name="resetPrivateAccessSettingsId")
    def reset_private_access_settings_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateAccessSettingsId", []))

    @jsii.member(jsii_name="resetStorageConfigurationId")
    def reset_storage_configuration_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageConfigurationId", []))

    @jsii.member(jsii_name="resetStorageCustomerManagedKeyId")
    def reset_storage_customer_managed_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageCustomerManagedKeyId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="resetWorkspaceId")
    def reset_workspace_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceId", []))

    @jsii.member(jsii_name="resetWorkspaceStatus")
    def reset_workspace_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceStatus", []))

    @jsii.member(jsii_name="resetWorkspaceStatusMessage")
    def reset_workspace_status_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceStatusMessage", []))

    @jsii.member(jsii_name="resetWorkspaceUrl")
    def reset_workspace_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceUrl", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="cloudResourceContainer")
    def cloud_resource_container(
        self,
    ) -> "MwsWorkspacesCloudResourceContainerOutputReference":
        return typing.cast("MwsWorkspacesCloudResourceContainerOutputReference", jsii.get(self, "cloudResourceContainer"))

    @builtins.property
    @jsii.member(jsii_name="externalCustomerInfo")
    def external_customer_info(
        self,
    ) -> "MwsWorkspacesExternalCustomerInfoOutputReference":
        return typing.cast("MwsWorkspacesExternalCustomerInfoOutputReference", jsii.get(self, "externalCustomerInfo"))

    @builtins.property
    @jsii.member(jsii_name="gcpManagedNetworkConfig")
    def gcp_managed_network_config(
        self,
    ) -> "MwsWorkspacesGcpManagedNetworkConfigOutputReference":
        return typing.cast("MwsWorkspacesGcpManagedNetworkConfigOutputReference", jsii.get(self, "gcpManagedNetworkConfig"))

    @builtins.property
    @jsii.member(jsii_name="gkeConfig")
    def gke_config(self) -> "MwsWorkspacesGkeConfigOutputReference":
        return typing.cast("MwsWorkspacesGkeConfigOutputReference", jsii.get(self, "gkeConfig"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MwsWorkspacesTimeoutsOutputReference":
        return typing.cast("MwsWorkspacesTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> "MwsWorkspacesTokenOutputReference":
        return typing.cast("MwsWorkspacesTokenOutputReference", jsii.get(self, "token"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegionInput")
    def aws_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudInput")
    def cloud_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudResourceContainerInput")
    def cloud_resource_container_input(
        self,
    ) -> typing.Optional["MwsWorkspacesCloudResourceContainer"]:
        return typing.cast(typing.Optional["MwsWorkspacesCloudResourceContainer"], jsii.get(self, "cloudResourceContainerInput"))

    @builtins.property
    @jsii.member(jsii_name="creationTimeInput")
    def creation_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "creationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsIdInput")
    def credentials_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialsIdInput"))

    @builtins.property
    @jsii.member(jsii_name="customerManagedKeyIdInput")
    def customer_managed_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerManagedKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentNameInput")
    def deployment_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentNameInput"))

    @builtins.property
    @jsii.member(jsii_name="externalCustomerInfoInput")
    def external_customer_info_input(
        self,
    ) -> typing.Optional["MwsWorkspacesExternalCustomerInfo"]:
        return typing.cast(typing.Optional["MwsWorkspacesExternalCustomerInfo"], jsii.get(self, "externalCustomerInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="gcpManagedNetworkConfigInput")
    def gcp_managed_network_config_input(
        self,
    ) -> typing.Optional["MwsWorkspacesGcpManagedNetworkConfig"]:
        return typing.cast(typing.Optional["MwsWorkspacesGcpManagedNetworkConfig"], jsii.get(self, "gcpManagedNetworkConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="gkeConfigInput")
    def gke_config_input(self) -> typing.Optional["MwsWorkspacesGkeConfig"]:
        return typing.cast(typing.Optional["MwsWorkspacesGkeConfig"], jsii.get(self, "gkeConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isNoPublicIpEnabledInput")
    def is_no_public_ip_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "isNoPublicIpEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="managedServicesCustomerManagedKeyIdInput")
    def managed_services_customer_managed_key_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedServicesCustomerManagedKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="networkIdInput")
    def network_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkIdInput"))

    @builtins.property
    @jsii.member(jsii_name="pricingTierInput")
    def pricing_tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pricingTierInput"))

    @builtins.property
    @jsii.member(jsii_name="privateAccessSettingsIdInput")
    def private_access_settings_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateAccessSettingsIdInput"))

    @builtins.property
    @jsii.member(jsii_name="storageConfigurationIdInput")
    def storage_configuration_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageConfigurationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="storageCustomerManagedKeyIdInput")
    def storage_customer_managed_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageCustomerManagedKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MwsWorkspacesTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MwsWorkspacesTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional["MwsWorkspacesToken"]:
        return typing.cast(typing.Optional["MwsWorkspacesToken"], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceIdInput")
    def workspace_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "workspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceNameInput")
    def workspace_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workspaceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceStatusInput")
    def workspace_status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workspaceStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceStatusMessageInput")
    def workspace_status_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workspaceStatusMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceUrlInput")
    def workspace_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workspaceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fc8a25da3f04303a2168a06b1f4e1014ebfadf671ed3ea5b77b4b060cceeb48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="awsRegion")
    def aws_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsRegion"))

    @aws_region.setter
    def aws_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e86ce2d6f650902fedda21daa708c0cc7df0078a74ec0cef7a10aea3d9fb2644)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegion", value)

    @builtins.property
    @jsii.member(jsii_name="cloud")
    def cloud(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloud"))

    @cloud.setter
    def cloud(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cdf64f7ef5066277c447d606d73a723fb851bbe5faa884b8480129ad0fafc63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloud", value)

    @builtins.property
    @jsii.member(jsii_name="creationTime")
    def creation_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "creationTime"))

    @creation_time.setter
    def creation_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56955ed99d9529c31b3d821027c6a65ebe01405a34c1954bda53794a2f559422)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creationTime", value)

    @builtins.property
    @jsii.member(jsii_name="credentialsId")
    def credentials_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentialsId"))

    @credentials_id.setter
    def credentials_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e1a3fab67362234a71fa1fba628a0de6eb6b85bdf0bb1d56a28d31f147e44b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialsId", value)

    @builtins.property
    @jsii.member(jsii_name="customerManagedKeyId")
    def customer_managed_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerManagedKeyId"))

    @customer_managed_key_id.setter
    def customer_managed_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__646722ca86daaddfc5212527cece12c4dbc9c65851c23ff757cc760b2268e96a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerManagedKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentName")
    def deployment_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentName"))

    @deployment_name.setter
    def deployment_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ccea7cc66c3fd342428907ed3b23beb94d36386d3ad71163e977091a8943256)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__089dd3cd1a76a11c5ecbf56e117891054e3675d9eed83514930e859428b620b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isNoPublicIpEnabled")
    def is_no_public_ip_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "isNoPublicIpEnabled"))

    @is_no_public_ip_enabled.setter
    def is_no_public_ip_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14abe54f313d5a7fc0fad331613745aa9f872c809e0c710aa31d3f115e03dd96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isNoPublicIpEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e80203ebb479d8321b6fcb54119a1b34ab68b098103d084239d385381ac20f90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="managedServicesCustomerManagedKeyId")
    def managed_services_customer_managed_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedServicesCustomerManagedKeyId"))

    @managed_services_customer_managed_key_id.setter
    def managed_services_customer_managed_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ff0162df8cecf7ca89a36a8f1fb9aa29ffa42c2d3a3c9e3dd7897c081c91107)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedServicesCustomerManagedKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="networkId")
    def network_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkId"))

    @network_id.setter
    def network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e57322c867461b22a4bb7c1a3e897306537f929aa6b9c7c3cb8402730465a45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkId", value)

    @builtins.property
    @jsii.member(jsii_name="pricingTier")
    def pricing_tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pricingTier"))

    @pricing_tier.setter
    def pricing_tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b2b3609dd8c1000e5d6648c0f040151278b2652b64f1a094c49e22345fbc8a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pricingTier", value)

    @builtins.property
    @jsii.member(jsii_name="privateAccessSettingsId")
    def private_access_settings_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateAccessSettingsId"))

    @private_access_settings_id.setter
    def private_access_settings_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3191601c7e4dc919d523f3077aaace259dce7e54858951d5d268562d38295208)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateAccessSettingsId", value)

    @builtins.property
    @jsii.member(jsii_name="storageConfigurationId")
    def storage_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageConfigurationId"))

    @storage_configuration_id.setter
    def storage_configuration_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d6a1dfa6b7b2b89892e12ae7dd7919cb213535f9bee2dd86dec11bcc209413c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageConfigurationId", value)

    @builtins.property
    @jsii.member(jsii_name="storageCustomerManagedKeyId")
    def storage_customer_managed_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageCustomerManagedKeyId"))

    @storage_customer_managed_key_id.setter
    def storage_customer_managed_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57ddb799358c62928bde43abc996c09bdae0ffeb72a84b37ac299ffa2b021de7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageCustomerManagedKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceId")
    def workspace_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "workspaceId"))

    @workspace_id.setter
    def workspace_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0ce05718b14b09c4c8844a4059c99c1ecf627d9d55d3c63c371f7d123763def)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceId", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceName")
    def workspace_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceName"))

    @workspace_name.setter
    def workspace_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0229516ca06a603d494089f4931d31e8d6bc3e7846991d47e7a826cc6eedb822)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceName", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceStatus")
    def workspace_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceStatus"))

    @workspace_status.setter
    def workspace_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69d214e397878c0ec8a7f275e010cbd7bd0299388a9357e6faed34612aec38a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceStatus", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceStatusMessage")
    def workspace_status_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceStatusMessage"))

    @workspace_status_message.setter
    def workspace_status_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9bb7d32ad4aa29bed8cd56dbe14f3abbd6cea19e3c48d48f710d0ba1e0f7945)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceStatusMessage", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceUrl")
    def workspace_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceUrl"))

    @workspace_url.setter
    def workspace_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6305e317a33fa9015268b511ca1d4c733bbbce161e0e138c61bca82b5eae7da7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceUrl", value)


@jsii.data_type(
    jsii_type="databricks.mwsWorkspaces.MwsWorkspacesCloudResourceContainer",
    jsii_struct_bases=[],
    name_mapping={"gcp": "gcp"},
)
class MwsWorkspacesCloudResourceContainer:
    def __init__(
        self,
        *,
        gcp: typing.Union["MwsWorkspacesCloudResourceContainerGcp", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param gcp: gcp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gcp MwsWorkspaces#gcp}
        '''
        if isinstance(gcp, dict):
            gcp = MwsWorkspacesCloudResourceContainerGcp(**gcp)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a865313bf4e71616e525c02b8971bc80df437cb55ca83d80dd27c21b71e7785)
            check_type(argname="argument gcp", value=gcp, expected_type=type_hints["gcp"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gcp": gcp,
        }

    @builtins.property
    def gcp(self) -> "MwsWorkspacesCloudResourceContainerGcp":
        '''gcp block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gcp MwsWorkspaces#gcp}
        '''
        result = self._values.get("gcp")
        assert result is not None, "Required property 'gcp' is missing"
        return typing.cast("MwsWorkspacesCloudResourceContainerGcp", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsWorkspacesCloudResourceContainer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.mwsWorkspaces.MwsWorkspacesCloudResourceContainerGcp",
    jsii_struct_bases=[],
    name_mapping={"project_id": "projectId"},
)
class MwsWorkspacesCloudResourceContainerGcp:
    def __init__(self, *, project_id: builtins.str) -> None:
        '''
        :param project_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#project_id MwsWorkspaces#project_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e715538b050404d96de16d5e27f817236f8bce327234cc98ed73fa018ba2f6b)
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_id": project_id,
        }

    @builtins.property
    def project_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#project_id MwsWorkspaces#project_id}.'''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsWorkspacesCloudResourceContainerGcp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsWorkspacesCloudResourceContainerGcpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsWorkspaces.MwsWorkspacesCloudResourceContainerGcpOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__82174805c2d098c3be1a597e4c94ba7fa6b6675a82159c75a15ac88db1f465b3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1b30b464b64c17a46b1f1b2f324578ff569a4d45d65f0b9ee6761226dc9c40f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwsWorkspacesCloudResourceContainerGcp]:
        return typing.cast(typing.Optional[MwsWorkspacesCloudResourceContainerGcp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwsWorkspacesCloudResourceContainerGcp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__544fbf94f88dd41e0fc9196469918931839300957f7a8f4f7714b20288b33d39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MwsWorkspacesCloudResourceContainerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsWorkspaces.MwsWorkspacesCloudResourceContainerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2baaeaf0e7b4e5e21190411f9cd0bfe6ccf9cb488fe5e0d8da3c81c254406232)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGcp")
    def put_gcp(self, *, project_id: builtins.str) -> None:
        '''
        :param project_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#project_id MwsWorkspaces#project_id}.
        '''
        value = MwsWorkspacesCloudResourceContainerGcp(project_id=project_id)

        return typing.cast(None, jsii.invoke(self, "putGcp", [value]))

    @builtins.property
    @jsii.member(jsii_name="gcp")
    def gcp(self) -> MwsWorkspacesCloudResourceContainerGcpOutputReference:
        return typing.cast(MwsWorkspacesCloudResourceContainerGcpOutputReference, jsii.get(self, "gcp"))

    @builtins.property
    @jsii.member(jsii_name="gcpInput")
    def gcp_input(self) -> typing.Optional[MwsWorkspacesCloudResourceContainerGcp]:
        return typing.cast(typing.Optional[MwsWorkspacesCloudResourceContainerGcp], jsii.get(self, "gcpInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwsWorkspacesCloudResourceContainer]:
        return typing.cast(typing.Optional[MwsWorkspacesCloudResourceContainer], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwsWorkspacesCloudResourceContainer],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53d824d78a4f4ed22186783515ef678767c04e0abf4afe3ce37e56f4a725f78d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.mwsWorkspaces.MwsWorkspacesConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_id": "accountId",
        "workspace_name": "workspaceName",
        "aws_region": "awsRegion",
        "cloud": "cloud",
        "cloud_resource_container": "cloudResourceContainer",
        "creation_time": "creationTime",
        "credentials_id": "credentialsId",
        "customer_managed_key_id": "customerManagedKeyId",
        "deployment_name": "deploymentName",
        "external_customer_info": "externalCustomerInfo",
        "gcp_managed_network_config": "gcpManagedNetworkConfig",
        "gke_config": "gkeConfig",
        "id": "id",
        "is_no_public_ip_enabled": "isNoPublicIpEnabled",
        "location": "location",
        "managed_services_customer_managed_key_id": "managedServicesCustomerManagedKeyId",
        "network_id": "networkId",
        "pricing_tier": "pricingTier",
        "private_access_settings_id": "privateAccessSettingsId",
        "storage_configuration_id": "storageConfigurationId",
        "storage_customer_managed_key_id": "storageCustomerManagedKeyId",
        "timeouts": "timeouts",
        "token": "token",
        "workspace_id": "workspaceId",
        "workspace_status": "workspaceStatus",
        "workspace_status_message": "workspaceStatusMessage",
        "workspace_url": "workspaceUrl",
    },
)
class MwsWorkspacesConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        account_id: builtins.str,
        workspace_name: builtins.str,
        aws_region: typing.Optional[builtins.str] = None,
        cloud: typing.Optional[builtins.str] = None,
        cloud_resource_container: typing.Optional[typing.Union[MwsWorkspacesCloudResourceContainer, typing.Dict[builtins.str, typing.Any]]] = None,
        creation_time: typing.Optional[jsii.Number] = None,
        credentials_id: typing.Optional[builtins.str] = None,
        customer_managed_key_id: typing.Optional[builtins.str] = None,
        deployment_name: typing.Optional[builtins.str] = None,
        external_customer_info: typing.Optional[typing.Union["MwsWorkspacesExternalCustomerInfo", typing.Dict[builtins.str, typing.Any]]] = None,
        gcp_managed_network_config: typing.Optional[typing.Union["MwsWorkspacesGcpManagedNetworkConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        gke_config: typing.Optional[typing.Union["MwsWorkspacesGkeConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        is_no_public_ip_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        location: typing.Optional[builtins.str] = None,
        managed_services_customer_managed_key_id: typing.Optional[builtins.str] = None,
        network_id: typing.Optional[builtins.str] = None,
        pricing_tier: typing.Optional[builtins.str] = None,
        private_access_settings_id: typing.Optional[builtins.str] = None,
        storage_configuration_id: typing.Optional[builtins.str] = None,
        storage_customer_managed_key_id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MwsWorkspacesTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        token: typing.Optional[typing.Union["MwsWorkspacesToken", typing.Dict[builtins.str, typing.Any]]] = None,
        workspace_id: typing.Optional[jsii.Number] = None,
        workspace_status: typing.Optional[builtins.str] = None,
        workspace_status_message: typing.Optional[builtins.str] = None,
        workspace_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#account_id MwsWorkspaces#account_id}.
        :param workspace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_name MwsWorkspaces#workspace_name}.
        :param aws_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#aws_region MwsWorkspaces#aws_region}.
        :param cloud: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#cloud MwsWorkspaces#cloud}.
        :param cloud_resource_container: cloud_resource_container block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#cloud_resource_container MwsWorkspaces#cloud_resource_container}
        :param creation_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#creation_time MwsWorkspaces#creation_time}.
        :param credentials_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#credentials_id MwsWorkspaces#credentials_id}.
        :param customer_managed_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#customer_managed_key_id MwsWorkspaces#customer_managed_key_id}.
        :param deployment_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#deployment_name MwsWorkspaces#deployment_name}.
        :param external_customer_info: external_customer_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#external_customer_info MwsWorkspaces#external_customer_info}
        :param gcp_managed_network_config: gcp_managed_network_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gcp_managed_network_config MwsWorkspaces#gcp_managed_network_config}
        :param gke_config: gke_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_config MwsWorkspaces#gke_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#id MwsWorkspaces#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_no_public_ip_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#is_no_public_ip_enabled MwsWorkspaces#is_no_public_ip_enabled}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#location MwsWorkspaces#location}.
        :param managed_services_customer_managed_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#managed_services_customer_managed_key_id MwsWorkspaces#managed_services_customer_managed_key_id}.
        :param network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#network_id MwsWorkspaces#network_id}.
        :param pricing_tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#pricing_tier MwsWorkspaces#pricing_tier}.
        :param private_access_settings_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#private_access_settings_id MwsWorkspaces#private_access_settings_id}.
        :param storage_configuration_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#storage_configuration_id MwsWorkspaces#storage_configuration_id}.
        :param storage_customer_managed_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#storage_customer_managed_key_id MwsWorkspaces#storage_customer_managed_key_id}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#timeouts MwsWorkspaces#timeouts}
        :param token: token block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token MwsWorkspaces#token}
        :param workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_id MwsWorkspaces#workspace_id}.
        :param workspace_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_status MwsWorkspaces#workspace_status}.
        :param workspace_status_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_status_message MwsWorkspaces#workspace_status_message}.
        :param workspace_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_url MwsWorkspaces#workspace_url}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cloud_resource_container, dict):
            cloud_resource_container = MwsWorkspacesCloudResourceContainer(**cloud_resource_container)
        if isinstance(external_customer_info, dict):
            external_customer_info = MwsWorkspacesExternalCustomerInfo(**external_customer_info)
        if isinstance(gcp_managed_network_config, dict):
            gcp_managed_network_config = MwsWorkspacesGcpManagedNetworkConfig(**gcp_managed_network_config)
        if isinstance(gke_config, dict):
            gke_config = MwsWorkspacesGkeConfig(**gke_config)
        if isinstance(timeouts, dict):
            timeouts = MwsWorkspacesTimeouts(**timeouts)
        if isinstance(token, dict):
            token = MwsWorkspacesToken(**token)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6d75a44b58628982f84c2f9d3e1d40e5db6a55e0572e37a3e4d6e693f29a8e9)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument workspace_name", value=workspace_name, expected_type=type_hints["workspace_name"])
            check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
            check_type(argname="argument cloud", value=cloud, expected_type=type_hints["cloud"])
            check_type(argname="argument cloud_resource_container", value=cloud_resource_container, expected_type=type_hints["cloud_resource_container"])
            check_type(argname="argument creation_time", value=creation_time, expected_type=type_hints["creation_time"])
            check_type(argname="argument credentials_id", value=credentials_id, expected_type=type_hints["credentials_id"])
            check_type(argname="argument customer_managed_key_id", value=customer_managed_key_id, expected_type=type_hints["customer_managed_key_id"])
            check_type(argname="argument deployment_name", value=deployment_name, expected_type=type_hints["deployment_name"])
            check_type(argname="argument external_customer_info", value=external_customer_info, expected_type=type_hints["external_customer_info"])
            check_type(argname="argument gcp_managed_network_config", value=gcp_managed_network_config, expected_type=type_hints["gcp_managed_network_config"])
            check_type(argname="argument gke_config", value=gke_config, expected_type=type_hints["gke_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_no_public_ip_enabled", value=is_no_public_ip_enabled, expected_type=type_hints["is_no_public_ip_enabled"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument managed_services_customer_managed_key_id", value=managed_services_customer_managed_key_id, expected_type=type_hints["managed_services_customer_managed_key_id"])
            check_type(argname="argument network_id", value=network_id, expected_type=type_hints["network_id"])
            check_type(argname="argument pricing_tier", value=pricing_tier, expected_type=type_hints["pricing_tier"])
            check_type(argname="argument private_access_settings_id", value=private_access_settings_id, expected_type=type_hints["private_access_settings_id"])
            check_type(argname="argument storage_configuration_id", value=storage_configuration_id, expected_type=type_hints["storage_configuration_id"])
            check_type(argname="argument storage_customer_managed_key_id", value=storage_customer_managed_key_id, expected_type=type_hints["storage_customer_managed_key_id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument workspace_id", value=workspace_id, expected_type=type_hints["workspace_id"])
            check_type(argname="argument workspace_status", value=workspace_status, expected_type=type_hints["workspace_status"])
            check_type(argname="argument workspace_status_message", value=workspace_status_message, expected_type=type_hints["workspace_status_message"])
            check_type(argname="argument workspace_url", value=workspace_url, expected_type=type_hints["workspace_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
            "workspace_name": workspace_name,
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
        if aws_region is not None:
            self._values["aws_region"] = aws_region
        if cloud is not None:
            self._values["cloud"] = cloud
        if cloud_resource_container is not None:
            self._values["cloud_resource_container"] = cloud_resource_container
        if creation_time is not None:
            self._values["creation_time"] = creation_time
        if credentials_id is not None:
            self._values["credentials_id"] = credentials_id
        if customer_managed_key_id is not None:
            self._values["customer_managed_key_id"] = customer_managed_key_id
        if deployment_name is not None:
            self._values["deployment_name"] = deployment_name
        if external_customer_info is not None:
            self._values["external_customer_info"] = external_customer_info
        if gcp_managed_network_config is not None:
            self._values["gcp_managed_network_config"] = gcp_managed_network_config
        if gke_config is not None:
            self._values["gke_config"] = gke_config
        if id is not None:
            self._values["id"] = id
        if is_no_public_ip_enabled is not None:
            self._values["is_no_public_ip_enabled"] = is_no_public_ip_enabled
        if location is not None:
            self._values["location"] = location
        if managed_services_customer_managed_key_id is not None:
            self._values["managed_services_customer_managed_key_id"] = managed_services_customer_managed_key_id
        if network_id is not None:
            self._values["network_id"] = network_id
        if pricing_tier is not None:
            self._values["pricing_tier"] = pricing_tier
        if private_access_settings_id is not None:
            self._values["private_access_settings_id"] = private_access_settings_id
        if storage_configuration_id is not None:
            self._values["storage_configuration_id"] = storage_configuration_id
        if storage_customer_managed_key_id is not None:
            self._values["storage_customer_managed_key_id"] = storage_customer_managed_key_id
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if token is not None:
            self._values["token"] = token
        if workspace_id is not None:
            self._values["workspace_id"] = workspace_id
        if workspace_status is not None:
            self._values["workspace_status"] = workspace_status
        if workspace_status_message is not None:
            self._values["workspace_status_message"] = workspace_status_message
        if workspace_url is not None:
            self._values["workspace_url"] = workspace_url

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
    def account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#account_id MwsWorkspaces#account_id}.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_name MwsWorkspaces#workspace_name}.'''
        result = self._values.get("workspace_name")
        assert result is not None, "Required property 'workspace_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#aws_region MwsWorkspaces#aws_region}.'''
        result = self._values.get("aws_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#cloud MwsWorkspaces#cloud}.'''
        result = self._values.get("cloud")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_resource_container(
        self,
    ) -> typing.Optional[MwsWorkspacesCloudResourceContainer]:
        '''cloud_resource_container block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#cloud_resource_container MwsWorkspaces#cloud_resource_container}
        '''
        result = self._values.get("cloud_resource_container")
        return typing.cast(typing.Optional[MwsWorkspacesCloudResourceContainer], result)

    @builtins.property
    def creation_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#creation_time MwsWorkspaces#creation_time}.'''
        result = self._values.get("creation_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def credentials_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#credentials_id MwsWorkspaces#credentials_id}.'''
        result = self._values.get("credentials_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def customer_managed_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#customer_managed_key_id MwsWorkspaces#customer_managed_key_id}.'''
        result = self._values.get("customer_managed_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deployment_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#deployment_name MwsWorkspaces#deployment_name}.'''
        result = self._values.get("deployment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_customer_info(
        self,
    ) -> typing.Optional["MwsWorkspacesExternalCustomerInfo"]:
        '''external_customer_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#external_customer_info MwsWorkspaces#external_customer_info}
        '''
        result = self._values.get("external_customer_info")
        return typing.cast(typing.Optional["MwsWorkspacesExternalCustomerInfo"], result)

    @builtins.property
    def gcp_managed_network_config(
        self,
    ) -> typing.Optional["MwsWorkspacesGcpManagedNetworkConfig"]:
        '''gcp_managed_network_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gcp_managed_network_config MwsWorkspaces#gcp_managed_network_config}
        '''
        result = self._values.get("gcp_managed_network_config")
        return typing.cast(typing.Optional["MwsWorkspacesGcpManagedNetworkConfig"], result)

    @builtins.property
    def gke_config(self) -> typing.Optional["MwsWorkspacesGkeConfig"]:
        '''gke_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_config MwsWorkspaces#gke_config}
        '''
        result = self._values.get("gke_config")
        return typing.cast(typing.Optional["MwsWorkspacesGkeConfig"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#id MwsWorkspaces#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_no_public_ip_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#is_no_public_ip_enabled MwsWorkspaces#is_no_public_ip_enabled}.'''
        result = self._values.get("is_no_public_ip_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#location MwsWorkspaces#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_services_customer_managed_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#managed_services_customer_managed_key_id MwsWorkspaces#managed_services_customer_managed_key_id}.'''
        result = self._values.get("managed_services_customer_managed_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#network_id MwsWorkspaces#network_id}.'''
        result = self._values.get("network_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pricing_tier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#pricing_tier MwsWorkspaces#pricing_tier}.'''
        result = self._values.get("pricing_tier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_access_settings_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#private_access_settings_id MwsWorkspaces#private_access_settings_id}.'''
        result = self._values.get("private_access_settings_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_configuration_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#storage_configuration_id MwsWorkspaces#storage_configuration_id}.'''
        result = self._values.get("storage_configuration_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_customer_managed_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#storage_customer_managed_key_id MwsWorkspaces#storage_customer_managed_key_id}.'''
        result = self._values.get("storage_customer_managed_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MwsWorkspacesTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#timeouts MwsWorkspaces#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MwsWorkspacesTimeouts"], result)

    @builtins.property
    def token(self) -> typing.Optional["MwsWorkspacesToken"]:
        '''token block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token MwsWorkspaces#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional["MwsWorkspacesToken"], result)

    @builtins.property
    def workspace_id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_id MwsWorkspaces#workspace_id}.'''
        result = self._values.get("workspace_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def workspace_status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_status MwsWorkspaces#workspace_status}.'''
        result = self._values.get("workspace_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workspace_status_message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_status_message MwsWorkspaces#workspace_status_message}.'''
        result = self._values.get("workspace_status_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workspace_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#workspace_url MwsWorkspaces#workspace_url}.'''
        result = self._values.get("workspace_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsWorkspacesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.mwsWorkspaces.MwsWorkspacesExternalCustomerInfo",
    jsii_struct_bases=[],
    name_mapping={
        "authoritative_user_email": "authoritativeUserEmail",
        "authoritative_user_full_name": "authoritativeUserFullName",
        "customer_name": "customerName",
    },
)
class MwsWorkspacesExternalCustomerInfo:
    def __init__(
        self,
        *,
        authoritative_user_email: builtins.str,
        authoritative_user_full_name: builtins.str,
        customer_name: builtins.str,
    ) -> None:
        '''
        :param authoritative_user_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#authoritative_user_email MwsWorkspaces#authoritative_user_email}.
        :param authoritative_user_full_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#authoritative_user_full_name MwsWorkspaces#authoritative_user_full_name}.
        :param customer_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#customer_name MwsWorkspaces#customer_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a64a843aa57aa46bac5e25767a74cbb281ad0d903f315946e0beebc3d3dac77)
            check_type(argname="argument authoritative_user_email", value=authoritative_user_email, expected_type=type_hints["authoritative_user_email"])
            check_type(argname="argument authoritative_user_full_name", value=authoritative_user_full_name, expected_type=type_hints["authoritative_user_full_name"])
            check_type(argname="argument customer_name", value=customer_name, expected_type=type_hints["customer_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authoritative_user_email": authoritative_user_email,
            "authoritative_user_full_name": authoritative_user_full_name,
            "customer_name": customer_name,
        }

    @builtins.property
    def authoritative_user_email(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#authoritative_user_email MwsWorkspaces#authoritative_user_email}.'''
        result = self._values.get("authoritative_user_email")
        assert result is not None, "Required property 'authoritative_user_email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authoritative_user_full_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#authoritative_user_full_name MwsWorkspaces#authoritative_user_full_name}.'''
        result = self._values.get("authoritative_user_full_name")
        assert result is not None, "Required property 'authoritative_user_full_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def customer_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#customer_name MwsWorkspaces#customer_name}.'''
        result = self._values.get("customer_name")
        assert result is not None, "Required property 'customer_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsWorkspacesExternalCustomerInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsWorkspacesExternalCustomerInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsWorkspaces.MwsWorkspacesExternalCustomerInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__653dd0c9637fca2f9430970e23e9450d67b64b02e4853d60d5773f167b8b390a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="authoritativeUserEmailInput")
    def authoritative_user_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authoritativeUserEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="authoritativeUserFullNameInput")
    def authoritative_user_full_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authoritativeUserFullNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customerNameInput")
    def customer_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="authoritativeUserEmail")
    def authoritative_user_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authoritativeUserEmail"))

    @authoritative_user_email.setter
    def authoritative_user_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cc575ddb1452c064f994517ddf79225bca27b8db69c01ace97c2167908ea57b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authoritativeUserEmail", value)

    @builtins.property
    @jsii.member(jsii_name="authoritativeUserFullName")
    def authoritative_user_full_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authoritativeUserFullName"))

    @authoritative_user_full_name.setter
    def authoritative_user_full_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44c1b5b43fbc03eacd5dcac7baab62f410c069aa1849392fb82b72885cb109d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authoritativeUserFullName", value)

    @builtins.property
    @jsii.member(jsii_name="customerName")
    def customer_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerName"))

    @customer_name.setter
    def customer_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33b90eb0eaa2c39bcee214f892db3ac7b7a6f584108d38e48f8356ba2911d33f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwsWorkspacesExternalCustomerInfo]:
        return typing.cast(typing.Optional[MwsWorkspacesExternalCustomerInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwsWorkspacesExternalCustomerInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49caf5a565767b56b3b2e5cdfb92dbc4f576748ed22f349771d6a1cdf0ea0882)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.mwsWorkspaces.MwsWorkspacesGcpManagedNetworkConfig",
    jsii_struct_bases=[],
    name_mapping={
        "gke_cluster_pod_ip_range": "gkeClusterPodIpRange",
        "gke_cluster_service_ip_range": "gkeClusterServiceIpRange",
        "subnet_cidr": "subnetCidr",
    },
)
class MwsWorkspacesGcpManagedNetworkConfig:
    def __init__(
        self,
        *,
        gke_cluster_pod_ip_range: builtins.str,
        gke_cluster_service_ip_range: builtins.str,
        subnet_cidr: builtins.str,
    ) -> None:
        '''
        :param gke_cluster_pod_ip_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_cluster_pod_ip_range MwsWorkspaces#gke_cluster_pod_ip_range}.
        :param gke_cluster_service_ip_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_cluster_service_ip_range MwsWorkspaces#gke_cluster_service_ip_range}.
        :param subnet_cidr: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#subnet_cidr MwsWorkspaces#subnet_cidr}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0a3cd858ef80c19fb598e7084f11e3a494adacdead5cf3f5f4470be19d6fd3f)
            check_type(argname="argument gke_cluster_pod_ip_range", value=gke_cluster_pod_ip_range, expected_type=type_hints["gke_cluster_pod_ip_range"])
            check_type(argname="argument gke_cluster_service_ip_range", value=gke_cluster_service_ip_range, expected_type=type_hints["gke_cluster_service_ip_range"])
            check_type(argname="argument subnet_cidr", value=subnet_cidr, expected_type=type_hints["subnet_cidr"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gke_cluster_pod_ip_range": gke_cluster_pod_ip_range,
            "gke_cluster_service_ip_range": gke_cluster_service_ip_range,
            "subnet_cidr": subnet_cidr,
        }

    @builtins.property
    def gke_cluster_pod_ip_range(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_cluster_pod_ip_range MwsWorkspaces#gke_cluster_pod_ip_range}.'''
        result = self._values.get("gke_cluster_pod_ip_range")
        assert result is not None, "Required property 'gke_cluster_pod_ip_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def gke_cluster_service_ip_range(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#gke_cluster_service_ip_range MwsWorkspaces#gke_cluster_service_ip_range}.'''
        result = self._values.get("gke_cluster_service_ip_range")
        assert result is not None, "Required property 'gke_cluster_service_ip_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_cidr(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#subnet_cidr MwsWorkspaces#subnet_cidr}.'''
        result = self._values.get("subnet_cidr")
        assert result is not None, "Required property 'subnet_cidr' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsWorkspacesGcpManagedNetworkConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsWorkspacesGcpManagedNetworkConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsWorkspaces.MwsWorkspacesGcpManagedNetworkConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c5662964fb83714ea18988f0684f825fced13321033f1ab3d88d4603e4b806b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="gkeClusterPodIpRangeInput")
    def gke_cluster_pod_ip_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gkeClusterPodIpRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="gkeClusterServiceIpRangeInput")
    def gke_cluster_service_ip_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gkeClusterServiceIpRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetCidrInput")
    def subnet_cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetCidrInput"))

    @builtins.property
    @jsii.member(jsii_name="gkeClusterPodIpRange")
    def gke_cluster_pod_ip_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gkeClusterPodIpRange"))

    @gke_cluster_pod_ip_range.setter
    def gke_cluster_pod_ip_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6be2095fbfabad7a3267f65c575f7e1017b7615fdf86542aeff74dec10d68918)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gkeClusterPodIpRange", value)

    @builtins.property
    @jsii.member(jsii_name="gkeClusterServiceIpRange")
    def gke_cluster_service_ip_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gkeClusterServiceIpRange"))

    @gke_cluster_service_ip_range.setter
    def gke_cluster_service_ip_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__702655ffe6ed7f74041f406484037137af7062aec9a52365f0151c38a745b89e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gkeClusterServiceIpRange", value)

    @builtins.property
    @jsii.member(jsii_name="subnetCidr")
    def subnet_cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetCidr"))

    @subnet_cidr.setter
    def subnet_cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4af7e003abf4b3603dac13ea41bdaca9dac6646bbfca1551704df370ae362d2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetCidr", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwsWorkspacesGcpManagedNetworkConfig]:
        return typing.cast(typing.Optional[MwsWorkspacesGcpManagedNetworkConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MwsWorkspacesGcpManagedNetworkConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0469ef61ad32dbba6b4c832dcf05298d5964c224031a1f52a7024c49d5d0319)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.mwsWorkspaces.MwsWorkspacesGkeConfig",
    jsii_struct_bases=[],
    name_mapping={
        "connectivity_type": "connectivityType",
        "master_ip_range": "masterIpRange",
    },
)
class MwsWorkspacesGkeConfig:
    def __init__(
        self,
        *,
        connectivity_type: builtins.str,
        master_ip_range: builtins.str,
    ) -> None:
        '''
        :param connectivity_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#connectivity_type MwsWorkspaces#connectivity_type}.
        :param master_ip_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#master_ip_range MwsWorkspaces#master_ip_range}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49a88226c19992c2342778c42b9673b3cc4a83e6fbbedd0fb244509bf533f4c9)
            check_type(argname="argument connectivity_type", value=connectivity_type, expected_type=type_hints["connectivity_type"])
            check_type(argname="argument master_ip_range", value=master_ip_range, expected_type=type_hints["master_ip_range"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connectivity_type": connectivity_type,
            "master_ip_range": master_ip_range,
        }

    @builtins.property
    def connectivity_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#connectivity_type MwsWorkspaces#connectivity_type}.'''
        result = self._values.get("connectivity_type")
        assert result is not None, "Required property 'connectivity_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def master_ip_range(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#master_ip_range MwsWorkspaces#master_ip_range}.'''
        result = self._values.get("master_ip_range")
        assert result is not None, "Required property 'master_ip_range' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsWorkspacesGkeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsWorkspacesGkeConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsWorkspaces.MwsWorkspacesGkeConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f133155bce6f48f15fe1e96aaa2306d1a4608b3edc47e89591c1a6f6aed13a0a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="connectivityTypeInput")
    def connectivity_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectivityTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="masterIpRangeInput")
    def master_ip_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterIpRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="connectivityType")
    def connectivity_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectivityType"))

    @connectivity_type.setter
    def connectivity_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d637f94377e13d17bcfb937c4fab1c2735d8ce53a2cee864abc1797e0fd7aed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectivityType", value)

    @builtins.property
    @jsii.member(jsii_name="masterIpRange")
    def master_ip_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterIpRange"))

    @master_ip_range.setter
    def master_ip_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b2df5a4b10a5671a4d320f5b07f7f5ea4f7b4d662ec07cbb20c8e4f968f253e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterIpRange", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwsWorkspacesGkeConfig]:
        return typing.cast(typing.Optional[MwsWorkspacesGkeConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MwsWorkspacesGkeConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0549f6c4b7e760c06fb890e6459198fb007b86e5034fa6256ea4e6bbe40bd253)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.mwsWorkspaces.MwsWorkspacesTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "read": "read", "update": "update"},
)
class MwsWorkspacesTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#create MwsWorkspaces#create}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#read MwsWorkspaces#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#update MwsWorkspaces#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec6e5cc8c345351284d9fb3d3c6846a471407e3c370cf8cfe61db81b2d808fed)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#create MwsWorkspaces#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#read MwsWorkspaces#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#update MwsWorkspaces#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsWorkspacesTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsWorkspacesTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsWorkspaces.MwsWorkspacesTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b2c1c185892b6f9355c2b9cdc8216e8758f49f52ca05e651437db3a1c6e084f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8b9d893b1ec6710ac54ea676825e78e6384129412e69d609dac5ffeae059499)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5e21d572a34379fa8e8daa4705d138145721a7bb0d6afbd2f3b2e115a3734b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65ceff66922641dde755d8e16b9327bc60b71296873fe9925f42ec386af571b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MwsWorkspacesTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MwsWorkspacesTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MwsWorkspacesTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ca406ff22339bea34de942601d1a4ad704e93f1a00b6f6bebc2a6c62d57cf66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.mwsWorkspaces.MwsWorkspacesToken",
    jsii_struct_bases=[],
    name_mapping={
        "comment": "comment",
        "lifetime_seconds": "lifetimeSeconds",
        "token_id": "tokenId",
        "token_value": "tokenValue",
    },
)
class MwsWorkspacesToken:
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        lifetime_seconds: typing.Optional[jsii.Number] = None,
        token_id: typing.Optional[builtins.str] = None,
        token_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#comment MwsWorkspaces#comment}.
        :param lifetime_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#lifetime_seconds MwsWorkspaces#lifetime_seconds}.
        :param token_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token_id MwsWorkspaces#token_id}.
        :param token_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token_value MwsWorkspaces#token_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3bd45c6e38eaf116642f70e24e0b3490c435a250268103e714da01a0a6b3cd3)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument lifetime_seconds", value=lifetime_seconds, expected_type=type_hints["lifetime_seconds"])
            check_type(argname="argument token_id", value=token_id, expected_type=type_hints["token_id"])
            check_type(argname="argument token_value", value=token_value, expected_type=type_hints["token_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if lifetime_seconds is not None:
            self._values["lifetime_seconds"] = lifetime_seconds
        if token_id is not None:
            self._values["token_id"] = token_id
        if token_value is not None:
            self._values["token_value"] = token_value

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#comment MwsWorkspaces#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifetime_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#lifetime_seconds MwsWorkspaces#lifetime_seconds}.'''
        result = self._values.get("lifetime_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token_id MwsWorkspaces#token_id}.'''
        result = self._values.get("token_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_workspaces#token_value MwsWorkspaces#token_value}.'''
        result = self._values.get("token_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsWorkspacesToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MwsWorkspacesTokenOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.mwsWorkspaces.MwsWorkspacesTokenOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea50cece29c7bc7e87e5d3a0cb37d8d4700900118f6508746fb2c2a3860095c9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetLifetimeSeconds")
    def reset_lifetime_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifetimeSeconds", []))

    @jsii.member(jsii_name="resetTokenId")
    def reset_token_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenId", []))

    @jsii.member(jsii_name="resetTokenValue")
    def reset_token_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenValue", []))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="lifetimeSecondsInput")
    def lifetime_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lifetimeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenIdInput")
    def token_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenValueInput")
    def token_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenValueInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f78b4e7983858b529dc0581621af3578757fd542f208842c7e773fb6cb76adec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="lifetimeSeconds")
    def lifetime_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lifetimeSeconds"))

    @lifetime_seconds.setter
    def lifetime_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d62fb800091cc289e2ded238a7c37cabbb32e4fffd1f9112f0c2f2e89f8e523d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifetimeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tokenId")
    def token_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenId"))

    @token_id.setter
    def token_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d38a2c487dedb89aa391e5508336e7b78fe63696f24200fb63005dfde42b80a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenId", value)

    @builtins.property
    @jsii.member(jsii_name="tokenValue")
    def token_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenValue"))

    @token_value.setter
    def token_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fa9f42f3ee7e81d38b38c28c38f9d1e86585adf5d2191c7a35c9fc00b2a5b70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MwsWorkspacesToken]:
        return typing.cast(typing.Optional[MwsWorkspacesToken], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MwsWorkspacesToken]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12b455fbbe92c37a16540e30b6d573f45e7eb7f8db56e82aa1c5108a3a032bdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MwsWorkspaces",
    "MwsWorkspacesCloudResourceContainer",
    "MwsWorkspacesCloudResourceContainerGcp",
    "MwsWorkspacesCloudResourceContainerGcpOutputReference",
    "MwsWorkspacesCloudResourceContainerOutputReference",
    "MwsWorkspacesConfig",
    "MwsWorkspacesExternalCustomerInfo",
    "MwsWorkspacesExternalCustomerInfoOutputReference",
    "MwsWorkspacesGcpManagedNetworkConfig",
    "MwsWorkspacesGcpManagedNetworkConfigOutputReference",
    "MwsWorkspacesGkeConfig",
    "MwsWorkspacesGkeConfigOutputReference",
    "MwsWorkspacesTimeouts",
    "MwsWorkspacesTimeoutsOutputReference",
    "MwsWorkspacesToken",
    "MwsWorkspacesTokenOutputReference",
]

publication.publish()

def _typecheckingstub__0706cd5c9907c8b2f0d0dc4529ff6077959730ca71d7c750bdcbe6b9d0a904a9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    account_id: builtins.str,
    workspace_name: builtins.str,
    aws_region: typing.Optional[builtins.str] = None,
    cloud: typing.Optional[builtins.str] = None,
    cloud_resource_container: typing.Optional[typing.Union[MwsWorkspacesCloudResourceContainer, typing.Dict[builtins.str, typing.Any]]] = None,
    creation_time: typing.Optional[jsii.Number] = None,
    credentials_id: typing.Optional[builtins.str] = None,
    customer_managed_key_id: typing.Optional[builtins.str] = None,
    deployment_name: typing.Optional[builtins.str] = None,
    external_customer_info: typing.Optional[typing.Union[MwsWorkspacesExternalCustomerInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    gcp_managed_network_config: typing.Optional[typing.Union[MwsWorkspacesGcpManagedNetworkConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    gke_config: typing.Optional[typing.Union[MwsWorkspacesGkeConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    is_no_public_ip_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    location: typing.Optional[builtins.str] = None,
    managed_services_customer_managed_key_id: typing.Optional[builtins.str] = None,
    network_id: typing.Optional[builtins.str] = None,
    pricing_tier: typing.Optional[builtins.str] = None,
    private_access_settings_id: typing.Optional[builtins.str] = None,
    storage_configuration_id: typing.Optional[builtins.str] = None,
    storage_customer_managed_key_id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[MwsWorkspacesTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    token: typing.Optional[typing.Union[MwsWorkspacesToken, typing.Dict[builtins.str, typing.Any]]] = None,
    workspace_id: typing.Optional[jsii.Number] = None,
    workspace_status: typing.Optional[builtins.str] = None,
    workspace_status_message: typing.Optional[builtins.str] = None,
    workspace_url: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__8fc8a25da3f04303a2168a06b1f4e1014ebfadf671ed3ea5b77b4b060cceeb48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e86ce2d6f650902fedda21daa708c0cc7df0078a74ec0cef7a10aea3d9fb2644(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cdf64f7ef5066277c447d606d73a723fb851bbe5faa884b8480129ad0fafc63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56955ed99d9529c31b3d821027c6a65ebe01405a34c1954bda53794a2f559422(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e1a3fab67362234a71fa1fba628a0de6eb6b85bdf0bb1d56a28d31f147e44b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__646722ca86daaddfc5212527cece12c4dbc9c65851c23ff757cc760b2268e96a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ccea7cc66c3fd342428907ed3b23beb94d36386d3ad71163e977091a8943256(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__089dd3cd1a76a11c5ecbf56e117891054e3675d9eed83514930e859428b620b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14abe54f313d5a7fc0fad331613745aa9f872c809e0c710aa31d3f115e03dd96(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e80203ebb479d8321b6fcb54119a1b34ab68b098103d084239d385381ac20f90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ff0162df8cecf7ca89a36a8f1fb9aa29ffa42c2d3a3c9e3dd7897c081c91107(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e57322c867461b22a4bb7c1a3e897306537f929aa6b9c7c3cb8402730465a45(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b2b3609dd8c1000e5d6648c0f040151278b2652b64f1a094c49e22345fbc8a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3191601c7e4dc919d523f3077aaace259dce7e54858951d5d268562d38295208(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d6a1dfa6b7b2b89892e12ae7dd7919cb213535f9bee2dd86dec11bcc209413c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57ddb799358c62928bde43abc996c09bdae0ffeb72a84b37ac299ffa2b021de7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0ce05718b14b09c4c8844a4059c99c1ecf627d9d55d3c63c371f7d123763def(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0229516ca06a603d494089f4931d31e8d6bc3e7846991d47e7a826cc6eedb822(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69d214e397878c0ec8a7f275e010cbd7bd0299388a9357e6faed34612aec38a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9bb7d32ad4aa29bed8cd56dbe14f3abbd6cea19e3c48d48f710d0ba1e0f7945(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6305e317a33fa9015268b511ca1d4c733bbbce161e0e138c61bca82b5eae7da7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a865313bf4e71616e525c02b8971bc80df437cb55ca83d80dd27c21b71e7785(
    *,
    gcp: typing.Union[MwsWorkspacesCloudResourceContainerGcp, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e715538b050404d96de16d5e27f817236f8bce327234cc98ed73fa018ba2f6b(
    *,
    project_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82174805c2d098c3be1a597e4c94ba7fa6b6675a82159c75a15ac88db1f465b3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1b30b464b64c17a46b1f1b2f324578ff569a4d45d65f0b9ee6761226dc9c40f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__544fbf94f88dd41e0fc9196469918931839300957f7a8f4f7714b20288b33d39(
    value: typing.Optional[MwsWorkspacesCloudResourceContainerGcp],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2baaeaf0e7b4e5e21190411f9cd0bfe6ccf9cb488fe5e0d8da3c81c254406232(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53d824d78a4f4ed22186783515ef678767c04e0abf4afe3ce37e56f4a725f78d(
    value: typing.Optional[MwsWorkspacesCloudResourceContainer],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6d75a44b58628982f84c2f9d3e1d40e5db6a55e0572e37a3e4d6e693f29a8e9(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    account_id: builtins.str,
    workspace_name: builtins.str,
    aws_region: typing.Optional[builtins.str] = None,
    cloud: typing.Optional[builtins.str] = None,
    cloud_resource_container: typing.Optional[typing.Union[MwsWorkspacesCloudResourceContainer, typing.Dict[builtins.str, typing.Any]]] = None,
    creation_time: typing.Optional[jsii.Number] = None,
    credentials_id: typing.Optional[builtins.str] = None,
    customer_managed_key_id: typing.Optional[builtins.str] = None,
    deployment_name: typing.Optional[builtins.str] = None,
    external_customer_info: typing.Optional[typing.Union[MwsWorkspacesExternalCustomerInfo, typing.Dict[builtins.str, typing.Any]]] = None,
    gcp_managed_network_config: typing.Optional[typing.Union[MwsWorkspacesGcpManagedNetworkConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    gke_config: typing.Optional[typing.Union[MwsWorkspacesGkeConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    is_no_public_ip_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    location: typing.Optional[builtins.str] = None,
    managed_services_customer_managed_key_id: typing.Optional[builtins.str] = None,
    network_id: typing.Optional[builtins.str] = None,
    pricing_tier: typing.Optional[builtins.str] = None,
    private_access_settings_id: typing.Optional[builtins.str] = None,
    storage_configuration_id: typing.Optional[builtins.str] = None,
    storage_customer_managed_key_id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[MwsWorkspacesTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    token: typing.Optional[typing.Union[MwsWorkspacesToken, typing.Dict[builtins.str, typing.Any]]] = None,
    workspace_id: typing.Optional[jsii.Number] = None,
    workspace_status: typing.Optional[builtins.str] = None,
    workspace_status_message: typing.Optional[builtins.str] = None,
    workspace_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a64a843aa57aa46bac5e25767a74cbb281ad0d903f315946e0beebc3d3dac77(
    *,
    authoritative_user_email: builtins.str,
    authoritative_user_full_name: builtins.str,
    customer_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__653dd0c9637fca2f9430970e23e9450d67b64b02e4853d60d5773f167b8b390a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cc575ddb1452c064f994517ddf79225bca27b8db69c01ace97c2167908ea57b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44c1b5b43fbc03eacd5dcac7baab62f410c069aa1849392fb82b72885cb109d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33b90eb0eaa2c39bcee214f892db3ac7b7a6f584108d38e48f8356ba2911d33f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49caf5a565767b56b3b2e5cdfb92dbc4f576748ed22f349771d6a1cdf0ea0882(
    value: typing.Optional[MwsWorkspacesExternalCustomerInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0a3cd858ef80c19fb598e7084f11e3a494adacdead5cf3f5f4470be19d6fd3f(
    *,
    gke_cluster_pod_ip_range: builtins.str,
    gke_cluster_service_ip_range: builtins.str,
    subnet_cidr: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c5662964fb83714ea18988f0684f825fced13321033f1ab3d88d4603e4b806b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6be2095fbfabad7a3267f65c575f7e1017b7615fdf86542aeff74dec10d68918(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__702655ffe6ed7f74041f406484037137af7062aec9a52365f0151c38a745b89e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4af7e003abf4b3603dac13ea41bdaca9dac6646bbfca1551704df370ae362d2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0469ef61ad32dbba6b4c832dcf05298d5964c224031a1f52a7024c49d5d0319(
    value: typing.Optional[MwsWorkspacesGcpManagedNetworkConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49a88226c19992c2342778c42b9673b3cc4a83e6fbbedd0fb244509bf533f4c9(
    *,
    connectivity_type: builtins.str,
    master_ip_range: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f133155bce6f48f15fe1e96aaa2306d1a4608b3edc47e89591c1a6f6aed13a0a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d637f94377e13d17bcfb937c4fab1c2735d8ce53a2cee864abc1797e0fd7aed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b2df5a4b10a5671a4d320f5b07f7f5ea4f7b4d662ec07cbb20c8e4f968f253e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0549f6c4b7e760c06fb890e6459198fb007b86e5034fa6256ea4e6bbe40bd253(
    value: typing.Optional[MwsWorkspacesGkeConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec6e5cc8c345351284d9fb3d3c6846a471407e3c370cf8cfe61db81b2d808fed(
    *,
    create: typing.Optional[builtins.str] = None,
    read: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b2c1c185892b6f9355c2b9cdc8216e8758f49f52ca05e651437db3a1c6e084f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8b9d893b1ec6710ac54ea676825e78e6384129412e69d609dac5ffeae059499(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5e21d572a34379fa8e8daa4705d138145721a7bb0d6afbd2f3b2e115a3734b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65ceff66922641dde755d8e16b9327bc60b71296873fe9925f42ec386af571b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ca406ff22339bea34de942601d1a4ad704e93f1a00b6f6bebc2a6c62d57cf66(
    value: typing.Optional[typing.Union[MwsWorkspacesTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3bd45c6e38eaf116642f70e24e0b3490c435a250268103e714da01a0a6b3cd3(
    *,
    comment: typing.Optional[builtins.str] = None,
    lifetime_seconds: typing.Optional[jsii.Number] = None,
    token_id: typing.Optional[builtins.str] = None,
    token_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea50cece29c7bc7e87e5d3a0cb37d8d4700900118f6508746fb2c2a3860095c9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f78b4e7983858b529dc0581621af3578757fd542f208842c7e773fb6cb76adec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d62fb800091cc289e2ded238a7c37cabbb32e4fffd1f9112f0c2f2e89f8e523d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d38a2c487dedb89aa391e5508336e7b78fe63696f24200fb63005dfde42b80a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fa9f42f3ee7e81d38b38c28c38f9d1e86585adf5d2191c7a35c9fc00b2a5b70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12b455fbbe92c37a16540e30b6d573f45e7eb7f8db56e82aa1c5108a3a032bdb(
    value: typing.Optional[MwsWorkspacesToken],
) -> None:
    """Type checking stubs"""
    pass
