import pytest
from clients.auth_client import AuthClient


@pytest.fixture(scope="session")
def auth_data():
    client = AuthClient()
    return client.get_token()