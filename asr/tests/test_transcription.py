"""Simple end-to-end test for the transcription endpoint."""
from http import HTTPStatus
from pathlib import Path

from app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_asr_simple() -> None:
    """Sends the short_audio.mp3 file to /asr endpoint to test transcription."""
    with Path.open("tests/short_audio.mp3", "rb") as f:
        response = client.post("/asr",
                               files={"file": ("short_audio.mp3", f, "audio/mpeg")})

    data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert "transcription" in data
    assert "duration" in data
