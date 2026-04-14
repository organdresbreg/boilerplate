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


class TestConfig:
    """Tests para configuración del sistema."""

    def test_secret_key_generation(self):
        """SECRET_KEY se genera automáticamente si está vacía."""
        from app.core.config import _generate_secret_key
        
        key1 = _generate_secret_key()
        key2 = _generate_secret_key()
        
        assert len(key1) == 43  # token_urlsafe(32) produce 43 chars
        assert key1 != key2  # Cada generación es única
        assert isinstance(key1, str)

    def test_parse_cors_origins_json(self):
        """Parsea correctamente formato JSON."""
        from app.core.config import _parse_cors_origins
        
        json_input = '["https://dominio.com", "https://otro.com"]'
        result = _parse_cors_origins(json_input)
        
        assert result == ["https://dominio.com", "https://otro.com"]
        assert isinstance(result, list)

    def test_parse_cors_origins_comma_separated(self):
        """Parsea correctamente formato comma-separated."""
        from app.core.config import _parse_cors_origins
        
        csv_input = "https://dom1.com,https://dom2.com, https://dom3.com"
        result = _parse_cors_origins(csv_input)
        
        assert result == ["https://dom1.com", "https://dom2.com", "https://dom3.com"]

    def test_parse_cors_origins_empty(self):
        """Retorna lista vacía para input vacío."""
        from app.core.config import _parse_cors_origins
        
        assert _parse_cors_origins("") == []
        assert _parse_cors_origins(None) == []

    def test_parse_cors_origins_invalid_json_fallback(self):
        """Fallback a comma-separated si JSON es inválido."""
        from app.core.config import _parse_cors_origins
        
        # JSON inválido que debería caer en fallback
        result = _parse_cors_origins("not-json-at-all")
        assert result == ["not-json-at-all"]

    def test_resolved_secret_key_with_env(self):
        """Usa SECRET_KEY definida por ENV si existe."""
        from app.core.config import Settings
        
        settings = Settings(SECRET_KEY="mi-clave-personalizada")
        assert settings.resolved_secret_key == "mi-clave-personalizada"

    def test_resolved_secret_key_auto_generate(self):
        """Genera clave automáticamente si SECRET_KEY está vacía."""
        from app.core.config import Settings
        
        settings = Settings(SECRET_KEY="")
        key = settings.resolved_secret_key
        
        assert len(key) == 43
        assert isinstance(key, str)
