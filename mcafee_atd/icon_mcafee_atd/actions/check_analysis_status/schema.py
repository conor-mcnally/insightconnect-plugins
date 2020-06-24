# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Checks the analysis status"


class Input:
    ANALYSIS_ID = "analysis_id"
    TYPE = "type"
    

class Output:
    JOB_RESULTS = "job_results"
    RESULTS = "results"
    SUCCESS = "success"
    

class CheckAnalysisStatusInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "analysis_id": {
      "type": "integer",
      "title": "Analysis ID",
      "description": "Task ID or job ID value which is returned in submission step",
      "order": 1
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Type of ID, default value is task",
      "default": "task",
      "enum": [
        "task",
        "job"
      ],
      "order": 2
    }
  },
  "required": [
    "analysis_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CheckAnalysisStatusOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "job_results": {
      "$ref": "#/definitions/job",
      "title": "Job Results",
      "description": "Return information about given Job ID",
      "order": 3
    },
    "results": {
      "$ref": "#/definitions/output",
      "title": "Results",
      "description": "Return information about given Task ID",
      "order": 2
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success status of analysis ID",
      "order": 1
    }
  },
  "definitions": {
    "job": {
      "type": "object",
      "title": "job",
      "properties": {
        "allEngineState": {
          "type": "integer",
          "title": "All Engine State",
          "description": "All engine state",
          "order": 2
        },
        "severity": {
          "type": "integer",
          "title": "Severity",
          "description": "Severity",
          "order": 3
        },
        "status": {
          "type": "integer",
          "title": "Status",
          "description": "Status",
          "order": 1
        }
      }
    },
    "output": {
      "type": "object",
      "title": "output",
      "properties": {
        "PEInfo": {
          "type": "string",
          "title": "PE info",
          "description": "PE info",
          "order": 13
        },
        "asmListing": {
          "type": "string",
          "title": "Asm Listing",
          "description": "Asm listing",
          "order": 12
        },
        "family": {
          "type": "string",
          "title": "Family",
          "description": "Family",
          "order": 14
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Filename",
          "order": 5
        },
        "istate": {
          "type": "integer",
          "title": "Istate",
          "description": "Istate",
          "order": 3
        },
        "jobid": {
          "type": "integer",
          "title": "Job ID",
          "description": "Job ID",
          "order": 8
        },
        "md5": {
          "type": "string",
          "title": "MD5",
          "description": "MD5",
          "order": 6
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 4
        },
        "submitTime": {
          "type": "string",
          "title": "Submit Time",
          "description": "Submit time",
          "order": 9
        },
        "summaryFiles": {
          "type": "string",
          "title": "Summary Files",
          "description": "Summary files",
          "order": 10
        },
        "taskid": {
          "type": "integer",
          "title": "Task ID",
          "description": "Task ID",
          "order": 2
        },
        "useLogs": {
          "type": "string",
          "title": "Use Logs",
          "description": "Use logs",
          "order": 11
        },
        "userid": {
          "type": "integer",
          "title": "User ID",
          "description": "User ID",
          "order": 1
        },
        "vmDesc": {
          "type": "string",
          "title": "VM Desc",
          "description": "VM desc",
          "order": 16
        },
        "vmName": {
          "type": "string",
          "title": "VM Name",
          "description": "VM name",
          "order": 15
        },
        "vmProfile": {
          "type": "string",
          "title": "VM Profile",
          "description": "VM profile",
          "order": 7
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
