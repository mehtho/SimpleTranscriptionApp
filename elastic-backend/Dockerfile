FROM ghcr.io/astral-sh/uv:alpine

WORKDIR /app

COPY pyproject.toml uv.lock* ./

COPY cv-index.py ./

# Do not copy over test deps
ENTRYPOINT [ "uv", "run", "cv-index.py" ]


