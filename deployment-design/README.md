# System Architecture Overview

This document explains the system design illustrated in the accompanying diagram.  
It describes the development workflow, deployment process, layers, and design decisions.  

---

## Workflow and Deployment

- **Development and CI/CD**  
  Developers push code commits to GitHub.  
  GitHub Actions automatically build container images and push them to **GitHub Container Registry (GHCR)**.  

- **Infrastructure Provisioning**  
  Developers use **Terraform** to provision a virtual machine (VM) on Microsoft Azure.  
  The VM startup script pulls prebuilt containers from GHCR and spins them up with Docker Compose.  

---

## Runtime Layers

- **Interface Layer**  
  - **ASR API** – Provides speech-to-text transcription.  
  - **Search UI** – React-based frontend for querying results.  
  - Both are exposed to users through the browser or API clients.  

- **Proxy Layer**  
  - Contains only the **Search UI proxy**.  
  - The proxy attaches a dynamically generated API key to requests before forwarding them to Elasticsearch.  
  - This ensures Elasticsearch is never directly exposed to the internet.
  - This can be extended to connect to authentication services

- **Data Layer**  
  - **Elasticsearch nodes (es01, es02)** – Work together by exchanging cluster state information for redundancy and fault tolerance.  
  - Store indexed transcription results and serve queries from the proxy layer.  

- **Ephemeral Setup Layer**  
  - **Uploader container** – Indexes a CSV file (`cv-valid-dev.csv`) into Elasticsearch automatically.  
  - **Elasticsearch setup container** – Initializes TLS certificates and security configurations for the cluster.  
  - These containers are short-lived and only run at startup.  

---

## Key Design Decisions

1. **Proxy Layer for Security**  
   - Directly exposing Elasticsearch is unsafe.  
   - Adding a proxy ensures API keys are injected server-side and allows for future integration with authentication services.  

2. **Containerized Deployment from GHCR**  
   - VMs automatically pull the latest containers from GHCR at startup.  
   - Simplifies demo setup and ensures consistency across environments.  

3. **Redundant Data Layer**  
   - Using two Elasticsearch nodes improves resilience by enabling state exchange and fault tolerance.  

---

This layered architecture separates concerns (interface, proxy, data, setup), improves security, and simplifies cloud demo deployment.
