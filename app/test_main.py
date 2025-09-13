import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    # Flaky test: sometimes fails
    assert response.status_code == 200
    assert response.json()["message"] in ["Hello from Dev!", "Hello from CI!"]

# Simulate a broken test
@pytest.mark.parametrize("env", ["dev", "ci", "prod"])
def test_env_mismatch(monkeypatch, env):
    monkeypatch.setenv("APP_ENV", env)
    response = client.get("/")
    # Bug: prod is not handled in main.py
    assert response.status_code == 200
