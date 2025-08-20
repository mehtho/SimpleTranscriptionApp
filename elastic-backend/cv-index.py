import csv
from pathlib import Path

from elasticsearch import Elasticsearch, helpers

es = Elasticsearch("http://es01:9200")

index_name = "cv-transcriptions"

# Only proceed if index does not exist
if not es.indices.exists(index=index_name):
    with Path("cv-valid-dev.csv").open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        actions = (
            {"_index": index_name, "_source": row}
            for row in reader
        )

        helpers.bulk(es, actions)
