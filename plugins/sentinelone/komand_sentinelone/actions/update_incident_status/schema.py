# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Updates an incident status for incident ID provided"


class Input:
    INCIDENT_STATUS = "incident_status"
    THREAT_ID = "threat_id"
    TYPE = "type"
    

class Output:
    AFFECTED = "affected"
    

class UpdateIncidentStatusInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incident_status": {
      "type": "string",
      "title": "Incident Status",
      "description": "Incident status",
      "enum": [
        "unresolved",
        "in progress",
        "resolved"
      ],
      "order": 2
    },
    "threat_id": {
      "type": "string",
      "title": "Threat ID",
      "description": "ID of a threat",
      "order": 1
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Type of incident",
      "enum": [
        "threat",
        "alert"
      ],
      "order": 3
    }
  },
  "required": [
    "incident_status",
    "threat_id",
    "type"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateIncidentStatusOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "affected": {
      "type": "integer",
      "title": "Affected",
      "description": "Number of entities affected by the requested operation",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
