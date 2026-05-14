import pytest
from clients.customer_registration_client import CustomerRegistrationClient
from builders.customer_builder import CustomerBuilder

@pytest.fixture
def customer_registration_response():
    def _make_customer(invalid_cpf=False, custom_email=None, underage_birthdate=False):

        customer_registration_client = CustomerRegistrationClient()

        builder = CustomerBuilder()

        if invalid_cpf:
            builder.with_invalid_cpf()
        if custom_email:
            builder.with_email(custom_email)
        if underage_birthdate:
            builder.with_underage_birthdate()

        customer_data = builder.build()
        print(f"Customer data being sent for registration: {customer_data}")  # Debug print
        
        response = customer_registration_client.register_customer(customer_data=customer_data)

        return response
    return _make_customer