# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get a list of tickets"


class Input:
    CONDITIONS = "conditions"
    PAGE = "page"
    PAGESIZE = "pageSize"
    

class Output:
    TICKETS = "tickets"
    

class GetTicketsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "conditions": {
      "type": "string",
      "title": "Conditions",
      "description": "Search results based on the provided fields. Supported operators are =, !=, \\u003c, \\u003c=, \\u003e, \\u003e=, contains, like, in, not",
      "order": 1
    },
    "page": {
      "type": "integer",
      "title": "Page",
      "description": "Number of the page",
      "order": 2
    },
    "pageSize": {
      "type": "integer",
      "title": "Page Size",
      "description": "Number of results returned per page (Defaults to 25)",
      "order": 3
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
      "description": "Results containing information about tickets",
      "items": {
        "$ref": "#/definitions/ticket"
      },
      "order": 1
    }
  },
  "definitions": {
    "agreement_details": {
      "type": "object",
      "title": "agreement_details",
      "properties": {
        "_info": {
          "type": "object",
          "title": "Info",
          "description": "Additional information",
          "order": 4
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 3
        }
      }
    },
    "currency_details": {
      "type": "object",
      "title": "currency_details",
      "properties": {
        "_info": {
          "type": "object",
          "title": "Info",
          "description": "Additional information",
          "order": 12
        },
        "currencyCode": {
          "type": "string",
          "title": "Currency Code",
          "description": "Currency code",
          "order": 3
        },
        "currencyIdentifier": {
          "type": "string",
          "title": "Currency Identifier",
          "description": "Currency identifier",
          "order": 8
        },
        "displayIdFlag": {
          "type": "boolean",
          "title": "Display ID Flag",
          "description": "Display ID flag",
          "order": 9
        },
        "displaySymbolFlag": {
          "type": "boolean",
          "title": "Display Symbol Flag",
          "description": "Display symbol flag",
          "order": 7
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 11
        },
        "negativeParenthesesFlag": {
          "type": "boolean",
          "title": "Negative Parentheses Flag",
          "description": "Negative parentheses flag",
          "order": 6
        },
        "numberOfDecimals": {
          "type": "integer",
          "title": "Number Of Decimals",
          "description": "Number of decimals",
          "order": 4
        },
        "rightAlign": {
          "type": "boolean",
          "title": "Right Align",
          "description": "Right align",
          "order": 10
        },
        "symbol": {
          "type": "string",
          "title": "Symbol",
          "description": "Symbol",
          "order": 2
        },
        "thousandsSeparator": {
          "type": "string",
          "title": "Thousands Separator",
          "description": "Thousands Separator",
          "order": 5
        }
      }
    },
    "details": {
      "type": "object",
      "title": "details",
      "properties": {
        "_info": {
          "type": "object",
          "title": "Info",
          "description": "Additional information",
          "order": 3
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        }
      }
    },
    "merged_parent_ticket_details": {
      "type": "object",
      "title": "merged_parent_ticket_details",
      "properties": {
        "_info": {
          "type": "object",
          "title": "Info",
          "description": "Additional information",
          "order": 3
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "summary": {
          "type": "string",
          "title": "Summary",
          "description": "Summary",
          "order": 2
        }
      }
    },
    "more_details": {
      "type": "object",
      "title": "more_details",
      "properties": {
        "_info": {
          "type": "object",
          "title": "Info",
          "description": "Additional information",
          "order": 4
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "identifier": {
          "type": "string",
          "title": "Identifier",
          "description": "Identifier",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 3
        }
      }
    },
    "ticket": {
      "type": "object",
      "title": "ticket",
      "properties": {
        "_info": {
          "type": "object",
          "title": "Info",
          "description": "Info",
          "order": 100
        },
        "actualHours": {
          "type": "number",
          "title": "Actual Hours",
          "description": "Actual hours",
          "order": 55
        },
        "addressLine1": {
          "type": "string",
          "title": "Address Line",
          "description": "First line of the address",
          "order": 11
        },
        "addressLine2": {
          "type": "string",
          "title": "Second Address Line",
          "description": "Second line of the address",
          "order": 12
        },
        "agreement": {
          "$ref": "#/definitions/agreement_details",
          "title": "Agreement",
          "description": "Agreement",
          "order": 33
        },
        "allowAllClientPortalView": {
          "type": "boolean",
          "title": "Allow All Client Portal View",
          "description": "Allow all client portal view",
          "order": 39
        },
        "approved": {
          "type": "boolean",
          "title": "Approved",
          "description": "Approved",
          "order": 56
        },
        "automaticEmailCc": {
          "type": "string",
          "title": "Automatic Email CC",
          "description": "Automatic email CC",
          "order": 44
        },
        "automaticEmailCcFlag": {
          "type": "boolean",
          "title": "Automatic Email CC Flag",
          "description": "Automatic email CC flag",
          "order": 43
        },
        "automaticEmailContactFlag": {
          "type": "boolean",
          "title": "Automatic Email Contact Flag",
          "description": "Automatic email contact flag",
          "order": 41
        },
        "automaticEmailResourceFlag": {
          "type": "boolean",
          "title": "Automatic Email Resource Flag",
          "description": "Automatic email resource flag",
          "order": 42
        },
        "billExpenses": {
          "type": "string",
          "title": "Bill Expenses",
          "description": "Bill expenses",
          "order": 83
        },
        "billProducts": {
          "type": "string",
          "title": "Bill Products",
          "description": "Bill products",
          "order": 84
        },
        "billTime": {
          "type": "string",
          "title": "Bill Time",
          "description": "Bill time",
          "order": 82
        },
        "billingAmount": {
          "type": "number",
          "title": "Billing Amount",
          "description": "Billing amount",
          "order": 64
        },
        "billingMethod": {
          "type": "string",
          "title": "Billing Method",
          "description": "Billing method",
          "order": 63
        },
        "board": {
          "$ref": "#/definitions/details",
          "title": "Board",
          "description": "Board",
          "order": 4
        },
        "budgetHours": {
          "type": "number",
          "title": "Budget Hours",
          "description": "Budget hours",
          "order": 31
        },
        "city": {
          "type": "string",
          "title": "City",
          "description": "City",
          "order": 13
        },
        "closedBy": {
          "type": "string",
          "title": "Closed By",
          "description": "Closed by",
          "order": 53
        },
        "closedDate": {
          "type": "string",
          "title": "Closed Date",
          "description": "Closed date",
          "order": 52
        },
        "closedFlag": {
          "type": "boolean",
          "title": "Closed Flag",
          "description": "Closed flag",
          "order": 54
        },
        "company": {
          "$ref": "#/definitions/more_details",
          "title": "Company",
          "description": "Company",
          "order": 8
        },
        "contact": {
          "$ref": "#/definitions/details",
          "title": "Contact",
          "description": "Contact",
          "order": 17
        },
        "contactEmailAddress": {
          "type": "string",
          "title": "Contact Email Address",
          "description": "Contact email address",
          "order": 21
        },
        "contactEmailLookup": {
          "type": "string",
          "title": "Contact Email Lookup",
          "description": "Contact Email Lookup",
          "order": 49
        },
        "contactName": {
          "type": "string",
          "title": "Contact Name",
          "description": "Contact name",
          "order": 18
        },
        "contactPhoneExtension": {
          "type": "string",
          "title": "Contact Phone Extension",
          "description": "Contact phone extension",
          "order": 20
        },
        "contactPhoneNumber": {
          "type": "string",
          "title": "Contact Phone Number",
          "description": "Contact phone number",
          "order": 19
        },
        "country": {
          "$ref": "#/definitions/more_details",
          "title": "Country",
          "description": "Country",
          "order": 16
        },
        "currency": {
          "$ref": "#/definitions/currency_details",
          "title": "Currency",
          "description": "Currency",
          "order": 97
        },
        "customFields": {
          "type": "array",
          "title": "Custom Fields",
          "description": "Custom fields",
          "items": {
            "type": "object"
          },
          "order": 101
        },
        "customerUpdateFlag": {
          "type": "boolean",
          "title": "Customer Update Flag",
          "description": "Customer update flag",
          "order": 40
        },
        "dateResolved": {
          "type": "string",
          "title": "Date Resolved",
          "description": "Date resolved",
          "order": 69
        },
        "dateResplan": {
          "type": "string",
          "title": "Date Resplan",
          "description": "Date resplan",
          "order": 70
        },
        "dateResponded": {
          "type": "string",
          "title": "Date Responded",
          "description": "Date responded",
          "order": 71
        },
        "department": {
          "$ref": "#/definitions/more_details",
          "title": "Department",
          "description": "Department",
          "order": 93
        },
        "duration": {
          "type": "integer",
          "title": "Duration",
          "description": "Duration",
          "order": 91
        },
        "estimatedExpenseCost": {
          "type": "number",
          "title": "Estimated Expense Cost",
          "description": "Estimated expense cost",
          "order": 57
        },
        "estimatedExpenseRevenue": {
          "type": "number",
          "title": "Estimated Expense Revenue",
          "description": "Estimated expense revenue",
          "order": 58
        },
        "estimatedProductCost": {
          "type": "number",
          "title": "Estimated Product Cost",
          "description": "Estimated product cost",
          "order": 59
        },
        "estimatedProductRevenue": {
          "type": "number",
          "title": "Estimated Product Revenue",
          "description": "Estimated product revenue",
          "order": 60
        },
        "estimatedStartDate": {
          "type": "string",
          "title": "Estimated Start Date",
          "description": "Estimated start date",
          "order": 90
        },
        "estimatedTimeCost": {
          "type": "number",
          "title": "Estimated Time Cost",
          "description": "Estimated time cost",
          "order": 61
        },
        "estimatedTimeRevenue": {
          "type": "number",
          "title": "Estimated Time Revenue",
          "description": "Estimated time revenue",
          "order": 62
        },
        "externalXRef": {
          "type": "string",
          "title": "External Reference",
          "description": "External reference",
          "order": 36
        },
        "hasChildTicket": {
          "type": "boolean",
          "title": "Has Child Ticket",
          "description": "Has child ticket",
          "order": 79
        },
        "hasMergedChildTicketFlag": {
          "type": "boolean",
          "title": "Has Merged Child Ticket Flag",
          "description": "Has merged child ticket flag",
          "order": 80
        },
        "hourlyRate": {
          "type": "number",
          "title": "Hourly Rate",
          "description": "Hourly rate",
          "order": 65
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Ticket ID",
          "order": 1
        },
        "impact": {
          "type": "string",
          "title": "Impact",
          "description": "Impact",
          "order": 35
        },
        "initialDescription": {
          "type": "string",
          "title": "Initial Description",
          "description": "Initial description",
          "order": 45
        },
        "initialDescriptionFrom": {
          "type": "string",
          "title": "Initial Description From",
          "description": "Initial description from",
          "order": 48
        },
        "initialInternalAnalysis": {
          "type": "string",
          "title": "Initial Internal Analysis",
          "description": "Initial internal analysis",
          "order": 46
        },
        "initialResolution": {
          "type": "string",
          "title": "Initial Resolution",
          "description": "Initial resolution",
          "order": 47
        },
        "integratorTags": {
          "type": "array",
          "title": "Integrator Tags",
          "description": "Integrator tags",
          "items": {
            "type": "string"
          },
          "order": 99
        },
        "isInSla": {
          "type": "boolean",
          "title": "Is In SLA",
          "description": "Is in SLA",
          "order": 75
        },
        "item": {
          "$ref": "#/definitions/details",
          "title": "Item",
          "description": "Item",
          "order": 24
        },
        "knowledgeBaseCategoryId": {
          "type": "integer",
          "title": "Knowledge Base Category ID",
          "description": "Knowledge base category ID",
          "order": 37
        },
        "knowledgeBaseLinkId": {
          "type": "integer",
          "title": "Knowledge Base Link ID",
          "description": "Knowledge base link ID",
          "order": 76
        },
        "knowledgeBaseLinkType": {
          "type": "string",
          "title": "Knowledge Base Link Type",
          "description": "Knowledge base link type",
          "order": 81
        },
        "knowledgeBaseSubCategoryId": {
          "type": "integer",
          "title": "Knowledge Base Subcategory ID",
          "description": "Knowledge base subcategory ID",
          "order": 38
        },
        "lagDays": {
          "type": "integer",
          "title": "Lag Days",
          "description": "Lag days",
          "order": 88
        },
        "lagNonworkingDaysFlag": {
          "type": "boolean",
          "title": "Lag Non Working Days Flag",
          "description": "Lag non working days flag",
          "order": 89
        },
        "location": {
          "$ref": "#/definitions/details",
          "title": "Location",
          "description": "Location",
          "order": 92
        },
        "mergedParentTicket": {
          "$ref": "#/definitions/merged_parent_ticket_details",
          "title": "Merged Parent Ticket",
          "description": "Merget parent ticket",
          "order": 98
        },
        "mobileGuid": {
          "type": "string",
          "title": "Mobile GUID",
          "description": "Mobile GUID",
          "order": 94
        },
        "opportunity": {
          "$ref": "#/definitions/details",
          "title": "Opportunity",
          "description": "Opportunity",
          "order": 32
        },
        "owner": {
          "$ref": "#/definitions/more_details",
          "title": "Owner",
          "description": "Owner",
          "order": 26
        },
        "parentTicketId": {
          "type": "integer",
          "title": "Parent Ticket ID",
          "description": "Parent ticket ID",
          "order": 78
        },
        "predecessorClosedFlag": {
          "type": "boolean",
          "title": "Predecessor Closed Flag",
          "description": "Predecessor closed flag",
          "order": 87
        },
        "predecessorId": {
          "type": "integer",
          "title": "Predecessor ID",
          "description": "Predecessor ID",
          "order": 86
        },
        "predecessorType": {
          "type": "string",
          "title": "Predecessor Type",
          "description": "Predecessor type",
          "order": 85
        },
        "priority": {
          "$ref": "#/definitions/details",
          "title": "Priority",
          "description": "Priority",
          "order": 27
        },
        "processNotifications": {
          "type": "boolean",
          "title": "Process Notifications",
          "description": "Process notifications",
          "order": 50
        },
        "recordType": {
          "type": "string",
          "title": "Record Type",
          "description": "Type of the record",
          "order": 3
        },
        "requiredDate": {
          "type": "string",
          "title": "Required Date",
          "description": "Required date",
          "order": 30
        },
        "resPlanMinutes": {
          "type": "integer",
          "title": "Resolve Plan Minutes",
          "description": "Resolve plan minutes",
          "order": 73
        },
        "resolveMinutes": {
          "type": "integer",
          "title": "Resolve Minutes",
          "description": "Resolve minutes",
          "order": 72
        },
        "resources": {
          "type": "string",
          "title": "Resources",
          "description": "Resources",
          "order": 77
        },
        "respondMinutes": {
          "type": "integer",
          "title": "Respond Minutes",
          "description": "Respond minutes",
          "order": 74
        },
        "serviceLocation": {
          "$ref": "#/definitions/details",
          "title": "Service Location",
          "description": "Service location",
          "order": 28
        },
        "severity": {
          "type": "string",
          "title": "Severity",
          "description": "Severity",
          "order": 34
        },
        "site": {
          "$ref": "#/definitions/details",
          "title": "Site",
          "description": "Site",
          "order": 9
        },
        "siteName": {
          "type": "string",
          "title": "Site Name",
          "description": "Site name",
          "order": 10
        },
        "skipCallback": {
          "type": "boolean",
          "title": "Skip Callback",
          "description": "Skip callback",
          "order": 51
        },
        "sla": {
          "$ref": "#/definitions/details",
          "title": "SLA",
          "description": "SLA",
          "order": 95
        },
        "slaStatus": {
          "type": "string",
          "title": "SLA Status",
          "description": "SLA status",
          "order": 96
        },
        "source": {
          "$ref": "#/definitions/details",
          "title": "Source",
          "description": "Source",
          "order": 29
        },
        "stateIdentifier": {
          "type": "string",
          "title": "State Identifier",
          "description": "State identifier",
          "order": 14
        },
        "status": {
          "$ref": "#/definitions/agreement_details",
          "title": "Status",
          "description": "Status",
          "order": 5
        },
        "subBillingAmount": {
          "type": "number",
          "title": "Sub Billing Amount",
          "description": "Sub billing amount",
          "order": 67
        },
        "subBillingMethod": {
          "type": "string",
          "title": "Sub Billing Method",
          "description": "Sub billing method",
          "order": 66
        },
        "subDateAccepted": {
          "type": "string",
          "title": "Sub Date Accepted",
          "description": "Sub date accepted",
          "order": 68
        },
        "subType": {
          "$ref": "#/definitions/details",
          "title": "Subtype",
          "description": "Subtype",
          "order": 23
        },
        "summary": {
          "type": "string",
          "title": "Summary",
          "description": "Ticket summary",
          "order": 2
        },
        "team": {
          "$ref": "#/definitions/details",
          "title": "Team",
          "description": "Team",
          "order": 25
        },
        "type": {
          "$ref": "#/definitions/details",
          "title": "Type",
          "description": "Type",
          "order": 22
        },
        "workRole": {
          "$ref": "#/definitions/details",
          "title": "Work Role",
          "description": "Work role",
          "order": 6
        },
        "workType": {
          "$ref": "#/definitions/details",
          "title": "Work Type",
          "description": "Work type",
          "order": 7
        },
        "zip": {
          "type": "string",
          "title": "ZIP",
          "description": "ZIP code",
          "order": 15
        }
      },
      "definitions": {
        "agreement_details": {
          "type": "object",
          "title": "agreement_details",
          "properties": {
            "_info": {
              "type": "object",
              "title": "Info",
              "description": "Additional information",
              "order": 4
            },
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type",
              "order": 3
            }
          }
        },
        "currency_details": {
          "type": "object",
          "title": "currency_details",
          "properties": {
            "_info": {
              "type": "object",
              "title": "Info",
              "description": "Additional information",
              "order": 12
            },
            "currencyCode": {
              "type": "string",
              "title": "Currency Code",
              "description": "Currency code",
              "order": 3
            },
            "currencyIdentifier": {
              "type": "string",
              "title": "Currency Identifier",
              "description": "Currency identifier",
              "order": 8
            },
            "displayIdFlag": {
              "type": "boolean",
              "title": "Display ID Flag",
              "description": "Display ID flag",
              "order": 9
            },
            "displaySymbolFlag": {
              "type": "boolean",
              "title": "Display Symbol Flag",
              "description": "Display symbol flag",
              "order": 7
            },
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 11
            },
            "negativeParenthesesFlag": {
              "type": "boolean",
              "title": "Negative Parentheses Flag",
              "description": "Negative parentheses flag",
              "order": 6
            },
            "numberOfDecimals": {
              "type": "integer",
              "title": "Number Of Decimals",
              "description": "Number of decimals",
              "order": 4
            },
            "rightAlign": {
              "type": "boolean",
              "title": "Right Align",
              "description": "Right align",
              "order": 10
            },
            "symbol": {
              "type": "string",
              "title": "Symbol",
              "description": "Symbol",
              "order": 2
            },
            "thousandsSeparator": {
              "type": "string",
              "title": "Thousands Separator",
              "description": "Thousands Separator",
              "order": 5
            }
          }
        },
        "details": {
          "type": "object",
          "title": "details",
          "properties": {
            "_info": {
              "type": "object",
              "title": "Info",
              "description": "Additional information",
              "order": 3
            },
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            }
          }
        },
        "merged_parent_ticket_details": {
          "type": "object",
          "title": "merged_parent_ticket_details",
          "properties": {
            "_info": {
              "type": "object",
              "title": "Info",
              "description": "Additional information",
              "order": 3
            },
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID",
              "order": 1
            },
            "summary": {
              "type": "string",
              "title": "Summary",
              "description": "Summary",
              "order": 2
            }
          }
        },
        "more_details": {
          "type": "object",
          "title": "more_details",
          "properties": {
            "_info": {
              "type": "object",
              "title": "Info",
              "description": "Additional information",
              "order": 4
            },
            "id": {
              "type": "integer",
              "title": "ID",
              "description": "ID",
              "order": 1
            },
            "identifier": {
              "type": "string",
              "title": "Identifier",
              "description": "Identifier",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 3
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
