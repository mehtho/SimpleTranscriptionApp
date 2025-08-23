###############################################################################
# Cleans up stale API keys before running docker compose
#
# This backend-only demo creates a keys directory for API key testing.
# It must be removed before each run from this directory, or it will cause
# API key issues.
###############################################################################

[ -d "./keys" ] && sudo rm -rf ./keys
sudo docker compose up
