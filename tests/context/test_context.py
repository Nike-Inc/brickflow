import base64
import functools
import os
import pickle
import sys
from unittest import mock
from unittest.mock import Mock, patch

import pytest

from brickflow.context import (
    BrickflowTaskComsObject,
    BrickflowTaskComs,
    ctx,
    Context,
    RETURN_VALUE_KEY,
    BRANCH_SKIP_EXCEPT,
    SKIP_EXCEPT_HACK,
    BrickflowBuiltInTaskVariables,
)
from brickflow.context.context import ContextMode
from brickflow import BrickflowEnvVars


def reset_ctx(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        resp = f(*args, **kwargs)
        ctx._configure()
        return resp

    return wrapper


def fake_task():
    pass


class TestContext:
    def test_brickflow_task_comms_obj(self):
        task_value = "hello-world"
        hidden_comms_obj = BrickflowTaskComsObject._TaskComsObject(task_value)
        b64_data = base64.b64encode(pickle.dumps(hidden_comms_obj)).decode("utf-8")
        comms_obj = BrickflowTaskComsObject(task_value)
        assert comms_obj.to_encoded_value == b64_data
        assert comms_obj.value == task_value
        assert BrickflowTaskComsObject.from_encoded_value(b64_data).value == task_value
        assert (
            BrickflowTaskComsObject.from_encoded_value(task_value).value == task_value
        )

    def test_brickflow_task_comms(self):
        task_comms = BrickflowTaskComs()
        task_id = "test-task"
        key = "test-key"
        value1 = "value 1"
        value2 = "value 2"
        task_comms.put(task_id, key, value1)
        assert task_comms.get(task_id, key) == value1
        task_comms.put(task_id, key, value2)
        assert task_comms.get(task_id, key) == value2
        assert task_comms.get(task_id)[key] == value2

    def test_brickflow_task_comms_dbutils(self):
        dbutils_mock = Mock()
        task_comms = BrickflowTaskComs(dbutils_mock)
        task_id = "test-task"
        key = "test-key"
        value1 = "value 1"
        value2 = "value 2"
        task_comms_v1 = BrickflowTaskComsObject(value1)
        task_comms_v2 = BrickflowTaskComsObject(value2)
        dbutils_mock.jobs.taskValues.get.return_value = task_comms_v1.to_encoded_value
        task_comms.put(task_id, key, value1)
        dbutils_mock.jobs.taskValues.set.assert_called_once_with(
            f"{key}", task_comms_v1.to_encoded_value
        )
        assert task_comms.get(task_id, key) == value1
        task_comms.put(task_id, key, value2)
        dbutils_mock.jobs.taskValues.set.assert_called_with(
            f"{key}", task_comms_v2.to_encoded_value
        )
        dbutils_mock.jobs.taskValues.get.return_value = task_comms_v2.to_encoded_value
        assert task_comms.get(task_id, key) == value2
        assert task_comms.get(task_id)[key] == value2

    # @reset_ctx
    @patch("brickflow.context.ctx._dbutils")
    def test_context_obj(self, dbutils: Mock):
        task_key = "hello-world"
        # assert that its a singleton
        assert id(ctx) == id(Context())
        ctx._dbutils = dbutils
        assert ctx.current_task is None
        ctx._set_current_task(task_key)
        assert ctx.current_task == task_key
        ctx._reset_current_task()
        assert ctx.current_task is None

        for e in BrickflowBuiltInTaskVariables:
            dbutils.widgets.get.return_value = "actual"
            assert getattr(ctx, e.name)(debug="test") == "actual"
            dbutils.widgets.get.assert_called_with(e.value)

        ctx._dbutils = None
        assert ctx.task_key(debug=task_key) == task_key

    @patch("brickflow.context.ctx._task_coms")
    def test_context_obj_task_coms(self, task_coms: Mock):
        current_task = "curr_task"
        task_key = "some_task"
        some_return_value = "some_value"
        task_coms.get.return_value = some_return_value
        assert ctx.get_return_value(task_key) == some_return_value
        task_coms.get.assert_called_once_with(task_key, RETURN_VALUE_KEY)
        # set the current task
        ctx._set_current_task(current_task)
        ctx.skip_all_except(task_key)
        task_coms.put.assert_called_with(current_task, BRANCH_SKIP_EXCEPT, task_key)
        ctx.skip_all_except(fake_task)
        task_coms.put.assert_called_with(
            current_task, BRANCH_SKIP_EXCEPT, fake_task.__name__
        )
        ctx.skip_all_following()
        task_coms.put.assert_called_with(
            current_task, BRANCH_SKIP_EXCEPT, SKIP_EXCEPT_HACK
        )
        ctx._reset_current_task()

    def test_context_skip_runtime_error(self):
        with pytest.raises(RuntimeError):
            ctx.skip_all_except("sometask")

        with pytest.raises(RuntimeError):
            ctx.skip_all_following()

    def test_dbutils_widget_get_or_else(self):
        key = "random-key"
        value = "default"
        assert ctx.dbutils_widget_get_or_else(key, value) == value

    def test_configure_dbutils(self):
        dbutils_class_mock = Mock()
        pyspark = Mock()
        pyspark_dbutils = Mock()
        ipython_mock = Mock()
        ipython_get_mock = Mock()
        ipython_mock.get_ipython = ipython_get_mock
        ipython_get_mock.user_ns.get.return_value = Mock()
        sys.modules["pyspark"] = pyspark
        sys.modules["IPython"] = ipython_mock
        sys.modules["pyspark.dbutils"] = pyspark_dbutils
        sys.modules["pyspark.dbutils.DBUtils"] = dbutils_class_mock
        assert ctx._configure_dbutils() == ContextMode.databricks
        sys.modules.pop("pyspark")
        sys.modules.pop("IPython")
        sys.modules.pop("pyspark.dbutils")
        sys.modules.pop("pyspark.dbutils.DBUtils")

    def test_configure_spark(self):
        spark_mock = Mock()
        pyspark = Mock()
        pyspark_sql = Mock()
        sys.modules["pyspark"] = pyspark
        sys.modules["pyspark.sql"] = pyspark_sql
        sys.modules["pyspark.sql.SparkSession"] = spark_mock
        assert ctx._set_spark_session() is None
        sys.modules.pop("pyspark")
        sys.modules.pop("pyspark.sql")
        sys.modules.pop("pyspark.sql.SparkSession")

    @mock.patch.dict(
        os.environ,
        {
            BrickflowEnvVars.BRICKFLOW_ENV.value: "dev",
        },
    )
    def test_get_by_env_happy_path(self):
        assert "dev" == ctx.get_by_env("testing...", dev="dev")

    @mock.patch.dict(
        os.environ,
        {
            BrickflowEnvVars.BRICKFLOW_ENV.value: "dev",
        },
    )
    def test_get_by_env_default(self):
        assert "default" == ctx.get_by_env("testing...", default="default")

    @mock.patch.dict(
        os.environ,
        {
            BrickflowEnvVars.BRICKFLOW_ENV.value: "dev",
        },
    )
    def test_get_by_env_no_default_value_error(self):
        with pytest.raises(KeyError):
            ctx.get_by_env("testing...")

    @patch("brickflow.context.ctx._dbutils")
    def test_get_project_parameter(self, dbutils: Mock):
        parameter_name = BrickflowEnvVars.BRICKFLOW_PROJECT_PARAMS.value.lower()
        expected_value = "k1=v1,k2=v2"
        dbutils.widgets.get.return_value = expected_value

        result = ctx.get_parameter(parameter_name)

        dbutils.widgets.get.assert_called_with(parameter_name)
        assert result == expected_value

        result = ctx.get_project_parameter("k1")
        assert result == "v1"

        result = ctx.get_project_parameter("k2")
        assert result == "v2"

        result = ctx.get_project_parameter("k3")
        assert result is None

        result = ctx.get_project_parameter("k3", "v3")
        assert result == "v3"
