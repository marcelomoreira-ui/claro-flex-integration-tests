
def get_specific_zipcode_mapping(cep: str, number: str) -> dict:

    mapping_specific_zipcode = {
        "request": {
            "method": "POST",
            "urlPath": "/flexbff/v1/customers/elegibilities",
            "bodyPatterns": [
                {
                    "equalToJson": f'{{ "postalCode": "{cep}", "number": "{number}" }}',
                    "ignoreExtraElements": True,
                }
            ],
        },
        "response": {
            "status": 201,
            "bodyFileName": "address-eligibility/post-response-201-specific-cep.json",
            "headers": {"Content-Type": "application/json"},
        },
    }

    return mapping_specific_zipcode

def get_generic_zipcode_mapping(cep: str, number: str) -> dict:

    mapping_generic_zipcode = {
        "request": {
            "method": "POST",
            "urlPath": "/flexbff/v1/customers/elegibilities",
            "bodyPatterns": [
                {
                    "equalToJson": f'{{ "postalCode": "{cep}" , "number": "{number}" }}',
                    "ignoreExtraElements": True,
                }
            ],
        },
        "response": {
            "status": 201,
            "bodyFileName": "address-eligibility/post-response-201-generic-cep.json",
            "headers": {"Content-Type": "application/json"},
        },
    }

    return mapping_generic_zipcode

def get_unsuccess_mapping(cep: str, number: str) -> dict:
    mapping_unsuccess = {
        "request": {
            "method": "POST",
            "urlPath": "/flexbff/v1/customers/elegibilities",
            "bodyPatterns": [
                {
                    "equalToJson": f'{{ "postalCode": "{cep}" , "number": "{number}" }}',
                    "ignoreExtraElements": True,
                }
            ],
        },
        "response": {
            "status": 400,
            "bodyFileName": "address-eligibility/post-response-400-not-elegible.json",
            "headers": {"Content-Type": "application/json"},
        },
    }
    return mapping_unsuccess
