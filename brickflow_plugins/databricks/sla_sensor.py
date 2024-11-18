from pydantic import SecretStr, BaseModel, ValidationError
from typing import Union, List, Optional, Literal
from datetime import timedelta, datetime, timezone
from warnings import warn
from textwrap import dedent
import requests
import time
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from brickflow import ctx
from brickflow_plugins.databricks.workflow_dependency_sensor import (
    WorkflowTaskDependencySensor,
    WorkflowDependencySensorException,
)


class EmailParams(BaseModel):
    email_list: List[str]
    sender_address: str
    port: int
    host: str
    cc: Optional[List[str]] = []
    priority: Optional[Literal["1", "2", "3", "4", "5"]] = "3"


class SLASensorTimeoutException(TimeoutError):
    pass


class SLASensorException(Exception):
    pass


class SLASensor(WorkflowTaskDependencySensor):
    # TODO: implement function report_sla_miss() that records the workflow metadata and the sla miss for reporting purposes
    """
    A special case of a WorkflowTaskDependencySensor that monitors a workflow's end task and expected completion time in UTC.
    Alerts specified users if end time is beyond `expected_sla_timestamp_utc`.

    Two options to provide an SLA:
        1. pass a datetime object with utc timezone specification as `expected_sla_timestamp_utc`
            * `expected_sla_timestamp_utc` must be passed as a datetime object in UTC. it will not be converted.
        2. tag the workflow with a key-value tag. pass the key to `sla_tag_key` and ensure that the value ENDS with a 5-place quartz cron expression (e.g. 0 10 @ @ @)

        If both options are provided, the sensor will default to using the datetime object in `expected_sla_timestamp_utc`

    This task should not be a dependency of the workflow it's monitoring. It should run concurrently with tasks in the monitored workflow:

        sla_sensor_task

        start -> task_1 -> task_2 -> end

    Parameters
        ----------
    monitored_task_name : str
        final task of target workflow
    env : str
        environment sensor is running in
    data_product : str
        name of data product
    run_date : str
        date that sensor is running for alert
    sla_sensor_task_names : List[str]
        name of tasks with SLASensor, to omit from reporting running tasks
    sla_tag_key : str
        key for tag that contains a quartz cron schedule indicating SLA time
        defaults to None
    expected_sla_timestamp_utc : datetime
        time workflow is expected to have been completed. datetime object with UTC timezone
        defaults to None
    dependency_job_name : str
        name of the databricks job the sensor is monitoring.  can be current workflow or other
    databricks_host : str
        databricks host url to find workflow
    databricks_token : Union[str, SecretStr]
        databricks token for authentication
    poke_interval_seconds : int
        frequency in seconds between status checks
        defaults to 60
    custom_description : str
        text to include in an additional context field.
        defaults to "SLA Missed"
    slack_webhook_url : str
        slack url to send notifications
    email_params : dict
        parameters to send emails:
            email_list : list of email recipients
            sender_address : email of sender
            cc : list of recipients to cc (optional)
            port : integer port number
            host : email host url
            priority : string priority level of email where 1 is highest and 5 is lowest. defaults to 3 (normal)
    timeout_seconds : int
        how long in seconds to check for a running workflow to monitor. if a task is found, the timeout seconds are ignored thereafter.
        defaults to an hour.

    Returns
    -------
    str: "SLA Met" or "SLA Missed"

    Example Usage
    --------

        service_principal_pat = ctx.dbutils.secrets.get("scope", "service_principal_id")

        sensor = SLASensor(
                    expected_sla_timestamp=datetime(2024, 1, 1, 10, 0, 0, tzinfo=pytz.utc),
                    monitored_task_name="end",
                    env="dev",
                    data_product="product_name",
                    run_date="2024-01-01",
                    sla_sensor_task_names=["sla_sensor_task"],
                    dependency_job_name="target_job_name",
                    databricks_host="https://your_workspace_url.cloud.databricks.com",
                    databricks_token=service_principle_pat,
                    custom_description="message to provide additional context",
                    slack_webhook_url="https://hooks.slack.com/your/webhook/url",
                    email_params={
                        "email_list": ["recipient_1@email.com", "recipient_2@email.com"],
                        "sender_address": "sender@email.com",
                        "cc": ["cc_1@email.com","cc_2@email.com"],
                        "port": 25,
                        "host": "your.email.host",
                        "priority": "1"
                    },
                    timeout_seconds=120
                )

        result = sensor.monitor()

    In the above snippet Databricks secrets are used as a secure service to store the databricks token.
    If you get your token from another secret management service, like AWS Secrets Manager, GCP Secret Manager
    or Azure Key Vault, just pass it in the databricks_token argument.

    """

    def __init__(
        self,
        monitored_task_name: str,
        env: str,
        data_product: str,
        run_date: str,
        sla_sensor_task_names: List[str],
        dependency_job_name: str,
        sla_tag_key: str = None,
        expected_sla_timestamp_utc: datetime = None,
        databricks_host: str = None,
        databricks_token: Union[str, SecretStr] = None,
        poke_interval_seconds: int = 60,
        custom_description: str = None,
        slack_webhook_url: str = None,
        email_params: dict = None,
        timeout_seconds: int = None,
    ):
        self.start_time = time.time()

        super().__init__(
            dependency_job_name=dependency_job_name,
            dependency_task_name=monitored_task_name,
            delta=timedelta(),
            timeout_seconds=None,
            databricks_host=databricks_host,
            databricks_token=databricks_token,
            poke_interval_seconds=poke_interval_seconds,
        )

        self.dependency_job_id = self._get_job_id
        self.monitored_task_name = monitored_task_name
        self.dependency_job_name = dependency_job_name
        self.databricks_host = databricks_host
        self.databricks_token = databricks_token
        self.sla_sensor_task_names = sla_sensor_task_names
        self.env = env
        self.data_product = data_product
        self.run_date = run_date
        self.sla_missed = False

        if sla_tag_key is None and expected_sla_timestamp_utc is None:
            raise SLASensorException(
                "No SLA provided. Either provide a tag with a cron expression in sla_tag or a datetime object in expected_sla_timestamp_utc"
            )

        if expected_sla_timestamp_utc:
            if expected_sla_timestamp_utc.tzinfo is None:
                warn(
                    "The provided expected_sla_timestamp_utc datetime object does not have any timezone information. It will be assumed to be UTC. If this is not the case, please add timezone information to your datetime object",
                    RuntimeWarning,
                    stacklevel=2,
                )

            self.log.info(
                f"Datetime object provided for SLA: {str(expected_sla_timestamp_utc)}"
            )
            self.expected_sla_timestamp_utc = expected_sla_timestamp_utc
        else:
            self.log.info(
                f"Retrieving expected SLA time from provided workflow tag: {sla_tag_key}"
            )
            self.expected_sla_timestamp_utc = self.parse_tagged_sla(sla_tag_key)

        # check the timezone of provided timestamp
        if self.expected_sla_timestamp_utc.tzinfo is None:
            warn(
                "The provided expected_sla_timestamp_utc datetime object does not have any timezone information. It will be assumed to be UTC. If this is not the case, please add timezone information to your datetime object",
                RuntimeWarning,
                stacklevel=2,
            )

        self.log.info(f"Retrieving an active run id for: {self.dependency_job_name}")
        self.timeout = (
            timeout_seconds if timeout_seconds else timedelta(hours=1).seconds
        )
        self.run_id = self.get_target_run_id(self.run_date, self.dependency_job_name)

        # get the start timestamp (unix) for the current job
        self.run_start_timestamp = self.get_execution_start_timestamp()

        # convert start timestamp to human readable
        self.display_start_timestamp = datetime.fromtimestamp(
            self.run_start_timestamp / 1000
        ).strftime("%Y-%m-%d %H:%M:%S")

        # hold for task list running if/when sla sensor fires
        self.running_tasks = None

        # where to send slack notifications
        self.slack_webhook_url = slack_webhook_url

        # email configuration
        if email_params:
            try:
                self.email_params = EmailParams(**email_params)
                self.alert_email_list = self.email_params.email_list
                self.sender = self.email_params.sender_address
                self.cc = self.email_params.cc
                self.email_port = self.email_params.port
                self.email_host = self.email_params.host
                self.email_priority = self.email_params.priority
            except ValidationError as e:
                self.log.error(f"Error with email_params: {e}")
        else:
            self.email_params = email_params  # will be None

        # warn if no alert destinations provided. sensor will work, will not have any alert sent.
        if not (self.slack_webhook_url or self.email_params):
            warn(
                "There is no one set to receive SLA notifications. Please add at least one of 'slack_webhook_url' or 'alert_email_list' to receive notifications from this sensor",
                RuntimeWarning,
                stacklevel=2,
            )

        self.custom_description = (
            custom_description if custom_description is not None else "SLA Missed"
        )

    def get_job_configuration(self):
        try:
            return self._workspace_obj.jobs.get(job_id=self.dependency_job_id)
        except SLASensorException as e:
            self.log.error(f"Error retrieving job configuration: {e}")

    def parse_tagged_sla(self, sla_tag_key):
        """
        Accepts a tag key to retrieve from job settings.
        Assumes it ends with a 5-place quartz cron expression and extracts the time only (first 2 positions)
        Must be a fixed time.
        Returns a datetime object using the extracted time and the current date.
        """
        job = self.get_job_configuration()

        try:
            tag_value = job.settings.tags[sla_tag_key]
        except:
            raise SLASensorException(
                f"Workflow tag {sla_tag_key} returns None. Cannot create an SLA timestamp. Please ensure this tag key has been added to your workflow"
            )

        cron_expression = tag_value.rstrip().split(" ")[
            -5:
        ]  # remove any inadvertent right side whitespace

        try:
            minute = int(cron_expression[0])
            hour = int(cron_expression[1])
            sla_datetime = datetime.now(timezone.utc).replace(
                hour=hour, minute=minute, second=0, microsecond=0
            )
            self.log.info(f"SLA read from {sla_tag_key}: {str(sla_datetime)}")
            return sla_datetime
        except ValueError as ve:
            self.log.error(f"Error converting SLA time fields to datetime object: {ve}")

    def construct_email(
        self,
        env,
        data_product,
        dep_job_name,
        run_date,
        start_timestamp,
        monitored_task_name,
        expected_sla_timestamp_utc,
        custom_description,
        running_tasks,
    ):
        """
        Constructs email for SLA Alert
        """
        subject = (
            f"{env.upper()}: SLA Missed for Workflow {dep_job_name} for {run_date} Run!"
        )
        body = f"""
                    <br><br> This Databricks workflow is running behind schedule and missed SLA on {run_date} <br><br>
                    <table>
                    <tr><td>Data product: {data_product}</td></tr>
                    <tr><td>Workflow name:</td> <td>{dep_job_name}</td> </tr>
                    <tr><td>Workflow execution time:</td> <td> <b> {start_timestamp} </b> </td> </tr>
                    <tr><td>Workflow started at:</td> <td> {start_timestamp} </td> </tr>
                    <tr><td>Task name:</td> <td> {monitored_task_name} </td> </tr>
                    <tr><td>Expected Workflow end timestamp:</td> <td> {str(expected_sla_timestamp_utc)}</td> </tr>
                    <tr><td>Additional context:</td> <td> {custom_description}</td> </tr>
                    <tr><td>Running tasks:</td> <td> {running_tasks}</td> </tr>
                    </table>
                    <br>
                    Please check your production support channels for next steps on <b>{dep_job_name}</b><br>
                    This is an auto-generated email. Please do not reply. <br><br>
                    Thank you! <br>
                """

        return {"subject": subject, "body": body}

    def send_slack_message(
        self,
        env,
        data_product,
        dep_job_name,
        run_date,
        start_timestamp,
        monitored_task_name,
        expected_sla_timestamp_utc,
        custom_description,
        running_tasks,
    ):
        """
        Sends Slack message to provided webhook for SLA Alert
        """
        title = f"SLA Missed for {dep_job_name}"

        content = f"""This Databricks workflow has missed SLA for the {run_date} Run!

                    ====================Details====================
                    Data product: {data_product}
                    Workflow name: {dep_job_name}
                    Workflow execution time: {start_timestamp}
                    Workflow started at: {start_timestamp}
                    Task name: {monitored_task_name}
                    Expected Workflow end timestamp: {str(expected_sla_timestamp_utc)}
                    Additional context: {custom_description}
                    Running tasks: {running_tasks}
                    ================================================

                    Please check your production support channels for next steps on {dep_job_name}.

                    This is an auto-generated message. Please do not reply.

                    Thank you!
                    """

        message = dedent(
            f"""
                    :large_yellow_circle:   *{"WARN"}:*  {title}
                    *Environment:* {env}
                    *Application:* {data_product}
                    *Message:* {content}
                    *Timestamp:* {datetime.now(timezone.utc)}
                """
        )

        payload = {
            "attachments": [
                {
                    "blocks": [
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": message,
                            },
                            "expand": True,
                        }
                    ],
                }
            ]
        }

        response = requests.post(
            self.slack_webhook_url,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"},
        )

        self.log.info(f"Response: {response.text}")
        self.log.info(f"Response status code: {response.status_code}")

    def send_email_alert(self, content):
        """
        Sends constructed email
        """
        email = MIMEMultipart("alternative")
        email["Subject"] = content["subject"]
        email["From"] = self.sender
        email["To"] = ",".join(self.alert_email_list)
        email["Cc"] = ",".join(self.cc)
        email["X-Priority"] = self.email_priority

        receiver = self.alert_email_list
        email_body = content["body"]
        html = MIMEText(email_body, "html")
        email.attach(html)
        smtp_obj = smtplib.SMTP("{0}".format(self.email_host), port=self.email_port)
        smtp_obj.sendmail(self.sender, receiver, email.as_string())
        smtp_obj.quit()

    def get_execution_start_timestamp(self):
        """
        Get the unix timestamp of the current job given the job run id
        """
        if self.run_id is None:
            raise SLASensorException(
                "run_id is empty, job with provided name was not found"
            )

        run = self._workspace_obj.jobs.get_run(run_id=self.run_id)

        return run.start_time

    def get_current_timestamp(self):
        return datetime.now(timezone.utc)

    def get_target_run_id(self, run_date, dependency_job_name):
        """
        Looks for an actively running job for a given workflow on a given run_date.
        """
        while True:
            jobs = self._workspace_obj.jobs.list(name=dependency_job_name)

            job_id = [i.job_id for i in jobs]

            runs = self._workspace_obj.jobs.list_runs(job_id=job_id[0])

            for run in runs:
                start_date = datetime.fromtimestamp(run.start_time / 1000).strftime(
                    "%Y-%m-%d"
                )

                if start_date == run_date:
                    if run.end_time == 0:
                        # there's an active run
                        self.log.info(f"Found an active run! id: {run.run_id}")
                        return run.run_id

            if (
                self.timeout is not None
                and (time.time() - self.start_time) > self.timeout
            ):
                raise SLASensorTimeoutException(
                    f"No running instances of dependency workflow found. The job has timed out."
                )

            self.log.info(
                f"No running instance of dependency workflow. Sleeping for: {self.poke_interval}"
            )
            time.sleep(self.poke_interval)

    def monitor(self):
        """
        Monitors the current workflow, specifically a monitored task to use as an indicator for meeting SLA
        """
        self.log.info(
            dedent(
                f"""
                      ********************
                      Starting SLA Sensor
                      Job Name: {self.dependency_job_name}
                      Run ID: {self.run_id}
                      Run Date: {self.run_date}
                      SLA Time: {self.expected_sla_timestamp_utc} UTC
                      ********************
                      """
            )
        )

        while True:
            """
            Poke the workspace object for status check
            """
            current_run = self._workspace_obj.jobs.get_run(run_id=self.run_id)

            """
            Check SLA first in event workflow started late. Notification should be sent ASAP.
            """
            current_timestamp = self.get_current_timestamp()

            if (
                not self.sla_missed
                and current_timestamp > self.expected_sla_timestamp_utc
            ):
                # get running tasks, ignoring the sla sensor tasks
                self.running_tasks = [
                    t.task_key
                    for t in current_run.tasks
                    if t.state.life_cycle_state.value == "RUNNING"
                    and t.task_key not in self.sla_sensor_task_names
                ]

                self.log.info(f"SLA HAS BEEN MISSED. SEND NOTIFICATION.")
                self.log.info(f"RUNNING TASKS: {', '.join(self.running_tasks)}")
                self.sla_missed = True

                if self.email_params:
                    try:
                        self.log.info(
                            f"Attemtping to send email notification to {self.alert_email_list}"
                        )
                        email_content = self.construct_email(
                            self.env,
                            self.data_product,
                            self.dependency_job_name,
                            self.run_date,
                            self.display_start_timestamp,
                            self.monitored_task_name,
                            self.expected_sla_timestamp_utc,
                            self.custom_description,
                            self.running_tasks,
                        )

                        self.send_email_alert(email_content)
                        self.log.info("Email sent successfully")
                    except SLASensorException as e:
                        self.log.info(
                            f"Problem sending notification email: {e}\nReview your email parameters: {self.email_params}"
                        )

                if self.slack_webhook_url:
                    try:
                        self.log.info("Attempting to send slack notification")
                        self.send_slack_message(
                            self.env,
                            self.data_product,
                            self.dependency_job_name,
                            self.run_date,
                            self.display_start_timestamp,
                            self.monitored_task_name,
                            self.expected_sla_timestamp_utc,
                            self.custom_description,
                            self.running_tasks,
                        )
                        self.log.info("Slack message sent successfully")
                    except SLASensorException as e:
                        self.log.info(
                            f"Problem sending slack message: {e}\nCheck your slack configuration for webhook: {self.slack_webhook_url}"
                        )

            if self.sla_missed:
                self.log.info("SLA Alert has fired. Finishing task.")
                return "SLA Missed"

            """
            SLA alert has not fired. Check for task completion
            """
            for task in current_run.tasks:
                if task.task_key == self.monitored_task_name:
                    self.log.info(f"Found target task: {self.monitored_task_name}")
                    task_state = task.state.result_state
                    task_life_cycle_state = task.state.life_cycle_state

                    self.log.info(
                        f"Current life cycle state: {task_life_cycle_state.value}"
                    )

                    if task_state:
                        self.log.info(f"Target task is in a terminated state!")
                        if task_state.value == "SUCCESS":
                            self.log.info(
                                f"Monitored task {self.monitored_task_name} for SLA sensor found in {task_state.value} state\n"
                                f"Workflow has completed at {str(datetime.now(timezone.utc))} UTC"
                            )
                            return "SLA Missed" if self.sla_missed else "SLA Met"
                        else:
                            self.log.info(
                                f"Monitored task {self.monitored_task_name} for SLA sensor found in {task_state.value} state\n"
                                f"Workflow is no longer running as of {str(datetime.now(timezone.utc))} UTC"
                            )
                            return "SLA Missed" if self.sla_missed else "SLA Met"

            self.log.info("Monitored task is still running...")

            self.log.info(f"Sleeping for: {self.poke_interval}")
            time.sleep(self.poke_interval)
