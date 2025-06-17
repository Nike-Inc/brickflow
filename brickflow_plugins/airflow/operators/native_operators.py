"""
Placeholder for native operators that are deprecated in favor of Databricks native operators.
These operators are provided for informational purposes.
"""


class ShortCircuitOperator:
    def __init__(self):
        raise RuntimeError(
            "ShortCircuitOperator is deprecated. Please use native IfElseConditionTask."
            "Ref: https://engineering.nike.com/brickflow/main/tasks/?h=if#ifelse-task"
        )


class BranchPythonOperator:
    def __init__(self):
        raise RuntimeError(
            "BranchPythonOperator is deprecated. Please use native IfElseConditionTask."
            "Ref: https://engineering.nike.com/brickflow/main/tasks/?h=if#ifelse-task"
        )


# TODO: is it even required?
# def _bash_execute(self, context):  # pylint:disable=unused-argument
#     p = None
#     returncode = None
#     start = time.time()
#     env = self.env
#     if env is None:
#         env = os.environ.copy()

#     # log.info("Command: %s", self.bash_command)

#     with tempfile.TemporaryDirectory(prefix="airflowtmp") as tmp_dir:
#         try:
#             p = subprocess.Popen(  # pylint:disable=consider-using-with
#                 self.bash_command,
#                 shell=True,
#                 cwd=tmp_dir,
#                 executable="/bin/bash",
#                 stderr=subprocess.STDOUT,
#                 stdout=subprocess.PIPE,
#                 universal_newlines=True,
#                 env=env,
#             )
#             for line in iter(p.stdout.readline, ""):
#                 resp = line
#                 log.info("[STDOUT]: %s", line.rstrip())
#             returncode = p.wait()
#             p = None
#             sys.stdout.flush()
#             if returncode != 0:
#                 raise subprocess.CalledProcessError(returncode, self.bash_command)
#         finally:
#             end = time.time()
#             if p is not None:
#                 p.terminate()
#                 p.wait()
#             log.info("Command: exited with return code %s", returncode)
#             log.info("Command took %s seconds", end - start)

#         if self.do_xcom_push is True:
#             return resp[:-1]  # skip newline char at end
#         return


# def _bash_empty_on_kill(self):  # pylint:disable=unused-argument
#     pass


# class BashOperatorModifier(OperatorModifier):
#     @check_if(BashOperator)
#     def modify(
#         self, operator: BashOperator, task: Task, workflow: Workflow
#     ) -> Optional["BashOperator"]:
#         f = types.MethodType(_bash_execute, operator)
#         operator.execute = f
#         operator.on_kill = _bash_empty_on_kill
#         return operator
