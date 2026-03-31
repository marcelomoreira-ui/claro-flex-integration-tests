📄 README.md
# Claro Flex - Integration Tests

Projeto de automação de testes de integração para a nova plataforma Claro Flex.

## 📌 Objetivo

Garantir a qualidade das APIs através de:

- Validação de status codes
- Validação de contrato (schema)
- Testes baseados em fluxos reais (Auth + APIs)
- Suporte a múltiplos ambientes (local, SIT, sanity)

---

## 🧱 Estrutura do Projeto


.
├── config/ # Configurações e ambientes
├── fixtures/ # Fixtures do pytest (auth, dados, schemas)
├── clients/ # Clients para chamadas de API
├── utils/ # Utilitários (PKCE, helpers, etc)
├── tests/ # Casos de teste
├── pytest.ini # Configuração do pytest
├── conftest.py # Registro global de fixtures
└── requirements.txt # Dependências do projeto


---

## ⚙️ Pré-requisitos

- Python 3.9+
- pip
- Virtualenv

---

## 🚀 Setup do Projeto

### 1. Criar ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate  # Linux / Mac
2. Instalar dependências
pip install -r requirements.txt
🌍 Configuração de Ambiente

Os ambientes estão em:

config/environments/

Exemplos:

env.local.json
env.sit.json
env.sanity.json

Selecione o ambiente via variável:

export ENV=sit
▶️ Execução dos Testes
pytest -m integration

Ou usando script:

./run.sh
🔐 Autenticação

O projeto implementa fluxo completo de autenticação com:

PKCE
PingFederate
Token dinâmico

O token é gerado automaticamente via fixture.

🧪 Tipos de Teste
✔ Status Code

Valida retorno esperado da API.

✔ Contract / Schema

Validação de estrutura da resposta utilizando jsonschema.

👥 Testes com múltiplos usuários

Usuários de teste ficam em:

config/test_users.py

Permite simular diferentes cenários de negócio.

🧠 Boas práticas adotadas
Uso de fixtures do pytest
Separação por responsabilidade (clients, utils, tests)
Configuração por ambiente
Reuso de autenticação
Código desacoplado e escalável
⚠️ Segurança
Credenciais NÃO devem ser versionadas
Arquivos sensíveis estão no .gitignore