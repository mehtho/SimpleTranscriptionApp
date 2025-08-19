# Installs UV. Restart terminal afterwards to apply changes.
curl -LsSf https://astral.sh/uv/install.sh | sh

# Downloads huggingface models
(mkdir -p models && \
    cd models && \
    git clone https://huggingface.co/facebook/wav2vec2-large-960h)

# Add the "unzip" program
(sudo apt-get update && \
    sudo apt-get install unzip)

# Download the test dataset
curl -L -o common_voice.zip "https://www.dropbox.com/scl/fi/i9yvfqpf7p8uye5o8k1sj/common_voice.zip?rlkey=lz3dtjuhekc3xw4jnoeoqy5yu&e=1&dl=1"
unzip common_voice.zip -d test_data
# rm common_voice.zip

# Install deps from requirements.txt to UV in the asr microservice directory
(cd asr && \
    uv sync --extra testing)

# Install linters dependencies
(cd linter && \
    uv sync)
