"""Tests for the API endpoints."""

import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """Create a test client."""
    with TestClient(app) as c:
        yield c


def test_root(client):
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert "API 2026" in response.json()["message"]


def test_health(client):
    """Test health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_api_v1_test(client):
    """Test API v1 test endpoint."""
    response = client.get("/api/v1/test/test")
    assert response.status_code == 200
    assert "API v1 is working" in response.json()["message"]
