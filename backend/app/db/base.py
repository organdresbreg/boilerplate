from sqlmodel import SQLModel, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

# SQLite con modo WAL para mejor concurrencia
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False},
    pool_pre_ping=True,  # Verificar conexión antes de usar
)

async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def init_db():
    """Inicializar DB con todas las tablas registradas"""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    logger.info("Database initialized successfully")


async def seed_db():
    """Precargar datos de ejemplo en la base de datos"""
    from sqlmodel import select
    from app.models.user import User
    from passlib.context import CryptContext
    
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    async with async_session_maker() as session:
        # Verificar si ya existen usuarios
        result = await session.execute(select(User))
        existing_users = result.scalars().all()
        
        if existing_users:
            logger.info("Database already has users, skipping seed")
            return
        
        # Crear usuario admin por defecto
        admin_user = User(
            email="admin@example.com",
            full_name="Admin User",
            is_active=True,
            hashed_password=pwd_context.hash("admin123"),
        )
        
        session.add(admin_user)
        await session.commit()
        logger.info("Database seeded with default admin user (admin@example.com / admin123)")


async def get_session() -> AsyncSession:
    """Dependencia para obtener sesión de DB"""
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
