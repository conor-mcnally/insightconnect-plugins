# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    CREDENTIALS = "credentials"
    DB = "db"
    HOST = "host"
    PORT = "port"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "credentials": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Database Credentials",
      "description": "Database username and password",
      "order": 4
    },
    "db": {
      "type": "string",
      "title": "Database Name",
      "description": "Database name",
      "order": 3
    },
    "host": {
      "type": "string",
      "title": "Host",
      "description": "Database hostname",
      "order": 1
    },
    "port": {
      "type": "number",
      "title": "Port",
      "description": "Database port. Port 1433 will be used if this is left blank",
      "order": 2
    }
  },
  "required": [
    "credentials",
    "db",
    "host"
  ],
  "definitions": {
    "credential_username_password": {
      "id": "credential_username_password",
      "type": "object",
      "title": "Credential: Username and Password",
      "description": "A username and password combination",
      "properties": {
        "password": {
          "type": "string",
          "title": "Password",
          "displayType": "password",
          "description": "The password",
          "format": "password"
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with"
        }
      },
      "required": [
        "username",
        "password"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
