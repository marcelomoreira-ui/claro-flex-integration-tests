import pytest
from clients.menu_client import MenuClient
from fixtures.schemas.menu_schema import menu_schema
from jsonschema import Draft7Validator

@pytest.mark.integration
@pytest.mark.statuscode
@pytest.mark.parametrize("auth_data", ["default"], indirect=True)
def test_get_menu_should_return_200(auth_data):
    # ------------------------
    # Arrange
    # ------------------------
    menu_client = MenuClient(auth_data["token"])

    # ------------------------
    # Act
    # ------------------------
    response = menu_client.get_menu(auth_data["customer_id"], 
                                    auth_data["product_id"])

    # ------------------------
    # Assert
    # ------------------------
    assert response.status_code == 200

@pytest.mark.integration
@pytest.mark.schema
@pytest.mark.parametrize("auth_data", ["multiple_products"], indirect=True)
def test_menu_should_match_schema(auth_data):
    # ------------------------
    # Arrange
    # ------------------------
    client = MenuClient(auth_data["token"])

    # ------------------------
    # Act
    # ------------------------
    response = client.get_menu(auth_data["customer_id"], auth_data["product_id"])

    # ------------------------
    # Assert
    # ------------------------
    assert response.status_code == 200
    response_json = response.json()
    validator = Draft7Validator(menu_schema)
    errors = sorted(validator.iter_errors(response_json), key=lambda e: e.path)
    print(f"Validation errors: {[e.message for e in errors]}")
    assert not errors, f"Schema validation errors: {[e.message for e in errors]}"
