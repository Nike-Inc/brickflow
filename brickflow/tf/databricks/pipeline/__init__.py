'''
# `databricks_pipeline`

Refer to the Terraform Registory for docs: [`databricks_pipeline`](https://www.terraform.io/docs/providers/databricks/r/pipeline).
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


class Pipeline(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.Pipeline",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/pipeline databricks_pipeline}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        allow_duplicate_names: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        catalog: typing.Optional[builtins.str] = None,
        channel: typing.Optional[builtins.str] = None,
        cluster: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PipelineCluster", typing.Dict[builtins.str, typing.Any]]]]] = None,
        configuration: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        continuous: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        development: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        edition: typing.Optional[builtins.str] = None,
        filters: typing.Optional[typing.Union["PipelineFilters", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        library: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PipelineLibrary", typing.Dict[builtins.str, typing.Any]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        photon: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        storage: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["PipelineTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/pipeline databricks_pipeline} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param allow_duplicate_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#allow_duplicate_names Pipeline#allow_duplicate_names}.
        :param catalog: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#catalog Pipeline#catalog}.
        :param channel: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#channel Pipeline#channel}.
        :param cluster: cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#cluster Pipeline#cluster}
        :param configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#configuration Pipeline#configuration}.
        :param continuous: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#continuous Pipeline#continuous}.
        :param development: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#development Pipeline#development}.
        :param edition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#edition Pipeline#edition}.
        :param filters: filters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#filters Pipeline#filters}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#id Pipeline#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param library: library block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#library Pipeline#library}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#name Pipeline#name}.
        :param photon: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#photon Pipeline#photon}.
        :param storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#storage Pipeline#storage}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#target Pipeline#target}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#timeouts Pipeline#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd4075cee20ed6f4c4e22fc800294564ffb556867030df6002d73865896ee693)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PipelineConfig(
            allow_duplicate_names=allow_duplicate_names,
            catalog=catalog,
            channel=channel,
            cluster=cluster,
            configuration=configuration,
            continuous=continuous,
            development=development,
            edition=edition,
            filters=filters,
            id=id,
            library=library,
            name=name,
            photon=photon,
            storage=storage,
            target=target,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCluster")
    def put_cluster(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PipelineCluster", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39dde6cd11a73698eb6e4e34372941bc40274aa570790d69a32d962f7a8e9999)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCluster", [value]))

    @jsii.member(jsii_name="putFilters")
    def put_filters(
        self,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param exclude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#exclude Pipeline#exclude}.
        :param include: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#include Pipeline#include}.
        '''
        value = PipelineFilters(exclude=exclude, include=include)

        return typing.cast(None, jsii.invoke(self, "putFilters", [value]))

    @jsii.member(jsii_name="putLibrary")
    def put_library(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PipelineLibrary", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a8eafb67f259cb5e92097a5e4f2e23bdf17d04bef1e1b345edfa4297f29cd04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLibrary", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#default Pipeline#default}.
        '''
        value = PipelineTimeouts(default=default)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAllowDuplicateNames")
    def reset_allow_duplicate_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowDuplicateNames", []))

    @jsii.member(jsii_name="resetCatalog")
    def reset_catalog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalog", []))

    @jsii.member(jsii_name="resetChannel")
    def reset_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChannel", []))

    @jsii.member(jsii_name="resetCluster")
    def reset_cluster(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCluster", []))

    @jsii.member(jsii_name="resetConfiguration")
    def reset_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfiguration", []))

    @jsii.member(jsii_name="resetContinuous")
    def reset_continuous(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContinuous", []))

    @jsii.member(jsii_name="resetDevelopment")
    def reset_development(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDevelopment", []))

    @jsii.member(jsii_name="resetEdition")
    def reset_edition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEdition", []))

    @jsii.member(jsii_name="resetFilters")
    def reset_filters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilters", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLibrary")
    def reset_library(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLibrary", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPhoton")
    def reset_photon(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhoton", []))

    @jsii.member(jsii_name="resetStorage")
    def reset_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorage", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> "PipelineClusterList":
        return typing.cast("PipelineClusterList", jsii.get(self, "cluster"))

    @builtins.property
    @jsii.member(jsii_name="filters")
    def filters(self) -> "PipelineFiltersOutputReference":
        return typing.cast("PipelineFiltersOutputReference", jsii.get(self, "filters"))

    @builtins.property
    @jsii.member(jsii_name="library")
    def library(self) -> "PipelineLibraryList":
        return typing.cast("PipelineLibraryList", jsii.get(self, "library"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "PipelineTimeoutsOutputReference":
        return typing.cast("PipelineTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="allowDuplicateNamesInput")
    def allow_duplicate_names_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowDuplicateNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogInput")
    def catalog_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogInput"))

    @builtins.property
    @jsii.member(jsii_name="channelInput")
    def channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterInput")
    def cluster_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PipelineCluster"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PipelineCluster"]]], jsii.get(self, "clusterInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationInput")
    def configuration_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "configurationInput"))

    @builtins.property
    @jsii.member(jsii_name="continuousInput")
    def continuous_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "continuousInput"))

    @builtins.property
    @jsii.member(jsii_name="developmentInput")
    def development_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "developmentInput"))

    @builtins.property
    @jsii.member(jsii_name="editionInput")
    def edition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "editionInput"))

    @builtins.property
    @jsii.member(jsii_name="filtersInput")
    def filters_input(self) -> typing.Optional["PipelineFilters"]:
        return typing.cast(typing.Optional["PipelineFilters"], jsii.get(self, "filtersInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="libraryInput")
    def library_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PipelineLibrary"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PipelineLibrary"]]], jsii.get(self, "libraryInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="photonInput")
    def photon_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "photonInput"))

    @builtins.property
    @jsii.member(jsii_name="storageInput")
    def storage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["PipelineTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["PipelineTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowDuplicateNames")
    def allow_duplicate_names(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowDuplicateNames"))

    @allow_duplicate_names.setter
    def allow_duplicate_names(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4649b808855fc680808bf4cbc9f0470127bb4d70bf1ccb6f972e4b82c9ec7a39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowDuplicateNames", value)

    @builtins.property
    @jsii.member(jsii_name="catalog")
    def catalog(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalog"))

    @catalog.setter
    def catalog(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbab7232bdd9b57c48bed8fe7afaa76bfea1416e8a79124b8b06c735e4c42680)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalog", value)

    @builtins.property
    @jsii.member(jsii_name="channel")
    def channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channel"))

    @channel.setter
    def channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5a3b6b3e69a428aad2fd4ee675ee598b64d58723686ff73a4279f82d894278d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channel", value)

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89f8d281b8ee6de08c6213c306372c17ef9f4e49598be12997e475b01c484c19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value)

    @builtins.property
    @jsii.member(jsii_name="continuous")
    def continuous(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "continuous"))

    @continuous.setter
    def continuous(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__178b299c31a874d2bcfd3ed03fb052eea218a678e88ccd9b85a3d7d1fd0522de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "continuous", value)

    @builtins.property
    @jsii.member(jsii_name="development")
    def development(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "development"))

    @development.setter
    def development(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adf94353028dc4ed3867b4fd380e1f8ed272bf30123ed8067ce0649fdb848711)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "development", value)

    @builtins.property
    @jsii.member(jsii_name="edition")
    def edition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "edition"))

    @edition.setter
    def edition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34e458cf24db6e90404c8086d653aff50023484fa7652a7d0d8f3f6e46551fb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edition", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0492ae7fcd38d39b9f59985669ade0fca372b3e5c41b0e348c6b71f39997932)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bacedfc8557e305856ceeedeaf82a96c7100d6afc97c0a4603f071800a4c809)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="photon")
    def photon(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "photon"))

    @photon.setter
    def photon(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bba47cdc47c438d856c3dd35a0beb1ad8dd5c7b6b95feb8acf9e48cf0a04f9a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "photon", value)

    @builtins.property
    @jsii.member(jsii_name="storage")
    def storage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storage"))

    @storage.setter
    def storage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66cc30ffd33cf9eace27280d5d360cfeb1f76ee56af93277bbae17f73d07742f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storage", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d31123f8955aaf33cd94f8f948975f3ff6ce841beb9b0381665da515f6a2a87a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineCluster",
    jsii_struct_bases=[],
    name_mapping={
        "apply_policy_default_values": "applyPolicyDefaultValues",
        "autoscale": "autoscale",
        "aws_attributes": "awsAttributes",
        "azure_attributes": "azureAttributes",
        "cluster_log_conf": "clusterLogConf",
        "custom_tags": "customTags",
        "driver_instance_pool_id": "driverInstancePoolId",
        "driver_node_type_id": "driverNodeTypeId",
        "enable_local_disk_encryption": "enableLocalDiskEncryption",
        "gcp_attributes": "gcpAttributes",
        "init_scripts": "initScripts",
        "instance_pool_id": "instancePoolId",
        "label": "label",
        "node_type_id": "nodeTypeId",
        "num_workers": "numWorkers",
        "policy_id": "policyId",
        "spark_conf": "sparkConf",
        "spark_env_vars": "sparkEnvVars",
        "ssh_public_keys": "sshPublicKeys",
    },
)
class PipelineCluster:
    def __init__(
        self,
        *,
        apply_policy_default_values: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        autoscale: typing.Optional[typing.Union["PipelineClusterAutoscale", typing.Dict[builtins.str, typing.Any]]] = None,
        aws_attributes: typing.Optional[typing.Union["PipelineClusterAwsAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        azure_attributes: typing.Optional[typing.Union["PipelineClusterAzureAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_log_conf: typing.Optional[typing.Union["PipelineClusterClusterLogConf", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        driver_instance_pool_id: typing.Optional[builtins.str] = None,
        driver_node_type_id: typing.Optional[builtins.str] = None,
        enable_local_disk_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        gcp_attributes: typing.Optional[typing.Union["PipelineClusterGcpAttributes", typing.Dict[builtins.str, typing.Any]]] = None,
        init_scripts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PipelineClusterInitScripts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        instance_pool_id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        node_type_id: typing.Optional[builtins.str] = None,
        num_workers: typing.Optional[jsii.Number] = None,
        policy_id: typing.Optional[builtins.str] = None,
        spark_conf: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        spark_env_vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param apply_policy_default_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#apply_policy_default_values Pipeline#apply_policy_default_values}.
        :param autoscale: autoscale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#autoscale Pipeline#autoscale}
        :param aws_attributes: aws_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#aws_attributes Pipeline#aws_attributes}
        :param azure_attributes: azure_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#azure_attributes Pipeline#azure_attributes}
        :param cluster_log_conf: cluster_log_conf block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#cluster_log_conf Pipeline#cluster_log_conf}
        :param custom_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#custom_tags Pipeline#custom_tags}.
        :param driver_instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#driver_instance_pool_id Pipeline#driver_instance_pool_id}.
        :param driver_node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#driver_node_type_id Pipeline#driver_node_type_id}.
        :param enable_local_disk_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#enable_local_disk_encryption Pipeline#enable_local_disk_encryption}.
        :param gcp_attributes: gcp_attributes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#gcp_attributes Pipeline#gcp_attributes}
        :param init_scripts: init_scripts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#init_scripts Pipeline#init_scripts}
        :param instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#instance_pool_id Pipeline#instance_pool_id}.
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#label Pipeline#label}.
        :param node_type_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#node_type_id Pipeline#node_type_id}.
        :param num_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#num_workers Pipeline#num_workers}.
        :param policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#policy_id Pipeline#policy_id}.
        :param spark_conf: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#spark_conf Pipeline#spark_conf}.
        :param spark_env_vars: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#spark_env_vars Pipeline#spark_env_vars}.
        :param ssh_public_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#ssh_public_keys Pipeline#ssh_public_keys}.
        '''
        if isinstance(autoscale, dict):
            autoscale = PipelineClusterAutoscale(**autoscale)
        if isinstance(aws_attributes, dict):
            aws_attributes = PipelineClusterAwsAttributes(**aws_attributes)
        if isinstance(azure_attributes, dict):
            azure_attributes = PipelineClusterAzureAttributes(**azure_attributes)
        if isinstance(cluster_log_conf, dict):
            cluster_log_conf = PipelineClusterClusterLogConf(**cluster_log_conf)
        if isinstance(gcp_attributes, dict):
            gcp_attributes = PipelineClusterGcpAttributes(**gcp_attributes)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68d3dbd3f224aeca0068c3ab93e02b1fd555709ae155e349bc21ead9e346714a)
            check_type(argname="argument apply_policy_default_values", value=apply_policy_default_values, expected_type=type_hints["apply_policy_default_values"])
            check_type(argname="argument autoscale", value=autoscale, expected_type=type_hints["autoscale"])
            check_type(argname="argument aws_attributes", value=aws_attributes, expected_type=type_hints["aws_attributes"])
            check_type(argname="argument azure_attributes", value=azure_attributes, expected_type=type_hints["azure_attributes"])
            check_type(argname="argument cluster_log_conf", value=cluster_log_conf, expected_type=type_hints["cluster_log_conf"])
            check_type(argname="argument custom_tags", value=custom_tags, expected_type=type_hints["custom_tags"])
            check_type(argname="argument driver_instance_pool_id", value=driver_instance_pool_id, expected_type=type_hints["driver_instance_pool_id"])
            check_type(argname="argument driver_node_type_id", value=driver_node_type_id, expected_type=type_hints["driver_node_type_id"])
            check_type(argname="argument enable_local_disk_encryption", value=enable_local_disk_encryption, expected_type=type_hints["enable_local_disk_encryption"])
            check_type(argname="argument gcp_attributes", value=gcp_attributes, expected_type=type_hints["gcp_attributes"])
            check_type(argname="argument init_scripts", value=init_scripts, expected_type=type_hints["init_scripts"])
            check_type(argname="argument instance_pool_id", value=instance_pool_id, expected_type=type_hints["instance_pool_id"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument node_type_id", value=node_type_id, expected_type=type_hints["node_type_id"])
            check_type(argname="argument num_workers", value=num_workers, expected_type=type_hints["num_workers"])
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
            check_type(argname="argument spark_conf", value=spark_conf, expected_type=type_hints["spark_conf"])
            check_type(argname="argument spark_env_vars", value=spark_env_vars, expected_type=type_hints["spark_env_vars"])
            check_type(argname="argument ssh_public_keys", value=ssh_public_keys, expected_type=type_hints["ssh_public_keys"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if apply_policy_default_values is not None:
            self._values["apply_policy_default_values"] = apply_policy_default_values
        if autoscale is not None:
            self._values["autoscale"] = autoscale
        if aws_attributes is not None:
            self._values["aws_attributes"] = aws_attributes
        if azure_attributes is not None:
            self._values["azure_attributes"] = azure_attributes
        if cluster_log_conf is not None:
            self._values["cluster_log_conf"] = cluster_log_conf
        if custom_tags is not None:
            self._values["custom_tags"] = custom_tags
        if driver_instance_pool_id is not None:
            self._values["driver_instance_pool_id"] = driver_instance_pool_id
        if driver_node_type_id is not None:
            self._values["driver_node_type_id"] = driver_node_type_id
        if enable_local_disk_encryption is not None:
            self._values["enable_local_disk_encryption"] = enable_local_disk_encryption
        if gcp_attributes is not None:
            self._values["gcp_attributes"] = gcp_attributes
        if init_scripts is not None:
            self._values["init_scripts"] = init_scripts
        if instance_pool_id is not None:
            self._values["instance_pool_id"] = instance_pool_id
        if label is not None:
            self._values["label"] = label
        if node_type_id is not None:
            self._values["node_type_id"] = node_type_id
        if num_workers is not None:
            self._values["num_workers"] = num_workers
        if policy_id is not None:
            self._values["policy_id"] = policy_id
        if spark_conf is not None:
            self._values["spark_conf"] = spark_conf
        if spark_env_vars is not None:
            self._values["spark_env_vars"] = spark_env_vars
        if ssh_public_keys is not None:
            self._values["ssh_public_keys"] = ssh_public_keys

    @builtins.property
    def apply_policy_default_values(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#apply_policy_default_values Pipeline#apply_policy_default_values}.'''
        result = self._values.get("apply_policy_default_values")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def autoscale(self) -> typing.Optional["PipelineClusterAutoscale"]:
        '''autoscale block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#autoscale Pipeline#autoscale}
        '''
        result = self._values.get("autoscale")
        return typing.cast(typing.Optional["PipelineClusterAutoscale"], result)

    @builtins.property
    def aws_attributes(self) -> typing.Optional["PipelineClusterAwsAttributes"]:
        '''aws_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#aws_attributes Pipeline#aws_attributes}
        '''
        result = self._values.get("aws_attributes")
        return typing.cast(typing.Optional["PipelineClusterAwsAttributes"], result)

    @builtins.property
    def azure_attributes(self) -> typing.Optional["PipelineClusterAzureAttributes"]:
        '''azure_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#azure_attributes Pipeline#azure_attributes}
        '''
        result = self._values.get("azure_attributes")
        return typing.cast(typing.Optional["PipelineClusterAzureAttributes"], result)

    @builtins.property
    def cluster_log_conf(self) -> typing.Optional["PipelineClusterClusterLogConf"]:
        '''cluster_log_conf block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#cluster_log_conf Pipeline#cluster_log_conf}
        '''
        result = self._values.get("cluster_log_conf")
        return typing.cast(typing.Optional["PipelineClusterClusterLogConf"], result)

    @builtins.property
    def custom_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#custom_tags Pipeline#custom_tags}.'''
        result = self._values.get("custom_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def driver_instance_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#driver_instance_pool_id Pipeline#driver_instance_pool_id}.'''
        result = self._values.get("driver_instance_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def driver_node_type_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#driver_node_type_id Pipeline#driver_node_type_id}.'''
        result = self._values.get("driver_node_type_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_local_disk_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#enable_local_disk_encryption Pipeline#enable_local_disk_encryption}.'''
        result = self._values.get("enable_local_disk_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def gcp_attributes(self) -> typing.Optional["PipelineClusterGcpAttributes"]:
        '''gcp_attributes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#gcp_attributes Pipeline#gcp_attributes}
        '''
        result = self._values.get("gcp_attributes")
        return typing.cast(typing.Optional["PipelineClusterGcpAttributes"], result)

    @builtins.property
    def init_scripts(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PipelineClusterInitScripts"]]]:
        '''init_scripts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#init_scripts Pipeline#init_scripts}
        '''
        result = self._values.get("init_scripts")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PipelineClusterInitScripts"]]], result)

    @builtins.property
    def instance_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#instance_pool_id Pipeline#instance_pool_id}.'''
        result = self._values.get("instance_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#label Pipeline#label}.'''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_type_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#node_type_id Pipeline#node_type_id}.'''
        result = self._values.get("node_type_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#num_workers Pipeline#num_workers}.'''
        result = self._values.get("num_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def policy_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#policy_id Pipeline#policy_id}.'''
        result = self._values.get("policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spark_conf(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#spark_conf Pipeline#spark_conf}.'''
        result = self._values.get("spark_conf")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def spark_env_vars(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#spark_env_vars Pipeline#spark_env_vars}.'''
        result = self._values.get("spark_env_vars")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def ssh_public_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#ssh_public_keys Pipeline#ssh_public_keys}.'''
        result = self._values.get("ssh_public_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineCluster(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineClusterAutoscale",
    jsii_struct_bases=[],
    name_mapping={
        "max_workers": "maxWorkers",
        "min_workers": "minWorkers",
        "mode": "mode",
    },
)
class PipelineClusterAutoscale:
    def __init__(
        self,
        *,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
        mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#max_workers Pipeline#max_workers}.
        :param min_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#min_workers Pipeline#min_workers}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#mode Pipeline#mode}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac34603de0ecea33f76dbb535b2a4cdb34422babdbba1a76b4ce6a092ec7de46)
            check_type(argname="argument max_workers", value=max_workers, expected_type=type_hints["max_workers"])
            check_type(argname="argument min_workers", value=min_workers, expected_type=type_hints["min_workers"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max_workers is not None:
            self._values["max_workers"] = max_workers
        if min_workers is not None:
            self._values["min_workers"] = min_workers
        if mode is not None:
            self._values["mode"] = mode

    @builtins.property
    def max_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#max_workers Pipeline#max_workers}.'''
        result = self._values.get("max_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#min_workers Pipeline#min_workers}.'''
        result = self._values.get("min_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#mode Pipeline#mode}.'''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineClusterAutoscale(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineClusterAutoscaleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineClusterAutoscaleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__34875dcef21db0b17c8cbdb94c21658cecb0685d7b36ad2ce70869b60fe35317)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxWorkers")
    def reset_max_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxWorkers", []))

    @jsii.member(jsii_name="resetMinWorkers")
    def reset_min_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinWorkers", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @builtins.property
    @jsii.member(jsii_name="maxWorkersInput")
    def max_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="minWorkersInput")
    def min_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWorkers")
    def max_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxWorkers"))

    @max_workers.setter
    def max_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7bb7cbf261c60fa54d3a7cb1da6eb3e29dc90bc934ce39bcddcd1c1d5f6b599)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="minWorkers")
    def min_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minWorkers"))

    @min_workers.setter
    def min_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e95cae38322cd180092a459ca9e2feec9afa7de0d0ce1285195bd08fbd2d923)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__282b2270e343de41bba32576029b32ad2f74d9ed44b35d5c3c0b732cd0009c92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PipelineClusterAutoscale]:
        return typing.cast(typing.Optional[PipelineClusterAutoscale], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PipelineClusterAutoscale]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de281bf42ad3fbcd0f79740d737971b86e9002fae45672fe3783e6a5df9cc2fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineClusterAwsAttributes",
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
class PipelineClusterAwsAttributes:
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
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#availability Pipeline#availability}.
        :param ebs_volume_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#ebs_volume_count Pipeline#ebs_volume_count}.
        :param ebs_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#ebs_volume_size Pipeline#ebs_volume_size}.
        :param ebs_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#ebs_volume_type Pipeline#ebs_volume_type}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#first_on_demand Pipeline#first_on_demand}.
        :param instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#instance_profile_arn Pipeline#instance_profile_arn}.
        :param spot_bid_price_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#spot_bid_price_percent Pipeline#spot_bid_price_percent}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#zone_id Pipeline#zone_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8448d88610d716872b148022875a285b9d5ef32c4473632bb42e48bd9c6150cf)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#availability Pipeline#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_volume_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#ebs_volume_count Pipeline#ebs_volume_count}.'''
        result = self._values.get("ebs_volume_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ebs_volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#ebs_volume_size Pipeline#ebs_volume_size}.'''
        result = self._values.get("ebs_volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ebs_volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#ebs_volume_type Pipeline#ebs_volume_type}.'''
        result = self._values.get("ebs_volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_on_demand(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#first_on_demand Pipeline#first_on_demand}.'''
        result = self._values.get("first_on_demand")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#instance_profile_arn Pipeline#instance_profile_arn}.'''
        result = self._values.get("instance_profile_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_bid_price_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#spot_bid_price_percent Pipeline#spot_bid_price_percent}.'''
        result = self._values.get("spot_bid_price_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#zone_id Pipeline#zone_id}.'''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineClusterAwsAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineClusterAwsAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineClusterAwsAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__04cebc34c0e073707f6d694a7843a676c105d9274d63cd7959ebaec74463817e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__750fae0bb4310a24c6e63613b85b6edd5c24a5c22272c16d37888eff5495101f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeCount")
    def ebs_volume_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsVolumeCount"))

    @ebs_volume_count.setter
    def ebs_volume_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d7d794def4f9845d4a9da44af9251c2bbb9d9f966a6a92e3b47e5bfdb6c3e6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeCount", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeSize")
    def ebs_volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ebsVolumeSize"))

    @ebs_volume_size.setter
    def ebs_volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__408f5724223715144ee0b88394dd3d9637dc26b35ee6a833bf901cb4d1c9e29e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="ebsVolumeType")
    def ebs_volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ebsVolumeType"))

    @ebs_volume_type.setter
    def ebs_volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1d92d3a986a2e842b8e487c8fcbedeceaf3abcb2b8e30a0641f53a598d82df3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsVolumeType", value)

    @builtins.property
    @jsii.member(jsii_name="firstOnDemand")
    def first_on_demand(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "firstOnDemand"))

    @first_on_demand.setter
    def first_on_demand(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcfc9c1c991c22e79a09fa94e0fdc3de4079715e0ad46a92823428e218e7f014)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstOnDemand", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfileArn")
    def instance_profile_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceProfileArn"))

    @instance_profile_arn.setter
    def instance_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f75177a5d06e510a12180a5703cf53717740de8c11d899ab0cc93e99b77f4d7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="spotBidPricePercent")
    def spot_bid_price_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotBidPricePercent"))

    @spot_bid_price_percent.setter
    def spot_bid_price_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8597f5bbf395aeb1430d35a7749689b490178dca3aebd079d9de8b8660580e97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotBidPricePercent", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86b82369d4c4ad3b6ae08c616dd536d5763bc9b853f4f0772eda2678bab93681)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PipelineClusterAwsAttributes]:
        return typing.cast(typing.Optional[PipelineClusterAwsAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PipelineClusterAwsAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e8bc568ff97cb23480fd1f8e2a5fb4a81d19767fe240bb0bf4c6ece3bd0aa2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineClusterAzureAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "first_on_demand": "firstOnDemand",
        "spot_bid_max_price": "spotBidMaxPrice",
    },
)
class PipelineClusterAzureAttributes:
    def __init__(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        first_on_demand: typing.Optional[jsii.Number] = None,
        spot_bid_max_price: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#availability Pipeline#availability}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#first_on_demand Pipeline#first_on_demand}.
        :param spot_bid_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#spot_bid_max_price Pipeline#spot_bid_max_price}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1ad13a4411d368bff446b879633a5a481c33de619837511f5907d211fa4a5be)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#availability Pipeline#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def first_on_demand(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#first_on_demand Pipeline#first_on_demand}.'''
        result = self._values.get("first_on_demand")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def spot_bid_max_price(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#spot_bid_max_price Pipeline#spot_bid_max_price}.'''
        result = self._values.get("spot_bid_max_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineClusterAzureAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineClusterAzureAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineClusterAzureAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__95d82b5fee246740a47492f5ae4a3d9f8b54ce10fd5b70aee1647c056577416e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f612fd3a40472541e8af626b98192f2bdf9a45ca52666df3e494e6ce697a2709)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="firstOnDemand")
    def first_on_demand(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "firstOnDemand"))

    @first_on_demand.setter
    def first_on_demand(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96e7d28fe6b4acf4627704280964ce18c032ab5ac1abbea5cffeee4238aa609f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firstOnDemand", value)

    @builtins.property
    @jsii.member(jsii_name="spotBidMaxPrice")
    def spot_bid_max_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "spotBidMaxPrice"))

    @spot_bid_max_price.setter
    def spot_bid_max_price(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3196f82d2c58bb796537400456d6a10c25eabd1c57936d456937211c88f8775c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotBidMaxPrice", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PipelineClusterAzureAttributes]:
        return typing.cast(typing.Optional[PipelineClusterAzureAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PipelineClusterAzureAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9f6523ab29403fc0f756e7672c1589a60c021e7f01e5668086633fbbc8070b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineClusterClusterLogConf",
    jsii_struct_bases=[],
    name_mapping={"dbfs": "dbfs", "s3": "s3"},
)
class PipelineClusterClusterLogConf:
    def __init__(
        self,
        *,
        dbfs: typing.Optional[typing.Union["PipelineClusterClusterLogConfDbfs", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["PipelineClusterClusterLogConfS3", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dbfs: dbfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#dbfs Pipeline#dbfs}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#s3 Pipeline#s3}
        '''
        if isinstance(dbfs, dict):
            dbfs = PipelineClusterClusterLogConfDbfs(**dbfs)
        if isinstance(s3, dict):
            s3 = PipelineClusterClusterLogConfS3(**s3)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e818fe1ba5c340172aa5fdd17eb61fa872ad290f10accd89987cf57da0c03dc0)
            check_type(argname="argument dbfs", value=dbfs, expected_type=type_hints["dbfs"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dbfs is not None:
            self._values["dbfs"] = dbfs
        if s3 is not None:
            self._values["s3"] = s3

    @builtins.property
    def dbfs(self) -> typing.Optional["PipelineClusterClusterLogConfDbfs"]:
        '''dbfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#dbfs Pipeline#dbfs}
        '''
        result = self._values.get("dbfs")
        return typing.cast(typing.Optional["PipelineClusterClusterLogConfDbfs"], result)

    @builtins.property
    def s3(self) -> typing.Optional["PipelineClusterClusterLogConfS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#s3 Pipeline#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["PipelineClusterClusterLogConfS3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineClusterClusterLogConf(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineClusterClusterLogConfDbfs",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class PipelineClusterClusterLogConfDbfs:
    def __init__(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1de909e645f8e2f3235ae7e84866fe85748e966e9f62424b0197354703e8cd78)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineClusterClusterLogConfDbfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineClusterClusterLogConfDbfsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineClusterClusterLogConfDbfsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__afd381da0ec83fe63aedf553cd5fc443b235e8b501858eb9b3bf418f5ce7fa7d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b72d6bb438c93f22060891a6c9a726832045cb565a0974a9cce1fbeadf8decf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PipelineClusterClusterLogConfDbfs]:
        return typing.cast(typing.Optional[PipelineClusterClusterLogConfDbfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PipelineClusterClusterLogConfDbfs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b9ea921fd8b9a60253c6204ad04a478ed2fd604de173d680c0bf78b46fe3e4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PipelineClusterClusterLogConfOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineClusterClusterLogConfOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6059d973a5573dd4b21b7de3210135a2300fe5927265a0af53c8dfac66751982)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDbfs")
    def put_dbfs(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.
        '''
        value = PipelineClusterClusterLogConfDbfs(destination=destination)

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
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#canned_acl Pipeline#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#enable_encryption Pipeline#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#encryption_type Pipeline#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#endpoint Pipeline#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#kms_key Pipeline#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#region Pipeline#region}.
        '''
        value = PipelineClusterClusterLogConfS3(
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
    def dbfs(self) -> PipelineClusterClusterLogConfDbfsOutputReference:
        return typing.cast(PipelineClusterClusterLogConfDbfsOutputReference, jsii.get(self, "dbfs"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "PipelineClusterClusterLogConfS3OutputReference":
        return typing.cast("PipelineClusterClusterLogConfS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="dbfsInput")
    def dbfs_input(self) -> typing.Optional[PipelineClusterClusterLogConfDbfs]:
        return typing.cast(typing.Optional[PipelineClusterClusterLogConfDbfs], jsii.get(self, "dbfsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(self) -> typing.Optional["PipelineClusterClusterLogConfS3"]:
        return typing.cast(typing.Optional["PipelineClusterClusterLogConfS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PipelineClusterClusterLogConf]:
        return typing.cast(typing.Optional[PipelineClusterClusterLogConf], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PipelineClusterClusterLogConf],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc004b6fe12fb908e4c4bc48a111e566afbb7338613f7c2cb1d86c75fad97cca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineClusterClusterLogConfS3",
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
class PipelineClusterClusterLogConfS3:
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
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#canned_acl Pipeline#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#enable_encryption Pipeline#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#encryption_type Pipeline#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#endpoint Pipeline#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#kms_key Pipeline#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#region Pipeline#region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1f54af77a9959e9f7dc7e851f5f6cd7ac033e4946777a4e12bf0290492ba020)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def canned_acl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#canned_acl Pipeline#canned_acl}.'''
        result = self._values.get("canned_acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#enable_encryption Pipeline#enable_encryption}.'''
        result = self._values.get("enable_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encryption_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#encryption_type Pipeline#encryption_type}.'''
        result = self._values.get("encryption_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#endpoint Pipeline#endpoint}.'''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#kms_key Pipeline#kms_key}.'''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#region Pipeline#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineClusterClusterLogConfS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineClusterClusterLogConfS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineClusterClusterLogConfS3OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea527b4c22975ff7e1961f390d6c070f27b22595a9af40cff3ce66acbb880bf0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__09eedfd34f79d757e0049a6ae5dacc4acc33f13df773f6155714a6e7b5715bba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cannedAcl", value)

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0659abadfb971de3697d1fcbb74c0b9240e652dcd180d1cdabd85868aaed6c9e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f872f1c9768844f492adaf29f8d5eab7a3861439b13536e7636a5b5b03661b6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionType")
    def encryption_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionType"))

    @encryption_type.setter
    def encryption_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0d3e138188ef48ebcd45dfe83ce5627182e36840e7905328b5c40dde752e1c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f63bdf195d98464b452a2c5e0aba73b609b8d48030879610f8e4b66a6fac54c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__069c23796879870274723d690d533000f6ed4b2e94b8504781d2b429be0ae168)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9398ed6f675e7994e3f223cc108b3bc514ee51574c97552d66fad52ff61d184a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PipelineClusterClusterLogConfS3]:
        return typing.cast(typing.Optional[PipelineClusterClusterLogConfS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PipelineClusterClusterLogConfS3],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__298b31792285d585f40fcb031067ddef545097a485f12333b61582566afd4fbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineClusterGcpAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "availability": "availability",
        "google_service_account": "googleServiceAccount",
        "zone_id": "zoneId",
    },
)
class PipelineClusterGcpAttributes:
    def __init__(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        google_service_account: typing.Optional[builtins.str] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#availability Pipeline#availability}.
        :param google_service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#google_service_account Pipeline#google_service_account}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#zone_id Pipeline#zone_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ce71244c3cedb4628281f54806de708e24b055ce57a0c7fe4359d98560ab79d)
            check_type(argname="argument availability", value=availability, expected_type=type_hints["availability"])
            check_type(argname="argument google_service_account", value=google_service_account, expected_type=type_hints["google_service_account"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability is not None:
            self._values["availability"] = availability
        if google_service_account is not None:
            self._values["google_service_account"] = google_service_account
        if zone_id is not None:
            self._values["zone_id"] = zone_id

    @builtins.property
    def availability(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#availability Pipeline#availability}.'''
        result = self._values.get("availability")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def google_service_account(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#google_service_account Pipeline#google_service_account}.'''
        result = self._values.get("google_service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#zone_id Pipeline#zone_id}.'''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineClusterGcpAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineClusterGcpAttributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineClusterGcpAttributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac4f4a53cbd2c91d7b06cb8de99ffb3e2c6012fb5a4d4e51eb1045354e1fdfa6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAvailability")
    def reset_availability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailability", []))

    @jsii.member(jsii_name="resetGoogleServiceAccount")
    def reset_google_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleServiceAccount", []))

    @jsii.member(jsii_name="resetZoneId")
    def reset_zone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneId", []))

    @builtins.property
    @jsii.member(jsii_name="availabilityInput")
    def availability_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="googleServiceAccountInput")
    def google_service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleServiceAccountInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__0dba14cd406ce22c9c069c05363ddfdb8eea310f3f3c2f662b6ab16091e5dbf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availability", value)

    @builtins.property
    @jsii.member(jsii_name="googleServiceAccount")
    def google_service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "googleServiceAccount"))

    @google_service_account.setter
    def google_service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d295f2f8ab1381da7a14b58d065ccff6e28cc18d407e1590e1e42d5d10bcfd9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "googleServiceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcd9074dacf53ba7638fb2e762f111dee8244f182d815c91c99dbf2f9ad8ef36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PipelineClusterGcpAttributes]:
        return typing.cast(typing.Optional[PipelineClusterGcpAttributes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PipelineClusterGcpAttributes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc48bceaca024d42ac70b1660922eba635018550fc07f7b87574545c78ccbcc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineClusterInitScripts",
    jsii_struct_bases=[],
    name_mapping={
        "abfss": "abfss",
        "dbfs": "dbfs",
        "file": "file",
        "gcs": "gcs",
        "s3": "s3",
    },
)
class PipelineClusterInitScripts:
    def __init__(
        self,
        *,
        abfss: typing.Optional[typing.Union["PipelineClusterInitScriptsAbfss", typing.Dict[builtins.str, typing.Any]]] = None,
        dbfs: typing.Optional[typing.Union["PipelineClusterInitScriptsDbfs", typing.Dict[builtins.str, typing.Any]]] = None,
        file: typing.Optional[typing.Union["PipelineClusterInitScriptsFile", typing.Dict[builtins.str, typing.Any]]] = None,
        gcs: typing.Optional[typing.Union["PipelineClusterInitScriptsGcs", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["PipelineClusterInitScriptsS3", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param abfss: abfss block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#abfss Pipeline#abfss}
        :param dbfs: dbfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#dbfs Pipeline#dbfs}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#file Pipeline#file}
        :param gcs: gcs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#gcs Pipeline#gcs}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#s3 Pipeline#s3}
        '''
        if isinstance(abfss, dict):
            abfss = PipelineClusterInitScriptsAbfss(**abfss)
        if isinstance(dbfs, dict):
            dbfs = PipelineClusterInitScriptsDbfs(**dbfs)
        if isinstance(file, dict):
            file = PipelineClusterInitScriptsFile(**file)
        if isinstance(gcs, dict):
            gcs = PipelineClusterInitScriptsGcs(**gcs)
        if isinstance(s3, dict):
            s3 = PipelineClusterInitScriptsS3(**s3)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11e4f70e64acf28604292dab99ebb77aeaf3f7e158e06a513fc7b02051b07051)
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
    def abfss(self) -> typing.Optional["PipelineClusterInitScriptsAbfss"]:
        '''abfss block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#abfss Pipeline#abfss}
        '''
        result = self._values.get("abfss")
        return typing.cast(typing.Optional["PipelineClusterInitScriptsAbfss"], result)

    @builtins.property
    def dbfs(self) -> typing.Optional["PipelineClusterInitScriptsDbfs"]:
        '''dbfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#dbfs Pipeline#dbfs}
        '''
        result = self._values.get("dbfs")
        return typing.cast(typing.Optional["PipelineClusterInitScriptsDbfs"], result)

    @builtins.property
    def file(self) -> typing.Optional["PipelineClusterInitScriptsFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#file Pipeline#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["PipelineClusterInitScriptsFile"], result)

    @builtins.property
    def gcs(self) -> typing.Optional["PipelineClusterInitScriptsGcs"]:
        '''gcs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#gcs Pipeline#gcs}
        '''
        result = self._values.get("gcs")
        return typing.cast(typing.Optional["PipelineClusterInitScriptsGcs"], result)

    @builtins.property
    def s3(self) -> typing.Optional["PipelineClusterInitScriptsS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#s3 Pipeline#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["PipelineClusterInitScriptsS3"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineClusterInitScripts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineClusterInitScriptsAbfss",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class PipelineClusterInitScriptsAbfss:
    def __init__(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08653553c412d16cc3c394e902d9d9136e1dc270400d97f53c4da3176f9cf921)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.'''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineClusterInitScriptsAbfss(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineClusterInitScriptsAbfssOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineClusterInitScriptsAbfssOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__185005a57a242c57b50ff8e2a4ac3ad2b94c3e5b38e46f1164ef3379fbbe15bb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2a2f6a45a0d69358944833d6f2782c267d91f62914c38a9a0d2fdafbadddf8cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PipelineClusterInitScriptsAbfss]:
        return typing.cast(typing.Optional[PipelineClusterInitScriptsAbfss], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PipelineClusterInitScriptsAbfss],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96427f8ce89f814bd5be8778b1332d7028c186c709b765e73382a0ed77ba48eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineClusterInitScriptsDbfs",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class PipelineClusterInitScriptsDbfs:
    def __init__(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5533972c2f5a5cac1bd2d4a983973d0cd6b9a3b177dc7131d51216e38c2bd072)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineClusterInitScriptsDbfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineClusterInitScriptsDbfsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineClusterInitScriptsDbfsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__448d6322b8835791794b355fa15b3606a7b4eb170516cfc11f4b5076d1960492)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b58e948cd446d5feb362c7047abda18a12ba88f1047abb9bee05e0a976af25ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PipelineClusterInitScriptsDbfs]:
        return typing.cast(typing.Optional[PipelineClusterInitScriptsDbfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PipelineClusterInitScriptsDbfs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccb509849d53df64fb76f3d6a87b6ae85c070cca9a2b91322ab23274e9239b7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineClusterInitScriptsFile",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class PipelineClusterInitScriptsFile:
    def __init__(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e4363a82d617cbd23354845694dd6c1a276a3cb1c9f9d7026cb8690d1df2c4f)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.'''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineClusterInitScriptsFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineClusterInitScriptsFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineClusterInitScriptsFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__86457c0c1b2c9138116d12c1363dfd74763edf426aa2deb316f55368908f3190)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c47880aabfde119a139292f7cbeae09d4cdc3ec3ebe9a84a7b9327426a63495)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PipelineClusterInitScriptsFile]:
        return typing.cast(typing.Optional[PipelineClusterInitScriptsFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PipelineClusterInitScriptsFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fec62fa063daa67a8514db5a41689d317be9b4bda310efb2687c13cfc8071b74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineClusterInitScriptsGcs",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class PipelineClusterInitScriptsGcs:
    def __init__(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae6bbe01689d68bd971c222bdd368a270b39468c9d7273278c7b691f14021a73)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.'''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineClusterInitScriptsGcs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineClusterInitScriptsGcsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineClusterInitScriptsGcsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e236792e6915ed3d932cd48279dfa2c158bee777adf11397aaa72dcf35c10ce)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f1fe29b1891eb05ede02df93e62291d089df51836676b49ec4f7eb33cbf59a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PipelineClusterInitScriptsGcs]:
        return typing.cast(typing.Optional[PipelineClusterInitScriptsGcs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PipelineClusterInitScriptsGcs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5de46d4981b30fbd57aafaa07bca85c69bfd750633274cdd4f38c5524638c95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PipelineClusterInitScriptsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineClusterInitScriptsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__38fc39631605a61319335f57d89d34d793b265d37153e7b0437b567aff7c2411)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PipelineClusterInitScriptsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45554416f127276a9cbcf094733043df94ac27996a009ac7b73404c69d2d6310)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PipelineClusterInitScriptsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35e4a30035090326e98f9efa5a9b75145ee37b078f127d50e51a09a7dc94c72d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4cbcf4965843ebd597e293c33ec0ce451a07ddcadf5383efe496cb0e5d50f4a9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__03699ed827890fe6dd7b57e965d7619adf2b33650fc00e324a5db14cf6e8cf73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PipelineClusterInitScripts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PipelineClusterInitScripts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PipelineClusterInitScripts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60e34009bc40aee52c2744271ce8e51c762e01a0623937b87d780a3913be6c65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PipelineClusterInitScriptsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineClusterInitScriptsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7b0a46a32c8b8e142dcfa3540c9b27b5037132f5c7bba804865abbbe7c79bf0e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAbfss")
    def put_abfss(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.
        '''
        value = PipelineClusterInitScriptsAbfss(destination=destination)

        return typing.cast(None, jsii.invoke(self, "putAbfss", [value]))

    @jsii.member(jsii_name="putDbfs")
    def put_dbfs(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.
        '''
        value = PipelineClusterInitScriptsDbfs(destination=destination)

        return typing.cast(None, jsii.invoke(self, "putDbfs", [value]))

    @jsii.member(jsii_name="putFile")
    def put_file(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.
        '''
        value = PipelineClusterInitScriptsFile(destination=destination)

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putGcs")
    def put_gcs(self, *, destination: typing.Optional[builtins.str] = None) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.
        '''
        value = PipelineClusterInitScriptsGcs(destination=destination)

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
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#canned_acl Pipeline#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#enable_encryption Pipeline#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#encryption_type Pipeline#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#endpoint Pipeline#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#kms_key Pipeline#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#region Pipeline#region}.
        '''
        value = PipelineClusterInitScriptsS3(
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
    def abfss(self) -> PipelineClusterInitScriptsAbfssOutputReference:
        return typing.cast(PipelineClusterInitScriptsAbfssOutputReference, jsii.get(self, "abfss"))

    @builtins.property
    @jsii.member(jsii_name="dbfs")
    def dbfs(self) -> PipelineClusterInitScriptsDbfsOutputReference:
        return typing.cast(PipelineClusterInitScriptsDbfsOutputReference, jsii.get(self, "dbfs"))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> PipelineClusterInitScriptsFileOutputReference:
        return typing.cast(PipelineClusterInitScriptsFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="gcs")
    def gcs(self) -> PipelineClusterInitScriptsGcsOutputReference:
        return typing.cast(PipelineClusterInitScriptsGcsOutputReference, jsii.get(self, "gcs"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "PipelineClusterInitScriptsS3OutputReference":
        return typing.cast("PipelineClusterInitScriptsS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="abfssInput")
    def abfss_input(self) -> typing.Optional[PipelineClusterInitScriptsAbfss]:
        return typing.cast(typing.Optional[PipelineClusterInitScriptsAbfss], jsii.get(self, "abfssInput"))

    @builtins.property
    @jsii.member(jsii_name="dbfsInput")
    def dbfs_input(self) -> typing.Optional[PipelineClusterInitScriptsDbfs]:
        return typing.cast(typing.Optional[PipelineClusterInitScriptsDbfs], jsii.get(self, "dbfsInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(self) -> typing.Optional[PipelineClusterInitScriptsFile]:
        return typing.cast(typing.Optional[PipelineClusterInitScriptsFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="gcsInput")
    def gcs_input(self) -> typing.Optional[PipelineClusterInitScriptsGcs]:
        return typing.cast(typing.Optional[PipelineClusterInitScriptsGcs], jsii.get(self, "gcsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(self) -> typing.Optional["PipelineClusterInitScriptsS3"]:
        return typing.cast(typing.Optional["PipelineClusterInitScriptsS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PipelineClusterInitScripts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PipelineClusterInitScripts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PipelineClusterInitScripts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35b39702ca8ed8764270737074675516daea2184430bab8421a959ccebb31af9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineClusterInitScriptsS3",
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
class PipelineClusterInitScriptsS3:
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
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#canned_acl Pipeline#canned_acl}.
        :param enable_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#enable_encryption Pipeline#enable_encryption}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#encryption_type Pipeline#encryption_type}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#endpoint Pipeline#endpoint}.
        :param kms_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#kms_key Pipeline#kms_key}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#region Pipeline#region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39337a1afe9c3ca9f2e4568fa5ef4f3040492f827313cd356c405c34f52dda4f)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#destination Pipeline#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def canned_acl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#canned_acl Pipeline#canned_acl}.'''
        result = self._values.get("canned_acl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#enable_encryption Pipeline#enable_encryption}.'''
        result = self._values.get("enable_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def encryption_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#encryption_type Pipeline#encryption_type}.'''
        result = self._values.get("encryption_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#endpoint Pipeline#endpoint}.'''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#kms_key Pipeline#kms_key}.'''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#region Pipeline#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineClusterInitScriptsS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineClusterInitScriptsS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineClusterInitScriptsS3OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f7ff7a8a78ff172e3583f1c31f812c703695cdec78a79e98917c17c4906885f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0951d76c77bb48847e77a69c806163ff2098b29799a15ee88c23d5c992fa8ac2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cannedAcl", value)

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d06d8524231383c14d82c88edd51499f1ef5cb3a0f4be35f93a7088ded11b6e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dddc44b09f8cbdc1ef170bfc1a7056a0cf25379f64af854c89a3b48fe3b1968d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionType")
    def encryption_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionType"))

    @encryption_type.setter
    def encryption_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c72353dd63ae46e5f64f1094a71ee62c7e78f6b2049ae7dac2ad2ccf1fd7d0d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8f38f89314f81b343f9bf4a609a82534b996876d0d51f54d6fa924d67fa910f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2980afb493f6bf2af038b4a3133b298935d1ab3b19f28f3c4a228d19feefba8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0ceb3236185d3b8b71f6b4c7054321916dc0cdf38a6acba8a1db45a742a21ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PipelineClusterInitScriptsS3]:
        return typing.cast(typing.Optional[PipelineClusterInitScriptsS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PipelineClusterInitScriptsS3],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34d56a257e85f0330f8bff84e45de55ef634162194552ec3f9bc88c97f7c2a20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PipelineClusterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineClusterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f3af632b79691d9a78344feaa1cc8c91ea03ca5f7697d6f8701c6e883086673)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PipelineClusterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__978c20e712a5c3762741441a7e2edd781c9cc172a2b1d499013c50561bef16cb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PipelineClusterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be5948a6bceda9e0f2e894aaa5f74c9929db60b502dbc0b46f2a033355b935f9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9135d0b63d1f562382c08ca864477fe80cfabbed9e0e5f27c9f9ab2418c048b9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bdc3e83321043f7078f71fb5755263d3dc053df38969fa0dfd923985dcb18db0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PipelineCluster]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PipelineCluster]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PipelineCluster]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__287148aeafd7e2738cc4a54f77d69c6e37dca894453f2e6401ac0c0ef113d026)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PipelineClusterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineClusterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fef6d754229036077ff0aa744e27db4b04a6999ad0e705a38c62c68cfe33621a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAutoscale")
    def put_autoscale(
        self,
        *,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
        mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#max_workers Pipeline#max_workers}.
        :param min_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#min_workers Pipeline#min_workers}.
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#mode Pipeline#mode}.
        '''
        value = PipelineClusterAutoscale(
            max_workers=max_workers, min_workers=min_workers, mode=mode
        )

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
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#availability Pipeline#availability}.
        :param ebs_volume_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#ebs_volume_count Pipeline#ebs_volume_count}.
        :param ebs_volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#ebs_volume_size Pipeline#ebs_volume_size}.
        :param ebs_volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#ebs_volume_type Pipeline#ebs_volume_type}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#first_on_demand Pipeline#first_on_demand}.
        :param instance_profile_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#instance_profile_arn Pipeline#instance_profile_arn}.
        :param spot_bid_price_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#spot_bid_price_percent Pipeline#spot_bid_price_percent}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#zone_id Pipeline#zone_id}.
        '''
        value = PipelineClusterAwsAttributes(
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
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#availability Pipeline#availability}.
        :param first_on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#first_on_demand Pipeline#first_on_demand}.
        :param spot_bid_max_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#spot_bid_max_price Pipeline#spot_bid_max_price}.
        '''
        value = PipelineClusterAzureAttributes(
            availability=availability,
            first_on_demand=first_on_demand,
            spot_bid_max_price=spot_bid_max_price,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureAttributes", [value]))

    @jsii.member(jsii_name="putClusterLogConf")
    def put_cluster_log_conf(
        self,
        *,
        dbfs: typing.Optional[typing.Union[PipelineClusterClusterLogConfDbfs, typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union[PipelineClusterClusterLogConfS3, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dbfs: dbfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#dbfs Pipeline#dbfs}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#s3 Pipeline#s3}
        '''
        value = PipelineClusterClusterLogConf(dbfs=dbfs, s3=s3)

        return typing.cast(None, jsii.invoke(self, "putClusterLogConf", [value]))

    @jsii.member(jsii_name="putGcpAttributes")
    def put_gcp_attributes(
        self,
        *,
        availability: typing.Optional[builtins.str] = None,
        google_service_account: typing.Optional[builtins.str] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param availability: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#availability Pipeline#availability}.
        :param google_service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#google_service_account Pipeline#google_service_account}.
        :param zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#zone_id Pipeline#zone_id}.
        '''
        value = PipelineClusterGcpAttributes(
            availability=availability,
            google_service_account=google_service_account,
            zone_id=zone_id,
        )

        return typing.cast(None, jsii.invoke(self, "putGcpAttributes", [value]))

    @jsii.member(jsii_name="putInitScripts")
    def put_init_scripts(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PipelineClusterInitScripts, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7237256fcb7e09fd66b7cc79d84d9bb6244ee66c47193eff456fec16481a046c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInitScripts", [value]))

    @jsii.member(jsii_name="resetApplyPolicyDefaultValues")
    def reset_apply_policy_default_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplyPolicyDefaultValues", []))

    @jsii.member(jsii_name="resetAutoscale")
    def reset_autoscale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscale", []))

    @jsii.member(jsii_name="resetAwsAttributes")
    def reset_aws_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsAttributes", []))

    @jsii.member(jsii_name="resetAzureAttributes")
    def reset_azure_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureAttributes", []))

    @jsii.member(jsii_name="resetClusterLogConf")
    def reset_cluster_log_conf(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterLogConf", []))

    @jsii.member(jsii_name="resetCustomTags")
    def reset_custom_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomTags", []))

    @jsii.member(jsii_name="resetDriverInstancePoolId")
    def reset_driver_instance_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverInstancePoolId", []))

    @jsii.member(jsii_name="resetDriverNodeTypeId")
    def reset_driver_node_type_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverNodeTypeId", []))

    @jsii.member(jsii_name="resetEnableLocalDiskEncryption")
    def reset_enable_local_disk_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableLocalDiskEncryption", []))

    @jsii.member(jsii_name="resetGcpAttributes")
    def reset_gcp_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcpAttributes", []))

    @jsii.member(jsii_name="resetInitScripts")
    def reset_init_scripts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitScripts", []))

    @jsii.member(jsii_name="resetInstancePoolId")
    def reset_instance_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancePoolId", []))

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @jsii.member(jsii_name="resetNodeTypeId")
    def reset_node_type_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeTypeId", []))

    @jsii.member(jsii_name="resetNumWorkers")
    def reset_num_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumWorkers", []))

    @jsii.member(jsii_name="resetPolicyId")
    def reset_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyId", []))

    @jsii.member(jsii_name="resetSparkConf")
    def reset_spark_conf(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkConf", []))

    @jsii.member(jsii_name="resetSparkEnvVars")
    def reset_spark_env_vars(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkEnvVars", []))

    @jsii.member(jsii_name="resetSshPublicKeys")
    def reset_ssh_public_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshPublicKeys", []))

    @builtins.property
    @jsii.member(jsii_name="autoscale")
    def autoscale(self) -> PipelineClusterAutoscaleOutputReference:
        return typing.cast(PipelineClusterAutoscaleOutputReference, jsii.get(self, "autoscale"))

    @builtins.property
    @jsii.member(jsii_name="awsAttributes")
    def aws_attributes(self) -> PipelineClusterAwsAttributesOutputReference:
        return typing.cast(PipelineClusterAwsAttributesOutputReference, jsii.get(self, "awsAttributes"))

    @builtins.property
    @jsii.member(jsii_name="azureAttributes")
    def azure_attributes(self) -> PipelineClusterAzureAttributesOutputReference:
        return typing.cast(PipelineClusterAzureAttributesOutputReference, jsii.get(self, "azureAttributes"))

    @builtins.property
    @jsii.member(jsii_name="clusterLogConf")
    def cluster_log_conf(self) -> PipelineClusterClusterLogConfOutputReference:
        return typing.cast(PipelineClusterClusterLogConfOutputReference, jsii.get(self, "clusterLogConf"))

    @builtins.property
    @jsii.member(jsii_name="gcpAttributes")
    def gcp_attributes(self) -> PipelineClusterGcpAttributesOutputReference:
        return typing.cast(PipelineClusterGcpAttributesOutputReference, jsii.get(self, "gcpAttributes"))

    @builtins.property
    @jsii.member(jsii_name="initScripts")
    def init_scripts(self) -> PipelineClusterInitScriptsList:
        return typing.cast(PipelineClusterInitScriptsList, jsii.get(self, "initScripts"))

    @builtins.property
    @jsii.member(jsii_name="applyPolicyDefaultValuesInput")
    def apply_policy_default_values_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "applyPolicyDefaultValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscaleInput")
    def autoscale_input(self) -> typing.Optional[PipelineClusterAutoscale]:
        return typing.cast(typing.Optional[PipelineClusterAutoscale], jsii.get(self, "autoscaleInput"))

    @builtins.property
    @jsii.member(jsii_name="awsAttributesInput")
    def aws_attributes_input(self) -> typing.Optional[PipelineClusterAwsAttributes]:
        return typing.cast(typing.Optional[PipelineClusterAwsAttributes], jsii.get(self, "awsAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="azureAttributesInput")
    def azure_attributes_input(self) -> typing.Optional[PipelineClusterAzureAttributes]:
        return typing.cast(typing.Optional[PipelineClusterAzureAttributes], jsii.get(self, "azureAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterLogConfInput")
    def cluster_log_conf_input(self) -> typing.Optional[PipelineClusterClusterLogConf]:
        return typing.cast(typing.Optional[PipelineClusterClusterLogConf], jsii.get(self, "clusterLogConfInput"))

    @builtins.property
    @jsii.member(jsii_name="customTagsInput")
    def custom_tags_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="driverInstancePoolIdInput")
    def driver_instance_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInstancePoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="driverNodeTypeIdInput")
    def driver_node_type_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverNodeTypeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="enableLocalDiskEncryptionInput")
    def enable_local_disk_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableLocalDiskEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="gcpAttributesInput")
    def gcp_attributes_input(self) -> typing.Optional[PipelineClusterGcpAttributes]:
        return typing.cast(typing.Optional[PipelineClusterGcpAttributes], jsii.get(self, "gcpAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="initScriptsInput")
    def init_scripts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PipelineClusterInitScripts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PipelineClusterInitScripts]]], jsii.get(self, "initScriptsInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolIdInput")
    def instance_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instancePoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

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
    @jsii.member(jsii_name="sshPublicKeysInput")
    def ssh_public_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sshPublicKeysInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__e9b310a829341c47858043dd2a235f598810c46490d3b2c781aca2bb9ba17a16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyPolicyDefaultValues", value)

    @builtins.property
    @jsii.member(jsii_name="customTags")
    def custom_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customTags"))

    @custom_tags.setter
    def custom_tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d3438aa4e0bea9b918574c2e222258111f37c98502aa8c07688c5db74d25aee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customTags", value)

    @builtins.property
    @jsii.member(jsii_name="driverInstancePoolId")
    def driver_instance_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driverInstancePoolId"))

    @driver_instance_pool_id.setter
    def driver_instance_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d81fa73ad3625ed37e56adf7a272476528ad58f406324d8f35130eb85bfcc50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverInstancePoolId", value)

    @builtins.property
    @jsii.member(jsii_name="driverNodeTypeId")
    def driver_node_type_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driverNodeTypeId"))

    @driver_node_type_id.setter
    def driver_node_type_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2b6ca3ec48c370ef7f224f222fa506d46487d019eeaab0378ae5071f9e0fec1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverNodeTypeId", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__c00e07b577c1634f6ea7bb8d836a0215319cf2db90d875e3567ac69968eb2fa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableLocalDiskEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="instancePoolId")
    def instance_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instancePoolId"))

    @instance_pool_id.setter
    def instance_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d7ed9f9bd311c2601e1614bae259b45959609e849636e4f8ca868fc526c8be8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instancePoolId", value)

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1b56e9940485ff52d7cdea2ca00769f9b98965cfada5a4f0103523386dabf99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="nodeTypeId")
    def node_type_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeTypeId"))

    @node_type_id.setter
    def node_type_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac80b8009125ce2e53f63fef39609721d551de57df36498858a86e55c4c9bcf3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeTypeId", value)

    @builtins.property
    @jsii.member(jsii_name="numWorkers")
    def num_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numWorkers"))

    @num_workers.setter
    def num_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f77463c2c31612d4b0b1420b2303a13604c64db12c37c3652276a516ccfb8c67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyId"))

    @policy_id.setter
    def policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e1c9e1a719372ccabbc0ae57ed97e3ff2492200be81371a2b04fbfb02f224ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyId", value)

    @builtins.property
    @jsii.member(jsii_name="sparkConf")
    def spark_conf(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sparkConf"))

    @spark_conf.setter
    def spark_conf(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73fdaa128f3f554bc373c83787f8233d550eeb91af5020c8ad52531759544913)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkConf", value)

    @builtins.property
    @jsii.member(jsii_name="sparkEnvVars")
    def spark_env_vars(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sparkEnvVars"))

    @spark_env_vars.setter
    def spark_env_vars(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd9418ad971d8cf80338ddc35c293fd1764396cc36d154f5d32f7f07b6055a48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkEnvVars", value)

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeys")
    def ssh_public_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sshPublicKeys"))

    @ssh_public_keys.setter
    def ssh_public_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97ab26d0aa329436e8075510b44916e57c9d82c16479680cc3ffc14465991541)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPublicKeys", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PipelineCluster, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PipelineCluster, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PipelineCluster, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ebf8661f6256cad973e3f9982c9eae2550158a4a964d82957c02e9ed1f0047f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "allow_duplicate_names": "allowDuplicateNames",
        "catalog": "catalog",
        "channel": "channel",
        "cluster": "cluster",
        "configuration": "configuration",
        "continuous": "continuous",
        "development": "development",
        "edition": "edition",
        "filters": "filters",
        "id": "id",
        "library": "library",
        "name": "name",
        "photon": "photon",
        "storage": "storage",
        "target": "target",
        "timeouts": "timeouts",
    },
)
class PipelineConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        allow_duplicate_names: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        catalog: typing.Optional[builtins.str] = None,
        channel: typing.Optional[builtins.str] = None,
        cluster: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PipelineCluster, typing.Dict[builtins.str, typing.Any]]]]] = None,
        configuration: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        continuous: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        development: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        edition: typing.Optional[builtins.str] = None,
        filters: typing.Optional[typing.Union["PipelineFilters", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        library: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PipelineLibrary", typing.Dict[builtins.str, typing.Any]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        photon: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        storage: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["PipelineTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param allow_duplicate_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#allow_duplicate_names Pipeline#allow_duplicate_names}.
        :param catalog: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#catalog Pipeline#catalog}.
        :param channel: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#channel Pipeline#channel}.
        :param cluster: cluster block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#cluster Pipeline#cluster}
        :param configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#configuration Pipeline#configuration}.
        :param continuous: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#continuous Pipeline#continuous}.
        :param development: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#development Pipeline#development}.
        :param edition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#edition Pipeline#edition}.
        :param filters: filters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#filters Pipeline#filters}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#id Pipeline#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param library: library block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#library Pipeline#library}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#name Pipeline#name}.
        :param photon: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#photon Pipeline#photon}.
        :param storage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#storage Pipeline#storage}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#target Pipeline#target}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#timeouts Pipeline#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(filters, dict):
            filters = PipelineFilters(**filters)
        if isinstance(timeouts, dict):
            timeouts = PipelineTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ebc2b0023c97b6cd7a6ed7c732dbb538c3f1e0ec54995e635c681ee76ac7b7b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument allow_duplicate_names", value=allow_duplicate_names, expected_type=type_hints["allow_duplicate_names"])
            check_type(argname="argument catalog", value=catalog, expected_type=type_hints["catalog"])
            check_type(argname="argument channel", value=channel, expected_type=type_hints["channel"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument continuous", value=continuous, expected_type=type_hints["continuous"])
            check_type(argname="argument development", value=development, expected_type=type_hints["development"])
            check_type(argname="argument edition", value=edition, expected_type=type_hints["edition"])
            check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument library", value=library, expected_type=type_hints["library"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument photon", value=photon, expected_type=type_hints["photon"])
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
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
        if allow_duplicate_names is not None:
            self._values["allow_duplicate_names"] = allow_duplicate_names
        if catalog is not None:
            self._values["catalog"] = catalog
        if channel is not None:
            self._values["channel"] = channel
        if cluster is not None:
            self._values["cluster"] = cluster
        if configuration is not None:
            self._values["configuration"] = configuration
        if continuous is not None:
            self._values["continuous"] = continuous
        if development is not None:
            self._values["development"] = development
        if edition is not None:
            self._values["edition"] = edition
        if filters is not None:
            self._values["filters"] = filters
        if id is not None:
            self._values["id"] = id
        if library is not None:
            self._values["library"] = library
        if name is not None:
            self._values["name"] = name
        if photon is not None:
            self._values["photon"] = photon
        if storage is not None:
            self._values["storage"] = storage
        if target is not None:
            self._values["target"] = target
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def allow_duplicate_names(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#allow_duplicate_names Pipeline#allow_duplicate_names}.'''
        result = self._values.get("allow_duplicate_names")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def catalog(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#catalog Pipeline#catalog}.'''
        result = self._values.get("catalog")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def channel(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#channel Pipeline#channel}.'''
        result = self._values.get("channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PipelineCluster]]]:
        '''cluster block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#cluster Pipeline#cluster}
        '''
        result = self._values.get("cluster")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PipelineCluster]]], result)

    @builtins.property
    def configuration(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#configuration Pipeline#configuration}.'''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def continuous(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#continuous Pipeline#continuous}.'''
        result = self._values.get("continuous")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def development(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#development Pipeline#development}.'''
        result = self._values.get("development")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def edition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#edition Pipeline#edition}.'''
        result = self._values.get("edition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filters(self) -> typing.Optional["PipelineFilters"]:
        '''filters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#filters Pipeline#filters}
        '''
        result = self._values.get("filters")
        return typing.cast(typing.Optional["PipelineFilters"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#id Pipeline#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def library(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PipelineLibrary"]]]:
        '''library block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#library Pipeline#library}
        '''
        result = self._values.get("library")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PipelineLibrary"]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#name Pipeline#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def photon(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#photon Pipeline#photon}.'''
        result = self._values.get("photon")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def storage(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#storage Pipeline#storage}.'''
        result = self._values.get("storage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#target Pipeline#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["PipelineTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#timeouts Pipeline#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["PipelineTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineFilters",
    jsii_struct_bases=[],
    name_mapping={"exclude": "exclude", "include": "include"},
)
class PipelineFilters:
    def __init__(
        self,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param exclude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#exclude Pipeline#exclude}.
        :param include: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#include Pipeline#include}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__400edb976c2c430e3ea0ba9bf6adae5161404b386bc44ad2e9d688fb585dbbf6)
            check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
            check_type(argname="argument include", value=include, expected_type=type_hints["include"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if exclude is not None:
            self._values["exclude"] = exclude
        if include is not None:
            self._values["include"] = include

    @builtins.property
    def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#exclude Pipeline#exclude}.'''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def include(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#include Pipeline#include}.'''
        result = self._values.get("include")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineFilters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineFiltersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineFiltersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f512ba7b8174dad011c60cf8e39ce500b5a7abee82589dabdd62f6d7063dd9c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExclude")
    def reset_exclude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclude", []))

    @jsii.member(jsii_name="resetInclude")
    def reset_include(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInclude", []))

    @builtins.property
    @jsii.member(jsii_name="excludeInput")
    def exclude_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludeInput"))

    @builtins.property
    @jsii.member(jsii_name="includeInput")
    def include_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includeInput"))

    @builtins.property
    @jsii.member(jsii_name="exclude")
    def exclude(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclude"))

    @exclude.setter
    def exclude(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32f269ba771416f5754c871d4e5defb67eca3e66458c176472fa9c7b4bb0adb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclude", value)

    @builtins.property
    @jsii.member(jsii_name="include")
    def include(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "include"))

    @include.setter
    def include(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d6e4c6838df29d1751c879733dbc18de255051fe3e780d2660c331d08e22834)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "include", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PipelineFilters]:
        return typing.cast(typing.Optional[PipelineFilters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PipelineFilters]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4cfe1c40e31ba1fdfc9155a7e506df9d0367f987d691732efb4eb447b42042b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineLibrary",
    jsii_struct_bases=[],
    name_mapping={
        "file": "file",
        "jar": "jar",
        "maven": "maven",
        "notebook": "notebook",
        "whl": "whl",
    },
)
class PipelineLibrary:
    def __init__(
        self,
        *,
        file: typing.Optional[typing.Union["PipelineLibraryFile", typing.Dict[builtins.str, typing.Any]]] = None,
        jar: typing.Optional[builtins.str] = None,
        maven: typing.Optional[typing.Union["PipelineLibraryMaven", typing.Dict[builtins.str, typing.Any]]] = None,
        notebook: typing.Optional[typing.Union["PipelineLibraryNotebook", typing.Dict[builtins.str, typing.Any]]] = None,
        whl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#file Pipeline#file}
        :param jar: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#jar Pipeline#jar}.
        :param maven: maven block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#maven Pipeline#maven}
        :param notebook: notebook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#notebook Pipeline#notebook}
        :param whl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#whl Pipeline#whl}.
        '''
        if isinstance(file, dict):
            file = PipelineLibraryFile(**file)
        if isinstance(maven, dict):
            maven = PipelineLibraryMaven(**maven)
        if isinstance(notebook, dict):
            notebook = PipelineLibraryNotebook(**notebook)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab38672557257f0630447a3266e7e9ca34eb43708590325a7db3b838bc1944ed)
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument jar", value=jar, expected_type=type_hints["jar"])
            check_type(argname="argument maven", value=maven, expected_type=type_hints["maven"])
            check_type(argname="argument notebook", value=notebook, expected_type=type_hints["notebook"])
            check_type(argname="argument whl", value=whl, expected_type=type_hints["whl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if file is not None:
            self._values["file"] = file
        if jar is not None:
            self._values["jar"] = jar
        if maven is not None:
            self._values["maven"] = maven
        if notebook is not None:
            self._values["notebook"] = notebook
        if whl is not None:
            self._values["whl"] = whl

    @builtins.property
    def file(self) -> typing.Optional["PipelineLibraryFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#file Pipeline#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["PipelineLibraryFile"], result)

    @builtins.property
    def jar(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#jar Pipeline#jar}.'''
        result = self._values.get("jar")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maven(self) -> typing.Optional["PipelineLibraryMaven"]:
        '''maven block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#maven Pipeline#maven}
        '''
        result = self._values.get("maven")
        return typing.cast(typing.Optional["PipelineLibraryMaven"], result)

    @builtins.property
    def notebook(self) -> typing.Optional["PipelineLibraryNotebook"]:
        '''notebook block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#notebook Pipeline#notebook}
        '''
        result = self._values.get("notebook")
        return typing.cast(typing.Optional["PipelineLibraryNotebook"], result)

    @builtins.property
    def whl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#whl Pipeline#whl}.'''
        result = self._values.get("whl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineLibrary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineLibraryFile",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class PipelineLibraryFile:
    def __init__(self, *, path: builtins.str) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#path Pipeline#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__551fe51a4b40af94c68a838b1e62617bb3265f541b41bf724bbbd6169142b716)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path": path,
        }

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#path Pipeline#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineLibraryFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineLibraryFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineLibraryFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f7b6edb54bd6ec5340fc07503cde089bc3f8ebc749e784647ee26c64a855a555)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30020fded81167ba7c24465924bc6819c87b8729a08dd352841f5cadfc74dddb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PipelineLibraryFile]:
        return typing.cast(typing.Optional[PipelineLibraryFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PipelineLibraryFile]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4385f097751ff3ac4405e398304569e877d9d2c8784c609ea774110fb68e452)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PipelineLibraryList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineLibraryList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__feaec27d96d60deadc7de92023d7d861bd8addb2f0b3cb79b7b0de97a20f3345)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PipelineLibraryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc577537d2cf384188b3811901416027d64926f7259e5f8a6e326f71c3b8194d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PipelineLibraryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cade30eb558d3005bdd87d3efc7a9fc5972c2d437d7e227dc2bea669cf99fd74)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8da48c46afba76ff9d82cd2b3366dd3c0cd2444dee99ad04104260ead7d8c7b3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e57bbb07f0dd56852ff85c2ade6690513556172b49a9302ecdaf005230b4166)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PipelineLibrary]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PipelineLibrary]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PipelineLibrary]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4572654c3fe5ff96fb45731a68d0ed414a7e518f2cbe692f44812c591467f05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineLibraryMaven",
    jsii_struct_bases=[],
    name_mapping={
        "coordinates": "coordinates",
        "exclusions": "exclusions",
        "repo": "repo",
    },
)
class PipelineLibraryMaven:
    def __init__(
        self,
        *,
        coordinates: builtins.str,
        exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param coordinates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#coordinates Pipeline#coordinates}.
        :param exclusions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#exclusions Pipeline#exclusions}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#repo Pipeline#repo}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__145952f0dfd595687f0284616a7953b02be0e5b6cef88142af4996d6917883ae)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#coordinates Pipeline#coordinates}.'''
        result = self._values.get("coordinates")
        assert result is not None, "Required property 'coordinates' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclusions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#exclusions Pipeline#exclusions}.'''
        result = self._values.get("exclusions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#repo Pipeline#repo}.'''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineLibraryMaven(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineLibraryMavenOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineLibraryMavenOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f256e1ecd65b00c87dca99df78c18328d02c273ba8607a750532f28e25762b0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae68527922d89feac3decb13f689acf3ef54a360f78e372391b54d377dad0299)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coordinates", value)

    @builtins.property
    @jsii.member(jsii_name="exclusions")
    def exclusions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclusions"))

    @exclusions.setter
    def exclusions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9f81b5f947bebb3f1df0607ccefb6d5024955a67d5aa8818a3582f9546843e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusions", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9455e9c03e1221a7208c60581916b32f97415d96011cc20a38187eae5db91ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PipelineLibraryMaven]:
        return typing.cast(typing.Optional[PipelineLibraryMaven], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PipelineLibraryMaven]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c917c0280b945797d7da35f4dff4ef82a596624eb54fc4addc1abde35ef9df5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineLibraryNotebook",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class PipelineLibraryNotebook:
    def __init__(self, *, path: builtins.str) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#path Pipeline#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85b6ecd237605f3d008151a2bc4b0dc57e33743c60e08ea76c200273fd3beb35)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path": path,
        }

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#path Pipeline#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineLibraryNotebook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineLibraryNotebookOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineLibraryNotebookOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7bc19f67b6de2c849df0710c250dc9c8fad562ba0fbd56e842249bd9704afc17)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d0620d988160f2fb6fcf17c4a5fc76877e30e8a8a681844e83c16bd74624407)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PipelineLibraryNotebook]:
        return typing.cast(typing.Optional[PipelineLibraryNotebook], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PipelineLibraryNotebook]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__145cabadfb54f3504212d46d8ec884e48caf91f904ac400f67e4d10424332121)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PipelineLibraryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineLibraryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3006c66944f9e4cb49c3bf1da0675631e8468f51e5989e8ebb77f1178094a652)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFile")
    def put_file(self, *, path: builtins.str) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#path Pipeline#path}.
        '''
        value = PipelineLibraryFile(path=path)

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putMaven")
    def put_maven(
        self,
        *,
        coordinates: builtins.str,
        exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param coordinates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#coordinates Pipeline#coordinates}.
        :param exclusions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#exclusions Pipeline#exclusions}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#repo Pipeline#repo}.
        '''
        value = PipelineLibraryMaven(
            coordinates=coordinates, exclusions=exclusions, repo=repo
        )

        return typing.cast(None, jsii.invoke(self, "putMaven", [value]))

    @jsii.member(jsii_name="putNotebook")
    def put_notebook(self, *, path: builtins.str) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#path Pipeline#path}.
        '''
        value = PipelineLibraryNotebook(path=path)

        return typing.cast(None, jsii.invoke(self, "putNotebook", [value]))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetJar")
    def reset_jar(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJar", []))

    @jsii.member(jsii_name="resetMaven")
    def reset_maven(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaven", []))

    @jsii.member(jsii_name="resetNotebook")
    def reset_notebook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotebook", []))

    @jsii.member(jsii_name="resetWhl")
    def reset_whl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhl", []))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> PipelineLibraryFileOutputReference:
        return typing.cast(PipelineLibraryFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="maven")
    def maven(self) -> PipelineLibraryMavenOutputReference:
        return typing.cast(PipelineLibraryMavenOutputReference, jsii.get(self, "maven"))

    @builtins.property
    @jsii.member(jsii_name="notebook")
    def notebook(self) -> PipelineLibraryNotebookOutputReference:
        return typing.cast(PipelineLibraryNotebookOutputReference, jsii.get(self, "notebook"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(self) -> typing.Optional[PipelineLibraryFile]:
        return typing.cast(typing.Optional[PipelineLibraryFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="jarInput")
    def jar_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jarInput"))

    @builtins.property
    @jsii.member(jsii_name="mavenInput")
    def maven_input(self) -> typing.Optional[PipelineLibraryMaven]:
        return typing.cast(typing.Optional[PipelineLibraryMaven], jsii.get(self, "mavenInput"))

    @builtins.property
    @jsii.member(jsii_name="notebookInput")
    def notebook_input(self) -> typing.Optional[PipelineLibraryNotebook]:
        return typing.cast(typing.Optional[PipelineLibraryNotebook], jsii.get(self, "notebookInput"))

    @builtins.property
    @jsii.member(jsii_name="whlInput")
    def whl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whlInput"))

    @builtins.property
    @jsii.member(jsii_name="jar")
    def jar(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jar"))

    @jar.setter
    def jar(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59dd279518b209ef52f3ff45e4288c809f867b19f9204b6b7639c3737e7c0e9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jar", value)

    @builtins.property
    @jsii.member(jsii_name="whl")
    def whl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whl"))

    @whl.setter
    def whl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9956a6832673bcc10c330ce08b0e458a7ee78867c7ccfe82f91bc5efd3ff661)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PipelineLibrary, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PipelineLibrary, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PipelineLibrary, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a599d39b6908e198c20ee7ea1e21a2fc074b3e03bfd88a19bfe4c23811cb4e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.pipeline.PipelineTimeouts",
    jsii_struct_bases=[],
    name_mapping={"default": "default"},
)
class PipelineTimeouts:
    def __init__(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#default Pipeline#default}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b598ef82f6f5d047e374b06f5a0f512cd2886df2602573765841224259b1d81)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/pipeline#default Pipeline#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PipelineTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.pipeline.PipelineTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7b1a5fe602fef6f78bae83ea42ac93d4f1b437163e8523763fa1b22bf9c5e113)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f63a2a6c4d709c183fb036acc80e081fd3dba3b850d13f48f08711108363bef4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PipelineTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PipelineTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PipelineTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c09495cab5573697f3dff8a616df10342c467910b158e35fc9e109963be856b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Pipeline",
    "PipelineCluster",
    "PipelineClusterAutoscale",
    "PipelineClusterAutoscaleOutputReference",
    "PipelineClusterAwsAttributes",
    "PipelineClusterAwsAttributesOutputReference",
    "PipelineClusterAzureAttributes",
    "PipelineClusterAzureAttributesOutputReference",
    "PipelineClusterClusterLogConf",
    "PipelineClusterClusterLogConfDbfs",
    "PipelineClusterClusterLogConfDbfsOutputReference",
    "PipelineClusterClusterLogConfOutputReference",
    "PipelineClusterClusterLogConfS3",
    "PipelineClusterClusterLogConfS3OutputReference",
    "PipelineClusterGcpAttributes",
    "PipelineClusterGcpAttributesOutputReference",
    "PipelineClusterInitScripts",
    "PipelineClusterInitScriptsAbfss",
    "PipelineClusterInitScriptsAbfssOutputReference",
    "PipelineClusterInitScriptsDbfs",
    "PipelineClusterInitScriptsDbfsOutputReference",
    "PipelineClusterInitScriptsFile",
    "PipelineClusterInitScriptsFileOutputReference",
    "PipelineClusterInitScriptsGcs",
    "PipelineClusterInitScriptsGcsOutputReference",
    "PipelineClusterInitScriptsList",
    "PipelineClusterInitScriptsOutputReference",
    "PipelineClusterInitScriptsS3",
    "PipelineClusterInitScriptsS3OutputReference",
    "PipelineClusterList",
    "PipelineClusterOutputReference",
    "PipelineConfig",
    "PipelineFilters",
    "PipelineFiltersOutputReference",
    "PipelineLibrary",
    "PipelineLibraryFile",
    "PipelineLibraryFileOutputReference",
    "PipelineLibraryList",
    "PipelineLibraryMaven",
    "PipelineLibraryMavenOutputReference",
    "PipelineLibraryNotebook",
    "PipelineLibraryNotebookOutputReference",
    "PipelineLibraryOutputReference",
    "PipelineTimeouts",
    "PipelineTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__bd4075cee20ed6f4c4e22fc800294564ffb556867030df6002d73865896ee693(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    allow_duplicate_names: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    catalog: typing.Optional[builtins.str] = None,
    channel: typing.Optional[builtins.str] = None,
    cluster: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PipelineCluster, typing.Dict[builtins.str, typing.Any]]]]] = None,
    configuration: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    continuous: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    development: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    edition: typing.Optional[builtins.str] = None,
    filters: typing.Optional[typing.Union[PipelineFilters, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    library: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PipelineLibrary, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: typing.Optional[builtins.str] = None,
    photon: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    storage: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[PipelineTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__39dde6cd11a73698eb6e4e34372941bc40274aa570790d69a32d962f7a8e9999(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PipelineCluster, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a8eafb67f259cb5e92097a5e4f2e23bdf17d04bef1e1b345edfa4297f29cd04(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PipelineLibrary, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4649b808855fc680808bf4cbc9f0470127bb4d70bf1ccb6f972e4b82c9ec7a39(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbab7232bdd9b57c48bed8fe7afaa76bfea1416e8a79124b8b06c735e4c42680(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5a3b6b3e69a428aad2fd4ee675ee598b64d58723686ff73a4279f82d894278d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89f8d281b8ee6de08c6213c306372c17ef9f4e49598be12997e475b01c484c19(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__178b299c31a874d2bcfd3ed03fb052eea218a678e88ccd9b85a3d7d1fd0522de(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adf94353028dc4ed3867b4fd380e1f8ed272bf30123ed8067ce0649fdb848711(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34e458cf24db6e90404c8086d653aff50023484fa7652a7d0d8f3f6e46551fb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0492ae7fcd38d39b9f59985669ade0fca372b3e5c41b0e348c6b71f39997932(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bacedfc8557e305856ceeedeaf82a96c7100d6afc97c0a4603f071800a4c809(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bba47cdc47c438d856c3dd35a0beb1ad8dd5c7b6b95feb8acf9e48cf0a04f9a0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66cc30ffd33cf9eace27280d5d360cfeb1f76ee56af93277bbae17f73d07742f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d31123f8955aaf33cd94f8f948975f3ff6ce841beb9b0381665da515f6a2a87a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68d3dbd3f224aeca0068c3ab93e02b1fd555709ae155e349bc21ead9e346714a(
    *,
    apply_policy_default_values: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    autoscale: typing.Optional[typing.Union[PipelineClusterAutoscale, typing.Dict[builtins.str, typing.Any]]] = None,
    aws_attributes: typing.Optional[typing.Union[PipelineClusterAwsAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    azure_attributes: typing.Optional[typing.Union[PipelineClusterAzureAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_log_conf: typing.Optional[typing.Union[PipelineClusterClusterLogConf, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    driver_instance_pool_id: typing.Optional[builtins.str] = None,
    driver_node_type_id: typing.Optional[builtins.str] = None,
    enable_local_disk_encryption: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    gcp_attributes: typing.Optional[typing.Union[PipelineClusterGcpAttributes, typing.Dict[builtins.str, typing.Any]]] = None,
    init_scripts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PipelineClusterInitScripts, typing.Dict[builtins.str, typing.Any]]]]] = None,
    instance_pool_id: typing.Optional[builtins.str] = None,
    label: typing.Optional[builtins.str] = None,
    node_type_id: typing.Optional[builtins.str] = None,
    num_workers: typing.Optional[jsii.Number] = None,
    policy_id: typing.Optional[builtins.str] = None,
    spark_conf: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    spark_env_vars: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac34603de0ecea33f76dbb535b2a4cdb34422babdbba1a76b4ce6a092ec7de46(
    *,
    max_workers: typing.Optional[jsii.Number] = None,
    min_workers: typing.Optional[jsii.Number] = None,
    mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34875dcef21db0b17c8cbdb94c21658cecb0685d7b36ad2ce70869b60fe35317(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7bb7cbf261c60fa54d3a7cb1da6eb3e29dc90bc934ce39bcddcd1c1d5f6b599(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e95cae38322cd180092a459ca9e2feec9afa7de0d0ce1285195bd08fbd2d923(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__282b2270e343de41bba32576029b32ad2f74d9ed44b35d5c3c0b732cd0009c92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de281bf42ad3fbcd0f79740d737971b86e9002fae45672fe3783e6a5df9cc2fd(
    value: typing.Optional[PipelineClusterAutoscale],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8448d88610d716872b148022875a285b9d5ef32c4473632bb42e48bd9c6150cf(
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

def _typecheckingstub__04cebc34c0e073707f6d694a7843a676c105d9274d63cd7959ebaec74463817e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__750fae0bb4310a24c6e63613b85b6edd5c24a5c22272c16d37888eff5495101f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d7d794def4f9845d4a9da44af9251c2bbb9d9f966a6a92e3b47e5bfdb6c3e6f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__408f5724223715144ee0b88394dd3d9637dc26b35ee6a833bf901cb4d1c9e29e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1d92d3a986a2e842b8e487c8fcbedeceaf3abcb2b8e30a0641f53a598d82df3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcfc9c1c991c22e79a09fa94e0fdc3de4079715e0ad46a92823428e218e7f014(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f75177a5d06e510a12180a5703cf53717740de8c11d899ab0cc93e99b77f4d7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8597f5bbf395aeb1430d35a7749689b490178dca3aebd079d9de8b8660580e97(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86b82369d4c4ad3b6ae08c616dd536d5763bc9b853f4f0772eda2678bab93681(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e8bc568ff97cb23480fd1f8e2a5fb4a81d19767fe240bb0bf4c6ece3bd0aa2d(
    value: typing.Optional[PipelineClusterAwsAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1ad13a4411d368bff446b879633a5a481c33de619837511f5907d211fa4a5be(
    *,
    availability: typing.Optional[builtins.str] = None,
    first_on_demand: typing.Optional[jsii.Number] = None,
    spot_bid_max_price: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95d82b5fee246740a47492f5ae4a3d9f8b54ce10fd5b70aee1647c056577416e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f612fd3a40472541e8af626b98192f2bdf9a45ca52666df3e494e6ce697a2709(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96e7d28fe6b4acf4627704280964ce18c032ab5ac1abbea5cffeee4238aa609f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3196f82d2c58bb796537400456d6a10c25eabd1c57936d456937211c88f8775c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9f6523ab29403fc0f756e7672c1589a60c021e7f01e5668086633fbbc8070b4(
    value: typing.Optional[PipelineClusterAzureAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e818fe1ba5c340172aa5fdd17eb61fa872ad290f10accd89987cf57da0c03dc0(
    *,
    dbfs: typing.Optional[typing.Union[PipelineClusterClusterLogConfDbfs, typing.Dict[builtins.str, typing.Any]]] = None,
    s3: typing.Optional[typing.Union[PipelineClusterClusterLogConfS3, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1de909e645f8e2f3235ae7e84866fe85748e966e9f62424b0197354703e8cd78(
    *,
    destination: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afd381da0ec83fe63aedf553cd5fc443b235e8b501858eb9b3bf418f5ce7fa7d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b72d6bb438c93f22060891a6c9a726832045cb565a0974a9cce1fbeadf8decf0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b9ea921fd8b9a60253c6204ad04a478ed2fd604de173d680c0bf78b46fe3e4a(
    value: typing.Optional[PipelineClusterClusterLogConfDbfs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6059d973a5573dd4b21b7de3210135a2300fe5927265a0af53c8dfac66751982(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc004b6fe12fb908e4c4bc48a111e566afbb7338613f7c2cb1d86c75fad97cca(
    value: typing.Optional[PipelineClusterClusterLogConf],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1f54af77a9959e9f7dc7e851f5f6cd7ac033e4946777a4e12bf0290492ba020(
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

def _typecheckingstub__ea527b4c22975ff7e1961f390d6c070f27b22595a9af40cff3ce66acbb880bf0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09eedfd34f79d757e0049a6ae5dacc4acc33f13df773f6155714a6e7b5715bba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0659abadfb971de3697d1fcbb74c0b9240e652dcd180d1cdabd85868aaed6c9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f872f1c9768844f492adaf29f8d5eab7a3861439b13536e7636a5b5b03661b6f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0d3e138188ef48ebcd45dfe83ce5627182e36840e7905328b5c40dde752e1c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f63bdf195d98464b452a2c5e0aba73b609b8d48030879610f8e4b66a6fac54c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__069c23796879870274723d690d533000f6ed4b2e94b8504781d2b429be0ae168(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9398ed6f675e7994e3f223cc108b3bc514ee51574c97552d66fad52ff61d184a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__298b31792285d585f40fcb031067ddef545097a485f12333b61582566afd4fbb(
    value: typing.Optional[PipelineClusterClusterLogConfS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ce71244c3cedb4628281f54806de708e24b055ce57a0c7fe4359d98560ab79d(
    *,
    availability: typing.Optional[builtins.str] = None,
    google_service_account: typing.Optional[builtins.str] = None,
    zone_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac4f4a53cbd2c91d7b06cb8de99ffb3e2c6012fb5a4d4e51eb1045354e1fdfa6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dba14cd406ce22c9c069c05363ddfdb8eea310f3f3c2f662b6ab16091e5dbf0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d295f2f8ab1381da7a14b58d065ccff6e28cc18d407e1590e1e42d5d10bcfd9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcd9074dacf53ba7638fb2e762f111dee8244f182d815c91c99dbf2f9ad8ef36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc48bceaca024d42ac70b1660922eba635018550fc07f7b87574545c78ccbcc0(
    value: typing.Optional[PipelineClusterGcpAttributes],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11e4f70e64acf28604292dab99ebb77aeaf3f7e158e06a513fc7b02051b07051(
    *,
    abfss: typing.Optional[typing.Union[PipelineClusterInitScriptsAbfss, typing.Dict[builtins.str, typing.Any]]] = None,
    dbfs: typing.Optional[typing.Union[PipelineClusterInitScriptsDbfs, typing.Dict[builtins.str, typing.Any]]] = None,
    file: typing.Optional[typing.Union[PipelineClusterInitScriptsFile, typing.Dict[builtins.str, typing.Any]]] = None,
    gcs: typing.Optional[typing.Union[PipelineClusterInitScriptsGcs, typing.Dict[builtins.str, typing.Any]]] = None,
    s3: typing.Optional[typing.Union[PipelineClusterInitScriptsS3, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08653553c412d16cc3c394e902d9d9136e1dc270400d97f53c4da3176f9cf921(
    *,
    destination: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__185005a57a242c57b50ff8e2a4ac3ad2b94c3e5b38e46f1164ef3379fbbe15bb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a2f6a45a0d69358944833d6f2782c267d91f62914c38a9a0d2fdafbadddf8cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96427f8ce89f814bd5be8778b1332d7028c186c709b765e73382a0ed77ba48eb(
    value: typing.Optional[PipelineClusterInitScriptsAbfss],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5533972c2f5a5cac1bd2d4a983973d0cd6b9a3b177dc7131d51216e38c2bd072(
    *,
    destination: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__448d6322b8835791794b355fa15b3606a7b4eb170516cfc11f4b5076d1960492(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b58e948cd446d5feb362c7047abda18a12ba88f1047abb9bee05e0a976af25ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccb509849d53df64fb76f3d6a87b6ae85c070cca9a2b91322ab23274e9239b7c(
    value: typing.Optional[PipelineClusterInitScriptsDbfs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e4363a82d617cbd23354845694dd6c1a276a3cb1c9f9d7026cb8690d1df2c4f(
    *,
    destination: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86457c0c1b2c9138116d12c1363dfd74763edf426aa2deb316f55368908f3190(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c47880aabfde119a139292f7cbeae09d4cdc3ec3ebe9a84a7b9327426a63495(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fec62fa063daa67a8514db5a41689d317be9b4bda310efb2687c13cfc8071b74(
    value: typing.Optional[PipelineClusterInitScriptsFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae6bbe01689d68bd971c222bdd368a270b39468c9d7273278c7b691f14021a73(
    *,
    destination: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e236792e6915ed3d932cd48279dfa2c158bee777adf11397aaa72dcf35c10ce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f1fe29b1891eb05ede02df93e62291d089df51836676b49ec4f7eb33cbf59a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5de46d4981b30fbd57aafaa07bca85c69bfd750633274cdd4f38c5524638c95(
    value: typing.Optional[PipelineClusterInitScriptsGcs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38fc39631605a61319335f57d89d34d793b265d37153e7b0437b567aff7c2411(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45554416f127276a9cbcf094733043df94ac27996a009ac7b73404c69d2d6310(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35e4a30035090326e98f9efa5a9b75145ee37b078f127d50e51a09a7dc94c72d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cbcf4965843ebd597e293c33ec0ce451a07ddcadf5383efe496cb0e5d50f4a9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03699ed827890fe6dd7b57e965d7619adf2b33650fc00e324a5db14cf6e8cf73(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60e34009bc40aee52c2744271ce8e51c762e01a0623937b87d780a3913be6c65(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PipelineClusterInitScripts]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b0a46a32c8b8e142dcfa3540c9b27b5037132f5c7bba804865abbbe7c79bf0e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35b39702ca8ed8764270737074675516daea2184430bab8421a959ccebb31af9(
    value: typing.Optional[typing.Union[PipelineClusterInitScripts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39337a1afe9c3ca9f2e4568fa5ef4f3040492f827313cd356c405c34f52dda4f(
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

def _typecheckingstub__5f7ff7a8a78ff172e3583f1c31f812c703695cdec78a79e98917c17c4906885f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0951d76c77bb48847e77a69c806163ff2098b29799a15ee88c23d5c992fa8ac2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d06d8524231383c14d82c88edd51499f1ef5cb3a0f4be35f93a7088ded11b6e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dddc44b09f8cbdc1ef170bfc1a7056a0cf25379f64af854c89a3b48fe3b1968d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c72353dd63ae46e5f64f1094a71ee62c7e78f6b2049ae7dac2ad2ccf1fd7d0d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8f38f89314f81b343f9bf4a609a82534b996876d0d51f54d6fa924d67fa910f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2980afb493f6bf2af038b4a3133b298935d1ab3b19f28f3c4a228d19feefba8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0ceb3236185d3b8b71f6b4c7054321916dc0cdf38a6acba8a1db45a742a21ba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34d56a257e85f0330f8bff84e45de55ef634162194552ec3f9bc88c97f7c2a20(
    value: typing.Optional[PipelineClusterInitScriptsS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f3af632b79691d9a78344feaa1cc8c91ea03ca5f7697d6f8701c6e883086673(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__978c20e712a5c3762741441a7e2edd781c9cc172a2b1d499013c50561bef16cb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be5948a6bceda9e0f2e894aaa5f74c9929db60b502dbc0b46f2a033355b935f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9135d0b63d1f562382c08ca864477fe80cfabbed9e0e5f27c9f9ab2418c048b9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdc3e83321043f7078f71fb5755263d3dc053df38969fa0dfd923985dcb18db0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__287148aeafd7e2738cc4a54f77d69c6e37dca894453f2e6401ac0c0ef113d026(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PipelineCluster]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fef6d754229036077ff0aa744e27db4b04a6999ad0e705a38c62c68cfe33621a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7237256fcb7e09fd66b7cc79d84d9bb6244ee66c47193eff456fec16481a046c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PipelineClusterInitScripts, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9b310a829341c47858043dd2a235f598810c46490d3b2c781aca2bb9ba17a16(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d3438aa4e0bea9b918574c2e222258111f37c98502aa8c07688c5db74d25aee(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d81fa73ad3625ed37e56adf7a272476528ad58f406324d8f35130eb85bfcc50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2b6ca3ec48c370ef7f224f222fa506d46487d019eeaab0378ae5071f9e0fec1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c00e07b577c1634f6ea7bb8d836a0215319cf2db90d875e3567ac69968eb2fa0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d7ed9f9bd311c2601e1614bae259b45959609e849636e4f8ca868fc526c8be8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1b56e9940485ff52d7cdea2ca00769f9b98965cfada5a4f0103523386dabf99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac80b8009125ce2e53f63fef39609721d551de57df36498858a86e55c4c9bcf3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f77463c2c31612d4b0b1420b2303a13604c64db12c37c3652276a516ccfb8c67(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e1c9e1a719372ccabbc0ae57ed97e3ff2492200be81371a2b04fbfb02f224ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73fdaa128f3f554bc373c83787f8233d550eeb91af5020c8ad52531759544913(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd9418ad971d8cf80338ddc35c293fd1764396cc36d154f5d32f7f07b6055a48(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97ab26d0aa329436e8075510b44916e57c9d82c16479680cc3ffc14465991541(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ebf8661f6256cad973e3f9982c9eae2550158a4a964d82957c02e9ed1f0047f(
    value: typing.Optional[typing.Union[PipelineCluster, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ebc2b0023c97b6cd7a6ed7c732dbb538c3f1e0ec54995e635c681ee76ac7b7b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    allow_duplicate_names: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    catalog: typing.Optional[builtins.str] = None,
    channel: typing.Optional[builtins.str] = None,
    cluster: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PipelineCluster, typing.Dict[builtins.str, typing.Any]]]]] = None,
    configuration: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    continuous: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    development: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    edition: typing.Optional[builtins.str] = None,
    filters: typing.Optional[typing.Union[PipelineFilters, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    library: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PipelineLibrary, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: typing.Optional[builtins.str] = None,
    photon: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    storage: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[PipelineTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__400edb976c2c430e3ea0ba9bf6adae5161404b386bc44ad2e9d688fb585dbbf6(
    *,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    include: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f512ba7b8174dad011c60cf8e39ce500b5a7abee82589dabdd62f6d7063dd9c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32f269ba771416f5754c871d4e5defb67eca3e66458c176472fa9c7b4bb0adb3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d6e4c6838df29d1751c879733dbc18de255051fe3e780d2660c331d08e22834(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4cfe1c40e31ba1fdfc9155a7e506df9d0367f987d691732efb4eb447b42042b(
    value: typing.Optional[PipelineFilters],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab38672557257f0630447a3266e7e9ca34eb43708590325a7db3b838bc1944ed(
    *,
    file: typing.Optional[typing.Union[PipelineLibraryFile, typing.Dict[builtins.str, typing.Any]]] = None,
    jar: typing.Optional[builtins.str] = None,
    maven: typing.Optional[typing.Union[PipelineLibraryMaven, typing.Dict[builtins.str, typing.Any]]] = None,
    notebook: typing.Optional[typing.Union[PipelineLibraryNotebook, typing.Dict[builtins.str, typing.Any]]] = None,
    whl: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__551fe51a4b40af94c68a838b1e62617bb3265f541b41bf724bbbd6169142b716(
    *,
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7b6edb54bd6ec5340fc07503cde089bc3f8ebc749e784647ee26c64a855a555(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30020fded81167ba7c24465924bc6819c87b8729a08dd352841f5cadfc74dddb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4385f097751ff3ac4405e398304569e877d9d2c8784c609ea774110fb68e452(
    value: typing.Optional[PipelineLibraryFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feaec27d96d60deadc7de92023d7d861bd8addb2f0b3cb79b7b0de97a20f3345(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc577537d2cf384188b3811901416027d64926f7259e5f8a6e326f71c3b8194d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cade30eb558d3005bdd87d3efc7a9fc5972c2d437d7e227dc2bea669cf99fd74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8da48c46afba76ff9d82cd2b3366dd3c0cd2444dee99ad04104260ead7d8c7b3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e57bbb07f0dd56852ff85c2ade6690513556172b49a9302ecdaf005230b4166(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4572654c3fe5ff96fb45731a68d0ed414a7e518f2cbe692f44812c591467f05(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PipelineLibrary]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__145952f0dfd595687f0284616a7953b02be0e5b6cef88142af4996d6917883ae(
    *,
    coordinates: builtins.str,
    exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
    repo: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f256e1ecd65b00c87dca99df78c18328d02c273ba8607a750532f28e25762b0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae68527922d89feac3decb13f689acf3ef54a360f78e372391b54d377dad0299(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9f81b5f947bebb3f1df0607ccefb6d5024955a67d5aa8818a3582f9546843e6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9455e9c03e1221a7208c60581916b32f97415d96011cc20a38187eae5db91ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c917c0280b945797d7da35f4dff4ef82a596624eb54fc4addc1abde35ef9df5(
    value: typing.Optional[PipelineLibraryMaven],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85b6ecd237605f3d008151a2bc4b0dc57e33743c60e08ea76c200273fd3beb35(
    *,
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bc19f67b6de2c849df0710c250dc9c8fad562ba0fbd56e842249bd9704afc17(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d0620d988160f2fb6fcf17c4a5fc76877e30e8a8a681844e83c16bd74624407(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__145cabadfb54f3504212d46d8ec884e48caf91f904ac400f67e4d10424332121(
    value: typing.Optional[PipelineLibraryNotebook],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3006c66944f9e4cb49c3bf1da0675631e8468f51e5989e8ebb77f1178094a652(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59dd279518b209ef52f3ff45e4288c809f867b19f9204b6b7639c3737e7c0e9a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9956a6832673bcc10c330ce08b0e458a7ee78867c7ccfe82f91bc5efd3ff661(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a599d39b6908e198c20ee7ea1e21a2fc074b3e03bfd88a19bfe4c23811cb4e3(
    value: typing.Optional[typing.Union[PipelineLibrary, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b598ef82f6f5d047e374b06f5a0f512cd2886df2602573765841224259b1d81(
    *,
    default: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b1a5fe602fef6f78bae83ea42ac93d4f1b437163e8523763fa1b22bf9c5e113(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f63a2a6c4d709c183fb036acc80e081fd3dba3b850d13f48f08711108363bef4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c09495cab5573697f3dff8a616df10342c467910b158e35fc9e109963be856b(
    value: typing.Optional[typing.Union[PipelineTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
