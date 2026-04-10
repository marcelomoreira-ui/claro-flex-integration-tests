import requests
from config.settings import config
from utils.pkce_generator import generate_pkce
from utils.logger import get_logger

class AuthClient:

    logger = get_logger(__name__)

    def __init__(self):
        self.session = requests.Session()
        self.base_auth = config["auth_url"]

    def get_token(self,username=None, password=None):

        username = username or config["username"]
        password = password or config["password"]

        #Limpa os cookies antes de iniciar o processo de autenticação
        self.logger.info(" ")
        self.logger.info("🔐 Starting authentication process")
        self.session.cookies.clear()

        code_verifier, code_challenge = generate_pkce()

        # Step 1 - Flow ID
        url = f"{self.base_auth}/as/authorization.oauth2"

        params = {
            "client_id": config["client_id"],
            "response_type": "code",
            "response_mode": "pi.flow",
            "scope": "openid flex",
            "nonce": "abc123",
            "authMs": "UP,EP,DOCP",
            "code_challenge": code_challenge,
            "code_challenge_method": "S256"
        }

        response = self.session.get(url, params=params)

        if response.status_code != 200:
            self.logger.error("❌ Failed to initiate authentication flow for user '%s'", username)
            self.logger.error("Status: %d", response.status_code)
            self.logger.error("Response: %s", response.text)
            return []


        flow_id = response.json()["id"]

        # DEBUG (adicione isso)
        self.logger.debug("Cookies: %s", self.session.cookies.get_dict())

        # Step 2 - Authorization Code
        url = f"{self.base_auth}/pf-ws/authn/flows/{flow_id}"

        payload = {
            "username": username,
            "password": password
        }

        headers = {
            "Content-Type": "application/vnd.pingidentity.checkUsernamePassword+json",
            "X-XSRF-Header": "PingFederate"
        }

        response = self.session.post(url, json=payload, headers=headers)

        if response.status_code != 200:
            self.logger.error("❌ Authentication failed for user '%s'", username)
            self.logger.error("Status: %d", response.status_code)
            self.logger.error("Response: %s", response.text)
            return []
    

        self.logger.debug("✔ Authorization Code")

        code = response.json()["authorizeResponse"]["code"]

        # Step 3 - Exchange for token
        url = f"{config['base_url']}/rw-middleware/v4/auth"

        payload = {
            "credentialType": "AUTH_CODE_CREDENTIALS",
            "credentials": code,
            "codeVerify": code_verifier
        }

        headers = {
            "x-application-id": "ac76a7739985cdacad94eecd7f04ff64a97e0e93",
            "x-application-key": "5a5f9fa028ad013c2605000d3ac06d76",
            "x-organization-slug": "claro",
            "x-platform": "Android",
            "x-channel-id": "6062f134-b4b1-41db-98ad-c3b289fed970",
            "x-app-version": "6.40.99",
            "X-Tracking-Id": "test-tracking-id",
            "no-auth-flex": "true",
            "Content-Type": "application/json",
            "X-XSRF-Header": "PingFederate"
        }

        response = self.session.post(url, json=payload, headers=headers)

        if response.status_code != 200:
            self.logger.error("❌ Token exchange failed for user '%s'", username)
            self.logger.error("Status: %d", response.status_code)
            self.logger.error("Response: %s", response.text)
            return []

        token = response.headers.get("x-access-token")

        content = response.json()["content"]

        return {
            "token": token,
            "customer_id": content["customer"]["id"],
            "product_id": content["products"][0]["id"]
        }