# Search UI

This directory hosts a [forked submodule](https://github.com/mehtho/app-search-reference-ui-react) of the **App Search Reference UI** application, configured to work with the Elasticsearch backend and uploader service in this project.

## Architecture

The Search UI is designed to interact securely with the Elasticsearch backend:

1. **Backend setup**  
   - A setup container generates TLS certificates and initializes the cluster.  
   - Once Elasticsearch is running, the uploader service loads data and writes API credentials.

2. **Search UI components**  
   - **Frontend**: A React-based interface that users interact with.  
   - **Proxy**: A lightweight server that handles requests to Elasticsearch.  
     - The proxy attaches an Elasticsearch API key to requests, preventing the frontend from storing or exposing the key.  
     - This enables port `9200` to be closed, ensuring Elasticsearch is never directly exposed to the internet.

3. **AuthN integration (Future Work)**  
   - When combined with an authentication service, the frontend can require login and securely delegate token handling.  
   - This results in a setup where authentication and authorization are managed by a dedicated service, further reducing risk.

## Usage

- Access the Search UI at:  
  - `http://localhost:3000` (local development)  
  - `http://<PUBLIC_IP>:3000` (remote deployment, e.g., via Terraform)

- Searchable fields:  
  - `generated_text`  
  - `duration`  
  - `age`  
  - `gender`  
  - `accent`  

## Contents
```
.
├── Dockerfile
├── README.md
├── run_searchui.sh         # Convenience script to pull the submodule and run the setup
├── app                     # Submodule located here
└── docker-compose.yml      # Docker compose for search-ui app
```