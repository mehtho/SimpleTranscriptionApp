variable "prefix" {
  description = "Resource name prefix"
  type        = string
  default     = "asr-demo"
}

variable "location" {
  description = "Closest region"
  type        = string
  default     = "Southeast Asia"
}

variable "admin_username" {
  description = "Admin username"
  type        = string
  default     = "azureuser"
}
