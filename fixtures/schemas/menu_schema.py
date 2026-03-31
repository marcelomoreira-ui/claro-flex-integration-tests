menu_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Generated schema for Root",
        "type": "object",
        "properties": {
            "content": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "sections": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "string"},
                                "title": {"type": "string"},
                                "subtitle": {"type": "string"},
                                "items": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "icon": {"type": "string"},
                                            "title": {"type": "string"},
                                            "action": {"type": "string"},
                                            "productId": {"type": "number"},
                                            "customFields": {
                                                "type": "object",
                                                "properties": {
                                                    "events": {
                                                        "type": "object",
                                                        "properties": {
                                                            "ga": {
                                                                "type": "object",
                                                                "properties": {
                                                                    "event": {
                                                                        "type": "string"
                                                                    },
                                                                    "parameters": {
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "object",
                                                                            "properties": {
                                                                                "name": {
                                                                                    "type": "string"
                                                                                },
                                                                                "value": {
                                                                                    "type": "string"
                                                                                },
                                                                            },
                                                                            "required": [
                                                                                "name",
                                                                                "value",
                                                                            ],
                                                                        },
                                                                    },
                                                                },
                                                                "required": [
                                                                    "event",
                                                                    "parameters",
                                                                ],
                                                            },
                                                            "dynatrace": {
                                                                "type": "object",
                                                                "properties": {
                                                                    "event": {
                                                                        "type": "string"
                                                                    },
                                                                    "parameters": {
                                                                        "type": "array",
                                                                        "items": {
                                                                            "type": "object",
                                                                            "properties": {
                                                                                "name": {
                                                                                    "type": "string"
                                                                                },
                                                                                "value": {
                                                                                    "type": "string"
                                                                                },
                                                                            },
                                                                            "required": [
                                                                                "name",
                                                                                "value",
                                                                            ],
                                                                        },
                                                                    },
                                                                },
                                                                "required": [
                                                                    "event",
                                                                    "parameters",
                                                                ],
                                                            },
                                                        },
                                                        "required": ["ga", "dynatrace"],
                                                    },
                                                    "dynamicScreenId": {
                                                        "type": "string"
                                                    },
                                                },
                                                "required": [
                                                    "events",
                                                    "dynamicScreenId",
                                                ],
                                            },
                                            "modal": {
                                                "type": "object",
                                                "properties": {
                                                    "title": {"type": "string"},
                                                    "message": {"type": "string"},
                                                    "buttonMessage": {"type": "string"},
                                                    "action": {"type": "string"},
                                                    "options": {
                                                        "type": "array",
                                                        "items": {
                                                            "type": "object",
                                                            "properties": {
                                                                "type": {
                                                                    "type": "string"
                                                                },
                                                                "title": {
                                                                    "type": "string"
                                                                },
                                                                "action": {
                                                                    "type": "string"
                                                                },
                                                            },
                                                            "required": [
                                                                "type",
                                                                "title",
                                                                "action",
                                                            ],
                                                        },
                                                    },
                                                },
                                                "required": [
                                                    "title",
                                                    "message",
                                                    "buttonMessage",
                                                    "action",
                                                    "options",
                                                ],
                                            },
                                        },
                                        "required": [
                                            "icon",
                                            "title",
                                            "action",
                                            "productId",
                                        ],
                                    },
                                },
                            },
                            "required": ["id", "title", "items"],
                        },
                    },
                    "version": {
                        "type": "object",
                        "properties": {"title": {"type": "string"}},
                        "required": ["title"],
                    },
                },
                "required": ["title", "sections", "version"],
            }
        },
        "required": ["content"],
    }
