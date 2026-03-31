import json
import os

ENV = os.getenv("ENV", "local").lower()

def load_config():
    path = f"config/environments/env.{ENV}.json"
    with open(path) as f:
        return json.load(f)

config = load_config()