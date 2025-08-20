FROM ghcr.io/astral-sh/uv:debian-slim AS builder

WORKDIR /app

COPY pyproject.toml uv.lock* ./

# Don't install testing deps
RUN uv sync --extra inference --frozen

COPY app/ .

FROM debian:bookworm-slim AS final

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv

CMD ["/app/.venv/bin/uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]
