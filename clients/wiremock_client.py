from config.settings import config
import requests


class WireMockClient:

    def __init__(self):
        self.base_url = config["wiremock_url"]
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def create_mappings(self, mapping_json: dict) -> None:
        """" Create WireMock mappings based on the provided mapping JSON. """

        url = f"{self.base_url}/__admin/mappings"

        response = self.session.post(url, json=mapping_json)

        response.raise_for_status()  # Raise an exception for HTTP errors

        return response

    def reset_mappings(self) -> None:
        url = f"{self.base_url}/__admin/mappings/reset"
        self.session.post(url)
