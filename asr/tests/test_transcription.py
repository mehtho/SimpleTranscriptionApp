from app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_asr_simple():
    with open("tests/short_audio.mp3", "rb") as f:
        response = client.post("/asr", files={"file": ("short_audio.mp3", f, "audio/mpeg")})
    assert response.status_code == 200
    data = response.json()
    assert "transcription" in data
    assert "duration" in data
