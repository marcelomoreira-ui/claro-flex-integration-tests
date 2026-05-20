import pytest
from clients.address_eligibility_client import AddressEligibilityClient
from clients.wiremock_client import WireMockClient
from mappings import address_eligibility_mappings
from config.settings import config

@pytest.fixture(scope="function")
def address_eligibility_response(auth_bff_data):

    wiremock_client = WireMockClient()
    current_env = config.get("ENV", "local").lower()
    
    def get_address_eligibility_response(cep: str, number: str, scenario: str) -> dict:

        if not cep or not number:
            raise ValueError("CEP and number parameters are required for address eligibility response fixture")
        
        address_eligibility_client = AddressEligibilityClient(auth_bff_data["token"])

        if current_env == "local":
            if scenario == "specific_zipcode":
                mapping = address_eligibility_mappings.get_specific_zipcode_mapping(cep, number)
            elif scenario == "generic_zipcode":
                mapping = address_eligibility_mappings.get_generic_zipcode_mapping(cep, number)
            elif scenario == "non_covered_zipcode":
                mapping = address_eligibility_mappings.get_unsuccess_mapping(cep, number)

        wiremock_client.create_mappings(mapping)

        response = address_eligibility_client.check_address_eligibility(cep, number)
        
        return response
    
    yield get_address_eligibility_response

    # Cleanup WireMock mappings after test
    if current_env == "local":
        wiremock_client.reset_mappings()