import requests
from config.settings import config


class MenuClient:

    def __init__(self, token):
        self.base_url = config["base_url"]
        self.token = token

    def get_menu(self, customer_id, product_id):
        url = f"{self.base_url}/ext-application/v3/menu"

        headers = {
            "Authorization": f"Bearer {self.token}",
            "x-customer-id": customer_id,
            "x-product-id": str(product_id),
            "X-Tracking-Id": "3b65f0aca838a2b3708dd9ecc34ba701",
            "Accept-Language": "pt-BR",
            "X-ContextTracking-Id": "3b65f0aca838a2b3708dd9ecc34ba701",
            "X-Organization-Slug": "claro",
            "x-platform-version": "18.6",
            "x-tracking-source": "3b65f0aca838a2b3708dd9ecc34ba701",
            "traceparent": "00-3b65f0aca838a2b3708dd9ecc34ba701-95da64316175820c-01",
            "local-session-id": "127A1D8E-4FB8-435B-A990-84D921B878F3",
            "X-MSISDN": "5511913057825",
            "x-app-version": "7.71.01.7 (100)",
            "x-dynatrace": "MT_3_6_70037419794998505_400-0_9f9937fb-c8d2-4a46-bdbb-a1943d6bb80f_30_18027_651",
            "x-platform": "Android",
            "X-Uid": "77ea66c0-22ed-11f1-a979-7e5b736c6c2e",
            "X-Channel-Id": "6062f134-b4b1-41db-98ad-c3b289fed970",
            "deviceId": "9B892CC3-6AD5-42A5-A2D0-C9F588BC19CB",
            "x-rw-tracking-id": "3b65f0aca838a2b3708dd9ecc34ba701",
            "X-Application-Key": "5a5f9fa028ad013c2605000d3ac06d76",
            "X-Tracking-Source-Id": "3b65f0aca838a2b3708dd9ecc34ba701",
            "X-Application-Id": "ac76a7739985cdacad94eecd7f04ff64a97e0e93"
        }

        return requests.get(url, headers=headers)
