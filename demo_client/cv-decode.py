"""A demonstration test script that calls the ASR API."""
import csv
from pathlib import Path

import requests

IN_CSV = "../test_data/cv-valid-dev.csv"
TEMP_CSV = "./temp-cv-valid-dev.csv"

TEST_DATA_DIR = "../test_data/"
FILE_NAME_COL = "filename"

def call_api(audio_path: str, url: str = "http://localhost:8001/asr") -> str:
    """Call the asr API with the given audio file path."""
    with Path.open(audio_path, "rb") as f:
        files = {"file": (audio_path, f, "audio/mpeg")}
        resp = requests.post(url, files=files, timeout=60)
        resp.raise_for_status()

    return resp.json()["transcription"]

def main() -> None:
    """Read the input CSV, adding the generated_text col from calling the API."""
    try:
        with Path.open(IN_CSV, "r", newline="", encoding="utf-8") as file_in, \
            Path.open(TEMP_CSV, "w", newline="", encoding="utf-8") as file_out:

            reader = csv.DictReader(file_in)

            fieldnames = list(reader.fieldnames)
            if "generated_text" not in fieldnames:
                fieldnames.append("generated_text")

            writer = csv.DictWriter(file_out, fieldnames=fieldnames)
            writer.writeheader()

            for _, row in enumerate(reader, start=1):
                mp3_path = "cv-valid-dev/" + row.get(FILE_NAME_COL).strip()

                row["generated_text"] = call_api(TEST_DATA_DIR + mp3_path)
                writer.writerow(row)

            Path(TEMP_CSV).replace(IN_CSV)
    finally:
        Path.unlink(TEMP_CSV, missing_ok=True)

if __name__ == "__main__":
    main()
