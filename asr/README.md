# Automatic Speech Recognition (ASR) Microservice

2a: Uses the wav2vec2-large-960h and resamples audio to 16KHz.

## Endpoints

- **Ping API**  
  2b: `GET /ping` → Returns `pong` as a healthcheck endpoint

- **ASR Inference API**  
  2c: `POST /asr` (multipart/form-data with `file` parameter), returns:
  - `transcription`: Transcribed text
  - `duration`: Audio duration in seconds

## Demo Client
2d: Uses the downloaded Common Voice dataset to generate transcribed text from
    the API into a new column in `cv-valid-dev.csv`

## Containerization
2e: Includes a Dockerfile for the `asr-api` service. Running this API involves converting audio formats in-memory, and demo-client destroys temp files it creates.

## Usage
- `sudo docker compose up --build` to create the ASR service
- `./run_client.sh` to run the transcription client that transcribes 4076 audio files in the Common Voice dataset against a given IP address (See script for details)
- `./run_tests.sh` to run a local end to end test
- `./demo_curl_script.sh` to use `curl` for a quick demonstration

## File Structure
```
.
├── Dockerfile                      # Dockerfile for asr-api
├── README.md                       # This file
├── /app                            # The asr-api app code
├── /demo-client                    # Demo client code
├── docker-compose.yml              # Docker compose to demo the asr-api
│
├── pyproject.toml                  # [Important] Package Information, replaces requirements.txt
├── requirements.txt                # Backup package information (Unused)
├── uv.lock                         
│
├── pytest.ini                      # End to end testing configuration
│
├── run_client.sh                   # Runs the demo-client app that transcribes 4076 audio files from Common Voice
└── run_tests.sh                    # Runs local end to end tests    
```
