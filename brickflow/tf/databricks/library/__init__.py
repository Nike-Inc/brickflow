'''
# `databricks_library`

Refer to the Terraform Registory for docs: [`databricks_library`](https://www.terraform.io/docs/providers/databricks/r/library).
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


class Library(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.library.Library",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/library databricks_library}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        cluster_id: builtins.str,
        cran: typing.Optional[typing.Union["LibraryCran", typing.Dict[builtins.str, typing.Any]]] = None,
        egg: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        jar: typing.Optional[builtins.str] = None,
        maven: typing.Optional[typing.Union["LibraryMaven", typing.Dict[builtins.str, typing.Any]]] = None,
        pypi: typing.Optional[typing.Union["LibraryPypi", typing.Dict[builtins.str, typing.Any]]] = None,
        whl: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/library databricks_library} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#cluster_id Library#cluster_id}.
        :param cran: cran block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#cran Library#cran}
        :param egg: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#egg Library#egg}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#id Library#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param jar: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#jar Library#jar}.
        :param maven: maven block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#maven Library#maven}
        :param pypi: pypi block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#pypi Library#pypi}
        :param whl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#whl Library#whl}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7415031307c4eeffe20e31fc1f3e9b97da59fdd590ce756893d17ff62ee7937)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LibraryConfig(
            cluster_id=cluster_id,
            cran=cran,
            egg=egg,
            id=id,
            jar=jar,
            maven=maven,
            pypi=pypi,
            whl=whl,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCran")
    def put_cran(
        self,
        *,
        package: builtins.str,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param package: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#package Library#package}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#repo Library#repo}.
        '''
        value = LibraryCran(package=package, repo=repo)

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
        :param coordinates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#coordinates Library#coordinates}.
        :param exclusions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#exclusions Library#exclusions}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#repo Library#repo}.
        '''
        value = LibraryMaven(coordinates=coordinates, exclusions=exclusions, repo=repo)

        return typing.cast(None, jsii.invoke(self, "putMaven", [value]))

    @jsii.member(jsii_name="putPypi")
    def put_pypi(
        self,
        *,
        package: builtins.str,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param package: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#package Library#package}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#repo Library#repo}.
        '''
        value = LibraryPypi(package=package, repo=repo)

        return typing.cast(None, jsii.invoke(self, "putPypi", [value]))

    @jsii.member(jsii_name="resetCran")
    def reset_cran(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCran", []))

    @jsii.member(jsii_name="resetEgg")
    def reset_egg(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgg", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="cran")
    def cran(self) -> "LibraryCranOutputReference":
        return typing.cast("LibraryCranOutputReference", jsii.get(self, "cran"))

    @builtins.property
    @jsii.member(jsii_name="maven")
    def maven(self) -> "LibraryMavenOutputReference":
        return typing.cast("LibraryMavenOutputReference", jsii.get(self, "maven"))

    @builtins.property
    @jsii.member(jsii_name="pypi")
    def pypi(self) -> "LibraryPypiOutputReference":
        return typing.cast("LibraryPypiOutputReference", jsii.get(self, "pypi"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cranInput")
    def cran_input(self) -> typing.Optional["LibraryCran"]:
        return typing.cast(typing.Optional["LibraryCran"], jsii.get(self, "cranInput"))

    @builtins.property
    @jsii.member(jsii_name="eggInput")
    def egg_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eggInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="jarInput")
    def jar_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jarInput"))

    @builtins.property
    @jsii.member(jsii_name="mavenInput")
    def maven_input(self) -> typing.Optional["LibraryMaven"]:
        return typing.cast(typing.Optional["LibraryMaven"], jsii.get(self, "mavenInput"))

    @builtins.property
    @jsii.member(jsii_name="pypiInput")
    def pypi_input(self) -> typing.Optional["LibraryPypi"]:
        return typing.cast(typing.Optional["LibraryPypi"], jsii.get(self, "pypiInput"))

    @builtins.property
    @jsii.member(jsii_name="whlInput")
    def whl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whlInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c76a22fa327f1429b24c9b43949ed0a32b67b035927b5ea63d038b7593a8fc89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="egg")
    def egg(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "egg"))

    @egg.setter
    def egg(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fb8fcc0763c9fabfd52c642def959a45da032dd4eb7f0cbaac6b1b4368bc194)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egg", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb4e004eaaa82f42b42dfc8d2ec3aeb4bd23c36c933a0c37f8cae6a7c1cc770f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="jar")
    def jar(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jar"))

    @jar.setter
    def jar(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26009f717bc1e9ebca0a0f22f83f3e31d17ff59875df9b71680d6c69fc230a4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jar", value)

    @builtins.property
    @jsii.member(jsii_name="whl")
    def whl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "whl"))

    @whl.setter
    def whl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b3bf3be4b3f7de82d4db3ef33b85d5d75cb7d5e32f731d6f8d6b7fd76344fe6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whl", value)


@jsii.data_type(
    jsii_type="databricks.library.LibraryConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cluster_id": "clusterId",
        "cran": "cran",
        "egg": "egg",
        "id": "id",
        "jar": "jar",
        "maven": "maven",
        "pypi": "pypi",
        "whl": "whl",
    },
)
class LibraryConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        cluster_id: builtins.str,
        cran: typing.Optional[typing.Union["LibraryCran", typing.Dict[builtins.str, typing.Any]]] = None,
        egg: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        jar: typing.Optional[builtins.str] = None,
        maven: typing.Optional[typing.Union["LibraryMaven", typing.Dict[builtins.str, typing.Any]]] = None,
        pypi: typing.Optional[typing.Union["LibraryPypi", typing.Dict[builtins.str, typing.Any]]] = None,
        whl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#cluster_id Library#cluster_id}.
        :param cran: cran block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#cran Library#cran}
        :param egg: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#egg Library#egg}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#id Library#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param jar: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#jar Library#jar}.
        :param maven: maven block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#maven Library#maven}
        :param pypi: pypi block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#pypi Library#pypi}
        :param whl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#whl Library#whl}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cran, dict):
            cran = LibraryCran(**cran)
        if isinstance(maven, dict):
            maven = LibraryMaven(**maven)
        if isinstance(pypi, dict):
            pypi = LibraryPypi(**pypi)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70c4ab0b2c8cb3a34010308f13c5ceafacc85830f9de2b07eef1db931c16abbd)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument cran", value=cran, expected_type=type_hints["cran"])
            check_type(argname="argument egg", value=egg, expected_type=type_hints["egg"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument jar", value=jar, expected_type=type_hints["jar"])
            check_type(argname="argument maven", value=maven, expected_type=type_hints["maven"])
            check_type(argname="argument pypi", value=pypi, expected_type=type_hints["pypi"])
            check_type(argname="argument whl", value=whl, expected_type=type_hints["whl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_id": cluster_id,
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
        if cran is not None:
            self._values["cran"] = cran
        if egg is not None:
            self._values["egg"] = egg
        if id is not None:
            self._values["id"] = id
        if jar is not None:
            self._values["jar"] = jar
        if maven is not None:
            self._values["maven"] = maven
        if pypi is not None:
            self._values["pypi"] = pypi
        if whl is not None:
            self._values["whl"] = whl

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
    def cluster_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#cluster_id Library#cluster_id}.'''
        result = self._values.get("cluster_id")
        assert result is not None, "Required property 'cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cran(self) -> typing.Optional["LibraryCran"]:
        '''cran block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#cran Library#cran}
        '''
        result = self._values.get("cran")
        return typing.cast(typing.Optional["LibraryCran"], result)

    @builtins.property
    def egg(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#egg Library#egg}.'''
        result = self._values.get("egg")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#id Library#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jar(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#jar Library#jar}.'''
        result = self._values.get("jar")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maven(self) -> typing.Optional["LibraryMaven"]:
        '''maven block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#maven Library#maven}
        '''
        result = self._values.get("maven")
        return typing.cast(typing.Optional["LibraryMaven"], result)

    @builtins.property
    def pypi(self) -> typing.Optional["LibraryPypi"]:
        '''pypi block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#pypi Library#pypi}
        '''
        result = self._values.get("pypi")
        return typing.cast(typing.Optional["LibraryPypi"], result)

    @builtins.property
    def whl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#whl Library#whl}.'''
        result = self._values.get("whl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LibraryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.library.LibraryCran",
    jsii_struct_bases=[],
    name_mapping={"package": "package", "repo": "repo"},
)
class LibraryCran:
    def __init__(
        self,
        *,
        package: builtins.str,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param package: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#package Library#package}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#repo Library#repo}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03cebfff3c5292910248090275f9a9110fae68e4fdef5721b0a39df182cffbc3)
            check_type(argname="argument package", value=package, expected_type=type_hints["package"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "package": package,
        }
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def package(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#package Library#package}.'''
        result = self._values.get("package")
        assert result is not None, "Required property 'package' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#repo Library#repo}.'''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LibraryCran(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LibraryCranOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.library.LibraryCranOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d3772a4956fcbe3cfa79ab7fa9bd3c206204e54124b3df42691351e7e306b0be)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c5b5c5a8e4e374ebf63c131cb27707f5de378b55354df15ad9512c669830fc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "package", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9858e3b43f55d3aa8853d1f251c3a211b52efe15662f37c35bc5dd8e448c5e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LibraryCran]:
        return typing.cast(typing.Optional[LibraryCran], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LibraryCran]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06582608102b2ceae934ec54af55e045b753b8a94ce93fbb996010d92ba48ea3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.library.LibraryMaven",
    jsii_struct_bases=[],
    name_mapping={
        "coordinates": "coordinates",
        "exclusions": "exclusions",
        "repo": "repo",
    },
)
class LibraryMaven:
    def __init__(
        self,
        *,
        coordinates: builtins.str,
        exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param coordinates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#coordinates Library#coordinates}.
        :param exclusions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#exclusions Library#exclusions}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#repo Library#repo}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5540259384c7fbc8766ea32fccb22d43dbbb3ba876548432b439b3f0361a0a97)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#coordinates Library#coordinates}.'''
        result = self._values.get("coordinates")
        assert result is not None, "Required property 'coordinates' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclusions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#exclusions Library#exclusions}.'''
        result = self._values.get("exclusions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#repo Library#repo}.'''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LibraryMaven(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LibraryMavenOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.library.LibraryMavenOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2abc953dadc70f1685db8e551c32dd451ad26e2b8af0af4839ff741500fde093)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad4975bdca4a99251122b8339836e1d4552099935ec167ffc61a65e51a0170c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coordinates", value)

    @builtins.property
    @jsii.member(jsii_name="exclusions")
    def exclusions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclusions"))

    @exclusions.setter
    def exclusions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dd40d4793dc4b95c9c5c30d68e80355f375a89830ad34b77ac5e8e7fa98cb50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusions", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__899e40ce4e14a4915862758efa53f8726dff5acd01585b5f683a64100127c65f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LibraryMaven]:
        return typing.cast(typing.Optional[LibraryMaven], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LibraryMaven]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d88919722039d3bd427393fb0cb0e8beabf23e0712c4e1868eff403d658e7aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.library.LibraryPypi",
    jsii_struct_bases=[],
    name_mapping={"package": "package", "repo": "repo"},
)
class LibraryPypi:
    def __init__(
        self,
        *,
        package: builtins.str,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param package: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#package Library#package}.
        :param repo: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#repo Library#repo}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ca600c3ff05c67d2732beb54512acdb4c66d2fee5c1659996a76c556a20ab5b)
            check_type(argname="argument package", value=package, expected_type=type_hints["package"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "package": package,
        }
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def package(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#package Library#package}.'''
        result = self._values.get("package")
        assert result is not None, "Required property 'package' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/library#repo Library#repo}.'''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LibraryPypi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LibraryPypiOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.library.LibraryPypiOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__44b40dd73cadc9ae47ab3e7c93f8eb2cf30fa702c2e2588eadfab6815e76a77d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__07ef40b6d72e171b6ccd76c4b526240608e2aecf795624602a3fb5b4aedac916)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "package", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dffb5c8067c7cb3b381c8de2c1ee9095146c1999a6f13b711f7b97fa25819392)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LibraryPypi]:
        return typing.cast(typing.Optional[LibraryPypi], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LibraryPypi]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f61e07a20f10f940f7febd832f67fd2697771ff4ef0dd191d1ffc3320a2b6e54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Library",
    "LibraryConfig",
    "LibraryCran",
    "LibraryCranOutputReference",
    "LibraryMaven",
    "LibraryMavenOutputReference",
    "LibraryPypi",
    "LibraryPypiOutputReference",
]

publication.publish()

def _typecheckingstub__b7415031307c4eeffe20e31fc1f3e9b97da59fdd590ce756893d17ff62ee7937(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    cluster_id: builtins.str,
    cran: typing.Optional[typing.Union[LibraryCran, typing.Dict[builtins.str, typing.Any]]] = None,
    egg: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    jar: typing.Optional[builtins.str] = None,
    maven: typing.Optional[typing.Union[LibraryMaven, typing.Dict[builtins.str, typing.Any]]] = None,
    pypi: typing.Optional[typing.Union[LibraryPypi, typing.Dict[builtins.str, typing.Any]]] = None,
    whl: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__c76a22fa327f1429b24c9b43949ed0a32b67b035927b5ea63d038b7593a8fc89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fb8fcc0763c9fabfd52c642def959a45da032dd4eb7f0cbaac6b1b4368bc194(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb4e004eaaa82f42b42dfc8d2ec3aeb4bd23c36c933a0c37f8cae6a7c1cc770f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26009f717bc1e9ebca0a0f22f83f3e31d17ff59875df9b71680d6c69fc230a4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b3bf3be4b3f7de82d4db3ef33b85d5d75cb7d5e32f731d6f8d6b7fd76344fe6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70c4ab0b2c8cb3a34010308f13c5ceafacc85830f9de2b07eef1db931c16abbd(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cluster_id: builtins.str,
    cran: typing.Optional[typing.Union[LibraryCran, typing.Dict[builtins.str, typing.Any]]] = None,
    egg: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    jar: typing.Optional[builtins.str] = None,
    maven: typing.Optional[typing.Union[LibraryMaven, typing.Dict[builtins.str, typing.Any]]] = None,
    pypi: typing.Optional[typing.Union[LibraryPypi, typing.Dict[builtins.str, typing.Any]]] = None,
    whl: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03cebfff3c5292910248090275f9a9110fae68e4fdef5721b0a39df182cffbc3(
    *,
    package: builtins.str,
    repo: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3772a4956fcbe3cfa79ab7fa9bd3c206204e54124b3df42691351e7e306b0be(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c5b5c5a8e4e374ebf63c131cb27707f5de378b55354df15ad9512c669830fc8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9858e3b43f55d3aa8853d1f251c3a211b52efe15662f37c35bc5dd8e448c5e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06582608102b2ceae934ec54af55e045b753b8a94ce93fbb996010d92ba48ea3(
    value: typing.Optional[LibraryCran],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5540259384c7fbc8766ea32fccb22d43dbbb3ba876548432b439b3f0361a0a97(
    *,
    coordinates: builtins.str,
    exclusions: typing.Optional[typing.Sequence[builtins.str]] = None,
    repo: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2abc953dadc70f1685db8e551c32dd451ad26e2b8af0af4839ff741500fde093(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad4975bdca4a99251122b8339836e1d4552099935ec167ffc61a65e51a0170c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dd40d4793dc4b95c9c5c30d68e80355f375a89830ad34b77ac5e8e7fa98cb50(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__899e40ce4e14a4915862758efa53f8726dff5acd01585b5f683a64100127c65f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d88919722039d3bd427393fb0cb0e8beabf23e0712c4e1868eff403d658e7aa(
    value: typing.Optional[LibraryMaven],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ca600c3ff05c67d2732beb54512acdb4c66d2fee5c1659996a76c556a20ab5b(
    *,
    package: builtins.str,
    repo: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44b40dd73cadc9ae47ab3e7c93f8eb2cf30fa702c2e2588eadfab6815e76a77d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07ef40b6d72e171b6ccd76c4b526240608e2aecf795624602a3fb5b4aedac916(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dffb5c8067c7cb3b381c8de2c1ee9095146c1999a6f13b711f7b97fa25819392(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f61e07a20f10f940f7febd832f67fd2697771ff4ef0dd191d1ffc3320a2b6e54(
    value: typing.Optional[LibraryPypi],
) -> None:
    """Type checking stubs"""
    pass
