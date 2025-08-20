# Installs UV. Restart terminal afterwards to apply changes.
curl -LsSf https://astral.sh/uv/install.sh | sh

# Downloads huggingface models
(mkdir -p models && \
    cd models && \
    git clone https://huggingface.co/facebook/wav2vec2-large-960h)

# Add the "unzip" program
(sudo apt-get update && \
    sudo apt-get install unzip ffmpeg)

# Download the test dataset if it does not already exist
if [ ! -d "test_data" ]; then
  curl -L -o common_voice.zip "https://www.dropbox.com/scl/fi/i9yvfqpf7p8uye5o8k1sj/common_voice.zip?rlkey=lz3dtjuhekc3xw4jnoeoqy5yu&e=1&dl=1"
  unzip common_voice.zip -d test_data
  rm common_voice.zip   # optional cleanup
else
  echo "Skipping download: test_data already exists"
fi

# Installs node js for search-ui
sudo curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

\. "$HOME/.nvm/nvm.sh"
nvm install 22

# Install deps from requirements.txt to UV in the asr microservice directory
# By default, for development, installs test and inference dependencies
(cd asr && \
    uv sync --all-extras)

# Install linters dependencies
(cd linter && \
    uv sync)
