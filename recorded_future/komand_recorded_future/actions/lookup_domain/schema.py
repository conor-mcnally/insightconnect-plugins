# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Return information about a specific domain entry"


class Input:
    COMMENT = "comment"
    DOMAIN = "domain"
    

class Output:
    ANALYSTNOTES = "analystNotes"
    COUNTS = "counts"
    ENTERPRISELISTS = "enterpriseLists"
    ENTITY = "entity"
    INTELCARD = "intelCard"
    METRICS = "metrics"
    RELATEDENTITIES = "relatedEntities"
    RISK = "risk"
    SIGHTINGS = "sightings"
    THREATLISTS = "threatLists"
    TIMESTAMPS = "timestamps"
    

class LookupDomainInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Add a comment to a domain",
      "order": 2
    },
    "domain": {
      "type": "string",
      "title": "Domain",
      "description": "Domain",
      "order": 1
    }
  },
  "required": [
    "domain"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class LookupDomainOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "analystNotes": {
      "type": "array",
      "title": "Analyst Notes",
      "description": "Notes from an analyst",
      "items": {
        "$ref": "#/definitions/analystNote"
      },
      "order": 3
    },
    "counts": {
      "type": "array",
      "title": "Counts",
      "description": "Counts",
      "items": {
        "$ref": "#/definitions/counts"
      },
      "order": 4
    },
    "enterpriseLists": {
      "type": "array",
      "title": "Enterprise Lists",
      "description": "Enterprise lists",
      "items": {
        "$ref": "#/definitions/enterpriseLists"
      },
      "order": 11
    },
    "entity": {
      "$ref": "#/definitions/entity",
      "title": "Entity",
      "description": "Entity",
      "order": 1
    },
    "intelCard": {
      "type": "string",
      "title": "Intel Card",
      "description": "Intel card",
      "order": 5
    },
    "metrics": {
      "type": "array",
      "title": "Metrics",
      "description": "Metrics",
      "items": {
        "$ref": "#/definitions/metrics"
      },
      "order": 6
    },
    "relatedEntities": {
      "type": "array",
      "title": "Related Entities",
      "description": "Related entities",
      "items": {
        "$ref": "#/definitions/relatedEntities"
      },
      "order": 7
    },
    "risk": {
      "$ref": "#/definitions/risk",
      "title": "Risk",
      "description": "Risk",
      "order": 10
    },
    "sightings": {
      "type": "array",
      "title": "Sightings",
      "description": "Sightings",
      "items": {
        "$ref": "#/definitions/sightings"
      },
      "order": 8
    },
    "threatLists": {
      "type": "array",
      "title": "Threat Lists",
      "description": "Threat lists",
      "items": {
        "$ref": "#/definitions/threatLists"
      },
      "order": 9
    },
    "timestamps": {
      "$ref": "#/definitions/timestamps",
      "title": "Timestamps",
      "description": "Timestamps",
      "order": 2
    }
  },
  "definitions": {
    "analystNote": {
      "type": "object",
      "title": "analystNote",
      "properties": {
        "attributes": {
          "$ref": "#/definitions/attributes",
          "title": "Attributes",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "Id",
          "order": 2
        },
        "source": {
          "$ref": "#/definitions/labels",
          "title": "Source",
          "order": 3
        }
      },
      "definitions": {
        "attributes": {
          "type": "object",
          "title": "attributes",
          "properties": {
            "context_entities": {
              "type": "array",
              "title": "Context Entities",
              "items": {
                "$ref": "#/definitions/context_entities"
              },
              "order": 1
            },
            "labels": {
              "type": "array",
              "title": "Labels",
              "items": {
                "$ref": "#/definitions/labels"
              },
              "order": 2
            },
            "note_entities": {
              "type": "array",
              "title": "Note Entities",
              "items": {
                "$ref": "#/definitions/labels"
              },
              "order": 3
            },
            "published": {
              "type": "string",
              "title": "Published",
              "order": 4
            },
            "text": {
              "type": "string",
              "title": "Text",
              "order": 5
            },
            "title": {
              "type": "string",
              "title": "Title",
              "order": 6
            },
            "topic": {
              "$ref": "#/definitions/context_entities",
              "title": "Topic",
              "order": 7
            },
            "validated_on": {
              "type": "string",
              "title": "Validated On",
              "order": 8
            },
            "validation_urls": {
              "type": "array",
              "title": "Validation Urls",
              "items": {
                "$ref": "#/definitions/labels"
              },
              "order": 9
            }
          },
          "definitions": {
            "context_entities": {
              "type": "object",
              "title": "context_entities",
              "properties": {
                "description": {
                  "type": "string",
                  "title": "Description",
                  "order": 1
                },
                "id": {
                  "type": "string",
                  "title": "Id",
                  "order": 2
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "order": 3
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "order": 4
                }
              }
            },
            "labels": {
              "type": "object",
              "title": "labels",
              "properties": {
                "id": {
                  "type": "string",
                  "title": "Id",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "order": 2
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "order": 3
                }
              }
            }
          }
        },
        "context_entities": {
          "type": "object",
          "title": "context_entities",
          "properties": {
            "description": {
              "type": "string",
              "title": "Description",
              "order": 1
            },
            "id": {
              "type": "string",
              "title": "Id",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 3
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 4
            }
          }
        },
        "labels": {
          "type": "object",
          "title": "labels",
          "properties": {
            "id": {
              "type": "string",
              "title": "Id",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 3
            }
          }
        }
      }
    },
    "attributes": {
      "type": "object",
      "title": "attributes",
      "properties": {
        "context_entities": {
          "type": "array",
          "title": "Context Entities",
          "items": {
            "$ref": "#/definitions/context_entities"
          },
          "order": 1
        },
        "labels": {
          "type": "array",
          "title": "Labels",
          "items": {
            "$ref": "#/definitions/labels"
          },
          "order": 2
        },
        "note_entities": {
          "type": "array",
          "title": "Note Entities",
          "items": {
            "$ref": "#/definitions/labels"
          },
          "order": 3
        },
        "published": {
          "type": "string",
          "title": "Published",
          "order": 4
        },
        "text": {
          "type": "string",
          "title": "Text",
          "order": 5
        },
        "title": {
          "type": "string",
          "title": "Title",
          "order": 6
        },
        "topic": {
          "$ref": "#/definitions/context_entities",
          "title": "Topic",
          "order": 7
        },
        "validated_on": {
          "type": "string",
          "title": "Validated On",
          "order": 8
        },
        "validation_urls": {
          "type": "array",
          "title": "Validation Urls",
          "items": {
            "$ref": "#/definitions/labels"
          },
          "order": 9
        }
      },
      "definitions": {
        "context_entities": {
          "type": "object",
          "title": "context_entities",
          "properties": {
            "description": {
              "type": "string",
              "title": "Description",
              "order": 1
            },
            "id": {
              "type": "string",
              "title": "Id",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 3
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 4
            }
          }
        },
        "labels": {
          "type": "object",
          "title": "labels",
          "properties": {
            "id": {
              "type": "string",
              "title": "Id",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 3
            }
          }
        }
      }
    },
    "context_entities": {
      "type": "object",
      "title": "context_entities",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "Id",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 3
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 4
        }
      }
    },
    "counts": {
      "type": "object",
      "title": "counts",
      "properties": {
        "count": {
          "type": "integer",
          "title": "Count",
          "order": 1
        },
        "date": {
          "type": "string",
          "title": "Date",
          "order": 2
        }
      }
    },
    "enterpriseLists": {
      "type": "object",
      "title": "enterpriseLists",
      "properties": {
        "added": {
          "type": "string",
          "title": "Added",
          "description": "Added",
          "order": 1
        },
        "list": {
          "$ref": "#/definitions/list",
          "title": "List",
          "description": "List",
          "order": 2
        }
      },
      "definitions": {
        "list": {
          "type": "object",
          "title": "list",
          "properties": {
            "id": {
              "type": "string",
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
        }
      }
    },
    "entities": {
      "type": "object",
      "title": "entities",
      "properties": {
        "count": {
          "type": "integer",
          "title": "Count",
          "order": 1
        },
        "entity": {
          "$ref": "#/definitions/entity",
          "title": "Entity",
          "order": 2
        }
      },
      "definitions": {
        "entity": {
          "type": "object",
          "title": "entity",
          "properties": {
            "description": {
              "type": "string",
              "title": "Description",
              "order": 4
            },
            "id": {
              "type": "string",
              "title": "Id",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 3
            }
          }
        }
      }
    },
    "entity": {
      "type": "object",
      "title": "entity",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "Id",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 3
        }
      }
    },
    "evidenceDetails": {
      "type": "object",
      "title": "evidenceDetails",
      "properties": {
        "criticality": {
          "type": "number",
          "title": "Criticality",
          "order": 1
        },
        "criticalityLabel": {
          "type": "string",
          "title": "Criticality Label",
          "order": 2
        },
        "evidenceString": {
          "type": "string",
          "title": "Evidence String",
          "order": 3
        },
        "rule": {
          "type": "string",
          "title": "Rule",
          "order": 4
        },
        "timestamp": {
          "type": "string",
          "title": "Timestamp",
          "order": 5
        }
      }
    },
    "labels": {
      "type": "object",
      "title": "labels",
      "properties": {
        "id": {
          "type": "string",
          "title": "Id",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 3
        }
      }
    },
    "list": {
      "type": "object",
      "title": "list",
      "properties": {
        "id": {
          "type": "string",
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
    "metrics": {
      "type": "object",
      "title": "metrics",
      "properties": {
        "type": {
          "type": "string",
          "title": "Type",
          "order": 1
        },
        "value": {
          "type": "number",
          "title": "Value",
          "order": 2
        }
      }
    },
    "relatedEntities": {
      "type": "object",
      "title": "relatedEntities",
      "properties": {
        "entities": {
          "type": "array",
          "title": "Entities",
          "items": {
            "$ref": "#/definitions/entities"
          },
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 2
        }
      },
      "definitions": {
        "entities": {
          "type": "object",
          "title": "entities",
          "properties": {
            "count": {
              "type": "integer",
              "title": "Count",
              "order": 1
            },
            "entity": {
              "$ref": "#/definitions/entity",
              "title": "Entity",
              "order": 2
            }
          },
          "definitions": {
            "entity": {
              "type": "object",
              "title": "entity",
              "properties": {
                "description": {
                  "type": "string",
                  "title": "Description",
                  "order": 4
                },
                "id": {
                  "type": "string",
                  "title": "Id",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "order": 2
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "order": 3
                }
              }
            }
          }
        },
        "entity": {
          "type": "object",
          "title": "entity",
          "properties": {
            "description": {
              "type": "string",
              "title": "Description",
              "order": 4
            },
            "id": {
              "type": "string",
              "title": "Id",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 3
            }
          }
        }
      }
    },
    "risk": {
      "type": "object",
      "title": "risk",
      "properties": {
        "criticality": {
          "type": "number",
          "title": "Criticality",
          "order": 1
        },
        "criticalityLabel": {
          "type": "string",
          "title": "Criticality Label",
          "order": 2
        },
        "evidenceDetails": {
          "type": "array",
          "title": "Evidence Details",
          "items": {
            "$ref": "#/definitions/evidenceDetails"
          },
          "order": 3
        },
        "riskSummary": {
          "type": "string",
          "title": "Risk Summary",
          "order": 4
        },
        "rules": {
          "type": "integer",
          "title": "Rules",
          "order": 5
        },
        "score": {
          "type": "integer",
          "title": "Score",
          "order": 6
        }
      },
      "definitions": {
        "evidenceDetails": {
          "type": "object",
          "title": "evidenceDetails",
          "properties": {
            "criticality": {
              "type": "number",
              "title": "Criticality",
              "order": 1
            },
            "criticalityLabel": {
              "type": "string",
              "title": "Criticality Label",
              "order": 2
            },
            "evidenceString": {
              "type": "string",
              "title": "Evidence String",
              "order": 3
            },
            "rule": {
              "type": "string",
              "title": "Rule",
              "order": 4
            },
            "timestamp": {
              "type": "string",
              "title": "Timestamp",
              "order": 5
            }
          }
        }
      }
    },
    "sightings": {
      "type": "object",
      "title": "sightings",
      "properties": {
        "fragment": {
          "type": "string",
          "title": "Fragment",
          "order": 1
        },
        "published": {
          "type": "string",
          "title": "Published",
          "order": 2
        },
        "source": {
          "type": "string",
          "title": "Source",
          "order": 3
        },
        "title": {
          "type": "string",
          "title": "Title",
          "order": 4
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 5
        },
        "url": {
          "type": "string",
          "title": "Url",
          "order": 6
        }
      }
    },
    "threatLists": {
      "type": "object",
      "title": "threatLists",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 3
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 4
        }
      }
    },
    "timestamps": {
      "type": "object",
      "title": "timestamps",
      "properties": {
        "firstSeen": {
          "type": "string",
          "title": "First Seen",
          "order": 1
        },
        "lastSeen": {
          "type": "string",
          "title": "Last Seen",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
