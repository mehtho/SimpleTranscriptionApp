"""Contains MIME type enums for validation."""
from enum import Enum


class MimeTypes(str, Enum):
    """Mime Type enums."""

    MP3 = "audio/mpeg"
    WAV = "audio/wav"
