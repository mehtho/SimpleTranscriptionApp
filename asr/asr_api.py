from fastapi import APIRouter, File, UploadFile
from inference.wav2vec2 import Wav2vec2

router = APIRouter()

asr_model = Wav2vec2()

@router.post("/asr")
async def asr(file: UploadFile = File(...)) -> dict[str, str | float]:
    # Assumes MP3 for now
    return asr_model.transcribe(await file.read(), file.content_type)
