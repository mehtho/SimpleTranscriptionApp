# Deploys a full instance on Azure to demo. (Used to deploy submitted demo)

# Important: Run login.sh before running this script

# Matt: I've tried to replicate how I got around Sandpit's restrictions,

#   (VM's are not allowed to have public-facing IPs and must be behind a
#   load balancer) and therefore added a load balancer, although it is
#   a managed component.

#   It's just there to make it easier to replicate and try yourself.

cd terraform

export ARM_SUBSCRIPTION_ID=$(az account show --query id -o tsv)
terraform init && \
    terraform apply --auto-approve



