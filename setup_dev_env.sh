###############################################################################
# Script to set up a development environment
#
# This script creates a heavy but fully loaded dev environment with all the
# tools needed to develop this project. A lighter version will be used to spin
# up demo environments.
###############################################################################

# Disable interactive prompts
sudo debconf-set-selections <<< "* libraries/restart-without-asking boolean true"

# Installs:
# - git and git-lfs           (To pull models and for dev work)
# - docker and docker compose (For containers)
(sudo apt-get update && \
    sudo apt-get install -y git git-lfs docker.io docker-compose-v2)

# Installs UV
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

# Downloads huggingface models
(mkdir -p models && \
    cd models && \
    git clone https://huggingface.co/facebook/wav2vec2-large-960h)

# Download the test dataset if it does not already exist
if [ ! -d "test_data" ]; then
  curl -L -o common_voice.zip "https://www.dropbox.com/scl/fi/i9yvfqpf7p8uye5o8k1sj/common_voice.zip?rlkey=lz3dtjuhekc3xw4jnoeoqy5yu&e=1&dl=1"
  unzip common_voice.zip -d test_data
else
  echo "Skipping download: test_data already exists"
fi

# Installs node js for search-ui
sudo curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

\. "$HOME/.nvm/nvm.sh"
nvm install 22

# Install yarn (node js package manager)
npm install --global yarn

# Install deps from requirements.txt to UV in the asr microservice directory
# By default, for development, installs test and inference dependencies
(cd asr && \
    uv sync --all-extras)

# Install linters dependencies
(cd linter && \
    uv sync)

# Install Azure CLI for demo deployments
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Install Terraform for demo deployments
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common
wget -O- https://apt.releases.hashicorp.com/gpg | \
  gpg --dearmor | \
  sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(grep -oP '(?<=UBUNTU_CODENAME=).*' /etc/os-release || lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

# Fixes issue with running elastic
sudo sysctl -w vm.max_map_count=262144

# Installs:
# - unzip     (for dataset)
# - ffmpeg    (for transcription)
# - terraform (for demo deployments)
(sudo apt-get update && \
    sudo apt-get install -y unzip ffmpeg terraform)
