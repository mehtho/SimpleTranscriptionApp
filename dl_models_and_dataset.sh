###############################################################################
# File download Script
#
# - Downloads Hugging Face models (Wav2Vec2) into ./models
# - Downloads and unpacks test dataset into ./test_data if not already present
###############################################################################

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
