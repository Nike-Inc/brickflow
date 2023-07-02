'''
# `databricks_cluster`

Refer to the Terraform Registory for docs: [`databricks_cluster`](https://www.terraform.io/docs/providers/databricks/r/cluster).
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


class Cluster(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.Cluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/cluster databricks_cluster}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        spark_version: builtins.str,
        apply_policy_default_values: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        autoscale: typing.Optional[typing.Union["ClusterAutoscale", typing.Dict[builtins.str, typing.Any]]] = None,
        autotermination_minutes: typing.Optional[jsii.Number] = None,
        aws_attributes: typing.Optional[typing.Union["ClusterAwsAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_attributes: typing.Optional[typing.Union["ClusterAzureAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        cluster_log_conf: typing.Optional[typing.Union["ClusterClusterLogConf", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_mount_info: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ClusterClusterMountInfo", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        data_security_mode: typing.Optional[builtins.str] = None,
        docker_image: typing.Optional[typing.Union["ClusterDockerImage", typing.Dict[builtins.str, typing.Any]]] = None,
        driver_instance_pool_id: typing.Optional[builtins.str] = None,
        driver_node_type_id: typing.Optional[builtins.str] = None,
        enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_local_disk_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        gcp_attributes: typing.Optional[typing.Union["ClusterGcpAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        idempotency_token: typing.Optional[builtins.str] = None,
        init_scripts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ClusterInitScripts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        instance_pool_id: typing.Optional[builtins.str] = None,
        is_pinned: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        library: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ClusterLibrary", typing.Dict[builtins.str, typing.Any]]]]] = None,
        node_type_id: typing.Optional[builtins.str] = None,
        num_workers: typing.Optional[jsii.Number] = None,
        policy_id: typing.Optional[builtins.str] = None,
        runtime_engine: typing.Optional[builtins.str] = None,
        single_user_name: typing.Optional[builtins.str] = None,
        spark_conf: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        spark_env_vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ClusterTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        workload_type: typing.Optional[typing.Union["ClusterWorkloadType", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/cluster databricks_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param spark_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_version Cluster#spark_version}.
        :param apply_policy_default_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#apply_policy_default_values Cluster#apply_policy_default_values}.
        :param autoscale: autoscale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#autoscale Cluster#autoscale}
        :param autotermination_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#autotermination_minutes Cluster#autotermination_minutes}.
        :param aws_attributes: aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#aws_attributes Cluster#aws_attributes}
        :param azure_attributes: azure_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#azure_attributes Cluster#azure_attributes}
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_id Cluster#cluster_id}.
        :param cluster_log_conf: cluster_log_conf block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_log_conf Cluster#cluster_log_conf}
        :param cluster_mount_info: cluster_mount_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_mount_info Cluster#cluster_mount_info}
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_name Cluster#cluster_name}.
        :param custom_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#custom_tags Cluster#custom_tags}.
        :param data_security_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#data_security_mode Cluster#data_security_mode}.
        :param docker_image: docker_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#docker_image Cluster#docker_image}
        :param driver_instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#driver_instance_pool_id Cluster#driver_instance_pool_id}.
        :param driver_node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#driver_node_type_id Cluster#driver_node_type_id}.
        :param enable_elastic_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_elastic_disk Cluster#enable_elastic_disk}.
        :param enable_local_disk_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_local_disk_encryption Cluster#enable_local_disk_encryption}.
        :param gcp_attributes: gcp_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#gcp_attributes Cluster#gcp_attributes}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#id Cluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idempotency_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#idempotency_token Cluster#idempotency_token}.
        :param init_scripts: init_scripts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#init_scripts Cluster#init_scripts}
        :param instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#instance_pool_id Cluster#instance_pool_id}.
        :param is_pinned: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#is_pinned Cluster#is_pinned}.
        :param library: library block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#library Cluster#library}
        :param node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#node_type_id Cluster#node_type_id}.
        :param num_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#num_workers Cluster#num_workers}.
        :param policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#policy_id Cluster#policy_id}.
        :param runtime_engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#runtime_engine Cluster#runtime_engine}.
        :param single_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#single_user_name Cluster#single_user_name}.
        :param spark_conf: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_conf Cluster#spark_conf}.
        :param spark_env_vars: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_env_vars Cluster#spark_env_vars}.
        :param ssh_public_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ssh_public_keys Cluster#ssh_public_keys}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#timeouts Cluster#timeouts}
        :param workload_type: workload_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#workload_type Cluster#workload_type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36a3206048502333d9aff7a4f56841ba1a9962695c76116ee7f47aaa93570b45)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ClusterConfig(
            spark_version=spark_version,
            apply_policy_default_values=apply_policy_default_values,
            autoscale=autoscale,
            autotermination_minutes=autotermination_minutes,
            aws_attributes=aws_attributes,
            azure_attributes=azure_attributes,
            cluster_id=cluster_id,
            cluster_log_conf=cluster_log_conf,
            cluster_mount_info=cluster_mount_info,
            cluster_name=cluster_name,
            custom_tags=custom_tags,
            data_security_mode=data_security_mode,
            docker_image=docker_image,
            driver_instance_pool_id=driver_instance_pool_id,
            driver_node_type_id=driver_node_type_id,
            enable_elastic_disk=enable_elastic_disk,
            enable_local_disk_encryption=enable_local_disk_encryption,
            gcp_attributes=gcp_attributes,
            id=id,
            idempotency_token=idempotency_token,
            init_scripts=init_scripts,
            instance_pool_id=instance_pool_id,
            is_pinned=is_pinned,
            library=library,
            node_type_id=node_type_id,
            num_workers=num_workers,
            policy_id=policy_id,
            runtime_engine=runtime_engine,
            single_user_name=single_user_name,
            spark_conf=spark_conf,
            spark_env_vars=spark_env_vars,
            ssh_public_keys=ssh_public_keys,
            timeouts=timeouts,
            workload_type=workload_type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAutoscale")
    def put_autoscale(
        self,
        *,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#max_workers Cluster#max_workers}.
        :param min_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#min_workers Cluster#min_workers}.
        '''
        value = ClusterAutoscale(max_workers=max_workers, min_workers=min_workers)

        return typing.cast(None, jsii.invoke(self, "putAutoscale", [value]))

    @jsii.member(jsii_name="putAwsAttributes")
    def put_aws_attributes(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        ebs_volume_count: typing.Optional[jsii.Number] = None,
        ebs_volume_size: typing.Optional[jsii.Number] = None,
        ebs_volume_type: typing.Optional[builtins.str] = None,
        first_on_demand: typing.Optional[jsii.Number] = None,
        instance_profile_arn: typing.Optional[builtins.str] = None,
        spot_bid_price_percent: typing.Optional[jsii.Number] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.
        :param ebs_volume_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_count Cluster#ebs_volume_count}.
        :param ebs_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_size Cluster#ebs_volume_size}.
        :param ebs_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_type Cluster#ebs_volume_type}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#first_on_demand Cluster#first_on_demand}.
        :param instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#instance_profile_arn Cluster#instance_profile_arn}.
        :param spot_bid_price_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spot_bid_price_percent Cluster#spot_bid_price_percent}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#zone_id Cluster#zone_id}.
        '''
        value = ClusterAwsAttributes(
            availability=availability,
            ebs_volume_count=ebs_volume_count,
            ebs_volume_size=ebs_volume_size,
            ebs_volume_type=ebs_volume_type,
            first_on_demand=first_on_demand,
            instance_profile_arn=instance_profile_arn,
            spot_bid_price_percent=spot_bid_price_percent,
            zone_id=zone_id,
        )

        return typing.cast(None, jsii.invoke(self, "putAwsAttributes", [value]))

    @jsii.member(jsii_name="putAzureAttributes")
    def put_azure_attributes(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        first_on_demand: typing.Optional[jsii.Number] = None,
        spot_bid_max_price: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#first_on_demand Cluster#first_on_demand}.
        :param spot_bid_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spot_bid_max_price Cluster#spot_bid_max_price}.
        '''
        value = ClusterAzureAttributes(
            availability=availability,
            first_on_demand=first_on_demand,
            spot_bid_max_price=spot_bid_max_price,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureAttributes", [value]))

    @jsii.member(jsii_name="putClusterLogConf")
    def put_cluster_log_conf(
        self,
        *,
        dbfs: typing.Optional[typing.Union["ClusterClusterLogConfDbfs", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["ClusterClusterLogConfS3", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dbfs: dbfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#dbfs Cluster#dbfs}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#s3 Cluster#s3}
        '''
        value = ClusterClusterLogConf(dbfs=dbfs, s3=s3)

        return typing.cast(None, jsii.invoke(self, "putClusterLogConf", [value]))

    @jsii.member(jsii_name="putClusterMountInfo")
    def put_cluster_mount_info(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ClusterClusterMountInfo", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77b8337184e282fb74f740e86ca3551f4f7f6f172b01bbb3a498e5c2ea3d9c32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putClusterMountInfo", [value]))

    @jsii.member(jsii_name="putDockerImage")
    def put_docker_image(
        self,
        *,
        url: builtins.str,
        basic_auth: typing.Optional[typing.Union["ClusterDockerImageBasicAuth", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#url Cluster#url}.
        :param basic_auth: basic_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#basic_auth Cluster#basic_auth}
        '''
        value = ClusterDockerImage(url=url, basic_auth=basic_auth)

        return typing.cast(None, jsii.invoke(self, "putDockerImage", [value]))

    @jsii.member(jsii_name="putGcpAttributes")
    def put_gcp_attributes(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        boot_disk_size: typing.Optional[jsii.Number] = None,
        google_service_account: typing.Optional[builtins.str] = None,
        use_preemptible_executors: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.
        :param boot_disk_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#boot_disk_size Cluster#boot_disk_size}.
        :param google_service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#google_service_account Cluster#google_service_account}.
        :param use_preemptible_executors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#use_preemptible_executors Cluster#use_preemptible_executors}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#zone_id Cluster#zone_id}.
        '''
        value = ClusterGcpAttributes(
            availability=availability,
            boot_disk_size=boot_disk_size,
            google_service_account=google_service_account,
            use_preemptible_executors=use_preemptible_executors,
            zone_id=zone_id,
        )

        return typing.cast(None, jsii.invoke(self, "putGcpAttributes", [value]))

    @jsii.member(jsii_name="putInitScripts")
    def put_init_scripts(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ClusterInitScripts", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d45f4b5255c9d996654ab273cfff68c8c5fc22dce2938b7df48c1bd7c6cd66c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInitScripts", [value]))

    @jsii.member(jsii_name="putLibrary")
    def put_library(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ClusterLibrary", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5a9a4a9f21f40274a26ecb4a86a9f3557fd0cdc5e8c8417fd801a36cd2fac4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLibrary", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#create Cluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#delete Cluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#update Cluster#update}.
        '''
        value = ClusterTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWorkloadType")
    def put_workload_type(
        self,
        *,
        clients: typing.Union["ClusterWorkloadTypeClients", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param clients: clients block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#clients Cluster#clients}
        '''
        value = ClusterWorkloadType(clients=clients)

        return typing.cast(None, jsii.invoke(self, "putWorkloadType", [value]))

    @jsii.member(jsii_name="resetApplyPolicyDefaultValues")
    def reset_apply_policy_default_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplyPolicyDefaultValues", []))

    @jsii.member(jsii_name="resetAutoscale")
    def reset_autoscale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscale", []))

    @jsii.member(jsii_name="resetAutoterminationMinutes")
    def reset_autotermination_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoterminationMinutes", []))

    @jsii.member(jsii_name="resetAwsAttributes")
    def reset_aws_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsAttributes", []))

    @jsii.member(jsii_name="resetAzureAttributes")
    def reset_azure_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureAttributes", []))

    @jsii.member(jsii_name="resetClusterId")
    def reset_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterId", []))

    @jsii.member(jsii_name="resetClusterLogConf")
    def reset_cluster_log_conf(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterLogConf", []))

    @jsii.member(jsii_name="resetClusterMountInfo")
    def reset_cluster_mount_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterMountInfo", []))

    @jsii.member(jsii_name="resetClusterName")
    def reset_cluster_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterName", []))

    @jsii.member(jsii_name="resetCustomTags")
    def reset_custom_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomTags", []))

    @jsii.member(jsii_name="resetDataSecurityMode")
    def reset_data_security_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataSecurityMode", []))

    @jsii.member(jsii_name="resetDockerImage")
    def reset_docker_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerImage", []))

    @jsii.member(jsii_name="resetDriverInstancePoolId")
    def reset_driver_instance_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverInstancePoolId", []))

    @jsii.member(jsii_name="resetDriverNodeTypeId")
    def reset_driver_node_type_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverNodeTypeId", []))

    @jsii.member(jsii_name="resetEnableElasticDisk")
    def reset_enable_elastic_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableElasticDisk", []))

    @jsii.member(jsii_name="resetEnableLocalDiskEncryption")
    def reset_enable_local_disk_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableLocalDiskEncryption", []))

    @jsii.member(jsii_name="resetGcpAttributes")
    def reset_gcp_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpAttributes", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdempotencyToken")
    def reset_idempotency_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdempotencyToken", []))

    @jsii.member(jsii_name="resetInitScripts")
    def reset_init_scripts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitScripts", []))

    @jsii.member(jsii_name="resetInstancePoolId")
    def reset_instance_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancePoolId", []))

    @jsii.member(jsii_name="resetIsPinned")
    def reset_is_pinned(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsPinned", []))

    @jsii.member(jsii_name="resetLibrary")
    def reset_library(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLibrary", []))

    @jsii.member(jsii_name="resetNodeTypeId")
    def reset_node_type_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeTypeId", []))

    @jsii.member(jsii_name="resetNumWorkers")
    def reset_num_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumWorkers", []))

    @jsii.member(jsii_name="resetPolicyId")
    def reset_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyId", []))

    @jsii.member(jsii_name="resetRuntimeEngine")
    def reset_runtime_engine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntimeEngine", []))

    @jsii.member(jsii_name="resetSingleUserName")
    def reset_single_user_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleUserName", []))

    @jsii.member(jsii_name="resetSparkConf")
    def reset_spark_conf(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkConf", []))

    @jsii.member(jsii_name="resetSparkEnvVars")
    def reset_spark_env_vars(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkEnvVars", []))

    @jsii.member(jsii_name="resetSshPublicKeys")
    def reset_ssh_public_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshPublicKeys", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWorkloadType")
    def reset_workload_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkloadType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="autoscale")
    def autoscale(self) -> "ClusterAutoscaleOutputReference":
        return typing.cast("ClusterAutoscaleOutputReference", jsii.get(self, "autoscale"))

    @builtins.property
    @jsii.member(jsii_name="awsAttributes")
    def aws_attributes(self) -> "ClusterAwsAttributesOutputReference":
        return typing.cast("ClusterAwsAttributesOutputReference", jsii.get(self, "awsAttributes"))

    @builtins.property
    @jsii.member(jsii_name="azureAttributes")
    def azure_attributes(self) -> "ClusterAzureAttributesOutputReference":
        return typing.cast("ClusterAzureAttributesOutputReference", jsii.get(self, "azureAttributes"))

    @builtins.property
    @jsii.member(jsii_name="clusterLogConf")
    def cluster_log_conf(self) -> "ClusterClusterLogConfOutputReference":
        return typing.cast("ClusterClusterLogConfOutputReference", jsii.get(self, "clusterLogConf"))

    @builtins.property
    @jsii.member(jsii_name="clusterMountInfo")
    def cluster_mount_info(self) -> "ClusterClusterMountInfoList":
        return typing.cast("ClusterClusterMountInfoList", jsii.get(self, "clusterMountInfo"))

    @builtins.property
    @jsii.member(jsii_name="defaultTags")
    def default_tags(self) -> _cdktf_9a9027ec.StringMap:
        return typing.cast(_cdktf_9a9027ec.StringMap, jsii.get(self, "defaultTags"))

    @builtins.property
    @jsii.member(jsii_name="dockerImage")
    def docker_image(self) -> "ClusterDockerImageOutputReference":
        return typing.cast("ClusterDockerImageOutputReference", jsii.get(self, "dockerImage"))

    @builtins.property
    @jsii.member(jsii_name="gcpAttributes")
    def gcp_attributes(self) -> "ClusterGcpAttributesOutputReference":
        return typing.cast("ClusterGcpAttributesOutputReference", jsii.get(self, "gcpAttributes"))

    @builtins.property
    @jsii.member(jsii_name="initScripts")
    def init_scripts(self) -> "ClusterInitScriptsList":
        return typing.cast("ClusterInitScriptsList", jsii.get(self, "initScripts"))

    @builtins.property
    @jsii.member(jsii_name="library")
    def library(self) -> "ClusterLibraryList":
        return typing.cast("ClusterLibraryList", jsii.get(self, "library"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ClusterTimeoutsOutputReference":
        return typing.cast("ClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="workloadType")
    def workload_type(self) -> "ClusterWorkloadTypeOutputReference":
        return typing.cast("ClusterWorkloadTypeOutputReference", jsii.get(self, "workloadType"))

    @builtins.property
    @jsii.member(jsii_name="applyPolicyDefaultValuesInput")
    def apply_policy_default_values_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "applyPolicyDefaultValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleInput")
    def autoscale_input(self) -> typing.Optional["ClusterAutoscale"]:
        return typing.cast(typing.Optional["ClusterAutoscale"], jsii.get(self, "autoscaleInput"))

    @builtins.property
    @jsii.member(jsii_name="autoterminationMinutesInput")
    def autotermination_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "autoterminationMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="awsAttributesInput")
    def aws_attributes_input(self) -> typing.Optional["ClusterAwsAttributes"]:
        return typing.cast(typing.Optional["ClusterAwsAttributes"], jsii.get(self, "awsAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="azureAttributesInput")
    def azure_attributes_input(self) -> typing.Optional["ClusterAzureAttributes"]:
        return typing.cast(typing.Optional["ClusterAzureAttributes"], jsii.get(self, "azureAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterLogConfInput")
    def cluster_log_conf_input(self) -> typing.Optional["ClusterClusterLogConf"]:
        return typing.cast(typing.Optional["ClusterClusterLogConf"], jsii.get(self, "clusterLogConfInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterMountInfoInput")
    def cluster_mount_info_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterClusterMountInfo"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterClusterMountInfo"]]], jsii.get(self, "clusterMountInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterNameInput")
    def cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customTagsInput")
    def custom_tags_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSecurityModeInput")
    def data_security_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSecurityModeInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerImageInput")
    def docker_image_input(self) -> typing.Optional["ClusterDockerImage"]:
        return typing.cast(typing.Optional["ClusterDockerImage"], jsii.get(self, "dockerImageInput"))

    @builtins.property
    @jsii.member(jsii_name="driverInstancePoolIdInput")
    def driver_instance_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInstancePoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="driverNodeTypeIdInput")
    def driver_node_type_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverNodeTypeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="enableElasticDiskInput")
    def enable_elastic_disk_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableElasticDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="enableLocalDiskEncryptionInput")
    def enable_local_disk_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableLocalDiskEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="gcpAttributesInput")
    def gcp_attributes_input(self) -> typing.Optional["ClusterGcpAttributes"]:
        return typing.cast(typing.Optional["ClusterGcpAttributes"], jsii.get(self, "gcpAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="idempotencyTokenInput")
    def idempotency_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idempotencyTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initScriptsInput")
    def init_scripts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterInitScripts"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterInitScripts"]]], jsii.get(self, "initScriptsInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolIdInput")
    def instance_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instancePoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="isPinnedInput")
    def is_pinned_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "isPinnedInput"))

    @builtins.property
    @jsii.member(jsii_name="libraryInput")
    def library_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterLibrary"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterLibrary"]]], jsii.get(self, "libraryInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeTypeIdInput")
    def node_type_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeTypeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="numWorkersInput")
    def num_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="policyIdInput")
    def policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeEngineInput")
    def runtime_engine_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeEngineInput"))

    @builtins.property
    @jsii.member(jsii_name="singleUserNameInput")
    def single_user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "singleUserNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkConfInput")
    def spark_conf_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sparkConfInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkEnvVarsInput")
    def spark_env_vars_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sparkEnvVarsInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkVersionInput")
    def spark_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sparkVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeysInput")
    def ssh_public_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sshPublicKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ClusterTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ClusterTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="workloadTypeInput")
    def workload_type_input(self) -> typing.Optional["ClusterWorkloadType"]:
        return typing.cast(typing.Optional["ClusterWorkloadType"], jsii.get(self, "workloadTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="applyPolicyDefaultValues")
    def apply_policy_default_values(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "applyPolicyDefaultValues"))

    @apply_policy_default_values.setter
    def apply_policy_default_values(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7cabbf0d6498931ae157c430bf39665c10ffea740f61d9ab7268362f8f7f881)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyPolicyDefaultValues", value)

    @builtins.property
    @jsii.member(jsii_name="autoterminationMinutes")
    def autotermination_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "autoterminationMinutes"))

    @autotermination_minutes.setter
    def autotermination_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2815e4e079050d81fdfc1cf01a79e883a2495044e6166a3b3c7f78272e4b1c27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoterminationMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ba01516306c52e1595d9a6f97f0fba15f1d1fa0906da3df1843d7b33f4d3d94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f60eec96f8acccca175c5e8c71028a8034f7733d87cc54bba294ff46016c74ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="customTags")
    def custom_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customTags"))

    @custom_tags.setter
    def custom_tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e0320aae032d8f03d5acd41313da90baf7fb01b0180e6ffd3d61ae8af52d350)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customTags", value)

    @builtins.property
    @jsii.member(jsii_name="dataSecurityMode")
    def data_security_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSecurityMode"))

    @data_security_mode.setter
    def data_security_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1e3e826e56a954b3d855e11cba3f9d9c6685e39a2c66acfc10cc2dd30ff7d52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSecurityMode", value)

    @builtins.property
    @jsii.member(jsii_name="driverInstancePoolId")
    def driver_instance_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driverInstancePoolId"))

    @driver_instance_pool_id.setter
    def driver_instance_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce09e7a0a3b35bd02eced9be68cc78c97ba7beb50ac5bbe8a953b7d9027f3d76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverInstancePoolId", value)

    @builtins.property
    @jsii.member(jsii_name="driverNodeTypeId")
    def driver_node_type_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driverNodeTypeId"))

    @driver_node_type_id.setter
    def driver_node_type_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0de5b50e979d719699b92adb86cb819244ecec94e3be70545edf528e0cdd60bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverNodeTypeId", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__93dbd987eba505db154a14da125bc1e22f31770df7ef01d945153fcecf70031e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableElasticDisk", value)

    @builtins.property
    @jsii.member(jsii_name="enableLocalDiskEncryption")
    def enable_local_disk_encryption(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableLocalDiskEncryption"))

    @enable_local_disk_encryption.setter
    def enable_local_disk_encryption(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3021600a1e56cba1a8ce733808acc7fcda74bd142a84595ce342ed6fb49f0f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableLocalDiskEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e99215eabdb87698969071969e44ccda3fe16c44de75b043b68bf712fe169aa7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="idempotencyToken")
    def idempotency_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idempotencyToken"))

    @idempotency_token.setter
    def idempotency_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0e831b68c49f94b0203c838ea45889d71eeb456249bc3ee018ba22d3c91ff7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idempotencyToken", value)

    @builtins.property
    @jsii.member(jsii_name="instancePoolId")
    def instance_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instancePoolId"))

    @instance_pool_id.setter
    def instance_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30893f97d75bb269317b623d3d8cb3aed547b9f6fa69b30bcbf9b6d6cff13ec8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instancePoolId", value)

    @builtins.property
    @jsii.member(jsii_name="isPinned")
    def is_pinned(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "isPinned"))

    @is_pinned.setter
    def is_pinned(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a7eeb0b6d5f23f9851583411621dc5fdacfce38b6dfcdda9e1a53921d6cca65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isPinned", value)

    @builtins.property
    @jsii.member(jsii_name="nodeTypeId")
    def node_type_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeTypeId"))

    @node_type_id.setter
    def node_type_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b699f459568e888b634d73fe252b3c6d606f8d3cb9f1fd4e93aa315b9b66bbcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeTypeId", value)

    @builtins.property
    @jsii.member(jsii_name="numWorkers")
    def num_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numWorkers"))

    @num_workers.setter
    def num_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f932a551fef8dafd16385fcbbb517d1baf7d515fc7bd9aaeabedb55bed2ec7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyId"))

    @policy_id.setter
    def policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c953fd3ef5af1a46aa69c4585d77a655716b686e68ddb0255c6d65ab744dec9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyId", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeEngine")
    def runtime_engine(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtimeEngine"))

    @runtime_engine.setter
    def runtime_engine(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc6628aad3d1cc745affe89e7a67c258ca04c8009429010c58f8e5a49b6e0a28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeEngine", value)

    @builtins.property
    @jsii.member(jsii_name="singleUserName")
    def single_user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "singleUserName"))

    @single_user_name.setter
    def single_user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bae38e870f81c0b261606c152e0e3284bdaa614ee015b28032fdee25f81131c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singleUserName", value)

    @builtins.property
    @jsii.member(jsii_name="sparkConf")
    def spark_conf(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sparkConf"))

    @spark_conf.setter
    def spark_conf(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d27c86ab0484f826ded796b14f133c650e6cc5419810ceda7ee665f611eb656)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkConf", value)

    @builtins.property
    @jsii.member(jsii_name="sparkEnvVars")
    def spark_env_vars(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sparkEnvVars"))

    @spark_env_vars.setter
    def spark_env_vars(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eebec4050a340c67486e772f758fb81f2dba6813577a6607ebf2a416f2b27465)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkEnvVars", value)

    @builtins.property
    @jsii.member(jsii_name="sparkVersion")
    def spark_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sparkVersion"))

    @spark_version.setter
    def spark_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad283c85743500c809e84234dffb1e9a58afb0e99759541149abda7962d7d488)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkVersion", value)

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeys")
    def ssh_public_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sshPublicKeys"))

    @ssh_public_keys.setter
    def ssh_public_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ba63478bcd5da4a8fc3f4e913208a94122c0b5d986e05da1857ba725fcd3f06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPublicKeys", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterAutoscale",
    jsii_struct_bases=[],
    name_mapping={"max_workers": "maxWorkers", "min_workers": "minWorkers"},
)
class ClusterAutoscale:
    def __init__(
        self,
        *,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#max_workers Cluster#max_workers}.
        :param min_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#min_workers Cluster#min_workers}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66c74f5775ba0d7faa41eb8981851bd915e25b7b61f359b00c886a4e861958ad)
            check_type(argname="argument max_workers", value=max_workers, expected_type=type_hints["max_workers"])
            check_type(argname="argument min_workers", value=min_workers, expected_type=type_hints["min_workers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max_workers is not None:
            self._values["max_workers"] = max_workers
        if min_workers is not None:
            self._values["min_workers"] = min_workers

    @builtins.property
    def max_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#max_workers Cluster#max_workers}.'''
        result = self._values.get("max_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#min_workers Cluster#min_workers}.'''
        result = self._values.get("min_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterAutoscale(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterAutoscaleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterAutoscaleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d07d79f2666b2cb985530d9fd9d4694ac97d6cc9be72867fe120454f45ec44f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxWorkers")
    def reset_max_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxWorkers", []))

    @jsii.member(jsii_name="resetMinWorkers")
    def reset_min_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinWorkers", []))

    @builtins.property
    @jsii.member(jsii_name="maxWorkersInput")
    def max_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="minWorkersInput")
    def min_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWorkers")
    def max_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxWorkers"))

    @max_workers.setter
    def max_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea0a156b7d5f9c09af769f8039137c053ee031bcf9dc8693e9a88a0e46461604)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="minWorkers")
    def min_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minWorkers"))

    @min_workers.setter
    def min_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8164a07dfd9a9ea59420bee66408f619ea4fffccc5234d370a1d1f7cb4ab0e8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterAutoscale]:
        return typing.cast(typing.Optional[ClusterAutoscale], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterAutoscale]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe1c2a6a0d3c78e3957c82ec8d98410e100eab3e2da05ffccfd32e62721c7482)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterAwsAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "ebs_volume_count": "ebsVolumeCount",
        "ebs_volume_size": "ebsVolumeSize",
        "ebs_volume_type": "ebsVolumeType",
        "first_on_demand": "firstOnDemand",
        "instance_profile_arn": "instanceProfileArn",
        "spot_bid_price_percent": "spotBidPricePercent",
        "zone_id": "zoneId",
    },
)
class ClusterAwsAttributes:
    def __init__(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        ebs_volume_count: typing.Optional[jsii.Number] = None,
        ebs_volume_size: typing.Optional[jsii.Number] = None,
        ebs_volume_type: typing.Optional[builtins.str] = None,
        first_on_demand: typing.Optional[jsii.Number] = None,
        instance_profile_arn: typing.Optional[builtins.str] = None,
        spot_bid_price_percent: typing.Optional[jsii.Number] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.
        :param ebs_volume_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_count Cluster#ebs_volume_count}.
        :param ebs_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_size Cluster#ebs_volume_size}.
        :param ebs_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_type Cluster#ebs_volume_type}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#first_on_demand Cluster#first_on_demand}.
        :param instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#instance_profile_arn Cluster#instance_profile_arn}.
        :param spot_bid_price_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spot_bid_price_percent Cluster#spot_bid_price_percent}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#zone_id Cluster#zone_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2193581a055ae819d0e7cf74e2c3465586630c2fd281671392cc24a15f15fba)
            check_type(argname="argument availability", value=availability, expected_type=type_hints["availability"])
            check_type(argname="argument ebs_volume_count", value=ebs_volume_count, expected_type=type_hints["ebs_volume_count"])
            check_type(argname="argument ebs_volume_size", value=ebs_volume_size, expected_type=type_hints["ebs_volume_size"])
            check_type(argname="argument ebs_volume_type", value=ebs_volume_type, expected_type=type_hints["ebs_volume_type"])
            check_type(argname="argument first_on_demand", value=first_on_demand, expected_type=type_hints["first_on_demand"])
            check_type(argname="argument instance_profile_arn", value=instance_profile_arn, expected_type=type_hints["instance_profile_arn"])
            check_type(argname="argument spot_bid_price_percent", value=spot_bid_price_percent, expected_type=type_hints["spot_bid_price_percent"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability is not None:
            self._values["availability"] = availability
        if ebs_volume_count is not None:
            self._values["ebs_volume_count"] = ebs_volume_count
        if ebs_volume_size is not None:
            self._values["ebs_volume_size"] = ebs_volume_size
        if ebs_volume_type is not None:
            self._values["ebs_volume_type"] = ebs_volume_type
        if first_on_demand is not None:
            self._values["first_on_demand"] = first_on_demand
        if instance_profile_arn is not None:
            self._values["instance_profile_arn"] = instance_profile_arn
        if spot_bid_price_percent is not None:
            self._values["spot_bid_price_percent"] = spot_bid_price_percent
        if zone_id is not None:
            self._values["zone_id"] = zone_id

    @builtins.property
    def availability(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_volume_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_count Cluster#ebs_volume_count}.'''
        result = self._values.get("ebs_volume_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ebs_volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_size Cluster#ebs_volume_size}.'''
        result = self._values.get("ebs_volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ebs_volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ebs_volume_type Cluster#ebs_volume_type}.'''
        result = self._values.get("ebs_volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_on_demand(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#first_on_demand Cluster#first_on_demand}.'''
        result = self._values.get("first_on_demand")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#instance_profile_arn Cluster#instance_profile_arn}.'''
        result = self._values.get("instance_profile_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_bid_price_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spot_bid_price_percent Cluster#spot_bid_price_percent}.'''
        result = self._values.get("spot_bid_price_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#zone_id Cluster#zone_id}.'''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterAwsAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterAwsAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterAwsAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__092369b78a672ba593d7d65cfd79c0f8edae66f6a389ba51552e46adf88a6896)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAvailability")
    def reset_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailability", []))

    @jsii.member(jsii_name="resetEbsVolumeCount")
    def reset_ebs_volume_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsVolumeCount", []))

    @jsii.member(jsii_name="resetEbsVolumeSize")
    def reset_ebs_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsVolumeSize", []))

    @jsii.member(jsii_name="resetEbsVolumeType")
    def reset_ebs_volume_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsVolumeType", []))

    @jsii.member(jsii_name="resetFirstOnDemand")
    def reset_first_on_demand(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirstOnDemand", []))

    @jsii.member(jsii_name="resetInstanceProfileArn")
    def reset_instance_profile_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceProfileArn", []))

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
    @jsii.member(jsii_name="ebsVolumeCountInput")
    def ebs_volume_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ebsVolumeCountInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeSizeInput")
    def ebs_volume_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ebsVolumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeTypeInput")
    def ebs_volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ebsVolumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="firstOnDemandInput")
    def first_on_demand_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "firstOnDemandInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceProfileArnInput")
    def instance_profile_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceProfileArnInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__418a0ff089fc6c4ee128f272a62e604059b9217c7d5a000272db3c3c78440389)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeCount")
    def ebs_volume_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsVolumeCount"))

    @ebs_volume_count.setter
    def ebs_volume_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80f4fdbf37ef427aa85342c2883f546fe84e5ab6ce252febf9a00fb5d4185d42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeCount", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeSize")
    def ebs_volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsVolumeSize"))

    @ebs_volume_size.setter
    def ebs_volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24188179135cccff3f94ac5b46c60bcb328118c8b08630a12d01ab6406b7bca0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeType")
    def ebs_volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ebsVolumeType"))

    @ebs_volume_type.setter
    def ebs_volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36c7e3f56a6ded46e13083b9d75f06ef867eace4546ccfd69855f97823e77922)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeType", value)

    @builtins.property
    @jsii.member(jsii_name="firstOnDemand")
    def first_on_demand(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "firstOnDemand"))

    @first_on_demand.setter
    def first_on_demand(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ee17e4e0608e80e14a7ca3e4530234174fe4da9b28035f144ff6c013950b3d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstOnDemand", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfileArn")
    def instance_profile_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceProfileArn"))

    @instance_profile_arn.setter
    def instance_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ee132e336ec9e069c7f1a21a2dad592d9d0978732f07148636e715417616a71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="spotBidPricePercent")
    def spot_bid_price_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotBidPricePercent"))

    @spot_bid_price_percent.setter
    def spot_bid_price_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__286b832824cf24a3c0932e8c9c66d780aa4ea78e12fcdbeddb333a092eb9f313)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotBidPricePercent", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__948b9fc625995b48fd2f573b2337357f3871f8c585fadf74f093294323b095f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterAwsAttributes]:
        return typing.cast(typing.Optional[ClusterAwsAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterAwsAttributes]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__049a0bb0306f1718c1e85e70742d8922c5b73ff484ae2d43943b3b876ab8ed45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterAzureAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "first_on_demand": "firstOnDemand",
        "spot_bid_max_price": "spotBidMaxPrice",
    },
)
class ClusterAzureAttributes:
    def __init__(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        first_on_demand: typing.Optional[jsii.Number] = None,
        spot_bid_max_price: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#first_on_demand Cluster#first_on_demand}.
        :param spot_bid_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spot_bid_max_price Cluster#spot_bid_max_price}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a0d09e1c8bf1cebfaafa3d5babe5a174f67c451b2b28e78955bba23ae8f9ec4)
            check_type(argname="argument availability", value=availability, expected_type=type_hints["availability"])
            check_type(argname="argument first_on_demand", value=first_on_demand, expected_type=type_hints["first_on_demand"])
            check_type(argname="argument spot_bid_max_price", value=spot_bid_max_price, expected_type=type_hints["spot_bid_max_price"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability is not None:
            self._values["availability"] = availability
        if first_on_demand is not None:
            self._values["first_on_demand"] = first_on_demand
        if spot_bid_max_price is not None:
            self._values["spot_bid_max_price"] = spot_bid_max_price

    @builtins.property
    def availability(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_on_demand(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#first_on_demand Cluster#first_on_demand}.'''
        result = self._values.get("first_on_demand")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def spot_bid_max_price(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spot_bid_max_price Cluster#spot_bid_max_price}.'''
        result = self._values.get("spot_bid_max_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterAzureAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterAzureAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterAzureAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fb09e2b38270eac5420a0289aefc445ba2a7515c3d00efdcb40fdf3c52fd08ba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAvailability")
    def reset_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailability", []))

    @jsii.member(jsii_name="resetFirstOnDemand")
    def reset_first_on_demand(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirstOnDemand", []))

    @jsii.member(jsii_name="resetSpotBidMaxPrice")
    def reset_spot_bid_max_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpotBidMaxPrice", []))

    @builtins.property
    @jsii.member(jsii_name="availabilityInput")
    def availability_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="firstOnDemandInput")
    def first_on_demand_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "firstOnDemandInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__de23baa37454659256743a5f9f538acaefa23597b2e9b02e411ab2865524ed12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="firstOnDemand")
    def first_on_demand(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "firstOnDemand"))

    @first_on_demand.setter
    def first_on_demand(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c8b82de0a39dca5cc8566093bb073dd3a1f2ec0030be37786e5f3a6b14832e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstOnDemand", value)

    @builtins.property
    @jsii.member(jsii_name="spotBidMaxPrice")
    def spot_bid_max_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotBidMaxPrice"))

    @spot_bid_max_price.setter
    def spot_bid_max_price(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90a6bd3c39d1bd751e0cfc06f53d108a28b1db947af8561bb00abd7f13b819d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotBidMaxPrice", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterAzureAttributes]:
        return typing.cast(typing.Optional[ClusterAzureAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterAzureAttributes]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00f86a26ac9cf57d6bbdcb08818ce6b728c44658856d10155b562ed3acefabf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterClusterLogConf",
    jsii_struct_bases=[],
    name_mapping={"dbfs": "dbfs", "s3": "s3"},
)
class ClusterClusterLogConf:
    def __init__(
        self,
        *,
        dbfs: typing.Optional[typing.Union["ClusterClusterLogConfDbfs", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["ClusterClusterLogConfS3", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dbfs: dbfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#dbfs Cluster#dbfs}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#s3 Cluster#s3}
        '''
        if isinstance(dbfs, dict):
            dbfs = ClusterClusterLogConfDbfs(**dbfs)
        if isinstance(s3, dict):
            s3 = ClusterClusterLogConfS3(**s3)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92bf88827d2646e52cfde2eef5d59f8e28f643d3f120b9e125c3c24ddade8fe3)
            check_type(argname="argument dbfs", value=dbfs, expected_type=type_hints["dbfs"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dbfs is not None:
            self._values["dbfs"] = dbfs
        if s3 is not None:
            self._values["s3"] = s3

    @builtins.property
    def dbfs(self) -> typing.Optional["ClusterClusterLogConfDbfs"]:
        '''dbfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#dbfs Cluster#dbfs}
        '''
        result = self._values.get("dbfs")
        return typing.cast(typing.Optional["ClusterClusterLogConfDbfs"], result)

    @builtins.property
    def s3(self) -> typing.Optional["ClusterClusterLogConfS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#s3 Cluster#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["ClusterClusterLogConfS3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterClusterLogConf(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterClusterLogConfDbfs",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class ClusterClusterLogConfDbfs:
    def __init__(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__681511e5f1a9577eb7317b443085cbfdbaf0889414e77f24b02fb2dd2307d33d)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterClusterLogConfDbfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterClusterLogConfDbfsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterClusterLogConfDbfsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf5b0a45faa306950ce0ec3e530f6b677b0f35adbee0693d90e8c81a6d2c2c7b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e00db5b54bc9dd4d8aa150bf88ecb5e9ce1ae54ca2b105accfa3fa5131cc3c1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterClusterLogConfDbfs]:
        return typing.cast(typing.Optional[ClusterClusterLogConfDbfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterClusterLogConfDbfs]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c68b4451499c161d610019799e4b41f5a73467ca0aa2245e876c4776974d21a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterClusterLogConfOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterClusterLogConfOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__98a6c2bb5e5fd69a56e95ac72e5c8f6b1e08ddf34263f99470fdb5826fa6be17)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDbfs")
    def put_dbfs(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        value = ClusterClusterLogConfDbfs(destination=destination)

        return typing.cast(None, jsii.invoke(self, "putDbfs", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        destination: builtins.str,
        canned_acl: typing.Optional[builtins.str] = None,
        enable_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encryption_type: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#canned_acl Cluster#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_encryption Cluster#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#encryption_type Cluster#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#endpoint Cluster#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#kms_key Cluster#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#region Cluster#region}.
        '''
        value = ClusterClusterLogConfS3(
            destination=destination,
            canned_acl=canned_acl,
            enable_encryption=enable_encryption,
            encryption_type=encryption_type,
            endpoint=endpoint,
            kms_key=kms_key,
            region=region,
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="resetDbfs")
    def reset_dbfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbfs", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @builtins.property
    @jsii.member(jsii_name="dbfs")
    def dbfs(self) -> ClusterClusterLogConfDbfsOutputReference:
        return typing.cast(ClusterClusterLogConfDbfsOutputReference, jsii.get(self, "dbfs"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "ClusterClusterLogConfS3OutputReference":
        return typing.cast("ClusterClusterLogConfS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="dbfsInput")
    def dbfs_input(self) -> typing.Optional[ClusterClusterLogConfDbfs]:
        return typing.cast(typing.Optional[ClusterClusterLogConfDbfs], jsii.get(self, "dbfsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(self) -> typing.Optional["ClusterClusterLogConfS3"]:
        return typing.cast(typing.Optional["ClusterClusterLogConfS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterClusterLogConf]:
        return typing.cast(typing.Optional[ClusterClusterLogConf], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterClusterLogConf]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10043d5410466ab9c13d2169a04e4b1f4ea56eebd97dcb06a669bf85d907ea97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterClusterLogConfS3",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "canned_acl": "cannedAcl",
        "enable_encryption": "enableEncryption",
        "encryption_type": "encryptionType",
        "endpoint": "endpoint",
        "kms_key": "kmsKey",
        "region": "region",
    },
)
class ClusterClusterLogConfS3:
    def __init__(
        self,
        *,
        destination: builtins.str,
        canned_acl: typing.Optional[builtins.str] = None,
        enable_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encryption_type: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#canned_acl Cluster#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_encryption Cluster#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#encryption_type Cluster#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#endpoint Cluster#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#kms_key Cluster#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#region Cluster#region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__301b8a78c470b4d4fef46eb0f7c16d19c02b3ef10b6f7d3aa455034ac733cd65)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument canned_acl", value=canned_acl, expected_type=type_hints["canned_acl"])
            check_type(argname="argument enable_encryption", value=enable_encryption, expected_type=type_hints["enable_encryption"])
            check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
        }
        if canned_acl is not None:
            self._values["canned_acl"] = canned_acl
        if enable_encryption is not None:
            self._values["enable_encryption"] = enable_encryption
        if encryption_type is not None:
            self._values["encryption_type"] = encryption_type
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def canned_acl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#canned_acl Cluster#canned_acl}.'''
        result = self._values.get("canned_acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_encryption Cluster#enable_encryption}.'''
        result = self._values.get("enable_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encryption_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#encryption_type Cluster#encryption_type}.'''
        result = self._values.get("encryption_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#endpoint Cluster#endpoint}.'''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#kms_key Cluster#kms_key}.'''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#region Cluster#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterClusterLogConfS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterClusterLogConfS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterClusterLogConfS3OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5cb54b052a47534b588d62abfeef00192815e6d36a488d8da1ea75fbc922f509)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCannedAcl")
    def reset_canned_acl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCannedAcl", []))

    @jsii.member(jsii_name="resetEnableEncryption")
    def reset_enable_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableEncryption", []))

    @jsii.member(jsii_name="resetEncryptionType")
    def reset_encryption_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionType", []))

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @jsii.member(jsii_name="resetKmsKey")
    def reset_kms_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKey", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @builtins.property
    @jsii.member(jsii_name="cannedAclInput")
    def canned_acl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cannedAclInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="enableEncryptionInput")
    def enable_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionTypeInput")
    def encryption_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyInput")
    def kms_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="cannedAcl")
    def canned_acl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cannedAcl"))

    @canned_acl.setter
    def canned_acl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b47007f0f324003c744765b78e673b209f7505d1ca20f98ec216644b2742c08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cannedAcl", value)

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c018f96ed41f2df877ce72b56fe9420c8e3fc209f88b24ad28f8fcd7184a902f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="enableEncryption")
    def enable_encryption(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableEncryption"))

    @enable_encryption.setter
    def enable_encryption(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b51c57bd4496defbfe4dd329f051fec31a0273778e1f0dc350e7798ad87a8b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionType")
    def encryption_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionType"))

    @encryption_type.setter
    def encryption_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43d879c34a2de94785bc67dbb0d4dff17a68864ff52eca552a6cfe030e0dce26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c250a9d528845d4df966d09ae643c23b5c90c24728c50833eec70b7799f6e117)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d240cb7c4dfdb29e425642eae8103bdedd0a77ca69d384d6c3aa99b69a68658f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4086f8d40ff2c3d2b4d7d19afdaa262eb44070a4ce55c9c4535e87f918fb01b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterClusterLogConfS3]:
        return typing.cast(typing.Optional[ClusterClusterLogConfS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterClusterLogConfS3]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1622989cac13ddcc7ee8728d5a6dd4b57ec793b959143784f7f754b8c38f4bfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterClusterMountInfo",
    jsii_struct_bases=[],
    name_mapping={
        "local_mount_dir_path": "localMountDirPath",
        "network_filesystem_info": "networkFilesystemInfo",
        "remote_mount_dir_path": "remoteMountDirPath",
    },
)
class ClusterClusterMountInfo:
    def __init__(
        self,
        *,
        local_mount_dir_path: builtins.str,
        network_filesystem_info: typing.Union["ClusterClusterMountInfoNetworkFilesystemInfo", typing.Dict[builtins.str, typing.Any]],
        remote_mount_dir_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param local_mount_dir_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#local_mount_dir_path Cluster#local_mount_dir_path}.
        :param network_filesystem_info: network_filesystem_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#network_filesystem_info Cluster#network_filesystem_info}
        :param remote_mount_dir_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#remote_mount_dir_path Cluster#remote_mount_dir_path}.
        '''
        if isinstance(network_filesystem_info, dict):
            network_filesystem_info = ClusterClusterMountInfoNetworkFilesystemInfo(**network_filesystem_info)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__116a9f144b5725a425a9eb4b8c8a972ca5617fc6b1850b2f7cd1749988df47b4)
            check_type(argname="argument local_mount_dir_path", value=local_mount_dir_path, expected_type=type_hints["local_mount_dir_path"])
            check_type(argname="argument network_filesystem_info", value=network_filesystem_info, expected_type=type_hints["network_filesystem_info"])
            check_type(argname="argument remote_mount_dir_path", value=remote_mount_dir_path, expected_type=type_hints["remote_mount_dir_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "local_mount_dir_path": local_mount_dir_path,
            "network_filesystem_info": network_filesystem_info,
        }
        if remote_mount_dir_path is not None:
            self._values["remote_mount_dir_path"] = remote_mount_dir_path

    @builtins.property
    def local_mount_dir_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#local_mount_dir_path Cluster#local_mount_dir_path}.'''
        result = self._values.get("local_mount_dir_path")
        assert result is not None, "Required property 'local_mount_dir_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_filesystem_info(self) -> "ClusterClusterMountInfoNetworkFilesystemInfo":
        '''network_filesystem_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#network_filesystem_info Cluster#network_filesystem_info}
        '''
        result = self._values.get("network_filesystem_info")
        assert result is not None, "Required property 'network_filesystem_info' is missing"
        return typing.cast("ClusterClusterMountInfoNetworkFilesystemInfo", result)

    @builtins.property
    def remote_mount_dir_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#remote_mount_dir_path Cluster#remote_mount_dir_path}.'''
        result = self._values.get("remote_mount_dir_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterClusterMountInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterClusterMountInfoList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterClusterMountInfoList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aeea47c59ed795ef0fad8ad94706a587e2897af191eb68eb7270d363b7a835aa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ClusterClusterMountInfoOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1164e6b84fd560940a07c38b77496bc4c99472811e65f884e31f5162807f11a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ClusterClusterMountInfoOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19e31f0d216ce632dd1e8596f163bd047794d27d7f5424d8da3fe5628dafdf22)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd542198e72ee5363f173f4536038a15295815c1c1a886607290fb6779b2884c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d13c3728ed7d0b6f259f68f2ff7cfc566600effb2a104d31ae617aebe097070)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterClusterMountInfo]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterClusterMountInfo]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterClusterMountInfo]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d54fd2e5c4cbaa84115d7d2dd75a4edd2890f8f4fd00e7e66eb12022f0c0a30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterClusterMountInfoNetworkFilesystemInfo",
    jsii_struct_bases=[],
    name_mapping={"server_address": "serverAddress", "mount_options": "mountOptions"},
)
class ClusterClusterMountInfoNetworkFilesystemInfo:
    def __init__(
        self,
        *,
        server_address: builtins.str,
        mount_options: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param server_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#server_address Cluster#server_address}.
        :param mount_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#mount_options Cluster#mount_options}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a110197c8c1e6dd7eb926ecd3bb53e8fc7324dea484f26eb0da8924bb1c49a0)
            check_type(argname="argument server_address", value=server_address, expected_type=type_hints["server_address"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "server_address": server_address,
        }
        if mount_options is not None:
            self._values["mount_options"] = mount_options

    @builtins.property
    def server_address(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#server_address Cluster#server_address}.'''
        result = self._values.get("server_address")
        assert result is not None, "Required property 'server_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mount_options(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#mount_options Cluster#mount_options}.'''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterClusterMountInfoNetworkFilesystemInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterClusterMountInfoNetworkFilesystemInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterClusterMountInfoNetworkFilesystemInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f56455d8ebc7b4c196edb334bc1b6699ac028034b56bed6339b23f80c0edb04f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMountOptions")
    def reset_mount_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountOptions", []))

    @builtins.property
    @jsii.member(jsii_name="mountOptionsInput")
    def mount_options_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="serverAddressInput")
    def server_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81a0f59a66177874939da9d85e1e2a4295bcb9639dbf59f2570882bb8bfdf798)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountOptions", value)

    @builtins.property
    @jsii.member(jsii_name="serverAddress")
    def server_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverAddress"))

    @server_address.setter
    def server_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5aa18dad41d63fb6c5c6cb4409422ca92d492971b6fae55fc5adef2d8503751)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverAddress", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ClusterClusterMountInfoNetworkFilesystemInfo]:
        return typing.cast(typing.Optional[ClusterClusterMountInfoNetworkFilesystemInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ClusterClusterMountInfoNetworkFilesystemInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__470680cdfddce4ae343b945ffa3211be6de7ea067f3c5ffb2dfacc24c892c3d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterClusterMountInfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterClusterMountInfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__01ed70addc78e26f30e9235722d0cd3eb8abfdbc12fca2641f18912adc92bf5e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNetworkFilesystemInfo")
    def put_network_filesystem_info(
        self,
        *,
        server_address: builtins.str,
        mount_options: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param server_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#server_address Cluster#server_address}.
        :param mount_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#mount_options Cluster#mount_options}.
        '''
        value = ClusterClusterMountInfoNetworkFilesystemInfo(
            server_address=server_address, mount_options=mount_options
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkFilesystemInfo", [value]))

    @jsii.member(jsii_name="resetRemoteMountDirPath")
    def reset_remote_mount_dir_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteMountDirPath", []))

    @builtins.property
    @jsii.member(jsii_name="networkFilesystemInfo")
    def network_filesystem_info(
        self,
    ) -> ClusterClusterMountInfoNetworkFilesystemInfoOutputReference:
        return typing.cast(ClusterClusterMountInfoNetworkFilesystemInfoOutputReference, jsii.get(self, "networkFilesystemInfo"))

    @builtins.property
    @jsii.member(jsii_name="localMountDirPathInput")
    def local_mount_dir_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localMountDirPathInput"))

    @builtins.property
    @jsii.member(jsii_name="networkFilesystemInfoInput")
    def network_filesystem_info_input(
        self,
    ) -> typing.Optional[ClusterClusterMountInfoNetworkFilesystemInfo]:
        return typing.cast(typing.Optional[ClusterClusterMountInfoNetworkFilesystemInfo], jsii.get(self, "networkFilesystemInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteMountDirPathInput")
    def remote_mount_dir_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remoteMountDirPathInput"))

    @builtins.property
    @jsii.member(jsii_name="localMountDirPath")
    def local_mount_dir_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localMountDirPath"))

    @local_mount_dir_path.setter
    def local_mount_dir_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec934ee0128ef62df76388ca5705ed5bcf6300265cd927ff4ce9ec7676e56db7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localMountDirPath", value)

    @builtins.property
    @jsii.member(jsii_name="remoteMountDirPath")
    def remote_mount_dir_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remoteMountDirPath"))

    @remote_mount_dir_path.setter
    def remote_mount_dir_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec411b8dcbe5ab68ab483f04f4b564c9c9ea8d01106813d3045abbeebe309a10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteMountDirPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ClusterClusterMountInfo, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ClusterClusterMountInfo, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ClusterClusterMountInfo, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__101453a2b4ba6a40af722a2f2e1b5d6968fea19259c9cc241d9e305748324dcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "spark_version": "sparkVersion",
        "apply_policy_default_values": "applyPolicyDefaultValues",
        "autoscale": "autoscale",
        "autotermination_minutes": "autoterminationMinutes",
        "aws_attributes": "awsAttributes",
        "azure_attributes": "azureAttributes",
        "cluster_id": "clusterId",
        "cluster_log_conf": "clusterLogConf",
        "cluster_mount_info": "clusterMountInfo",
        "cluster_name": "clusterName",
        "custom_tags": "customTags",
        "data_security_mode": "dataSecurityMode",
        "docker_image": "dockerImage",
        "driver_instance_pool_id": "driverInstancePoolId",
        "driver_node_type_id": "driverNodeTypeId",
        "enable_elastic_disk": "enableElasticDisk",
        "enable_local_disk_encryption": "enableLocalDiskEncryption",
        "gcp_attributes": "gcpAttributes",
        "id": "id",
        "idempotency_token": "idempotencyToken",
        "init_scripts": "initScripts",
        "instance_pool_id": "instancePoolId",
        "is_pinned": "isPinned",
        "library": "library",
        "node_type_id": "nodeTypeId",
        "num_workers": "numWorkers",
        "policy_id": "policyId",
        "runtime_engine": "runtimeEngine",
        "single_user_name": "singleUserName",
        "spark_conf": "sparkConf",
        "spark_env_vars": "sparkEnvVars",
        "ssh_public_keys": "sshPublicKeys",
        "timeouts": "timeouts",
        "workload_type": "workloadType",
    },
)
class ClusterConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        spark_version: builtins.str,
        apply_policy_default_values: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        autoscale: typing.Optional[typing.Union[ClusterAutoscale, typing.Dict[builtins.str, typing.Any]]] = None,
        autotermination_minutes: typing.Optional[jsii.Number] = None,
        aws_attributes: typing.Optional[typing.Union[ClusterAwsAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
        azure_attributes: typing.Optional[typing.Union[ClusterAzureAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        cluster_log_conf: typing.Optional[typing.Union[ClusterClusterLogConf, typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_mount_info: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterClusterMountInfo, typing.Dict[builtins.str, typing.Any]]]]] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        data_security_mode: typing.Optional[builtins.str] = None,
        docker_image: typing.Optional[typing.Union["ClusterDockerImage", typing.Dict[builtins.str, typing.Any]]] = None,
        driver_instance_pool_id: typing.Optional[builtins.str] = None,
        driver_node_type_id: typing.Optional[builtins.str] = None,
        enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_local_disk_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        gcp_attributes: typing.Optional[typing.Union["ClusterGcpAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        idempotency_token: typing.Optional[builtins.str] = None,
        init_scripts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ClusterInitScripts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        instance_pool_id: typing.Optional[builtins.str] = None,
        is_pinned: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        library: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ClusterLibrary", typing.Dict[builtins.str, typing.Any]]]]] = None,
        node_type_id: typing.Optional[builtins.str] = None,
        num_workers: typing.Optional[jsii.Number] = None,
        policy_id: typing.Optional[builtins.str] = None,
        runtime_engine: typing.Optional[builtins.str] = None,
        single_user_name: typing.Optional[builtins.str] = None,
        spark_conf: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        spark_env_vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ClusterTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        workload_type: typing.Optional[typing.Union["ClusterWorkloadType", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param spark_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_version Cluster#spark_version}.
        :param apply_policy_default_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#apply_policy_default_values Cluster#apply_policy_default_values}.
        :param autoscale: autoscale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#autoscale Cluster#autoscale}
        :param autotermination_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#autotermination_minutes Cluster#autotermination_minutes}.
        :param aws_attributes: aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#aws_attributes Cluster#aws_attributes}
        :param azure_attributes: azure_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#azure_attributes Cluster#azure_attributes}
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_id Cluster#cluster_id}.
        :param cluster_log_conf: cluster_log_conf block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_log_conf Cluster#cluster_log_conf}
        :param cluster_mount_info: cluster_mount_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_mount_info Cluster#cluster_mount_info}
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_name Cluster#cluster_name}.
        :param custom_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#custom_tags Cluster#custom_tags}.
        :param data_security_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#data_security_mode Cluster#data_security_mode}.
        :param docker_image: docker_image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#docker_image Cluster#docker_image}
        :param driver_instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#driver_instance_pool_id Cluster#driver_instance_pool_id}.
        :param driver_node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#driver_node_type_id Cluster#driver_node_type_id}.
        :param enable_elastic_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_elastic_disk Cluster#enable_elastic_disk}.
        :param enable_local_disk_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_local_disk_encryption Cluster#enable_local_disk_encryption}.
        :param gcp_attributes: gcp_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#gcp_attributes Cluster#gcp_attributes}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#id Cluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idempotency_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#idempotency_token Cluster#idempotency_token}.
        :param init_scripts: init_scripts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#init_scripts Cluster#init_scripts}
        :param instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#instance_pool_id Cluster#instance_pool_id}.
        :param is_pinned: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#is_pinned Cluster#is_pinned}.
        :param library: library block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#library Cluster#library}
        :param node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#node_type_id Cluster#node_type_id}.
        :param num_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#num_workers Cluster#num_workers}.
        :param policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#policy_id Cluster#policy_id}.
        :param runtime_engine: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#runtime_engine Cluster#runtime_engine}.
        :param single_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#single_user_name Cluster#single_user_name}.
        :param spark_conf: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_conf Cluster#spark_conf}.
        :param spark_env_vars: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_env_vars Cluster#spark_env_vars}.
        :param ssh_public_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ssh_public_keys Cluster#ssh_public_keys}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#timeouts Cluster#timeouts}
        :param workload_type: workload_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#workload_type Cluster#workload_type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(autoscale, dict):
            autoscale = ClusterAutoscale(**autoscale)
        if isinstance(aws_attributes, dict):
            aws_attributes = ClusterAwsAttributes(**aws_attributes)
        if isinstance(azure_attributes, dict):
            azure_attributes = ClusterAzureAttributes(**azure_attributes)
        if isinstance(cluster_log_conf, dict):
            cluster_log_conf = ClusterClusterLogConf(**cluster_log_conf)
        if isinstance(docker_image, dict):
            docker_image = ClusterDockerImage(**docker_image)
        if isinstance(gcp_attributes, dict):
            gcp_attributes = ClusterGcpAttributes(**gcp_attributes)
        if isinstance(timeouts, dict):
            timeouts = ClusterTimeouts(**timeouts)
        if isinstance(workload_type, dict):
            workload_type = ClusterWorkloadType(**workload_type)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14d046f126561eb6a7b17010f64421803233432f70dc54f0884903b8f749b430)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument spark_version", value=spark_version, expected_type=type_hints["spark_version"])
            check_type(argname="argument apply_policy_default_values", value=apply_policy_default_values, expected_type=type_hints["apply_policy_default_values"])
            check_type(argname="argument autoscale", value=autoscale, expected_type=type_hints["autoscale"])
            check_type(argname="argument autotermination_minutes", value=autotermination_minutes, expected_type=type_hints["autotermination_minutes"])
            check_type(argname="argument aws_attributes", value=aws_attributes, expected_type=type_hints["aws_attributes"])
            check_type(argname="argument azure_attributes", value=azure_attributes, expected_type=type_hints["azure_attributes"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument cluster_log_conf", value=cluster_log_conf, expected_type=type_hints["cluster_log_conf"])
            check_type(argname="argument cluster_mount_info", value=cluster_mount_info, expected_type=type_hints["cluster_mount_info"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument custom_tags", value=custom_tags, expected_type=type_hints["custom_tags"])
            check_type(argname="argument data_security_mode", value=data_security_mode, expected_type=type_hints["data_security_mode"])
            check_type(argname="argument docker_image", value=docker_image, expected_type=type_hints["docker_image"])
            check_type(argname="argument driver_instance_pool_id", value=driver_instance_pool_id, expected_type=type_hints["driver_instance_pool_id"])
            check_type(argname="argument driver_node_type_id", value=driver_node_type_id, expected_type=type_hints["driver_node_type_id"])
            check_type(argname="argument enable_elastic_disk", value=enable_elastic_disk, expected_type=type_hints["enable_elastic_disk"])
            check_type(argname="argument enable_local_disk_encryption", value=enable_local_disk_encryption, expected_type=type_hints["enable_local_disk_encryption"])
            check_type(argname="argument gcp_attributes", value=gcp_attributes, expected_type=type_hints["gcp_attributes"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument idempotency_token", value=idempotency_token, expected_type=type_hints["idempotency_token"])
            check_type(argname="argument init_scripts", value=init_scripts, expected_type=type_hints["init_scripts"])
            check_type(argname="argument instance_pool_id", value=instance_pool_id, expected_type=type_hints["instance_pool_id"])
            check_type(argname="argument is_pinned", value=is_pinned, expected_type=type_hints["is_pinned"])
            check_type(argname="argument library", value=library, expected_type=type_hints["library"])
            check_type(argname="argument node_type_id", value=node_type_id, expected_type=type_hints["node_type_id"])
            check_type(argname="argument num_workers", value=num_workers, expected_type=type_hints["num_workers"])
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
            check_type(argname="argument runtime_engine", value=runtime_engine, expected_type=type_hints["runtime_engine"])
            check_type(argname="argument single_user_name", value=single_user_name, expected_type=type_hints["single_user_name"])
            check_type(argname="argument spark_conf", value=spark_conf, expected_type=type_hints["spark_conf"])
            check_type(argname="argument spark_env_vars", value=spark_env_vars, expected_type=type_hints["spark_env_vars"])
            check_type(argname="argument ssh_public_keys", value=ssh_public_keys, expected_type=type_hints["ssh_public_keys"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument workload_type", value=workload_type, expected_type=type_hints["workload_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "spark_version": spark_version,
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
        if apply_policy_default_values is not None:
            self._values["apply_policy_default_values"] = apply_policy_default_values
        if autoscale is not None:
            self._values["autoscale"] = autoscale
        if autotermination_minutes is not None:
            self._values["autotermination_minutes"] = autotermination_minutes
        if aws_attributes is not None:
            self._values["aws_attributes"] = aws_attributes
        if azure_attributes is not None:
            self._values["azure_attributes"] = azure_attributes
        if cluster_id is not None:
            self._values["cluster_id"] = cluster_id
        if cluster_log_conf is not None:
            self._values["cluster_log_conf"] = cluster_log_conf
        if cluster_mount_info is not None:
            self._values["cluster_mount_info"] = cluster_mount_info
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if custom_tags is not None:
            self._values["custom_tags"] = custom_tags
        if data_security_mode is not None:
            self._values["data_security_mode"] = data_security_mode
        if docker_image is not None:
            self._values["docker_image"] = docker_image
        if driver_instance_pool_id is not None:
            self._values["driver_instance_pool_id"] = driver_instance_pool_id
        if driver_node_type_id is not None:
            self._values["driver_node_type_id"] = driver_node_type_id
        if enable_elastic_disk is not None:
            self._values["enable_elastic_disk"] = enable_elastic_disk
        if enable_local_disk_encryption is not None:
            self._values["enable_local_disk_encryption"] = enable_local_disk_encryption
        if gcp_attributes is not None:
            self._values["gcp_attributes"] = gcp_attributes
        if id is not None:
            self._values["id"] = id
        if idempotency_token is not None:
            self._values["idempotency_token"] = idempotency_token
        if init_scripts is not None:
            self._values["init_scripts"] = init_scripts
        if instance_pool_id is not None:
            self._values["instance_pool_id"] = instance_pool_id
        if is_pinned is not None:
            self._values["is_pinned"] = is_pinned
        if library is not None:
            self._values["library"] = library
        if node_type_id is not None:
            self._values["node_type_id"] = node_type_id
        if num_workers is not None:
            self._values["num_workers"] = num_workers
        if policy_id is not None:
            self._values["policy_id"] = policy_id
        if runtime_engine is not None:
            self._values["runtime_engine"] = runtime_engine
        if single_user_name is not None:
            self._values["single_user_name"] = single_user_name
        if spark_conf is not None:
            self._values["spark_conf"] = spark_conf
        if spark_env_vars is not None:
            self._values["spark_env_vars"] = spark_env_vars
        if ssh_public_keys is not None:
            self._values["ssh_public_keys"] = ssh_public_keys
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if workload_type is not None:
            self._values["workload_type"] = workload_type

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
    def spark_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_version Cluster#spark_version}.'''
        result = self._values.get("spark_version")
        assert result is not None, "Required property 'spark_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def apply_policy_default_values(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#apply_policy_default_values Cluster#apply_policy_default_values}.'''
        result = self._values.get("apply_policy_default_values")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def autoscale(self) -> typing.Optional[ClusterAutoscale]:
        '''autoscale block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#autoscale Cluster#autoscale}
        '''
        result = self._values.get("autoscale")
        return typing.cast(typing.Optional[ClusterAutoscale], result)

    @builtins.property
    def autotermination_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#autotermination_minutes Cluster#autotermination_minutes}.'''
        result = self._values.get("autotermination_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def aws_attributes(self) -> typing.Optional[ClusterAwsAttributes]:
        '''aws_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#aws_attributes Cluster#aws_attributes}
        '''
        result = self._values.get("aws_attributes")
        return typing.cast(typing.Optional[ClusterAwsAttributes], result)

    @builtins.property
    def azure_attributes(self) -> typing.Optional[ClusterAzureAttributes]:
        '''azure_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#azure_attributes Cluster#azure_attributes}
        '''
        result = self._values.get("azure_attributes")
        return typing.cast(typing.Optional[ClusterAzureAttributes], result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_id Cluster#cluster_id}.'''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_log_conf(self) -> typing.Optional[ClusterClusterLogConf]:
        '''cluster_log_conf block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_log_conf Cluster#cluster_log_conf}
        '''
        result = self._values.get("cluster_log_conf")
        return typing.cast(typing.Optional[ClusterClusterLogConf], result)

    @builtins.property
    def cluster_mount_info(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterClusterMountInfo]]]:
        '''cluster_mount_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_mount_info Cluster#cluster_mount_info}
        '''
        result = self._values.get("cluster_mount_info")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterClusterMountInfo]]], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cluster_name Cluster#cluster_name}.'''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#custom_tags Cluster#custom_tags}.'''
        result = self._values.get("custom_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def data_security_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#data_security_mode Cluster#data_security_mode}.'''
        result = self._values.get("data_security_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_image(self) -> typing.Optional["ClusterDockerImage"]:
        '''docker_image block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#docker_image Cluster#docker_image}
        '''
        result = self._values.get("docker_image")
        return typing.cast(typing.Optional["ClusterDockerImage"], result)

    @builtins.property
    def driver_instance_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#driver_instance_pool_id Cluster#driver_instance_pool_id}.'''
        result = self._values.get("driver_instance_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def driver_node_type_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#driver_node_type_id Cluster#driver_node_type_id}.'''
        result = self._values.get("driver_node_type_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_elastic_disk(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_elastic_disk Cluster#enable_elastic_disk}.'''
        result = self._values.get("enable_elastic_disk")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_local_disk_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_local_disk_encryption Cluster#enable_local_disk_encryption}.'''
        result = self._values.get("enable_local_disk_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def gcp_attributes(self) -> typing.Optional["ClusterGcpAttributes"]:
        '''gcp_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#gcp_attributes Cluster#gcp_attributes}
        '''
        result = self._values.get("gcp_attributes")
        return typing.cast(typing.Optional["ClusterGcpAttributes"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#id Cluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idempotency_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#idempotency_token Cluster#idempotency_token}.'''
        result = self._values.get("idempotency_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def init_scripts(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterInitScripts"]]]:
        '''init_scripts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#init_scripts Cluster#init_scripts}
        '''
        result = self._values.get("init_scripts")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterInitScripts"]]], result)

    @builtins.property
    def instance_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#instance_pool_id Cluster#instance_pool_id}.'''
        result = self._values.get("instance_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_pinned(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#is_pinned Cluster#is_pinned}.'''
        result = self._values.get("is_pinned")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def library(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterLibrary"]]]:
        '''library block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#library Cluster#library}
        '''
        result = self._values.get("library")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ClusterLibrary"]]], result)

    @builtins.property
    def node_type_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#node_type_id Cluster#node_type_id}.'''
        result = self._values.get("node_type_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#num_workers Cluster#num_workers}.'''
        result = self._values.get("num_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def policy_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#policy_id Cluster#policy_id}.'''
        result = self._values.get("policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime_engine(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#runtime_engine Cluster#runtime_engine}.'''
        result = self._values.get("runtime_engine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_user_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#single_user_name Cluster#single_user_name}.'''
        result = self._values.get("single_user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spark_conf(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_conf Cluster#spark_conf}.'''
        result = self._values.get("spark_conf")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def spark_env_vars(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#spark_env_vars Cluster#spark_env_vars}.'''
        result = self._values.get("spark_env_vars")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def ssh_public_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#ssh_public_keys Cluster#ssh_public_keys}.'''
        result = self._values.get("ssh_public_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#timeouts Cluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ClusterTimeouts"], result)

    @builtins.property
    def workload_type(self) -> typing.Optional["ClusterWorkloadType"]:
        '''workload_type block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#workload_type Cluster#workload_type}
        '''
        result = self._values.get("workload_type")
        return typing.cast(typing.Optional["ClusterWorkloadType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterDockerImage",
    jsii_struct_bases=[],
    name_mapping={"url": "url", "basic_auth": "basicAuth"},
)
class ClusterDockerImage:
    def __init__(
        self,
        *,
        url: builtins.str,
        basic_auth: typing.Optional[typing.Union["ClusterDockerImageBasicAuth", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#url Cluster#url}.
        :param basic_auth: basic_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#basic_auth Cluster#basic_auth}
        '''
        if isinstance(basic_auth, dict):
            basic_auth = ClusterDockerImageBasicAuth(**basic_auth)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37926b7c231bdb77c8e117e6b2de5f17124539a2bcdf0a831fb0267bdb3d75e3)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument basic_auth", value=basic_auth, expected_type=type_hints["basic_auth"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if basic_auth is not None:
            self._values["basic_auth"] = basic_auth

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#url Cluster#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def basic_auth(self) -> typing.Optional["ClusterDockerImageBasicAuth"]:
        '''basic_auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#basic_auth Cluster#basic_auth}
        '''
        result = self._values.get("basic_auth")
        return typing.cast(typing.Optional["ClusterDockerImageBasicAuth"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterDockerImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterDockerImageBasicAuth",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class ClusterDockerImageBasicAuth:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#password Cluster#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#username Cluster#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b422412080207b5e3eb95df190661862cb3f274293c32c50feda49d52d8438a)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#password Cluster#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#username Cluster#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterDockerImageBasicAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterDockerImageBasicAuthOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterDockerImageBasicAuthOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a758ae3ef2547ff793de7cab8e09b8f3a0b3b7001b7d2a360d76be5827d95c8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__05ce539b347a5f8c7f53ceb91ae0446c4881411068d8ba1d9bfe43b44ddd633a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f6df8fb344db3c1a346bb498c0b2a6026785dd69dbe333f6985b4e59d969b88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterDockerImageBasicAuth]:
        return typing.cast(typing.Optional[ClusterDockerImageBasicAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ClusterDockerImageBasicAuth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12cea82b838986e9f7796c87b441bdc1c11c046f42d5825c2d0dc59a10daa819)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterDockerImageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterDockerImageOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9293205bc15dc0229b5d52f743ae267259a1000216023d18c6d4f271efdb2dc8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBasicAuth")
    def put_basic_auth(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#password Cluster#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#username Cluster#username}.
        '''
        value = ClusterDockerImageBasicAuth(password=password, username=username)

        return typing.cast(None, jsii.invoke(self, "putBasicAuth", [value]))

    @jsii.member(jsii_name="resetBasicAuth")
    def reset_basic_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuth", []))

    @builtins.property
    @jsii.member(jsii_name="basicAuth")
    def basic_auth(self) -> ClusterDockerImageBasicAuthOutputReference:
        return typing.cast(ClusterDockerImageBasicAuthOutputReference, jsii.get(self, "basicAuth"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthInput")
    def basic_auth_input(self) -> typing.Optional[ClusterDockerImageBasicAuth]:
        return typing.cast(typing.Optional[ClusterDockerImageBasicAuth], jsii.get(self, "basicAuthInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__20d9fb12bfbfeedb4e6d72e8492bebd7b17409b1fb529da3e2ef0a883b97e150)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterDockerImage]:
        return typing.cast(typing.Optional[ClusterDockerImage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterDockerImage]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__937e6a79496d3ca1b320ea195251b23da6d62ca2f0acfb8dc7768ce5b9c5e704)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterGcpAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "boot_disk_size": "bootDiskSize",
        "google_service_account": "googleServiceAccount",
        "use_preemptible_executors": "usePreemptibleExecutors",
        "zone_id": "zoneId",
    },
)
class ClusterGcpAttributes:
    def __init__(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        boot_disk_size: typing.Optional[jsii.Number] = None,
        google_service_account: typing.Optional[builtins.str] = None,
        use_preemptible_executors: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.
        :param boot_disk_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#boot_disk_size Cluster#boot_disk_size}.
        :param google_service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#google_service_account Cluster#google_service_account}.
        :param use_preemptible_executors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#use_preemptible_executors Cluster#use_preemptible_executors}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#zone_id Cluster#zone_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be63bfc07bad962fb9da45b72c617e4909affe17cf24fb6cb3077529ca56f0eb)
            check_type(argname="argument availability", value=availability, expected_type=type_hints["availability"])
            check_type(argname="argument boot_disk_size", value=boot_disk_size, expected_type=type_hints["boot_disk_size"])
            check_type(argname="argument google_service_account", value=google_service_account, expected_type=type_hints["google_service_account"])
            check_type(argname="argument use_preemptible_executors", value=use_preemptible_executors, expected_type=type_hints["use_preemptible_executors"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability is not None:
            self._values["availability"] = availability
        if boot_disk_size is not None:
            self._values["boot_disk_size"] = boot_disk_size
        if google_service_account is not None:
            self._values["google_service_account"] = google_service_account
        if use_preemptible_executors is not None:
            self._values["use_preemptible_executors"] = use_preemptible_executors
        if zone_id is not None:
            self._values["zone_id"] = zone_id

    @builtins.property
    def availability(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#availability Cluster#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def boot_disk_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#boot_disk_size Cluster#boot_disk_size}.'''
        result = self._values.get("boot_disk_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def google_service_account(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#google_service_account Cluster#google_service_account}.'''
        result = self._values.get("google_service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_preemptible_executors(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#use_preemptible_executors Cluster#use_preemptible_executors}.'''
        result = self._values.get("use_preemptible_executors")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#zone_id Cluster#zone_id}.'''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterGcpAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterGcpAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterGcpAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7bbb16a6b9dc82a0a9fe5cf674d02acdcb671b0c4e0232ab6dc4cb290566ff20)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAvailability")
    def reset_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailability", []))

    @jsii.member(jsii_name="resetBootDiskSize")
    def reset_boot_disk_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiskSize", []))

    @jsii.member(jsii_name="resetGoogleServiceAccount")
    def reset_google_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleServiceAccount", []))

    @jsii.member(jsii_name="resetUsePreemptibleExecutors")
    def reset_use_preemptible_executors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsePreemptibleExecutors", []))

    @jsii.member(jsii_name="resetZoneId")
    def reset_zone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneId", []))

    @builtins.property
    @jsii.member(jsii_name="availabilityInput")
    def availability_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiskSizeInput")
    def boot_disk_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bootDiskSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="googleServiceAccountInput")
    def google_service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleServiceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="usePreemptibleExecutorsInput")
    def use_preemptible_executors_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "usePreemptibleExecutorsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__99c79b7e530aa0db44e0c4fabe9f23baa357250590f4318e0b7b34f5ddf66860)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="bootDiskSize")
    def boot_disk_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bootDiskSize"))

    @boot_disk_size.setter
    def boot_disk_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94241de581cf0c729b5cb2735afd6119ffb9806f5dbfb1ab789c0a484224f17a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDiskSize", value)

    @builtins.property
    @jsii.member(jsii_name="googleServiceAccount")
    def google_service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "googleServiceAccount"))

    @google_service_account.setter
    def google_service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__558da5a6fcaed9b5505124416a4ff869e5704feeca31eb38467ce21d2a6095c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "googleServiceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="usePreemptibleExecutors")
    def use_preemptible_executors(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "usePreemptibleExecutors"))

    @use_preemptible_executors.setter
    def use_preemptible_executors(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d83c028737969885dd577e4f3c6b2caf4f3be0e8809d5ac3fe7eee0a1dadb253)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usePreemptibleExecutors", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c36ca7d6dd70c73dbf0f14607acd1cbfb51192f2d2c8d6b38ff9b8e9851b642e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterGcpAttributes]:
        return typing.cast(typing.Optional[ClusterGcpAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterGcpAttributes]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b012f7736e21e4ddd96a7ef109a4a57e677d3b76c1afe7865d0f7198c9393f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterInitScripts",
    jsii_struct_bases=[],
    name_mapping={
        "abfss": "abfss",
        "dbfs": "dbfs",
        "file": "file",
        "gcs": "gcs",
        "s3": "s3",
    },
)
class ClusterInitScripts:
    def __init__(
        self,
        *,
        abfss: typing.Optional[typing.Union["ClusterInitScriptsAbfss", typing.Dict[builtins.str, typing.Any]]] = None,
        dbfs: typing.Optional[typing.Union["ClusterInitScriptsDbfs", typing.Dict[builtins.str, typing.Any]]] = None,
        file: typing.Optional[typing.Union["ClusterInitScriptsFile", typing.Dict[builtins.str, typing.Any]]] = None,
        gcs: typing.Optional[typing.Union["ClusterInitScriptsGcs", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["ClusterInitScriptsS3", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param abfss: abfss block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#abfss Cluster#abfss}
        :param dbfs: dbfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#dbfs Cluster#dbfs}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#file Cluster#file}
        :param gcs: gcs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#gcs Cluster#gcs}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#s3 Cluster#s3}
        '''
        if isinstance(abfss, dict):
            abfss = ClusterInitScriptsAbfss(**abfss)
        if isinstance(dbfs, dict):
            dbfs = ClusterInitScriptsDbfs(**dbfs)
        if isinstance(file, dict):
            file = ClusterInitScriptsFile(**file)
        if isinstance(gcs, dict):
            gcs = ClusterInitScriptsGcs(**gcs)
        if isinstance(s3, dict):
            s3 = ClusterInitScriptsS3(**s3)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__494fb6b11b41dea3e2cd7c053299b63ae19f37fd4ed4b7c4a14df6b5b2946868)
            check_type(argname="argument abfss", value=abfss, expected_type=type_hints["abfss"])
            check_type(argname="argument dbfs", value=dbfs, expected_type=type_hints["dbfs"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument gcs", value=gcs, expected_type=type_hints["gcs"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if abfss is not None:
            self._values["abfss"] = abfss
        if dbfs is not None:
            self._values["dbfs"] = dbfs
        if file is not None:
            self._values["file"] = file
        if gcs is not None:
            self._values["gcs"] = gcs
        if s3 is not None:
            self._values["s3"] = s3

    @builtins.property
    def abfss(self) -> typing.Optional["ClusterInitScriptsAbfss"]:
        '''abfss block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#abfss Cluster#abfss}
        '''
        result = self._values.get("abfss")
        return typing.cast(typing.Optional["ClusterInitScriptsAbfss"], result)

    @builtins.property
    def dbfs(self) -> typing.Optional["ClusterInitScriptsDbfs"]:
        '''dbfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#dbfs Cluster#dbfs}
        '''
        result = self._values.get("dbfs")
        return typing.cast(typing.Optional["ClusterInitScriptsDbfs"], result)

    @builtins.property
    def file(self) -> typing.Optional["ClusterInitScriptsFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#file Cluster#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["ClusterInitScriptsFile"], result)

    @builtins.property
    def gcs(self) -> typing.Optional["ClusterInitScriptsGcs"]:
        '''gcs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#gcs Cluster#gcs}
        '''
        result = self._values.get("gcs")
        return typing.cast(typing.Optional["ClusterInitScriptsGcs"], result)

    @builtins.property
    def s3(self) -> typing.Optional["ClusterInitScriptsS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#s3 Cluster#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["ClusterInitScriptsS3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterInitScripts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterInitScriptsAbfss",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class ClusterInitScriptsAbfss:
    def __init__(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cab747a6f7cc796d9d369ae4f336ab5b3980c5c5c41e3e3562563859e8fc0f99)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.'''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterInitScriptsAbfss(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterInitScriptsAbfssOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterInitScriptsAbfssOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c86fa149004e6c4dbc48e35a84a05a39ffebf5bcdd8a58f83ee7f52271620802)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDestination")
    def reset_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestination", []))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a9f6396ecc27d204e343ea63d1777c324922913bc93a1f58307cbc924736a3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterInitScriptsAbfss]:
        return typing.cast(typing.Optional[ClusterInitScriptsAbfss], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterInitScriptsAbfss]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc10b53d4d2d943e15aa455920c16cc728fcf8522e335bd359ab290838d72c9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterInitScriptsDbfs",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class ClusterInitScriptsDbfs:
    def __init__(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3ad4dcb860716faf8eba38f16409d789b114e1e1a0f2778d3d7ed34a22805d4)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterInitScriptsDbfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterInitScriptsDbfsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterInitScriptsDbfsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__897215de756898935e3b8d81c565a196cebcdfccf75e3b7ac3c9e5d76a0b97ba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e757e1d8af34d081b7fccc2452fec07e42756d46cfef509ae2a8b9f2357c60b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterInitScriptsDbfs]:
        return typing.cast(typing.Optional[ClusterInitScriptsDbfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterInitScriptsDbfs]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a2cbd1c01acb74113c9bcc7c7beba608e802337b64196ce5960dc654356547e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterInitScriptsFile",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class ClusterInitScriptsFile:
    def __init__(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a22b3eb9e2745fcbbd27569b7aec04de12fb91d63b354ba95311f37ca95e75d2)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.'''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterInitScriptsFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterInitScriptsFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterInitScriptsFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__01afb610dd0ec5b8159a17c28de91e14ad5320181c0adf08f0fd038047dc1b0b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDestination")
    def reset_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestination", []))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f0d0107ac197d93211a7e57efcd3a4ebe873fe2838700776b4ee39e736e851a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterInitScriptsFile]:
        return typing.cast(typing.Optional[ClusterInitScriptsFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterInitScriptsFile]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9e673057ed8053135b9e4051f628329599f69aa2e1720b8667d6205b7f16dc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterInitScriptsGcs",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class ClusterInitScriptsGcs:
    def __init__(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__408189c618246c045002f2adca0ab2867c9ed3fa870106b072b5855fc34847d0)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.'''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterInitScriptsGcs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterInitScriptsGcsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterInitScriptsGcsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d4bbf8a86a14323eff2056642ec87137320e8262f92307e49d2904490b959ccb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDestination")
    def reset_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestination", []))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b82862eaa7e1117314e2db0833e6be5553984515347c9354d46ef18ba2ee38f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterInitScriptsGcs]:
        return typing.cast(typing.Optional[ClusterInitScriptsGcs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterInitScriptsGcs]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff32fd09cb2aceaab8772822fa7f10fb10fb2d4b505a7079a6f502c036260316)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterInitScriptsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterInitScriptsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__42283c361e63a817b9f942d6874dc7443408878905638d3d08eee2aea93c1fb5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ClusterInitScriptsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__959f60f88ac906727641cb526b58dbc99a9ccb1dc7f71b8460211b05a6a50b0e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ClusterInitScriptsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38a69e09aa8cce292b857a095c90c287a495a689a06eefbddf53acf288c26002)
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
            type_hints = typing.get_type_hints(_typecheckingstub__022fec918f2e97f5f306e595271f10833b2412a433e9b6251f5c0151954cde95)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eadd03891ac4e73bd0abcd5ac9e157fc99fa7db206ddf986b53e5aaea7070c4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterInitScripts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterInitScripts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterInitScripts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a39862aff9c53c1f61d26b0a55b76ef5a99d139142f0560090d0c4705b15b1ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterInitScriptsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterInitScriptsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d8f162a29d01e2b6979490eda8cae41bcd46b45001c210d11fb591893a6a189)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAbfss")
    def put_abfss(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        value = ClusterInitScriptsAbfss(destination=destination)

        return typing.cast(None, jsii.invoke(self, "putAbfss", [value]))

    @jsii.member(jsii_name="putDbfs")
    def put_dbfs(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        value = ClusterInitScriptsDbfs(destination=destination)

        return typing.cast(None, jsii.invoke(self, "putDbfs", [value]))

    @jsii.member(jsii_name="putFile")
    def put_file(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        value = ClusterInitScriptsFile(destination=destination)

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putGcs")
    def put_gcs(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        '''
        value = ClusterInitScriptsGcs(destination=destination)

        return typing.cast(None, jsii.invoke(self, "putGcs", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        destination: builtins.str,
        canned_acl: typing.Optional[builtins.str] = None,
        enable_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encryption_type: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#canned_acl Cluster#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_encryption Cluster#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#encryption_type Cluster#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#endpoint Cluster#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#kms_key Cluster#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#region Cluster#region}.
        '''
        value = ClusterInitScriptsS3(
            destination=destination,
            canned_acl=canned_acl,
            enable_encryption=enable_encryption,
            encryption_type=encryption_type,
            endpoint=endpoint,
            kms_key=kms_key,
            region=region,
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="resetAbfss")
    def reset_abfss(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAbfss", []))

    @jsii.member(jsii_name="resetDbfs")
    def reset_dbfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbfs", []))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetGcs")
    def reset_gcs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcs", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @builtins.property
    @jsii.member(jsii_name="abfss")
    def abfss(self) -> ClusterInitScriptsAbfssOutputReference:
        return typing.cast(ClusterInitScriptsAbfssOutputReference, jsii.get(self, "abfss"))

    @builtins.property
    @jsii.member(jsii_name="dbfs")
    def dbfs(self) -> ClusterInitScriptsDbfsOutputReference:
        return typing.cast(ClusterInitScriptsDbfsOutputReference, jsii.get(self, "dbfs"))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> ClusterInitScriptsFileOutputReference:
        return typing.cast(ClusterInitScriptsFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="gcs")
    def gcs(self) -> ClusterInitScriptsGcsOutputReference:
        return typing.cast(ClusterInitScriptsGcsOutputReference, jsii.get(self, "gcs"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "ClusterInitScriptsS3OutputReference":
        return typing.cast("ClusterInitScriptsS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="abfssInput")
    def abfss_input(self) -> typing.Optional[ClusterInitScriptsAbfss]:
        return typing.cast(typing.Optional[ClusterInitScriptsAbfss], jsii.get(self, "abfssInput"))

    @builtins.property
    @jsii.member(jsii_name="dbfsInput")
    def dbfs_input(self) -> typing.Optional[ClusterInitScriptsDbfs]:
        return typing.cast(typing.Optional[ClusterInitScriptsDbfs], jsii.get(self, "dbfsInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(self) -> typing.Optional[ClusterInitScriptsFile]:
        return typing.cast(typing.Optional[ClusterInitScriptsFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="gcsInput")
    def gcs_input(self) -> typing.Optional[ClusterInitScriptsGcs]:
        return typing.cast(typing.Optional[ClusterInitScriptsGcs], jsii.get(self, "gcsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(self) -> typing.Optional["ClusterInitScriptsS3"]:
        return typing.cast(typing.Optional["ClusterInitScriptsS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ClusterInitScripts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ClusterInitScripts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ClusterInitScripts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__febad621ee9c7866a0bbe4a924b357ceee67e0f507e1d22f6d771d8797ebe48a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterInitScriptsS3",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "canned_acl": "cannedAcl",
        "enable_encryption": "enableEncryption",
        "encryption_type": "encryptionType",
        "endpoint": "endpoint",
        "kms_key": "kmsKey",
        "region": "region",
    },
)
class ClusterInitScriptsS3:
    def __init__(
        self,
        *,
        destination: builtins.str,
        canned_acl: typing.Optional[builtins.str] = None,
        enable_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        encryption_type: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#canned_acl Cluster#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_encryption Cluster#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#encryption_type Cluster#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#endpoint Cluster#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#kms_key Cluster#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#region Cluster#region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b0bd2dc4ac819928b8c0e1d334484bd488b5b8801652408c8242afd918acfbc)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument canned_acl", value=canned_acl, expected_type=type_hints["canned_acl"])
            check_type(argname="argument enable_encryption", value=enable_encryption, expected_type=type_hints["enable_encryption"])
            check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
        }
        if canned_acl is not None:
            self._values["canned_acl"] = canned_acl
        if enable_encryption is not None:
            self._values["enable_encryption"] = enable_encryption
        if encryption_type is not None:
            self._values["encryption_type"] = encryption_type
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#destination Cluster#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def canned_acl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#canned_acl Cluster#canned_acl}.'''
        result = self._values.get("canned_acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#enable_encryption Cluster#enable_encryption}.'''
        result = self._values.get("enable_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encryption_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#encryption_type Cluster#encryption_type}.'''
        result = self._values.get("encryption_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#endpoint Cluster#endpoint}.'''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#kms_key Cluster#kms_key}.'''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#region Cluster#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterInitScriptsS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterInitScriptsS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterInitScriptsS3OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f0c746ea776606e726f333910845e49bcc05a924283bd07f6e3f3dfa4e3402a7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCannedAcl")
    def reset_canned_acl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCannedAcl", []))

    @jsii.member(jsii_name="resetEnableEncryption")
    def reset_enable_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableEncryption", []))

    @jsii.member(jsii_name="resetEncryptionType")
    def reset_encryption_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionType", []))

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @jsii.member(jsii_name="resetKmsKey")
    def reset_kms_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKey", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @builtins.property
    @jsii.member(jsii_name="cannedAclInput")
    def canned_acl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cannedAclInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="enableEncryptionInput")
    def enable_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionTypeInput")
    def encryption_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyInput")
    def kms_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="cannedAcl")
    def canned_acl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cannedAcl"))

    @canned_acl.setter
    def canned_acl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__018577fbccec2824ea8fc0289d8b6ee607e6b7c6e6bf35cb5d663fb94bf91e39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cannedAcl", value)

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec6b545aae826c8b56eccc90b7dad5eeae38471607e2dba1839c536db9fba4f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="enableEncryption")
    def enable_encryption(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableEncryption"))

    @enable_encryption.setter
    def enable_encryption(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88d3bfe09c8b3ac3c50b07dc34d338705dff879bce86b96daf2cc12fb7f49883)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionType")
    def encryption_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionType"))

    @encryption_type.setter
    def encryption_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56649e2cbcc783055f4f141702d80dc36d7720060d28545007106adb39ac43e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72c487ae09268491a02819bc3cdbf71a08e249f18ea92b540d43a7c87eadc701)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1c1ea54d2dcf3f547b3e1627fe285bf683a71530017452f76fcaaad9de649ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18ce5a6694c984e2c22d71ffe2df7db528d0bc0bde93e52eb43f0610e20a2fd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterInitScriptsS3]:
        return typing.cast(typing.Optional[ClusterInitScriptsS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterInitScriptsS3]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c5aaefe34b9075b98486d5df164281760dca96050828ffc2051bf8b2ec4e5d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterLibrary",
    jsii_struct_bases=[],
    name_mapping={
        "cran": "cran",
        "egg": "egg",
        "jar": "jar",
        "maven": "maven",
        "pypi": "pypi",
        "whl": "whl",
    },
)
class ClusterLibrary:
    def __init__(
        self,
        *,
        cran: typing.Optional[typing.Union["ClusterLibraryCran", typing.Dict[builtins.str, typing.Any]]] = None,
        egg: typing.Optional[builtins.str] = None,
        jar: typing.Optional[builtins.str] = None,
        maven: typing.Optional[typing.Union["ClusterLibraryMaven", typing.Dict[builtins.str, typing.Any]]] = None,
        pypi: typing.Optional[typing.Union["ClusterLibraryPypi", typing.Dict[builtins.str, typing.Any]]] = None,
        whl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cran: cran block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cran Cluster#cran}
        :param egg: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#egg Cluster#egg}.
        :param jar: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#jar Cluster#jar}.
        :param maven: maven block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#maven Cluster#maven}
        :param pypi: pypi block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#pypi Cluster#pypi}
        :param whl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#whl Cluster#whl}.
        '''
        if isinstance(cran, dict):
            cran = ClusterLibraryCran(**cran)
        if isinstance(maven, dict):
            maven = ClusterLibraryMaven(**maven)
        if isinstance(pypi, dict):
            pypi = ClusterLibraryPypi(**pypi)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__becf6b973435c78b2067ceaae644277db171b285d1b1db9a025ea96505bcaf36)
            check_type(argname="argument cran", value=cran, expected_type=type_hints["cran"])
            check_type(argname="argument egg", value=egg, expected_type=type_hints["egg"])
            check_type(argname="argument jar", value=jar, expected_type=type_hints["jar"])
            check_type(argname="argument maven", value=maven, expected_type=type_hints["maven"])
            check_type(argname="argument pypi", value=pypi, expected_type=type_hints["pypi"])
            check_type(argname="argument whl", value=whl, expected_type=type_hints["whl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cran is not None:
            self._values["cran"] = cran
        if egg is not None:
            self._values["egg"] = egg
        if jar is not None:
            self._values["jar"] = jar
        if maven is not None:
            self._values["maven"] = maven
        if pypi is not None:
            self._values["pypi"] = pypi
        if whl is not None:
            self._values["whl"] = whl

    @builtins.property
    def cran(self) -> typing.Optional["ClusterLibraryCran"]:
        '''cran block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#cran Cluster#cran}
        '''
        result = self._values.get("cran")
        return typing.cast(typing.Optional["ClusterLibraryCran"], result)

    @builtins.property
    def egg(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#egg Cluster#egg}.'''
        result = self._values.get("egg")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jar(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#jar Cluster#jar}.'''
        result = self._values.get("jar")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maven(self) -> typing.Optional["ClusterLibraryMaven"]:
        '''maven block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#maven Cluster#maven}
        '''
        result = self._values.get("maven")
        return typing.cast(typing.Optional["ClusterLibraryMaven"], result)

    @builtins.property
    def pypi(self) -> typing.Optional["ClusterLibraryPypi"]:
        '''pypi block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#pypi Cluster#pypi}
        '''
        result = self._values.get("pypi")
        return typing.cast(typing.Optional["ClusterLibraryPypi"], result)

    @builtins.property
    def whl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#whl Cluster#whl}.'''
        result = self._values.get("whl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterLibrary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterLibraryCran",
    jsii_struct_bases=[],
    name_mapping={"package": "package", "repo": "repo"},
)
class ClusterLibraryCran:
    def __init__(
        self,
        *,
        package: builtins.str,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param package: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#package Cluster#package}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__485358356798bc354f00dc8dd2d323f01183fa98ea22b35642ddd753fbe478fd)
            check_type(argname="argument package", value=package, expected_type=type_hints["package"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "package": package,
        }
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def package(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#package Cluster#package}.'''
        result = self._values.get("package")
        assert result is not None, "Required property 'package' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.'''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterLibraryCran(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterLibraryCranOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterLibraryCranOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e63eaa1ba046f6bfb93082b88fa0cd3db2950780b72c5998666b5c81983865e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRepo")
    def reset_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepo", []))

    @builtins.property
    @jsii.member(jsii_name="packageInput")
    def package_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "packageInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

    @builtins.property
    @jsii.member(jsii_name="package")
    def package(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "package"))

    @package.setter
    def package(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4416d2b77d322e82686d82a15681d3935800cbfabdd129d6c01cb9aeefef01be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "package", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__678e91f9004e6c48080f2cf3d941acfe2db8a19c117ce61c849edc291dc97055)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterLibraryCran]:
        return typing.cast(typing.Optional[ClusterLibraryCran], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterLibraryCran]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1001a4ae4c774cfd2c333457b1ef4672990e59fc32a96083ba233db6fe6e4c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterLibraryList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterLibraryList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ab3de513b29018fcc7c0651b74da99b8ead141cf97e4532b6fa2f04965d1ba10)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ClusterLibraryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4bc06c33382cab995aa74b62707132de9dd887640335bf7286bf874bae310e8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ClusterLibraryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7abc31bd2d1171c40f415c6bcdf7ea55f076d69b3a6bd7a5940f590f2b5bc1a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b5c57e9abfe463ad1d8c887e498288e398d767509840320fd60de7ac364ce70a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8bf17beb7446922d62bef521af65876430a1b5d2576d4d558af3fd3faf8a614f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterLibrary]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterLibrary]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterLibrary]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55a38bd275d3b152d6d58b6d775eb84b2771303f149266dc436c1b6660ee432e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterLibraryMaven",
    jsii_struct_bases=[],
    name_mapping={
        "coordinates": "coordinates",
        "exclusions": "exclusions",
        "repo": "repo",
    },
)
class ClusterLibraryMaven:
    def __init__(
        self,
        *,
        coordinates: builtins.str,
        exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param coordinates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#coordinates Cluster#coordinates}.
        :param exclusions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#exclusions Cluster#exclusions}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e0dc26666e722c084a2693f6a63f1d78fafa0e656ad037101e16837a4bf2c2a)
            check_type(argname="argument coordinates", value=coordinates, expected_type=type_hints["coordinates"])
            check_type(argname="argument exclusions", value=exclusions, expected_type=type_hints["exclusions"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "coordinates": coordinates,
        }
        if exclusions is not None:
            self._values["exclusions"] = exclusions
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def coordinates(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#coordinates Cluster#coordinates}.'''
        result = self._values.get("coordinates")
        assert result is not None, "Required property 'coordinates' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclusions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#exclusions Cluster#exclusions}.'''
        result = self._values.get("exclusions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.'''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterLibraryMaven(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterLibraryMavenOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterLibraryMavenOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c7731916d0580b75dffeaf50ae811d7aa814e411a721285788a57fbc83649da)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExclusions")
    def reset_exclusions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusions", []))

    @jsii.member(jsii_name="resetRepo")
    def reset_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepo", []))

    @builtins.property
    @jsii.member(jsii_name="coordinatesInput")
    def coordinates_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "coordinatesInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusionsInput")
    def exclusions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exclusionsInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

    @builtins.property
    @jsii.member(jsii_name="coordinates")
    def coordinates(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "coordinates"))

    @coordinates.setter
    def coordinates(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0f25dfb34842191b143d367131ea58edf560cbd8bdee512216a16db4e502e67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coordinates", value)

    @builtins.property
    @jsii.member(jsii_name="exclusions")
    def exclusions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclusions"))

    @exclusions.setter
    def exclusions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecb82508531a91ffdbda6838120fcbad6b92f3cd8017084bb852b79481b71f17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusions", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6c3f668836cc8c80804367e0224689d08406c60c77371032ab2147fab7184d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterLibraryMaven]:
        return typing.cast(typing.Optional[ClusterLibraryMaven], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterLibraryMaven]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3713f9c266d998800b2988b75e19e4b87a8bf8f5ef72d4ff0c270a2ec1f41c87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterLibraryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterLibraryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4beab7cde01790ec9a746485365ca663cb0895a7a06c1dcd2d8c83bfd688c51e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCran")
    def put_cran(
        self,
        *,
        package: builtins.str,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param package: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#package Cluster#package}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.
        '''
        value = ClusterLibraryCran(package=package, repo=repo)

        return typing.cast(None, jsii.invoke(self, "putCran", [value]))

    @jsii.member(jsii_name="putMaven")
    def put_maven(
        self,
        *,
        coordinates: builtins.str,
        exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param coordinates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#coordinates Cluster#coordinates}.
        :param exclusions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#exclusions Cluster#exclusions}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.
        '''
        value = ClusterLibraryMaven(
            coordinates=coordinates, exclusions=exclusions, repo=repo
        )

        return typing.cast(None, jsii.invoke(self, "putMaven", [value]))

    @jsii.member(jsii_name="putPypi")
    def put_pypi(
        self,
        *,
        package: builtins.str,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param package: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#package Cluster#package}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.
        '''
        value = ClusterLibraryPypi(package=package, repo=repo)

        return typing.cast(None, jsii.invoke(self, "putPypi", [value]))

    @jsii.member(jsii_name="resetCran")
    def reset_cran(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCran", []))

    @jsii.member(jsii_name="resetEgg")
    def reset_egg(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgg", []))

    @jsii.member(jsii_name="resetJar")
    def reset_jar(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJar", []))

    @jsii.member(jsii_name="resetMaven")
    def reset_maven(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaven", []))

    @jsii.member(jsii_name="resetPypi")
    def reset_pypi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPypi", []))

    @jsii.member(jsii_name="resetWhl")
    def reset_whl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhl", []))

    @builtins.property
    @jsii.member(jsii_name="cran")
    def cran(self) -> ClusterLibraryCranOutputReference:
        return typing.cast(ClusterLibraryCranOutputReference, jsii.get(self, "cran"))

    @builtins.property
    @jsii.member(jsii_name="maven")
    def maven(self) -> ClusterLibraryMavenOutputReference:
        return typing.cast(ClusterLibraryMavenOutputReference, jsii.get(self, "maven"))

    @builtins.property
    @jsii.member(jsii_name="pypi")
    def pypi(self) -> "ClusterLibraryPypiOutputReference":
        return typing.cast("ClusterLibraryPypiOutputReference", jsii.get(self, "pypi"))

    @builtins.property
    @jsii.member(jsii_name="cranInput")
    def cran_input(self) -> typing.Optional[ClusterLibraryCran]:
        return typing.cast(typing.Optional[ClusterLibraryCran], jsii.get(self, "cranInput"))

    @builtins.property
    @jsii.member(jsii_name="eggInput")
    def egg_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eggInput"))

    @builtins.property
    @jsii.member(jsii_name="jarInput")
    def jar_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jarInput"))

    @builtins.property
    @jsii.member(jsii_name="mavenInput")
    def maven_input(self) -> typing.Optional[ClusterLibraryMaven]:
        return typing.cast(typing.Optional[ClusterLibraryMaven], jsii.get(self, "mavenInput"))

    @builtins.property
    @jsii.member(jsii_name="pypiInput")
    def pypi_input(self) -> typing.Optional["ClusterLibraryPypi"]:
        return typing.cast(typing.Optional["ClusterLibraryPypi"], jsii.get(self, "pypiInput"))

    @builtins.property
    @jsii.member(jsii_name="whlInput")
    def whl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whlInput"))

    @builtins.property
    @jsii.member(jsii_name="egg")
    def egg(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "egg"))

    @egg.setter
    def egg(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__189fbfb48d3f1121e43b82c7f46947b64832812f2742f352aad05930555a1ffd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egg", value)

    @builtins.property
    @jsii.member(jsii_name="jar")
    def jar(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jar"))

    @jar.setter
    def jar(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__853e34a19557d83e1e15d46f23b5f77228280bb7821aaffd4d26b1e7e5b7bc34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jar", value)

    @builtins.property
    @jsii.member(jsii_name="whl")
    def whl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whl"))

    @whl.setter
    def whl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0b08d03aefba502de5880000ef07670994844522c14c2879dcfa7b2501ca9d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ClusterLibrary, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ClusterLibrary, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ClusterLibrary, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c693be5b40365e58756dec1a5f2b7805277bd07e4f14678a6aa3c2aca1f16e85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterLibraryPypi",
    jsii_struct_bases=[],
    name_mapping={"package": "package", "repo": "repo"},
)
class ClusterLibraryPypi:
    def __init__(
        self,
        *,
        package: builtins.str,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param package: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#package Cluster#package}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81f52f5b45ea0376ddf0bb49133aa7be89133811328a4529a0a45654cd7bc41d)
            check_type(argname="argument package", value=package, expected_type=type_hints["package"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "package": package,
        }
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def package(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#package Cluster#package}.'''
        result = self._values.get("package")
        assert result is not None, "Required property 'package' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#repo Cluster#repo}.'''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterLibraryPypi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterLibraryPypiOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterLibraryPypiOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7d3c46242a4458c69a237061ea7f9757d44cb8901df36580c8b535c04ae49052)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRepo")
    def reset_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepo", []))

    @builtins.property
    @jsii.member(jsii_name="packageInput")
    def package_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "packageInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

    @builtins.property
    @jsii.member(jsii_name="package")
    def package(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "package"))

    @package.setter
    def package(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2624d098297936eb087b409e52a669a9354e922d3db455b3b7cf82aacdb41140)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "package", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cbb38c25eeca993d809044fa5696656dbee58adb2cacc505f7eafcb2ca48c67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterLibraryPypi]:
        return typing.cast(typing.Optional[ClusterLibraryPypi], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterLibraryPypi]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1edede53ec44a55be5c3d4b2d1367bd6d89e7278f6739e28a84c49afb625b7c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class ClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#create Cluster#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#delete Cluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#update Cluster#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92c334c703aef0d0f636e7c9aef42d453265fa37f5828d8e39869e7cd4981a3c)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#create Cluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#delete Cluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#update Cluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4646ff02031c0d72331532320390ecb339a0bf85b60d616cc955f5b71bf0ea65)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__cc81255c78863a3634921d3ee04c5e4d99105bc692c91d2b04bd6d1f2e89ff76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fc9abf346334b1ad9fedeaba669504e24686a560309880832fc66cf96f40a55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5ab72cc08b84814e65f54550046ec38a594d5c27abb02d83277964bcffb8d2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ClusterTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ClusterTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ClusterTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2377f1f1d52d642aa148773ae1941fb84bede817b8e366fe52450368aa29c338)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterWorkloadType",
    jsii_struct_bases=[],
    name_mapping={"clients": "clients"},
)
class ClusterWorkloadType:
    def __init__(
        self,
        *,
        clients: typing.Union["ClusterWorkloadTypeClients", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param clients: clients block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#clients Cluster#clients}
        '''
        if isinstance(clients, dict):
            clients = ClusterWorkloadTypeClients(**clients)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91d6675b4d9372e46590bd6682391996df423eb3b05ac786045b0594928233d9)
            check_type(argname="argument clients", value=clients, expected_type=type_hints["clients"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "clients": clients,
        }

    @builtins.property
    def clients(self) -> "ClusterWorkloadTypeClients":
        '''clients block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#clients Cluster#clients}
        '''
        result = self._values.get("clients")
        assert result is not None, "Required property 'clients' is missing"
        return typing.cast("ClusterWorkloadTypeClients", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterWorkloadType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.cluster.ClusterWorkloadTypeClients",
    jsii_struct_bases=[],
    name_mapping={"jobs": "jobs", "notebooks": "notebooks"},
)
class ClusterWorkloadTypeClients:
    def __init__(
        self,
        *,
        jobs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        notebooks: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param jobs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#jobs Cluster#jobs}.
        :param notebooks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#notebooks Cluster#notebooks}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4c45320c179e87039fdeadb2fa7fcf5de82491459b1105a911f1341ce7362d3)
            check_type(argname="argument jobs", value=jobs, expected_type=type_hints["jobs"])
            check_type(argname="argument notebooks", value=notebooks, expected_type=type_hints["notebooks"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if jobs is not None:
            self._values["jobs"] = jobs
        if notebooks is not None:
            self._values["notebooks"] = notebooks

    @builtins.property
    def jobs(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#jobs Cluster#jobs}.'''
        result = self._values.get("jobs")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def notebooks(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#notebooks Cluster#notebooks}.'''
        result = self._values.get("notebooks")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterWorkloadTypeClients(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClusterWorkloadTypeClientsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterWorkloadTypeClientsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c9a5e13a6e5c5d8cb2fa254a4868533cd415eef903e1c75b4833f0df68d4465a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetJobs")
    def reset_jobs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobs", []))

    @jsii.member(jsii_name="resetNotebooks")
    def reset_notebooks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotebooks", []))

    @builtins.property
    @jsii.member(jsii_name="jobsInput")
    def jobs_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "jobsInput"))

    @builtins.property
    @jsii.member(jsii_name="notebooksInput")
    def notebooks_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "notebooksInput"))

    @builtins.property
    @jsii.member(jsii_name="jobs")
    def jobs(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "jobs"))

    @jobs.setter
    def jobs(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e289268e6667bef907a88d8c0b585fb43729ab6080060c90856c408ec61bed74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobs", value)

    @builtins.property
    @jsii.member(jsii_name="notebooks")
    def notebooks(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "notebooks"))

    @notebooks.setter
    def notebooks(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20f55440d1c99aa179300b46259dfe3a75219d7e2e2c05fd6b4777a93ce48caf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notebooks", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterWorkloadTypeClients]:
        return typing.cast(typing.Optional[ClusterWorkloadTypeClients], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ClusterWorkloadTypeClients],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96b05367c91aa04db08b328b9e2b6a9f6130dc9842d4fcdcdf8ef3fe72632974)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ClusterWorkloadTypeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.cluster.ClusterWorkloadTypeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b889ed11097998d72e08bf909fe623c8e39755e9ea4cd76ab89ea616c46826dd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putClients")
    def put_clients(
        self,
        *,
        jobs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        notebooks: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param jobs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#jobs Cluster#jobs}.
        :param notebooks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/cluster#notebooks Cluster#notebooks}.
        '''
        value = ClusterWorkloadTypeClients(jobs=jobs, notebooks=notebooks)

        return typing.cast(None, jsii.invoke(self, "putClients", [value]))

    @builtins.property
    @jsii.member(jsii_name="clients")
    def clients(self) -> ClusterWorkloadTypeClientsOutputReference:
        return typing.cast(ClusterWorkloadTypeClientsOutputReference, jsii.get(self, "clients"))

    @builtins.property
    @jsii.member(jsii_name="clientsInput")
    def clients_input(self) -> typing.Optional[ClusterWorkloadTypeClients]:
        return typing.cast(typing.Optional[ClusterWorkloadTypeClients], jsii.get(self, "clientsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ClusterWorkloadType]:
        return typing.cast(typing.Optional[ClusterWorkloadType], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ClusterWorkloadType]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e29e8015eed67955bda3224be20ee90c0f51e1ef6596c7629c57e7d2f95eac74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Cluster",
    "ClusterAutoscale",
    "ClusterAutoscaleOutputReference",
    "ClusterAwsAttributes",
    "ClusterAwsAttributesOutputReference",
    "ClusterAzureAttributes",
    "ClusterAzureAttributesOutputReference",
    "ClusterClusterLogConf",
    "ClusterClusterLogConfDbfs",
    "ClusterClusterLogConfDbfsOutputReference",
    "ClusterClusterLogConfOutputReference",
    "ClusterClusterLogConfS3",
    "ClusterClusterLogConfS3OutputReference",
    "ClusterClusterMountInfo",
    "ClusterClusterMountInfoList",
    "ClusterClusterMountInfoNetworkFilesystemInfo",
    "ClusterClusterMountInfoNetworkFilesystemInfoOutputReference",
    "ClusterClusterMountInfoOutputReference",
    "ClusterConfig",
    "ClusterDockerImage",
    "ClusterDockerImageBasicAuth",
    "ClusterDockerImageBasicAuthOutputReference",
    "ClusterDockerImageOutputReference",
    "ClusterGcpAttributes",
    "ClusterGcpAttributesOutputReference",
    "ClusterInitScripts",
    "ClusterInitScriptsAbfss",
    "ClusterInitScriptsAbfssOutputReference",
    "ClusterInitScriptsDbfs",
    "ClusterInitScriptsDbfsOutputReference",
    "ClusterInitScriptsFile",
    "ClusterInitScriptsFileOutputReference",
    "ClusterInitScriptsGcs",
    "ClusterInitScriptsGcsOutputReference",
    "ClusterInitScriptsList",
    "ClusterInitScriptsOutputReference",
    "ClusterInitScriptsS3",
    "ClusterInitScriptsS3OutputReference",
    "ClusterLibrary",
    "ClusterLibraryCran",
    "ClusterLibraryCranOutputReference",
    "ClusterLibraryList",
    "ClusterLibraryMaven",
    "ClusterLibraryMavenOutputReference",
    "ClusterLibraryOutputReference",
    "ClusterLibraryPypi",
    "ClusterLibraryPypiOutputReference",
    "ClusterTimeouts",
    "ClusterTimeoutsOutputReference",
    "ClusterWorkloadType",
    "ClusterWorkloadTypeClients",
    "ClusterWorkloadTypeClientsOutputReference",
    "ClusterWorkloadTypeOutputReference",
]

publication.publish()

def _typecheckingstub__36a3206048502333d9aff7a4f56841ba1a9962695c76116ee7f47aaa93570b45(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    spark_version: builtins.str,
    apply_policy_default_values: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    autoscale: typing.Optional[typing.Union[ClusterAutoscale, typing.Dict[builtins.str, typing.Any]]] = None,
    autotermination_minutes: typing.Optional[jsii.Number] = None,
    aws_attributes: typing.Optional[typing.Union[ClusterAwsAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_attributes: typing.Optional[typing.Union[ClusterAzureAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_id: typing.Optional[builtins.str] = None,
    cluster_log_conf: typing.Optional[typing.Union[ClusterClusterLogConf, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_mount_info: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterClusterMountInfo, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    data_security_mode: typing.Optional[builtins.str] = None,
    docker_image: typing.Optional[typing.Union[ClusterDockerImage, typing.Dict[builtins.str, typing.Any]]] = None,
    driver_instance_pool_id: typing.Optional[builtins.str] = None,
    driver_node_type_id: typing.Optional[builtins.str] = None,
    enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_local_disk_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    gcp_attributes: typing.Optional[typing.Union[ClusterGcpAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    idempotency_token: typing.Optional[builtins.str] = None,
    init_scripts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterInitScripts, typing.Dict[builtins.str, typing.Any]]]]] = None,
    instance_pool_id: typing.Optional[builtins.str] = None,
    is_pinned: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    library: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterLibrary, typing.Dict[builtins.str, typing.Any]]]]] = None,
    node_type_id: typing.Optional[builtins.str] = None,
    num_workers: typing.Optional[jsii.Number] = None,
    policy_id: typing.Optional[builtins.str] = None,
    runtime_engine: typing.Optional[builtins.str] = None,
    single_user_name: typing.Optional[builtins.str] = None,
    spark_conf: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    spark_env_vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ClusterTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    workload_type: typing.Optional[typing.Union[ClusterWorkloadType, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__77b8337184e282fb74f740e86ca3551f4f7f6f172b01bbb3a498e5c2ea3d9c32(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterClusterMountInfo, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d45f4b5255c9d996654ab273cfff68c8c5fc22dce2938b7df48c1bd7c6cd66c0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterInitScripts, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5a9a4a9f21f40274a26ecb4a86a9f3557fd0cdc5e8c8417fd801a36cd2fac4b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterLibrary, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7cabbf0d6498931ae157c430bf39665c10ffea740f61d9ab7268362f8f7f881(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2815e4e079050d81fdfc1cf01a79e883a2495044e6166a3b3c7f78272e4b1c27(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ba01516306c52e1595d9a6f97f0fba15f1d1fa0906da3df1843d7b33f4d3d94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f60eec96f8acccca175c5e8c71028a8034f7733d87cc54bba294ff46016c74ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e0320aae032d8f03d5acd41313da90baf7fb01b0180e6ffd3d61ae8af52d350(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1e3e826e56a954b3d855e11cba3f9d9c6685e39a2c66acfc10cc2dd30ff7d52(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce09e7a0a3b35bd02eced9be68cc78c97ba7beb50ac5bbe8a953b7d9027f3d76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0de5b50e979d719699b92adb86cb819244ecec94e3be70545edf528e0cdd60bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93dbd987eba505db154a14da125bc1e22f31770df7ef01d945153fcecf70031e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3021600a1e56cba1a8ce733808acc7fcda74bd142a84595ce342ed6fb49f0f4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e99215eabdb87698969071969e44ccda3fe16c44de75b043b68bf712fe169aa7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0e831b68c49f94b0203c838ea45889d71eeb456249bc3ee018ba22d3c91ff7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30893f97d75bb269317b623d3d8cb3aed547b9f6fa69b30bcbf9b6d6cff13ec8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a7eeb0b6d5f23f9851583411621dc5fdacfce38b6dfcdda9e1a53921d6cca65(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b699f459568e888b634d73fe252b3c6d606f8d3cb9f1fd4e93aa315b9b66bbcf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f932a551fef8dafd16385fcbbb517d1baf7d515fc7bd9aaeabedb55bed2ec7b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c953fd3ef5af1a46aa69c4585d77a655716b686e68ddb0255c6d65ab744dec9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc6628aad3d1cc745affe89e7a67c258ca04c8009429010c58f8e5a49b6e0a28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bae38e870f81c0b261606c152e0e3284bdaa614ee015b28032fdee25f81131c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d27c86ab0484f826ded796b14f133c650e6cc5419810ceda7ee665f611eb656(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eebec4050a340c67486e772f758fb81f2dba6813577a6607ebf2a416f2b27465(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad283c85743500c809e84234dffb1e9a58afb0e99759541149abda7962d7d488(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ba63478bcd5da4a8fc3f4e913208a94122c0b5d986e05da1857ba725fcd3f06(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66c74f5775ba0d7faa41eb8981851bd915e25b7b61f359b00c886a4e861958ad(
    *,
    max_workers: typing.Optional[jsii.Number] = None,
    min_workers: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d07d79f2666b2cb985530d9fd9d4694ac97d6cc9be72867fe120454f45ec44f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea0a156b7d5f9c09af769f8039137c053ee031bcf9dc8693e9a88a0e46461604(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8164a07dfd9a9ea59420bee66408f619ea4fffccc5234d370a1d1f7cb4ab0e8b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe1c2a6a0d3c78e3957c82ec8d98410e100eab3e2da05ffccfd32e62721c7482(
    value: typing.Optional[ClusterAutoscale],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2193581a055ae819d0e7cf74e2c3465586630c2fd281671392cc24a15f15fba(
    *,
    availability: typing.Optional[builtins.str] = None,
    ebs_volume_count: typing.Optional[jsii.Number] = None,
    ebs_volume_size: typing.Optional[jsii.Number] = None,
    ebs_volume_type: typing.Optional[builtins.str] = None,
    first_on_demand: typing.Optional[jsii.Number] = None,
    instance_profile_arn: typing.Optional[builtins.str] = None,
    spot_bid_price_percent: typing.Optional[jsii.Number] = None,
    zone_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__092369b78a672ba593d7d65cfd79c0f8edae66f6a389ba51552e46adf88a6896(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__418a0ff089fc6c4ee128f272a62e604059b9217c7d5a000272db3c3c78440389(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80f4fdbf37ef427aa85342c2883f546fe84e5ab6ce252febf9a00fb5d4185d42(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24188179135cccff3f94ac5b46c60bcb328118c8b08630a12d01ab6406b7bca0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36c7e3f56a6ded46e13083b9d75f06ef867eace4546ccfd69855f97823e77922(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ee17e4e0608e80e14a7ca3e4530234174fe4da9b28035f144ff6c013950b3d9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ee132e336ec9e069c7f1a21a2dad592d9d0978732f07148636e715417616a71(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__286b832824cf24a3c0932e8c9c66d780aa4ea78e12fcdbeddb333a092eb9f313(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__948b9fc625995b48fd2f573b2337357f3871f8c585fadf74f093294323b095f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__049a0bb0306f1718c1e85e70742d8922c5b73ff484ae2d43943b3b876ab8ed45(
    value: typing.Optional[ClusterAwsAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a0d09e1c8bf1cebfaafa3d5babe5a174f67c451b2b28e78955bba23ae8f9ec4(
    *,
    availability: typing.Optional[builtins.str] = None,
    first_on_demand: typing.Optional[jsii.Number] = None,
    spot_bid_max_price: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb09e2b38270eac5420a0289aefc445ba2a7515c3d00efdcb40fdf3c52fd08ba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de23baa37454659256743a5f9f538acaefa23597b2e9b02e411ab2865524ed12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c8b82de0a39dca5cc8566093bb073dd3a1f2ec0030be37786e5f3a6b14832e2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90a6bd3c39d1bd751e0cfc06f53d108a28b1db947af8561bb00abd7f13b819d1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00f86a26ac9cf57d6bbdcb08818ce6b728c44658856d10155b562ed3acefabf2(
    value: typing.Optional[ClusterAzureAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92bf88827d2646e52cfde2eef5d59f8e28f643d3f120b9e125c3c24ddade8fe3(
    *,
    dbfs: typing.Optional[typing.Union[ClusterClusterLogConfDbfs, typing.Dict[builtins.str, typing.Any]]] = None,
    s3: typing.Optional[typing.Union[ClusterClusterLogConfS3, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__681511e5f1a9577eb7317b443085cbfdbaf0889414e77f24b02fb2dd2307d33d(
    *,
    destination: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf5b0a45faa306950ce0ec3e530f6b677b0f35adbee0693d90e8c81a6d2c2c7b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e00db5b54bc9dd4d8aa150bf88ecb5e9ce1ae54ca2b105accfa3fa5131cc3c1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c68b4451499c161d610019799e4b41f5a73467ca0aa2245e876c4776974d21a5(
    value: typing.Optional[ClusterClusterLogConfDbfs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98a6c2bb5e5fd69a56e95ac72e5c8f6b1e08ddf34263f99470fdb5826fa6be17(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10043d5410466ab9c13d2169a04e4b1f4ea56eebd97dcb06a669bf85d907ea97(
    value: typing.Optional[ClusterClusterLogConf],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__301b8a78c470b4d4fef46eb0f7c16d19c02b3ef10b6f7d3aa455034ac733cd65(
    *,
    destination: builtins.str,
    canned_acl: typing.Optional[builtins.str] = None,
    enable_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encryption_type: typing.Optional[builtins.str] = None,
    endpoint: typing.Optional[builtins.str] = None,
    kms_key: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cb54b052a47534b588d62abfeef00192815e6d36a488d8da1ea75fbc922f509(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b47007f0f324003c744765b78e673b209f7505d1ca20f98ec216644b2742c08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c018f96ed41f2df877ce72b56fe9420c8e3fc209f88b24ad28f8fcd7184a902f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b51c57bd4496defbfe4dd329f051fec31a0273778e1f0dc350e7798ad87a8b6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43d879c34a2de94785bc67dbb0d4dff17a68864ff52eca552a6cfe030e0dce26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c250a9d528845d4df966d09ae643c23b5c90c24728c50833eec70b7799f6e117(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d240cb7c4dfdb29e425642eae8103bdedd0a77ca69d384d6c3aa99b69a68658f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4086f8d40ff2c3d2b4d7d19afdaa262eb44070a4ce55c9c4535e87f918fb01b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1622989cac13ddcc7ee8728d5a6dd4b57ec793b959143784f7f754b8c38f4bfc(
    value: typing.Optional[ClusterClusterLogConfS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__116a9f144b5725a425a9eb4b8c8a972ca5617fc6b1850b2f7cd1749988df47b4(
    *,
    local_mount_dir_path: builtins.str,
    network_filesystem_info: typing.Union[ClusterClusterMountInfoNetworkFilesystemInfo, typing.Dict[builtins.str, typing.Any]],
    remote_mount_dir_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeea47c59ed795ef0fad8ad94706a587e2897af191eb68eb7270d363b7a835aa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1164e6b84fd560940a07c38b77496bc4c99472811e65f884e31f5162807f11a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19e31f0d216ce632dd1e8596f163bd047794d27d7f5424d8da3fe5628dafdf22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd542198e72ee5363f173f4536038a15295815c1c1a886607290fb6779b2884c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d13c3728ed7d0b6f259f68f2ff7cfc566600effb2a104d31ae617aebe097070(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d54fd2e5c4cbaa84115d7d2dd75a4edd2890f8f4fd00e7e66eb12022f0c0a30(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterClusterMountInfo]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a110197c8c1e6dd7eb926ecd3bb53e8fc7324dea484f26eb0da8924bb1c49a0(
    *,
    server_address: builtins.str,
    mount_options: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f56455d8ebc7b4c196edb334bc1b6699ac028034b56bed6339b23f80c0edb04f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81a0f59a66177874939da9d85e1e2a4295bcb9639dbf59f2570882bb8bfdf798(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5aa18dad41d63fb6c5c6cb4409422ca92d492971b6fae55fc5adef2d8503751(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__470680cdfddce4ae343b945ffa3211be6de7ea067f3c5ffb2dfacc24c892c3d0(
    value: typing.Optional[ClusterClusterMountInfoNetworkFilesystemInfo],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01ed70addc78e26f30e9235722d0cd3eb8abfdbc12fca2641f18912adc92bf5e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec934ee0128ef62df76388ca5705ed5bcf6300265cd927ff4ce9ec7676e56db7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec411b8dcbe5ab68ab483f04f4b564c9c9ea8d01106813d3045abbeebe309a10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__101453a2b4ba6a40af722a2f2e1b5d6968fea19259c9cc241d9e305748324dcb(
    value: typing.Optional[typing.Union[ClusterClusterMountInfo, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14d046f126561eb6a7b17010f64421803233432f70dc54f0884903b8f749b430(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    spark_version: builtins.str,
    apply_policy_default_values: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    autoscale: typing.Optional[typing.Union[ClusterAutoscale, typing.Dict[builtins.str, typing.Any]]] = None,
    autotermination_minutes: typing.Optional[jsii.Number] = None,
    aws_attributes: typing.Optional[typing.Union[ClusterAwsAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_attributes: typing.Optional[typing.Union[ClusterAzureAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_id: typing.Optional[builtins.str] = None,
    cluster_log_conf: typing.Optional[typing.Union[ClusterClusterLogConf, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_mount_info: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterClusterMountInfo, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cluster_name: typing.Optional[builtins.str] = None,
    custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    data_security_mode: typing.Optional[builtins.str] = None,
    docker_image: typing.Optional[typing.Union[ClusterDockerImage, typing.Dict[builtins.str, typing.Any]]] = None,
    driver_instance_pool_id: typing.Optional[builtins.str] = None,
    driver_node_type_id: typing.Optional[builtins.str] = None,
    enable_elastic_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_local_disk_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    gcp_attributes: typing.Optional[typing.Union[ClusterGcpAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    idempotency_token: typing.Optional[builtins.str] = None,
    init_scripts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterInitScripts, typing.Dict[builtins.str, typing.Any]]]]] = None,
    instance_pool_id: typing.Optional[builtins.str] = None,
    is_pinned: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    library: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ClusterLibrary, typing.Dict[builtins.str, typing.Any]]]]] = None,
    node_type_id: typing.Optional[builtins.str] = None,
    num_workers: typing.Optional[jsii.Number] = None,
    policy_id: typing.Optional[builtins.str] = None,
    runtime_engine: typing.Optional[builtins.str] = None,
    single_user_name: typing.Optional[builtins.str] = None,
    spark_conf: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    spark_env_vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ClusterTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    workload_type: typing.Optional[typing.Union[ClusterWorkloadType, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37926b7c231bdb77c8e117e6b2de5f17124539a2bcdf0a831fb0267bdb3d75e3(
    *,
    url: builtins.str,
    basic_auth: typing.Optional[typing.Union[ClusterDockerImageBasicAuth, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b422412080207b5e3eb95df190661862cb3f274293c32c50feda49d52d8438a(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a758ae3ef2547ff793de7cab8e09b8f3a0b3b7001b7d2a360d76be5827d95c8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05ce539b347a5f8c7f53ceb91ae0446c4881411068d8ba1d9bfe43b44ddd633a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f6df8fb344db3c1a346bb498c0b2a6026785dd69dbe333f6985b4e59d969b88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12cea82b838986e9f7796c87b441bdc1c11c046f42d5825c2d0dc59a10daa819(
    value: typing.Optional[ClusterDockerImageBasicAuth],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9293205bc15dc0229b5d52f743ae267259a1000216023d18c6d4f271efdb2dc8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20d9fb12bfbfeedb4e6d72e8492bebd7b17409b1fb529da3e2ef0a883b97e150(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__937e6a79496d3ca1b320ea195251b23da6d62ca2f0acfb8dc7768ce5b9c5e704(
    value: typing.Optional[ClusterDockerImage],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be63bfc07bad962fb9da45b72c617e4909affe17cf24fb6cb3077529ca56f0eb(
    *,
    availability: typing.Optional[builtins.str] = None,
    boot_disk_size: typing.Optional[jsii.Number] = None,
    google_service_account: typing.Optional[builtins.str] = None,
    use_preemptible_executors: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    zone_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bbb16a6b9dc82a0a9fe5cf674d02acdcb671b0c4e0232ab6dc4cb290566ff20(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99c79b7e530aa0db44e0c4fabe9f23baa357250590f4318e0b7b34f5ddf66860(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94241de581cf0c729b5cb2735afd6119ffb9806f5dbfb1ab789c0a484224f17a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__558da5a6fcaed9b5505124416a4ff869e5704feeca31eb38467ce21d2a6095c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d83c028737969885dd577e4f3c6b2caf4f3be0e8809d5ac3fe7eee0a1dadb253(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c36ca7d6dd70c73dbf0f14607acd1cbfb51192f2d2c8d6b38ff9b8e9851b642e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b012f7736e21e4ddd96a7ef109a4a57e677d3b76c1afe7865d0f7198c9393f8(
    value: typing.Optional[ClusterGcpAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__494fb6b11b41dea3e2cd7c053299b63ae19f37fd4ed4b7c4a14df6b5b2946868(
    *,
    abfss: typing.Optional[typing.Union[ClusterInitScriptsAbfss, typing.Dict[builtins.str, typing.Any]]] = None,
    dbfs: typing.Optional[typing.Union[ClusterInitScriptsDbfs, typing.Dict[builtins.str, typing.Any]]] = None,
    file: typing.Optional[typing.Union[ClusterInitScriptsFile, typing.Dict[builtins.str, typing.Any]]] = None,
    gcs: typing.Optional[typing.Union[ClusterInitScriptsGcs, typing.Dict[builtins.str, typing.Any]]] = None,
    s3: typing.Optional[typing.Union[ClusterInitScriptsS3, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cab747a6f7cc796d9d369ae4f336ab5b3980c5c5c41e3e3562563859e8fc0f99(
    *,
    destination: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c86fa149004e6c4dbc48e35a84a05a39ffebf5bcdd8a58f83ee7f52271620802(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a9f6396ecc27d204e343ea63d1777c324922913bc93a1f58307cbc924736a3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc10b53d4d2d943e15aa455920c16cc728fcf8522e335bd359ab290838d72c9e(
    value: typing.Optional[ClusterInitScriptsAbfss],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3ad4dcb860716faf8eba38f16409d789b114e1e1a0f2778d3d7ed34a22805d4(
    *,
    destination: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__897215de756898935e3b8d81c565a196cebcdfccf75e3b7ac3c9e5d76a0b97ba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e757e1d8af34d081b7fccc2452fec07e42756d46cfef509ae2a8b9f2357c60b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a2cbd1c01acb74113c9bcc7c7beba608e802337b64196ce5960dc654356547e(
    value: typing.Optional[ClusterInitScriptsDbfs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a22b3eb9e2745fcbbd27569b7aec04de12fb91d63b354ba95311f37ca95e75d2(
    *,
    destination: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01afb610dd0ec5b8159a17c28de91e14ad5320181c0adf08f0fd038047dc1b0b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f0d0107ac197d93211a7e57efcd3a4ebe873fe2838700776b4ee39e736e851a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9e673057ed8053135b9e4051f628329599f69aa2e1720b8667d6205b7f16dc0(
    value: typing.Optional[ClusterInitScriptsFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__408189c618246c045002f2adca0ab2867c9ed3fa870106b072b5855fc34847d0(
    *,
    destination: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4bbf8a86a14323eff2056642ec87137320e8262f92307e49d2904490b959ccb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b82862eaa7e1117314e2db0833e6be5553984515347c9354d46ef18ba2ee38f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff32fd09cb2aceaab8772822fa7f10fb10fb2d4b505a7079a6f502c036260316(
    value: typing.Optional[ClusterInitScriptsGcs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42283c361e63a817b9f942d6874dc7443408878905638d3d08eee2aea93c1fb5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__959f60f88ac906727641cb526b58dbc99a9ccb1dc7f71b8460211b05a6a50b0e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38a69e09aa8cce292b857a095c90c287a495a689a06eefbddf53acf288c26002(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__022fec918f2e97f5f306e595271f10833b2412a433e9b6251f5c0151954cde95(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eadd03891ac4e73bd0abcd5ac9e157fc99fa7db206ddf986b53e5aaea7070c4e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a39862aff9c53c1f61d26b0a55b76ef5a99d139142f0560090d0c4705b15b1ae(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterInitScripts]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d8f162a29d01e2b6979490eda8cae41bcd46b45001c210d11fb591893a6a189(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__febad621ee9c7866a0bbe4a924b357ceee67e0f507e1d22f6d771d8797ebe48a(
    value: typing.Optional[typing.Union[ClusterInitScripts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b0bd2dc4ac819928b8c0e1d334484bd488b5b8801652408c8242afd918acfbc(
    *,
    destination: builtins.str,
    canned_acl: typing.Optional[builtins.str] = None,
    enable_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    encryption_type: typing.Optional[builtins.str] = None,
    endpoint: typing.Optional[builtins.str] = None,
    kms_key: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0c746ea776606e726f333910845e49bcc05a924283bd07f6e3f3dfa4e3402a7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__018577fbccec2824ea8fc0289d8b6ee607e6b7c6e6bf35cb5d663fb94bf91e39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec6b545aae826c8b56eccc90b7dad5eeae38471607e2dba1839c536db9fba4f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88d3bfe09c8b3ac3c50b07dc34d338705dff879bce86b96daf2cc12fb7f49883(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56649e2cbcc783055f4f141702d80dc36d7720060d28545007106adb39ac43e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72c487ae09268491a02819bc3cdbf71a08e249f18ea92b540d43a7c87eadc701(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1c1ea54d2dcf3f547b3e1627fe285bf683a71530017452f76fcaaad9de649ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18ce5a6694c984e2c22d71ffe2df7db528d0bc0bde93e52eb43f0610e20a2fd4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c5aaefe34b9075b98486d5df164281760dca96050828ffc2051bf8b2ec4e5d0(
    value: typing.Optional[ClusterInitScriptsS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__becf6b973435c78b2067ceaae644277db171b285d1b1db9a025ea96505bcaf36(
    *,
    cran: typing.Optional[typing.Union[ClusterLibraryCran, typing.Dict[builtins.str, typing.Any]]] = None,
    egg: typing.Optional[builtins.str] = None,
    jar: typing.Optional[builtins.str] = None,
    maven: typing.Optional[typing.Union[ClusterLibraryMaven, typing.Dict[builtins.str, typing.Any]]] = None,
    pypi: typing.Optional[typing.Union[ClusterLibraryPypi, typing.Dict[builtins.str, typing.Any]]] = None,
    whl: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__485358356798bc354f00dc8dd2d323f01183fa98ea22b35642ddd753fbe478fd(
    *,
    package: builtins.str,
    repo: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e63eaa1ba046f6bfb93082b88fa0cd3db2950780b72c5998666b5c81983865e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4416d2b77d322e82686d82a15681d3935800cbfabdd129d6c01cb9aeefef01be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__678e91f9004e6c48080f2cf3d941acfe2db8a19c117ce61c849edc291dc97055(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1001a4ae4c774cfd2c333457b1ef4672990e59fc32a96083ba233db6fe6e4c8(
    value: typing.Optional[ClusterLibraryCran],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab3de513b29018fcc7c0651b74da99b8ead141cf97e4532b6fa2f04965d1ba10(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4bc06c33382cab995aa74b62707132de9dd887640335bf7286bf874bae310e8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7abc31bd2d1171c40f415c6bcdf7ea55f076d69b3a6bd7a5940f590f2b5bc1a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5c57e9abfe463ad1d8c887e498288e398d767509840320fd60de7ac364ce70a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bf17beb7446922d62bef521af65876430a1b5d2576d4d558af3fd3faf8a614f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55a38bd275d3b152d6d58b6d775eb84b2771303f149266dc436c1b6660ee432e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ClusterLibrary]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e0dc26666e722c084a2693f6a63f1d78fafa0e656ad037101e16837a4bf2c2a(
    *,
    coordinates: builtins.str,
    exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
    repo: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c7731916d0580b75dffeaf50ae811d7aa814e411a721285788a57fbc83649da(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0f25dfb34842191b143d367131ea58edf560cbd8bdee512216a16db4e502e67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecb82508531a91ffdbda6838120fcbad6b92f3cd8017084bb852b79481b71f17(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6c3f668836cc8c80804367e0224689d08406c60c77371032ab2147fab7184d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3713f9c266d998800b2988b75e19e4b87a8bf8f5ef72d4ff0c270a2ec1f41c87(
    value: typing.Optional[ClusterLibraryMaven],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4beab7cde01790ec9a746485365ca663cb0895a7a06c1dcd2d8c83bfd688c51e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__189fbfb48d3f1121e43b82c7f46947b64832812f2742f352aad05930555a1ffd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__853e34a19557d83e1e15d46f23b5f77228280bb7821aaffd4d26b1e7e5b7bc34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0b08d03aefba502de5880000ef07670994844522c14c2879dcfa7b2501ca9d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c693be5b40365e58756dec1a5f2b7805277bd07e4f14678a6aa3c2aca1f16e85(
    value: typing.Optional[typing.Union[ClusterLibrary, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81f52f5b45ea0376ddf0bb49133aa7be89133811328a4529a0a45654cd7bc41d(
    *,
    package: builtins.str,
    repo: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d3c46242a4458c69a237061ea7f9757d44cb8901df36580c8b535c04ae49052(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2624d098297936eb087b409e52a669a9354e922d3db455b3b7cf82aacdb41140(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cbb38c25eeca993d809044fa5696656dbee58adb2cacc505f7eafcb2ca48c67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1edede53ec44a55be5c3d4b2d1367bd6d89e7278f6739e28a84c49afb625b7c0(
    value: typing.Optional[ClusterLibraryPypi],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92c334c703aef0d0f636e7c9aef42d453265fa37f5828d8e39869e7cd4981a3c(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4646ff02031c0d72331532320390ecb339a0bf85b60d616cc955f5b71bf0ea65(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc81255c78863a3634921d3ee04c5e4d99105bc692c91d2b04bd6d1f2e89ff76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fc9abf346334b1ad9fedeaba669504e24686a560309880832fc66cf96f40a55(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5ab72cc08b84814e65f54550046ec38a594d5c27abb02d83277964bcffb8d2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2377f1f1d52d642aa148773ae1941fb84bede817b8e366fe52450368aa29c338(
    value: typing.Optional[typing.Union[ClusterTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91d6675b4d9372e46590bd6682391996df423eb3b05ac786045b0594928233d9(
    *,
    clients: typing.Union[ClusterWorkloadTypeClients, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4c45320c179e87039fdeadb2fa7fcf5de82491459b1105a911f1341ce7362d3(
    *,
    jobs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    notebooks: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9a5e13a6e5c5d8cb2fa254a4868533cd415eef903e1c75b4833f0df68d4465a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e289268e6667bef907a88d8c0b585fb43729ab6080060c90856c408ec61bed74(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20f55440d1c99aa179300b46259dfe3a75219d7e2e2c05fd6b4777a93ce48caf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96b05367c91aa04db08b328b9e2b6a9f6130dc9842d4fcdcdf8ef3fe72632974(
    value: typing.Optional[ClusterWorkloadTypeClients],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b889ed11097998d72e08bf909fe623c8e39755e9ea4cd76ab89ea616c46826dd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e29e8015eed67955bda3224be20ee90c0f51e1ef6596c7629c57e7d2f95eac74(
    value: typing.Optional[ClusterWorkloadType],
) -> None:
    """Type checking stubs"""
    pass
