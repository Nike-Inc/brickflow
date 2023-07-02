'''
# `databricks_permissions`

Refer to the Terraform Registory for docs: [`databricks_permissions`](https://www.terraform.io/docs/providers/databricks/r/permissions).
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


class Permissions(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.permissions.Permissions",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/permissions databricks_permissions}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        access_control: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PermissionsAccessControl", typing.Dict[builtins.str, typing.Any]]]],
        authorization: typing.Optional[builtins.str] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        cluster_policy_id: typing.Optional[builtins.str] = None,
        directory_id: typing.Optional[builtins.str] = None,
        directory_path: typing.Optional[builtins.str] = None,
        experiment_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        instance_pool_id: typing.Optional[builtins.str] = None,
        job_id: typing.Optional[builtins.str] = None,
        notebook_id: typing.Optional[builtins.str] = None,
        notebook_path: typing.Optional[builtins.str] = None,
        object_type: typing.Optional[builtins.str] = None,
        pipeline_id: typing.Optional[builtins.str] = None,
        registered_model_id: typing.Optional[builtins.str] = None,
        repo_id: typing.Optional[builtins.str] = None,
        repo_path: typing.Optional[builtins.str] = None,
        sql_alert_id: typing.Optional[builtins.str] = None,
        sql_dashboard_id: typing.Optional[builtins.str] = None,
        sql_endpoint_id: typing.Optional[builtins.str] = None,
        sql_query_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/permissions databricks_permissions} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param access_control: access_control block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#access_control Permissions#access_control}
        :param authorization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#authorization Permissions#authorization}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#cluster_id Permissions#cluster_id}.
        :param cluster_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#cluster_policy_id Permissions#cluster_policy_id}.
        :param directory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#directory_id Permissions#directory_id}.
        :param directory_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#directory_path Permissions#directory_path}.
        :param experiment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#experiment_id Permissions#experiment_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#id Permissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#instance_pool_id Permissions#instance_pool_id}.
        :param job_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#job_id Permissions#job_id}.
        :param notebook_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#notebook_id Permissions#notebook_id}.
        :param notebook_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#notebook_path Permissions#notebook_path}.
        :param object_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#object_type Permissions#object_type}.
        :param pipeline_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#pipeline_id Permissions#pipeline_id}.
        :param registered_model_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#registered_model_id Permissions#registered_model_id}.
        :param repo_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#repo_id Permissions#repo_id}.
        :param repo_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#repo_path Permissions#repo_path}.
        :param sql_alert_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#sql_alert_id Permissions#sql_alert_id}.
        :param sql_dashboard_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#sql_dashboard_id Permissions#sql_dashboard_id}.
        :param sql_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#sql_endpoint_id Permissions#sql_endpoint_id}.
        :param sql_query_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#sql_query_id Permissions#sql_query_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__213f4267377282fa03303ffaac106931ae364eb78331bf18eb0e55bf22d47923)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PermissionsConfig(
            access_control=access_control,
            authorization=authorization,
            cluster_id=cluster_id,
            cluster_policy_id=cluster_policy_id,
            directory_id=directory_id,
            directory_path=directory_path,
            experiment_id=experiment_id,
            id=id,
            instance_pool_id=instance_pool_id,
            job_id=job_id,
            notebook_id=notebook_id,
            notebook_path=notebook_path,
            object_type=object_type,
            pipeline_id=pipeline_id,
            registered_model_id=registered_model_id,
            repo_id=repo_id,
            repo_path=repo_path,
            sql_alert_id=sql_alert_id,
            sql_dashboard_id=sql_dashboard_id,
            sql_endpoint_id=sql_endpoint_id,
            sql_query_id=sql_query_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAccessControl")
    def put_access_control(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PermissionsAccessControl", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a22d3ca55914593e30c2dfa2dc73e7431b78743621030ffa7410454838c55de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccessControl", [value]))

    @jsii.member(jsii_name="resetAuthorization")
    def reset_authorization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorization", []))

    @jsii.member(jsii_name="resetClusterId")
    def reset_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterId", []))

    @jsii.member(jsii_name="resetClusterPolicyId")
    def reset_cluster_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterPolicyId", []))

    @jsii.member(jsii_name="resetDirectoryId")
    def reset_directory_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectoryId", []))

    @jsii.member(jsii_name="resetDirectoryPath")
    def reset_directory_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectoryPath", []))

    @jsii.member(jsii_name="resetExperimentId")
    def reset_experiment_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExperimentId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstancePoolId")
    def reset_instance_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancePoolId", []))

    @jsii.member(jsii_name="resetJobId")
    def reset_job_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobId", []))

    @jsii.member(jsii_name="resetNotebookId")
    def reset_notebook_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotebookId", []))

    @jsii.member(jsii_name="resetNotebookPath")
    def reset_notebook_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotebookPath", []))

    @jsii.member(jsii_name="resetObjectType")
    def reset_object_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjectType", []))

    @jsii.member(jsii_name="resetPipelineId")
    def reset_pipeline_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPipelineId", []))

    @jsii.member(jsii_name="resetRegisteredModelId")
    def reset_registered_model_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegisteredModelId", []))

    @jsii.member(jsii_name="resetRepoId")
    def reset_repo_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepoId", []))

    @jsii.member(jsii_name="resetRepoPath")
    def reset_repo_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepoPath", []))

    @jsii.member(jsii_name="resetSqlAlertId")
    def reset_sql_alert_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlAlertId", []))

    @jsii.member(jsii_name="resetSqlDashboardId")
    def reset_sql_dashboard_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlDashboardId", []))

    @jsii.member(jsii_name="resetSqlEndpointId")
    def reset_sql_endpoint_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlEndpointId", []))

    @jsii.member(jsii_name="resetSqlQueryId")
    def reset_sql_query_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqlQueryId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accessControl")
    def access_control(self) -> "PermissionsAccessControlList":
        return typing.cast("PermissionsAccessControlList", jsii.get(self, "accessControl"))

    @builtins.property
    @jsii.member(jsii_name="accessControlInput")
    def access_control_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PermissionsAccessControl"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PermissionsAccessControl"]]], jsii.get(self, "accessControlInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizationInput")
    def authorization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterPolicyIdInput")
    def cluster_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryIdInput")
    def directory_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryPathInput")
    def directory_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryPathInput"))

    @builtins.property
    @jsii.member(jsii_name="experimentIdInput")
    def experiment_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "experimentIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolIdInput")
    def instance_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instancePoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="jobIdInput")
    def job_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobIdInput"))

    @builtins.property
    @jsii.member(jsii_name="notebookIdInput")
    def notebook_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notebookIdInput"))

    @builtins.property
    @jsii.member(jsii_name="notebookPathInput")
    def notebook_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notebookPathInput"))

    @builtins.property
    @jsii.member(jsii_name="objectTypeInput")
    def object_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="pipelineIdInput")
    def pipeline_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pipelineIdInput"))

    @builtins.property
    @jsii.member(jsii_name="registeredModelIdInput")
    def registered_model_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registeredModelIdInput"))

    @builtins.property
    @jsii.member(jsii_name="repoIdInput")
    def repo_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoIdInput"))

    @builtins.property
    @jsii.member(jsii_name="repoPathInput")
    def repo_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoPathInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlAlertIdInput")
    def sql_alert_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlAlertIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlDashboardIdInput")
    def sql_dashboard_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlDashboardIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlEndpointIdInput")
    def sql_endpoint_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlEndpointIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlQueryIdInput")
    def sql_query_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlQueryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="authorization")
    def authorization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorization"))

    @authorization.setter
    def authorization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__915783a9f2f364750b7d1bf6b969ed4a9c9e01a140bf478a0a485d575619448f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorization", value)

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__472a7034eb650e04db013bb575e338377a57a2a8cc937acdcb40bed011a76d4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="clusterPolicyId")
    def cluster_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterPolicyId"))

    @cluster_policy_id.setter
    def cluster_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c07acbb5d41cc4158a79b000c850ff743e42f9decff00eb99a7b69d96e9853ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterPolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="directoryId")
    def directory_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryId"))

    @directory_id.setter
    def directory_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__203bddbc9e3acd97bf7afe194eb2e0c9cc0ae87f1138eea4ac4941595ff97f11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryId", value)

    @builtins.property
    @jsii.member(jsii_name="directoryPath")
    def directory_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryPath"))

    @directory_path.setter
    def directory_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa75b995b8e650cea3b63bfb686c1ae8c21256c4bd71144ee93d3e6f408aac4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryPath", value)

    @builtins.property
    @jsii.member(jsii_name="experimentId")
    def experiment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "experimentId"))

    @experiment_id.setter
    def experiment_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc31e406e2fa89a2f4202373a36e60b4a1566d700bf3053c2eafc7351d301b98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "experimentId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efd8ff75f5b79f501b1cffe72ad5fc6445613112c15a956d0002ae780cd5bbb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instancePoolId")
    def instance_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instancePoolId"))

    @instance_pool_id.setter
    def instance_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a513a9d0ed92da2fa5f36144539f24d0da224fe52f52a7e08c140cc59d2677be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instancePoolId", value)

    @builtins.property
    @jsii.member(jsii_name="jobId")
    def job_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobId"))

    @job_id.setter
    def job_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4b0a23dbdbceb4274635ea209120a10fc8236b351bd9bb7ccbaa91e5c71dd91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobId", value)

    @builtins.property
    @jsii.member(jsii_name="notebookId")
    def notebook_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notebookId"))

    @notebook_id.setter
    def notebook_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__189ae7ea2556d0b045d2c98a80c7d1cad1082cbbff31d7f32b4ba385e709ac4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notebookId", value)

    @builtins.property
    @jsii.member(jsii_name="notebookPath")
    def notebook_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notebookPath"))

    @notebook_path.setter
    def notebook_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__962a466be93bd37c8bc719b64bcbbb7ed8dbb4cfd609323979c84cf3683ee642)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notebookPath", value)

    @builtins.property
    @jsii.member(jsii_name="objectType")
    def object_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectType"))

    @object_type.setter
    def object_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__972e8731e648dc98d7c562caf4629246da29d418367a3079e5f899d7f715c955)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectType", value)

    @builtins.property
    @jsii.member(jsii_name="pipelineId")
    def pipeline_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pipelineId"))

    @pipeline_id.setter
    def pipeline_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a129963d5ae4021ce13f2276a2d9276f95b68ad5df38938683d2abf644aa3a5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pipelineId", value)

    @builtins.property
    @jsii.member(jsii_name="registeredModelId")
    def registered_model_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registeredModelId"))

    @registered_model_id.setter
    def registered_model_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8e3e7fd4921eb6da0e9f2f37fe702d6663a37af464d8b309dd1cabf9b63d563)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registeredModelId", value)

    @builtins.property
    @jsii.member(jsii_name="repoId")
    def repo_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repoId"))

    @repo_id.setter
    def repo_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b23b3c59704f31cf770210afa6287917559fbd1bd576f444c6d0da04fc614b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repoId", value)

    @builtins.property
    @jsii.member(jsii_name="repoPath")
    def repo_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repoPath"))

    @repo_path.setter
    def repo_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__583db6e735fa49b760dc61da1688a94dfa0a7a18f4a63e23dc1873ad4a6873fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repoPath", value)

    @builtins.property
    @jsii.member(jsii_name="sqlAlertId")
    def sql_alert_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlAlertId"))

    @sql_alert_id.setter
    def sql_alert_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e71356a7ce9e862bd743e1dc8cbbcaa025546e76e1ccd2409d0d283575915b86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlAlertId", value)

    @builtins.property
    @jsii.member(jsii_name="sqlDashboardId")
    def sql_dashboard_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlDashboardId"))

    @sql_dashboard_id.setter
    def sql_dashboard_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86f67fe4751df8a979a5b4e6abfec7d51aed85074fb8dbea0985993514680bdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlDashboardId", value)

    @builtins.property
    @jsii.member(jsii_name="sqlEndpointId")
    def sql_endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlEndpointId"))

    @sql_endpoint_id.setter
    def sql_endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58658130ed60e996bfe4fda6ff05927a50ea4edc915d1b178d958b75ca9d77db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlEndpointId", value)

    @builtins.property
    @jsii.member(jsii_name="sqlQueryId")
    def sql_query_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlQueryId"))

    @sql_query_id.setter
    def sql_query_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6c7b91998c5c96a46b73dfec4a13dbcf54e79b91045c8f246e072cdaf0c044d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlQueryId", value)


@jsii.data_type(
    jsii_type="databricks.permissions.PermissionsAccessControl",
    jsii_struct_bases=[],
    name_mapping={
        "permission_level": "permissionLevel",
        "group_name": "groupName",
        "service_principal_name": "servicePrincipalName",
        "user_name": "userName",
    },
)
class PermissionsAccessControl:
    def __init__(
        self,
        *,
        permission_level: builtins.str,
        group_name: typing.Optional[builtins.str] = None,
        service_principal_name: typing.Optional[builtins.str] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param permission_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#permission_level Permissions#permission_level}.
        :param group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#group_name Permissions#group_name}.
        :param service_principal_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#service_principal_name Permissions#service_principal_name}.
        :param user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#user_name Permissions#user_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b24c582d0340d0bb4552c44bec44241d79fc66b8c74d654f4804c96ae7a2b88)
            check_type(argname="argument permission_level", value=permission_level, expected_type=type_hints["permission_level"])
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument service_principal_name", value=service_principal_name, expected_type=type_hints["service_principal_name"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "permission_level": permission_level,
        }
        if group_name is not None:
            self._values["group_name"] = group_name
        if service_principal_name is not None:
            self._values["service_principal_name"] = service_principal_name
        if user_name is not None:
            self._values["user_name"] = user_name

    @builtins.property
    def permission_level(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#permission_level Permissions#permission_level}.'''
        result = self._values.get("permission_level")
        assert result is not None, "Required property 'permission_level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#group_name Permissions#group_name}.'''
        result = self._values.get("group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_principal_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#service_principal_name Permissions#service_principal_name}.'''
        result = self._values.get("service_principal_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#user_name Permissions#user_name}.'''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PermissionsAccessControl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PermissionsAccessControlList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.permissions.PermissionsAccessControlList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6b95d1424fc93693843eb263d37a1b44a08b8e1ff67e2810e6ee52c3ca5118e2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PermissionsAccessControlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20465a414674a38dd9b29bc6225c5118ce1496220c5d8a2cdb0f441f5cda7a6f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PermissionsAccessControlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6aa5dd6e1d553409d335a6cbd83653805b9be5983a85897567865da038194571)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d69a187b8b5082173dbed65ad5d91c9f0eb082c130194d9b10e6f6587922cbf5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a0204e5475711d5afeb2346b69cc66645593f9d0255cb30bf371185ffa60778b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PermissionsAccessControl]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PermissionsAccessControl]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PermissionsAccessControl]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a84ca953cca331ce81055150020a673a5ad7982632e4ee66e50da8317af3d29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PermissionsAccessControlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="databricks.permissions.PermissionsAccessControlOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__356bb6e253b3f5e81701dd03f7901e48a46a69dd4196091521ffab5bad2f2ee8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroupName")
    def reset_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupName", []))

    @jsii.member(jsii_name="resetServicePrincipalName")
    def reset_service_principal_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServicePrincipalName", []))

    @jsii.member(jsii_name="resetUserName")
    def reset_user_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserName", []))

    @builtins.property
    @jsii.member(jsii_name="groupNameInput")
    def group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionLevelInput")
    def permission_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="servicePrincipalNameInput")
    def service_principal_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicePrincipalNameInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameInput")
    def user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userNameInput"))

    @builtins.property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupName"))

    @group_name.setter
    def group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49444097389297741e8254aa7f287544d13d539759f535e9d9272e4f29f8b7c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupName", value)

    @builtins.property
    @jsii.member(jsii_name="permissionLevel")
    def permission_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permissionLevel"))

    @permission_level.setter
    def permission_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e257528eecc77da2c03a3f9a43adc90ad53117d9d75c50faafcfebb904e75a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionLevel", value)

    @builtins.property
    @jsii.member(jsii_name="servicePrincipalName")
    def service_principal_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicePrincipalName"))

    @service_principal_name.setter
    def service_principal_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cce9bb1126d07434a345ef7896d588403741a31bc5387073cbd16e3a1410c05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicePrincipalName", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63e6b37191eb606b130407bbc9747b5e3939ba586d9713509fc652f21ef8e1ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PermissionsAccessControl, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PermissionsAccessControl, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PermissionsAccessControl, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__282a7c3dc271699b5e700af1febc856d93176077559e249dbe87cfe18b4dc7bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="databricks.permissions.PermissionsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "access_control": "accessControl",
        "authorization": "authorization",
        "cluster_id": "clusterId",
        "cluster_policy_id": "clusterPolicyId",
        "directory_id": "directoryId",
        "directory_path": "directoryPath",
        "experiment_id": "experimentId",
        "id": "id",
        "instance_pool_id": "instancePoolId",
        "job_id": "jobId",
        "notebook_id": "notebookId",
        "notebook_path": "notebookPath",
        "object_type": "objectType",
        "pipeline_id": "pipelineId",
        "registered_model_id": "registeredModelId",
        "repo_id": "repoId",
        "repo_path": "repoPath",
        "sql_alert_id": "sqlAlertId",
        "sql_dashboard_id": "sqlDashboardId",
        "sql_endpoint_id": "sqlEndpointId",
        "sql_query_id": "sqlQueryId",
    },
)
class PermissionsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        access_control: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PermissionsAccessControl, typing.Dict[builtins.str, typing.Any]]]],
        authorization: typing.Optional[builtins.str] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        cluster_policy_id: typing.Optional[builtins.str] = None,
        directory_id: typing.Optional[builtins.str] = None,
        directory_path: typing.Optional[builtins.str] = None,
        experiment_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        instance_pool_id: typing.Optional[builtins.str] = None,
        job_id: typing.Optional[builtins.str] = None,
        notebook_id: typing.Optional[builtins.str] = None,
        notebook_path: typing.Optional[builtins.str] = None,
        object_type: typing.Optional[builtins.str] = None,
        pipeline_id: typing.Optional[builtins.str] = None,
        registered_model_id: typing.Optional[builtins.str] = None,
        repo_id: typing.Optional[builtins.str] = None,
        repo_path: typing.Optional[builtins.str] = None,
        sql_alert_id: typing.Optional[builtins.str] = None,
        sql_dashboard_id: typing.Optional[builtins.str] = None,
        sql_endpoint_id: typing.Optional[builtins.str] = None,
        sql_query_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param access_control: access_control block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#access_control Permissions#access_control}
        :param authorization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#authorization Permissions#authorization}.
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#cluster_id Permissions#cluster_id}.
        :param cluster_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#cluster_policy_id Permissions#cluster_policy_id}.
        :param directory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#directory_id Permissions#directory_id}.
        :param directory_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#directory_path Permissions#directory_path}.
        :param experiment_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#experiment_id Permissions#experiment_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#id Permissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#instance_pool_id Permissions#instance_pool_id}.
        :param job_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#job_id Permissions#job_id}.
        :param notebook_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#notebook_id Permissions#notebook_id}.
        :param notebook_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#notebook_path Permissions#notebook_path}.
        :param object_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#object_type Permissions#object_type}.
        :param pipeline_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#pipeline_id Permissions#pipeline_id}.
        :param registered_model_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#registered_model_id Permissions#registered_model_id}.
        :param repo_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#repo_id Permissions#repo_id}.
        :param repo_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#repo_path Permissions#repo_path}.
        :param sql_alert_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#sql_alert_id Permissions#sql_alert_id}.
        :param sql_dashboard_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#sql_dashboard_id Permissions#sql_dashboard_id}.
        :param sql_endpoint_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#sql_endpoint_id Permissions#sql_endpoint_id}.
        :param sql_query_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#sql_query_id Permissions#sql_query_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbd08d63c541176ce3111e48665ce69d8eee1423d633a1c863c5a4a64a05dc1a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument access_control", value=access_control, expected_type=type_hints["access_control"])
            check_type(argname="argument authorization", value=authorization, expected_type=type_hints["authorization"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument cluster_policy_id", value=cluster_policy_id, expected_type=type_hints["cluster_policy_id"])
            check_type(argname="argument directory_id", value=directory_id, expected_type=type_hints["directory_id"])
            check_type(argname="argument directory_path", value=directory_path, expected_type=type_hints["directory_path"])
            check_type(argname="argument experiment_id", value=experiment_id, expected_type=type_hints["experiment_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_pool_id", value=instance_pool_id, expected_type=type_hints["instance_pool_id"])
            check_type(argname="argument job_id", value=job_id, expected_type=type_hints["job_id"])
            check_type(argname="argument notebook_id", value=notebook_id, expected_type=type_hints["notebook_id"])
            check_type(argname="argument notebook_path", value=notebook_path, expected_type=type_hints["notebook_path"])
            check_type(argname="argument object_type", value=object_type, expected_type=type_hints["object_type"])
            check_type(argname="argument pipeline_id", value=pipeline_id, expected_type=type_hints["pipeline_id"])
            check_type(argname="argument registered_model_id", value=registered_model_id, expected_type=type_hints["registered_model_id"])
            check_type(argname="argument repo_id", value=repo_id, expected_type=type_hints["repo_id"])
            check_type(argname="argument repo_path", value=repo_path, expected_type=type_hints["repo_path"])
            check_type(argname="argument sql_alert_id", value=sql_alert_id, expected_type=type_hints["sql_alert_id"])
            check_type(argname="argument sql_dashboard_id", value=sql_dashboard_id, expected_type=type_hints["sql_dashboard_id"])
            check_type(argname="argument sql_endpoint_id", value=sql_endpoint_id, expected_type=type_hints["sql_endpoint_id"])
            check_type(argname="argument sql_query_id", value=sql_query_id, expected_type=type_hints["sql_query_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_control": access_control,
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
        if authorization is not None:
            self._values["authorization"] = authorization
        if cluster_id is not None:
            self._values["cluster_id"] = cluster_id
        if cluster_policy_id is not None:
            self._values["cluster_policy_id"] = cluster_policy_id
        if directory_id is not None:
            self._values["directory_id"] = directory_id
        if directory_path is not None:
            self._values["directory_path"] = directory_path
        if experiment_id is not None:
            self._values["experiment_id"] = experiment_id
        if id is not None:
            self._values["id"] = id
        if instance_pool_id is not None:
            self._values["instance_pool_id"] = instance_pool_id
        if job_id is not None:
            self._values["job_id"] = job_id
        if notebook_id is not None:
            self._values["notebook_id"] = notebook_id
        if notebook_path is not None:
            self._values["notebook_path"] = notebook_path
        if object_type is not None:
            self._values["object_type"] = object_type
        if pipeline_id is not None:
            self._values["pipeline_id"] = pipeline_id
        if registered_model_id is not None:
            self._values["registered_model_id"] = registered_model_id
        if repo_id is not None:
            self._values["repo_id"] = repo_id
        if repo_path is not None:
            self._values["repo_path"] = repo_path
        if sql_alert_id is not None:
            self._values["sql_alert_id"] = sql_alert_id
        if sql_dashboard_id is not None:
            self._values["sql_dashboard_id"] = sql_dashboard_id
        if sql_endpoint_id is not None:
            self._values["sql_endpoint_id"] = sql_endpoint_id
        if sql_query_id is not None:
            self._values["sql_query_id"] = sql_query_id

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
    def access_control(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PermissionsAccessControl]]:
        '''access_control block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#access_control Permissions#access_control}
        '''
        result = self._values.get("access_control")
        assert result is not None, "Required property 'access_control' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PermissionsAccessControl]], result)

    @builtins.property
    def authorization(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#authorization Permissions#authorization}.'''
        result = self._values.get("authorization")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#cluster_id Permissions#cluster_id}.'''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_policy_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#cluster_policy_id Permissions#cluster_policy_id}.'''
        result = self._values.get("cluster_policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#directory_id Permissions#directory_id}.'''
        result = self._values.get("directory_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#directory_path Permissions#directory_path}.'''
        result = self._values.get("directory_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def experiment_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#experiment_id Permissions#experiment_id}.'''
        result = self._values.get("experiment_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#id Permissions#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#instance_pool_id Permissions#instance_pool_id}.'''
        result = self._values.get("instance_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#job_id Permissions#job_id}.'''
        result = self._values.get("job_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notebook_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#notebook_id Permissions#notebook_id}.'''
        result = self._values.get("notebook_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notebook_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#notebook_path Permissions#notebook_path}.'''
        result = self._values.get("notebook_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#object_type Permissions#object_type}.'''
        result = self._values.get("object_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pipeline_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#pipeline_id Permissions#pipeline_id}.'''
        result = self._values.get("pipeline_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def registered_model_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#registered_model_id Permissions#registered_model_id}.'''
        result = self._values.get("registered_model_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repo_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#repo_id Permissions#repo_id}.'''
        result = self._values.get("repo_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repo_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#repo_path Permissions#repo_path}.'''
        result = self._values.get("repo_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sql_alert_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#sql_alert_id Permissions#sql_alert_id}.'''
        result = self._values.get("sql_alert_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sql_dashboard_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#sql_dashboard_id Permissions#sql_dashboard_id}.'''
        result = self._values.get("sql_dashboard_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sql_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#sql_endpoint_id Permissions#sql_endpoint_id}.'''
        result = self._values.get("sql_endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sql_query_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/permissions#sql_query_id Permissions#sql_query_id}.'''
        result = self._values.get("sql_query_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PermissionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Permissions",
    "PermissionsAccessControl",
    "PermissionsAccessControlList",
    "PermissionsAccessControlOutputReference",
    "PermissionsConfig",
]

publication.publish()

def _typecheckingstub__213f4267377282fa03303ffaac106931ae364eb78331bf18eb0e55bf22d47923(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    access_control: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PermissionsAccessControl, typing.Dict[builtins.str, typing.Any]]]],
    authorization: typing.Optional[builtins.str] = None,
    cluster_id: typing.Optional[builtins.str] = None,
    cluster_policy_id: typing.Optional[builtins.str] = None,
    directory_id: typing.Optional[builtins.str] = None,
    directory_path: typing.Optional[builtins.str] = None,
    experiment_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    instance_pool_id: typing.Optional[builtins.str] = None,
    job_id: typing.Optional[builtins.str] = None,
    notebook_id: typing.Optional[builtins.str] = None,
    notebook_path: typing.Optional[builtins.str] = None,
    object_type: typing.Optional[builtins.str] = None,
    pipeline_id: typing.Optional[builtins.str] = None,
    registered_model_id: typing.Optional[builtins.str] = None,
    repo_id: typing.Optional[builtins.str] = None,
    repo_path: typing.Optional[builtins.str] = None,
    sql_alert_id: typing.Optional[builtins.str] = None,
    sql_dashboard_id: typing.Optional[builtins.str] = None,
    sql_endpoint_id: typing.Optional[builtins.str] = None,
    sql_query_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__6a22d3ca55914593e30c2dfa2dc73e7431b78743621030ffa7410454838c55de(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PermissionsAccessControl, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__915783a9f2f364750b7d1bf6b969ed4a9c9e01a140bf478a0a485d575619448f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__472a7034eb650e04db013bb575e338377a57a2a8cc937acdcb40bed011a76d4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c07acbb5d41cc4158a79b000c850ff743e42f9decff00eb99a7b69d96e9853ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__203bddbc9e3acd97bf7afe194eb2e0c9cc0ae87f1138eea4ac4941595ff97f11(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa75b995b8e650cea3b63bfb686c1ae8c21256c4bd71144ee93d3e6f408aac4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc31e406e2fa89a2f4202373a36e60b4a1566d700bf3053c2eafc7351d301b98(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efd8ff75f5b79f501b1cffe72ad5fc6445613112c15a956d0002ae780cd5bbb9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a513a9d0ed92da2fa5f36144539f24d0da224fe52f52a7e08c140cc59d2677be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4b0a23dbdbceb4274635ea209120a10fc8236b351bd9bb7ccbaa91e5c71dd91(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__189ae7ea2556d0b045d2c98a80c7d1cad1082cbbff31d7f32b4ba385e709ac4c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__962a466be93bd37c8bc719b64bcbbb7ed8dbb4cfd609323979c84cf3683ee642(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__972e8731e648dc98d7c562caf4629246da29d418367a3079e5f899d7f715c955(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a129963d5ae4021ce13f2276a2d9276f95b68ad5df38938683d2abf644aa3a5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8e3e7fd4921eb6da0e9f2f37fe702d6663a37af464d8b309dd1cabf9b63d563(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b23b3c59704f31cf770210afa6287917559fbd1bd576f444c6d0da04fc614b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__583db6e735fa49b760dc61da1688a94dfa0a7a18f4a63e23dc1873ad4a6873fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e71356a7ce9e862bd743e1dc8cbbcaa025546e76e1ccd2409d0d283575915b86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86f67fe4751df8a979a5b4e6abfec7d51aed85074fb8dbea0985993514680bdf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58658130ed60e996bfe4fda6ff05927a50ea4edc915d1b178d958b75ca9d77db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6c7b91998c5c96a46b73dfec4a13dbcf54e79b91045c8f246e072cdaf0c044d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b24c582d0340d0bb4552c44bec44241d79fc66b8c74d654f4804c96ae7a2b88(
    *,
    permission_level: builtins.str,
    group_name: typing.Optional[builtins.str] = None,
    service_principal_name: typing.Optional[builtins.str] = None,
    user_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b95d1424fc93693843eb263d37a1b44a08b8e1ff67e2810e6ee52c3ca5118e2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20465a414674a38dd9b29bc6225c5118ce1496220c5d8a2cdb0f441f5cda7a6f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aa5dd6e1d553409d335a6cbd83653805b9be5983a85897567865da038194571(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d69a187b8b5082173dbed65ad5d91c9f0eb082c130194d9b10e6f6587922cbf5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0204e5475711d5afeb2346b69cc66645593f9d0255cb30bf371185ffa60778b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a84ca953cca331ce81055150020a673a5ad7982632e4ee66e50da8317af3d29(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PermissionsAccessControl]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__356bb6e253b3f5e81701dd03f7901e48a46a69dd4196091521ffab5bad2f2ee8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49444097389297741e8254aa7f287544d13d539759f535e9d9272e4f29f8b7c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e257528eecc77da2c03a3f9a43adc90ad53117d9d75c50faafcfebb904e75a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cce9bb1126d07434a345ef7896d588403741a31bc5387073cbd16e3a1410c05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63e6b37191eb606b130407bbc9747b5e3939ba586d9713509fc652f21ef8e1ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__282a7c3dc271699b5e700af1febc856d93176077559e249dbe87cfe18b4dc7bf(
    value: typing.Optional[typing.Union[PermissionsAccessControl, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbd08d63c541176ce3111e48665ce69d8eee1423d633a1c863c5a4a64a05dc1a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    access_control: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PermissionsAccessControl, typing.Dict[builtins.str, typing.Any]]]],
    authorization: typing.Optional[builtins.str] = None,
    cluster_id: typing.Optional[builtins.str] = None,
    cluster_policy_id: typing.Optional[builtins.str] = None,
    directory_id: typing.Optional[builtins.str] = None,
    directory_path: typing.Optional[builtins.str] = None,
    experiment_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    instance_pool_id: typing.Optional[builtins.str] = None,
    job_id: typing.Optional[builtins.str] = None,
    notebook_id: typing.Optional[builtins.str] = None,
    notebook_path: typing.Optional[builtins.str] = None,
    object_type: typing.Optional[builtins.str] = None,
    pipeline_id: typing.Optional[builtins.str] = None,
    registered_model_id: typing.Optional[builtins.str] = None,
    repo_id: typing.Optional[builtins.str] = None,
    repo_path: typing.Optional[builtins.str] = None,
    sql_alert_id: typing.Optional[builtins.str] = None,
    sql_dashboard_id: typing.Optional[builtins.str] = None,
    sql_endpoint_id: typing.Optional[builtins.str] = None,
    sql_query_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
