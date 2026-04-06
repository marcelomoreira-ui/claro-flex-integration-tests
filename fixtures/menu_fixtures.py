import pytest
from clients.menu_client import MenuClient

@pytest.fixture
def menu_client(auth_data):
    return MenuClient(auth_data["token"])

@pytest.fixture
def menu_response(menu_client, auth_data):

    response = menu_client.get_menu(
        auth_data["customer_id"], 
        auth_data["product_id"])
    
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    return response