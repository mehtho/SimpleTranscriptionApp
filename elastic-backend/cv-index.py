import csv
import os
from pathlib import Path

from elasticsearch import Elasticsearch, helpers

api_key_path = Path("keys/api-key.txt")
api_key = None

# If API key already exists, read it
if api_key_path.exists() and api_key_path.stat().st_size > 0:
    api_key = api_key_path.read_text().strip()
else:
    # Use bootstrap password to create API key
    elastic_password = os.environ.get("ELASTIC_PASSWORD")
    if not elastic_password:
        raise RuntimeError("ELASTIC_PASSWORD environment variable not set")

    es_bootstrap = Elasticsearch(
        "https://es01:9200",
        basic_auth=("elastic", elastic_password),
        verify_certs=False,
        ssl_show_warn=False,
    )

    resp = es_bootstrap.security.create_api_key(name="search-ui-key", role_descriptors={})
    api_key = resp["encoded"]
    api_key_path.write_text(api_key)

# Reconnect using API key
es = Elasticsearch(
    "https://es01:9200",
    api_key=api_key,
    verify_certs=False,
    ssl_show_warn=False,
)

index_name = "cv-transcriptions"

if not es.indices.exists(index=index_name):
    with Path("cv-valid-dev.csv").open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        actions = ({"_index": index_name, "_source": row} for row in reader)
        helpers.bulk(es, actions)
