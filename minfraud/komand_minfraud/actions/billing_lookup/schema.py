# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Query billing address info"


class Input:
    ADDRESS = "address"
    BILLING_ADDRESS = "billing_address"
    BILLING_ADDRESS_2 = "billing_address_2"
    BILLING_CITY = "billing_city"
    BILLING_COMPANY = "billing_company"
    BILLING_COUNTRY = "billing_country"
    BILLING_FIRST_NAME = "billing_first_name"
    BILLING_LAST_NAME = "billing_last_name"
    BILLING_PHONE_COUNTRY_CODE = "billing_phone_country_code"
    BILLING_PHONE_NUMBER = "billing_phone_number"
    BILLING_POSTAL = "billing_postal"
    BILLING_REGION = "billing_region"
    

class Output:
    BILLING_RESULT = "billing_result"
    RISK_SCORE = "risk_score"
    

class BillingLookupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "IP Address",
      "description": "IP address to query",
      "order": 1
    },
    "billing_address": {
      "type": "string",
      "title": "Billing Address",
      "description": "Billing address line 1",
      "order": 5
    },
    "billing_address_2": {
      "type": "string",
      "title": "Billing Address 2",
      "description": "Billing address line 2",
      "order": 6
    },
    "billing_city": {
      "type": "string",
      "title": "City",
      "description": "City of billing address",
      "order": 7
    },
    "billing_company": {
      "type": "string",
      "title": "Company Name",
      "description": "Company name in billing info",
      "order": 4
    },
    "billing_country": {
      "type": "string",
      "title": "Country Code",
      "description": "Two character country code",
      "order": 9
    },
    "billing_first_name": {
      "type": "string",
      "title": "First Name",
      "description": "First name in billing info",
      "order": 2
    },
    "billing_last_name": {
      "type": "string",
      "title": "Last Name",
      "description": "Last name in billing info",
      "order": 3
    },
    "billing_phone_country_code": {
      "type": "string",
      "title": "Phone Country Code",
      "description": "Country code for phone number",
      "order": 12
    },
    "billing_phone_number": {
      "type": "string",
      "title": "Phone Number",
      "description": "Phone number without country code",
      "order": 11
    },
    "billing_postal": {
      "type": "string",
      "title": "Postal Code",
      "description": "Postal Code in billing address",
      "order": 10
    },
    "billing_region": {
      "type": "string",
      "title": "Region Code",
      "description": "Subdivision code in billing address",
      "order": 8
    }
  },
  "required": [
    "address"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class BillingLookupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "billing_result": {
      "$ref": "#/definitions/billing",
      "title": "Billing Result",
      "description": "Results for billing",
      "order": 1
    },
    "risk_score": {
      "type": "string",
      "title": "Risk Score",
      "description": "Overall risk score",
      "order": 2
    }
  },
  "definitions": {
    "billing": {
      "type": "object",
      "title": "billing",
      "properties": {
        "distance_to_ip_location": {
          "type": "integer",
          "title": "Distance To Ip Location",
          "description": "Distance to IP location",
          "order": 4
        },
        "is_ip_in_country": {
          "type": "boolean",
          "title": "Is Ip In Country",
          "description": "Is IP in country",
          "order": 5
        },
        "is_postal_in_city": {
          "type": "boolean",
          "title": "Is Postal In City",
          "description": "Is postal code in city",
          "order": 1
        },
        "latitude": {
          "type": "string",
          "title": "Latitude",
          "description": "Latitude for billing address",
          "order": 2
        },
        "longitude": {
          "type": "string",
          "title": "Longitude",
          "description": "Longitude for billing address",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
