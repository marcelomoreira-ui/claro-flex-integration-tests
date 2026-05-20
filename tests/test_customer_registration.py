import pytest
from fixtures.schemas.customer_schema import CUSTOMER_REGISTRATION_SCHEMA as customer_schema
from utils.logger import get_logger as logger
from utils.json_validator import assert_schema_validation

logger = logger(__name__)

#TESTS
@pytest.mark.integration
@pytest.mark.customer_registration
def test_customer_should_match_schema(customer_registration_response):
    """"
    FLXRED-1436 - ID: 13 - [BACKEND][INTEGRAÇÃO] Persistência Completa Salesforce e Criação de Basket
    """
    logger.info("\nTesting customer schema validation")

    response = customer_registration_response(invalid_cpf=False)

    response_json = response.json()

    assert_schema_validation(response_json, customer_schema)

@pytest.mark.integration
@pytest.mark.customer_registration
def test_customer_registration_with_invalid_cpf(customer_registration_response):
    """"
    FLXRED-1424 - ID: 01 - [BACKEND][CADASTRO] Validar rejeição de CPF inválido ou sequencial
    """
    logger.info("\nTesting customer registration with invalid CPF")

    response = customer_registration_response(invalid_cpf=True)

    assert response.status_code == 400, f"Expected status code 400 for invalid CPF, got {response.status_code}"

@pytest.mark.integration
@pytest.mark.customer_registration
def test_customer_registration_with_under_eighteen_years_old(customer_registration_response):
    """"
    FLXRED-1427 - ID: 04 - [BACKEND][CADASTRO] Restrição de Idade Mínima (Menor de 18 anos)
    """
    logger.info("\nTesting customer registration with under eighteen years old")

    response = customer_registration_response(underage_birthdate=True)

    assert response.status_code == 400, f"Expected status code 400 for underage birthdate, got {response.status_code}"