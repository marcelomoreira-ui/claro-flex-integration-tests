import pytest
from clients.customer_registration_client import CustomerRegistrationClient
from builders.customer_builder import CustomerBuilder

@pytest.fixture
def customer_registration_response(invalid_cpf=False, custom_email=None) -> pytest.Response:

    customer_registration_client = CustomerRegistrationClient()

    builder = CustomerBuilder()

    if invalid_cpf:
        builder.with_invalid_cpf()
    if custom_email:
        builder.with_email(custom_email)

    customer_data = builder.build()

    response = customer_registration_client.register_customer(customer_data=customer_data)

    return response