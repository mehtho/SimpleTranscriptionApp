"""Configuration and classes for the Wav2Vec2 model."""
import io

import torch
import torchaudio
from enums.file_formats import MimeTypes
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

MODEL_PATH = "facebook/wav2vec2-large-960h"
SAMPLING_RATE = 16000 # 16 KHz sampling rate

class Wav2vec2:
    """Class containing Wav2Vec2 transcription functions."""

    def __init__(self) -> None:
        """Initialize models when class is instantiated."""
        self.processor = Wav2Vec2Processor.from_pretrained(MODEL_PATH)
        self.model = Wav2Vec2ForCTC.from_pretrained(MODEL_PATH)
        self.model.eval()

    def transcribe(self, audio_file: bytes, file_type:str) -> dict[str, str | float]:
        """Transcribes audio files from /asr endpoint.

        Receives audio_file bytes and the file extension to do appropriate
        conversions before transcribing.

        Will raise ValueError on unsupported file_type (MIME Type)
        """
        mime_type = MimeTypes(file_type)    # Raises ValueError for invalid MIME types
        audio_file_bytes = io.BytesIO(audio_file)

        # Load file into torchaudio with corresponding file type
        waveform, sr = torchaudio.load(audio_file_bytes, format="mp3"
                                       if mime_type == MimeTypes.MP3 else "wav")

        # Convert to audio to mono
        if waveform.shape[0] > 1:
            waveform = waveform.mean(dim=0, keepdim=True)

        # Enforces 16 KHz sampling rate on audio
        if sr != SAMPLING_RATE:
            waveform = torchaudio.functional.resample(waveform, sr, SAMPLING_RATE)

        # Formats input for model
        inputs = self.processor(
            waveform.squeeze().numpy(),
            sampling_rate=SAMPLING_RATE,
            return_tensors="pt",
            padding=True,
        )

        # Perform inference
        with torch.no_grad():
            logits = self.model(inputs.input_values).logits
            predicted_ids = torch.argmax(logits, dim=-1)
            transcription = self.processor.batch_decode(predicted_ids)[0]

            return {
                "transcription": transcription,
                "duration": waveform.shape[1] / SAMPLING_RATE,
            }
