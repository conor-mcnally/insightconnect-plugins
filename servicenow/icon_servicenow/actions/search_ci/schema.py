# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve CI record(s) from ServiceNow based on the provided query"


class Input:
    QUERY = "query"
    TABLE = "table"
    

class Output:
    SERVICENOW_CIS = "servicenow_cis"
    

class SearchCiInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Non-encoded query string for retrieving ServiceNow CI record(s) (e.g. number=INC0000055^ORshort_description=New bug)",
      "order": 2
    },
    "table": {
      "type": "string",
      "title": "Table",
      "description": "The ServiceNow table to execute the query against",
      "order": 1
    }
  },
  "required": [
    "query",
    "table"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchCiOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "servicenow_cis": {
      "type": "array",
      "title": "ServiceNow CIs",
      "description": "List of JSON objects representing the CI record(s) returned by the query",
      "items": {
        "type": "object"
      },
      "order": 1
    }
  },
  "required": [
    "servicenow_cis"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
