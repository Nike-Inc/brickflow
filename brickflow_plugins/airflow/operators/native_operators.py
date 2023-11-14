import os
import subprocess
import sys
import tempfile
import time
import types
from typing import Optional

from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator, ShortCircuitOperator

from brickflow.context import BRANCH_SKIP_EXCEPT, SKIP_EXCEPT_HACK
from brickflow.engine.task import Task
from brickflow.engine.workflow import Workflow
from brickflow_plugins import log
from brickflow_plugins.airflow.operators import OperatorModifier, check_if


def _bash_execute(self, context):  # pylint:disable=unused-argument
    p = None
    returncode = None
    start = time.time()
    env = self.env
    if env is None:
        env = os.environ.copy()

    # log.info("Command: %s", self.bash_command)

    with tempfile.TemporaryDirectory(prefix="airflowtmp") as tmp_dir:
        try:
            p = subprocess.Popen(  # pylint:disable=consider-using-with
                self.bash_command,
                shell=True,
                cwd=tmp_dir,
                executable="/bin/bash",
                stderr=subprocess.STDOUT,
                stdout=subprocess.PIPE,
                universal_newlines=True,
                env=env,
            )
            for line in iter(p.stdout.readline, ""):
                resp = line
                log.info("[STDOUT]: %s", line.rstrip())
            returncode = p.wait()
            p = None
            sys.stdout.flush()
            if returncode != 0:
                raise subprocess.CalledProcessError(returncode, self.bash_command)
        finally:
            end = time.time()
            if p is not None:
                p.terminate()
                p.wait()
            log.info("Command: exited with return code %s", returncode)
            log.info("Command took %s seconds", end - start)

        if self.do_xcom_push is True:
            return resp[:-1]  # skip newline char at end
        return


def _bash_empty_on_kill(self):  # pylint:disable=unused-argument
    pass


def _skip_all_except(
    self, ti: "FakeTaskInstance", branch_task_ids
):  # pylint:disable=unused-argument
    log.info("Skipping all tasks except: %s", branch_task_ids)
    ti.xcom_push(BRANCH_SKIP_EXCEPT, branch_task_ids)


def _short_circuit_execute(self, context):
    condition = super(ShortCircuitOperator, self).execute(context)
    log.info("Condition result is %s", condition)

    if condition:
        log.info("Proceeding with downstream tasks...")
        return

    # log
    log.info("Skipping downstream tasks...")
    ti = context["ti"]
    ti.xcom_push(BRANCH_SKIP_EXCEPT, SKIP_EXCEPT_HACK)


class BashOperatorModifier(OperatorModifier):
    @check_if(BashOperator)
    def modify(
        self, operator: BashOperator, task: Task, workflow: Workflow
    ) -> Optional["BashOperator"]:
        f = types.MethodType(_bash_execute, operator)
        operator.execute = f
        operator.on_kill = _bash_empty_on_kill
        return operator


class BranchPythonOperatorModifier(OperatorModifier):
    @check_if(BranchPythonOperator)
    def modify(
        self, operator: BranchPythonOperator, task: Task, workflow: Workflow
    ) -> Optional["BranchPythonOperator"]:
        f = types.MethodType(_skip_all_except, operator)
        operator.skip_all_except = f
        return operator


class ShortCircuitOperatorModifier(OperatorModifier):
    @check_if(ShortCircuitOperator)
    def modify(
        self, operator: ShortCircuitOperator, task: Task, workflow: Workflow
    ) -> Optional["ShortCircuitOperator"]:
        f = types.MethodType(_short_circuit_execute, operator)
        operator.execute = f
        return operator
