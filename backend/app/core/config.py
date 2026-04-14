from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import Optional


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
    
    # Security
    SECRET_KEY: str = "CHANGE_ME_IN_PROD_USE_SECRETS_MANAGER"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS - Configurar según dominio de producción
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:5173"]
    
    # Feature flags para 2026
    ENABLE_HTTP3: bool = False
    ENABLE_OTEL: bool = True


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
