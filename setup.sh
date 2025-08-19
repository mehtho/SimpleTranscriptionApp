# Installs UV. Restart terminal afterwards to apply changes.
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install deps from requirements.txt to UV in the asr directory
cd asr && uv add -r requirements.txt && uv sync
