import pytest
from clients.address_eligibility_client import AddressEligibilityClient
from clients.auth_bff_client import AuthBFFClient

@pytest.fixture
def address_eligibility_response(auth_bff_data):
    
    def get_address_eligibility_response(cep: str, number: str) -> dict:

        if not cep or not number:
            raise ValueError("CEP and number parameters are required for address eligibility response fixture")
        
        address_eligibility_client = AddressEligibilityClient(auth_bff_data["token"])

        response = address_eligibility_client.check_address_eligibility(cep, number)
        
        return response
    
    return get_address_eligibility_response