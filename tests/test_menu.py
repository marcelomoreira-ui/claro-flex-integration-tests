import pytest
from clients.menu_client import MenuClient
from fixtures.schemas.menu_schema import menu_schema
from jsonschema import Draft7Validator
from helper import menu_helper as menu_helper

# TESTS
@pytest.mark.integration
@pytest.mark.parametrize("auth_data", ["default"], indirect=True)
def test_get_menu_should_return_200(auth_data, menu_response):
    """"
    Test to verify that the /menu endpoint returns a 200 status code.
    This test uses the menu_response fixture to get the response and then checks the status code.
    """

    response = menu_response  # Using the response from the fixture

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

#TESTS
@pytest.mark.integration
@pytest.mark.contract
@pytest.mark.parametrize("auth_data", ["multiple_products"], indirect=True)
def test_menu_should_match_schema(auth_data, menu_response):
    """"
    Test to validate that the response from the /menu endpoint matches the expected JSON schema.
    This test uses the menu_response fixture to get the response and then validates it against the menu_schema.
    """

    response = menu_response

    response_json = response.json()
    validator = Draft7Validator(menu_schema)
    errors = sorted(validator.iter_errors(response_json), key=lambda e: e.path)
    print(f"Validation errors: {[e.message for e in errors]}")
    assert not errors, f"Schema validation errors: {[e.message for e in errors]}"

#TESTS
@pytest.mark.integration
@pytest.mark.parametrize("auth_data", ["default"], indirect=True)
def test_menu_should_contain_expected_sections(auth_data, menu_response):
    """"
    Test to verify that the /menu endpoint response contains the expected sections.
    This test uses the menu_response fixture to get the response, extracts the section IDs
    """

    response = menu_response

    response_json = response.json()

    section_ids = menu_helper.get_section_ids(response_json)

    expected_items = ["MOBILE", "BROADBAND", "GENERAL"]

    menu_helper.assert_sections_present(section_ids, expected_items)