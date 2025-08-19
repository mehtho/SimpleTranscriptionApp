"""Contains the asr transcription endpoint."""
from typing import Annotated

from fastapi import APIRouter, File, UploadFile
from inference.wav2vec2 import Wav2vec2

router = APIRouter()

asr_model = Wav2vec2()

@router.post("/asr")
async def asr(file: Annotated[UploadFile, File()] = ...) -> dict[str, str | float]:
    """Call the transcription function.

    Returns a json response based on the returned dict
    """
    return asr_model.transcribe(await file.read())
