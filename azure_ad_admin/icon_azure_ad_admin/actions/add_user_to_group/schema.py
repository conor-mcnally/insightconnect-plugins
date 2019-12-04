# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Add a user to a group"


class Input:
    GROUP_NAME = "group_name"
    USER_ID = "user_id"
    

class Output:
    SUCCESS = "success"
    

class AddUserToGroupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "group_name": {
      "type": "string",
      "title": "Group Name",
      "description": "Group Name e.g. My Azure Group",
      "order": 2
    },
    "user_id": {
      "type": "string",
      "title": "User ID",
      "description": "User ID e.g. user@example.com",
      "order": 1
    }
  },
  "required": [
    "group_name",
    "user_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddUserToGroupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Was operation successful",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
