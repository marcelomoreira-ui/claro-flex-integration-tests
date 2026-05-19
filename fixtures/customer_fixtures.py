import pytest
from clients.customer_client import CustomerClient
from builders.customer_builder import CustomerBuilder
from config.settings import config
from clients.wiremock_client import WireMockClient

@pytest.fixture(scope="function")
def customer_registration_response(request):

    # Initialize clients
    customer_registration_client = CustomerClient()
    wiremock_client = WireMockClient()
    current_env = config.get("ENV", "local").lower()

    def _make_customer(invalid_cpf=False, custom_email=None, underage_birthdate=False):

        builder = CustomerBuilder()
        if invalid_cpf:
            builder.with_invalid_cpf()
        if custom_email:
            builder.with_email(custom_email)
        if underage_birthdate:
            builder.with_underage_birthdate()

        customer_data = builder.build()
        print(f"Customer data being sent for registration: {customer_data}")  # Debug print
        
        if current_env == "local":
            wiremock_client.update_mappings(cpf=customer_data["user"]["document"])
            print(f"WireMock mapping updated for CPF: {customer_data['user']['document']}")  # Debug print

        response = customer_registration_client.register_customer(customer_data=customer_data)

        return response
    
    yield _make_customer

    # Cleanup WireMock mappings after test
    if current_env == "local":
        wiremock_client.reset_mappings()