from fastapi import FastAPI
from asr_api import router as asr_router

app = FastAPI()

@app.get("/ping")
def ping():
    return "pong"

# include the ASR routes
app.include_router(asr_router)
