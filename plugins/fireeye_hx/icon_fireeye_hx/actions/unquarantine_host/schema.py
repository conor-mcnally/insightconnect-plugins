# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Remove a host from quarantine"


class Input:
    AGENT_ID = "agent_id"
    

class Output:
    SUCCESS = "success"
    

class UnquarantineHostInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent_id": {
      "type": "string",
      "title": "Agent ID",
      "description": "The ID of the agent you want to unisolate",
      "order": 1
    }
  },
  "required": [
    "agent_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UnquarantineHostOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether the action was successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)