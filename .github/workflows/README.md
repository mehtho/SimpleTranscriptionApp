# GitHub Actions Workflow

This directory contains a single workflow definition that automates container builds and publishing.

## Overview
The workflow:
1. Builds the following containers:
   - **ASR API**
   - **Uploader** (`cv-index.py`)
   - **Search UI**
2. Publishes the built images to the **GitHub Container Registry (GHCR)**.

## Purpose
By pre-building and publishing containers, the Terraform deployment is simplified:
- The VM does **not** need to install development dependencies or build containers at runtime.
- Startup time is significantly reduced, since the VM only needs to:
  1. Connect to GHCR,
  2. Pull the published images,
  3. Run the root-level Docker Compose.

This separation makes the VM faster to instantiate, and prevents us from having to maintain a separate set of deployment environment dependencies since the containers are all-inclusive.
