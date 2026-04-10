import pytest
from fixtures.schemas.menu_schema import menu_schema
from jsonschema import Draft7Validator
from helper import menu_helper as menu_helper
from utils.logger import get_logger

logger = get_logger(__name__)

#TESTS
@pytest.mark.integration
@pytest.mark.parametrize("auth_data", ["multiple_products"], indirect=True)
def test_menu_should_match_schema(auth_data, menu_response):
    """"
    Test to verify that the /menu endpoint response matches the expected schema.
    """
    logger.info("Testing menu schema validation")
    response = menu_response

    response_json = response.json()
    validator = Draft7Validator(menu_schema)
    errors = sorted(validator.iter_errors(response_json), key=lambda e: e.path)
    print(f"Validation errors: {[e.message for e in errors]}")
    assert not errors, f"Schema validation errors: {[e.message for e in errors]}"

# TESTS
@pytest.mark.integration
@pytest.mark.parametrize("auth_data", ["mobile_sim_del_one_line_active"], indirect=True)
def test_menu_should_contain_expected_sections_mobile(auth_data, menu_response):
    """"
    Test to verify that the /menu endpoint response contains the expected sections for a user with only mobile product active.
    """

    logger.info("Testing menu sections for mobile user")
    response = menu_response  # Using the response from the fixture
    response_json = response.json()
    expected_items = ["MOBILE", "GENERAL"]
    not_expected_items = ["BROADBAND"]

    logger.info(f"Expected sections: {expected_items}")
    menu_helper.assert_sections_present(menu_helper.get_section_ids(response_json), expected_items)
    menu_helper.assert_section_not_present(menu_helper.get_section_ids(response_json), not_expected_items)

@pytest.mark.integration
@pytest.mark.parametrize("auth_data", ["mobile_sim_del_one_line_active"], indirect=True)
def test_menu_should_contain_expected_item_broadband(auth_data, menu_response):
    """"
    Test to verify that the /menu endpoint response contains the expected buy_broadband item for a user with broadband product active.
    """

    logger.info("Testing menu items for broadband user")
    response = menu_response 
    response_json = response.json()
    expected_items = ["BUY_BROADBAND"]

    menu_helper.assert_itens_present(menu_helper.get_itens_from_general_section(response_json), expected_items)

#TESTS
@pytest.mark.integration
@pytest.mark.building
@pytest.mark.parametrize("auth_data", ["default"], indirect=True)
def test_menu_should_contain_expected_sections_mobile_bl(auth_data, menu_response):
    """"
    Test to verify that the /menu endpoint response contains the expected sections for a user with mobile and broadband products active.
    """

    logger.info("Testing menu sections for mobile and broadband user")
    response = menu_response
    response_json = response.json()
    section_ids = menu_helper.get_section_ids(response_json)
    expected_items = ["MOBILE", "BROADBAND", "GENERAL"]
    menu_helper.assert_sections_present(section_ids, expected_items)