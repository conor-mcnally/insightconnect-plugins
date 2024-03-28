# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve a list of localized internet anonymization countries"


class Input:
    pass


class Output:
    COUNTRIES = "countries"


class ListCountriesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListCountriesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "countries": {
      "type": "array",
      "title": "Countries",
      "description": "List of localized internet anonymization countries",
      "items": {
        "$ref": "#/definitions/country"
      },
      "order": 1
    }
  },
  "required": [
    "countries"
  ],
  "definitions": {
    "country": {
      "type": "object",
      "title": "country",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the country",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)