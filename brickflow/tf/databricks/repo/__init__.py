'''
# `databricks_repo`

Refer to the Terraform Registory for docs: [`databricks_repo`](https://www.terraform.io/docs/providers/databricks/r/repo).
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


class Repo(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.repo.Repo",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/repo databricks_repo}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        url: builtins.str,
        branch: typing.Optional[builtins.str] = None,
        commit_hash: typing.Optional[builtins.str] = None,
        git_provider: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        sparse_checkout: typing.Optional[typing.Union["RepoSparseCheckout", typing.Dict[builtins.str, typing.Any]]] = None,
        tag: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/repo databricks_repo} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#url Repo#url}.
        :param branch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#branch Repo#branch}.
        :param commit_hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#commit_hash Repo#commit_hash}.
        :param git_provider: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#git_provider Repo#git_provider}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#id Repo#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#path Repo#path}.
        :param sparse_checkout: sparse_checkout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#sparse_checkout Repo#sparse_checkout}
        :param tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#tag Repo#tag}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9387c7f061b8825d073f60e9122749b6aa07cc0bdeeb33fb292ce84624a81eb8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RepoConfig(
            url=url,
            branch=branch,
            commit_hash=commit_hash,
            git_provider=git_provider,
            id=id,
            path=path,
            sparse_checkout=sparse_checkout,
            tag=tag,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putSparseCheckout")
    def put_sparse_checkout(self, *, patterns: typing.Sequence[builtins.str]) -> None:
        '''
        :param patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#patterns Repo#patterns}.
        '''
        value = RepoSparseCheckout(patterns=patterns)

        return typing.cast(None, jsii.invoke(self, "putSparseCheckout", [value]))

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetCommitHash")
    def reset_commit_hash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommitHash", []))

    @jsii.member(jsii_name="resetGitProvider")
    def reset_git_provider(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitProvider", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetSparseCheckout")
    def reset_sparse_checkout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparseCheckout", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="sparseCheckout")
    def sparse_checkout(self) -> "RepoSparseCheckoutOutputReference":
        return typing.cast("RepoSparseCheckoutOutputReference", jsii.get(self, "sparseCheckout"))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="commitHashInput")
    def commit_hash_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commitHashInput"))

    @builtins.property
    @jsii.member(jsii_name="gitProviderInput")
    def git_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gitProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="sparseCheckoutInput")
    def sparse_checkout_input(self) -> typing.Optional["RepoSparseCheckout"]:
        return typing.cast(typing.Optional["RepoSparseCheckout"], jsii.get(self, "sparseCheckoutInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7232f077787ab04b641ba404ce15ac9cbac7535436f8cf517027e9c3ab649b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="commitHash")
    def commit_hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commitHash"))

    @commit_hash.setter
    def commit_hash(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e1709f94dd99fc88527b0b98931754409a9dddaa906c8d9208d464e29097e53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commitHash", value)

    @builtins.property
    @jsii.member(jsii_name="gitProvider")
    def git_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gitProvider"))

    @git_provider.setter
    def git_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbe1c89a042a80b1f37fca33edacd6316a6ae350cd1607476457dbdafc01f389)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gitProvider", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf0fa62e6b8fc387153d6cca8e7150a2e91a5fe19cbea097a264c556f8b5e230)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62c13110c585d09382275309de92c572fe7d752e34de6f53cec7faeb0c40289b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2083e3008b6a01994c506775d8fd4380222b16a70b85540204abc8a6ff519b10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4ff1287de725339952e1e40e74211d7f53e4bebccd32fa70db0d96efce3a91d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)


@jsii.data_type(
    jsii_type="databricks.repo.RepoConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "url": "url",
        "branch": "branch",
        "commit_hash": "commitHash",
        "git_provider": "gitProvider",
        "id": "id",
        "path": "path",
        "sparse_checkout": "sparseCheckout",
        "tag": "tag",
    },
)
class RepoConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        url: builtins.str,
        branch: typing.Optional[builtins.str] = None,
        commit_hash: typing.Optional[builtins.str] = None,
        git_provider: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        sparse_checkout: typing.Optional[typing.Union["RepoSparseCheckout", typing.Dict[builtins.str, typing.Any]]] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#url Repo#url}.
        :param branch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#branch Repo#branch}.
        :param commit_hash: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#commit_hash Repo#commit_hash}.
        :param git_provider: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#git_provider Repo#git_provider}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#id Repo#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#path Repo#path}.
        :param sparse_checkout: sparse_checkout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#sparse_checkout Repo#sparse_checkout}
        :param tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#tag Repo#tag}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(sparse_checkout, dict):
            sparse_checkout = RepoSparseCheckout(**sparse_checkout)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55ff8a17f304af88ef89be4f0f10c8ffaba9785a7a41ae7b547354d8bd4fdc05)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument commit_hash", value=commit_hash, expected_type=type_hints["commit_hash"])
            check_type(argname="argument git_provider", value=git_provider, expected_type=type_hints["git_provider"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument sparse_checkout", value=sparse_checkout, expected_type=type_hints["sparse_checkout"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
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
        if branch is not None:
            self._values["branch"] = branch
        if commit_hash is not None:
            self._values["commit_hash"] = commit_hash
        if git_provider is not None:
            self._values["git_provider"] = git_provider
        if id is not None:
            self._values["id"] = id
        if path is not None:
            self._values["path"] = path
        if sparse_checkout is not None:
            self._values["sparse_checkout"] = sparse_checkout
        if tag is not None:
            self._values["tag"] = tag

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
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#url Repo#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#branch Repo#branch}.'''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def commit_hash(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#commit_hash Repo#commit_hash}.'''
        result = self._values.get("commit_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def git_provider(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#git_provider Repo#git_provider}.'''
        result = self._values.get("git_provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#id Repo#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#path Repo#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sparse_checkout(self) -> typing.Optional["RepoSparseCheckout"]:
        '''sparse_checkout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#sparse_checkout Repo#sparse_checkout}
        '''
        result = self._values.get("sparse_checkout")
        return typing.cast(typing.Optional["RepoSparseCheckout"], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#tag Repo#tag}.'''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepoConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="databricks.repo.RepoSparseCheckout",
    jsii_struct_bases=[],
    name_mapping={"patterns": "patterns"},
)
class RepoSparseCheckout:
    def __init__(self, *, patterns: typing.Sequence[builtins.str]) -> None:
        '''
        :param patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#patterns Repo#patterns}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1610a3467884f04cd3cc5074de988a7af0a154979538c36a87577f73d6f582df)
            check_type(argname="argument patterns", value=patterns, expected_type=type_hints["patterns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "patterns": patterns,
        }

    @builtins.property
    def patterns(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/repo#patterns Repo#patterns}.'''
        result = self._values.get("patterns")
        assert result is not None, "Required property 'patterns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepoSparseCheckout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RepoSparseCheckoutOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.repo.RepoSparseCheckoutOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c1870a85072d3f01a3cc92ef437334aefb2f5e5b830b61f4a99ddeeac6db55f3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="patternsInput")
    def patterns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "patternsInput"))

    @builtins.property
    @jsii.member(jsii_name="patterns")
    def patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "patterns"))

    @patterns.setter
    def patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e78de6bac9d8ace558ca568655607eebf08c82a0ecf11a47c236456eafe5db31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "patterns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RepoSparseCheckout]:
        return typing.cast(typing.Optional[RepoSparseCheckout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RepoSparseCheckout]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a4066dce80c3d73590a5cf39e1e75af84acdca69cb484791a296dd35bc041f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Repo",
    "RepoConfig",
    "RepoSparseCheckout",
    "RepoSparseCheckoutOutputReference",
]

publication.publish()

def _typecheckingstub__9387c7f061b8825d073f60e9122749b6aa07cc0bdeeb33fb292ce84624a81eb8(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    url: builtins.str,
    branch: typing.Optional[builtins.str] = None,
    commit_hash: typing.Optional[builtins.str] = None,
    git_provider: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
    sparse_checkout: typing.Optional[typing.Union[RepoSparseCheckout, typing.Dict[builtins.str, typing.Any]]] = None,
    tag: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__a7232f077787ab04b641ba404ce15ac9cbac7535436f8cf517027e9c3ab649b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e1709f94dd99fc88527b0b98931754409a9dddaa906c8d9208d464e29097e53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbe1c89a042a80b1f37fca33edacd6316a6ae350cd1607476457dbdafc01f389(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf0fa62e6b8fc387153d6cca8e7150a2e91a5fe19cbea097a264c556f8b5e230(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62c13110c585d09382275309de92c572fe7d752e34de6f53cec7faeb0c40289b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2083e3008b6a01994c506775d8fd4380222b16a70b85540204abc8a6ff519b10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4ff1287de725339952e1e40e74211d7f53e4bebccd32fa70db0d96efce3a91d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55ff8a17f304af88ef89be4f0f10c8ffaba9785a7a41ae7b547354d8bd4fdc05(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    url: builtins.str,
    branch: typing.Optional[builtins.str] = None,
    commit_hash: typing.Optional[builtins.str] = None,
    git_provider: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
    sparse_checkout: typing.Optional[typing.Union[RepoSparseCheckout, typing.Dict[builtins.str, typing.Any]]] = None,
    tag: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1610a3467884f04cd3cc5074de988a7af0a154979538c36a87577f73d6f582df(
    *,
    patterns: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1870a85072d3f01a3cc92ef437334aefb2f5e5b830b61f4a99ddeeac6db55f3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e78de6bac9d8ace558ca568655607eebf08c82a0ecf11a47c236456eafe5db31(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a4066dce80c3d73590a5cf39e1e75af84acdca69cb484791a296dd35bc041f6(
    value: typing.Optional[RepoSparseCheckout],
) -> None:
    """Type checking stubs"""
    pass
