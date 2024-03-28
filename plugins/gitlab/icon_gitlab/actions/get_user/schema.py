# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get GitLab user"


class Input:
    ID = "id"


class Output:
    USER = "user"


class GetUserInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "User ID",
      "description": "User ID",
      "order": 1
    }
  },
  "required": [
    "id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetUserOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user": {
      "$ref": "#/definitions/get_user_output",
      "title": "User",
      "description": "User profile",
      "order": 1
    }
  },
  "definitions": {
    "get_user_output": {
      "type": "object",
      "title": "get_user_output",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 1
        },
        "avatar_url": {
          "type": "string",
          "title": "Avatar URL",
          "description": "Avatar URL",
          "order": 2
        },
        "state": {
          "type": "string",
          "title": "State",
          "description": "State",
          "order": 3
        },
        "web_url": {
          "type": "string",
          "title": "Web URL",
          "description": "Web URL",
          "order": 4
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 5
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "Username",
          "order": 6
        },
        "created_at": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Created At",
          "description": "Create at",
          "order": 7
        },
        "bio": {
          "type": "string",
          "title": "Bio",
          "description": "Bio",
          "order": 8
        },
        "location": {
          "type": "string",
          "title": "Location",
          "description": "Location",
          "order": 9
        },
        "skype": {
          "type": "string",
          "title": "Skype",
          "description": "Skype",
          "order": 10
        },
        "linkedin": {
          "type": "string",
          "title": "LinkedIn",
          "description": "LinkedIn",
          "order": 11
        },
        "twitter": {
          "type": "string",
          "title": "Twitter",
          "description": "Twitter",
          "order": 12
        },
        "website_url": {
          "type": "string",
          "title": "Website URL",
          "description": "Website URL",
          "order": 13
        },
        "organization": {
          "type": "string",
          "title": "Organization",
          "description": "Organization",
          "order": 14
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)