import datetime
from collections import namedtuple
from unittest.mock import Mock, patch

import pytest
from deepdiff import DeepDiff

from brickflow import BrickflowProjectDeploymentSettings
from brickflow.context import (
    ctx,
    BRANCH_SKIP_EXCEPT,
    SKIP_EXCEPT_HACK,
    RETURN_VALUE_KEY,
    BrickflowInternalVariables,
)
from brickflow.engine.task import (
    InvalidTaskSignatureDefinition,
    EmailNotifications,
    TaskSettings,
    JarTaskLibrary,
    EggTaskLibrary,
    WheelTaskLibrary,
    PypiTaskLibrary,
    MavenTaskLibrary,
    CranTaskLibrary,
    InvalidTaskLibraryError,
    TaskLibrary,
    get_brickflow_lib_version,
    get_brickflow_libraries,
)
from tests.engine.sample_workflow import (
    wf,
    task_function,
    task_function_nokwargs,
    task_function_2,
    task_function_3,
    task_function_4,
    custom_python_task_push,
)


class TestTask:
    builtin_task_params = {
        "brickflow_job_id": "{{job_id}}",
        "brickflow_run_id": "{{run_id}}",
        "brickflow_start_date": "{{start_date}}",
        "brickflow_start_time": "{{start_time}}",
        "brickflow_task_retry_count": "{{task_retry_count}}",
        "brickflow_parent_run_id": "{{parent_run_id}}",
        "brickflow_task_key": "{{task_key}}",
    }

    def test_builtin_notebook_params(self):
        assert (
            wf.get_task(task_function.__name__).builtin_notebook_params
            == self.builtin_task_params
        )

    def test_builtin_default_params(self):
        assert wf.get_task(task_function.__name__).brickflow_default_params == {
            "brickflow_internal_workflow_name": wf.name,
            "brickflow_internal_task_name": "{{task_key}}",
            "brickflow_internal_only_run_tasks": "",
            "brickflow_internal_workflow_prefix": "",
            "brickflow_internal_workflow_suffix": "",
            "brickflow_env": ctx.env,
        }

        wf.prefix = "my_prefix"
        wf.suffix = "my_suffix"
        assert wf.get_task(task_function.__name__).brickflow_default_params == {
            "brickflow_internal_workflow_name": wf.name,
            "brickflow_internal_task_name": "{{task_key}}",
            "brickflow_internal_only_run_tasks": "",
            "brickflow_internal_workflow_prefix": "my_prefix",
            "brickflow_internal_workflow_suffix": "my_suffix",
            "brickflow_env": ctx.env,
        }

    def test_custom_task_params(self):
        assert wf.get_task(task_function.__name__).custom_task_parameters == {
            "all_tasks1": "test",
            "all_tasks3": "123",
            "test": "var",
        }
        assert wf.get_task(task_function_nokwargs.__name__).custom_task_parameters == {
            "all_tasks1": "test",
            "all_tasks3": "123",
        }

        wf.common_task_parameters = {
            "all_tasks1": "test",
            "all_tasks3": "123",
            "test": "to_be_overridden",  # This should be overridden by the task argument passed with same key
        }
        assert wf.get_task(task_function.__name__).custom_task_parameters == {
            "all_tasks1": "test",
            "all_tasks3": "123",
            "test": "var",
        }
        wf.common_task_parameters = {}
        assert wf.get_task(task_function_nokwargs.__name__).custom_task_parameters == {}

    def test_task_settings(self):
        assert wf.get_task(task_function.__name__).task_settings is None

    def test_parents(self):
        assert wf.get_task(task_function_2.__name__).parents == ["task_function"]

    def test_task_type(self):
        assert (
            wf.get_task(task_function_2.__name__).databricks_task_type_str
            == "notebook_task"
        )

    def test_depends_on(self):
        assert wf.get_task(task_function_3.__name__).depends_on == ["task_function_2"]
        assert wf.get_task(task_function_2.__name__).depends_on == [task_function]
        assert wf.get_task(task_function.__name__).depends_on == []

    def test_invalid_task_signature(self):
        with pytest.raises(InvalidTaskSignatureDefinition):
            # missing * and kwargs
            @wf.task
            def _fake_task1(test):  # noqa
                # pylint: disable=unused-argument
                pass

        with pytest.raises(InvalidTaskSignatureDefinition):
            # missing *
            @wf.task
            def _fake_task2(test="test"):  # noqa
                # pylint: disable=unused-argument
                pass

    @pytest.mark.parametrize(
        "test_input",
        [123413, 13231.32, b"test", False, {"test": "test"}, ["hello"], (2, 3)],
    )
    def test_invalid_task_signature_objects(self, test_input):
        with pytest.raises(InvalidTaskSignatureDefinition):
            # doesnt support bytes-like
            @wf.task(name=f"fake_task_{str(test_input)}")
            def _fake_task(*, test=test_input):  # noqa
                # pylint: disable=unused-argument
                pass

    @patch("brickflow.context.ctx._task_coms")
    def test_should_skip_false(self, task_coms_mock: Mock):
        task_coms_mock.get.return_value = task_function_3.__name__
        skip, reason = wf.get_task(task_function_3.__name__).should_skip()
        assert skip is False
        assert reason is None
        task_coms_mock.get.assert_called_once()
        ctx._configure()

        task_coms_mock.get.value = task_function.__name__
        task_coms_mock.get.side_effect = Exception("error")
        skip, reason = wf.get_task(task_function_3.__name__).should_skip()
        assert skip is False
        assert reason is None
        ctx._configure()

        skip, reason = wf.get_task(task_function.__name__).should_skip()
        assert skip is False
        assert reason is None
        ctx._configure()

        skip, reason = wf.get_task(task_function_4.__name__).should_skip()
        assert skip is False
        assert reason is None
        ctx._configure()

    @patch("brickflow.context.ctx.get_parameter")
    def test_skip_not_selected_task(self, dbutils):
        dbutils.value = "sometihngelse"
        skip, reason = wf.get_task(
            task_function_4.__name__
        )._skip_because_not_selected()
        dbutils.assert_called_once_with(
            BrickflowInternalVariables.only_run_tasks.value, ""
        )
        assert skip is True
        assert reason.startswith(
            f"This task: {task_function_4.__name__} is not a selected task"
        )
        assert wf.get_task(task_function_4.__name__).execute() is None

    @patch("brickflow.context.ctx.get_parameter")
    def test_no_skip_selected_task(self, dbutils: Mock):
        dbutils.return_value = task_function_4.__name__
        skip, reason = wf.get_task(
            task_function_4.__name__
        )._skip_because_not_selected()
        dbutils.assert_called_once_with(
            BrickflowInternalVariables.only_run_tasks.value, ""
        )
        assert skip is False
        assert reason is None
        assert wf.get_task(task_function_4.__name__).execute() == task_function_4()

    @patch("brickflow.engine.task.Task._skip_because_not_selected")
    @patch("brickflow.context.ctx._task_coms")
    def test_should_skip_true(
        self, task_coms_mock: Mock, task_skip_selected_mock: Mock
    ):
        task_skip_selected_mock.return_value = (False, None)
        task_coms_mock.get.value = task_function_2.__name__
        skip, reason = wf.get_task(task_function_3.__name__).should_skip()
        assert skip is True
        assert reason == "All tasks before this were not successful"
        task_coms_mock.get.assert_called_once()
        assert wf.get_task(task_function_3.__name__).execute() is None
        task_coms_mock.put.assert_called_once_with(
            task_function_3.__name__, BRANCH_SKIP_EXCEPT, SKIP_EXCEPT_HACK
        )

    @patch("brickflow.context.ctx.get_parameter")
    @patch("brickflow.context.ctx._task_coms")
    def test_execute(self, task_coms_mock: Mock, dbutils: Mock):
        dbutils.return_value = ""
        resp = wf.get_task(task_function.__name__).execute()
        task_coms_mock.put.assert_called_once_with(
            task_function.__name__, RETURN_VALUE_KEY, task_function()
        )

        assert resp is task_function()

    @patch("brickflow.context.ctx.get_parameter")
    @patch("brickflow.context.ctx._task_coms")
    def test_execute_custom(self, task_coms_mock: Mock, dbutils: Mock):
        dbutils.return_value = ""
        resp = wf.get_task(custom_python_task_push.__name__).execute()
        task_coms_mock.put.assert_called_once_with(
            custom_python_task_push.__name__,
            RETURN_VALUE_KEY,
            custom_python_task_push.__name__,
        )

        assert resp is custom_python_task_push.__name__

    def test_email_notifications(self):
        email_arr = ["abc@abc.com"]
        en = EmailNotifications(
            on_start=email_arr,
            on_failure=email_arr,
            on_success=email_arr,
        )
        assert en.to_tf_dict() == {
            "on_start": email_arr,
            "on_failure": email_arr,
            "on_success": email_arr,
        }

    def test_task_settings_tf_dict(self):
        email_arr = ["abc@abc.com"]
        default_int = 10
        default_bool = True
        en = EmailNotifications(
            on_start=email_arr,
            on_failure=email_arr,
            on_success=email_arr,
        )
        ts = TaskSettings(
            email_notifications=en,
            timeout_seconds=default_int,
            max_retries=default_int,
            min_retry_interval_millis=default_int,
            retry_on_timeout=default_bool,
        )
        assert ts.to_tf_dict() == {
            "email_notifications": en.to_tf_dict(),
            "timeout_seconds": default_int,
            "max_retries": default_int,
            "min_retry_interval_millis": default_int,
            "retry_on_timeout": default_bool,
        }

    def test_task_settings_merge(self):
        email_arr = ["abc@abc.com"]
        other_email_arr = ["new@new.com"]
        default_int = 10
        other_default_int = 20
        default_bool = True
        en = EmailNotifications(
            on_start=email_arr,
            on_failure=email_arr,
            on_success=email_arr,
        )
        other_en = EmailNotifications(
            on_start=other_email_arr,
            on_failure=other_email_arr,
        )
        ts = TaskSettings(
            email_notifications=en,
            timeout_seconds=default_int,
            max_retries=default_int,
            min_retry_interval_millis=default_int,
            retry_on_timeout=default_bool,
        )
        other_ts = TaskSettings(
            email_notifications=other_en,
            timeout_seconds=other_default_int,
            max_retries=other_default_int,
            retry_on_timeout=default_bool,
        )

        final_ts = ts.merge(other_ts)
        assert final_ts.to_tf_dict() == {
            "email_notifications": other_en.to_tf_dict(),
            "timeout_seconds": other_default_int,
            "max_retries": other_default_int,
            "min_retry_interval_millis": default_int,
            "retry_on_timeout": default_bool,
        }

        final_ts = ts.merge(None)
        assert final_ts.to_tf_dict() == {
            "email_notifications": en.to_tf_dict(),
            "timeout_seconds": default_int,
            "max_retries": default_int,
            "min_retry_interval_millis": default_int,
            "retry_on_timeout": default_bool,
        }

    def test_task_settings_small_timeout(self):
        small_to = TaskSettings(
            timeout_seconds=30,
        )
        print(small_to.timeout_seconds)
        assert not wf.log_timeout_warning(small_to)

    def test_task_settings_big_timeout_warning(self):
        big_to = TaskSettings(
            timeout_seconds=datetime.timedelta(hours=0.5).seconds,
        )
        print(big_to.timeout_seconds)
        assert wf.log_timeout_warning(big_to)

    def test_task_settings_no_timeout_warning(self):
        no_to = TaskSettings()
        print(no_to.timeout_seconds)
        assert not wf.log_timeout_warning(no_to)

    def test_task_libraries(self):
        s3_path = "s3://somepath-in-s3"
        repo = "somerepo"
        package = "somepackage"
        coordinates = package
        exclusions = None
        assert JarTaskLibrary(s3_path).dict == {"jar": s3_path}
        assert EggTaskLibrary(s3_path).dict == {"egg": s3_path}
        assert WheelTaskLibrary(s3_path).dict == {"whl": s3_path}
        assert PypiTaskLibrary(package, repo).dict == {
            "pypi": {"package": package, "repo": repo}
        }
        assert MavenTaskLibrary(coordinates, repo, exclusions).dict == {
            "maven": {
                "coordinates": coordinates,
                "repo": repo,
                "exclusions": exclusions,
            }
        }
        assert CranTaskLibrary(package, repo).dict == {
            "cran": {"package": package, "repo": repo}
        }

    def test_invalid_storage_library_path(self):
        with pytest.raises(InvalidTaskLibraryError):
            JarTaskLibrary("somebadpath")

    def test_task_library_unique_list(self):
        s3_path = "s3://somepath-in-s3"
        assert TaskLibrary.unique_libraries(
            [
                JarTaskLibrary(s3_path),
                JarTaskLibrary(s3_path),
            ]
        ) == [JarTaskLibrary(s3_path)]

        assert not TaskLibrary.unique_libraries(None)

    def test_get_brickflow_lib_version(self):
        settings = BrickflowProjectDeploymentSettings()
        InputOutput = namedtuple(
            "MyNamedTuple", ["bf_version", "cli_version", "expected_version"]
        )

        input_outputs = [
            InputOutput("1.0.0", "1.0.0", "1.0.0"),
            InputOutput("1.0.0rc12312", "1.0.0", "v1.0.0rc12312"),
            InputOutput("main", "1.0.0", "main"),
            InputOutput("auto", "0.1.0rcabc12e312", "main"),
            InputOutput("auto", "0.1.0", "0.1.0"),
            InputOutput("auto", "something", "main"),
            InputOutput("v1.0.0", "something", "1.0.0"),
        ]
        for input_output in input_outputs:
            settings.brickflow_project_runtime_version = input_output.bf_version
            assert (
                get_brickflow_lib_version(
                    input_output.bf_version, input_output.cli_version
                )
                == input_output.expected_version
            )
            settings.brickflow_project_runtime_version = None

    # TODO: parameterize these tests
    def test_get_brickflow_libraries(self):
        settings = BrickflowProjectDeploymentSettings()
        settings.brickflow_project_runtime_version = "1.0.0"
        assert len(get_brickflow_libraries(enable_plugins=True)) == 3
        assert len(get_brickflow_libraries(enable_plugins=False)) == 1
        lib = get_brickflow_libraries(enable_plugins=False)[0].dict
        expected = {
            "pypi": {
                "package": "brickflows==1.0.0",
                "repo": None,
            }
        }
        diff = DeepDiff(expected, lib)
        assert not diff, diff

    def test_get_brickflow_libraries_semver_non_numeric(self):
        settings = BrickflowProjectDeploymentSettings()
        tag = "1.0.1rc1234"
        settings.brickflow_project_runtime_version = tag
        assert len(get_brickflow_libraries(enable_plugins=True)) == 3
        assert len(get_brickflow_libraries(enable_plugins=False)) == 1
        lib = get_brickflow_libraries(enable_plugins=False)[0].dict
        expected = {
            "pypi": {
                "package": f"brickflows @ git+https://github.com/Nike-Inc/brickflow.git@v{tag}",
                "repo": None,
            }
        }
        diff = DeepDiff(expected, lib)
        assert not diff, diff

    def test_get_brickflow_libraries_non_semver(self):
        settings = BrickflowProjectDeploymentSettings()
        tag = "somebranch"
        settings.brickflow_project_runtime_version = tag
        assert len(get_brickflow_libraries(enable_plugins=True)) == 3
        assert len(get_brickflow_libraries(enable_plugins=False)) == 1
        lib = get_brickflow_libraries(enable_plugins=False)[0].dict
        expected = {
            "pypi": {
                "package": f"brickflows @ git+https://github.com/Nike-Inc/brickflow.git@{tag}",
                "repo": None,
            }
        }
        diff = DeepDiff(expected, lib)
        assert not diff, diff
