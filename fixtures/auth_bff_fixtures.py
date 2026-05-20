import pytest
from clients.auth_bff_client import AuthBFFClient

@pytest.fixture(scope="session")
def auth_bff_data():
    auth_bff_client = AuthBFFClient()
    token = auth_bff_client.get_access_token()

    return {
        "token": token
    }
