# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Search based on MD5 hash"


class Input:
    MD5 = "md5"
    

class Output:
    SIGNATURES = "signatures"
    

class SearchInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "md5": {
      "type": "string",
      "title": "MD5 Hash",
      "description": "MD5 hash",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "signatures": {
      "type": "array",
      "title": "Signatures",
      "description": "Signatures found",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)