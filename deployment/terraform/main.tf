provider "azurerm" {
  features {}
}

terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.39.0"
    }
    local = {
      source  = "hashicorp/local"
      version = "2.5.3"
    }
    tls = {
      source  = "hashicorp/tls"
      version = "4.1.0"
    }
  }

  required_version = ">= 1.5.7"
}

resource "azurerm_resource_group" "rg" {
  name     = "${var.prefix}-rg"
  location = var.location
}

resource "tls_private_key" "ssh" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "local_file" "private_key" {
  content         = tls_private_key.ssh.private_key_pem
  filename        = "${path.module}/asr-demo-key.pem"
  file_permission = "0600"
}

resource "azurerm_linux_virtual_machine" "vm" {
  name                  = "${var.prefix}-vm"
  location              = azurerm_resource_group.rg.location
  resource_group_name   = azurerm_resource_group.rg.name
  size                  = "Standard_B4ms"
  admin_username        = var.admin_username
  network_interface_ids = [azurerm_network_interface.nic.id]

  disable_password_authentication = true

  admin_ssh_key {
    username   = var.admin_username
    public_key = tls_private_key.ssh.public_key_openssh
  }

  os_disk {
    name                 = "${var.prefix}-osdisk"
    caching              = "ReadWrite"
    storage_account_type = "Premium_LRS"
    disk_size_gb         = 512
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts-gen2"
    version   = "latest"
  }

  user_data = base64encode(<<-EOT
    #!/bin/bash
    debconf-set-selections <<< "* libraries/restart-without-asking boolean true"

    (apt-get update && \
      apt-get install -y git git-lfs docker.io docker-compose-v2 curl)
    
    git clone https://github.com/mehtho/SimpleTranscriptionApp.git
    cd SimpleTranscriptionApp
    git submodule update --init --recursive

    (mkdir -p models && \
      cd models && \
      git clone https://huggingface.co/facebook/wav2vec2-large-960h)

    sysctl -w vm.max_map_count=262144

    cp .env.example .env
    sed -i '/^SYS_PUBLIC_IP=/d' .env && echo "SYS_PUBLIC_IP=$(curl -s ifconfig.me)" >> .env

    touch /startup-complete
    docker compose pull
    docker compose up -d

  EOT
  )
}
