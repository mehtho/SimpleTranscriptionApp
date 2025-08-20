"""Simple test for the ping endpoint."""
from http import HTTPStatus

from app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_ping() -> None:
    """Test with HTTP get on /ping endpoint."""
    response = client.get("/ping")
    assert response.status_code == HTTPStatus.OK
    assert "pong" in response.text

