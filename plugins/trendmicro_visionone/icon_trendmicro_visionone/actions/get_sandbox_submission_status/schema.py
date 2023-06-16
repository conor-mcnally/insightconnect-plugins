# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieves the status of a sandbox analysis submission"


class Input:
    TASK_ID = "task_id"
    

class Output:
    ACTION = "action"
    ARGUMENTS = "arguments"
    CREATED_DATE_TIME = "created_date_time"
    DIGEST = "digest"
    ERROR = "error"
    ID = "id"
    IS_CACHED = "is_cached"
    LAST_ACTION_DATE_TIME = "last_action_date_time"
    RESOURCE_LOCATION = "resource_location"
    STATUS = "status"
    

class GetSandboxSubmissionStatusInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "task_id": {
      "type": "string",
      "title": "Task ID",
      "description": "Task_id from the trendmicro-visionone-submit-file-to-sandbox command output",
      "order": 1
    }
  },
  "required": [
    "task_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetSandboxSubmissionStatusOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "action": {
      "type": "string",
      "title": "Action",
      "description": "Action applied to a submitted object",
      "enum": [
        "analyzeFile",
        "analyzeUrl"
      ],
      "order": 3
    },
    "arguments": {
      "type": "string",
      "title": "Arguments",
      "description": "Arguments for the file submitted",
      "order": 10
    },
    "created_date_time": {
      "type": "string",
      "title": "Created Date Time",
      "description": "Timestamp in ISO 8601 that indicates the object was submitted to the sandbox",
      "order": 6
    },
    "digest": {
      "type": "object",
      "title": "Digest",
      "description": "The hash values for the file analyzed",
      "order": 5
    },
    "error": {
      "type": "object",
      "title": "Error",
      "description": "Error code and message for the submission",
      "order": 4
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Unique alphanumeric string that identifies a submission",
      "order": 1
    },
    "is_cached": {
      "type": "boolean",
      "title": "Is Cached",
      "description": "Parameter that indicates if an object has been analyzed before by the Sandbox Analysis App. Submissions marked as cached do not count toward the daily reserve",
      "order": 9
    },
    "last_action_date_time": {
      "type": "string",
      "title": "Last Action Date Time",
      "description": "Timestamp in ISO 8601 format that indicates when the information about a submission was last updated",
      "order": 7
    },
    "resource_location": {
      "type": "string",
      "title": "Resource Location",
      "description": "Location of the submitted file",
      "order": 8
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Response code for the action call",
      "enum": [
        "succeeded",
        "running",
        "failed"
      ],
      "order": 2
    }
  },
  "required": [
    "action",
    "created_date_time",
    "id",
    "last_action_date_time",
    "status"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)