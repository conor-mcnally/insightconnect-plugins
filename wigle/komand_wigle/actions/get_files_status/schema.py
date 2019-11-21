# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get the status of files uploaded by the current user"


class Input:
    PAGEEND = "pageend"
    PAGESTART = "pagestart"
    

class Output:
    PROCESSINGQUEUEDEPTH = "processingQueueDepth"
    RESULTS = "results"
    

class GetFilesStatusInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "pageend": {
      "type": "integer",
      "title": "Page End",
      "description": "Number of results to fetch from offset. Defaults to 100",
      "default": 100,
      "order": 2
    },
    "pagestart": {
      "type": "integer",
      "title": "Page Start",
      "description": "Most recent record to fetch descending chronologically. Defaults to 0",
      "default": 0,
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetFilesStatusOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "processingQueueDepth": {
      "type": "integer",
      "title": "Processing Queue Depth",
      "description": "Processing queue depth",
      "order": 2
    },
    "results": {
      "type": "array",
      "title": "Results",
      "description": "Information about uploaded files",
      "items": {
        "$ref": "#/definitions/transaction"
      },
      "order": 1
    }
  },
  "required": [
    "processingQueueDepth",
    "results"
  ],
  "definitions": {
    "transaction": {
      "type": "object",
      "title": "transaction",
      "properties": {
        "discovered": {
          "type": "integer",
          "title": "Discovered",
          "order": 10
        },
        "discoveredGps": {
          "type": "integer",
          "title": "Discovered GPS",
          "order": 9
        },
        "fileLines": {
          "type": "integer",
          "title": "File Lines",
          "order": 8
        },
        "fileName": {
          "type": "string",
          "title": "File Name",
          "order": 3
        },
        "fileSize": {
          "type": "integer",
          "title": "File Size",
          "order": 7
        },
        "firstTime": {
          "type": "string",
          "title": "First Time",
          "displayType": "date",
          "format": "date-time",
          "order": 5
        },
        "genDiscovered": {
          "type": "integer",
          "title": "Gen Discovered",
          "order": 16
        },
        "genDiscoveredGps": {
          "type": "integer",
          "title": "Gen Discovered GPS",
          "order": 17
        },
        "genTotal": {
          "type": "integer",
          "title": "Gen Total",
          "order": 18
        },
        "genTotalGps": {
          "type": "integer",
          "title": "Gen Total GPS",
          "order": 19
        },
        "genTotalLocations": {
          "type": "integer",
          "title": "Gen Total Locations",
          "order": 20
        },
        "lastupdt": {
          "type": "string",
          "title": "Last Updated",
          "displayType": "date",
          "format": "date-time",
          "order": 6
        },
        "percentDone": {
          "type": "number",
          "title": "Percent Done",
          "order": 14
        },
        "status": {
          "type": "string",
          "title": "Status",
          "order": 4
        },
        "timeParsing": {
          "type": "integer",
          "title": "Time Parsing",
          "order": 15
        },
        "total": {
          "type": "integer",
          "title": "Total",
          "order": 11
        },
        "totalGps": {
          "type": "integer",
          "title": "Total GPS",
          "order": 12
        },
        "totalLocations": {
          "type": "integer",
          "title": "Total Locations",
          "order": 13
        },
        "transid": {
          "type": "string",
          "title": "Transaction ID",
          "order": 1
        },
        "username": {
          "type": "string",
          "title": "Username",
          "order": 2
        },
        "wait": {
          "type": "integer",
          "title": "Wait",
          "order": 21
        }
      },
      "required": [
        "discovered",
        "discoveredGps",
        "fileLines",
        "fileName",
        "fileSize",
        "firstTime",
        "genDiscovered",
        "genDiscoveredGps",
        "genTotal",
        "genTotalGps",
        "genTotalLocations",
        "lastupdt",
        "percentDone",
        "status",
        "timeParsing",
        "total",
        "totalGps",
        "totalLocations",
        "transid",
        "username"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
