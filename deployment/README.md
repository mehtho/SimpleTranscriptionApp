# Automatic Terraform Deployment

This directory contains the infrastructure-as-code files used to deploy the application with Terraform.

## Overview
The deployment process provisions a virtual machine, pulls the application’s container images from the GitHub Container Registry, and runs the root-level Docker Compose after downloading the required model files.  

Once complete, you can access:
- **Search UI**: `http://<VM_IP>:3000`
- **ASR API endpoint**: `http://<VM_IP>:8001`

For debugging or experimentation, you may also connect directly to the VM via SSH using the output command provided by Terraform.

## Usage
After installing terraform (e.g., from the development environment setup script), 
log into Azure with `login.sh`, and run the deployment with `deploy.sh`

## Contents
```
.
├── README.md
├── deploy.sh       # Convenience script to deploy after logging in
├── login.sh        # Convenience script to log in
└── terraform       # Terraform config for deployment
    ├── main.tf     # Contains startup script
    ├── network.tf  # Networking config
    ├── outputs.tf  # CLI output for debugging/connections (Not needed for simple use)
    └── vars.tf     # Configurable variables
```

## Notes on the load balancer
Although the project guidelines specify avoiding managed components, a load balancer is included.
This is required for compatibility with HTX’s Sandpit Azure environment, which does not allow VMs to have direct public IPs. The load balancer functions purely as a reverse proxy to enable access and does not provide any additional functionality.
