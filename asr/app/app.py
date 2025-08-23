"""Main application entrypoint."""
from asr_api import router as asr_router
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping() -> str:
    """Return simple health check message."""
    return "pong"

# Include the transcription routes in asr_api.py
app.include_router(asr_router)
