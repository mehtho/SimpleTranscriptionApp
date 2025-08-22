# Public IP (from the load balancer's Public IP resource)
output "public_ip" {
  description = "Public IP to reach the VM via the LB"
  value       = azurerm_public_ip.lb_pip.ip_address
}

# Private IP of the VM NIC (inside the VNet)
output "private_ip" {
  description = "Private IP of the VM NIC"
  value       = azurerm_network_interface.nic.private_ip_address
}

# Convenience SSH command (adjust username if needed)
output "ssh_command" {
  description = "SSH via the LB public IP"
  value       = "ssh -i ./asr-demo-key.pem azureuser@${azurerm_public_ip.lb_pip.ip_address}"
}
