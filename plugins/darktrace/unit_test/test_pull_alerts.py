import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock

import timeout_decorator
from icon_darktrace.connection.connection import Connection
from icon_darktrace.triggers.pull_alerts import PullAlerts
from icon_darktrace.triggers.pull_alerts.schema import Output

from mock import STUB_CONNECTION, ErrorChecker, MockTriggerResponse, mock_request_200, timeout_pass

TIMEOUT = 2

STUB_TRIGGER_SEND_RESPONSE = {
    "creationTime": 1599807740000,
    "commentCount": 0,
    "pbid": 11,
    "time": 1599807736000,
    "model": {
        "then": {
            "name": "System::Packet Loss",
            "pid": 371,
            "phid": 371,
            "uuid": "b81117bc-2d11-4ed6-11d0-9dd2958cfbff",
            "logic": {"data": [780], "type": "componentList", "version": 1},
            "throttle": 86400,
            "sharedEndpoints": False,
            "actions": {
                "alert": True,
                "antigena": {},
                "breach": True,
                "model": True,
                "setPriority": False,
                "setTag": False,
                "setType": False,
            },
            "tags": [],
            "interval": 3600,
            "sequenced": False,
            "active": True,
            "modified": "2020-09-01 00:11:34",
            "activeTimes": {"devices": {}, "tags": {}, "type": "exclusions", "version": 2},
            "priority": 0,
            "autoUpdatable": True,
            "autoUpdate": True,
            "autoSuppress": True,
            "description": "Packet loss is higher than 30%. Sustained packet loss at or above this level will significantly impact Darktrace detections.\\n\\nAction: Investigate why Darktrace is missing so much traffic. Use the status page to see if the loss is occurring on specific subnets. This model indicates the packet loss is occurring before Darktrace ingestion rather than a problem with the appliance.",
            "behaviour": "decreasing",
            "defeats": [],
            "created": {"by": "System"},
            "edited": {"by": "Nobody"},
            "version": 10,
        },
        "now": {
            "name": "System::Packet Loss",
            "pid": 371,
            "phid": 371,
            "uuid": "b81117bc-2d11-4ed6-11d0-9dd2958cfbff",
            "logic": {"data": [780], "type": "componentList", "version": 1},
            "throttle": 86400,
            "sharedEndpoints": False,
            "actions": {
                "alert": True,
                "antigena": {},
                "breach": True,
                "model": True,
                "setPriority": False,
                "setTag": False,
                "setType": False,
            },
            "tags": [],
            "interval": 3600,
            "sequenced": False,
            "active": True,
            "modified": "2020-09-01 00:11:34",
            "activeTimes": {"devices": {}, "tags": {}, "type": "exclusions", "version": 2},
            "priority": 0,
            "autoUpdatable": True,
            "autoUpdate": True,
            "autoSuppress": True,
            "description": "Packet loss is higher than 30%. Sustained packet loss at or above this level will significantly impact Darktrace detections.\\n\\nAction: Investigate why Darktrace is missing so much traffic. Use the status page to see if the loss is occurring on specific subnets. This model indicates the packet loss is occurring before Darktrace ingestion rather than a problem with the appliance.",
            "behaviour": "decreasing",
            "defeats": [],
            "created": {"by": "System"},
            "edited": {"by": "Nobody"},
            "message": "Increasing cooldown to 24 hours, as the 3.1 software update improved the recognition and reporting of packet loss feeding into Darktrace, which has resulted in this model firing more frequently than required.",
            "version": 10,
        },
    },
    "triggeredComponents": [
        {
            "time": 1599807735000,
            "cbid": 11,
            "cid": 780,
            "chid": 780,
            "size": 1,
            "threshold": 0,
            "interval": 3600,
            "logic": {"data": {"left": "A"}, "version": "v0.1"},
            "metric": {"mlid": 256, "name": "capturelosstoomuchloss", "label": "Capture loss Detected upstream"},
            "triggeredFilters": [
                {
                    "cfid": 7657,
                    "id": "A",
                    "filterType": "Message",
                    "arguments": {"value": ".*rate above [3-9][0-9]\\..*\\%$"},
                    "comparatorType": "matches regular expression",
                    "trigger": {
                        "value": "Host ip-192-168-10-1: The capture loss script detected an estimated loss rate above 45.679%, worker drop rate: 0.000%"
                    },
                }
            ],
        }
    ],
    "score": 0.278,
    "device": {"did": -1},
}


class TestPullAlerts(TestCase):
    @mock.patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_request: mock.Mock) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.trigger = PullAlerts()
        self.trigger.connection = self.connection
        self.trigger.logger = logging.getLogger("action logger")

    @timeout_pass(error_callback=ErrorChecker.check_error)
    @timeout_decorator.timeout(TIMEOUT)
    @mock.patch("requests.request", side_effect=mock_request_200)
    @mock.patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTriggerResponse.send)
    def test_pull_alerts_ok(self, mocked_request: mock.Mock, mocked_trigger_send: mock.Mock) -> None:
        ErrorChecker.set_expected({Output.RESULTS: [STUB_TRIGGER_SEND_RESPONSE]})
        self.trigger.run()
