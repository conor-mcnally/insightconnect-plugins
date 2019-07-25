# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "List notes for this project"


class Input:
    PROJECT_NAME = "project_name"
    

class Output:
    NOTES = "notes"
    

class ListNotesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "project_name": {
      "type": "string",
      "title": "Project Name",
      "order": 1
    }
  },
  "required": [
    "project_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListNotesOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "notes": {
      "type": "array",
      "title": "Notes",
      "items": {
        "$ref": "#/definitions/Note"
      },
      "order": 1
    }
  },
  "required": [
    "notes"
  ],
  "definitions": {
    "Note": {
      "type": "object",
      "title": "Note",
      "properties": {
        "body": {
          "type": "string",
          "title": "Description",
          "description": "Note description",
          "order": 3
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Note ID",
          "order": 1
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Note title",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
