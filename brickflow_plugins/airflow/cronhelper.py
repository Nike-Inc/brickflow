import functools
import os
from pathlib import Path

from brickflow_plugins import log

try:
    from py4j.protocol import Py4JError
except ImportError:
    raise ImportError(
        "You must install py4j to use cronhelper, "
        "please try pip install py4j. "
        "This library is not installed as "
        "it is provided by databricks OOTB."
    )


class CronHelper:
    _jvm = None

    def __init__(self):
        self._j_cron_mapper = None
        self._unix_parser = None
        self._quartz_parser = None

    @classmethod
    def get_jvm(cls):
        if cls._jvm is None:  # Initialize the JVM only once and cache it
            try:
                log.info(
                    "Attempting to load JVM from pip installation of py4j for cronhelper"
                )
                from py4j.java_gateway import JavaGateway

                cron_utils = (
                    Path(os.path.abspath(__file__)).parent.absolute()
                    / "cron-utils-9.2.0.jar"
                )
                jg = JavaGateway.launch_gateway(classpath=str(cron_utils))
                log.info(
                    "Launched py4j gateway with cronutils jar added to class path from py4j pip installation"
                )
                cls._jvm = jg.jvm
            except Py4JError as e:
                if str(e).startswith("Could not find py4j jar"):
                    log.info(
                        "Could not find py4j jar, attempting to load JVM from SparkSession"
                    )
                    from pyspark.sql import SparkSession

                    cls._jvm = SparkSession.getActiveSession()._jvm
                else:
                    raise e
        return cls._jvm

    def _initialize_jvm(self):
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

    def _get_unix_parser(self):
        if self._unix_parser is None:
            self._initialize_jvm()
        return self._unix_parser

    def _get_quartz_parser(self):
        if self._quartz_parser is None:
            self._initialize_jvm()
        return self._quartz_parser

    @functools.lru_cache(maxsize=128)  # cron expression conversion will not change
    def unix_to_quartz(self, unix_cron: str) -> str:
        unix_parser = self._get_unix_parser()
        quartz_expr = (
            self._j_cron_mapper.fromUnixToQuartz()
            .map(unix_parser.parse(unix_cron))
            .asString()
        )
        log.info("Converted unix cron %s to quartz cron %s", unix_cron, quartz_expr)
        return quartz_expr

    @functools.lru_cache(maxsize=128)  # cron expression conversion will not change
    def quartz_to_unix(self, quartz_cron: str) -> str:
        quartz_parser = self._get_quartz_parser()
        unix_expr = (
            self._j_cron_mapper.fromQuartzToUnix()
            .map(quartz_parser.parse(quartz_cron))
            .asString()
        )
        log.info("Converted quartz cron %s to unix cron %s", quartz_cron, unix_expr)
        return unix_expr


cron_helper = CronHelper()
