'''
# `databricks_instance_pool`

Refer to the Terraform Registory for docs: [`databricks_instance_pool`](https://www.terraform.io/docs/providers/databricks/r/instance_pool).
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


class InstancePool(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.instancePool.InstancePool",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool databricks_instance_pool}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        idle_instance_autotermination_minutes: jsii.Number,
        instance_pool_name: builtins.str,
        aws_attributes: typing.Optional[typing.Union["InstancePoolAwsAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_attributes: typing.Optional[typing.Union["InstancePoolAzureAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        disk_spec: typing.Optional[typing.Union["InstancePoolDiskSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        gcp_attributes: typing.Optional[typing.Union["InstancePoolGcpAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        instance_pool_fleet_attributes: typing.Optional[typing.Union["InstancePoolInstancePoolFleetAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        instance_pool_id: typing.Optional[builtins.str] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_idle_instances: typing.Optional[jsii.Number] = None,
        node_type_id: typing.Optional[builtins.str] = None,
        preloaded_docker_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["InstancePoolPreloadedDockerImage", typing.Dict[builtins.str, typing.Any]]]]] = None,
        preloaded_spark_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool databricks_instance_pool} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param idle_instance_autotermination_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#idle_instance_autotermination_minutes InstancePool#idle_instance_autotermination_minutes}.
        :param instance_pool_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#instance_pool_name InstancePool#instance_pool_name}.
        :param aws_attributes: aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#aws_attributes InstancePool#aws_attributes}
        :param azure_attributes: azure_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#azure_attributes InstancePool#azure_attributes}
        :param custom_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#custom_tags InstancePool#custom_tags}.
        :param disk_spec: disk_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#disk_spec InstancePool#disk_spec}
        :param enable_elastic_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#enable_elastic_disk InstancePool#enable_elastic_disk}.
        :param gcp_attributes: gcp_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#gcp_attributes InstancePool#gcp_attributes}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#id InstancePool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_pool_fleet_attributes: instance_pool_fleet_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#instance_pool_fleet_attributes InstancePool#instance_pool_fleet_attributes}
        :param instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#instance_pool_id InstancePool#instance_pool_id}.
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#max_capacity InstancePool#max_capacity}.
        :param min_idle_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#min_idle_instances InstancePool#min_idle_instances}.
        :param node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#node_type_id InstancePool#node_type_id}.
        :param preloaded_docker_image: preloaded_docker_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#preloaded_docker_image InstancePool#preloaded_docker_image}
        :param preloaded_spark_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#preloaded_spark_versions InstancePool#preloaded_spark_versions}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5ea839c8aaa9545921e314cf9efda0b91a853802dd7dcddd32bdfa1fda6e78a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = InstancePoolConfig(
            idle_instance_autotermination_minutes=idle_instance_autotermination_minutes,
            instance_pool_name=instance_pool_name,
            aws_attributes=aws_attributes,
            azure_attributes=azure_attributes,
            custom_tags=custom_tags,
            disk_spec=disk_spec,
            enable_elastic_disk=enable_elastic_disk,
            gcp_attributes=gcp_attributes,
            id=id,
            instance_pool_fleet_attributes=instance_pool_fleet_attributes,
            instance_pool_id=instance_pool_id,
            max_capacity=max_capacity,
            min_idle_instances=min_idle_instances,
            node_type_id=node_type_id,
            preloaded_docker_image=preloaded_docker_image,
            preloaded_spark_versions=preloaded_spark_versions,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAwsAttributes")
    def put_aws_attributes(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        spot_bid_price_percent: typing.Optional[jsii.Number] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#availability InstancePool#availability}.
        :param spot_bid_price_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#spot_bid_price_percent InstancePool#spot_bid_price_percent}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#zone_id InstancePool#zone_id}.
        '''
        value = InstancePoolAwsAttributes(
            availability=availability,
            spot_bid_price_percent=spot_bid_price_percent,
            zone_id=zone_id,
        )

        return typing.cast(None, jsii.invoke(self, "putAwsAttributes", [value]))

    @jsii.member(jsii_name="putAzureAttributes")
    def put_azure_attributes(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        spot_bid_max_price: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#availability InstancePool#availability}.
        :param spot_bid_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#spot_bid_max_price InstancePool#spot_bid_max_price}.
        '''
        value = InstancePoolAzureAttributes(
            availability=availability, spot_bid_max_price=spot_bid_max_price
        )

        return typing.cast(None, jsii.invoke(self, "putAzureAttributes", [value]))

    @jsii.member(jsii_name="putDiskSpec")
    def put_disk_spec(
        self,
        *,
        disk_count: typing.Optional[jsii.Number] = None,
        disk_size: typing.Optional[jsii.Number] = None,
        disk_type: typing.Optional[typing.Union["InstancePoolDiskSpecDiskType", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param disk_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#disk_count InstancePool#disk_count}.
        :param disk_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#disk_size InstancePool#disk_size}.
        :param disk_type: disk_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#disk_type InstancePool#disk_type}
        '''
        value = InstancePoolDiskSpec(
            disk_count=disk_count, disk_size=disk_size, disk_type=disk_type
        )

        return typing.cast(None, jsii.invoke(self, "putDiskSpec", [value]))

    @jsii.member(jsii_name="putGcpAttributes")
    def put_gcp_attributes(
        self,
        *,
        gcp_availability: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param gcp_availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#gcp_availability InstancePool#gcp_availability}.
        '''
        value = InstancePoolGcpAttributes(gcp_availability=gcp_availability)

        return typing.cast(None, jsii.invoke(self, "putGcpAttributes", [value]))

    @jsii.member(jsii_name="putInstancePoolFleetAttributes")
    def put_instance_pool_fleet_attributes(
        self,
        *,
        launch_template_override: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride", typing.Dict[builtins.str, typing.Any]]]],
        fleet_on_demand_option: typing.Optional[typing.Union["InstancePoolInstancePoolFleetAttributesFleetOnDemandOption", typing.Dict[builtins.str, typing.Any]]] = None,
        fleet_spot_option: typing.Optional[typing.Union["InstancePoolInstancePoolFleetAttributesFleetSpotOption", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param launch_template_override: launch_template_override block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#launch_template_override InstancePool#launch_template_override}
        :param fleet_on_demand_option: fleet_on_demand_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#fleet_on_demand_option InstancePool#fleet_on_demand_option}
        :param fleet_spot_option: fleet_spot_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#fleet_spot_option InstancePool#fleet_spot_option}
        '''
        value = InstancePoolInstancePoolFleetAttributes(
            launch_template_override=launch_template_override,
            fleet_on_demand_option=fleet_on_demand_option,
            fleet_spot_option=fleet_spot_option,
        )

        return typing.cast(None, jsii.invoke(self, "putInstancePoolFleetAttributes", [value]))

    @jsii.member(jsii_name="putPreloadedDockerImage")
    def put_preloaded_docker_image(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["InstancePoolPreloadedDockerImage", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dbd35f6c97620051b66be8ec8f4723b3e4f59d9fc43331542922b4adf6785d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPreloadedDockerImage", [value]))

    @jsii.member(jsii_name="resetAwsAttributes")
    def reset_aws_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsAttributes", []))

    @jsii.member(jsii_name="resetAzureAttributes")
    def reset_azure_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureAttributes", []))

    @jsii.member(jsii_name="resetCustomTags")
    def reset_custom_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomTags", []))

    @jsii.member(jsii_name="resetDiskSpec")
    def reset_disk_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSpec", []))

    @jsii.member(jsii_name="resetEnableElasticDisk")
    def reset_enable_elastic_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableElasticDisk", []))

    @jsii.member(jsii_name="resetGcpAttributes")
    def reset_gcp_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpAttributes", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstancePoolFleetAttributes")
    def reset_instance_pool_fleet_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancePoolFleetAttributes", []))

    @jsii.member(jsii_name="resetInstancePoolId")
    def reset_instance_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancePoolId", []))

    @jsii.member(jsii_name="resetMaxCapacity")
    def reset_max_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxCapacity", []))

    @jsii.member(jsii_name="resetMinIdleInstances")
    def reset_min_idle_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinIdleInstances", []))

    @jsii.member(jsii_name="resetNodeTypeId")
    def reset_node_type_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeTypeId", []))

    @jsii.member(jsii_name="resetPreloadedDockerImage")
    def reset_preloaded_docker_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreloadedDockerImage", []))

    @jsii.member(jsii_name="resetPreloadedSparkVersions")
    def reset_preloaded_spark_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreloadedSparkVersions", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="awsAttributes")
    def aws_attributes(self) -> "InstancePoolAwsAttributesOutputReference":
        return typing.cast("InstancePoolAwsAttributesOutputReference", jsii.get(self, "awsAttributes"))

    @builtins.property
    @jsii.member(jsii_name="azureAttributes")
    def azure_attributes(self) -> "InstancePoolAzureAttributesOutputReference":
        return typing.cast("InstancePoolAzureAttributesOutputReference", jsii.get(self, "azureAttributes"))

    @builtins.property
    @jsii.member(jsii_name="diskSpec")
    def disk_spec(self) -> "InstancePoolDiskSpecOutputReference":
        return typing.cast("InstancePoolDiskSpecOutputReference", jsii.get(self, "diskSpec"))

    @builtins.property
    @jsii.member(jsii_name="gcpAttributes")
    def gcp_attributes(self) -> "InstancePoolGcpAttributesOutputReference":
        return typing.cast("InstancePoolGcpAttributesOutputReference", jsii.get(self, "gcpAttributes"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolFleetAttributes")
    def instance_pool_fleet_attributes(
        self,
    ) -> "InstancePoolInstancePoolFleetAttributesOutputReference":
        return typing.cast("InstancePoolInstancePoolFleetAttributesOutputReference", jsii.get(self, "instancePoolFleetAttributes"))

    @builtins.property
    @jsii.member(jsii_name="preloadedDockerImage")
    def preloaded_docker_image(self) -> "InstancePoolPreloadedDockerImageList":
        return typing.cast("InstancePoolPreloadedDockerImageList", jsii.get(self, "preloadedDockerImage"))

    @builtins.property
    @jsii.member(jsii_name="awsAttributesInput")
    def aws_attributes_input(self) -> typing.Optional["InstancePoolAwsAttributes"]:
        return typing.cast(typing.Optional["InstancePoolAwsAttributes"], jsii.get(self, "awsAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="azureAttributesInput")
    def azure_attributes_input(self) -> typing.Optional["InstancePoolAzureAttributes"]:
        return typing.cast(typing.Optional["InstancePoolAzureAttributes"], jsii.get(self, "azureAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="customTagsInput")
    def custom_tags_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSpecInput")
    def disk_spec_input(self) -> typing.Optional["InstancePoolDiskSpec"]:
        return typing.cast(typing.Optional["InstancePoolDiskSpec"], jsii.get(self, "diskSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="enableElasticDiskInput")
    def enable_elastic_disk_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableElasticDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="gcpAttributesInput")
    def gcp_attributes_input(self) -> typing.Optional["InstancePoolGcpAttributes"]:
        return typing.cast(typing.Optional["InstancePoolGcpAttributes"], jsii.get(self, "gcpAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="idleInstanceAutoterminationMinutesInput")
    def idle_instance_autotermination_minutes_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleInstanceAutoterminationMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolFleetAttributesInput")
    def instance_pool_fleet_attributes_input(
        self,
    ) -> typing.Optional["InstancePoolInstancePoolFleetAttributes"]:
        return typing.cast(typing.Optional["InstancePoolInstancePoolFleetAttributes"], jsii.get(self, "instancePoolFleetAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolIdInput")
    def instance_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instancePoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolNameInput")
    def instance_pool_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instancePoolNameInput"))

    @builtins.property
    @jsii.member(jsii_name="maxCapacityInput")
    def max_capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCapacityInput"))

    @builtins.property
    @jsii.member(jsii_name="minIdleInstancesInput")
    def min_idle_instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minIdleInstancesInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeTypeIdInput")
    def node_type_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeTypeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="preloadedDockerImageInput")
    def preloaded_docker_image_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstancePoolPreloadedDockerImage"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstancePoolPreloadedDockerImage"]]], jsii.get(self, "preloadedDockerImageInput"))

    @builtins.property
    @jsii.member(jsii_name="preloadedSparkVersionsInput")
    def preloaded_spark_versions_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "preloadedSparkVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="customTags")
    def custom_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customTags"))

    @custom_tags.setter
    def custom_tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15c429b17414a942f1c0c22d0547c0caa43c7b7637e079c39561a2c3dba098b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customTags", value)

    @builtins.property
    @jsii.member(jsii_name="enableElasticDisk")
    def enable_elastic_disk(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableElasticDisk"))

    @enable_elastic_disk.setter
    def enable_elastic_disk(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfa2eaf59f275f122b02a3ae43a672d7c8793458189437fa8b76c7c2b8ea5ce0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableElasticDisk", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9cb2a33e88be8cef92a32206e6a8e62c52dd392939c77ad2f65fe92c41c1920)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="idleInstanceAutoterminationMinutes")
    def idle_instance_autotermination_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleInstanceAutoterminationMinutes"))

    @idle_instance_autotermination_minutes.setter
    def idle_instance_autotermination_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91e290646897ef29f579923558e41f53fb4ef8919a0baa3deb5d72a7a3067eb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleInstanceAutoterminationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="instancePoolId")
    def instance_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instancePoolId"))

    @instance_pool_id.setter
    def instance_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de082ad17e4f3fdbb468936de92ebf1d89da2eb7dfdc97ad624b02173e90e1e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instancePoolId", value)

    @builtins.property
    @jsii.member(jsii_name="instancePoolName")
    def instance_pool_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instancePoolName"))

    @instance_pool_name.setter
    def instance_pool_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d49679b82068420a96b74d53ff885c42be3a802b4334eee121c49d3392dd2d98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instancePoolName", value)

    @builtins.property
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxCapacity"))

    @max_capacity.setter
    def max_capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0a0efd524649d11b5b14e2eed536f1f349f33c3de76eed14000a4efcb0e05ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="minIdleInstances")
    def min_idle_instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minIdleInstances"))

    @min_idle_instances.setter
    def min_idle_instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bf640f3d08684315d975758ebc042fdcd41dc9c9dbe362363e499c8c9593d5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minIdleInstances", value)

    @builtins.property
    @jsii.member(jsii_name="nodeTypeId")
    def node_type_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeTypeId"))

    @node_type_id.setter
    def node_type_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5c6ac6f0ef4f8890f0b2319a44b648e33ef5d877d59a575062a68a46f742541)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeTypeId", value)

    @builtins.property
    @jsii.member(jsii_name="preloadedSparkVersions")
    def preloaded_spark_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "preloadedSparkVersions"))

    @preloaded_spark_versions.setter
    def preloaded_spark_versions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8013f36da9777061d56e74fba94313ad047157770657b2ce8cd020c2c13d9c60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preloadedSparkVersions", value)


@jsii.data_type(
    jsii_type="databricks.instancePool.InstancePoolAwsAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "spot_bid_price_percent": "spotBidPricePercent",
        "zone_id": "zoneId",
    },
)
class InstancePoolAwsAttributes:
    def __init__(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        spot_bid_price_percent: typing.Optional[jsii.Number] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#availability InstancePool#availability}.
        :param spot_bid_price_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#spot_bid_price_percent InstancePool#spot_bid_price_percent}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#zone_id InstancePool#zone_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba22b2c379432da4cf4b0709c4edff67e90219e41756dd205b3fc7c0da1b18a7)
            check_type(argname="argument availability", value=availability, expected_type=type_hints["availability"])
            check_type(argname="argument spot_bid_price_percent", value=spot_bid_price_percent, expected_type=type_hints["spot_bid_price_percent"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability is not None:
            self._values["availability"] = availability
        if spot_bid_price_percent is not None:
            self._values["spot_bid_price_percent"] = spot_bid_price_percent
        if zone_id is not None:
            self._values["zone_id"] = zone_id

    @builtins.property
    def availability(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#availability InstancePool#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_bid_price_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#spot_bid_price_percent InstancePool#spot_bid_price_percent}.'''
        result = self._values.get("spot_bid_price_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#zone_id InstancePool#zone_id}.'''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstancePoolAwsAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstancePoolAwsAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.instancePool.InstancePoolAwsAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__07602bc492766916dca591b5a2d85c4addb697e7f88605e0cbbe71a133f83c69)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAvailability")
    def reset_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailability", []))

    @jsii.member(jsii_name="resetSpotBidPricePercent")
    def reset_spot_bid_price_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotBidPricePercent", []))

    @jsii.member(jsii_name="resetZoneId")
    def reset_zone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneId", []))

    @builtins.property
    @jsii.member(jsii_name="availabilityInput")
    def availability_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="spotBidPricePercentInput")
    def spot_bid_price_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "spotBidPricePercentInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="availability")
    def availability(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availability"))

    @availability.setter
    def availability(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c1fcb81d0fa5b5bbd4c4a1e642326aa02ea0d6842ee274428142a508cee08aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="spotBidPricePercent")
    def spot_bid_price_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotBidPricePercent"))

    @spot_bid_price_percent.setter
    def spot_bid_price_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__911d554eb23f677dff0df7fc71af340f85cd091c3bc9f749c2d9b2eef72eac10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotBidPricePercent", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c4188d816ebca7245e03f0b786853f8163172c56961b97682dc32cb7c28a3d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[InstancePoolAwsAttributes]:
        return typing.cast(typing.Optional[InstancePoolAwsAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[InstancePoolAwsAttributes]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3005d9283791d1d48f84830be527d041e7cc3f5289cb9bb3324c85cbce48397)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.instancePool.InstancePoolAzureAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "spot_bid_max_price": "spotBidMaxPrice",
    },
)
class InstancePoolAzureAttributes:
    def __init__(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        spot_bid_max_price: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#availability InstancePool#availability}.
        :param spot_bid_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#spot_bid_max_price InstancePool#spot_bid_max_price}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c0898794c6dd2be8f15c001f6517bf926adbf8e06f0150c86fa5337187fe08c)
            check_type(argname="argument availability", value=availability, expected_type=type_hints["availability"])
            check_type(argname="argument spot_bid_max_price", value=spot_bid_max_price, expected_type=type_hints["spot_bid_max_price"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability is not None:
            self._values["availability"] = availability
        if spot_bid_max_price is not None:
            self._values["spot_bid_max_price"] = spot_bid_max_price

    @builtins.property
    def availability(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#availability InstancePool#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_bid_max_price(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#spot_bid_max_price InstancePool#spot_bid_max_price}.'''
        result = self._values.get("spot_bid_max_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstancePoolAzureAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstancePoolAzureAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.instancePool.InstancePoolAzureAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__904c574d53cc3ad5aa3dd1e12b6bebd09e8c76681545d72437792511471ebb53)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAvailability")
    def reset_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailability", []))

    @jsii.member(jsii_name="resetSpotBidMaxPrice")
    def reset_spot_bid_max_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotBidMaxPrice", []))

    @builtins.property
    @jsii.member(jsii_name="availabilityInput")
    def availability_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="spotBidMaxPriceInput")
    def spot_bid_max_price_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "spotBidMaxPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="availability")
    def availability(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availability"))

    @availability.setter
    def availability(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92dfdf4797255895c5b7f042e105e9e0ab082de1065033b9f804ea967c452c62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="spotBidMaxPrice")
    def spot_bid_max_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotBidMaxPrice"))

    @spot_bid_max_price.setter
    def spot_bid_max_price(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de0612a06606404882280b3c5b6963ff6b137de3ef1ac22f64361c4553a4adb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotBidMaxPrice", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[InstancePoolAzureAttributes]:
        return typing.cast(typing.Optional[InstancePoolAzureAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[InstancePoolAzureAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23a857eb15580ae255c8aa3aabfe458578a254db137088c7a4fc0dc2a8ac42b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.instancePool.InstancePoolConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "idle_instance_autotermination_minutes": "idleInstanceAutoterminationMinutes",
        "instance_pool_name": "instancePoolName",
        "aws_attributes": "awsAttributes",
        "azure_attributes": "azureAttributes",
        "custom_tags": "customTags",
        "disk_spec": "diskSpec",
        "enable_elastic_disk": "enableElasticDisk",
        "gcp_attributes": "gcpAttributes",
        "id": "id",
        "instance_pool_fleet_attributes": "instancePoolFleetAttributes",
        "instance_pool_id": "instancePoolId",
        "max_capacity": "maxCapacity",
        "min_idle_instances": "minIdleInstances",
        "node_type_id": "nodeTypeId",
        "preloaded_docker_image": "preloadedDockerImage",
        "preloaded_spark_versions": "preloadedSparkVersions",
    },
)
class InstancePoolConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        idle_instance_autotermination_minutes: jsii.Number,
        instance_pool_name: builtins.str,
        aws_attributes: typing.Optional[typing.Union[InstancePoolAwsAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
        azure_attributes: typing.Optional[typing.Union[InstancePoolAzureAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
        custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        disk_spec: typing.Optional[typing.Union["InstancePoolDiskSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        gcp_attributes: typing.Optional[typing.Union["InstancePoolGcpAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        instance_pool_fleet_attributes: typing.Optional[typing.Union["InstancePoolInstancePoolFleetAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        instance_pool_id: typing.Optional[builtins.str] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        min_idle_instances: typing.Optional[jsii.Number] = None,
        node_type_id: typing.Optional[builtins.str] = None,
        preloaded_docker_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["InstancePoolPreloadedDockerImage", typing.Dict[builtins.str, typing.Any]]]]] = None,
        preloaded_spark_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param idle_instance_autotermination_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#idle_instance_autotermination_minutes InstancePool#idle_instance_autotermination_minutes}.
        :param instance_pool_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#instance_pool_name InstancePool#instance_pool_name}.
        :param aws_attributes: aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#aws_attributes InstancePool#aws_attributes}
        :param azure_attributes: azure_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#azure_attributes InstancePool#azure_attributes}
        :param custom_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#custom_tags InstancePool#custom_tags}.
        :param disk_spec: disk_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#disk_spec InstancePool#disk_spec}
        :param enable_elastic_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#enable_elastic_disk InstancePool#enable_elastic_disk}.
        :param gcp_attributes: gcp_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#gcp_attributes InstancePool#gcp_attributes}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#id InstancePool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_pool_fleet_attributes: instance_pool_fleet_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#instance_pool_fleet_attributes InstancePool#instance_pool_fleet_attributes}
        :param instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#instance_pool_id InstancePool#instance_pool_id}.
        :param max_capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#max_capacity InstancePool#max_capacity}.
        :param min_idle_instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#min_idle_instances InstancePool#min_idle_instances}.
        :param node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#node_type_id InstancePool#node_type_id}.
        :param preloaded_docker_image: preloaded_docker_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#preloaded_docker_image InstancePool#preloaded_docker_image}
        :param preloaded_spark_versions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#preloaded_spark_versions InstancePool#preloaded_spark_versions}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(aws_attributes, dict):
            aws_attributes = InstancePoolAwsAttributes(**aws_attributes)
        if isinstance(azure_attributes, dict):
            azure_attributes = InstancePoolAzureAttributes(**azure_attributes)
        if isinstance(disk_spec, dict):
            disk_spec = InstancePoolDiskSpec(**disk_spec)
        if isinstance(gcp_attributes, dict):
            gcp_attributes = InstancePoolGcpAttributes(**gcp_attributes)
        if isinstance(instance_pool_fleet_attributes, dict):
            instance_pool_fleet_attributes = InstancePoolInstancePoolFleetAttributes(**instance_pool_fleet_attributes)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d07a77b13d6be09181db7e3f640048744d2c6e4af3f14af6f7758f307df9d65)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument idle_instance_autotermination_minutes", value=idle_instance_autotermination_minutes, expected_type=type_hints["idle_instance_autotermination_minutes"])
            check_type(argname="argument instance_pool_name", value=instance_pool_name, expected_type=type_hints["instance_pool_name"])
            check_type(argname="argument aws_attributes", value=aws_attributes, expected_type=type_hints["aws_attributes"])
            check_type(argname="argument azure_attributes", value=azure_attributes, expected_type=type_hints["azure_attributes"])
            check_type(argname="argument custom_tags", value=custom_tags, expected_type=type_hints["custom_tags"])
            check_type(argname="argument disk_spec", value=disk_spec, expected_type=type_hints["disk_spec"])
            check_type(argname="argument enable_elastic_disk", value=enable_elastic_disk, expected_type=type_hints["enable_elastic_disk"])
            check_type(argname="argument gcp_attributes", value=gcp_attributes, expected_type=type_hints["gcp_attributes"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_pool_fleet_attributes", value=instance_pool_fleet_attributes, expected_type=type_hints["instance_pool_fleet_attributes"])
            check_type(argname="argument instance_pool_id", value=instance_pool_id, expected_type=type_hints["instance_pool_id"])
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument min_idle_instances", value=min_idle_instances, expected_type=type_hints["min_idle_instances"])
            check_type(argname="argument node_type_id", value=node_type_id, expected_type=type_hints["node_type_id"])
            check_type(argname="argument preloaded_docker_image", value=preloaded_docker_image, expected_type=type_hints["preloaded_docker_image"])
            check_type(argname="argument preloaded_spark_versions", value=preloaded_spark_versions, expected_type=type_hints["preloaded_spark_versions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "idle_instance_autotermination_minutes": idle_instance_autotermination_minutes,
            "instance_pool_name": instance_pool_name,
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
        if aws_attributes is not None:
            self._values["aws_attributes"] = aws_attributes
        if azure_attributes is not None:
            self._values["azure_attributes"] = azure_attributes
        if custom_tags is not None:
            self._values["custom_tags"] = custom_tags
        if disk_spec is not None:
            self._values["disk_spec"] = disk_spec
        if enable_elastic_disk is not None:
            self._values["enable_elastic_disk"] = enable_elastic_disk
        if gcp_attributes is not None:
            self._values["gcp_attributes"] = gcp_attributes
        if id is not None:
            self._values["id"] = id
        if instance_pool_fleet_attributes is not None:
            self._values["instance_pool_fleet_attributes"] = instance_pool_fleet_attributes
        if instance_pool_id is not None:
            self._values["instance_pool_id"] = instance_pool_id
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity
        if min_idle_instances is not None:
            self._values["min_idle_instances"] = min_idle_instances
        if node_type_id is not None:
            self._values["node_type_id"] = node_type_id
        if preloaded_docker_image is not None:
            self._values["preloaded_docker_image"] = preloaded_docker_image
        if preloaded_spark_versions is not None:
            self._values["preloaded_spark_versions"] = preloaded_spark_versions

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
    def idle_instance_autotermination_minutes(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#idle_instance_autotermination_minutes InstancePool#idle_instance_autotermination_minutes}.'''
        result = self._values.get("idle_instance_autotermination_minutes")
        assert result is not None, "Required property 'idle_instance_autotermination_minutes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def instance_pool_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#instance_pool_name InstancePool#instance_pool_name}.'''
        result = self._values.get("instance_pool_name")
        assert result is not None, "Required property 'instance_pool_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_attributes(self) -> typing.Optional[InstancePoolAwsAttributes]:
        '''aws_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#aws_attributes InstancePool#aws_attributes}
        '''
        result = self._values.get("aws_attributes")
        return typing.cast(typing.Optional[InstancePoolAwsAttributes], result)

    @builtins.property
    def azure_attributes(self) -> typing.Optional[InstancePoolAzureAttributes]:
        '''azure_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#azure_attributes InstancePool#azure_attributes}
        '''
        result = self._values.get("azure_attributes")
        return typing.cast(typing.Optional[InstancePoolAzureAttributes], result)

    @builtins.property
    def custom_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#custom_tags InstancePool#custom_tags}.'''
        result = self._values.get("custom_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def disk_spec(self) -> typing.Optional["InstancePoolDiskSpec"]:
        '''disk_spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#disk_spec InstancePool#disk_spec}
        '''
        result = self._values.get("disk_spec")
        return typing.cast(typing.Optional["InstancePoolDiskSpec"], result)

    @builtins.property
    def enable_elastic_disk(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#enable_elastic_disk InstancePool#enable_elastic_disk}.'''
        result = self._values.get("enable_elastic_disk")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def gcp_attributes(self) -> typing.Optional["InstancePoolGcpAttributes"]:
        '''gcp_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#gcp_attributes InstancePool#gcp_attributes}
        '''
        result = self._values.get("gcp_attributes")
        return typing.cast(typing.Optional["InstancePoolGcpAttributes"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#id InstancePool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_pool_fleet_attributes(
        self,
    ) -> typing.Optional["InstancePoolInstancePoolFleetAttributes"]:
        '''instance_pool_fleet_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#instance_pool_fleet_attributes InstancePool#instance_pool_fleet_attributes}
        '''
        result = self._values.get("instance_pool_fleet_attributes")
        return typing.cast(typing.Optional["InstancePoolInstancePoolFleetAttributes"], result)

    @builtins.property
    def instance_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#instance_pool_id InstancePool#instance_pool_id}.'''
        result = self._values.get("instance_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#max_capacity InstancePool#max_capacity}.'''
        result = self._values.get("max_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_idle_instances(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#min_idle_instances InstancePool#min_idle_instances}.'''
        result = self._values.get("min_idle_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def node_type_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#node_type_id InstancePool#node_type_id}.'''
        result = self._values.get("node_type_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preloaded_docker_image(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstancePoolPreloadedDockerImage"]]]:
        '''preloaded_docker_image block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#preloaded_docker_image InstancePool#preloaded_docker_image}
        '''
        result = self._values.get("preloaded_docker_image")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstancePoolPreloadedDockerImage"]]], result)

    @builtins.property
    def preloaded_spark_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#preloaded_spark_versions InstancePool#preloaded_spark_versions}.'''
        result = self._values.get("preloaded_spark_versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstancePoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.instancePool.InstancePoolDiskSpec",
    jsii_struct_bases=[],
    name_mapping={
        "disk_count": "diskCount",
        "disk_size": "diskSize",
        "disk_type": "diskType",
    },
)
class InstancePoolDiskSpec:
    def __init__(
        self,
        *,
        disk_count: typing.Optional[jsii.Number] = None,
        disk_size: typing.Optional[jsii.Number] = None,
        disk_type: typing.Optional[typing.Union["InstancePoolDiskSpecDiskType", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param disk_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#disk_count InstancePool#disk_count}.
        :param disk_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#disk_size InstancePool#disk_size}.
        :param disk_type: disk_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#disk_type InstancePool#disk_type}
        '''
        if isinstance(disk_type, dict):
            disk_type = InstancePoolDiskSpecDiskType(**disk_type)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bddb93edcd29eaac6cf73a38cb2157dd3a20d1e953ebd8cd75dbe866e8b0ce54)
            check_type(argname="argument disk_count", value=disk_count, expected_type=type_hints["disk_count"])
            check_type(argname="argument disk_size", value=disk_size, expected_type=type_hints["disk_size"])
            check_type(argname="argument disk_type", value=disk_type, expected_type=type_hints["disk_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if disk_count is not None:
            self._values["disk_count"] = disk_count
        if disk_size is not None:
            self._values["disk_size"] = disk_size
        if disk_type is not None:
            self._values["disk_type"] = disk_type

    @builtins.property
    def disk_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#disk_count InstancePool#disk_count}.'''
        result = self._values.get("disk_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#disk_size InstancePool#disk_size}.'''
        result = self._values.get("disk_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_type(self) -> typing.Optional["InstancePoolDiskSpecDiskType"]:
        '''disk_type block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#disk_type InstancePool#disk_type}
        '''
        result = self._values.get("disk_type")
        return typing.cast(typing.Optional["InstancePoolDiskSpecDiskType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstancePoolDiskSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.instancePool.InstancePoolDiskSpecDiskType",
    jsii_struct_bases=[],
    name_mapping={
        "azure_disk_volume_type": "azureDiskVolumeType",
        "ebs_volume_type": "ebsVolumeType",
    },
)
class InstancePoolDiskSpecDiskType:
    def __init__(
        self,
        *,
        azure_disk_volume_type: typing.Optional[builtins.str] = None,
        ebs_volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param azure_disk_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#azure_disk_volume_type InstancePool#azure_disk_volume_type}.
        :param ebs_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#ebs_volume_type InstancePool#ebs_volume_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0a2de6f486e3df3ac2427dcfc740fd333ceafd9435c6c62be3d069fd26e9f74)
            check_type(argname="argument azure_disk_volume_type", value=azure_disk_volume_type, expected_type=type_hints["azure_disk_volume_type"])
            check_type(argname="argument ebs_volume_type", value=ebs_volume_type, expected_type=type_hints["ebs_volume_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if azure_disk_volume_type is not None:
            self._values["azure_disk_volume_type"] = azure_disk_volume_type
        if ebs_volume_type is not None:
            self._values["ebs_volume_type"] = ebs_volume_type

    @builtins.property
    def azure_disk_volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#azure_disk_volume_type InstancePool#azure_disk_volume_type}.'''
        result = self._values.get("azure_disk_volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#ebs_volume_type InstancePool#ebs_volume_type}.'''
        result = self._values.get("ebs_volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstancePoolDiskSpecDiskType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstancePoolDiskSpecDiskTypeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.instancePool.InstancePoolDiskSpecDiskTypeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e8ff5a3a80ddc3107f43864b8c8baa234e6fbcf0d2a3a821dc0b88ed36e5341b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAzureDiskVolumeType")
    def reset_azure_disk_volume_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureDiskVolumeType", []))

    @jsii.member(jsii_name="resetEbsVolumeType")
    def reset_ebs_volume_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsVolumeType", []))

    @builtins.property
    @jsii.member(jsii_name="azureDiskVolumeTypeInput")
    def azure_disk_volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureDiskVolumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeTypeInput")
    def ebs_volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ebsVolumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="azureDiskVolumeType")
    def azure_disk_volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureDiskVolumeType"))

    @azure_disk_volume_type.setter
    def azure_disk_volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__326f3a6ada4d6eb1565da8e39dcd5d11edbd81793ba46609da52dae5cfd68df5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureDiskVolumeType", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeType")
    def ebs_volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ebsVolumeType"))

    @ebs_volume_type.setter
    def ebs_volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f96b2a500469b56a314c9a2f5724920e1c36586c6ca07c2e0727faa98bb44ac6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[InstancePoolDiskSpecDiskType]:
        return typing.cast(typing.Optional[InstancePoolDiskSpecDiskType], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[InstancePoolDiskSpecDiskType],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd408caa97d0b252c4679c6c842ec8db92ccecacfa52d6c0e8cb7f0071f4d0da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class InstancePoolDiskSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.instancePool.InstancePoolDiskSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ac5bf9a9aa2d2f4899208cde8876db773bb8fc6704976279f5b9be7de2946e3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDiskType")
    def put_disk_type(
        self,
        *,
        azure_disk_volume_type: typing.Optional[builtins.str] = None,
        ebs_volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param azure_disk_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#azure_disk_volume_type InstancePool#azure_disk_volume_type}.
        :param ebs_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#ebs_volume_type InstancePool#ebs_volume_type}.
        '''
        value = InstancePoolDiskSpecDiskType(
            azure_disk_volume_type=azure_disk_volume_type,
            ebs_volume_type=ebs_volume_type,
        )

        return typing.cast(None, jsii.invoke(self, "putDiskType", [value]))

    @jsii.member(jsii_name="resetDiskCount")
    def reset_disk_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskCount", []))

    @jsii.member(jsii_name="resetDiskSize")
    def reset_disk_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSize", []))

    @jsii.member(jsii_name="resetDiskType")
    def reset_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskType", []))

    @builtins.property
    @jsii.member(jsii_name="diskType")
    def disk_type(self) -> InstancePoolDiskSpecDiskTypeOutputReference:
        return typing.cast(InstancePoolDiskSpecDiskTypeOutputReference, jsii.get(self, "diskType"))

    @builtins.property
    @jsii.member(jsii_name="diskCountInput")
    def disk_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskCountInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeInput")
    def disk_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="diskTypeInput")
    def disk_type_input(self) -> typing.Optional[InstancePoolDiskSpecDiskType]:
        return typing.cast(typing.Optional[InstancePoolDiskSpecDiskType], jsii.get(self, "diskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="diskCount")
    def disk_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskCount"))

    @disk_count.setter
    def disk_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfcf633dd88d29e81356a05b37a4c259fd07eab17f444b1aff53b2cccc54974b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskCount", value)

    @builtins.property
    @jsii.member(jsii_name="diskSize")
    def disk_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSize"))

    @disk_size.setter
    def disk_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb825a0daa7ea2311f59241e16867a8fd830562fea51372cea68e15c52acdf3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSize", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[InstancePoolDiskSpec]:
        return typing.cast(typing.Optional[InstancePoolDiskSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[InstancePoolDiskSpec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ab9fe41d01c014a1d7634f22d1f969d365cdbf47de020f365f2f109df2d437e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.instancePool.InstancePoolGcpAttributes",
    jsii_struct_bases=[],
    name_mapping={"gcp_availability": "gcpAvailability"},
)
class InstancePoolGcpAttributes:
    def __init__(
        self,
        *,
        gcp_availability: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param gcp_availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#gcp_availability InstancePool#gcp_availability}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7740037fc8ec74ae8d3764f9b23b0504e29dfec89ef075242271217b2cb92839)
            check_type(argname="argument gcp_availability", value=gcp_availability, expected_type=type_hints["gcp_availability"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if gcp_availability is not None:
            self._values["gcp_availability"] = gcp_availability

    @builtins.property
    def gcp_availability(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#gcp_availability InstancePool#gcp_availability}.'''
        result = self._values.get("gcp_availability")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstancePoolGcpAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstancePoolGcpAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.instancePool.InstancePoolGcpAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d657a8831e5715191a9751301b021e6565cc8d638f9efefbc5530a3962696be)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGcpAvailability")
    def reset_gcp_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpAvailability", []))

    @builtins.property
    @jsii.member(jsii_name="gcpAvailabilityInput")
    def gcp_availability_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gcpAvailabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="gcpAvailability")
    def gcp_availability(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gcpAvailability"))

    @gcp_availability.setter
    def gcp_availability(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7b417f3e67fa1b631bc770962806f69de4907e6d865879f18946d16f08fc8d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gcpAvailability", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[InstancePoolGcpAttributes]:
        return typing.cast(typing.Optional[InstancePoolGcpAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[InstancePoolGcpAttributes]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__360e5714cb0653031d94f5862ef3c3129f6adbeab694a2cb95c9b53786a0b99a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.instancePool.InstancePoolInstancePoolFleetAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "launch_template_override": "launchTemplateOverride",
        "fleet_on_demand_option": "fleetOnDemandOption",
        "fleet_spot_option": "fleetSpotOption",
    },
)
class InstancePoolInstancePoolFleetAttributes:
    def __init__(
        self,
        *,
        launch_template_override: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride", typing.Dict[builtins.str, typing.Any]]]],
        fleet_on_demand_option: typing.Optional[typing.Union["InstancePoolInstancePoolFleetAttributesFleetOnDemandOption", typing.Dict[builtins.str, typing.Any]]] = None,
        fleet_spot_option: typing.Optional[typing.Union["InstancePoolInstancePoolFleetAttributesFleetSpotOption", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param launch_template_override: launch_template_override block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#launch_template_override InstancePool#launch_template_override}
        :param fleet_on_demand_option: fleet_on_demand_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#fleet_on_demand_option InstancePool#fleet_on_demand_option}
        :param fleet_spot_option: fleet_spot_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#fleet_spot_option InstancePool#fleet_spot_option}
        '''
        if isinstance(fleet_on_demand_option, dict):
            fleet_on_demand_option = InstancePoolInstancePoolFleetAttributesFleetOnDemandOption(**fleet_on_demand_option)
        if isinstance(fleet_spot_option, dict):
            fleet_spot_option = InstancePoolInstancePoolFleetAttributesFleetSpotOption(**fleet_spot_option)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83b738c616e60521cd7093dae47a8658228bab85728a208de4b2e2e3aea38834)
            check_type(argname="argument launch_template_override", value=launch_template_override, expected_type=type_hints["launch_template_override"])
            check_type(argname="argument fleet_on_demand_option", value=fleet_on_demand_option, expected_type=type_hints["fleet_on_demand_option"])
            check_type(argname="argument fleet_spot_option", value=fleet_spot_option, expected_type=type_hints["fleet_spot_option"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "launch_template_override": launch_template_override,
        }
        if fleet_on_demand_option is not None:
            self._values["fleet_on_demand_option"] = fleet_on_demand_option
        if fleet_spot_option is not None:
            self._values["fleet_spot_option"] = fleet_spot_option

    @builtins.property
    def launch_template_override(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride"]]:
        '''launch_template_override block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#launch_template_override InstancePool#launch_template_override}
        '''
        result = self._values.get("launch_template_override")
        assert result is not None, "Required property 'launch_template_override' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride"]], result)

    @builtins.property
    def fleet_on_demand_option(
        self,
    ) -> typing.Optional["InstancePoolInstancePoolFleetAttributesFleetOnDemandOption"]:
        '''fleet_on_demand_option block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#fleet_on_demand_option InstancePool#fleet_on_demand_option}
        '''
        result = self._values.get("fleet_on_demand_option")
        return typing.cast(typing.Optional["InstancePoolInstancePoolFleetAttributesFleetOnDemandOption"], result)

    @builtins.property
    def fleet_spot_option(
        self,
    ) -> typing.Optional["InstancePoolInstancePoolFleetAttributesFleetSpotOption"]:
        '''fleet_spot_option block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#fleet_spot_option InstancePool#fleet_spot_option}
        '''
        result = self._values.get("fleet_spot_option")
        return typing.cast(typing.Optional["InstancePoolInstancePoolFleetAttributesFleetSpotOption"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstancePoolInstancePoolFleetAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.instancePool.InstancePoolInstancePoolFleetAttributesFleetOnDemandOption",
    jsii_struct_bases=[],
    name_mapping={
        "allocation_strategy": "allocationStrategy",
        "instance_pools_to_use_count": "instancePoolsToUseCount",
    },
)
class InstancePoolInstancePoolFleetAttributesFleetOnDemandOption:
    def __init__(
        self,
        *,
        allocation_strategy: builtins.str,
        instance_pools_to_use_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#allocation_strategy InstancePool#allocation_strategy}.
        :param instance_pools_to_use_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#instance_pools_to_use_count InstancePool#instance_pools_to_use_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddc51e7431c5af2002151ab97843f78f5a8a8cdbcc0c831bad1209ce5c99f77e)
            check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
            check_type(argname="argument instance_pools_to_use_count", value=instance_pools_to_use_count, expected_type=type_hints["instance_pools_to_use_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allocation_strategy": allocation_strategy,
        }
        if instance_pools_to_use_count is not None:
            self._values["instance_pools_to_use_count"] = instance_pools_to_use_count

    @builtins.property
    def allocation_strategy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#allocation_strategy InstancePool#allocation_strategy}.'''
        result = self._values.get("allocation_strategy")
        assert result is not None, "Required property 'allocation_strategy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_pools_to_use_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#instance_pools_to_use_count InstancePool#instance_pools_to_use_count}.'''
        result = self._values.get("instance_pools_to_use_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstancePoolInstancePoolFleetAttributesFleetOnDemandOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstancePoolInstancePoolFleetAttributesFleetOnDemandOptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.instancePool.InstancePoolInstancePoolFleetAttributesFleetOnDemandOptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb7024030e39296f450a4bfd27536a8c73c24c9a677f3c2360bbce13421a71b4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstancePoolsToUseCount")
    def reset_instance_pools_to_use_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancePoolsToUseCount", []))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategyInput")
    def allocation_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolsToUseCountInput")
    def instance_pools_to_use_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instancePoolsToUseCountInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategy")
    def allocation_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allocationStrategy"))

    @allocation_strategy.setter
    def allocation_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69c76d3d7e97a3607349dd266cef12a12056c9ec9a0a9968e6d31be2166ab76c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="instancePoolsToUseCount")
    def instance_pools_to_use_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instancePoolsToUseCount"))

    @instance_pools_to_use_count.setter
    def instance_pools_to_use_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11cc4648bde1705d9653bfaa5b26d8ab3bc066d37996a21d03d32b9b7e137c44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instancePoolsToUseCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[InstancePoolInstancePoolFleetAttributesFleetOnDemandOption]:
        return typing.cast(typing.Optional[InstancePoolInstancePoolFleetAttributesFleetOnDemandOption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[InstancePoolInstancePoolFleetAttributesFleetOnDemandOption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4022b2860337c140abd38ae8af9619a22c39a5be68bb995b30c7f8ded9038eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.instancePool.InstancePoolInstancePoolFleetAttributesFleetSpotOption",
    jsii_struct_bases=[],
    name_mapping={
        "allocation_strategy": "allocationStrategy",
        "instance_pools_to_use_count": "instancePoolsToUseCount",
    },
)
class InstancePoolInstancePoolFleetAttributesFleetSpotOption:
    def __init__(
        self,
        *,
        allocation_strategy: builtins.str,
        instance_pools_to_use_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#allocation_strategy InstancePool#allocation_strategy}.
        :param instance_pools_to_use_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#instance_pools_to_use_count InstancePool#instance_pools_to_use_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fb93437ea198df7da8de576786f34b12b6a7ca5c6529b6b669ab35c87e9be8f)
            check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
            check_type(argname="argument instance_pools_to_use_count", value=instance_pools_to_use_count, expected_type=type_hints["instance_pools_to_use_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allocation_strategy": allocation_strategy,
        }
        if instance_pools_to_use_count is not None:
            self._values["instance_pools_to_use_count"] = instance_pools_to_use_count

    @builtins.property
    def allocation_strategy(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#allocation_strategy InstancePool#allocation_strategy}.'''
        result = self._values.get("allocation_strategy")
        assert result is not None, "Required property 'allocation_strategy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_pools_to_use_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#instance_pools_to_use_count InstancePool#instance_pools_to_use_count}.'''
        result = self._values.get("instance_pools_to_use_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstancePoolInstancePoolFleetAttributesFleetSpotOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstancePoolInstancePoolFleetAttributesFleetSpotOptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.instancePool.InstancePoolInstancePoolFleetAttributesFleetSpotOptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__86bf10666d0cd2e5dbc39b00159f47e1e7acce3dc9cabb6187f66a4ac3bfc999)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstancePoolsToUseCount")
    def reset_instance_pools_to_use_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancePoolsToUseCount", []))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategyInput")
    def allocation_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolsToUseCountInput")
    def instance_pools_to_use_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instancePoolsToUseCountInput"))

    @builtins.property
    @jsii.member(jsii_name="allocationStrategy")
    def allocation_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allocationStrategy"))

    @allocation_strategy.setter
    def allocation_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4a61dc032da1389d8fe7721df562db78d7646a00ce08ba144c8d41d6459a9c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="instancePoolsToUseCount")
    def instance_pools_to_use_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instancePoolsToUseCount"))

    @instance_pools_to_use_count.setter
    def instance_pools_to_use_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__914de61e01ee578f2a7a1b6860b05939a1343e69d308ed339d0b8cd77ce3c423)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instancePoolsToUseCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[InstancePoolInstancePoolFleetAttributesFleetSpotOption]:
        return typing.cast(typing.Optional[InstancePoolInstancePoolFleetAttributesFleetSpotOption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[InstancePoolInstancePoolFleetAttributesFleetSpotOption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c60f43a73e49b81ee595ee4af90cb6a56d3f56bc17149d7b42aaa4545fd76661)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.instancePool.InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zone": "availabilityZone",
        "instance_type": "instanceType",
    },
)
class InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride:
    def __init__(
        self,
        *,
        availability_zone: builtins.str,
        instance_type: builtins.str,
    ) -> None:
        '''
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#availability_zone InstancePool#availability_zone}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#instance_type InstancePool#instance_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f7fb24d19008dac805f57b2235b04da17be33107ce72c1b1e61d35960fc6a43)
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "availability_zone": availability_zone,
            "instance_type": instance_type,
        }

    @builtins.property
    def availability_zone(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#availability_zone InstancePool#availability_zone}.'''
        result = self._values.get("availability_zone")
        assert result is not None, "Required property 'availability_zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#instance_type InstancePool#instance_type}.'''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstancePoolInstancePoolFleetAttributesLaunchTemplateOverrideList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.instancePool.InstancePoolInstancePoolFleetAttributesLaunchTemplateOverrideList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75b141658659ac95242b575a6f470494a4f3ef6dfd80be29c2bd48399428ffb7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "InstancePoolInstancePoolFleetAttributesLaunchTemplateOverrideOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9419b356cccab5699f18e8ef87017d8ca9a8f7fd0eef24ff2a14b357bf559ae1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("InstancePoolInstancePoolFleetAttributesLaunchTemplateOverrideOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fff06d97d8b05460f6259b838684bbca5c61364f164d3c629ce13e078a5a971)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5635c2e246908a60098ddd650e0deb9aaf628d24c7e2e0327482b9c26101fe0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79fbaba38801a59d50109ccae2b2c5e7118d1bc968adcf0e2292bd88d7112357)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b3b059df66f1dbda70c9d761368a9a0d41b1a4eca998e67f4ff271957ea216b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class InstancePoolInstancePoolFleetAttributesLaunchTemplateOverrideOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.instancePool.InstancePoolInstancePoolFleetAttributesLaunchTemplateOverrideOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07a72c5d61a95a72f01385612405b43a87da00268d0967d17e63cd308e4f1618)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneInput")
    def availability_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b69c07cc3ee110f56c42041c4298a418a357bb40a1d557797cd11c4dd55adb4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8c444d1a516247a4b97c6aac92321b4281c7e0581a15c809bc30c7d2b61d59e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2abe6d857642ee98f75fb3fce79539d62bbc606391c9948aa90f5132f0bf095)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class InstancePoolInstancePoolFleetAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.instancePool.InstancePoolInstancePoolFleetAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__770d487793b9246a1febd49ae9b38df33b54bbb9e1331426ee1225a2a83d19cd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFleetOnDemandOption")
    def put_fleet_on_demand_option(
        self,
        *,
        allocation_strategy: builtins.str,
        instance_pools_to_use_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#allocation_strategy InstancePool#allocation_strategy}.
        :param instance_pools_to_use_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#instance_pools_to_use_count InstancePool#instance_pools_to_use_count}.
        '''
        value = InstancePoolInstancePoolFleetAttributesFleetOnDemandOption(
            allocation_strategy=allocation_strategy,
            instance_pools_to_use_count=instance_pools_to_use_count,
        )

        return typing.cast(None, jsii.invoke(self, "putFleetOnDemandOption", [value]))

    @jsii.member(jsii_name="putFleetSpotOption")
    def put_fleet_spot_option(
        self,
        *,
        allocation_strategy: builtins.str,
        instance_pools_to_use_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param allocation_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#allocation_strategy InstancePool#allocation_strategy}.
        :param instance_pools_to_use_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#instance_pools_to_use_count InstancePool#instance_pools_to_use_count}.
        '''
        value = InstancePoolInstancePoolFleetAttributesFleetSpotOption(
            allocation_strategy=allocation_strategy,
            instance_pools_to_use_count=instance_pools_to_use_count,
        )

        return typing.cast(None, jsii.invoke(self, "putFleetSpotOption", [value]))

    @jsii.member(jsii_name="putLaunchTemplateOverride")
    def put_launch_template_override(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f27dcbe32f0aeaf8cb2bab2cc8993217eac91d2ca7b1276cf7015eccf03164d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLaunchTemplateOverride", [value]))

    @jsii.member(jsii_name="resetFleetOnDemandOption")
    def reset_fleet_on_demand_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFleetOnDemandOption", []))

    @jsii.member(jsii_name="resetFleetSpotOption")
    def reset_fleet_spot_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFleetSpotOption", []))

    @builtins.property
    @jsii.member(jsii_name="fleetOnDemandOption")
    def fleet_on_demand_option(
        self,
    ) -> InstancePoolInstancePoolFleetAttributesFleetOnDemandOptionOutputReference:
        return typing.cast(InstancePoolInstancePoolFleetAttributesFleetOnDemandOptionOutputReference, jsii.get(self, "fleetOnDemandOption"))

    @builtins.property
    @jsii.member(jsii_name="fleetSpotOption")
    def fleet_spot_option(
        self,
    ) -> InstancePoolInstancePoolFleetAttributesFleetSpotOptionOutputReference:
        return typing.cast(InstancePoolInstancePoolFleetAttributesFleetSpotOptionOutputReference, jsii.get(self, "fleetSpotOption"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateOverride")
    def launch_template_override(
        self,
    ) -> InstancePoolInstancePoolFleetAttributesLaunchTemplateOverrideList:
        return typing.cast(InstancePoolInstancePoolFleetAttributesLaunchTemplateOverrideList, jsii.get(self, "launchTemplateOverride"))

    @builtins.property
    @jsii.member(jsii_name="fleetOnDemandOptionInput")
    def fleet_on_demand_option_input(
        self,
    ) -> typing.Optional[InstancePoolInstancePoolFleetAttributesFleetOnDemandOption]:
        return typing.cast(typing.Optional[InstancePoolInstancePoolFleetAttributesFleetOnDemandOption], jsii.get(self, "fleetOnDemandOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="fleetSpotOptionInput")
    def fleet_spot_option_input(
        self,
    ) -> typing.Optional[InstancePoolInstancePoolFleetAttributesFleetSpotOption]:
        return typing.cast(typing.Optional[InstancePoolInstancePoolFleetAttributesFleetSpotOption], jsii.get(self, "fleetSpotOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTemplateOverrideInput")
    def launch_template_override_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride]]], jsii.get(self, "launchTemplateOverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[InstancePoolInstancePoolFleetAttributes]:
        return typing.cast(typing.Optional[InstancePoolInstancePoolFleetAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[InstancePoolInstancePoolFleetAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0874263d116b60b5fe66db11737fc9f4b2c91d0ad80ef69d48dc2eb67eaef87f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.instancePool.InstancePoolPreloadedDockerImage",
    jsii_struct_bases=[],
    name_mapping={"url": "url", "basic_auth": "basicAuth"},
)
class InstancePoolPreloadedDockerImage:
    def __init__(
        self,
        *,
        url: builtins.str,
        basic_auth: typing.Optional[typing.Union["InstancePoolPreloadedDockerImageBasicAuth", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#url InstancePool#url}.
        :param basic_auth: basic_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#basic_auth InstancePool#basic_auth}
        '''
        if isinstance(basic_auth, dict):
            basic_auth = InstancePoolPreloadedDockerImageBasicAuth(**basic_auth)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebfa3e0630de3f821247be7b1a7863ecf90c3abc961f259cf5e5065ad21cb7d9)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument basic_auth", value=basic_auth, expected_type=type_hints["basic_auth"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if basic_auth is not None:
            self._values["basic_auth"] = basic_auth

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#url InstancePool#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def basic_auth(
        self,
    ) -> typing.Optional["InstancePoolPreloadedDockerImageBasicAuth"]:
        '''basic_auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#basic_auth InstancePool#basic_auth}
        '''
        result = self._values.get("basic_auth")
        return typing.cast(typing.Optional["InstancePoolPreloadedDockerImageBasicAuth"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstancePoolPreloadedDockerImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.instancePool.InstancePoolPreloadedDockerImageBasicAuth",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class InstancePoolPreloadedDockerImageBasicAuth:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#password InstancePool#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#username InstancePool#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf3f8612264520bb04033f4f367c35d3f090ec59e4c1138ede9332dd48d6cc1a)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#password InstancePool#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#username InstancePool#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstancePoolPreloadedDockerImageBasicAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InstancePoolPreloadedDockerImageBasicAuthOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.instancePool.InstancePoolPreloadedDockerImageBasicAuthOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d95d074a4f1598a16e693ca56ab0fda1098ece76fb66889d05e5cd996db4ae01)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf2ec25e0f502fadc1788d6d8725221edf681f4c2b1eccbec70d16f672f43455)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5530a57e3ad2decccacdc69a241d9d248fafc4c312424743cb8c43c62e77d5a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[InstancePoolPreloadedDockerImageBasicAuth]:
        return typing.cast(typing.Optional[InstancePoolPreloadedDockerImageBasicAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[InstancePoolPreloadedDockerImageBasicAuth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26821032d9e394093aa1c04a5ca232920898e7d18b7e6aa60b6141faf15ba371)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class InstancePoolPreloadedDockerImageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.instancePool.InstancePoolPreloadedDockerImageList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8188dbf8fd3500adfc18b412558305b15523ada01e66f641becaaef6c568add9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "InstancePoolPreloadedDockerImageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52ab10ac8dca86aeed98420e8401ac83a40cc54df69ce2f5235fd95ce2ba9595)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("InstancePoolPreloadedDockerImageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b97c7ae8852e26f4e8ae0ec898811848273b717d98bcef183dcfbf5e90ff9c53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99f8fac2cd10e25bb0f81d127c726acab7548b3fb28696afe42b9646f2485aa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30d501405bf282efa4fd69284225cd7991abecce1ab8c40b72c7f7217cae9308)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstancePoolPreloadedDockerImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstancePoolPreloadedDockerImage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstancePoolPreloadedDockerImage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a204830ad9e4a3b01e0bbc60405cbc392f50fc42f4313d538e0086b0cd866feb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class InstancePoolPreloadedDockerImageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.instancePool.InstancePoolPreloadedDockerImageOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__893c8b29e6ac174f8f7a9558d59a551b6cb73ba1d33805e7c702967b4ae4becd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putBasicAuth")
    def put_basic_auth(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#password InstancePool#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/instance_pool#username InstancePool#username}.
        '''
        value = InstancePoolPreloadedDockerImageBasicAuth(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putBasicAuth", [value]))

    @jsii.member(jsii_name="resetBasicAuth")
    def reset_basic_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuth", []))

    @builtins.property
    @jsii.member(jsii_name="basicAuth")
    def basic_auth(self) -> InstancePoolPreloadedDockerImageBasicAuthOutputReference:
        return typing.cast(InstancePoolPreloadedDockerImageBasicAuthOutputReference, jsii.get(self, "basicAuth"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthInput")
    def basic_auth_input(
        self,
    ) -> typing.Optional[InstancePoolPreloadedDockerImageBasicAuth]:
        return typing.cast(typing.Optional[InstancePoolPreloadedDockerImageBasicAuth], jsii.get(self, "basicAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7edb3892fd8f4ad7972eef5bdd9ef74191183254ff495c53b775dd02950e80d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[InstancePoolPreloadedDockerImage, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[InstancePoolPreloadedDockerImage, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[InstancePoolPreloadedDockerImage, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__763bdf3547c1d99f3fae009cdad4929792c4dc49f35eadc6193807b25c8438a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "InstancePool",
    "InstancePoolAwsAttributes",
    "InstancePoolAwsAttributesOutputReference",
    "InstancePoolAzureAttributes",
    "InstancePoolAzureAttributesOutputReference",
    "InstancePoolConfig",
    "InstancePoolDiskSpec",
    "InstancePoolDiskSpecDiskType",
    "InstancePoolDiskSpecDiskTypeOutputReference",
    "InstancePoolDiskSpecOutputReference",
    "InstancePoolGcpAttributes",
    "InstancePoolGcpAttributesOutputReference",
    "InstancePoolInstancePoolFleetAttributes",
    "InstancePoolInstancePoolFleetAttributesFleetOnDemandOption",
    "InstancePoolInstancePoolFleetAttributesFleetOnDemandOptionOutputReference",
    "InstancePoolInstancePoolFleetAttributesFleetSpotOption",
    "InstancePoolInstancePoolFleetAttributesFleetSpotOptionOutputReference",
    "InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride",
    "InstancePoolInstancePoolFleetAttributesLaunchTemplateOverrideList",
    "InstancePoolInstancePoolFleetAttributesLaunchTemplateOverrideOutputReference",
    "InstancePoolInstancePoolFleetAttributesOutputReference",
    "InstancePoolPreloadedDockerImage",
    "InstancePoolPreloadedDockerImageBasicAuth",
    "InstancePoolPreloadedDockerImageBasicAuthOutputReference",
    "InstancePoolPreloadedDockerImageList",
    "InstancePoolPreloadedDockerImageOutputReference",
]

publication.publish()

def _typecheckingstub__c5ea839c8aaa9545921e314cf9efda0b91a853802dd7dcddd32bdfa1fda6e78a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    idle_instance_autotermination_minutes: jsii.Number,
    instance_pool_name: builtins.str,
    aws_attributes: typing.Optional[typing.Union[InstancePoolAwsAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_attributes: typing.Optional[typing.Union[InstancePoolAzureAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    disk_spec: typing.Optional[typing.Union[InstancePoolDiskSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    gcp_attributes: typing.Optional[typing.Union[InstancePoolGcpAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    instance_pool_fleet_attributes: typing.Optional[typing.Union[InstancePoolInstancePoolFleetAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    instance_pool_id: typing.Optional[builtins.str] = None,
    max_capacity: typing.Optional[jsii.Number] = None,
    min_idle_instances: typing.Optional[jsii.Number] = None,
    node_type_id: typing.Optional[builtins.str] = None,
    preloaded_docker_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[InstancePoolPreloadedDockerImage, typing.Dict[builtins.str, typing.Any]]]]] = None,
    preloaded_spark_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__8dbd35f6c97620051b66be8ec8f4723b3e4f59d9fc43331542922b4adf6785d2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[InstancePoolPreloadedDockerImage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15c429b17414a942f1c0c22d0547c0caa43c7b7637e079c39561a2c3dba098b9(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfa2eaf59f275f122b02a3ae43a672d7c8793458189437fa8b76c7c2b8ea5ce0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9cb2a33e88be8cef92a32206e6a8e62c52dd392939c77ad2f65fe92c41c1920(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91e290646897ef29f579923558e41f53fb4ef8919a0baa3deb5d72a7a3067eb7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de082ad17e4f3fdbb468936de92ebf1d89da2eb7dfdc97ad624b02173e90e1e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d49679b82068420a96b74d53ff885c42be3a802b4334eee121c49d3392dd2d98(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0a0efd524649d11b5b14e2eed536f1f349f33c3de76eed14000a4efcb0e05ee(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bf640f3d08684315d975758ebc042fdcd41dc9c9dbe362363e499c8c9593d5e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5c6ac6f0ef4f8890f0b2319a44b648e33ef5d877d59a575062a68a46f742541(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8013f36da9777061d56e74fba94313ad047157770657b2ce8cd020c2c13d9c60(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba22b2c379432da4cf4b0709c4edff67e90219e41756dd205b3fc7c0da1b18a7(
    *,
    availability: typing.Optional[builtins.str] = None,
    spot_bid_price_percent: typing.Optional[jsii.Number] = None,
    zone_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07602bc492766916dca591b5a2d85c4addb697e7f88605e0cbbe71a133f83c69(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c1fcb81d0fa5b5bbd4c4a1e642326aa02ea0d6842ee274428142a508cee08aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__911d554eb23f677dff0df7fc71af340f85cd091c3bc9f749c2d9b2eef72eac10(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c4188d816ebca7245e03f0b786853f8163172c56961b97682dc32cb7c28a3d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3005d9283791d1d48f84830be527d041e7cc3f5289cb9bb3324c85cbce48397(
    value: typing.Optional[InstancePoolAwsAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c0898794c6dd2be8f15c001f6517bf926adbf8e06f0150c86fa5337187fe08c(
    *,
    availability: typing.Optional[builtins.str] = None,
    spot_bid_max_price: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__904c574d53cc3ad5aa3dd1e12b6bebd09e8c76681545d72437792511471ebb53(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92dfdf4797255895c5b7f042e105e9e0ab082de1065033b9f804ea967c452c62(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de0612a06606404882280b3c5b6963ff6b137de3ef1ac22f64361c4553a4adb0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23a857eb15580ae255c8aa3aabfe458578a254db137088c7a4fc0dc2a8ac42b7(
    value: typing.Optional[InstancePoolAzureAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d07a77b13d6be09181db7e3f640048744d2c6e4af3f14af6f7758f307df9d65(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    idle_instance_autotermination_minutes: jsii.Number,
    instance_pool_name: builtins.str,
    aws_attributes: typing.Optional[typing.Union[InstancePoolAwsAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_attributes: typing.Optional[typing.Union[InstancePoolAzureAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    disk_spec: typing.Optional[typing.Union[InstancePoolDiskSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    gcp_attributes: typing.Optional[typing.Union[InstancePoolGcpAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    instance_pool_fleet_attributes: typing.Optional[typing.Union[InstancePoolInstancePoolFleetAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    instance_pool_id: typing.Optional[builtins.str] = None,
    max_capacity: typing.Optional[jsii.Number] = None,
    min_idle_instances: typing.Optional[jsii.Number] = None,
    node_type_id: typing.Optional[builtins.str] = None,
    preloaded_docker_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[InstancePoolPreloadedDockerImage, typing.Dict[builtins.str, typing.Any]]]]] = None,
    preloaded_spark_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bddb93edcd29eaac6cf73a38cb2157dd3a20d1e953ebd8cd75dbe866e8b0ce54(
    *,
    disk_count: typing.Optional[jsii.Number] = None,
    disk_size: typing.Optional[jsii.Number] = None,
    disk_type: typing.Optional[typing.Union[InstancePoolDiskSpecDiskType, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0a2de6f486e3df3ac2427dcfc740fd333ceafd9435c6c62be3d069fd26e9f74(
    *,
    azure_disk_volume_type: typing.Optional[builtins.str] = None,
    ebs_volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8ff5a3a80ddc3107f43864b8c8baa234e6fbcf0d2a3a821dc0b88ed36e5341b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__326f3a6ada4d6eb1565da8e39dcd5d11edbd81793ba46609da52dae5cfd68df5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f96b2a500469b56a314c9a2f5724920e1c36586c6ca07c2e0727faa98bb44ac6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd408caa97d0b252c4679c6c842ec8db92ccecacfa52d6c0e8cb7f0071f4d0da(
    value: typing.Optional[InstancePoolDiskSpecDiskType],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ac5bf9a9aa2d2f4899208cde8876db773bb8fc6704976279f5b9be7de2946e3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfcf633dd88d29e81356a05b37a4c259fd07eab17f444b1aff53b2cccc54974b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb825a0daa7ea2311f59241e16867a8fd830562fea51372cea68e15c52acdf3d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ab9fe41d01c014a1d7634f22d1f969d365cdbf47de020f365f2f109df2d437e(
    value: typing.Optional[InstancePoolDiskSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7740037fc8ec74ae8d3764f9b23b0504e29dfec89ef075242271217b2cb92839(
    *,
    gcp_availability: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d657a8831e5715191a9751301b021e6565cc8d638f9efefbc5530a3962696be(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7b417f3e67fa1b631bc770962806f69de4907e6d865879f18946d16f08fc8d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__360e5714cb0653031d94f5862ef3c3129f6adbeab694a2cb95c9b53786a0b99a(
    value: typing.Optional[InstancePoolGcpAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83b738c616e60521cd7093dae47a8658228bab85728a208de4b2e2e3aea38834(
    *,
    launch_template_override: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride, typing.Dict[builtins.str, typing.Any]]]],
    fleet_on_demand_option: typing.Optional[typing.Union[InstancePoolInstancePoolFleetAttributesFleetOnDemandOption, typing.Dict[builtins.str, typing.Any]]] = None,
    fleet_spot_option: typing.Optional[typing.Union[InstancePoolInstancePoolFleetAttributesFleetSpotOption, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddc51e7431c5af2002151ab97843f78f5a8a8cdbcc0c831bad1209ce5c99f77e(
    *,
    allocation_strategy: builtins.str,
    instance_pools_to_use_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb7024030e39296f450a4bfd27536a8c73c24c9a677f3c2360bbce13421a71b4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69c76d3d7e97a3607349dd266cef12a12056c9ec9a0a9968e6d31be2166ab76c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11cc4648bde1705d9653bfaa5b26d8ab3bc066d37996a21d03d32b9b7e137c44(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4022b2860337c140abd38ae8af9619a22c39a5be68bb995b30c7f8ded9038eb(
    value: typing.Optional[InstancePoolInstancePoolFleetAttributesFleetOnDemandOption],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fb93437ea198df7da8de576786f34b12b6a7ca5c6529b6b669ab35c87e9be8f(
    *,
    allocation_strategy: builtins.str,
    instance_pools_to_use_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86bf10666d0cd2e5dbc39b00159f47e1e7acce3dc9cabb6187f66a4ac3bfc999(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4a61dc032da1389d8fe7721df562db78d7646a00ce08ba144c8d41d6459a9c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__914de61e01ee578f2a7a1b6860b05939a1343e69d308ed339d0b8cd77ce3c423(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c60f43a73e49b81ee595ee4af90cb6a56d3f56bc17149d7b42aaa4545fd76661(
    value: typing.Optional[InstancePoolInstancePoolFleetAttributesFleetSpotOption],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f7fb24d19008dac805f57b2235b04da17be33107ce72c1b1e61d35960fc6a43(
    *,
    availability_zone: builtins.str,
    instance_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75b141658659ac95242b575a6f470494a4f3ef6dfd80be29c2bd48399428ffb7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9419b356cccab5699f18e8ef87017d8ca9a8f7fd0eef24ff2a14b357bf559ae1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fff06d97d8b05460f6259b838684bbca5c61364f164d3c629ce13e078a5a971(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5635c2e246908a60098ddd650e0deb9aaf628d24c7e2e0327482b9c26101fe0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79fbaba38801a59d50109ccae2b2c5e7118d1bc968adcf0e2292bd88d7112357(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b3b059df66f1dbda70c9d761368a9a0d41b1a4eca998e67f4ff271957ea216b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07a72c5d61a95a72f01385612405b43a87da00268d0967d17e63cd308e4f1618(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b69c07cc3ee110f56c42041c4298a418a357bb40a1d557797cd11c4dd55adb4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8c444d1a516247a4b97c6aac92321b4281c7e0581a15c809bc30c7d2b61d59e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2abe6d857642ee98f75fb3fce79539d62bbc606391c9948aa90f5132f0bf095(
    value: typing.Optional[typing.Union[InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__770d487793b9246a1febd49ae9b38df33b54bbb9e1331426ee1225a2a83d19cd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f27dcbe32f0aeaf8cb2bab2cc8993217eac91d2ca7b1276cf7015eccf03164d8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[InstancePoolInstancePoolFleetAttributesLaunchTemplateOverride, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0874263d116b60b5fe66db11737fc9f4b2c91d0ad80ef69d48dc2eb67eaef87f(
    value: typing.Optional[InstancePoolInstancePoolFleetAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebfa3e0630de3f821247be7b1a7863ecf90c3abc961f259cf5e5065ad21cb7d9(
    *,
    url: builtins.str,
    basic_auth: typing.Optional[typing.Union[InstancePoolPreloadedDockerImageBasicAuth, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf3f8612264520bb04033f4f367c35d3f090ec59e4c1138ede9332dd48d6cc1a(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d95d074a4f1598a16e693ca56ab0fda1098ece76fb66889d05e5cd996db4ae01(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf2ec25e0f502fadc1788d6d8725221edf681f4c2b1eccbec70d16f672f43455(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5530a57e3ad2decccacdc69a241d9d248fafc4c312424743cb8c43c62e77d5a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26821032d9e394093aa1c04a5ca232920898e7d18b7e6aa60b6141faf15ba371(
    value: typing.Optional[InstancePoolPreloadedDockerImageBasicAuth],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8188dbf8fd3500adfc18b412558305b15523ada01e66f641becaaef6c568add9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52ab10ac8dca86aeed98420e8401ac83a40cc54df69ce2f5235fd95ce2ba9595(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b97c7ae8852e26f4e8ae0ec898811848273b717d98bcef183dcfbf5e90ff9c53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99f8fac2cd10e25bb0f81d127c726acab7548b3fb28696afe42b9646f2485aa0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30d501405bf282efa4fd69284225cd7991abecce1ab8c40b72c7f7217cae9308(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a204830ad9e4a3b01e0bbc60405cbc392f50fc42f4313d538e0086b0cd866feb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[InstancePoolPreloadedDockerImage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__893c8b29e6ac174f8f7a9558d59a551b6cb73ba1d33805e7c702967b4ae4becd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7edb3892fd8f4ad7972eef5bdd9ef74191183254ff495c53b775dd02950e80d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__763bdf3547c1d99f3fae009cdad4929792c4dc49f35eadc6193807b25c8438a4(
    value: typing.Optional[typing.Union[InstancePoolPreloadedDockerImage, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
