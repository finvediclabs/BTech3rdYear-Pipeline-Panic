# Simulated Vault client
import os

def get_secret(key):
    # In real usage, fetch from Vault
    return os.getenv(key, "default_secret")
