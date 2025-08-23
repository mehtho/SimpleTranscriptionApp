# Copy the .env file
cp .env.example .env

# Download models and test data
sh dl_models_and_dataset.sh

# Fixes issue with running elastic
sudo sysctl -w vm.max_map_count=262144

# Run the system
sudo docker compose pull
sudo docker compose up
