post_scripts_request = {
    "type" : "object",
    "required": ["scriptNum", "parts"],
    "properties" : {
        "scriptNum": {
            "type": "number",
        },
        "parts": {
            "type" : "array",
            "items": {
                "type": "object",
                "properties": {
                    "part": {
                        "type": "number"
                    },
                    "blocking": {
                        "type":"array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": { "type" : "string"},
                                "position": {"type": "number"},
                            }
                        },
                    }
                }
            }   
        },
    },
}


schemas = {
    'addBlocking': post_scripts_request,
}