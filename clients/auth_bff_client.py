import requests
from config.settings import config

class AuthBFFClient:
    def __init__(self):
        self.base_url = config["auth_bff_url"]

    def get_access_token(self):

        url = f"{self.base_url}/flexbff/v1/oauth2/tokens"

        headers = {
            "Authorization": config["auth_bff_basic_token"],
            "Content-Type": "application/x-www-form-urlencoded"
        }

        payload = {
            "grant_type": "client_credentials"
        }
        
        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            print("Access token obtained successfully")
            return response.json().get("access_token")
        else:
            raise Exception(f"Failed to get access token: {response.status_code} - {response.text}")