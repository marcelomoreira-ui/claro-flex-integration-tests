import requests
from config.settings import config


class AddressEligibilityClient:
    
    def __init__(self, token):
        self.base_url = config["base_url"]
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def check_address_eligibility(self, cep: str, number: str) -> dict:

        url = f"{self.base_url}/flexbff/v1/customers/elegibilities"

        payload = {
            "postalCode": cep, 
            "number": number, 
            "page": 1, 
            "limit": 100
            }

        response = requests.post(url, headers=self.headers, json=payload)

        if response.status_code in [200, 201, 400]:
            return response
        else:
            raise Exception(
                f"Failed to check address eligibility: {response.status_code} - {response.text}"
            )