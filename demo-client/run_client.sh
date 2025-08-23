###############################################################################
# Demo Client
#
# Runs the cv-decode.py script against an ASR API instance.
# Usage:
#   ./demo-client.sh http://hostname:port
# Defaults to http://localhost:8001 if no argument is provided.
###############################################################################

uv sync
uv run python cv-decode.py "${1:-http://localhost:8001}"
