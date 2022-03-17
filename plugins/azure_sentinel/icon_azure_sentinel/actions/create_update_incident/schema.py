# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This action creates or updates an incident"


class Input:
    ETAG = "etag"
    INCIDENTID = "incidentId"
    PROPERTIES = "properties"
    RESOURCEGROUPNAME = "resourceGroupName"
    SUBSCRIPTIONID = "subscriptionId"
    WORKSPACENAME = "workspaceName"
    

class Output:
    ETAG = "etag"
    ID = "id"
    NAME = "name"
    PROPERTIES = "properties"
    TYPE = "type"
    

class CreateUpdateIncidentInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "etag": {
      "type": "string",
      "title": "Etag",
      "description": "Etag of the azure resource",
      "order": 5
    },
    "incidentId": {
      "type": "string",
      "title": "Incident ID",
      "description": "Incident ID",
      "order": 1
    },
    "properties": {
      "$ref": "#/definitions/IncidentProperties",
      "title": "Properties",
      "description": "Incident properties object",
      "order": 6
    },
    "resourceGroupName": {
      "type": "string",
      "title": "Resource Group Name",
      "description": "The name of the resource group within the user's subscription. The name is case-insensitive",
      "order": 2
    },
    "subscriptionId": {
      "type": "string",
      "title": "Subscription ID",
      "description": "Azure subscription ID",
      "order": 3
    },
    "workspaceName": {
      "type": "string",
      "title": "Workspace Name",
      "description": "The name of the workspace",
      "order": 4
    }
  },
  "required": [
    "incidentId",
    "properties",
    "resourceGroupName",
    "subscriptionId",
    "workspaceName"
  ],
  "definitions": {
    "CreatedByType": {
      "type": "object",
      "title": "CreatedByType",
      "properties": {
        "Application": {
          "type": "string",
          "title": "Application",
          "description": "Application",
          "order": 1
        },
        "Key": {
          "type": "string",
          "title": "Key",
          "description": "Description",
          "order": 2
        },
        "ManagedIdentity": {
          "type": "string",
          "title": "Managed Indetity",
          "description": "Managed identity",
          "order": 3
        },
        "User": {
          "type": "string",
          "title": "User",
          "description": "User",
          "order": 4
        }
      }
    },
    "IncidentAdditionalData": {
      "type": "object",
      "title": "IncidentAdditionalData",
      "properties": {
        "alertProductNames": {
          "type": "array",
          "title": "Alert Product Names",
          "description": "List of product names of alerts in the incident",
          "items": {
            "type": "string"
          },
          "order": 1
        },
        "alertsCount": {
          "type": "integer",
          "title": "Alert's Count",
          "description": "The number of alerts in the incident",
          "order": 2
        },
        "bookmarksCount": {
          "type": "integer",
          "title": "Bookmarks Count",
          "description": "The number of bookmarks in the incident",
          "order": 3
        },
        "commentsCount": {
          "type": "integer",
          "title": "Comments Count",
          "description": "The number of comments in the incident",
          "order": 4
        },
        "tactics": {
          "type": "array",
          "title": "Tactics",
          "description": "The tactics associated with incident",
          "items": {
            "type": "string"
          },
          "order": 5
        }
      }
    },
    "IncidentLabel": {
      "type": "object",
      "title": "IncidentLabel",
      "properties": {
        "labelName": {
          "type": "string",
          "title": "Label Name",
          "description": "The name of the label",
          "order": 1
        },
        "labelType": {
          "type": "string",
          "title": "The type of label",
          "description": "Label Type",
          "order": 2
        }
      }
    },
    "IncidentOwnerInfo": {
      "type": "object",
      "title": "IncidentOwnerInfo",
      "properties": {
        "assignedTo": {
          "type": "string",
          "title": "Assigned To",
          "description": "The name of the user the incident is assigned to",
          "order": 1
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "The mail of the user the incident is assigned to",
          "order": 2
        },
        "objectId": {
          "type": "string",
          "title": "Object ID",
          "description": "The object id of the user the incident is assigned to",
          "order": 3
        },
        "userPrincipalName": {
          "type": "string",
          "title": "User Principal Name",
          "description": "The user principal name of the user the incident is assigned to",
          "order": 4
        }
      }
    },
    "IncidentProperties": {
      "type": "object",
      "title": "IncidentProperties",
      "properties": {
        "additionalData": {
          "$ref": "#/definitions/IncidentAdditionalData",
          "title": "Additional Data",
          "description": "Additional data on the incident",
          "order": 1
        },
        "classification": {
          "type": "string",
          "title": "Classification",
          "description": "The reason the incident was closed",
          "order": 2
        },
        "classificationComment": {
          "type": "string",
          "title": "Classification Comment",
          "description": "Describes the reason the incident was closed",
          "order": 3
        },
        "classificationReason": {
          "type": "string",
          "title": "Classification Reason",
          "description": "The classification reason the incident was closed with",
          "order": 4
        },
        "createdTimeUtc": {
          "type": "string",
          "title": "Created Time UTC",
          "displayType": "date",
          "description": "The time the incident was created",
          "format": "date-time",
          "order": 5
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "The description of the incident",
          "order": 6
        },
        "etag": {
          "type": "string",
          "title": "Etag",
          "description": "Etag of the azure resource",
          "order": 7
        },
        "firstActivityTimeUtc": {
          "type": "string",
          "title": "First Activity Time UTC",
          "displayType": "date",
          "description": "The time of the first activity in the incident",
          "format": "date-time",
          "order": 8
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Azure resource ID",
          "order": 9
        },
        "incidentNumber": {
          "type": "integer",
          "title": "Incident Number",
          "description": "A sequential number",
          "order": 10
        },
        "incidentUrl": {
          "type": "string",
          "title": "Incident URL",
          "description": "The deep-link URL to the incident in Azure portal",
          "order": 11
        },
        "labels": {
          "type": "array",
          "title": "Labels",
          "description": "List of labels relevant to this incident",
          "items": {
            "$ref": "#/definitions/IncidentLabel"
          },
          "order": 12
        },
        "lastActivityTimeUtc": {
          "type": "string",
          "title": "Last Activity Time UTC",
          "displayType": "date",
          "description": "The time of the last activity in the incident",
          "format": "date-time",
          "order": 13
        },
        "lastModifiedTimeUtc": {
          "type": "string",
          "title": "Last Modified Time UTC",
          "displayType": "date",
          "description": "The last time the incident was updated",
          "format": "date-time",
          "order": 14
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Azure resource name",
          "order": 15
        },
        "owner": {
          "$ref": "#/definitions/IncidentOwnerInfo",
          "title": "Owner",
          "description": "Describes a user that the incident is assigned to",
          "order": 16
        },
        "relatedAnalyticRuleIds": {
          "type": "array",
          "title": "Related Analytic Rule IDs",
          "description": "List of resource ids of Analytic rules related to the incident",
          "items": {
            "type": "string"
          },
          "order": 17
        },
        "severity": {
          "type": "string",
          "title": "Severity",
          "description": "Incidents severity",
          "order": 18
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Incidents status",
          "order": 19
        },
        "systemData": {
          "$ref": "#/definitions/SystemData",
          "title": "System Data",
          "description": "Azure Resource Manager metadata containing createdBy and modifiedBy information",
          "order": 20
        },
        "title": {
          "type": "string",
          "title": "The title of the incident",
          "description": "The title of the incident",
          "order": 21
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Azure resource type",
          "order": 22
        }
      },
      "required": [
        "severity",
        "status"
      ],
      "definitions": {
        "CreatedByType": {
          "type": "object",
          "title": "CreatedByType",
          "properties": {
            "Application": {
              "type": "string",
              "title": "Application",
              "description": "Application",
              "order": 1
            },
            "Key": {
              "type": "string",
              "title": "Key",
              "description": "Description",
              "order": 2
            },
            "ManagedIdentity": {
              "type": "string",
              "title": "Managed Indetity",
              "description": "Managed identity",
              "order": 3
            },
            "User": {
              "type": "string",
              "title": "User",
              "description": "User",
              "order": 4
            }
          }
        },
        "IncidentAdditionalData": {
          "type": "object",
          "title": "IncidentAdditionalData",
          "properties": {
            "alertProductNames": {
              "type": "array",
              "title": "Alert Product Names",
              "description": "List of product names of alerts in the incident",
              "items": {
                "type": "string"
              },
              "order": 1
            },
            "alertsCount": {
              "type": "integer",
              "title": "Alert's Count",
              "description": "The number of alerts in the incident",
              "order": 2
            },
            "bookmarksCount": {
              "type": "integer",
              "title": "Bookmarks Count",
              "description": "The number of bookmarks in the incident",
              "order": 3
            },
            "commentsCount": {
              "type": "integer",
              "title": "Comments Count",
              "description": "The number of comments in the incident",
              "order": 4
            },
            "tactics": {
              "type": "array",
              "title": "Tactics",
              "description": "The tactics associated with incident",
              "items": {
                "type": "string"
              },
              "order": 5
            }
          }
        },
        "IncidentLabel": {
          "type": "object",
          "title": "IncidentLabel",
          "properties": {
            "labelName": {
              "type": "string",
              "title": "Label Name",
              "description": "The name of the label",
              "order": 1
            },
            "labelType": {
              "type": "string",
              "title": "The type of label",
              "description": "Label Type",
              "order": 2
            }
          }
        },
        "IncidentOwnerInfo": {
          "type": "object",
          "title": "IncidentOwnerInfo",
          "properties": {
            "assignedTo": {
              "type": "string",
              "title": "Assigned To",
              "description": "The name of the user the incident is assigned to",
              "order": 1
            },
            "email": {
              "type": "string",
              "title": "Email",
              "description": "The mail of the user the incident is assigned to",
              "order": 2
            },
            "objectId": {
              "type": "string",
              "title": "Object ID",
              "description": "The object id of the user the incident is assigned to",
              "order": 3
            },
            "userPrincipalName": {
              "type": "string",
              "title": "User Principal Name",
              "description": "The user principal name of the user the incident is assigned to",
              "order": 4
            }
          }
        },
        "SystemData": {
          "type": "object",
          "title": "SystemData",
          "properties": {
            "createdAt": {
              "type": "string",
              "title": "Created At",
              "displayType": "date",
              "description": "The timestamp of resource creation (UTC)",
              "format": "date-time",
              "order": 1
            },
            "createdBy": {
              "type": "string",
              "title": "Created By",
              "description": "The identity that created the resource",
              "order": 2
            },
            "createdByType": {
              "$ref": "#/definitions/CreatedByType",
              "title": "Created By Type",
              "description": "The type of identity that created the resource",
              "order": 3
            },
            "lastModifiedAt": {
              "type": "string",
              "title": "Last Modified At",
              "displayType": "date",
              "description": "The timestamp of resource last modification (UTC)",
              "format": "date-time",
              "order": 4
            },
            "lastModifiedBy": {
              "type": "string",
              "title": "Last Modified By",
              "description": "The identity that last modified the resource",
              "order": 5
            },
            "lastModifiedByType": {
              "$ref": "#/definitions/CreatedByType",
              "title": "Last Modified By Type",
              "description": "The type of identity that last modified the resource",
              "order": 6
            }
          },
          "definitions": {
            "CreatedByType": {
              "type": "object",
              "title": "CreatedByType",
              "properties": {
                "Application": {
                  "type": "string",
                  "title": "Application",
                  "description": "Application",
                  "order": 1
                },
                "Key": {
                  "type": "string",
                  "title": "Key",
                  "description": "Description",
                  "order": 2
                },
                "ManagedIdentity": {
                  "type": "string",
                  "title": "Managed Indetity",
                  "description": "Managed identity",
                  "order": 3
                },
                "User": {
                  "type": "string",
                  "title": "User",
                  "description": "User",
                  "order": 4
                }
              }
            }
          }
        }
      }
    },
    "SystemData": {
      "type": "object",
      "title": "SystemData",
      "properties": {
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "The timestamp of resource creation (UTC)",
          "format": "date-time",
          "order": 1
        },
        "createdBy": {
          "type": "string",
          "title": "Created By",
          "description": "The identity that created the resource",
          "order": 2
        },
        "createdByType": {
          "$ref": "#/definitions/CreatedByType",
          "title": "Created By Type",
          "description": "The type of identity that created the resource",
          "order": 3
        },
        "lastModifiedAt": {
          "type": "string",
          "title": "Last Modified At",
          "displayType": "date",
          "description": "The timestamp of resource last modification (UTC)",
          "format": "date-time",
          "order": 4
        },
        "lastModifiedBy": {
          "type": "string",
          "title": "Last Modified By",
          "description": "The identity that last modified the resource",
          "order": 5
        },
        "lastModifiedByType": {
          "$ref": "#/definitions/CreatedByType",
          "title": "Last Modified By Type",
          "description": "The type of identity that last modified the resource",
          "order": 6
        }
      },
      "definitions": {
        "CreatedByType": {
          "type": "object",
          "title": "CreatedByType",
          "properties": {
            "Application": {
              "type": "string",
              "title": "Application",
              "description": "Application",
              "order": 1
            },
            "Key": {
              "type": "string",
              "title": "Key",
              "description": "Description",
              "order": 2
            },
            "ManagedIdentity": {
              "type": "string",
              "title": "Managed Indetity",
              "description": "Managed identity",
              "order": 3
            },
            "User": {
              "type": "string",
              "title": "User",
              "description": "User",
              "order": 4
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateUpdateIncidentOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "etag": {
      "type": "string",
      "title": "Etag",
      "description": "Etag",
      "order": 4
    },
    "id": {
      "type": "string",
      "title": "Full Incident ID",
      "description": "Full incident ID",
      "order": 1
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Incident name - short ID",
      "order": 2
    },
    "properties": {
      "$ref": "#/definitions/IncidentProperties",
      "title": "Properties",
      "description": "Incident properties object",
      "order": 5
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Type",
      "order": 3
    }
  },
  "definitions": {
    "CreatedByType": {
      "type": "object",
      "title": "CreatedByType",
      "properties": {
        "Application": {
          "type": "string",
          "title": "Application",
          "description": "Application",
          "order": 1
        },
        "Key": {
          "type": "string",
          "title": "Key",
          "description": "Description",
          "order": 2
        },
        "ManagedIdentity": {
          "type": "string",
          "title": "Managed Indetity",
          "description": "Managed identity",
          "order": 3
        },
        "User": {
          "type": "string",
          "title": "User",
          "description": "User",
          "order": 4
        }
      }
    },
    "IncidentAdditionalData": {
      "type": "object",
      "title": "IncidentAdditionalData",
      "properties": {
        "alertProductNames": {
          "type": "array",
          "title": "Alert Product Names",
          "description": "List of product names of alerts in the incident",
          "items": {
            "type": "string"
          },
          "order": 1
        },
        "alertsCount": {
          "type": "integer",
          "title": "Alert's Count",
          "description": "The number of alerts in the incident",
          "order": 2
        },
        "bookmarksCount": {
          "type": "integer",
          "title": "Bookmarks Count",
          "description": "The number of bookmarks in the incident",
          "order": 3
        },
        "commentsCount": {
          "type": "integer",
          "title": "Comments Count",
          "description": "The number of comments in the incident",
          "order": 4
        },
        "tactics": {
          "type": "array",
          "title": "Tactics",
          "description": "The tactics associated with incident",
          "items": {
            "type": "string"
          },
          "order": 5
        }
      }
    },
    "IncidentLabel": {
      "type": "object",
      "title": "IncidentLabel",
      "properties": {
        "labelName": {
          "type": "string",
          "title": "Label Name",
          "description": "The name of the label",
          "order": 1
        },
        "labelType": {
          "type": "string",
          "title": "The type of label",
          "description": "Label Type",
          "order": 2
        }
      }
    },
    "IncidentOwnerInfo": {
      "type": "object",
      "title": "IncidentOwnerInfo",
      "properties": {
        "assignedTo": {
          "type": "string",
          "title": "Assigned To",
          "description": "The name of the user the incident is assigned to",
          "order": 1
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "The mail of the user the incident is assigned to",
          "order": 2
        },
        "objectId": {
          "type": "string",
          "title": "Object ID",
          "description": "The object id of the user the incident is assigned to",
          "order": 3
        },
        "userPrincipalName": {
          "type": "string",
          "title": "User Principal Name",
          "description": "The user principal name of the user the incident is assigned to",
          "order": 4
        }
      }
    },
    "IncidentProperties": {
      "type": "object",
      "title": "IncidentProperties",
      "properties": {
        "additionalData": {
          "$ref": "#/definitions/IncidentAdditionalData",
          "title": "Additional Data",
          "description": "Additional data on the incident",
          "order": 1
        },
        "classification": {
          "type": "string",
          "title": "Classification",
          "description": "The reason the incident was closed",
          "order": 2
        },
        "classificationComment": {
          "type": "string",
          "title": "Classification Comment",
          "description": "Describes the reason the incident was closed",
          "order": 3
        },
        "classificationReason": {
          "type": "string",
          "title": "Classification Reason",
          "description": "The classification reason the incident was closed with",
          "order": 4
        },
        "createdTimeUtc": {
          "type": "string",
          "title": "Created Time UTC",
          "displayType": "date",
          "description": "The time the incident was created",
          "format": "date-time",
          "order": 5
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "The description of the incident",
          "order": 6
        },
        "etag": {
          "type": "string",
          "title": "Etag",
          "description": "Etag of the azure resource",
          "order": 7
        },
        "firstActivityTimeUtc": {
          "type": "string",
          "title": "First Activity Time UTC",
          "displayType": "date",
          "description": "The time of the first activity in the incident",
          "format": "date-time",
          "order": 8
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Azure resource ID",
          "order": 9
        },
        "incidentNumber": {
          "type": "integer",
          "title": "Incident Number",
          "description": "A sequential number",
          "order": 10
        },
        "incidentUrl": {
          "type": "string",
          "title": "Incident URL",
          "description": "The deep-link URL to the incident in Azure portal",
          "order": 11
        },
        "labels": {
          "type": "array",
          "title": "Labels",
          "description": "List of labels relevant to this incident",
          "items": {
            "$ref": "#/definitions/IncidentLabel"
          },
          "order": 12
        },
        "lastActivityTimeUtc": {
          "type": "string",
          "title": "Last Activity Time UTC",
          "displayType": "date",
          "description": "The time of the last activity in the incident",
          "format": "date-time",
          "order": 13
        },
        "lastModifiedTimeUtc": {
          "type": "string",
          "title": "Last Modified Time UTC",
          "displayType": "date",
          "description": "The last time the incident was updated",
          "format": "date-time",
          "order": 14
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Azure resource name",
          "order": 15
        },
        "owner": {
          "$ref": "#/definitions/IncidentOwnerInfo",
          "title": "Owner",
          "description": "Describes a user that the incident is assigned to",
          "order": 16
        },
        "relatedAnalyticRuleIds": {
          "type": "array",
          "title": "Related Analytic Rule IDs",
          "description": "List of resource ids of Analytic rules related to the incident",
          "items": {
            "type": "string"
          },
          "order": 17
        },
        "severity": {
          "type": "string",
          "title": "Severity",
          "description": "Incidents severity",
          "order": 18
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Incidents status",
          "order": 19
        },
        "systemData": {
          "$ref": "#/definitions/SystemData",
          "title": "System Data",
          "description": "Azure Resource Manager metadata containing createdBy and modifiedBy information",
          "order": 20
        },
        "title": {
          "type": "string",
          "title": "The title of the incident",
          "description": "The title of the incident",
          "order": 21
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Azure resource type",
          "order": 22
        }
      },
      "required": [
        "severity",
        "status"
      ],
      "definitions": {
        "CreatedByType": {
          "type": "object",
          "title": "CreatedByType",
          "properties": {
            "Application": {
              "type": "string",
              "title": "Application",
              "description": "Application",
              "order": 1
            },
            "Key": {
              "type": "string",
              "title": "Key",
              "description": "Description",
              "order": 2
            },
            "ManagedIdentity": {
              "type": "string",
              "title": "Managed Indetity",
              "description": "Managed identity",
              "order": 3
            },
            "User": {
              "type": "string",
              "title": "User",
              "description": "User",
              "order": 4
            }
          }
        },
        "IncidentAdditionalData": {
          "type": "object",
          "title": "IncidentAdditionalData",
          "properties": {
            "alertProductNames": {
              "type": "array",
              "title": "Alert Product Names",
              "description": "List of product names of alerts in the incident",
              "items": {
                "type": "string"
              },
              "order": 1
            },
            "alertsCount": {
              "type": "integer",
              "title": "Alert's Count",
              "description": "The number of alerts in the incident",
              "order": 2
            },
            "bookmarksCount": {
              "type": "integer",
              "title": "Bookmarks Count",
              "description": "The number of bookmarks in the incident",
              "order": 3
            },
            "commentsCount": {
              "type": "integer",
              "title": "Comments Count",
              "description": "The number of comments in the incident",
              "order": 4
            },
            "tactics": {
              "type": "array",
              "title": "Tactics",
              "description": "The tactics associated with incident",
              "items": {
                "type": "string"
              },
              "order": 5
            }
          }
        },
        "IncidentLabel": {
          "type": "object",
          "title": "IncidentLabel",
          "properties": {
            "labelName": {
              "type": "string",
              "title": "Label Name",
              "description": "The name of the label",
              "order": 1
            },
            "labelType": {
              "type": "string",
              "title": "The type of label",
              "description": "Label Type",
              "order": 2
            }
          }
        },
        "IncidentOwnerInfo": {
          "type": "object",
          "title": "IncidentOwnerInfo",
          "properties": {
            "assignedTo": {
              "type": "string",
              "title": "Assigned To",
              "description": "The name of the user the incident is assigned to",
              "order": 1
            },
            "email": {
              "type": "string",
              "title": "Email",
              "description": "The mail of the user the incident is assigned to",
              "order": 2
            },
            "objectId": {
              "type": "string",
              "title": "Object ID",
              "description": "The object id of the user the incident is assigned to",
              "order": 3
            },
            "userPrincipalName": {
              "type": "string",
              "title": "User Principal Name",
              "description": "The user principal name of the user the incident is assigned to",
              "order": 4
            }
          }
        },
        "SystemData": {
          "type": "object",
          "title": "SystemData",
          "properties": {
            "createdAt": {
              "type": "string",
              "title": "Created At",
              "displayType": "date",
              "description": "The timestamp of resource creation (UTC)",
              "format": "date-time",
              "order": 1
            },
            "createdBy": {
              "type": "string",
              "title": "Created By",
              "description": "The identity that created the resource",
              "order": 2
            },
            "createdByType": {
              "$ref": "#/definitions/CreatedByType",
              "title": "Created By Type",
              "description": "The type of identity that created the resource",
              "order": 3
            },
            "lastModifiedAt": {
              "type": "string",
              "title": "Last Modified At",
              "displayType": "date",
              "description": "The timestamp of resource last modification (UTC)",
              "format": "date-time",
              "order": 4
            },
            "lastModifiedBy": {
              "type": "string",
              "title": "Last Modified By",
              "description": "The identity that last modified the resource",
              "order": 5
            },
            "lastModifiedByType": {
              "$ref": "#/definitions/CreatedByType",
              "title": "Last Modified By Type",
              "description": "The type of identity that last modified the resource",
              "order": 6
            }
          },
          "definitions": {
            "CreatedByType": {
              "type": "object",
              "title": "CreatedByType",
              "properties": {
                "Application": {
                  "type": "string",
                  "title": "Application",
                  "description": "Application",
                  "order": 1
                },
                "Key": {
                  "type": "string",
                  "title": "Key",
                  "description": "Description",
                  "order": 2
                },
                "ManagedIdentity": {
                  "type": "string",
                  "title": "Managed Indetity",
                  "description": "Managed identity",
                  "order": 3
                },
                "User": {
                  "type": "string",
                  "title": "User",
                  "description": "User",
                  "order": 4
                }
              }
            }
          }
        }
      }
    },
    "SystemData": {
      "type": "object",
      "title": "SystemData",
      "properties": {
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "The timestamp of resource creation (UTC)",
          "format": "date-time",
          "order": 1
        },
        "createdBy": {
          "type": "string",
          "title": "Created By",
          "description": "The identity that created the resource",
          "order": 2
        },
        "createdByType": {
          "$ref": "#/definitions/CreatedByType",
          "title": "Created By Type",
          "description": "The type of identity that created the resource",
          "order": 3
        },
        "lastModifiedAt": {
          "type": "string",
          "title": "Last Modified At",
          "displayType": "date",
          "description": "The timestamp of resource last modification (UTC)",
          "format": "date-time",
          "order": 4
        },
        "lastModifiedBy": {
          "type": "string",
          "title": "Last Modified By",
          "description": "The identity that last modified the resource",
          "order": 5
        },
        "lastModifiedByType": {
          "$ref": "#/definitions/CreatedByType",
          "title": "Last Modified By Type",
          "description": "The type of identity that last modified the resource",
          "order": 6
        }
      },
      "definitions": {
        "CreatedByType": {
          "type": "object",
          "title": "CreatedByType",
          "properties": {
            "Application": {
              "type": "string",
              "title": "Application",
              "description": "Application",
              "order": 1
            },
            "Key": {
              "type": "string",
              "title": "Key",
              "description": "Description",
              "order": 2
            },
            "ManagedIdentity": {
              "type": "string",
              "title": "Managed Indetity",
              "description": "Managed identity",
              "order": 3
            },
            "User": {
              "type": "string",
              "title": "User",
              "description": "User",
              "order": 4
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
