# Assertion helper to validate the response JSON against the provided schema
from jsonschema import Draft7Validator

from jsonschema import Draft7Validator

def assert_schema_validation(response_json: dict, schema: dict):

    validator = Draft7Validator(schema)
    
    # Coleta e ordena os erros pelo caminho do campo
    errors = sorted(validator.iter_errors(response_json), key=lambda e: e.path)

    if errors:
        error_details = []
        for error in errors:
            # error.path é uma lista, ex: ['user', 'address', 'zipCode']
            # .join() transforma em: "user -> address -> zipCode"
            path = " -> ".join(map(str, error.path))
            error_details.append(f"[{path}]: {error.message}")
        
        # Consolida todos os erros em uma mensagem única e legível
        full_message = "\n".join(error_details)
        
        # O assert agora falha mostrando exatamente onde e por que
        assert not errors, f"Falha no Contrato da API:\n{full_message}"