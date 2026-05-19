# Assertion helper to validate the response JSON against the provided schema
from jsonschema import Draft7Validator

def assert_schema_validation(response_json: dict, schema: dict):

    validator = Draft7Validator(schema)

    errors = sorted(validator.iter_errors(response_json), key=lambda e: e.path)

    print(f"Validation errors: {[e.message for e in errors]}")
    
    assert not errors, f"Schema validation errors: {[e.message for e in errors]}"