import requests
from config.settings import config


class AddressEligibilityClient:
    def __init__(self, token):
        self.base_url = config["base_url"]
        print(f"Auth BFF URL: {self.base_url}")  # Debugging line to check the URL being used
        self.token = token

    def check_address_eligibility(self, cep: str, number: str) -> dict:
        url = f"{self.base_url}/flexbff/v1/customers/elegibilities"

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

        payload = {
            "postalCode": cep, 
            "number": number, 
            "page": 1, 
            "limit": 100
            }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code in [200, 201, 400]:
            return response
        else:
            raise Exception(
                f"Failed to check address eligibility: {response.status_code} - {response.text}"
            )
