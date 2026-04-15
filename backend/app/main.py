from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from contextlib import asynccontextmanager
from app.core.config import settings
from app.api.v1.router import api_router
from app.db.base import init_db
from app.core.exceptions import APIException, NotFoundException, BadRequestException, UnauthorizedException
import time
import logging
from collections import defaultdict
from typing import Dict, Tuple

# Configurar logging estructurado
logging.basicConfig(
    level=logging.INFO,
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
)
logger = logging.getLogger(__name__)

# Rate Limiting simple en memoria
class RateLimiter:
    def __init__(self):
        self.requests: Dict[str, list] = defaultdict(list)
    
    def is_allowed(self, client_ip: str, max_requests: int = 10, window_seconds: int = 60) -> bool:
        now = time.time()
        # Limpiar requests antiguos
        self.requests[client_ip] = [
            req_time for req_time in self.requests[client_ip] 
            if now - req_time < window_seconds
        ]
        
        if len(self.requests[client_ip]) >= max_requests:
            return False
        
        self.requests[client_ip].append(now)
        return True

rate_limiter = RateLimiter()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    logger.info("Application startup complete")
    yield
    # Shutdown
    logger.info("Application shutdown complete")

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

# Middleware de Rate Limiting
@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    # Obtener IP del cliente
    client_ip = request.client.host if request.client else "unknown"
    
    # Endpoints sensibles con rate limiting más estricto
    sensitive_paths = ["/api/v1/auth/login", "/api/v1/auth/register"]
    if any(request.url.path.startswith(path) for path in sensitive_paths):
        if not rate_limiter.is_allowed(client_ip, max_requests=5, window_seconds=60):
            logger.warning(f"Rate limit exceeded for IP: {client_ip} on {request.url.path}")
            return JSONResponse(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                content={"detail": "Too many requests. Please try again later."}
            )
    
    # Rate limiting general para todas las rutas
    if not rate_limiter.is_allowed(client_ip, max_requests=100, window_seconds=60):
        return JSONResponse(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            content={"detail": "Too many requests. Please try again later."}
        )
    
    response = await call_next(request)
    return response

# Manejo Global de Excepciones
@app.exception_handler(APIException)
async def api_exception_handler(request: Request, exc: APIException):
    logger.error(f"API Exception: {exc.detail} - Path: {request.url.path}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "path": request.url.path}
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Validation Error: {exc.errors()} - Path: {request.url.path}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Validation error", "errors": exc.errors()}
    )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # Loggear el error completo internamente
    logger.error(f"Unhandled exception: {str(exc)} - Path: {request.url.path}", exc_info=True)
    
    # No exponer detalles del error en producción
    detail = "Internal server error" if settings.DISABLE_DOCS else str(exc)
    
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": detail}
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
