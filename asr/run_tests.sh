###############################################################################
# Test Runner
#
# Runs all pytest tests with extras (transcription and test libs) enabled.
# NOTE: Requires ffmpeg to be installed in the test environment.
###############################################################################

uv run --all-extras pytest
