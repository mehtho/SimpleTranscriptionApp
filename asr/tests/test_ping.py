from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert "pong" in response.text

