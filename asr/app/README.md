# asr-api application code
```
.
├── README.md                   # This file
├── app.py                      # Main app file with ping endpoint
├── asr_api.py                  # Inference endpoint for transcription
├── inference
│   ├── __init__.py
│   └── wav2vec2.py             # Inference logic
└── tests
    ├── __init__.py
    ├── short_audio.mp3         # Short test audio from Common Voice
    ├── test_ping.py            # Tests the ping endpoint
    └── test_transcription.py   # Tests the transcription endpoint
```
