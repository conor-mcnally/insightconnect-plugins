# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Retrieves all events matching the input search criteria. Response is a list of events in JSON format. Resulting events are sorted in descending order of time"


class Input:
    APPLICATIONNAME = "applicationName"
    EVENTTYPE = "eventType"
    HOSTNAME = "hostName"
    HOSTNAMEEXACT = "hostNameExact"
    IPADDRESS = "ipAddress"
    OWNERNAME = "ownerName"
    OWNERNAMEEXACT = "ownerNameExact"
    SEARCHWINDOW = "searchWindow"
    SHA256HASH = "sha256hash"
    

class Output:
    ELAPSED = "elapsed"
    LATESTTIME = "latestTime"
    MESSAGE = "message"
    RESULTS = "results"
    SUCCESS = "success"
    TOTALRESULTS = "totalResults"
    

class FindEventInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "applicationName": {
      "type": "string",
      "title": "Application Name",
      "description": "Filter on events generated by a process with the given application name (for example, googleupdate.exe. Note that this name must be lowercase)",
      "order": 7
    },
    "eventType": {
      "type": "string",
      "title": "Event Type",
      "description": "Filter on events with a given event type",
      "enum": [
        "",
        "NETWORK",
        "FILE_CREATE",
        "REGISTRY_ACCESS",
        "SYSTEM_API_CALL",
        "CREATE_PROCESS",
        "DATA_ACCESS",
        "INJECT_CODE"
      ],
      "order": 8
    },
    "hostName": {
      "type": "string",
      "title": "Hostname",
      "description": "Filter on hostnames case insensitive. For example hostName=win-IA9NQ1GN8OI will match the hostname WIN-IA9NQ1GN8OI",
      "order": 1
    },
    "hostNameExact": {
      "type": "string",
      "title": "Hostname Exact",
      "description": "Filter on the exact hostname. For example hostName=WIN-IA9NQ1GN8OI will only return devices with the exact hostname WIN-IA9NQ1GN8OI but not a host named win-IA9NQ1GN8OI",
      "order": 2
    },
    "ipAddress": {
      "type": "string",
      "title": "IP Address",
      "description": "Filter on events generated by a device with a given external or internal IP address",
      "order": 5
    },
    "ownerName": {
      "type": "string",
      "title": "Owners Name",
      "description": "Filter on owner name case insensitive",
      "order": 3
    },
    "ownerNameExact": {
      "type": "string",
      "title": "Owners Name Exact",
      "description": "Same as 'Owners Name' but with case sensitivity",
      "order": 4
    },
    "searchWindow": {
      "type": "string",
      "title": "Search Window",
      "description": "Filter on events generated within a given relative time frame. Note that the default is one day if a searchWindow is not specified. Note that events may not be available past 30 days due to retention policies e.g. 4d, 2w",
      "order": 9
    },
    "sha256hash": {
      "type": "string",
      "title": "SHA-256 Hash",
      "description": "Filter on events generated by a process with the given SHA-256 hash. Note that this hash must be lowercase",
      "order": 6
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class FindEventOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "elapsed": {
      "type": "integer",
      "title": "Elapsed",
      "description": "Elapsed",
      "order": 4
    },
    "latestTime": {
      "type": "integer",
      "title": "Latest Time",
      "description": "Latest Time",
      "order": 2
    },
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Message",
      "order": 5
    },
    "results": {
      "type": "array",
      "title": "Results",
      "description": "Results",
      "items": {
        "$ref": "#/definitions/results"
      },
      "order": 3
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success",
      "order": 1
    },
    "totalResults": {
      "type": "integer",
      "title": "Total Results",
      "description": "Total Results",
      "order": 6
    }
  },
  "definitions": {
    "deviceDetails": {
      "type": "object",
      "title": "deviceDetails",
      "properties": {
        "agentLocation": {
          "type": "string",
          "title": "Agent Location",
          "description": "Agent Location",
          "order": 1
        },
        "deviceHostName": {
          "type": "string",
          "title": "Device Host Name",
          "description": "Device Host Name",
          "order": 2
        },
        "deviceId": {
          "type": "integer",
          "title": "Device ID",
          "description": "Device ID",
          "order": 3
        },
        "deviceIpAddress": {
          "type": "string",
          "title": "Device IP Address",
          "description": "Device IP Address",
          "order": 4
        },
        "deviceIpV4Address": {
          "type": "string",
          "title": "Device IPv4 Address",
          "description": "Device IPv4 Address",
          "order": 5
        },
        "deviceLocation": {
          "$ref": "#/definitions/deviceLocation",
          "title": "Device Location",
          "description": "Device Location",
          "order": 6
        },
        "deviceName": {
          "type": "string",
          "title": "Device Name",
          "description": "Device Name",
          "order": 7
        },
        "deviceOwnerName": {
          "type": "string",
          "title": "Device Owner Name",
          "description": "Device Owner Name",
          "order": 8
        },
        "deviceType": {
          "type": "string",
          "title": "Device Type",
          "description": "Device Type",
          "order": 9
        },
        "deviceVersion": {
          "type": "string",
          "title": "Device Version",
          "description": "Device Version",
          "order": 10
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Email",
          "order": 11
        },
        "groupName": {
          "type": "string",
          "title": "Group Name",
          "description": "Group Name",
          "order": 12
        },
        "targetPriorityCode": {
          "type": "integer",
          "title": "Target Priority Code",
          "description": "Target Priority Code",
          "order": 13
        },
        "targetPriorityType": {
          "type": "string",
          "title": "Target Priority Type",
          "description": "Target Priority Type",
          "order": 14
        }
      },
      "definitions": {
        "deviceLocation": {
          "type": "object",
          "title": "deviceLocation",
          "properties": {
            "areaCode": {
              "type": "integer",
              "title": "Area Code",
              "description": "Area Code",
              "order": 1
            },
            "city": {
              "type": "string",
              "title": "City",
              "description": "City",
              "order": 2
            },
            "countryCode": {
              "type": "string",
              "title": "Country Code",
              "description": "Country Code",
              "order": 3
            },
            "countryName": {
              "type": "string",
              "title": "Country Name",
              "description": "Country Name",
              "order": 4
            },
            "dmaCode": {
              "type": "integer",
              "title": "DMA Code",
              "description": "DMA Code",
              "order": 5
            },
            "latitude": {
              "type": "number",
              "title": "Latitude",
              "description": "Latitude",
              "order": 6
            },
            "longitude": {
              "type": "number",
              "title": "Longitude",
              "description": "Longitude",
              "order": 7
            },
            "metroCode": {
              "type": "integer",
              "title": "Metro Code",
              "description": "Metro Code",
              "order": 8
            },
            "postalCode": {
              "type": "string",
              "title": "Postal Code",
              "description": "Postal Code",
              "order": 9
            },
            "region": {
              "type": "string",
              "title": "Region",
              "description": "Region",
              "order": 10
            }
          }
        }
      }
    },
    "deviceLocation": {
      "type": "object",
      "title": "deviceLocation",
      "properties": {
        "areaCode": {
          "type": "integer",
          "title": "Area Code",
          "description": "Area Code",
          "order": 1
        },
        "city": {
          "type": "string",
          "title": "City",
          "description": "City",
          "order": 2
        },
        "countryCode": {
          "type": "string",
          "title": "Country Code",
          "description": "Country Code",
          "order": 3
        },
        "countryName": {
          "type": "string",
          "title": "Country Name",
          "description": "Country Name",
          "order": 4
        },
        "dmaCode": {
          "type": "integer",
          "title": "DMA Code",
          "description": "DMA Code",
          "order": 5
        },
        "latitude": {
          "type": "number",
          "title": "Latitude",
          "description": "Latitude",
          "order": 6
        },
        "longitude": {
          "type": "number",
          "title": "Longitude",
          "description": "Longitude",
          "order": 7
        },
        "metroCode": {
          "type": "integer",
          "title": "Metro Code",
          "description": "Metro Code",
          "order": 8
        },
        "postalCode": {
          "type": "string",
          "title": "Postal Code",
          "description": "Postal Code",
          "order": 9
        },
        "region": {
          "type": "string",
          "title": "Region",
          "description": "Region",
          "order": 10
        }
      }
    },
    "netFlow": {
      "type": "object",
      "title": "netFlow",
      "properties": {
        "destAddress": {
          "type": "string",
          "title": "Net Flow",
          "description": "Net Flow",
          "order": 1
        },
        "destPort": {
          "type": "string",
          "title": "Destination Port",
          "description": "Destination Port",
          "order": 2
        },
        "peerFqdn": {
          "type": "string",
          "title": "Peer FQDN",
          "description": "Peer Fully Qualified Domain Name",
          "order": 3
        },
        "peerIpAddress": {
          "type": "string",
          "title": "Peer IP Address",
          "description": "Peer IP Address",
          "order": 4
        },
        "peerIpV4Address": {
          "type": "string",
          "title": "Peer IPv4 Address",
          "description": "Peer IPv4 Address",
          "order": 5
        },
        "peerLocation": {
          "type": "object",
          "title": "Peer Location",
          "description": "Peer Location",
          "order": 6
        },
        "peerSiteReputation": {
          "type": "string",
          "title": "Peer Site Reputation",
          "description": "Peer Site Reputation",
          "order": 7
        },
        "service": {
          "type": "string",
          "title": "Service",
          "description": "Service",
          "order": 8
        },
        "sourceAddress": {
          "type": "string",
          "title": "Source Address",
          "description": "Source Address",
          "order": 9
        },
        "sourcePort": {
          "type": "string",
          "title": "Source Port",
          "description": "Source Port",
          "order": 10
        }
      }
    },
    "parentApp": {
      "type": "object",
      "title": "parentApp",
      "properties": {
        "applicationName": {
          "type": "string",
          "title": "Application Name",
          "description": "Application Name",
          "order": 1
        },
        "applicationPath": {
          "type": "string",
          "title": "Application Path",
          "description": "Application Path",
          "order": 2
        },
        "effectiveReputation": {
          "type": "string",
          "title": "Effective Reputation",
          "description": "Effective Reputation",
          "order": 3
        },
        "effectiveReputationSource": {
          "type": "string",
          "title": "Effective Reputation Source",
          "description": "Effective Reputation Source",
          "order": 4
        },
        "md5Hash": {
          "type": "string",
          "title": "MD5 Hash",
          "description": "MD5 Hash",
          "order": 5
        },
        "reputationProperty": {
          "type": "string",
          "title": "Reputation Property",
          "description": "Reputation Property",
          "order": 6
        },
        "sha256Hash": {
          "type": "string",
          "title": "SHA-256 Hash",
          "description": "SHA-256 Hash",
          "order": 7
        },
        "virusCategory": {
          "type": "string",
          "title": "Virus Category",
          "description": "Virus Category",
          "order": 8
        },
        "virusName": {
          "type": "string",
          "title": "Virus Name",
          "description": "Virus Name",
          "order": 9
        },
        "virusSubCategory": {
          "type": "string",
          "title": "Virus Sub Category",
          "description": "Virus Sub Category",
          "order": 10
        }
      }
    },
    "processDetails": {
      "type": "object",
      "title": "processDetails",
      "properties": {
        "commandLine": {
          "type": "string",
          "title": "Process Details",
          "description": "Process Details",
          "order": 1
        },
        "fullUserName": {
          "type": "string",
          "title": "Full User Name",
          "description": "Full User Name",
          "order": 2
        },
        "interpreterHash": {
          "type": "string",
          "title": "Interpreter Hash",
          "description": "Interpreter Hash",
          "order": 3
        },
        "interpreterName": {
          "type": "string",
          "title": "Interpreter Name",
          "description": "Interpreter Name",
          "order": 4
        },
        "milisSinceProcessStart": {
          "type": "integer",
          "title": "Milliseconds Since Process has Started",
          "description": "Milliseconds since process has started",
          "order": 5
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 6
        },
        "parentCommandLine": {
          "type": "string",
          "title": "Parent Command Line",
          "description": "Parent Command Line",
          "order": 7
        },
        "parentName": {
          "type": "string",
          "title": "Parent Name",
          "description": "Parent Name",
          "order": 8
        },
        "parentPid": {
          "type": "integer",
          "title": "Parent PID",
          "description": "Parent Process ID",
          "order": 9
        },
        "parentPrivatePid": {
          "type": "string",
          "title": "Parent Private PID",
          "description": "Parent Private Process ID",
          "order": 10
        },
        "privatePid": {
          "type": "string",
          "title": "Private Process ID",
          "description": "Private Process ID",
          "order": 11
        },
        "processId": {
          "type": "integer",
          "title": "Process ID",
          "description": "Process ID",
          "order": 12
        },
        "targetCommandLine": {
          "type": "string",
          "title": "Target Command Line",
          "description": "Target Command Line",
          "order": 13
        },
        "targetName": {
          "type": "string",
          "title": "Target Name",
          "description": "Target Name",
          "order": 14
        },
        "targetPid": {
          "type": "integer",
          "title": "Target Process ID",
          "description": "Target Process ID",
          "order": 15
        },
        "targetPrivatePid": {
          "type": "string",
          "title": "Target Private PID",
          "description": "Target Private Process ID",
          "order": 16
        },
        "userName": {
          "type": "string",
          "title": "User Name",
          "description": "User Name",
          "order": 17
        }
      }
    },
    "results": {
      "type": "object",
      "title": "results",
      "properties": {
        "alertCategory": {
          "type": "string",
          "title": "Alert Category",
          "description": "Alert Category",
          "order": 1
        },
        "alertScore": {
          "type": "integer",
          "title": "Alert Score",
          "description": "Alert Score",
          "order": 2
        },
        "attackStage": {
          "type": "string",
          "title": "Attack Stage",
          "description": "Attack Stage",
          "order": 3
        },
        "createTime": {
          "type": "integer",
          "title": "Create Time",
          "description": "Create Time",
          "order": 4
        },
        "deviceDetails": {
          "$ref": "#/definitions/deviceDetails",
          "title": "Device Details",
          "description": "Device Details",
          "order": 5
        },
        "eventId": {
          "type": "string",
          "title": "Event ID",
          "description": "Event ID",
          "order": 6
        },
        "eventTime": {
          "type": "integer",
          "title": "Event Time",
          "description": "Event Time",
          "order": 7
        },
        "eventType": {
          "type": "string",
          "title": "Event Time",
          "description": "Event Type",
          "order": 8
        },
        "incidentId": {
          "type": "string",
          "title": "Incident ID",
          "description": "Incident ID",
          "order": 9
        },
        "longDescription": {
          "type": "string",
          "title": "Long Description",
          "description": "Long Description",
          "order": 10
        },
        "netFlow": {
          "$ref": "#/definitions/netFlow",
          "title": "Net Flow",
          "description": "Net Flow",
          "order": 11
        },
        "parentApp": {
          "$ref": "#/definitions/parentApp",
          "title": "Parent Application",
          "description": "Parent Application",
          "order": 12
        },
        "processDetails": {
          "$ref": "#/definitions/processDetails",
          "title": "Process Details",
          "description": "Process Details",
          "order": 13
        },
        "registryValue": {
          "type": "string",
          "title": "Registry Value",
          "description": "Registry Value",
          "order": 14
        },
        "securityEventCode": {
          "type": "string",
          "title": "Security Event Code",
          "description": "Security Event Code",
          "order": 15
        },
        "selectedApp": {
          "$ref": "#/definitions/parentApp",
          "title": "Selected Application",
          "description": "Selected Application",
          "order": 16
        },
        "shortDescription": {
          "type": "string",
          "title": "Short Description",
          "description": "Short Description",
          "order": 17
        },
        "targetApp": {
          "$ref": "#/definitions/parentApp",
          "title": "Target Application",
          "description": "Target Application",
          "order": 18
        },
        "threatIndicators": {
          "type": "array",
          "title": "Threat Indicators",
          "description": "Threat Indicators",
          "items": {
            "type": "string"
          },
          "order": 19
        }
      },
      "definitions": {
        "deviceDetails": {
          "type": "object",
          "title": "deviceDetails",
          "properties": {
            "agentLocation": {
              "type": "string",
              "title": "Agent Location",
              "description": "Agent Location",
              "order": 1
            },
            "deviceHostName": {
              "type": "string",
              "title": "Device Host Name",
              "description": "Device Host Name",
              "order": 2
            },
            "deviceId": {
              "type": "integer",
              "title": "Device ID",
              "description": "Device ID",
              "order": 3
            },
            "deviceIpAddress": {
              "type": "string",
              "title": "Device IP Address",
              "description": "Device IP Address",
              "order": 4
            },
            "deviceIpV4Address": {
              "type": "string",
              "title": "Device IPv4 Address",
              "description": "Device IPv4 Address",
              "order": 5
            },
            "deviceLocation": {
              "$ref": "#/definitions/deviceLocation",
              "title": "Device Location",
              "description": "Device Location",
              "order": 6
            },
            "deviceName": {
              "type": "string",
              "title": "Device Name",
              "description": "Device Name",
              "order": 7
            },
            "deviceOwnerName": {
              "type": "string",
              "title": "Device Owner Name",
              "description": "Device Owner Name",
              "order": 8
            },
            "deviceType": {
              "type": "string",
              "title": "Device Type",
              "description": "Device Type",
              "order": 9
            },
            "deviceVersion": {
              "type": "string",
              "title": "Device Version",
              "description": "Device Version",
              "order": 10
            },
            "email": {
              "type": "string",
              "title": "Email",
              "description": "Email",
              "order": 11
            },
            "groupName": {
              "type": "string",
              "title": "Group Name",
              "description": "Group Name",
              "order": 12
            },
            "targetPriorityCode": {
              "type": "integer",
              "title": "Target Priority Code",
              "description": "Target Priority Code",
              "order": 13
            },
            "targetPriorityType": {
              "type": "string",
              "title": "Target Priority Type",
              "description": "Target Priority Type",
              "order": 14
            }
          },
          "definitions": {
            "deviceLocation": {
              "type": "object",
              "title": "deviceLocation",
              "properties": {
                "areaCode": {
                  "type": "integer",
                  "title": "Area Code",
                  "description": "Area Code",
                  "order": 1
                },
                "city": {
                  "type": "string",
                  "title": "City",
                  "description": "City",
                  "order": 2
                },
                "countryCode": {
                  "type": "string",
                  "title": "Country Code",
                  "description": "Country Code",
                  "order": 3
                },
                "countryName": {
                  "type": "string",
                  "title": "Country Name",
                  "description": "Country Name",
                  "order": 4
                },
                "dmaCode": {
                  "type": "integer",
                  "title": "DMA Code",
                  "description": "DMA Code",
                  "order": 5
                },
                "latitude": {
                  "type": "number",
                  "title": "Latitude",
                  "description": "Latitude",
                  "order": 6
                },
                "longitude": {
                  "type": "number",
                  "title": "Longitude",
                  "description": "Longitude",
                  "order": 7
                },
                "metroCode": {
                  "type": "integer",
                  "title": "Metro Code",
                  "description": "Metro Code",
                  "order": 8
                },
                "postalCode": {
                  "type": "string",
                  "title": "Postal Code",
                  "description": "Postal Code",
                  "order": 9
                },
                "region": {
                  "type": "string",
                  "title": "Region",
                  "description": "Region",
                  "order": 10
                }
              }
            }
          }
        },
        "deviceLocation": {
          "type": "object",
          "title": "deviceLocation",
          "properties": {
            "areaCode": {
              "type": "integer",
              "title": "Area Code",
              "description": "Area Code",
              "order": 1
            },
            "city": {
              "type": "string",
              "title": "City",
              "description": "City",
              "order": 2
            },
            "countryCode": {
              "type": "string",
              "title": "Country Code",
              "description": "Country Code",
              "order": 3
            },
            "countryName": {
              "type": "string",
              "title": "Country Name",
              "description": "Country Name",
              "order": 4
            },
            "dmaCode": {
              "type": "integer",
              "title": "DMA Code",
              "description": "DMA Code",
              "order": 5
            },
            "latitude": {
              "type": "number",
              "title": "Latitude",
              "description": "Latitude",
              "order": 6
            },
            "longitude": {
              "type": "number",
              "title": "Longitude",
              "description": "Longitude",
              "order": 7
            },
            "metroCode": {
              "type": "integer",
              "title": "Metro Code",
              "description": "Metro Code",
              "order": 8
            },
            "postalCode": {
              "type": "string",
              "title": "Postal Code",
              "description": "Postal Code",
              "order": 9
            },
            "region": {
              "type": "string",
              "title": "Region",
              "description": "Region",
              "order": 10
            }
          }
        },
        "netFlow": {
          "type": "object",
          "title": "netFlow",
          "properties": {
            "destAddress": {
              "type": "string",
              "title": "Net Flow",
              "description": "Net Flow",
              "order": 1
            },
            "destPort": {
              "type": "string",
              "title": "Destination Port",
              "description": "Destination Port",
              "order": 2
            },
            "peerFqdn": {
              "type": "string",
              "title": "Peer FQDN",
              "description": "Peer Fully Qualified Domain Name",
              "order": 3
            },
            "peerIpAddress": {
              "type": "string",
              "title": "Peer IP Address",
              "description": "Peer IP Address",
              "order": 4
            },
            "peerIpV4Address": {
              "type": "string",
              "title": "Peer IPv4 Address",
              "description": "Peer IPv4 Address",
              "order": 5
            },
            "peerLocation": {
              "type": "object",
              "title": "Peer Location",
              "description": "Peer Location",
              "order": 6
            },
            "peerSiteReputation": {
              "type": "string",
              "title": "Peer Site Reputation",
              "description": "Peer Site Reputation",
              "order": 7
            },
            "service": {
              "type": "string",
              "title": "Service",
              "description": "Service",
              "order": 8
            },
            "sourceAddress": {
              "type": "string",
              "title": "Source Address",
              "description": "Source Address",
              "order": 9
            },
            "sourcePort": {
              "type": "string",
              "title": "Source Port",
              "description": "Source Port",
              "order": 10
            }
          }
        },
        "parentApp": {
          "type": "object",
          "title": "parentApp",
          "properties": {
            "applicationName": {
              "type": "string",
              "title": "Application Name",
              "description": "Application Name",
              "order": 1
            },
            "applicationPath": {
              "type": "string",
              "title": "Application Path",
              "description": "Application Path",
              "order": 2
            },
            "effectiveReputation": {
              "type": "string",
              "title": "Effective Reputation",
              "description": "Effective Reputation",
              "order": 3
            },
            "effectiveReputationSource": {
              "type": "string",
              "title": "Effective Reputation Source",
              "description": "Effective Reputation Source",
              "order": 4
            },
            "md5Hash": {
              "type": "string",
              "title": "MD5 Hash",
              "description": "MD5 Hash",
              "order": 5
            },
            "reputationProperty": {
              "type": "string",
              "title": "Reputation Property",
              "description": "Reputation Property",
              "order": 6
            },
            "sha256Hash": {
              "type": "string",
              "title": "SHA-256 Hash",
              "description": "SHA-256 Hash",
              "order": 7
            },
            "virusCategory": {
              "type": "string",
              "title": "Virus Category",
              "description": "Virus Category",
              "order": 8
            },
            "virusName": {
              "type": "string",
              "title": "Virus Name",
              "description": "Virus Name",
              "order": 9
            },
            "virusSubCategory": {
              "type": "string",
              "title": "Virus Sub Category",
              "description": "Virus Sub Category",
              "order": 10
            }
          }
        },
        "processDetails": {
          "type": "object",
          "title": "processDetails",
          "properties": {
            "commandLine": {
              "type": "string",
              "title": "Process Details",
              "description": "Process Details",
              "order": 1
            },
            "fullUserName": {
              "type": "string",
              "title": "Full User Name",
              "description": "Full User Name",
              "order": 2
            },
            "interpreterHash": {
              "type": "string",
              "title": "Interpreter Hash",
              "description": "Interpreter Hash",
              "order": 3
            },
            "interpreterName": {
              "type": "string",
              "title": "Interpreter Name",
              "description": "Interpreter Name",
              "order": 4
            },
            "milisSinceProcessStart": {
              "type": "integer",
              "title": "Milliseconds Since Process has Started",
              "description": "Milliseconds since process has started",
              "order": 5
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 6
            },
            "parentCommandLine": {
              "type": "string",
              "title": "Parent Command Line",
              "description": "Parent Command Line",
              "order": 7
            },
            "parentName": {
              "type": "string",
              "title": "Parent Name",
              "description": "Parent Name",
              "order": 8
            },
            "parentPid": {
              "type": "integer",
              "title": "Parent PID",
              "description": "Parent Process ID",
              "order": 9
            },
            "parentPrivatePid": {
              "type": "string",
              "title": "Parent Private PID",
              "description": "Parent Private Process ID",
              "order": 10
            },
            "privatePid": {
              "type": "string",
              "title": "Private Process ID",
              "description": "Private Process ID",
              "order": 11
            },
            "processId": {
              "type": "integer",
              "title": "Process ID",
              "description": "Process ID",
              "order": 12
            },
            "targetCommandLine": {
              "type": "string",
              "title": "Target Command Line",
              "description": "Target Command Line",
              "order": 13
            },
            "targetName": {
              "type": "string",
              "title": "Target Name",
              "description": "Target Name",
              "order": 14
            },
            "targetPid": {
              "type": "integer",
              "title": "Target Process ID",
              "description": "Target Process ID",
              "order": 15
            },
            "targetPrivatePid": {
              "type": "string",
              "title": "Target Private PID",
              "description": "Target Private Process ID",
              "order": 16
            },
            "userName": {
              "type": "string",
              "title": "User Name",
              "description": "User Name",
              "order": 17
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
