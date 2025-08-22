# Script to log into Azure and export subscription ID

# Needed once per environment
az login
export ARM_SUBSCRIPTION_ID=$(az account show --query id -o tsv)
