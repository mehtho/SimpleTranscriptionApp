import csv
from pathlib import Path

from elasticsearch import Elasticsearch, helpers

es = Elasticsearch("http://localhost:9200")

with Path.open("cv-valid-dev.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    actions = (
        {"_index": "cv-transcriptions", "_source": row}
        for row in reader
    )

    helpers.bulk(es, actions)
