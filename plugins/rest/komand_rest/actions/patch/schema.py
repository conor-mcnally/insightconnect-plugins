# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Make a PATCH request"


class Input:
    BODY = "body"
    HEADERS = "headers"
    ROUTE = "route"
    

class Output:
    BODY_OBJECT = "body_object"
    BODY_STRING = "body_string"
    HEADERS = "headers"
    STATUS = "status"
    

class PatchInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "body": {
      "type": "array",
      "title": "Body",
      "description": "Payload to submit to the server when making the HTTP Request call",
      "items": {
        "type": "object"
      },
      "order": 3
    },
    "headers": {
      "type": "object",
      "title": "Headers",
      "description": "Headers to use for the request. These will override any default headers",
      "order": 2
    },
    "route": {
      "type": "string",
      "title": "Route",
      "description": "The route to append to the base URL e.g. /org/users",
      "order": 1
    }
  },
  "required": [
    "route"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PatchOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "body_object": {
      "type": "object",
      "title": "Body Object",
      "description": "Response payload from the server as an object",
      "order": 1
    },
    "body_string": {
      "type": "string",
      "title": "Body String",
      "description": "Response payload from the server as a string",
      "order": 2
    },
    "headers": {
      "type": "object",
      "title": "Headers",
      "description": "Response headers from the server",
      "order": 4
    },
    "status": {
      "type": "integer",
      "title": "Status",
      "description": "Status code of the response from the server",
      "order": 3
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
