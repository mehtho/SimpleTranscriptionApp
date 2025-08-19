from fastapi import APIRouter, File, UploadFile

router = APIRouter()

@router.post("/asr")
async def asr(file: UploadFile = File(...)):
    # TODO(Matt): Add calls to inference here
    return {"transcription": "TODO", "duration": 10}
