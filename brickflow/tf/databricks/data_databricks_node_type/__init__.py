'''
# `data_databricks_node_type`

Refer to the Terraform Registory for docs: [`data_databricks_node_type`](https://www.terraform.io/docs/providers/databricks/d/node_type).
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


class DataDatabricksNodeType(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.dataDatabricksNodeType.DataDatabricksNodeType",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/d/node_type databricks_node_type}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        category: typing.Optional[builtins.str] = None,
        fleet: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        gb_per_core: typing.Optional[jsii.Number] = None,
        graviton: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        is_io_cache_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        local_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        local_disk_min_size: typing.Optional[jsii.Number] = None,
        min_cores: typing.Optional[jsii.Number] = None,
        min_gpus: typing.Optional[jsii.Number] = None,
        min_memory_gb: typing.Optional[jsii.Number] = None,
        photon_driver_capable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        photon_worker_capable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        support_port_forwarding: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/d/node_type databricks_node_type} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param category: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#category DataDatabricksNodeType#category}.
        :param fleet: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#fleet DataDatabricksNodeType#fleet}.
        :param gb_per_core: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#gb_per_core DataDatabricksNodeType#gb_per_core}.
        :param graviton: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#graviton DataDatabricksNodeType#graviton}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#id DataDatabricksNodeType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_io_cache_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#is_io_cache_enabled DataDatabricksNodeType#is_io_cache_enabled}.
        :param local_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#local_disk DataDatabricksNodeType#local_disk}.
        :param local_disk_min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#local_disk_min_size DataDatabricksNodeType#local_disk_min_size}.
        :param min_cores: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_cores DataDatabricksNodeType#min_cores}.
        :param min_gpus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_gpus DataDatabricksNodeType#min_gpus}.
        :param min_memory_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_memory_gb DataDatabricksNodeType#min_memory_gb}.
        :param photon_driver_capable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#photon_driver_capable DataDatabricksNodeType#photon_driver_capable}.
        :param photon_worker_capable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#photon_worker_capable DataDatabricksNodeType#photon_worker_capable}.
        :param support_port_forwarding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#support_port_forwarding DataDatabricksNodeType#support_port_forwarding}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff334258931bef8460f15bd68cf621b3cc458c9abbad197370676ab0dfd99112)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataDatabricksNodeTypeConfig(
            category=category,
            fleet=fleet,
            gb_per_core=gb_per_core,
            graviton=graviton,
            id=id,
            is_io_cache_enabled=is_io_cache_enabled,
            local_disk=local_disk,
            local_disk_min_size=local_disk_min_size,
            min_cores=min_cores,
            min_gpus=min_gpus,
            min_memory_gb=min_memory_gb,
            photon_driver_capable=photon_driver_capable,
            photon_worker_capable=photon_worker_capable,
            support_port_forwarding=support_port_forwarding,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCategory")
    def reset_category(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCategory", []))

    @jsii.member(jsii_name="resetFleet")
    def reset_fleet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFleet", []))

    @jsii.member(jsii_name="resetGbPerCore")
    def reset_gb_per_core(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGbPerCore", []))

    @jsii.member(jsii_name="resetGraviton")
    def reset_graviton(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGraviton", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsIoCacheEnabled")
    def reset_is_io_cache_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsIoCacheEnabled", []))

    @jsii.member(jsii_name="resetLocalDisk")
    def reset_local_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalDisk", []))

    @jsii.member(jsii_name="resetLocalDiskMinSize")
    def reset_local_disk_min_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalDiskMinSize", []))

    @jsii.member(jsii_name="resetMinCores")
    def reset_min_cores(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinCores", []))

    @jsii.member(jsii_name="resetMinGpus")
    def reset_min_gpus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinGpus", []))

    @jsii.member(jsii_name="resetMinMemoryGb")
    def reset_min_memory_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinMemoryGb", []))

    @jsii.member(jsii_name="resetPhotonDriverCapable")
    def reset_photon_driver_capable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhotonDriverCapable", []))

    @jsii.member(jsii_name="resetPhotonWorkerCapable")
    def reset_photon_worker_capable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhotonWorkerCapable", []))

    @jsii.member(jsii_name="resetSupportPortForwarding")
    def reset_support_port_forwarding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSupportPortForwarding", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="categoryInput")
    def category_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "categoryInput"))

    @builtins.property
    @jsii.member(jsii_name="fleetInput")
    def fleet_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "fleetInput"))

    @builtins.property
    @jsii.member(jsii_name="gbPerCoreInput")
    def gb_per_core_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gbPerCoreInput"))

    @builtins.property
    @jsii.member(jsii_name="gravitonInput")
    def graviton_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "gravitonInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isIoCacheEnabledInput")
    def is_io_cache_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "isIoCacheEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="localDiskInput")
    def local_disk_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "localDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="localDiskMinSizeInput")
    def local_disk_min_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "localDiskMinSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="minCoresInput")
    def min_cores_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minCoresInput"))

    @builtins.property
    @jsii.member(jsii_name="minGpusInput")
    def min_gpus_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minGpusInput"))

    @builtins.property
    @jsii.member(jsii_name="minMemoryGbInput")
    def min_memory_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minMemoryGbInput"))

    @builtins.property
    @jsii.member(jsii_name="photonDriverCapableInput")
    def photon_driver_capable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "photonDriverCapableInput"))

    @builtins.property
    @jsii.member(jsii_name="photonWorkerCapableInput")
    def photon_worker_capable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "photonWorkerCapableInput"))

    @builtins.property
    @jsii.member(jsii_name="supportPortForwardingInput")
    def support_port_forwarding_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "supportPortForwardingInput"))

    @builtins.property
    @jsii.member(jsii_name="category")
    def category(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "category"))

    @category.setter
    def category(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f47f7327e009d80c22c44547f9fecf10e76cf16da121b2bf6a8e79b7e384d1c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "category", value)

    @builtins.property
    @jsii.member(jsii_name="fleet")
    def fleet(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "fleet"))

    @fleet.setter
    def fleet(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8ce1c140e25d45d988ea0138e41db8f2cb5eeb1e88cc8d0ffb573ddbf85abd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fleet", value)

    @builtins.property
    @jsii.member(jsii_name="gbPerCore")
    def gb_per_core(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gbPerCore"))

    @gb_per_core.setter
    def gb_per_core(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04fbcb2e8b3980443c8bbf3019d3b86694c6648aa69b207d4e636dc5a29f4789)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gbPerCore", value)

    @builtins.property
    @jsii.member(jsii_name="graviton")
    def graviton(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "graviton"))

    @graviton.setter
    def graviton(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c58e90e929525ccff2b66fcae41fcee5a360a73d074f7d69e66d0bb14fc9b9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "graviton", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39e076cd2273b844e31a90865aadbbcf3c55a3ef2732c927fe5e84ac8044fa4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isIoCacheEnabled")
    def is_io_cache_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "isIoCacheEnabled"))

    @is_io_cache_enabled.setter
    def is_io_cache_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac23b0cc8f92450fbe14dd57044b7ed5d5fa257f96cef9e327787270e9562568)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isIoCacheEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="localDisk")
    def local_disk(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "localDisk"))

    @local_disk.setter
    def local_disk(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2144d541a03234df63e609e537742342bf764a830e85d2fb5f718284581bbd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localDisk", value)

    @builtins.property
    @jsii.member(jsii_name="localDiskMinSize")
    def local_disk_min_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "localDiskMinSize"))

    @local_disk_min_size.setter
    def local_disk_min_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cceb9ce7e997b0ecee1a51492e17c0cafa58f365d619812d9724fd222c823eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localDiskMinSize", value)

    @builtins.property
    @jsii.member(jsii_name="minCores")
    def min_cores(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minCores"))

    @min_cores.setter
    def min_cores(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e3c4b033d31d5da97d3d67704a52dc987ca7113e972b3ebc26455a938222337)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minCores", value)

    @builtins.property
    @jsii.member(jsii_name="minGpus")
    def min_gpus(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minGpus"))

    @min_gpus.setter
    def min_gpus(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06490b570fded27be5dd1637e113daec483b3f762d9038ca266af8360d6c2d7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minGpus", value)

    @builtins.property
    @jsii.member(jsii_name="minMemoryGb")
    def min_memory_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minMemoryGb"))

    @min_memory_gb.setter
    def min_memory_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54dd7e3a65cda402649bd35b79f28919f7c98bbc9f71f36f78cc177be1f7eed9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minMemoryGb", value)

    @builtins.property
    @jsii.member(jsii_name="photonDriverCapable")
    def photon_driver_capable(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "photonDriverCapable"))

    @photon_driver_capable.setter
    def photon_driver_capable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05c31abe8a764df69996b964697b338bfb9dd4f9c6f27a54149c10ae0f364ce2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "photonDriverCapable", value)

    @builtins.property
    @jsii.member(jsii_name="photonWorkerCapable")
    def photon_worker_capable(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "photonWorkerCapable"))

    @photon_worker_capable.setter
    def photon_worker_capable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb582704ecfdbda0409b50da0acc51e107f9b312f1665ab8d9ff53b06d1c07d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "photonWorkerCapable", value)

    @builtins.property
    @jsii.member(jsii_name="supportPortForwarding")
    def support_port_forwarding(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "supportPortForwarding"))

    @support_port_forwarding.setter
    def support_port_forwarding(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52d4a0bd3e6ba79ac380ee40a3ec12625b2f4a5b4f548c21045bd5ffed1e3e5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportPortForwarding", value)


@jsii.data_type(
    jsii_type="databricks.dataDatabricksNodeType.DataDatabricksNodeTypeConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "category": "category",
        "fleet": "fleet",
        "gb_per_core": "gbPerCore",
        "graviton": "graviton",
        "id": "id",
        "is_io_cache_enabled": "isIoCacheEnabled",
        "local_disk": "localDisk",
        "local_disk_min_size": "localDiskMinSize",
        "min_cores": "minCores",
        "min_gpus": "minGpus",
        "min_memory_gb": "minMemoryGb",
        "photon_driver_capable": "photonDriverCapable",
        "photon_worker_capable": "photonWorkerCapable",
        "support_port_forwarding": "supportPortForwarding",
    },
)
class DataDatabricksNodeTypeConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        category: typing.Optional[builtins.str] = None,
        fleet: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        gb_per_core: typing.Optional[jsii.Number] = None,
        graviton: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        is_io_cache_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        local_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        local_disk_min_size: typing.Optional[jsii.Number] = None,
        min_cores: typing.Optional[jsii.Number] = None,
        min_gpus: typing.Optional[jsii.Number] = None,
        min_memory_gb: typing.Optional[jsii.Number] = None,
        photon_driver_capable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        photon_worker_capable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        support_port_forwarding: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param category: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#category DataDatabricksNodeType#category}.
        :param fleet: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#fleet DataDatabricksNodeType#fleet}.
        :param gb_per_core: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#gb_per_core DataDatabricksNodeType#gb_per_core}.
        :param graviton: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#graviton DataDatabricksNodeType#graviton}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#id DataDatabricksNodeType#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_io_cache_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#is_io_cache_enabled DataDatabricksNodeType#is_io_cache_enabled}.
        :param local_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#local_disk DataDatabricksNodeType#local_disk}.
        :param local_disk_min_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#local_disk_min_size DataDatabricksNodeType#local_disk_min_size}.
        :param min_cores: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_cores DataDatabricksNodeType#min_cores}.
        :param min_gpus: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_gpus DataDatabricksNodeType#min_gpus}.
        :param min_memory_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_memory_gb DataDatabricksNodeType#min_memory_gb}.
        :param photon_driver_capable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#photon_driver_capable DataDatabricksNodeType#photon_driver_capable}.
        :param photon_worker_capable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#photon_worker_capable DataDatabricksNodeType#photon_worker_capable}.
        :param support_port_forwarding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#support_port_forwarding DataDatabricksNodeType#support_port_forwarding}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7abac7aa85fb70c6fd65e58407b4371b1a6315c1f84ba8688a430e5fb4533822)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument category", value=category, expected_type=type_hints["category"])
            check_type(argname="argument fleet", value=fleet, expected_type=type_hints["fleet"])
            check_type(argname="argument gb_per_core", value=gb_per_core, expected_type=type_hints["gb_per_core"])
            check_type(argname="argument graviton", value=graviton, expected_type=type_hints["graviton"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_io_cache_enabled", value=is_io_cache_enabled, expected_type=type_hints["is_io_cache_enabled"])
            check_type(argname="argument local_disk", value=local_disk, expected_type=type_hints["local_disk"])
            check_type(argname="argument local_disk_min_size", value=local_disk_min_size, expected_type=type_hints["local_disk_min_size"])
            check_type(argname="argument min_cores", value=min_cores, expected_type=type_hints["min_cores"])
            check_type(argname="argument min_gpus", value=min_gpus, expected_type=type_hints["min_gpus"])
            check_type(argname="argument min_memory_gb", value=min_memory_gb, expected_type=type_hints["min_memory_gb"])
            check_type(argname="argument photon_driver_capable", value=photon_driver_capable, expected_type=type_hints["photon_driver_capable"])
            check_type(argname="argument photon_worker_capable", value=photon_worker_capable, expected_type=type_hints["photon_worker_capable"])
            check_type(argname="argument support_port_forwarding", value=support_port_forwarding, expected_type=type_hints["support_port_forwarding"])
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
        if category is not None:
            self._values["category"] = category
        if fleet is not None:
            self._values["fleet"] = fleet
        if gb_per_core is not None:
            self._values["gb_per_core"] = gb_per_core
        if graviton is not None:
            self._values["graviton"] = graviton
        if id is not None:
            self._values["id"] = id
        if is_io_cache_enabled is not None:
            self._values["is_io_cache_enabled"] = is_io_cache_enabled
        if local_disk is not None:
            self._values["local_disk"] = local_disk
        if local_disk_min_size is not None:
            self._values["local_disk_min_size"] = local_disk_min_size
        if min_cores is not None:
            self._values["min_cores"] = min_cores
        if min_gpus is not None:
            self._values["min_gpus"] = min_gpus
        if min_memory_gb is not None:
            self._values["min_memory_gb"] = min_memory_gb
        if photon_driver_capable is not None:
            self._values["photon_driver_capable"] = photon_driver_capable
        if photon_worker_capable is not None:
            self._values["photon_worker_capable"] = photon_worker_capable
        if support_port_forwarding is not None:
            self._values["support_port_forwarding"] = support_port_forwarding

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
    def category(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#category DataDatabricksNodeType#category}.'''
        result = self._values.get("category")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fleet(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#fleet DataDatabricksNodeType#fleet}.'''
        result = self._values.get("fleet")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def gb_per_core(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#gb_per_core DataDatabricksNodeType#gb_per_core}.'''
        result = self._values.get("gb_per_core")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def graviton(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#graviton DataDatabricksNodeType#graviton}.'''
        result = self._values.get("graviton")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#id DataDatabricksNodeType#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_io_cache_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#is_io_cache_enabled DataDatabricksNodeType#is_io_cache_enabled}.'''
        result = self._values.get("is_io_cache_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def local_disk(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#local_disk DataDatabricksNodeType#local_disk}.'''
        result = self._values.get("local_disk")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def local_disk_min_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#local_disk_min_size DataDatabricksNodeType#local_disk_min_size}.'''
        result = self._values.get("local_disk_min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_cores(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_cores DataDatabricksNodeType#min_cores}.'''
        result = self._values.get("min_cores")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_gpus(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_gpus DataDatabricksNodeType#min_gpus}.'''
        result = self._values.get("min_gpus")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_memory_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#min_memory_gb DataDatabricksNodeType#min_memory_gb}.'''
        result = self._values.get("min_memory_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def photon_driver_capable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#photon_driver_capable DataDatabricksNodeType#photon_driver_capable}.'''
        result = self._values.get("photon_driver_capable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def photon_worker_capable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#photon_worker_capable DataDatabricksNodeType#photon_worker_capable}.'''
        result = self._values.get("photon_worker_capable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def support_port_forwarding(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/d/node_type#support_port_forwarding DataDatabricksNodeType#support_port_forwarding}.'''
        result = self._values.get("support_port_forwarding")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataDatabricksNodeTypeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataDatabricksNodeType",
    "DataDatabricksNodeTypeConfig",
]

publication.publish()

def _typecheckingstub__ff334258931bef8460f15bd68cf621b3cc458c9abbad197370676ab0dfd99112(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    category: typing.Optional[builtins.str] = None,
    fleet: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    gb_per_core: typing.Optional[jsii.Number] = None,
    graviton: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    is_io_cache_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    local_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    local_disk_min_size: typing.Optional[jsii.Number] = None,
    min_cores: typing.Optional[jsii.Number] = None,
    min_gpus: typing.Optional[jsii.Number] = None,
    min_memory_gb: typing.Optional[jsii.Number] = None,
    photon_driver_capable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    photon_worker_capable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    support_port_forwarding: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__f47f7327e009d80c22c44547f9fecf10e76cf16da121b2bf6a8e79b7e384d1c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8ce1c140e25d45d988ea0138e41db8f2cb5eeb1e88cc8d0ffb573ddbf85abd9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04fbcb2e8b3980443c8bbf3019d3b86694c6648aa69b207d4e636dc5a29f4789(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c58e90e929525ccff2b66fcae41fcee5a360a73d074f7d69e66d0bb14fc9b9d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39e076cd2273b844e31a90865aadbbcf3c55a3ef2732c927fe5e84ac8044fa4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac23b0cc8f92450fbe14dd57044b7ed5d5fa257f96cef9e327787270e9562568(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2144d541a03234df63e609e537742342bf764a830e85d2fb5f718284581bbd7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cceb9ce7e997b0ecee1a51492e17c0cafa58f365d619812d9724fd222c823eb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e3c4b033d31d5da97d3d67704a52dc987ca7113e972b3ebc26455a938222337(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06490b570fded27be5dd1637e113daec483b3f762d9038ca266af8360d6c2d7e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54dd7e3a65cda402649bd35b79f28919f7c98bbc9f71f36f78cc177be1f7eed9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05c31abe8a764df69996b964697b338bfb9dd4f9c6f27a54149c10ae0f364ce2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb582704ecfdbda0409b50da0acc51e107f9b312f1665ab8d9ff53b06d1c07d2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52d4a0bd3e6ba79ac380ee40a3ec12625b2f4a5b4f548c21045bd5ffed1e3e5c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7abac7aa85fb70c6fd65e58407b4371b1a6315c1f84ba8688a430e5fb4533822(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    category: typing.Optional[builtins.str] = None,
    fleet: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    gb_per_core: typing.Optional[jsii.Number] = None,
    graviton: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    is_io_cache_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    local_disk: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    local_disk_min_size: typing.Optional[jsii.Number] = None,
    min_cores: typing.Optional[jsii.Number] = None,
    min_gpus: typing.Optional[jsii.Number] = None,
    min_memory_gb: typing.Optional[jsii.Number] = None,
    photon_driver_capable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    photon_worker_capable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    support_port_forwarding: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
