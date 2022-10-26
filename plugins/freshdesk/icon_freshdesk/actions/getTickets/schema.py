# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get tickets list"


class Input:
    FILTERBY = "filterBy"
    INCLUDE = "include"
    ORDERBY = "orderBy"
    ORDERTYPE = "orderType"
    PAGE = "page"
    PERPAGE = "perPage"
    PREDEFINEDFILTER = "predefinedFilter"
    

class Output:
    TICKETS = "tickets"
    

class GetTicketsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "filterBy": {
      "$ref": "#/definitions/ticketsFilter",
      "title": "Filter By",
      "description": "Filter tickets by a specific fields",
      "order": 3
    },
    "include": {
      "type": "string",
      "title": "Include",
      "description": "Include additional ticket informations",
      "enum": [
        "requester",
        "company",
        "stats",
        "None"
      ],
      "order": 2
    },
    "orderBy": {
      "type": "string",
      "title": "Order By",
      "description": "Order tickets by specific field",
      "enum": [
        "created_at",
        "due_by",
        "updated_at",
        "status"
      ],
      "order": 4
    },
    "orderType": {
      "type": "string",
      "title": "Order Type",
      "description": "Type of the order",
      "enum": [
        "asc",
        "desc"
      ],
      "order": 5
    },
    "page": {
      "type": "integer",
      "title": "Page",
      "description": "Page number",
      "order": 7
    },
    "perPage": {
      "type": "integer",
      "title": "Per Page",
      "description": "Results per page. Less or equal to 100",
      "order": 6
    },
    "predefinedFilter": {
      "type": "string",
      "title": "Predefined Filter",
      "description": "The various filters available are new_and_my_open, watching, spam, deleted",
      "order": 1
    }
  },
  "definitions": {
    "ticketsFilter": {
      "type": "object",
      "title": "ticketsFilter",
      "properties": {
        "companyId": {
          "type": "integer",
          "title": "Company ID",
          "description": "Company ID of the requester",
          "order": 4
        },
        "email": {
          "type": "string",
          "title": "Requester Email",
          "description": "Email of the requester",
          "order": 2
        },
        "requesterId": {
          "type": "integer",
          "title": "Requester ID",
          "description": "ID of the requester",
          "order": 1
        },
        "uniqueExternalId": {
          "type": "string",
          "title": "Requester Unique External ID",
          "description": "External ID of the requester",
          "order": 3
        },
        "updatedSince": {
          "type": "string",
          "title": "Updated Since",
          "displayType": "date",
          "description": "Tickets updated since specified date",
          "format": "date-time",
          "order": 5
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetTicketsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "tickets": {
      "type": "array",
      "title": "Tickets",
      "description": "List of tickets",
      "items": {
        "$ref": "#/definitions/ticket"
      },
      "order": 1
    }
  },
  "required": [
    "tickets"
  ],
  "definitions": {
    "attachmentOutput": {
      "type": "object",
      "title": "attachmentOutput",
      "properties": {
        "attachmentUrl": {
          "type": "string",
          "title": "Attachment URL",
          "description": "URL of the attachment",
          "order": 2
        },
        "contentType": {
          "type": "string",
          "title": "Content Type",
          "description": "Content type of the attachment",
          "order": 3
        },
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "description": "Date of the attachment creation",
          "order": 4
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID of the attachment",
          "order": 6
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Attachment name",
          "order": 1
        },
        "size": {
          "type": "integer",
          "title": "Size",
          "description": "Size of the attachment",
          "order": 7
        },
        "updatedAt": {
          "type": "string",
          "title": "Updated At",
          "description": "Date of the attachment update",
          "order": 5
        }
      }
    },
    "company": {
      "type": "object",
      "title": "company",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Company ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Company name",
          "order": 2
        }
      }
    },
    "conversation": {
      "type": "object",
      "title": "conversation",
      "properties": {
        "attachments": {
          "type": "array",
          "title": "Attachments",
          "description": "Conversation attachments",
          "items": {
            "$ref": "#/definitions/attachmentOutput"
          },
          "order": 19
        },
        "autoResponse": {
          "type": "boolean",
          "title": "Auto Response",
          "description": "Auto response",
          "order": 22
        },
        "automationId": {
          "type": "integer",
          "title": "Automation ID",
          "description": "Automation ID",
          "order": 20
        },
        "automationTypeId": {
          "type": "integer",
          "title": "Automation Type ID",
          "description": "Automation type ID",
          "order": 21
        },
        "bccEmails": {
          "type": "array",
          "title": "BCC Emails",
          "description": "BCC emails",
          "items": {
            "type": "string"
          },
          "order": 11
        },
        "body": {
          "type": "string",
          "title": "Body",
          "description": "Conversation body",
          "order": 1
        },
        "body_text": {
          "type": "string",
          "title": "Body Text",
          "description": "Conversation body text",
          "order": 2
        },
        "ccEmails": {
          "type": "array",
          "title": "CC Emails",
          "description": "CC emails",
          "items": {
            "type": "string"
          },
          "order": 10
        },
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "description": "Date of the conversation creation",
          "order": 15
        },
        "emailFailureCount": {
          "type": "integer",
          "title": "Email Failure Count",
          "description": "Email failure count",
          "order": 12
        },
        "fromEmail": {
          "type": "string",
          "title": "From Email",
          "description": "From email",
          "order": 9
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Conversation ID",
          "order": 3
        },
        "incoming": {
          "type": "boolean",
          "title": "Incoming",
          "description": "Incoming conversation",
          "order": 4
        },
        "lastEditedAt": {
          "type": "string",
          "title": "Last Edited At",
          "description": "Date of the last conversation edit",
          "order": 17
        },
        "lastEditedUserId": {
          "type": "integer",
          "title": "Last Edited User ID",
          "description": "Last edited user ID",
          "order": 18
        },
        "private": {
          "type": "boolean",
          "title": "Private",
          "description": "Private conversation",
          "order": 5
        },
        "supportEmail": {
          "type": "string",
          "title": "Support Email",
          "description": "Support email",
          "order": 7
        },
        "threadId": {
          "type": "integer",
          "title": "Thread ID",
          "description": "Thread ID",
          "order": 13
        },
        "threadMessageId": {
          "type": "integer",
          "title": "Thread Message ID",
          "description": "Thread message ID",
          "order": 14
        },
        "ticketId": {
          "type": "integer",
          "title": "Ticket ID",
          "description": "Ticket ID",
          "order": 23
        },
        "toEmails": {
          "type": "array",
          "title": "To Emails",
          "description": "To emails",
          "items": {
            "type": "string"
          },
          "order": 8
        },
        "updatedAt": {
          "type": "string",
          "title": "Updated At",
          "description": "Date of the conversation update",
          "order": 16
        },
        "userId": {
          "type": "integer",
          "title": "User ID",
          "description": "Conversation user ID",
          "order": 6
        }
      },
      "definitions": {
        "attachmentOutput": {
          "type": "object",
          "title": "attachmentOutput",
          "properties": {
            "attachmentUrl": {
              "type": "string",
              "title": "Attachment URL",
              "description": "URL of the attachment",
              "order": 2
            },
            "contentType": {
              "type": "string",
              "title": "Content Type",
              "description": "Content type of the attachment",
              "order": 3
            },
            "createdAt": {
              "type": "string",
              "title": "Created At",
              "description": "Date of the attachment creation",
              "order": 4
            },
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID of the attachment",
              "order": 6
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Attachment name",
              "order": 1
            },
            "size": {
              "type": "integer",
              "title": "Size",
              "description": "Size of the attachment",
              "order": 7
            },
            "updatedAt": {
              "type": "string",
              "title": "Updated At",
              "description": "Date of the attachment update",
              "order": 5
            }
          }
        }
      }
    },
    "requester": {
      "type": "object",
      "title": "requester",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Requester email",
          "order": 3
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Requester ID",
          "order": 1
        },
        "mobile": {
          "type": "string",
          "title": "Mobile",
          "description": "Requester mobile",
          "order": 4
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Requester name",
          "order": 2
        },
        "phone": {
          "type": "string",
          "title": "Phone",
          "description": "Requester phone",
          "order": 5
        }
      }
    },
    "stats": {
      "type": "object",
      "title": "stats",
      "properties": {
        "agentRespondedAt": {
          "type": "string",
          "title": "Agent Responded At",
          "description": "Agent responded at",
          "order": 1
        },
        "closedAt": {
          "type": "string",
          "title": "Closed At",
          "description": "Closed at",
          "order": 7
        },
        "firstRespondedAt": {
          "type": "string",
          "title": "First Responded At",
          "description": "First responded at",
          "order": 3
        },
        "pendingSince": {
          "type": "string",
          "title": "Pending Since",
          "description": "Pending since",
          "order": 8
        },
        "reopeneddAt": {
          "type": "string",
          "title": "Reopened At",
          "description": "Reopened at",
          "order": 5
        },
        "requesterRespondedAt": {
          "type": "string",
          "title": "Requester Responded At",
          "description": "Requester responded at",
          "order": 2
        },
        "resolvedAt": {
          "type": "string",
          "title": "Resolved At",
          "description": "Resolved at",
          "order": 6
        },
        "statusUpdatedAt": {
          "type": "string",
          "title": "Status Updated At",
          "description": "Status updated at",
          "order": 4
        }
      }
    },
    "ticket": {
      "type": "object",
      "title": "ticket",
      "properties": {
        "attachments": {
          "type": "array",
          "title": "Attachments",
          "description": "Ticket attachments. The total size of these attachments cannot exceed 20MB",
          "items": {
            "$ref": "#/definitions/attachmentOutput"
          },
          "order": 12
        },
        "ccEmails": {
          "type": "array",
          "title": "CC Emails",
          "description": "Email address added in the 'CC' field of the incoming ticket email",
          "items": {
            "type": "string"
          },
          "order": 13
        },
        "company": {
          "$ref": "#/definitions/company",
          "title": "Company",
          "description": "Company details",
          "order": 28
        },
        "companyId": {
          "type": "integer",
          "title": "Company ID",
          "description": "Company ID of the requester",
          "order": 22
        },
        "conversations": {
          "type": "array",
          "title": "Conversations",
          "description": "Ticket conversations",
          "items": {
            "$ref": "#/definitions/conversation"
          },
          "order": 30
        },
        "customFields": {
          "type": "object",
          "title": "Custom Fields",
          "description": "Key value pairs containing the names and values of custom fields. Read more at https://support.freshdesk.com/support/solutions/articles/216548",
          "order": 14
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "HTML content of the ticket",
          "order": 11
        },
        "dueBy": {
          "type": "string",
          "title": "Due By",
          "description": "Timestamp that denotes when the ticket is due to be resolved",
          "order": 15
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Email address of the requester",
          "order": 3
        },
        "emailConfigId": {
          "type": "integer",
          "title": "Email Config ID",
          "description": "ID of email config which is used for this ticket",
          "order": 16
        },
        "frDueBy": {
          "type": "string",
          "title": "First Response Due By",
          "displayType": "date",
          "description": "Timestamp that denotes when the first response is due",
          "format": "date-time",
          "order": 17
        },
        "groupId": {
          "type": "integer",
          "title": "Group ID",
          "description": "ID of the group to which the ticket has been assigned",
          "order": 18
        },
        "internalAgentId": {
          "type": "integer",
          "title": "Internal Agent ID",
          "description": "ID of the internal agent which the ticket should be assigned with",
          "order": 23
        },
        "internalGroupId": {
          "type": "integer",
          "title": "Internal Group ID",
          "description": "ID of the internal group to which the ticket should be assigned with",
          "order": 24
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the requester",
          "order": 1
        },
        "parentId": {
          "type": "integer",
          "title": "Parent ID",
          "description": "ID of the parent ticket under which the child ticket needs to be created",
          "order": 26
        },
        "phone": {
          "type": "string",
          "title": "Phone",
          "description": "Phone number of the requester",
          "order": 4
        },
        "priority": {
          "type": "string",
          "title": "Priority",
          "description": "Priority of the ticket",
          "order": 10
        },
        "productId": {
          "type": "integer",
          "title": "Product ID",
          "description": "ID of the product to which the ticket is associated",
          "order": 19
        },
        "relatedTicketIds": {
          "type": "array",
          "title": "Related Ticket IDs",
          "description": "List of Ticket IDs which needs to be linked to the Tracker being created",
          "items": {
            "type": "integer"
          },
          "order": 25
        },
        "requester": {
          "$ref": "#/definitions/requester",
          "title": "Requester",
          "description": "Requester details",
          "order": 29
        },
        "requesterId": {
          "type": "integer",
          "title": "Requester ID",
          "description": "User ID of the requester",
          "order": 2
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "The channel through which the ticket was created",
          "order": 20
        },
        "stats": {
          "$ref": "#/definitions/stats",
          "title": "Stats",
          "description": "Ticket stats",
          "order": 27
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status of the ticket",
          "order": 9
        },
        "subject": {
          "type": "string",
          "title": "Subject",
          "description": "Subject of the ticket",
          "order": 7
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Tags that have been associated with the ticket",
          "items": {
            "type": "string"
          },
          "order": 21
        },
        "twitterId": {
          "type": "string",
          "title": "Twitter ID",
          "description": "Twitter handle of the requester",
          "order": 5
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Helps categorize the ticket according to the different kinds of issues your support team deals with",
          "order": 8
        },
        "uniqueExternalId": {
          "type": "string",
          "title": "Unique External ID",
          "description": "External ID of the requester",
          "order": 6
        }
      },
      "definitions": {
        "attachmentOutput": {
          "type": "object",
          "title": "attachmentOutput",
          "properties": {
            "attachmentUrl": {
              "type": "string",
              "title": "Attachment URL",
              "description": "URL of the attachment",
              "order": 2
            },
            "contentType": {
              "type": "string",
              "title": "Content Type",
              "description": "Content type of the attachment",
              "order": 3
            },
            "createdAt": {
              "type": "string",
              "title": "Created At",
              "description": "Date of the attachment creation",
              "order": 4
            },
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID of the attachment",
              "order": 6
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Attachment name",
              "order": 1
            },
            "size": {
              "type": "integer",
              "title": "Size",
              "description": "Size of the attachment",
              "order": 7
            },
            "updatedAt": {
              "type": "string",
              "title": "Updated At",
              "description": "Date of the attachment update",
              "order": 5
            }
          }
        },
        "company": {
          "type": "object",
          "title": "company",
          "properties": {
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "Company ID",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Company name",
              "order": 2
            }
          }
        },
        "conversation": {
          "type": "object",
          "title": "conversation",
          "properties": {
            "attachments": {
              "type": "array",
              "title": "Attachments",
              "description": "Conversation attachments",
              "items": {
                "$ref": "#/definitions/attachmentOutput"
              },
              "order": 19
            },
            "autoResponse": {
              "type": "boolean",
              "title": "Auto Response",
              "description": "Auto response",
              "order": 22
            },
            "automationId": {
              "type": "integer",
              "title": "Automation ID",
              "description": "Automation ID",
              "order": 20
            },
            "automationTypeId": {
              "type": "integer",
              "title": "Automation Type ID",
              "description": "Automation type ID",
              "order": 21
            },
            "bccEmails": {
              "type": "array",
              "title": "BCC Emails",
              "description": "BCC emails",
              "items": {
                "type": "string"
              },
              "order": 11
            },
            "body": {
              "type": "string",
              "title": "Body",
              "description": "Conversation body",
              "order": 1
            },
            "body_text": {
              "type": "string",
              "title": "Body Text",
              "description": "Conversation body text",
              "order": 2
            },
            "ccEmails": {
              "type": "array",
              "title": "CC Emails",
              "description": "CC emails",
              "items": {
                "type": "string"
              },
              "order": 10
            },
            "createdAt": {
              "type": "string",
              "title": "Created At",
              "description": "Date of the conversation creation",
              "order": 15
            },
            "emailFailureCount": {
              "type": "integer",
              "title": "Email Failure Count",
              "description": "Email failure count",
              "order": 12
            },
            "fromEmail": {
              "type": "string",
              "title": "From Email",
              "description": "From email",
              "order": 9
            },
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "Conversation ID",
              "order": 3
            },
            "incoming": {
              "type": "boolean",
              "title": "Incoming",
              "description": "Incoming conversation",
              "order": 4
            },
            "lastEditedAt": {
              "type": "string",
              "title": "Last Edited At",
              "description": "Date of the last conversation edit",
              "order": 17
            },
            "lastEditedUserId": {
              "type": "integer",
              "title": "Last Edited User ID",
              "description": "Last edited user ID",
              "order": 18
            },
            "private": {
              "type": "boolean",
              "title": "Private",
              "description": "Private conversation",
              "order": 5
            },
            "supportEmail": {
              "type": "string",
              "title": "Support Email",
              "description": "Support email",
              "order": 7
            },
            "threadId": {
              "type": "integer",
              "title": "Thread ID",
              "description": "Thread ID",
              "order": 13
            },
            "threadMessageId": {
              "type": "integer",
              "title": "Thread Message ID",
              "description": "Thread message ID",
              "order": 14
            },
            "ticketId": {
              "type": "integer",
              "title": "Ticket ID",
              "description": "Ticket ID",
              "order": 23
            },
            "toEmails": {
              "type": "array",
              "title": "To Emails",
              "description": "To emails",
              "items": {
                "type": "string"
              },
              "order": 8
            },
            "updatedAt": {
              "type": "string",
              "title": "Updated At",
              "description": "Date of the conversation update",
              "order": 16
            },
            "userId": {
              "type": "integer",
              "title": "User ID",
              "description": "Conversation user ID",
              "order": 6
            }
          },
          "definitions": {
            "attachmentOutput": {
              "type": "object",
              "title": "attachmentOutput",
              "properties": {
                "attachmentUrl": {
                  "type": "string",
                  "title": "Attachment URL",
                  "description": "URL of the attachment",
                  "order": 2
                },
                "contentType": {
                  "type": "string",
                  "title": "Content Type",
                  "description": "Content type of the attachment",
                  "order": 3
                },
                "createdAt": {
                  "type": "string",
                  "title": "Created At",
                  "description": "Date of the attachment creation",
                  "order": 4
                },
                "id": {
                  "type": "integer",
                  "title": "ID",
                  "description": "ID of the attachment",
                  "order": 6
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Attachment name",
                  "order": 1
                },
                "size": {
                  "type": "integer",
                  "title": "Size",
                  "description": "Size of the attachment",
                  "order": 7
                },
                "updatedAt": {
                  "type": "string",
                  "title": "Updated At",
                  "description": "Date of the attachment update",
                  "order": 5
                }
              }
            }
          }
        },
        "requester": {
          "type": "object",
          "title": "requester",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "description": "Requester email",
              "order": 3
            },
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "Requester ID",
              "order": 1
            },
            "mobile": {
              "type": "string",
              "title": "Mobile",
              "description": "Requester mobile",
              "order": 4
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Requester name",
              "order": 2
            },
            "phone": {
              "type": "string",
              "title": "Phone",
              "description": "Requester phone",
              "order": 5
            }
          }
        },
        "stats": {
          "type": "object",
          "title": "stats",
          "properties": {
            "agentRespondedAt": {
              "type": "string",
              "title": "Agent Responded At",
              "description": "Agent responded at",
              "order": 1
            },
            "closedAt": {
              "type": "string",
              "title": "Closed At",
              "description": "Closed at",
              "order": 7
            },
            "firstRespondedAt": {
              "type": "string",
              "title": "First Responded At",
              "description": "First responded at",
              "order": 3
            },
            "pendingSince": {
              "type": "string",
              "title": "Pending Since",
              "description": "Pending since",
              "order": 8
            },
            "reopeneddAt": {
              "type": "string",
              "title": "Reopened At",
              "description": "Reopened at",
              "order": 5
            },
            "requesterRespondedAt": {
              "type": "string",
              "title": "Requester Responded At",
              "description": "Requester responded at",
              "order": 2
            },
            "resolvedAt": {
              "type": "string",
              "title": "Resolved At",
              "description": "Resolved at",
              "order": 6
            },
            "statusUpdatedAt": {
              "type": "string",
              "title": "Status Updated At",
              "description": "Status updated at",
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
