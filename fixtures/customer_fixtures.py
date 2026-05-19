import pytest
from clients.customer_client import CustomerClient
from builders.customer_builder import CustomerBuilder
from config.settings import config
from clients.wiremock_client import WireMockClient
from mappings import customer_mappings as cm

@pytest.fixture(scope="function")
def customer_registration_response():

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
        
        if current_env == "local":
            if invalid_cpf:
                mapping = cm.get_unsuccess_mapping()
            elif underage_birthdate:
                mapping = cm.get_underage_mapping()
            else:
                mapping = cm.get_success_mapping(cpf=customer_data["user"]["document"])

            wiremock_client.create_mappings(mapping)

        response = customer_registration_client.register_customer(customer_data=customer_data)

        return response
    
    yield _make_customer

    # Cleanup WireMock mappings after test
    if current_env == "local":
        wiremock_client.reset_mappings()