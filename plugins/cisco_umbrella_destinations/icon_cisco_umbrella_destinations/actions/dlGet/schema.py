# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get a destination list"


class Input:
    DESTINATIONLISTID = "destinationListId"
    

class Output:
    SUCCESS = "success"
    

class DlGetInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "destinationListId": {
      "type": "integer",
      "title": "Destination List ID",
      "description": "Unique ID for destination list",
      "order": 1
    }
  },
  "required": [
    "destinationListId"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DlGetOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "$ref": "#/definitions/destinationList",
      "title": "Success",
      "description": "Successful returned value",
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {
    "destinationList": {
      "type": "object",
      "title": "destinationList",
      "properties": {
        "access": {
          "type": "string",
          "title": "Access",
          "description": "Can be allow or block",
          "order": 3
        },
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "Timestamp for creation of the destination list",
          "format": "date-time",
          "order": 7
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Unique ID of the destination list",
          "order": 1
        },
        "isGlobal": {
          "type": "boolean",
          "title": "Is Global",
          "description": "Boolean value indicating global state",
          "order": 4
        },
        "isMspDefault": {
          "type": "boolean",
          "title": "Is MSP Default",
          "description": "Whether or not MSP is default",
          "order": 9
        },
        "markedForDeletion": {
          "type": "boolean",
          "title": "Marked for Deletion",
          "description": "Whether or not destination list is marked for deletion",
          "order": 10
        },
        "modifiedAt": {
          "type": "string",
          "title": "Modified At",
          "displayType": "date",
          "description": "Timestamp for modification of the destination list",
          "format": "date-time",
          "order": 8
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Title for the destination list",
          "order": 5
        },
        "organizationId": {
          "type": "integer",
          "title": "Organization ID",
          "description": "ID of organization",
          "order": 2
        },
        "thirdpartyCategoryId": {
          "type": "integer",
          "title": "Third Party Category ID",
          "description": "ID, if any, for third parties",
          "order": 6
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
