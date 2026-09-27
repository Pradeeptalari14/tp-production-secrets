#!/usr/bin/env python3
"""
Dynamic Credentials Access Python SDK Wrapper
Connects to HashiCorp Vault via HVAC with automated token handling
"""
import os
from typing import Dict, Any

try:
    import hvac
    HAS_HVAC = True
except ImportError:
    HAS_HVAC = False

def get_database_credentials() -> Dict[str, Any]:
    if not HAS_HVAC:
        return {"username": "v-token-readonly-mock", "password": "vault-ephemeral-pass-3948"}

    vault_addr = os.environ.get("VAULT_ADDR", "https://vault.production.local:8200")
    client = hvac.Client(url=vault_addr)
    
    sa_token_path = "/var/run/secrets/kubernetes.io/serviceaccount/token"
    if os.path.exists(sa_token_path):
        with open(sa_token_path, "r") as f:
            jwt = f.read().strip()
        client.auth.kubernetes.login(role="production-app", jwt=jwt)
    elif os.environ.get("VAULT_TOKEN"):
        client.token = os.environ["VAULT_TOKEN"]

    response = client.secrets.database.generate_credentials(name="readonly")
    return {
        "username": response["data"]["username"],
        "password": response["data"]["password"]
    }

if __name__ == "__main__":
    creds = get_database_credentials()
    print(f"Acquired dynamic DB credentials for user: {creds['username']}")
