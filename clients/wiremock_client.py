from config.settings import config
import requests


class WireMockClient:

    def __init__(self):
        self.base_url = config["wiremock_url"]
        self.session = requests.Session()

    def update_mappings(self, cpf: str = None):

        url = f"{self.base_url}/__admin/mappings"

        cpf_value = cpf or "99978004009"

        mapping_success = {
            "request": {
                "method": "POST",
                "urlPath": "/ext-application/v3/customer/registration",
                "bodyPatterns": [
                    {
                        "matchesJsonPath": f"$.user[?(@.document == '{cpf_value}')]",
                        "ignoreExtraElements": True,
                    }
                ],
            },
            "response": {
                "status": 201,
                "bodyFileName": "customer-acquisition/post-customer-acquisition-201.json",
                "headers": {"Content-Type": "application/json"},
            },
        }
        mapping_unsuccess = {
            "request": {
                "method": "POST",
                "urlPath": "/ext-application/v3/customer/registration",
                "bodyPatterns": [
                    {
                        "matchesJsonPath": "$.user[?(@.document == '12345678900')]",
                        "ignoreExtraElements": True,
                    }
                ],
            },
            "response": {
                "status": 400,
                "bodyFileName": "customer-acquisition/post-customer-acquisition-400-invalid-cpf.json",
                "headers": {"Content-Type": "application/json"},
            },
        }
        mapping_underage = {
            "request": {
                "method": "POST",
                "urlPath": "/ext-application/v3/customer/registration",
                "bodyPatterns": [
                    {
                        "matchesJsonPath": "$.user[?(@.document == '12345678911')]",
                        "ignoreExtraElements": True,
                    }
                ],
            },
            "response": {
                "status": 400,
                "bodyFileName": "customer-acquisition/post-customer-acquisition-400-under-age.json",
                "headers": {"Content-Type": "application/json"},
            },
        }

        if cpf_value == "12345678900":
            response = self.session.post(url, json=mapping_unsuccess)
            print(
                f"WireMock mapping update response for invalid CPF: {response.status_code}, {response.text}"
            )  # Debug print
        elif cpf_value == "12345678911":
            response = self.session.post(url, json=mapping_underage)
            print(
                f"WireMock mapping update response for underage birthdate: {response.status_code}, {response.text}"
            )  # Debug print
        else:
            response = self.session.post(url, json=mapping_success)
            print(
                f"WireMock mapping update response: {response.status_code}, {response.text}"
            )  # Debug print

    def reset_mappings(self) -> None:
        url = f"{self.base_url}/__admin/mappings/reset"
        response = self.session.post(url)
        print(
            f"WireMock mappings reset response: {response.status_code}, {response.text}"
        )  # Debug print
