from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.core.config import settings
from app.api.v1.router import api_router
from app.db.base import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    yield
    # Shutdown
    pass


# Configurar URLs de docs según flag de producción
docs_config = {} if settings.DISABLE_DOCS else {
    "docs_url": "/docs",
    "redoc_url": "/redoc",
    "openapi_url": f"{settings.API_V1_STR}/openapi.json"
}

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    lifespan=lifespan,
    **docs_config
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/health")
async def health_check():
    return {"status": "ok", "version": settings.VERSION, "year": 2026}


@app.get("/")
async def root():
    return {"message": "API 2026 - Ready for the future"}
