"""Main application entrypoint."""
from asr_api import router as asr_router
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping() -> str:
    """Return simple health check message."""
    return "pong"

# include the ASR routes
app.include_router(asr_router)
