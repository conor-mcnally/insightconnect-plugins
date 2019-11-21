# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Tweet"


class Input:
    MSG = "msg"
    

class Output:
    URL = "url"
    

class PostInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "msg": {
      "type": "string",
      "title": "Msg",
      "description": "Text to tweet",
      "order": 1
    }
  },
  "required": [
    "msg"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PostOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "url": {
      "type": "string",
      "title": "URL of Tweet",
      "description": "URL",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
