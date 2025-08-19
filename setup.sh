# Installs UV. Restart terminal afterwards to apply changes.
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install deps from requirements.txt to UV in the asr directory
cd asr && uv add -r requirements.txt && uv sync

mkdir -p models && cd models && git clone https://huggingface.co/facebook/wav2vec2-large-960h
