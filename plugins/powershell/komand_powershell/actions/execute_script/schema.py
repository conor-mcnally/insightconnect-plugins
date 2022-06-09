# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Execute PowerShell script encoded as a base64 file on a remote host. This action allows you to you provide additional credentials such as username, password, secret_key available in script as PowerShell variables (`$username`, `$password`, `$secret_key`)"


class Input:
    ADD_CREDENTIALS_TO_SCRIPT = "add_credentials_to_script"
    ADDRESS = "address"
    HOST_NAME = "host_name"
    SCRIPT = "script"
    SECRET_KEY = "secret_key"
    USERNAME_AND_PASSWORD = "username_and_password"
    

class Output:
    STDERR = "stderr"
    STDOUT = "stdout"
    

class ExecuteScriptInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "add_credentials_to_script": {
      "type": "boolean",
      "title": "Add Credentials to Script",
      "description": "This parameter indicates whether `Username and Password` and `Secret Key` action parameters will be added to script as PowerShell variables or not. Choosing `True` creates PowerShell variables (`$username`, `$password` and `$secret_key`) which you can use in your script in `Script` parameter. If you don't need those credentials choose `False` and provide some random values for `Username and Password` and `Secret Key` parameters",
      "order": 4
    },
    "address": {
      "type": "string",
      "title": "Address",
      "description": "IP address of the remote host e.g. 192.168.1.1. If address is left blank PowerShell will run locally",
      "order": 2
    },
    "host_name": {
      "type": "string",
      "title": "Host Name",
      "description": "Case-sensitive name of the remote host, eg. MyComputer for Kerberos connection only",
      "order": 3
    },
    "script": {
      "type": "string",
      "title": "Script",
      "displayType": "bytes",
      "description": "PowerShell script as base64",
      "format": "bytes",
      "order": 1
    },
    "secret_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Secret Key",
      "description": "Credential secret key available in script as PowerShell variable (`$secret_key`)",
      "order": 5
    },
    "username_and_password": {
      "$ref": "#/definitions/credential_username_password",
      "title": "Username and Password",
      "description": "Username and password available in script as PowerShell variables (`$username`, `$password`)",
      "order": 6
    }
  },
  "required": [
    "add_credentials_to_script",
    "script",
    "secret_key",
    "username_and_password"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "displayType": "password",
          "description": "The shared secret key",
          "format": "password"
        }
      },
      "required": [
        "secretKey"
      ]
    },
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
          "format": "password",
          "order": 2
        },
        "username": {
          "type": "string",
          "title": "Username",
          "description": "The username to log in with",
          "order": 1
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


class ExecuteScriptOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "stderr": {
      "type": "string",
      "title": "PowerShell Standard Error",
      "description": "PowerShell standard error",
      "order": 2
    },
    "stdout": {
      "type": "string",
      "title": "PowerShell Standard Output",
      "description": "PowerShell standard output",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
