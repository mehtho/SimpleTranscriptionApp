FROM ghcr.io/astral-sh/uv:debian-slim AS builder

WORKDIR /app

COPY pyproject.toml uv.lock* ./

# Do not copy over test deps
RUN uv sync --extra inference --locked --no-cache

FROM ghcr.io/astral-sh/uv:debian-slim AS final

WORKDIR /app

# Copy only code and .venv
COPY --from=builder /app/.venv /app/.venv
COPY app/ ./

# Install ffmpeg
# Could be done in builder, but links break when copying
# Try fixing with: https://github.com/jrottenberg/ffmpeg/issues/99#issuecomment-396659630
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*

RUN uv venv --allow-existing

ENTRYPOINT ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]
