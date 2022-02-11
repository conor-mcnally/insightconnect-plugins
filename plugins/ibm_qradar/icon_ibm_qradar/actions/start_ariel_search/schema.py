# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Start an Ariel search"


class Input:
    AQL = "aql"
    

class Output:
    DATA = "data"
    

class StartArielSearchInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "aql": {
      "type": "string",
      "title": "AQL Query",
      "description": "AQL query to perform the search",
      "order": 1
    }
  },
  "required": [
    "aql"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class StartArielSearchOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "$ref": "#/definitions/search",
      "title": "Search Data",
      "description": "JSON data for the Search",
      "order": 1
    }
  },
  "definitions": {
    "error_messages": {
      "type": "object",
      "title": "error_messages",
      "properties": {
        "code": {
          "type": "string",
          "title": "Code",
          "description": "Error Code",
          "order": 1
        },
        "contexts": {
          "type": "array",
          "title": "Contexts",
          "description": "Contexts",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "message": {
          "type": "string",
          "title": "Message",
          "description": "Error message",
          "order": 3
        },
        "severity": {
          "type": "string",
          "title": "Severity",
          "description": "Severity",
          "order": 4
        }
      }
    },
    "search": {
      "type": "object",
      "title": "search",
      "properties": {
        "compressed_data_file_count": {
          "type": "integer",
          "title": "Compressed Data File Count",
          "description": "Compressed data file count",
          "order": 2
        },
        "compressed_data_total_size": {
          "type": "integer",
          "title": "Compressed Data Total Size",
          "description": "Compressed data total size",
          "order": 3
        },
        "cursor_id": {
          "type": "string",
          "title": "Cursor ID",
          "description": "Cursor ID",
          "order": 1
        },
        "data_file_count": {
          "type": "integer",
          "title": "Data File Count",
          "description": "Data file count",
          "order": 4
        },
        "data_total_size": {
          "type": "integer",
          "title": "Data Total Size",
          "description": "Data total size",
          "order": 5
        },
        "desired_retention_time_msec": {
          "type": "integer",
          "title": "Desired Retention Time Milliseconds",
          "description": "Desired retention time Milliseconds",
          "order": 10
        },
        "error_messages": {
          "type": "array",
          "title": "Error Messages",
          "description": "Error messages",
          "items": {
            "$ref": "#/definitions/error_messages"
          },
          "order": 9
        },
        "index_file_count": {
          "type": "integer",
          "title": "Index File Count",
          "description": "Index file count",
          "order": 6
        },
        "index_total_size": {
          "type": "integer",
          "title": "Index Total Size",
          "description": "Index total size",
          "order": 7
        },
        "processed_record_count": {
          "type": "integer",
          "title": "Processed Record Count",
          "description": "Processed record count",
          "order": 8
        },
        "progress": {
          "type": "integer",
          "title": "Progress",
          "description": "Progress",
          "order": 11
        },
        "progress_details": {
          "type": "array",
          "title": "Progress Details",
          "description": "Progress details",
          "items": {
            "type": "integer"
          },
          "order": 12
        },
        "query_execution_time": {
          "type": "integer",
          "title": "Query Execution Time",
          "description": "Query execution time",
          "order": 13
        },
        "query_string": {
          "type": "string",
          "title": "Query String",
          "description": "Query string",
          "order": 14
        },
        "record_count": {
          "type": "integer",
          "title": "Record Count",
          "description": "Record count",
          "order": 15
        },
        "save_results": {
          "type": "boolean",
          "title": "Save Results",
          "description": "Save results",
          "order": 16
        },
        "search_id": {
          "type": "string",
          "title": "Search ID",
          "description": "Search ID",
          "order": 19
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 17
        },
        "subsearch_ids": {
          "type": "array",
          "title": "Sub search IDs",
          "description": "Sub search IDs",
          "items": {
            "type": "string"
          },
          "order": 18
        }
      },
      "definitions": {
        "error_messages": {
          "type": "object",
          "title": "error_messages",
          "properties": {
            "code": {
              "type": "string",
              "title": "Code",
              "description": "Error Code",
              "order": 1
            },
            "contexts": {
              "type": "array",
              "title": "Contexts",
              "description": "Contexts",
              "items": {
                "type": "string"
              },
              "order": 2
            },
            "message": {
              "type": "string",
              "title": "Message",
              "description": "Error message",
              "order": 3
            },
            "severity": {
              "type": "string",
              "title": "Severity",
              "description": "Severity",
              "order": 4
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)