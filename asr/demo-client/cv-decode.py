"""A demonstration test script that calls the ASR API."""
import csv
import logging
import sys
from pathlib import Path

import requests
from tqdm import tqdm

logger = logging.getLogger(__name__)

IN_CSV = "../../test_data/cv-valid-dev.csv"
TEMP_CSV = "./temp-cv-valid-dev.csv"

TEST_DATA_DIR = "../../test_data/"
FILE_NAME_COL = "filename"

NUM_MANDATORY_ARGS = 2

def call_api(audio_path: str, url: str) -> tuple[str, float]:
    """Call the ASR API with the given audio file path."""
    with Path.open(audio_path, "rb") as f:
        files = {"file": (audio_path, f, "audio/mpeg")}
        resp = requests.post(url, files=files, timeout=60)
        resp.raise_for_status()
        resp_json = resp.json()
    return resp_json["transcription"], resp_json["duration"]


def main(base_url: str) -> None:
    """Read the input CSV, adding the generated_text col from calling the API."""
    api_url = f"{base_url}/asr"

    try:
        total_rows = sum(1 for _ in Path.open(IN_CSV, encoding="utf-8")) - 1

        with Path.open(IN_CSV, "r", newline="", encoding="utf-8") as file_in, \
             Path.open(TEMP_CSV, "w", newline="", encoding="utf-8") as file_out:

            reader = csv.DictReader(file_in)
            fieldnames = list(reader.fieldnames)
            if "generated_text" not in fieldnames:
                fieldnames.append("generated_text")

            writer = csv.DictWriter(file_out, fieldnames=fieldnames)
            writer.writeheader()

            for row in tqdm(reader, total=total_rows, desc="Processing", unit="row"):
                mp3_path = "cv-valid-dev/" + row.get(FILE_NAME_COL).strip()
                row["generated_text"], row["duration"] = call_api(
                    TEST_DATA_DIR + mp3_path, api_url
                )
                writer.writerow(row)

            Path(TEMP_CSV).replace(IN_CSV)
    finally:
        Path.unlink(TEMP_CSV, missing_ok=True)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    if len(sys.argv) != NUM_MANDATORY_ARGS:
        logger.error("Usage: python cv-decode.py <BASE_URL>")
        logger.error("Example: python cv-decode.py http://localhost:8001")
        sys.exit(1)

    base_url = sys.argv[1].rstrip("/")
    logger.info("Starting test script with base URL: %s", base_url)
    main(base_url)
