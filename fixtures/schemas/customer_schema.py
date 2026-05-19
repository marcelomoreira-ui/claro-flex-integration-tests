CUSTOMER_REGISTRATION_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Generated schema for Root",
    "type": "object",
    "properties": {
        "customerId": {"type": "string"},
        "token": {
            "type": "object",
            "properties": {"trusted": {"type": "string"}, "type": {"type": "string"}},
            "required": ["trusted", "type"],
        },
        "modalList": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {"type": "string"},
                    "title": {"type": "string"},
                    "message": {"type": "string"},
                    "ignorable": {"type": "boolean"},
                    "bottomButtons": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {"type": "string"},
                                "title": {"type": "string"},
                                "screenAction": {"type": "string"},
                            },
                            "required": ["type", "title", "screenAction"],
                        },
                    },
                    "closeButton": {"type": "string"},
                },
                "required": [
                    "type",
                    "title",
                    "message",
                    "ignorable",
                    "bottomButtons",
                    "closeButton",
                ],
            },
        },
        "direction": {"type": "string"},
    },
    "required": ["customerId", "token", "modalList", "direction"],
}
