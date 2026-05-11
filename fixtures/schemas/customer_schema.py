CUSTOMER_REGISTRATION_SCHEMA = {
    {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Generated schema for Root",
        "type": "object",
        "properties": {
            "customerId": {"type": "string"},
            "trustedToken": {"type": "string"},
            "trustedTokenType": {"type": "string"},
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
                                    "action": {"type": "string"},
                                },
                                "required": ["type", "title", "action"],
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
        },
        "required": ["customerId", "trustedToken", "trustedTokenType", "modalList"],
    }
}
