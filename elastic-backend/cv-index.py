import base64
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
        http_auth=("elastic", elastic_password),
        verify_certs=False,
        ssl_show_warn=False,
    )

    resp = es_bootstrap.security.create_api_key(body={
        "name": "search-ui-key",
        "role_descriptors": {}
    })

    # Build base64-encoded id:api_key string
    raw = f"{resp['id']}:{resp['api_key']}"
    api_key = base64.b64encode(raw.encode()).decode()

    api_key_path.write_text(api_key)

# Reconnect using base64 API key
es = Elasticsearch(
    "https://es01:9200",
    api_key=api_key,
    verify_certs=False,
    ssl_show_warn=False,
)

index_name = "cv-transcriptions"

# Define explicit mapping
mapping = {
    "mappings": {
        "properties": {
            "generated_text": {"type": "text"},
            "age": {"type": "keyword"},
            "gender": {"type": "keyword"},
            "accent": {"type": "keyword"},
            "duration": {"type": "float"}
        }
    }
}

# Drop old index if it exists
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)

# Create new index with mapping
es.indices.create(index=index_name, body=mapping)

# Bulk insert CSV rows with proper type conversion
with Path("cv-valid-dev.csv").open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    actions = []
    for row in reader:
        # Ensure duration is numeric
        if "duration" in row and row["duration"] != "":
            try:
                row["duration"] = float(row["duration"])
            except ValueError:
                row["duration"] = None
        actions.append({"_index": index_name, "_source": row})

    if actions:
        helpers.bulk(es, actions)
