# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ASSET_HOSTNAME_DSM = "asset_hostname_dsm"
    ASSET_HOSTNAME_IVM = "asset_hostname_ivm"
    DSM_API_KEY = "dsm_api_key"
    DSM_URL = "dsm_url"
    IVM_URL = "ivm_url"
    IVM_USER_PASSWORD = "ivm_user_password"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "asset_hostname_dsm": {
      "type": "string",
      "title": "Asset Hostname on DSM",
      "description": "Hostname of the asset in the Deep Security Manager",
      "order": 1
    },
    "asset_hostname_ivm": {
      "type": "string",
      "title": "Asset Hostname on IVM",
      "description": "Hostname of the asset in InsightVM",
      "order": 4
    },
    "dsm_api_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Deep Security Manager API Key",
      "description": "API key of the Deep Security Manager",
      "order": 3
    },
    "dsm_url": {
      "type": "string",
      "title": "Deep Security Manager URL",
      "description": "URL of the Deep Security Manager",
      "default": "https://app.deepsecurity.trendmicro.com",
      "order": 2
    },
    "ivm_url": {
      "type": "string",
      "title": "InsightVM URL",
      "description": "URL of the InsightVM console",
      "default": "https://insightvm.company.de:3780/",
      "order": 5
    },
    "ivm_user_password": {
      "$ref": "#/definitions/credential_username_password",
      "title": "IVM Credentials",
      "description": "InsightVM username and password",
      "order": 6
    }
  },
  "required": [
    "dsm_api_key",
    "dsm_url"
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
