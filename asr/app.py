from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/ping")
def ping():
    return "pong"

@app.post("/asr")
async def asr(file: UploadFile = File(...)):
    return {"transcription": "TODO", "duration": 10}
