# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Displays information of the specified API key"


class Input:
    ID = "id"


class Output:
    DESCRIPTION = "description"
    ETAG = "etag"
    EXPIRED_DATE_TIME = "expired_date_time"
    ID = "id"
    LAST_USED_DATE_TIME = "last_used_date_time"
    NAME = "name"
    ROLE = "role"
    STATUS = "status"


class GetApiKeyInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The unique identifier of the API key",
      "order": 1
    }
  },
  "required": [
    "id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetApiKeyOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "description": {
      "type": "string",
      "title": "Description",
      "description": "A brief note about the API key",
      "order": 6
    },
    "etag": {
      "type": "string",
      "title": "ETag",
      "description": "Unique alphanumeric string that identifies the version of a resource",
      "order": 1
    },
    "expired_date_time": {
      "type": "string",
      "title": "Expired Date Time",
      "description": "Timestamp in ISO 8601 format indicating the expiration date of the API key",
      "order": 8
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The unique identifier of the API key",
      "order": 2
    },
    "last_used_date_time": {
      "type": "string",
      "title": "Last Used Date Time",
      "description": "Timestamp in ISO 8601 format indicating the last time the API key was used",
      "order": 7
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "The unique name of the API key",
      "order": 3
    },
    "role": {
      "type": "string",
      "title": "Role",
      "description": "The user role assigned to the API key",
      "order": 5
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "The status of an API key",
      "enum": [
        "enabled",
        "disabled"
      ],
      "order": 4
    }
  },
  "required": [
    "expired_date_time",
    "id",
    "last_used_date_time",
    "name",
    "role",
    "status"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)