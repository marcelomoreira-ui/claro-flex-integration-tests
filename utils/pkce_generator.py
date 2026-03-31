import base64
import hashlib
import os

def generate_pkce():
    code_verifier = base64.urlsafe_b64encode(os.urandom(40)).decode().rstrip("=")
    
    code_challenge = base64.urlsafe_b64encode(
        hashlib.sha256(code_verifier.encode()).digest()
    ).decode().rstrip("=")

    return code_verifier, code_challenge