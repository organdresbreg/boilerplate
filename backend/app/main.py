from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.core.config import settings
from app.api.v1.router import api_router
from app.db.base import init_db

# OpenTelemetry setup (opcional para 2026)
if settings.ENABLE_OTEL:
    try:
        from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
    except ImportError:
        FastAPIInstrumentor = None  # type: ignore


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    if settings.ENABLE_OTEL and FastAPIInstrumentor:
        FastAPIInstrumentor.instrument_app(app)
    yield
    # Shutdown
    if settings.ENABLE_OTEL and FastAPIInstrumentor:
        FastAPIInstrumentor.uninstrument_app(app)


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # ReDoc
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
