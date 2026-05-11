import pytest
from clients.customer_registration_client import CustomerRegistrationClient
from builders.customer_builder import CustomerBuilder

@pytest.fixture
def customer_registration_response(auth_data):

    customer_registration_client = CustomerRegistrationClient(auth_data["token"])

    customer_data = CustomerBuilder().build()
    
    response = customer_registration_client.register_customer(customer_data=customer_data)

    return response