import pytest
from utils.logger import get_logger as logger
from utils.json_validator import assert_schema_validation
from fixtures.schemas.address_eligibility_schema import ADDRESS_ELIGIBILITY_SUCCESS_SCHEMA

logger = logger(__name__)

@pytest.mark.integration
@pytest.mark.address_eligibility
def test_address_elegibility_should_match_schema(address_eligibility_response):
    """"
    FLXRED-1492 - ID: 02 - [BACKEND][CONTRATO] Conformidade do Payload de Endereço
    Test that the address eligibility response payload matches the expected schema.
    """
    logger.info("\nTesting address eligibility schema validation")

    cep = "01310930"
    number = "100"

    response = address_eligibility_response(cep, number, scenario="specific_zipcode")

    response_json = response.json()

    assert_schema_validation(response_json, ADDRESS_ELIGIBILITY_SUCCESS_SCHEMA)

@pytest.mark.integration
@pytest.mark.address_eligibility
def test_address_elegibility_should_return_status_eligible_for_especific_zipcode(address_eligibility_response):
    """"
    FLXRED-1493 - ID: 03 - [BACKEND][ELEGIBILIDADE] Viabilidade CEP Específico (Endereço Cadastrado)
    Test that the address eligibility response returns status "ELIGIBLE" for a specific zipcode (registered zipcode).
    """
    logger.info("\nTesting address eligibility status validation for specific zipcode")

    cep = "01310930"
    number = "100"

    response = address_eligibility_response(cep, number, scenario="specific_zipcode")
    response_json = response.json()

    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    assert response_json["status"] == "ELIGIBLE", f"Expected status 'ELIGIBLE', but got '{response_json['status']}'"
    assert response_json["isGenericZipcode"] == False, f"Expected isGenericZipcode to be False, but got '{response_json['isGenericZipcode']}'"

@pytest.mark.integration
@pytest.mark.address_eligibility
def test_address_elegibility_should_return_status_eligible_for_generic_zipcode(address_eligibility_response):

    """"
    FLXRED-1499 - ID: 09 - [BACKEND][ELEGIBILIDADE] CEP Genérico (Endereço Cadastrado)
    Test that the address eligibility response returns status "ELIGIBLE" for a generic zipcode (unregistered zipcode).
    """
    logger.info("\nTesting address eligibility status validation for generic zipcode")

    cep = "01310931"
    number = "100"

    response = address_eligibility_response(cep, number, scenario="generic_zipcode")
    response_json = response.json()

    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    assert response_json["status"] == "ELIGIBLE", f"Expected status 'ELIGIBLE', but got '{response_json['status']}'"
    assert response_json["isGenericZipcode"] == True, f"Expected isGenericZipcode to be True, but got '{response_json['isGenericZipcode']}'"

@pytest.mark.integration
@pytest.mark.address_eligibility
def test_address_elegibility_should_return_status_not_eligible_for_non_covered_zipcode(address_eligibility_response):

    """"
    FLXRED-1506 - ID: 15 - [BACKEND][ELEGIBILIDADE] Fora de Cobertura (CEP Específico)
    Test that the address eligibility response returns status "NOT ELIGIBLE" for a non-covered area zipcode (unregistered address).
    """
    logger.info("\nTesting address eligibility status validation for non-covered area zipcode")

    cep = "00000000"
    number = "100"

    response = address_eligibility_response(cep, number, scenario="non_covered_zipcode")
    response_json = response.json()

    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert response_json["status"] == "NOT ELIGIBLE", f"Expected status 'NOT ELIGIBLE', but got '{response_json['status']}'"
    assert response_json["isGenericZipcode"] == False, f"Expected isGenericZipcode to be False, but got '{response_json['isGenericZipcode']}'"