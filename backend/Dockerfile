# Stage 1: Builder
FROM python:3.13-slim as builder

WORKDIR /app
RUN pip install uv
COPY requirements.txt ./
RUN uv pip install --system --no-cache -r requirements.txt

# Stage 2: Runtime minimal
FROM python:3.13-slim

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .

RUN adduser --disabled-password --gecos '' appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
