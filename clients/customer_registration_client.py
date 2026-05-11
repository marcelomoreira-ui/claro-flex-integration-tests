import requests
from config.settings import config

class CustomerRegistrationClient:
    
    def __init__(self, token=None):
        self.base_url = config["base_url"]
        self.token = token

    def register_customer(self, customer_data: dict) -> requests.Response:
        url = f"{self.base_url}/ext-application/v3/customer/registration"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Organization-Slug": "claro",
            "X-Application-Key": "5a5f9fa028ad013c2605000d3ac06d76",
            "X-Tracking-Source-Id": "3b65f0aca838a2b3708dd9ecc34ba701",
            "X-Application-Id": "ac76a7739985cdacad94eecd7f04ff64a97e0e93"
        }
    
        response = requests.post(url, json=customer_data, headers=headers)
    
        return response