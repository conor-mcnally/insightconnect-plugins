# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get sensor"


class Input:
    INDICATOR = "indicator"
    

class Output:
    SENSOR = "sensor"
    

class GetSensorInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "indicator": {
      "type": "string",
      "title": "Indicator",
      "description": "The unique identifier of the machine you wish to perform the operation on, this can be an internal IPv4 address, hostname or sensor GUID",
      "order": 1
    }
  },
  "required": [
    "indicator"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetSensorOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "sensor": {
      "$ref": "#/definitions/sensors",
      "title": "Sensor",
      "description": "Sensor",
      "order": 1
    }
  },
  "required": [
    "sensor"
  ],
  "definitions": {
    "sensors": {
      "type": "object",
      "title": "sensors",
      "properties": {
        "actionsInProgress": {
          "type": "integer",
          "title": "Actions In Progress",
          "description": "The number of actions in progress (i.e. Not Resolved) on the machine",
          "order": 59
        },
        "amModeOrigin": {
          "type": "string",
          "title": "Anti-Malware Mode Origin",
          "description": "The source of the value for the Anti-Malware Signatures mode setting",
          "order": 40
        },
        "amStatus": {
          "type": "string",
          "title": "Anti-Malware Status",
          "description": "The Anti-Malware installation status for the sensor",
          "order": 39
        },
        "antiExploitStatus": {
          "type": "string",
          "title": "Anti Exploit Status",
          "description": "The status of the Exploit Prevention feature. This field returns a value only if you have enabled Exploit Prevention.",
          "order": 47
        },
        "antiMalwareModeOrigin": {
          "type": "string",
          "title": "Anti Malware Mode Origin",
          "description": "The source of the value for the Anti-Malware setting",
          "order": 54
        },
        "antiMalwareStatus": {
          "type": "string",
          "title": "Anti Malware Status",
          "description": "The Anti-Malware prevention mode for the sensor",
          "order": 53
        },
        "archiveTimeMs": {
          "type": "string",
          "title": "Archive Time MS",
          "description": "The time (in epoch) when the sensor was archived",
          "order": 19
        },
        "archivedOrUnarchiveComment": {
          "type": "string",
          "title": "Archived Or Unarchive Comment",
          "description": "The comment added when a sensor was archived or unarchived",
          "order": 22
        },
        "avDbLastUpdateTime": {
          "type": "integer",
          "title": "AV DB Last Update Time",
          "description": "The time when the Anti-Malware Signatures database on the machine where the sensor is installed was last updated",
          "order": 42
        },
        "avDbVersion": {
          "type": "string",
          "title": "AV DB Version",
          "description": "The version of the Anti-Malware Signatures database on the machine where the sensor is installed",
          "order": 41
        },
        "collectionComponents": {
          "type": "string",
          "title": "Collection Components",
          "description": "Any special collections enabled on the server and/or sensor",
          "order": 73
        },
        "collectionStatus": {
          "type": "string",
          "title": "Collection Status",
          "description": "States whether the machine has data collection enabled",
          "order": 31
        },
        "collectiveUuid": {
          "type": "string",
          "title": "Collective UUID",
          "description": "The identifier for the Registration server for the sensor",
          "order": 28
        },
        "compliance": {
          "type": "boolean",
          "title": "Compliance",
          "description": "Indicates whether the current sensor settings match the policy settings",
          "order": 82
        },
        "consoleVersion": {
          "type": "string",
          "title": "Console Version",
          "description": "The version for the console for your Cybereason environment",
          "order": 33
        },
        "cpuUsage": {
          "type": "number",
          "title": "CPU Usage",
          "description": "The amount of CPU used by the machine (expressed as a percentage)",
          "order": 36
        },
        "criticalAsset": {
          "type": "string",
          "title": "Critical Asset",
          "description": "The value assigned for the machine for the CRITICAL ASSET sensor tag",
          "order": 64
        },
        "customTags": {
          "type": "string",
          "title": "Custom Tags",
          "description": "A list of custom sensor tags assigned to the machine",
          "order": 66
        },
        "deliveryTime": {
          "type": "string",
          "title": "Delivery Time",
          "description": "The time (in epoch) when the last policy update was delivered to the sensor",
          "order": 80
        },
        "department": {
          "type": "string",
          "title": "Department",
          "description": "The value assigned to the machine for the DEPARTMENT sensor tag",
          "order": 62
        },
        "deviceModel": {
          "type": "string",
          "title": "Device Model",
          "description": "The model added for a device in the allowed devices section of the Endpoint Controls settings",
          "order": 51
        },
        "deviceType": {
          "type": "string",
          "title": "Device Type",
          "description": "The value assigned to the machine for the DEVICE TYPE sensor tag",
          "order": 65
        },
        "disconnected": {
          "type": "boolean",
          "title": "Disconnected",
          "description": "Indicates whether a sensor is currently disconnected",
          "order": 68
        },
        "disconnectionTime": {
          "type": "string",
          "title": "Disconnection Time",
          "description": "Time the machine was disconnected. Returns 0 if this is the first connection time. After the first connection, this is the time it was last connected",
          "order": 13
        },
        "documentProtectionMode": {
          "type": "string",
          "title": "Document Protection Mode",
          "description": "The mode set for the Document Protection mode",
          "order": 49
        },
        "documentProtectionStatus": {
          "type": "string",
          "title": "Document Protection Status",
          "description": "The status for the Document Protection mode",
          "order": 48
        },
        "exitReason": {
          "type": "string",
          "title": "Exit Reason",
          "description": "The reason the sensor service (minionhost.exe) stopped",
          "order": 58
        },
        "externalIpAddress": {
          "type": "string",
          "title": "External IP Address",
          "description": "The machine's external IP address for the local network",
          "order": 7
        },
        "firstSeenTime": {
          "type": "string",
          "title": "First Seen Time",
          "description": "The first time the machine was recognized. Timestamp values are returned in epoch",
          "order": 34
        },
        "fqdn": {
          "type": "string",
          "title": "Fully Qualified Domain Name",
          "description": "the fully qualified domain name (fqdn) for the machine",
          "order": 4
        },
        "fullScanStatus": {
          "type": "string",
          "title": "Full Scan Status",
          "description": "The status set for the sensor for the full scan",
          "order": 75
        },
        "fwStatus": {
          "type": "string",
          "title": "Fire Wall Status",
          "description": "The status of the Personal Firewall Control feature. This field returns a value only if you have enabled Endpoint Controls.",
          "order": 46
        },
        "groupId": {
          "type": "string",
          "title": "Group ID",
          "description": "The identifier the Cybereason platform uses for the group to which the sensor is assigned",
          "order": 83
        },
        "groupName": {
          "type": "string",
          "title": "Group Name",
          "description": "The name for the group to which the sensor is assigned",
          "order": 84
        },
        "groupStickiness": {
          "type": "boolean",
          "title": "Group Stickiness",
          "description": "Indicates whether this sensor is automatically assigned back to the group based on an assignment rule",
          "order": 85
        },
        "groupStickinessLabel": {
          "type": "string",
          "title": "Group Stickiness Label",
          "description": "The method by which the sensor was assigned to the group",
          "order": 87
        },
        "guid": {
          "type": "string",
          "title": "Global Unique ID",
          "description": "The globally unique sensor identifier",
          "order": 3
        },
        "internalIpAddress": {
          "type": "string",
          "title": "Internal IP Address",
          "description": "The machine's internal IP address as identified by the sensor",
          "order": 6
        },
        "isolated": {
          "type": "boolean",
          "title": "Isolated",
          "description": "States whether the machine is isolated. Returns true if the machine is isolated",
          "order": 12
        },
        "lastFullScheduleScanSuccessTime": {
          "type": "string",
          "title": "Last Full Schedule Scan Success Time",
          "description": "The time (in epoch) that the sensor last did a successful full scan",
          "order": 77
        },
        "lastQuickScheduleScanSuccessTime": {
          "type": "string",
          "title": "Last Quick Schedule Scan Success Time",
          "description": "The time (in epoch) that the sensor last did a successful quick scan",
          "order": 78
        },
        "lastStatusAction": {
          "type": "string",
          "title": "Last Status Action",
          "description": "The last action taken that changed the sensor status",
          "order": 21
        },
        "lastUpgradeResult": {
          "type": "string",
          "title": "Last Upgrade Result",
          "description": "The result of the last upgrade process",
          "order": 61
        },
        "lastUpgradeSteps": {
          "type": "string",
          "title": "Last Upgrade Steps",
          "description": "A list of step taken in the upgrade process. If there is a failure to upgrade the sensor, this list shows the failure",
          "order": 67
        },
        "location": {
          "type": "string",
          "title": "Location",
          "description": "The value assigned for this machine for the LOCATION sensor tag",
          "order": 63
        },
        "machineName": {
          "type": "string",
          "title": "Machine Name",
          "description": "The name of the machine",
          "order": 5
        },
        "memoryUsage": {
          "type": "integer",
          "title": "Memory Usage",
          "description": "The amount of RAM on the hosting computer used by the sensor",
          "order": 37
        },
        "offlineTimeMS": {
          "type": "string",
          "title": "Offline Time MS",
          "description": "he last time (in epoch) that the sensor was offline",
          "order": 17
        },
        "onlineTimeMS": {
          "type": "string",
          "title": "Online Time MS",
          "description": "The last time the sensor was seen online",
          "order": 16
        },
        "organization": {
          "type": "string",
          "title": "Organization",
          "description": "The organization name for the machine on which the sensor is installed",
          "order": 55
        },
        "organizationalUnit": {
          "type": "string",
          "title": "Organizational Unit",
          "description": "The name of the organization unit taken from the Active Directory on the machine on which the sensor is installed",
          "order": 52
        },
        "osType": {
          "type": "string",
          "title": "OS Type",
          "description": "The operating system running on the machine",
          "order": 29
        },
        "osVersionType": {
          "type": "string",
          "title": "OS Version Type",
          "description": "collectionStatus",
          "order": 30
        },
        "outdated": {
          "type": "boolean",
          "title": "Outdated",
          "description": "States whether or not the sensor version is out of sync with the server version",
          "order": 38
        },
        "pendingActions": {
          "type": "string",
          "title": "Pending Actions",
          "description": "An array containing batch numbers for actions pending to run on the sensor",
          "order": 60
        },
        "policyId": {
          "type": "string",
          "title": "Policy ID",
          "description": "The unique identifier the Cybereason platform uses for the policy assigned to the sensor",
          "order": 81
        },
        "policyName": {
          "type": "string",
          "title": "Policy Name",
          "description": "The name of the policy assigned to this sensor",
          "order": 79
        },
        "powerShellStatus": {
          "type": "string",
          "title": "Power Shell Status",
          "description": "The PowerShell Prevention mode",
          "order": 43
        },
        "preventionError": {
          "type": "string",
          "title": "Prevention Error",
          "description": "The error received for prevention by the sensor",
          "order": 57
        },
        "preventionStatus": {
          "type": "string",
          "title": "Prevention Status",
          "description": "The Execution Prevention mode",
          "order": 11
        },
        "privateServerIp": {
          "type": "string",
          "title": "Private Server IP",
          "description": "The private IP address for the Detection server for the sensor",
          "order": 27
        },
        "proxyAddress": {
          "type": "string",
          "title": "proxy Address",
          "description": "The address for the Proxy server used by this sensor",
          "order": 56
        },
        "purgedSensors": {
          "type": "boolean",
          "title": "Purged Sensors",
          "description": "Indicates whether this sensor was removed from the Sensors screen",
          "order": 86
        },
        "pylumId": {
          "type": "string",
          "title": "Pylum ID",
          "description": "The unique identifier assigned by Cybereason to the sensor",
          "order": 2
        },
        "quickScanStatus": {
          "type": "string",
          "title": "Quick Scan Status",
          "description": "The status set for the sensor for a quick scan",
          "order": 76
        },
        "ransomwareStatus": {
          "type": "string",
          "title": "Ransomware Status",
          "description": "The Anti-Ransomware mode",
          "order": 10
        },
        "remoteShellStatus": {
          "type": "string",
          "title": "Remote Shell Status",
          "description": "Whether or not the Remote Shell utility is enabled for the sensor. This field returns a value only if you have enabled Remote Shell for your Cybereason server",
          "order": 44
        },
        "sensorArchivedByUser": {
          "type": "string",
          "title": "Sensor Archived By User",
          "description": "The Cybereason user name for the user who archived the selected sensor",
          "order": 23
        },
        "sensorLastUpdate": {
          "type": "string",
          "title": "Sensor Last Update",
          "description": "The last time (in epoch) that the sensor was updated",
          "order": 74
        },
        "sensor_id": {
          "type": "string",
          "title": "Sensor ID",
          "description": "The unique identifier for a sensor",
          "order": 1
        },
        "serialNumber": {
          "type": "string",
          "title": "Serial Number",
          "description": "The serial number added for a device in the allowed devices section of the Endpoint Controls settings",
          "order": 50
        },
        "serverId": {
          "type": "string",
          "title": "Server ID",
          "description": "The unique identifier for the Detection server for the sensor",
          "order": 25
        },
        "serverIp": {
          "type": "string",
          "title": "Server IP",
          "description": "The IP address for the Detection server for the sensor",
          "order": 26
        },
        "serverName": {
          "type": "string",
          "title": "Server Name",
          "description": "The name of the server for the sensor",
          "order": 24
        },
        "serviceStatus": {
          "type": "string",
          "title": "Service Status",
          "description": "Indicates the current value of the Anti-Malware service",
          "order": 15
        },
        "siteId": {
          "type": "integer",
          "title": "Machine Name",
          "description": "The identifier for the sensor's site",
          "order": 9
        },
        "siteName": {
          "type": "string",
          "title": "Site Name",
          "description": "The name of the site for the sensor",
          "order": 8
        },
        "staleTimeMS": {
          "type": "string",
          "title": "Stale Time MS",
          "description": "The time (in epoch) when the Sensor was classified as Stale",
          "order": 18
        },
        "staticAnalysisDetectMode": {
          "type": "string",
          "title": "Static Analysis Detect Mode",
          "description": "The value for the Artificial Intelligence Detect mode in the Anti-Malware settings",
          "order": 69
        },
        "staticAnalysisDetectModeOrigin": {
          "type": "string",
          "title": "Static Analysis Detect Mode Origin",
          "description": "The source of the value for the Artificial Intelligence Detect mode setting",
          "order": 70
        },
        "staticAnalysisPreventMode": {
          "type": "string",
          "title": "Static Analysis Prevent Mode",
          "description": "The value for the Artificial Intelligence Prevent Mode in the Anti-Malware settings",
          "order": 71
        },
        "staticAnalysisPreventModeOrigin": {
          "type": "string",
          "title": "Static Analysis Prevent Mode Origin",
          "description": "The source of the value for the Artificial Intelligence Prevent mode setting",
          "order": 72
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The status of the sensor",
          "order": 14
        },
        "statusTimeMS": {
          "type": "string",
          "title": "Status Time MS",
          "description": "The last time (in epoch) when the sensor sent a status",
          "order": 20
        },
        "upTime": {
          "type": "string",
          "title": "Up Time",
          "description": "The time the sensors have been in the UP state",
          "order": 35
        },
        "usbStatus": {
          "type": "string",
          "title": "USB Status",
          "description": "The status of the Device Control feature. This field returns a value only if you have enabled Endpoint Controls.",
          "order": 45
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "The sensor version number",
          "order": 32
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
