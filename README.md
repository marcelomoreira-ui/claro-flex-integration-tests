📄 README.md
# Claro Flex Integration Tests

Automated integration test suite for Claro Flex platform APIs.

This project validates authentication flow (OAuth + PKCE), API responses, and contract/schema using Python and pytest.

---

## 🚀 Tech Stack

- Python 3.x
- Pytest
- Requests
- JSONSchema (contract validation)

---

## 📁 Project Structure


claro-flex-integration-tests/
│
├── config/ # Environment configurations
├── fixtures/ # Pytest fixtures (auth, test data)
├── clients/ # API clients (auth, menu, etc.)
├── utils/ # Helpers (PKCE, request utils)
├── tests/ # Test cases
│
├── pytest.ini
├── conftest.py
└── requirements.txt


---

## ⚙️ Environment Configuration

Tests support multiple environments:

- `local`
- `sit`
- `sanity`

Each environment must have its own config file:


config/environments/env.<env>.json


Example:

```json
{
  "base_url": "",
  "auth_url": "",
  "client_id": "",
  "username": "",
  "password": ""
}

⚠️ Do not commit real credentials

▶️ Running Tests
1. Create virtual environment
python3 -m venv venv
source venv/bin/activate
2. Install dependencies
pip install -r requirements.txt
3. Set environment
export ENV=sit
4. Run tests
pytest -m integration -v
🔐 Authentication Flow

The project implements OAuth with PKCE:

Generate PKCE (code_verifier / code_challenge)
Retrieve flowId
Authenticate user (username/password)
Exchange authorization code for access token

Token is reused via pytest fixtures.

🧪 Test Strategy

Tests are organized into:

Status validation (HTTP responses)
Contract validation (JSON schema)
Functional scenarios (based on user profiles)
👥 Test Data Strategy
Default user from environment config
Multiple user profiles supported via fixtures
Dynamic data retrieved from authentication flow
📌 Best Practices
Avoid hardcoded test data
Use fixtures for shared setup
Keep tests independent
Validate only relevant fields in schema
Never commit sensitive data
🚀 Future Improvements
Token caching and refresh
CI/CD pipeline integration
Parallel test execution
Contract testing with Pact
Test reporting (Allure)
🤝 Contributing
Create a new branch
Implement tests following project patterns
Run tests locally
Submit pull request
📄 License

Internal use only