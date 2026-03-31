import pytest
from clients.auth_client import AuthClient
from clients.menu_client import MenuClient
from fixtures.schemas.menu_schema import menu_schema
from jsonschema import Draft7Validator

@pytest.mark.parametrize("auth_data", ["default"], indirect=True)
@pytest.mark.integration
def test_get_menu_should_return_200(auth_data):
    auth_client = AuthClient()

    menu_client = MenuClient(auth_data["token"])

    response = menu_client.get_menu(auth_data["customer_id"], 
                                    auth_data["product_id"])

    assert response.status_code == 200

@pytest.mark.parametrize("auth_data", ["multiple_products"], indirect=True)
@pytest.mark.integration
def test_menu_should_match_schema(auth_data):
    client = MenuClient(auth_data["token"])

    response = client.get_menu(auth_data["customer_id"], auth_data["product_id"])

    assert response.status_code == 200

    response_json = response.json()

    validator = Draft7Validator(menu_schema)

    errors = sorted(validator.iter_errors(response_json), key=lambda e: e.path)

    print(f"Validation errors: {[e.message for e in errors]}")

    assert not errors, f"Schema validation errors: {[e.message for e in errors]}"
