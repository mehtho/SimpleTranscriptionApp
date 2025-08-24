# SimpleTranscriptionApp

This repository contains a complete speech-to-text demonstration system with:
- Automatic speech recognition (ASR) with the wav2vec2-large-960h model
- 2-node Elasticsearch backend using TLS and API keys
- A frontend search application with a proxy layer over Elasticsearch

The aforementioned components are supported by
- Docker compose files to spin up the system locally
- Terraform IaC scripts to spin up the system on Azure
- GitHub Actions and GitHub Container Registry Integration
- The ruff linter

Link: `http://4.194.198.130:3000/`

---

## Components

- **ASR API (/asr)**  
  Provides an endpoint for speech-to-text transcription using the wav2vec2-large-960h model
  - Contains a demonstration client application that sends in 4076 audio files for transcription
  - Contains pytest end-to-end testing scripts

- **Elasticsearch Backend (/elastic-backend)**  
  Runs as a secured 2-node cluster with TLS enabled. Includes:  
  - An **uploader service** that indexes a transcript dataset (`cv-valid-dev.csv`) for demo purposes.  
  - Support for API keys or `elastic:elasticpassword` authentication.

- **Search UI (/search-ui, includes submodule from fork)**  
  A React-based frontend (forked from [`app-search-reference-ui-react`](https://github.com/mehtho/app-search-reference-ui-react)) for querying and visualizing indexed transcripts.
  This code was included through a submodule to avoid introducing a large amount of external code to the main codebase.
  Requests are routed through a proxy that appends API keys, so the frontend does not directly expose credentials.

- **Automation & Tooling**  
  - **Docker Integration** through Dockerfiles and docker-compose.yml files for containerized deployment
  - **Terraform (/deployment)** scripts for deploying the system on a VM with container images from GitHub Container Registry (GHCR)
  - **GitHub Actions (/.github/workflows)** workflow for building and publishing Docker images automatically
  - **Linters (/linter)** and configuration for enforcing code quality (`ruff`)

## Trying the Application
The system is deployed at
- `http://4.194.198.130:3000` for the Search UI (Use a browser)
- `http://4.194.198.130:8001/asr` for the ASR endpoint (Use the demo client in `asr/democlient` or `curl` commands)

## Running the Application yourself...
### Locally
Run `quickstart_local.sh` to quickly start a complete local deployment with docker-compose.

This assumes that docker is already installed on the machine.

Elasticsearch is exposed at `http://localhost:9200` for development or internal testing purposes

### Online
Use the terraform IaC scripts with your Microsoft Azure account by running the login and deploy scripts inside the `deployment` directory, which contains a second README with more detailed instructions.

Replace the IP addresses shown in the section above with the one shown by terraform to access your application instance.
Do note that for security reasons, port 9200 is never exposed to the open internet. However, it can be accessed directly when deployed locally.

### For Development
Run the `setup_dev_env.sh` script to download all dependencies on your local machine to enable development. This includes:

1. **git** – version control  
2. **git-lfs** – large file storage (for models/data)  
3. **Docker** – containerization  
4. **Docker Compose** – multi-container orchestration  
5. **UV** – Python package manager  
6. **Node.js (v22)** – runtime for search-ui  
7. **Yarn** – Node.js package manager  
8. **Python dependencies** – for ASR and linter services  
9. **Azure CLI** – for demo deployments  
10. **Terraform** – infrastructure as code (for demo deployments)  
11. **unzip** – dataset extraction  
12. **ffmpeg** – audio processing for transcription  
13. **Downloaded models and datasets** – for testing  
14. **Git submodules** – initializes search-ui and other project modules

## Directory Structure
```
.
├── asr/                      # ASR API service and demo client
├── elastic-backend/          # Elasticsearch cluster and uploader
├── search-ui/                # React frontend (submodule fork)
├── deployment/               # Terraform scripts for Azure deployment
├── linter/                   # Ruff linter configuration
├── demo-client/              # Simple ASR API test client
├── .github/workflows/        # GitHub Actions CI/CD definitions
│
├── .env.example              # An example .env file (Rename a copy to .env)
├── quickstart_local.sh       # Quickly sets up a local demo
├── setup_dev_env.sh          # Downloads dependencies needed for local development
├── dl_models_and_dataset.sh  # Downloads models and the common voice dataset
│
├── docker-compose.yml        # All-in-one local demo Compose
└── README.md                 # Top-level project overview
```
