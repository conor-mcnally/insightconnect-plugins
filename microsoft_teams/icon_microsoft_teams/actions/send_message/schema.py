# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Send a message"


class Input:
    CHANNEL_NAME = "channel_name"
    MESSAGE = "message"
    TEAM_NAME = "team_name"
    

class Output:
    MESSAGE = "message"
    

class SendMessageInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "channel_name": {
      "type": "string",
      "title": "Channel Name",
      "description": "Channel",
      "order": 2
    },
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Message to send",
      "order": 3
    },
    "team_name": {
      "type": "string",
      "title": "Team Name",
      "description": "Team name",
      "order": 1
    }
  },
  "required": [
    "channel_name",
    "message",
    "team_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SendMessageOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "$ref": "#/definitions/message",
      "title": "Message",
      "description": "The message object that was created",
      "order": 1
    }
  },
  "definitions": {
    "body": {
      "type": "object",
      "title": "body",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "Content",
          "order": 1
        },
        "contentType": {
          "type": "string",
          "title": "Content Type",
          "description": "Content type",
          "order": 2
        }
      }
    },
    "from": {
      "type": "object",
      "title": "from",
      "properties": {
        "user": {
          "$ref": "#/definitions/user",
          "title": "User",
          "description": "User",
          "order": 1
        }
      },
      "definitions": {
        "user": {
          "type": "object",
          "title": "user",
          "properties": {
            "displayName": {
              "type": "string",
              "title": "Display name",
              "description": "Display name",
              "order": 1
            },
            "id": {
              "type": "string",
              "title": "ID",
              "description": "ID",
              "order": 2
            }
          }
        }
      }
    },
    "message": {
      "type": "object",
      "title": "message",
      "properties": {
        "body": {
          "$ref": "#/definitions/body",
          "title": "Body",
          "description": "Body",
          "order": 1
        },
        "createdDateTime": {
          "type": "string",
          "title": "Created Date Time",
          "description": "Created date time",
          "order": 3
        },
        "from": {
          "$ref": "#/definitions/from",
          "title": "From",
          "description": "From",
          "order": 2
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 8
        },
        "importance": {
          "type": "string",
          "title": "Importance",
          "description": "Importance",
          "order": 5
        },
        "locale": {
          "type": "string",
          "title": "Locale",
          "description": "Locale",
          "order": 7
        },
        "messageType": {
          "type": "string",
          "title": "Message Type",
          "description": "Message type",
          "order": 6
        },
        "webUrl": {
          "type": "string",
          "title": "Web URL",
          "description": "Web URL",
          "order": 4
        }
      },
      "definitions": {
        "body": {
          "type": "object",
          "title": "body",
          "properties": {
            "content": {
              "type": "string",
              "title": "Content",
              "description": "Content",
              "order": 1
            },
            "contentType": {
              "type": "string",
              "title": "Content Type",
              "description": "Content type",
              "order": 2
            }
          }
        },
        "from": {
          "type": "object",
          "title": "from",
          "properties": {
            "user": {
              "$ref": "#/definitions/user",
              "title": "User",
              "description": "User",
              "order": 1
            }
          },
          "definitions": {
            "user": {
              "type": "object",
              "title": "user",
              "properties": {
                "displayName": {
                  "type": "string",
                  "title": "Display name",
                  "description": "Display name",
                  "order": 1
                },
                "id": {
                  "type": "string",
                  "title": "ID",
                  "description": "ID",
                  "order": 2
                }
              }
            }
          }
        },
        "user": {
          "type": "object",
          "title": "user",
          "properties": {
            "displayName": {
              "type": "string",
              "title": "Display name",
              "description": "Display name",
              "order": 1
            },
            "id": {
              "type": "string",
              "title": "ID",
              "description": "ID",
              "order": 2
            }
          }
        }
      }
    },
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "displayName": {
          "type": "string",
          "title": "Display name",
          "description": "Display name",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
