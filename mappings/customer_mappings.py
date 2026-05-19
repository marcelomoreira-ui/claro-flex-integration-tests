def get_success_mapping(cpf: str) -> dict:
    mapping_success = {
        "request": {
            "method": "POST",
            "urlPath": "/ext-application/v3/customer/registration",
            "bodyPatterns": [
                {
                    "matchesJsonPath": f"$.user[?(@.document == '{cpf}')]",
                    "ignoreExtraElements": True,
                }
            ],
        },
        "response": {
            "status": 201,
            "bodyFileName": "customer-acquisition/post-customer-acquisition-201.json",
            "headers": {"Content-Type": "application/json"},
        },
    }

    return mapping_success


def get_unsuccess_mapping(cpf: str = None) -> dict:
    mapping_unsuccess = {
        "request": {
            "method": "POST",
            "urlPath": "/ext-application/v3/customer/registration",
            "bodyPatterns": [
                {
                    "matchesJsonPath": f"$.user[?(@.document == '{cpf or '12345678900'}')]",
                    "ignoreExtraElements": True,
                }
            ],
        },
        "response": {
            "status": 400,
            "bodyFileName": "customer-acquisition/post-customer-acquisition-400-invalid-cpf.json",
            "headers": {"Content-Type": "application/json"},
        },
    }
    return mapping_unsuccess


def get_underage_mapping(cpf: str = None) -> dict:
    mapping_underage = {
        "request": {
            "method": "POST",
            "urlPath": "/ext-application/v3/customer/registration",
            "bodyPatterns": [
                {
                    "matchesJsonPath": f"$.user[?(@.document == '{cpf or '12345678911'}')]",
                    "ignoreExtraElements": True,
                }
            ],
        },
        "response": {
            "status": 400,
            "bodyFileName": "customer-acquisition/post-customer-acquisition-400-under-age.json",
            "headers": {"Content-Type": "application/json"},
        },
    }
    return mapping_underage