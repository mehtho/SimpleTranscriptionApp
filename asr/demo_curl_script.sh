# Demo: Send an audio file to the ASR API for transcription
curl -X POST \
  -F "file=@../test_data/cv-other-test/cv-other-test/sample-000000.mp3" \
  http://localhost:8001/asr
