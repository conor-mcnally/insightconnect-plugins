# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a vulnerability exception submission"


class Input:
    COMMENT = "comment"
    EXPIRATION = "expiration"
    KEY = "key"
    PORT = "port"
    REASON = "reason"
    SCOPE = "scope"
    TYPE = "type"
    VULNERABILITY = "vulnerability"
    

class Output:
    ID = "id"
    LINKS = "links"
    

class CreateExceptionInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Comment to include in the vulnerability exception submission",
      "default": "Exception created with InsightConnect",
      "order": 5
    },
    "expiration": {
      "type": "string",
      "title": "Expiration",
      "displayType": "date",
      "description": "The date the vulnerability exception expires",
      "format": "date-time",
      "order": 4
    },
    "key": {
      "type": "string",
      "title": "Vulnerability Key",
      "description": "The key to identify a specific instance if the type is Instance",
      "order": 7
    },
    "port": {
      "type": "integer",
      "title": "Vulnerability Port",
      "description": "The port the vulnerability appears on if the type is Instance",
      "order": 8
    },
    "reason": {
      "type": "string",
      "title": "Reason",
      "description": "Reason for the exception",
      "enum": [
        "False Positive",
        "Compensating Control",
        "Acceptable Use",
        "Acceptable Risk",
        "Other"
      ],
      "order": 6
    },
    "scope": {
      "type": "integer",
      "title": "Scope ID",
      "description": "The ID of the scope the vulnerability exception applies to. May be empty if type is Global",
      "order": 3
    },
    "type": {
      "type": "string",
      "title": "Exception Type",
      "description": "The type of vulnerability exception to create",
      "enum": [
        "Global",
        "Site",
        "Asset",
        "Asset Group",
        "Instance"
      ],
      "order": 1
    },
    "vulnerability": {
      "type": "string",
      "title": "Vulnerability",
      "description": "The vulnerability this exception applies to",
      "order": 2
    }
  },
  "required": [
    "comment",
    "reason",
    "type",
    "vulnerability"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateExceptionOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "Created Exception ID",
      "description": "The vulnerability exception that was created",
      "order": 1
    },
    "links": {
      "type": "array",
      "title": "Links",
      "description": "Hypermedia links to corresponding or related resources",
      "items": {
        "$ref": "#/definitions/link"
      },
      "order": 2
    }
  },
  "required": [
    "id",
    "links"
  ],
  "definitions": {
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "href": {
          "type": "string",
          "title": "URL",
          "description": "A hypertext reference, which is either a URI (see RFC 3986) or URI template (see RFC 6570)",
          "order": 1
        },
        "rel": {
          "type": "string",
          "title": "Rel",
          "description": "Link relation type following RFC 5988",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
