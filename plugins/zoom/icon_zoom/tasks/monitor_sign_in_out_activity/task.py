import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import (
    MonitorSignInOutActivityInput,
    MonitorSignInOutActivityOutput,
    MonitorSignInOutActivityState,
    Component,
)

# Custom imports below
from datetime import datetime, timedelta, timezone, date
from typing import Optional, Union

from icon_zoom.tasks.enums import RunState
from icon_zoom.tasks.dataclasses import TaskOutput
from icon_zoom.util.api import AuthenticationRetryLimitError, AuthenticationError
from icon_zoom.util.event import Event
from typing import Dict, Any


class MonitorSignInOutActivity(insightconnect_plugin_runtime.Task):
    MAX_PAGE_SIZE = 300
    LAST_REQUEST_TIMESTAMP = "last_request_timestamp"
    LATEST_EVENT_TIMESTAMP = "latest_event_timestamp"
    LATEST_EVENT_TIMESTAMP_LATCH = "latest_event_timestamp_latch"
    STATUS_CODE = "status_code"
    PREVIOUS_RUN_STATE = "previous_run_state"

    # Constants related to pagination
    NEXT_PAGE_TOKEN = "next_page_token"  # nosec
    PARAM_START_DATE = "param_start_date"
    PARAM_END_DATE = "param_end_date"

    ZOOM_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

    AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_CAUSE = "OAuth authentication retry limit was met."
    AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_ASSISTANCE = (
        "Ensure your OAuth connection credentials are valid. If running a large number of "
        "integrations with Zoom, consider increasing the OAuth authentication "
        "retry limit to accommodate."
    )
    AUTHENTICATION_ERROR_MESSAGE = (
        "The OAuth token credentials provided in the connection "
        "configuration is invalid. Please verify the credentials are correct "
        "and try again."
    )
    API_CHANGED_ERROR_MESSAGE_CAUSE = "The Zoom API has changed and is no longer supported by this plugin."
    API_CHANGED_ERROR_MESSAGE_ASSISTANCE = "Please contact support for assistance."
    PERMISSIONS_ERROR_MESSAGE = (
        "Health check failed. An error occurred during event collection: insufficient permissions for this action. "
        "Please ensure you add all required scopes for the Rapid7 app in Zoom."
    )
    PERMISSIONS_ERROR_MESSAGE_USER = (
        "Health check failed. An error occurred during event collection: insufficient permissions for this action. "
        "Please ensure you add all required user permissions for the Rapid7 app in Zoom."
    )
    DEFAULT_CUTOFF_HOURS = 24

    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_sign_in_out_activity",
            description=Component.DESCRIPTION,
            input=MonitorSignInOutActivityInput(),
            output=MonitorSignInOutActivityOutput(),
            state=MonitorSignInOutActivityState(),
        )

    # pylint: disable=unused-argument
    def run(self, params={}, state={}, custom_config={}):
        try:
            task_output: TaskOutput = self.loop(state=state, custom_config=custom_config)

            # Turn events list back into a list of dicts
            output = [event.__dict__ for event in task_output.output]
            return output, task_output.state, task_output.has_more_pages, task_output.status_code, task_output.error

        except Exception as error:
            self.logger.error(
                f"An Exception has been raised. Unhandled exception occurred during {self.name} task: {error}"
            )
            return [], {}, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def loop(self, state: Dict[str, Any], custom_config: Dict[str, Any]):  # noqa: C901
        now = self._format_datetime_for_zoom(dt=self._get_datetime_now())

        cutoff = custom_config.get("cutoff", {})
        cutoff_date = cutoff.get("date")
        lookback = custom_config.get("lookback")

        if lookback is not None:
            start_time = self._format_datetime_for_zoom(
                # a default of up to 12 months is used to allow for this to always run if there is missing value in the custom config
                # as if the request is larger than 30 days, the api will only return 30 days worth of data
                datetime(
                    lookback.get("year", date.today().year),
                    lookback.get("month", 1),
                    lookback.get("day", 1),
                    lookback.get("hour", 0),
                    lookback.get("minute", 0),
                    lookback.get("second", 0),
                )
            )
            self.logger.info(f"A custom start time of {start_time} will be used")
        else:
            if cutoff_date is not None:
                start_time = self._format_datetime_for_zoom(
                    # a default of up to 12 months is used to allow for this to always run if there is missing value in the custom config
                    # as if the request is larger than 30 days, the api will only return 30 days worth of data
                    datetime(
                        cutoff_date.get("year", date.today().year),
                        cutoff_date.get("month", 1),
                        cutoff_date.get("day", 1),
                        cutoff_date.get("hour", 0),
                        cutoff_date.get("minute", 0),
                        cutoff_date.get("second", 0),
                    )
                )
            else:
                start_time = self._format_datetime_for_zoom(
                    dt=self._get_datetime_last_x_hours(cutoff.get("hours", self.DEFAULT_CUTOFF_HOURS))
                )

        start_date_params = {
            RunState.starting: start_time,
            RunState.paginating: state.get(self.PARAM_START_DATE),
            RunState.continuing: self._get_last_valid_timestamp(start_time, state),
        }

        end_date_params = {
            RunState.starting: now,
            RunState.paginating: state.get(self.PARAM_END_DATE),
            # last request timestamp if coming from end of pagination, otherwise default to now
            RunState.continuing: state.get(self.PARAM_END_DATE, now),
        }
        rs = self.determine_runstate(state=state)
        self.logger.info(f"Current runstate is: {rs.value}")

        param_request_start_date = start_date_params[rs]
        param_request_end_date = end_date_params[rs]

        self.logger.info(
            f"Getting events for timeframe {param_request_start_date} to {param_request_end_date}. "
            f"Currently paginating: {'false' if rs != RunState.paginating else 'true'}"
        )

        try:
            if state.get(self.NEXT_PAGE_TOKEN):
                self.logger.info(f"About to paginate with token: {state.get(self.NEXT_PAGE_TOKEN)}")
            new_events, pagination_token = self.connection.zoom_api.get_user_activity_events_task(
                start_date=param_request_start_date,
                end_date=param_request_end_date,
                page_size=self.MAX_PAGE_SIZE,
                next_page_token=state.get(self.NEXT_PAGE_TOKEN),
            )
        except Exception as exception:
            self.logger.error(f"An Exception has been raised. Error: {exception}, returning state={state}")
            return self.handle_request_exception(exception=exception, now=now)

        try:
            new_events = sorted([Event(**event) for event in new_events])
        except TypeError as exception:
            self.logger.error(
                f"A TypeError has been raised. Zoom API endpoint output has changed, unable to parse events: {exception}"
            )
            return self.handle_api_changed_exception(now=now)

        # Latest event is used for boundary hash calculation and de-duping if needed
        self.logger.info(f"Got {len(new_events)} raw events from Zoom (pre-deduping)!")
        try:
            latest_event = new_events[-1]
            self.logger.info(f"Latest event from raw event set is {latest_event.time}")
        except IndexError:
            self.logger.info("Unable to get latest event time, no new events found!")
            return self.handle_no_new_events_found(now=now)

        # RunState of 'continuing' requires de-duping
        # 'starting' does not since there are no previous events
        # 'paginating' does not since pages should not include duplicates
        if rs == RunState.continuing or (
            rs == RunState.paginating and state.get(self.PREVIOUS_RUN_STATE) == RunState.continuing.value
        ):
            self.logger.info("Event set requires de-duping")
            # De-dupe events using boundary event hashes from previous run
            deduped_events = self._dedupe_events(
                all_events=new_events,
                latest_event_timestamp=state.get(self.LATEST_EVENT_TIMESTAMP),
            )
            self.logger.info(f"After de-duping, total event count is {len(deduped_events)}")
            new_events = deduped_events

        # Depending on if we get a pagination token, we need to either persist our current query OR reset it
        if pagination_token and len(new_events) >= self.MAX_PAGE_SIZE:
            self.logger.info(f"Pagination token returned by Zoom API ({pagination_token}) - storing pagination info")
            has_more_pages = True
            state[self.NEXT_PAGE_TOKEN] = pagination_token
            state[self.PARAM_START_DATE] = param_request_start_date
            state[self.PARAM_END_DATE] = param_request_end_date
        else:
            if now != param_request_end_date:
                self.logger.info(
                    "No pagination token returned by Zoom API - but end time has not caught up to current time"
                )
                has_more_pages = True
            else:
                self.logger.info("No pagination token returned by Zoom API - all pages have been consumed")
                has_more_pages = False
            if rs == RunState.paginating:
                del state[self.NEXT_PAGE_TOKEN]
                del state[self.PARAM_START_DATE]
                del state[self.PARAM_END_DATE]

        # If we're paginating, that means we just came from a RunState of 'continuing' and are now going
        # through earlier events, so don't store the latest event time.
        if rs != RunState.paginating:
            if has_more_pages:
                state[self.LATEST_EVENT_TIMESTAMP_LATCH] = latest_event.time
            else:
                state[self.LATEST_EVENT_TIMESTAMP] = latest_event.time
            state[self.PREVIOUS_RUN_STATE] = rs.value
        else:
            if not has_more_pages:
                state[self.LATEST_EVENT_TIMESTAMP] = state.get(self.LATEST_EVENT_TIMESTAMP_LATCH)
        state[self.LAST_REQUEST_TIMESTAMP] = now

        self.logger.info(f"Updated state, state is now: {state}")
        return TaskOutput(output=new_events, state=state, has_more_pages=has_more_pages, status_code=200, error=None)

    def _get_last_valid_timestamp(self, start_time: str, state: Dict[str, Union[str, None]]) -> Optional[str]:
        """
        Get the last valid timestamp based on the provided start_time and state.

        This method checks if the last request timestamp in the 'state' dictionary is earlier
        than 'start_time' and returns 'start_time' if true, or returns the last request timestamp
        from the 'state' dictionary if it is later.

        Args:
            start_time (str): The last day to compare against.
            state (dict): The state dictionary containing the last request timestamp.

        Returns:
            int: The last valid timestamp.
        """

        last_request_timestamp = state.get(self.LAST_REQUEST_TIMESTAMP)
        if not last_request_timestamp:
            return
        if last_request_timestamp < start_time:
            self.logger.info(
                f"Saved state {last_request_timestamp} exceeds the cut off. Reverting to use time: {start_time}"
            )
            return start_time
        else:
            return last_request_timestamp

    def determine_runstate(self, state: Dict[str, Any]) -> RunState:
        # First run, clean state, need to calculate start and end times
        if not state.get(self.LAST_REQUEST_TIMESTAMP) and not state.get(self.NEXT_PAGE_TOKEN):
            rs: RunState = RunState.starting

        # 'n' run, no need to calculate start and end times due to continuation of pagination
        elif state.get(self.NEXT_PAGE_TOKEN):
            rs = RunState.paginating

        # 'n' run, no pagination occurring, needs to use latest request timestamp
        else:
            rs = RunState.continuing

        return rs

    def handle_no_new_events_found(self, now: str) -> TaskOutput:
        return TaskOutput(
            output=[],
            state={
                self.LAST_REQUEST_TIMESTAMP: now,
                self.LATEST_EVENT_TIMESTAMP: None,
            },
            has_more_pages=False,
            status_code=200,
            error=None,
        )

    def handle_api_changed_exception(self, now: str) -> TaskOutput:
        return TaskOutput(
            output=[],
            state={
                self.LAST_REQUEST_TIMESTAMP: now,
                self.LATEST_EVENT_TIMESTAMP: None,
            },
            has_more_pages=False,
            status_code=500,
            error=PluginException(
                cause=PluginException.causes[PluginException.Preset.SERVER_ERROR],
                assistance=self.API_CHANGED_ERROR_MESSAGE_ASSISTANCE,
            ),
        )

    def handle_request_exception(self, exception: Exception, now: str) -> TaskOutput:
        if isinstance(exception, (AuthenticationRetryLimitError, AuthenticationError)):
            self.logger.error(
                f"{self.AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_CAUSE} "
                f"{self.AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_ASSISTANCE}"
                if isinstance(exception, AuthenticationRetryLimitError)
                else self.AUTHENTICATION_ERROR_MESSAGE
            )
            return TaskOutput(
                output=[],
                state={
                    self.LAST_REQUEST_TIMESTAMP: now,
                    self.LATEST_EVENT_TIMESTAMP: None,
                },
                has_more_pages=False,
                status_code=401,
                error=PluginException(
                    cause=PluginException.causes[PluginException.Preset.API_KEY],
                    assistance=self.AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_ASSISTANCE,
                ),
            )
        elif isinstance(exception, PluginException):
            # Add additional information to aid customer if correct permissions are not set in the Zoom App
            if "Invalid access token, does not contain scope" in exception.data:
                self.logger.error(self.PERMISSIONS_ERROR_MESSAGE)
                return TaskOutput(
                    output=[],
                    state={
                        self.LAST_REQUEST_TIMESTAMP: now,
                        self.LATEST_EVENT_TIMESTAMP: None,
                    },
                    has_more_pages=False,
                    status_code=403,
                    error=PluginException(
                        cause=PluginException.causes[PluginException.Preset.UNAUTHORIZED],
                        assistance=self.PERMISSIONS_ERROR_MESSAGE,
                        data=exception.data,
                    ),
                )
            elif "No permission." in exception.data:
                self.logger.error(self.PERMISSIONS_ERROR_MESSAGE_USER)
                return TaskOutput(
                    output=[],
                    state={
                        self.LAST_REQUEST_TIMESTAMP: now,
                        self.LATEST_EVENT_TIMESTAMP: None,
                    },
                    has_more_pages=False,
                    status_code=403,
                    error=PluginException(
                        cause=PluginException.causes[PluginException.Preset.UNAUTHORIZED],
                        assistance=self.PERMISSIONS_ERROR_MESSAGE_USER,
                        data=exception.data,
                    ),
                )
        else:
            raise exception

    @staticmethod
    def _dedupe_events(all_events: [Event], latest_event_timestamp: Optional[str] = None) -> [Event]:
        if latest_event_timestamp is None:
            return all_events
        return list(filter(lambda event: event.time > latest_event_timestamp, all_events))

    @staticmethod
    def _get_datetime_now() -> datetime:
        return datetime.now(timezone.utc)

    def _get_datetime_last_x_hours(self, hours: int) -> datetime:
        return self._get_datetime_now() - timedelta(hours=hours)

    def _format_datetime_for_zoom(self, dt: datetime) -> str:
        return dt.strftime(self.ZOOM_TIME_FORMAT)
