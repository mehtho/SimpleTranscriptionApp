# Elastic Backend

This directory contains an Elasticsearch backend that runs on `https://localhost:9200` with TLS enabled and authentication configured.  

Run it with the provided `run_backend.sh` script. This script resets any stale keys and starts the backend fresh using Docker Compose.  

---

## Docker Compose Components
1. **Elasticsearch Cluster** – A 2-node cluster (`es01`, `es02`) with TLS enabled  
2. **Setup Service** – One-time job that generates CA and node certificates  
3. **Uploader** – Uploads a transcript results CSV (`cv-valid-dev.csv`) and writes a demo API key into `./keys/api-key.txt` (host-visible)  

---

## Authentication

You can authenticate with Elasticsearch using either of these methods:

**1. API Key** (recommended)  

`curl -k -H "Authorization: ApiKey <Key>" https://localhost:9200/`

**2. Basic Auth**

`curl -k -u elastic:elasticpassword https://localhost:9200/`

---

## Contents
```
.
├── Dockerfile              # Dockerfile for the uploader (cv-index.py)
├── README.md
├── config
│   └── elasticsearch.yml   # Elastic search config file
├── cv-index.py             # Indexes cv-valid-dev.csv in the elastic search instance
├── cv-valid-dev.csv        # Transcription results
├── docker-compose.yml      # Backend-only docker compose
├── pyproject.toml          # Dependencies for the uploader
├── run_backend.sh          # Runs the Backend-only docker compose
└── uv.lock
```
