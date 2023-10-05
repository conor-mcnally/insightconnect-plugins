# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve a page of investigations matching the given request parameters"


class Input:
    EMAIL = "email"
    END_TIME = "end_time"
    INDEX = "index"
    PRIORITIES = "priorities"
    SIZE = "size"
    SORT = "sort"
    SOURCES = "sources"
    START_TIME = "start_time"
    STATUSES = "statuses"


class Output:
    INVESTIGATIONS = "investigations"
    METADATA = "metadata"


class ListInvestigationsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "email": {
      "type": "string",
      "title": "Email",
      "description": "A user's email address, where only investigations assigned to that user will be included",
      "order": 6
    },
    "end_time": {
      "type": "string",
      "title": "End Time",
      "displayType": "date",
      "description": "An optional-ISO formatted timestamp, where only investigations whose createTime is before this date will be returned",
      "format": "date-time",
      "order": 3
    },
    "index": {
      "type": "integer",
      "title": "Index",
      "description": "Zero-based index of the page to retrieve, where value must be greater than or equal to 0",
      "default": 0,
      "order": 5
    },
    "priorities": {
      "type": "array",
      "title": "Priorities",
      "description": "A comma-separated list of investigation priorities to include in the result, where possible values are LOW, MEDIUM, HIGH, CRITICAL",
      "items": {
        "type": "string"
      },
      "order": 7
    },
    "size": {
      "type": "integer",
      "title": "Size",
      "description": "Amount of data for a page to retrieve, where its value must be greater than 0 or less than or equal to 100",
      "default": 100,
      "order": 4
    },
    "sort": {
      "type": "string",
      "title": "Sort",
      "description": "A field for investigations to be sorted",
      "enum": [
        "",
        "Create time Ascending",
        "Create time Descending",
        "Priority Ascending",
        "Priority Descending",
        "Last alert time Ascending",
        "Last alert time Descending",
        "RRN Ascending",
        "RRN Descending",
        "Alerts most recent created time Ascending",
        "Alerts most recent created time Descending",
        "Alerts most recent detection created time Ascending",
        "Alerts most recent detection created time Descending"
      ],
      "order": 8
    },
    "sources": {
      "type": "array",
      "title": "Sources",
      "description": "A comma-separated list of investigation sources to include in the result, where possible values are USER, ALERT, HUNT, AUTOMATION",
      "items": {
        "type": "string"
      },
      "order": 9
    },
    "start_time": {
      "type": "string",
      "title": "Start Time",
      "displayType": "date",
      "description": "An optional ISO-formatted timestamp, where only investigations whose createTime is after this date will be returned",
      "format": "date-time",
      "order": 2
    },
    "statuses": {
      "type": "array",
      "title": "Statuses",
      "description": "Comma-separated list of investigation statuses to include in the result. Possible values are OPEN, CLOSED, INVESTIGATING, WAITING",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "index",
    "size"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListInvestigationsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "investigations": {
      "type": "array",
      "title": "Investigations",
      "description": "A list of found investigations",
      "items": {
        "$ref": "#/definitions/investigation"
      },
      "order": 1
    },
    "metadata": {
      "$ref": "#/definitions/investigation_metadata",
      "title": "Metadata",
      "description": "The pagination parameters used to generate this page result",
      "order": 2
    }
  },
  "required": [
    "investigations",
    "metadata"
  ],
  "definitions": {
    "assignee": {
      "type": "object",
      "title": "assignee",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "description": "The email of the assigned user",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the assigned user",
          "order": 2
        }
      }
    },
    "investigation": {
      "type": "object",
      "title": "investigation",
      "properties": {
        "assignee": {
          "$ref": "#/definitions/assignee",
          "title": "Assignee",
          "description": "The user assigned to this investigation, if any",
          "order": 1
        },
        "created_time": {
          "type": "string",
          "title": "Created Time",
          "description": "The time the investigation was created as an ISO formatted timestamp",
          "order": 2
        },
        "disposition": {
          "type": "string",
          "title": "Disposition",
          "description": "The disposition of this investigation, where possible values are BENIGN, MALICIOUS, NOT_APPLICABLE, and UNSPECIFIED",
          "order": 3
        },
        "first_alert_time": {
          "type": "string",
          "title": "First Alert Time",
          "description": "The create time of the first alert belonging to this investigation",
          "order": 4
        },
        "last_accessed": {
          "type": "string",
          "title": "Last Accessed",
          "description": "The time investigation was last viewed or modified",
          "order": 5
        },
        "latest_alert_time": {
          "type": "string",
          "title": "Latest Alert Time",
          "description": "The create time of the most recent alert belonging to this investigation",
          "order": 6
        },
        "organization_id": {
          "type": "string",
          "title": "Organization ID",
          "description": "The id of the organization that owns this investigation",
          "order": 7
        },
        "priority": {
          "type": "string",
          "title": "Priority",
          "description": "The investigations priority, where possible values are CRITICAL, HIGH, MEDIUM, LOW, and UNKNOWN",
          "order": 8
        },
        "rrn": {
          "type": "string",
          "title": "RRN",
          "description": "The RRN of the investigation",
          "order": 9
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "The source of this investigation",
          "order": 10
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The status of the investigation",
          "order": 11
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Investigation title",
          "order": 12
        }
      },
      "required": [
        "created_time",
        "disposition",
        "last_accessed",
        "organization_id",
        "priority",
        "rrn",
        "source",
        "status",
        "title"
      ],
      "definitions": {
        "assignee": {
          "type": "object",
          "title": "assignee",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "description": "The email of the assigned user",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the assigned user",
              "order": 2
            }
          }
        }
      }
    },
    "investigation_metadata": {
      "type": "object",
      "title": "investigation_metadata",
      "properties": {
        "index": {
          "type": "integer",
          "title": "Index",
          "description": "The zero-based index of the page retrieved",
          "order": 1
        },
        "size": {
          "type": "integer",
          "title": "Size",
          "description": "The size of the page requested",
          "order": 2
        },
        "total_data": {
          "type": "integer",
          "title": "Total Data",
          "description": "The total number of results available with the given filter parameters",
          "order": 3
        },
        "total_pages": {
          "type": "integer",
          "title": "Total Pages",
          "description": "The total number of pages available with the given filter parameters",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
