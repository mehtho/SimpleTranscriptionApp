import io

import torch
import torchaudio
from enums.file_formats import MimeTypes
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

MODEL_ID = "facebook/wav2vec2-large-960h"
SAMPLING_RATE = 16000 # 16 KHz sampling rate

class Wav2vec2:
    def __init__(self):
        self.processor = Wav2Vec2Processor.from_pretrained(MODEL_ID)
        self.model = Wav2Vec2ForCTC.from_pretrained(MODEL_ID)
        self.model.eval()

    def transcribe(self, audio_file: bytes, file_type:str) -> dict[str, str | float]:
        mime_type = MimeTypes(file_type)
        audio_file_bytes = io.BytesIO(audio_file)

        # torchaudio can read from in-memory buffer
        waveform, sr = torchaudio.load(audio_file_bytes, format="mp3" if mime_type == MimeTypes.MP3 else "wav")

        # mono
        if waveform.shape[0] > 1:
            waveform = waveform.mean(dim=0, keepdim=True)

        # resample
        if sr != SAMPLING_RATE:
            waveform = torchaudio.functional.resample(waveform, sr, SAMPLING_RATE)

        # prepare for model
        inputs = self.processor(
            waveform.squeeze().numpy(),
            sampling_rate=SAMPLING_RATE,
            return_tensors="pt",
            padding=True,
        )

        with torch.no_grad():
            logits = self.model(inputs.input_values).logits
            predicted_ids = torch.argmax(logits, dim=-1)

        return {
            "transcription": self.processor.batch_decode(predicted_ids)[0],
            "duration": waveform.shape[1] / SAMPLING_RATE,
            }
