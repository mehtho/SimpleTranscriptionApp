# Installs UV. Restart terminal afterwards to apply changes.
curl -LsSf https://astral.sh/uv/install.sh | sh

# Downloads huggingface models
(mkdir -p models && \
    cd models && \
    git clone https://huggingface.co/facebook/wav2vec2-large-960h)

# Install deps from requirements.txt to UV in the asr directory
(cd asr && \
    uv add -r requirements.txt && \
    uv sync)

# Install ruff
(cd linters && \
    uv sync)
