# Minimal Dockerfile for backend
FROM python:3.13-slim

WORKDIR /app

# Create non-root user
RUN useradd --create-home --shell /bin/bash appuser

# Install uv and dependencies in virtual environment
RUN pip install uv
COPY requirements.txt ./
RUN uv venv /app/.venv && . /app/.venv/bin/activate && uv pip install --no-cache -r requirements.txt

# Copy application code
COPY . .

# Change ownership to appuser
RUN chown -R appuser:appuser /app

USER appuser

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
