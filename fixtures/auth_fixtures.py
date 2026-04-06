import pytest
from clients.auth_client import AuthClient
from config.test_users import TEST_USERS


@pytest.fixture
def auth_data(request):
    user_key = request.param
    
    if user_key not in TEST_USERS:
        raise ValueError(f"User key '{user_key}' not found in TEST_USERS")

    user = TEST_USERS[user_key]

    client = AuthClient()

    return client.get_token(
        username=user["username"],
        password=user["password"]
    )