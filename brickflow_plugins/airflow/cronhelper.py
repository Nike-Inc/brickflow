import os
from pathlib import Path

from py4j.protocol import Py4JError


class CronHelper:
    def __init__(self):
        jvm = self.get_jvm()

        j_cron_parser = jvm.com.cronutils.parser.CronParser
        j_cron_definition_builder = (
            jvm.com.cronutils.model.definition.CronDefinitionBuilder
        )
        j_cron_type = jvm.com.cronutils.model.CronType
        self._j_cron_mapper = jvm.com.cronutils.mapper.CronMapper
        self._unix_parser = j_cron_parser(
            j_cron_definition_builder.instanceDefinitionFor(j_cron_type.UNIX)
        )
        self._quartz_parser = j_cron_parser(
            j_cron_definition_builder.instanceDefinitionFor(j_cron_type.QUARTZ)
        )

    @staticmethod
    def get_jvm():
        try:
            from py4j.java_gateway import JavaGateway

            cron_utils = (
                Path(os.path.abspath(__file__)).parent.absolute()
                / "cron-utils-9.2.0.jar"
            )
            jg = JavaGateway.launch_gateway(classpath=str(cron_utils))
            return jg.jvm
        except Py4JError as e:
            if str(e).startswith("Could not find py4j jar"):
                from pyspark.sql import SparkSession

                return SparkSession.getActiveSession()._jvm
            else:
                raise e

    def unix_to_quartz(self, unix_cron: str) -> str:
        return (
            self._j_cron_mapper.fromUnixToQuartz()
            .map(self._unix_parser.parse(unix_cron))
            .asString()
        )

    def quartz_to_unix(self, unix_cron: str) -> str:
        return (
            self._j_cron_mapper.fromQuartzToUnix()
            .map(self._quartz_parser.parse(unix_cron))
            .asString()
        )


cron_helper = CronHelper()
