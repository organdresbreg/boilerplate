from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from app.core.config import settings

# Re-export para compatibilidad
async_session_maker = None  # type: ignore

__all__ = ["async_session_maker", "AsyncSession"]
