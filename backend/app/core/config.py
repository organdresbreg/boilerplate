from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import Optional
import secrets
import json


def _generate_secret_key() -> str:
    """Genera una SECRET_KEY segura si no está definida."""
    return secrets.token_urlsafe(32)


def _parse_cors_origins(value: str) -> list[str]:
    """Parsea orígenes CORS desde string JSON o lista comma-separated."""
    if not value:
        return []
    try:
        # Intentar parsear como JSON primero
        origins = json.loads(value)
        if isinstance(origins, list):
            return origins
    except (json.JSONDecodeError, TypeError):
        pass
    # Fallback: comma-separated
    return [origin.strip() for origin in value.split(",") if origin.strip()]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"  # Ignora variables no definidas (seguridad)
    )
    
    PROJECT_NAME: str = "Boilerplate API 2026"
    VERSION: str = "2.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database - SQLite con modo estricto y WAL
    SQLITE_DB_PATH: str = "./app.db"
    DATABASE_URL: str = "sqlite+aiosqlite:///./app.db"
    
    # Security - Genera automáticamente si no está definida
    SECRET_KEY: str = ""
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS - Parseado dinámicamente desde ENV
    BACKEND_CORS_ORIGINS_RAW: str = '["http://localhost:5173"]'
    
    # Feature flags para 2026
    ENABLE_HTTP3: bool = False
    ENABLE_OTEL: bool = False
    
    # Producción: deshabilitar docs y openapi
    DISABLE_DOCS: bool = False
    
    @property
    def BACKEND_CORS_ORIGINS(self) -> list[str]:
        """Retorna orígenes CORS parseados desde variable de entorno."""
        return _parse_cors_origins(self.BACKEND_CORS_ORIGINS_RAW)
    
    @property
    def resolved_secret_key(self) -> str:
        """Retorna SECRET_KEY definida o genera una nueva automáticamente."""
        if self.SECRET_KEY and self.SECRET_KEY != "CHANGE_ME_IN_PROD_USE_SECRETS_MANAGER":
            return self.SECRET_KEY
        return _generate_secret_key()


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
