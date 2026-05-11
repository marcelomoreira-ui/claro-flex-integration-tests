import pytest
from fixtures.schemas.customer_schema import CUSTOMER_REGISTRATION_SCHEMA as customer_schema
from helper import menu_helper as menu_helper
from utils.logger import get_logger

logger = get_logger(__name__)

#TESTS
@pytest.mark.integration
@pytest.mark.parametrize("auth_data", ["multiple_products"], indirect=True)
def test_customer_should_match_schema(auth_data, customer_response):
    """"
    Test to verify that the /customer registration endpoint response matches the expected schema.
    """
    logger.info("Testing customer schema validation")
    response = customer_response

    response_json = response.json()

    menu_helper.assert_schema_validation(response_json, customer_schema)