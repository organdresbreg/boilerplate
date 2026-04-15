# 🚀 Modern Full-Stack Boilerplate Specification (2026 Edition)
## FastAPI + Pydantic v2 + SQLite + Preact + Vite

**Versión:** 2.1.0  
**Última actualización:** Abril 2026  
**Objetivo:** Proporcionar una base profesional, ligera, tipada y escalable para aplicaciones web modernas con mínimos recursos, siguiendo los estándares de 2026.

---

## 📋 Índice

1. [Filosofía y Principios](#filosofía-y-principios)
2. [Stack Tecnológico Detallado](#stack-tecnológico-detallado)
3. [Estructura de Directorios](#estructura-de-directorios)
4. [Configuración del Backend (FastAPI)](#configuración-del-backend-fastapi)
5. [Configuración del Frontend (Preact + Vite)](#configuración-del-frontend-preact--vite)
6. [Base de Datos (SQLite + SQLModel)](#base-de-datos-sqlite--sqlmodel)
7. [Dockerización y Despliegue](#dockerización-y-despliegue)
8. [Scripts y Comandos Esenciales](#scripts-y-comandos-esenciales)
9. [Guía de Desarrollo](#guía-de-desarrollo)
10. [Checklist de Producción](#checklist-de-producción)

---

## 🧠 Filosofía y Principios

- **Minimalismo Funcional:** Solo dependencias estrictamente necesarias. Cada librería debe justificar su existencia reduciendo complejidad o mejorando performance.
- **Type-Safety End-to-End:** Tipado estático desde la BD hasta el componente UI.
- **Zero-Config Experience:** Configuraciones optimizadas por defecto. El desarrollador no debería perder tiempo configurando herramientas; todo funciona out-of-the-box.
- **Performance First:** Bundle size < 30KB (gzipped), TTFB < 50ms local.
- **Developer Experience (DX):** Hot reload instantáneo, linting automático, testing integrado.
- **Edge-Ready:** Arquitectura preparada para despliegue en edge computing.
- **Sustainability:** Código optimizado para menor consumo energético.

---

## 🛠️ Stack Tecnológico Detallado

### Backend
| Componente | Versión | Justificación |
|------------|---------|---------------|
| **Lenguaje** | Python 3.13.2 | JIT experimental, mejoras en GC, typing reforzado |
| **Package Manager** | uv 0.6+ | 10-100x más rápido que pip, gestión unificada de proyectos |
| **Framework Web** | FastAPI 0.122.0 | Integración nativa optimizada para Pydantic 2.11+, Python 3.13 |
| **Validación** | Pydantic 2.11.0 | Validador de alto rendimiento, núcleo en Rust |
| **Config** | pydantic-settings 2.8.1 | Gestión de variables de entorno para Pydantic v2 |
| **ORM** | SQLModel 0.0.24 | Compatible con SQLAlchemy 2.0.38+, unifica schemas y modelos |
| **DB Driver** | SQLAlchemy 2.0.38 + aiosqlite 0.21.0 | Base asíncrona robusta, driver SQLite async |
| **Migrations** | Alembic 1.14.1 | Soporte completo para async, autogeneración mejorada |
| **Server** | Uvicorn 0.35.2 | Soporte Python 3.13, uvloop actualizado |
| **Security** | bcrypt 4.2.1 + python-jose 3.4.0 | Hashing moderno, JWT estándar |

### Frontend
| Componente | Versión | Justificación |
|------------|---------|---------------|
| **Librería UI** | Preact 10.26.2 | Alternativa ligera a React (~3KB), misma API |
| **Build Tool** | Vite 8.0.4 | Motor de compilación estable, HMR instantáneo |
| **Lenguaje** | TypeScript 5.7.3 | Inferencia mejorada, tipado estricto |
| **HTTP Client** | TanStack Query 5.66.0 | Offline-first, caché inteligente, optimistic updates |
| **Router** | Preact Router 4.1.2 | Lazy loading nativo, transiciones integradas |
| **Preset** | @preact/preset-vite 5.0.0 | Adaptador oficial para Vite 8 |

### DevOps & Calidad
- **Contenedores:** Docker + Docker Compose v3 (Multi-stage builds optimizados)
- **Linting:** Ruff 0.9.4 (Python) - Linter y formateador unificado
- **Testing Backend:** Pytest 8.3.4 + pytest-asyncio 0.25.3 + pytest-cov 6.0.0
- **Testing Frontend:** Vitest 3.0.5 (Entorno nativo para Vite)
- **HTTP Client Tests:** httpx 0.28.1 (Cliente HTTP asíncrono para FastAPI)
- **Security Audit:** pip-audit 2.8.2 (Análisis de vulnerabilidades)
- **CI/CD:** GitHub Actions 2026 + Deploy preview automático
- **Logs:** Logs estructurados JSON integrados

---

## 📂 Estructura de Directorios

```text
.
├── backend/
│   ├── app/
│   │   ├── api/            # Endpoints routers
│   │   │   ├── v1/
│   │   │   │   ├── endpoints/
│   │   │   │   └── router.py
│   │   ├── core/           # Config, security, exceptions
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── exceptions.py
│   │   ├── db/             # DB session, base model
│   │   │   ├── base.py
│   │   │   ├── session.py
│   │   │   └── crud.py
│   │   ├── models/         # SQLModel definitions
│   │   ├── schemas/        # Pydantic schemas (Request/Response)
│   │   ├── services/       # Lógica de negocio
│   │   ├── main.py         # Entry point
│   │   └── __init__.py
│   ├── alembic/            # Migrations
│   ├── tests/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── pyproject.toml      # O requirements.txt según preferencia
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/     # Componentes reutilizables
│   │   ├── hooks/          # Custom hooks
│   │   ├── layouts/        # Layouts principales
│   │   ├── pages/          # Vistas/Rutas
│   │   ├── services/       # API calls (axios/fetch wrappers)
│   │   ├── store/          # Estado global (Signals)
│   │   ├── types/          # Tipos TS globales
│   │   ├── utils/          # Helpers
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── vite-env.d.ts
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── Dockerfile
│
├── docker-compose.yml
├── .env.example
├── .gitignore
├── README.md
└── Makefile                # Comandos unificados
```

---

## ⚙️ Configuración del Backend (FastAPI)

### `backend/app/core/config.py`
Uso de `pydantic-settings` v2 para gestión de variables de entorno tipadas.

```python
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
    DATABASE_URL: str = f"sqlite+aiosqlite:///{SQLITE_DB_PATH}"
    
    # Security
    SECRET_KEY: str = "CHANGE_ME_IN_PROD_USE_SECRETS_MANAGER"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS - Configurar según dominio de producción
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:5173"]
    
    # Producción: deshabilitar docs y openapi
    DISABLE_DOCS: bool = False

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
```

### `backend/app/main.py`
Configuración centralizada con lifespan asíncrono.

```python
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
```

---

## 🎨 Configuración del Frontend (Preact + Vite)

### Estrategia de Estilos: CSS Modules

Este proyecto utiliza **CSS Modules** como estrategia oficial de estilos, alineada con los principios de minimalismo y modularidad.

**¿Por qué CSS Modules?**
- ✅ **Scope local automático:** Los nombres de clase se transforman globalmente únicos, evitando colisiones.
- ✅ **Cero configuración:** Vite 8 soporta CSS Modules nativamente (`*.module.css`).
- ✅ **Rendimiento óptimo:** CSS puro, sin runtime JavaScript ni bundles pesados.
- ✅ **TypeScript friendly:** Tipado automático de clases importadas.
- ✅ **Minimalismo:** Sin dependencias adicionales (styled-components, Emotion, Tailwind).

**Ejemplo de uso:**

```css
/* Button.module.css */
.button {
  padding: 0.75rem 1.5rem;
  border-radius: 0.375rem;
  font-weight: 600;
  transition: all 0.2s ease;
}

.primary {
  background-color: #3b82f6;
  color: white;
}

.primary:hover {
  background-color: #2563eb;
}

.secondary {
  background-color: #e5e7eb;
  color: #374151;
}

.secondary:hover {
  background-color: #d1d5db;
}
```

```tsx
/* Button.tsx */
import styles from './Button.module.css'

interface ButtonProps {
  variant?: 'primary' | 'secondary'
  children: string
  onClick?: () => void
}

export function Button({ variant = 'primary', children, onClick }: ButtonProps) {
  const className = variant === 'primary' ? styles.primary : styles.secondary
  
  return (
    <button 
      className={`${styles.button} ${className}`}
      onClick={onClick}
    >
      {children}
    </button>
  )
}
```

**Buenas prácticas:**
- Usar nombres descriptivos en los archivos: `ComponentName.module.css`
- Componer clases locales cuando sea necesario
- Evitar selectores globales (`:global()`) salvo casos excepcionales
- Mantener los módulos pequeños y enfocados en un componente

---

### `frontend/vite.config.ts`
Optimizado para Vite 8, alias y proxy de API.

```typescript
import { defineConfig } from 'vite'
import preact from '@preact/preset-vite'
import path from 'path'

export default defineConfig({
  plugins: [preact()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
  build: {
    target: 'es2026',  // ES2025 para 2026
    minify: 'terser',
    sourcemap: false,  // Deshabilitar en prod por seguridad
    terserOptions: {
      compress: {
        drop_console: true,
        drop_debugger: true,
      },
    },
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['preact', 'preact/hooks', 'preact/compat'],
          query: ['@tanstack/react-query'],
        },
      },
    },
  },
  optimizeDeps: {
    include: ['preact', 'preact/hooks'],
  },
})
```

### `frontend/src/main.tsx`
Entry point limpio con Preact Signals y TanStack Query.

```tsx
import { render } from 'preact'
import { App } from './App'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import './index.css'

// Configurar Query Client para 2026
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60 * 5,  // 5 minutos
      retry: 2,
      refetchOnWindowFocus: false,
    },
  },
})

render(
  <QueryClientProvider client={queryClient}>
    <App />
  </QueryClientProvider>,
  document.getElementById('app')!
)
```

### `frontend/src/App.tsx`
Ejemplo con Preact Router 4.1.2 y Signals.

```tsx
import { Router, Route } from 'preact-router'
import { Home } from './pages/Home'
import { About } from './pages/About'
import { Header } from './components/Header'

export function App() {
  return (
    <div class="app">
      <Header />
      <Router>
        <Route path="/" component={Home} />
        <Route path="/about" component={About} />
      </Router>
    </div>
  )
}
```

---

## 💾 Base de Datos (SQLite + SQLModel)

> **Nota sobre SQLite en Desarrollo:** La elección de SQLite no es una limitación, es una **decisión estratégica** para desarrollo modular. SQLite ofrece cero configuración, portabilidad total (archivo único), y es ideal para módulos independientes que pueden ejecutarse de forma aislada. Para producción con alta concurrencia o grandes volúmenes, el stack está diseñado para escalar a PostgreSQL cambiando únicamente la variable de entorno `DATABASE_URL`.

### Estrategia de Escalado: SQLite → PostgreSQL

Este boilerplate sigue el principio **"Develop Simple, Deploy Scalable"**:

| Entorno | Base de Datos | Justificación |
|---------|--------------|---------------|
| **Desarrollo** | SQLite (WAL + strict tables) | Cero configuración, portable, rápido para pruebas unitarias |
| **Producción (MVP)** | SQLite | Adecuado para < 100K req/día, edge computing, módulos aislados |
| **Producción (Escalado)** | PostgreSQL 16+ | Alta concurrencia, escrituras paralelas, replicación, particionamiento |

#### Cómo escalar a PostgreSQL

Solo necesitas cambiar la variable de entorno `DATABASE_URL` en tu `.env` o gestor de secretos:

```bash
# Desarrollo (default)
DATABASE_URL="sqlite+aiosqlite:///./app.db"

# Producción (PostgreSQL)
DATABASE_URL="postgresql+asyncpg://user:password@localhost:5432/mydb"
```

No hay cambios en el código. SQLModel + SQLAlchemy 2.0 abstraen el dialecto de base de datos automáticamente.

### Guía de Migración: SQLite → PostgreSQL

#### ¿Cuándo considerar el cambio?

- ✅ **Permanecer en SQLite si:** 
  - Módulo independiente con < 100K operaciones diarias
  - Arquitectura edge/serverless
  - Prototipo o MVP temprano
  - Lecturas predominantes (>90%)

- 🔄 **Migrar a PostgreSQL si:**
  - Concurrencia alta (>50 escrituras simultáneas)
  - Necesitas replicación o high-availability
  - Volúmenes > 10GB de datos
  - Requeres características avanzadas (full-text search complejo, JSONB avanzado, geolocalización)

#### Pasos para ejecutar la migración

1. **Exportar datos desde SQLite:**
```bash
cd backend
python -c "
import sqlite3
import json
from app.db.session import engine
from sqlmodel import SQLModel

conn = sqlite3.connect('app.db')
cursor = conn.cursor()

# Exportar tablas a JSON
tables = ['users', 'your_tables']
for table in tables:
    cursor.execute(f'SELECT * FROM {table}')
    columns = [desc[0] for desc in cursor.description]
    rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    with open(f'{table}.json', 'w') as f:
        json.dump(rows, f, indent=2, default=str)
"
```

2. **Configurar PostgreSQL en docker-compose.yml:**
```yaml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  pgdata:
```

3. **Actualizar DATABASE_URL en .env:**
```bash
DATABASE_URL="postgresql+asyncpg://user:password@db:5432/mydb"
```

4. **Ejecutar migraciones con Alembic:**
```bash
cd backend
alembic upgrade head
```

5. **Importar datos (opcional):**
```bash
python scripts/import_from_sqlite.py
```

#### Configuración recomendada para PostgreSQL en producción

```python
# backend/app/core/config.py
DATABASE_URL: str = "postgresql+asyncpg://user:password@host:5432/dbname"

# Pool de conexiones optimizado
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
    pool_size=20,           # Ajustar según carga esperada
    max_overflow=40,        # Conexiones temporales adicionales
    pool_pre_ping=True,     # Verificar conexión antes de usar
    pool_recycle=3600,      # Reciclar conexiones cada hora
)
```

**docker-compose.prod.yml:**
```yaml
services:
  db:
    image: postgres:16-alpine
    deploy:
      resources:
        limits:
          memory: 1G
        reservations:
          memory: 512M
    command: >
      postgres
      -c max_connections=200
      -c shared_buffers=256MB
      -c effective_cache_size=768MB
      -c work_mem=16MB
      -c checkpoint_timeout=10min
      -c wal_level=replica
```

---

### `backend/app/db/base.py`
Inicialización asíncrona con SQLite modo estricto y WAL.

```python
from sqlmodel import SQLModel, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

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
```

### Modelo Ejemplo (`backend/app/models/user.py`)

```python
from sqlmodel import Field, SQLModel
from datetime import datetime
from typing import Optional
import uuid

class UserBase(SQLModel):
    email: str = Field(unique=True, index=True, min_length=5, max_length=255)
    full_name: Optional[str] = Field(default=None, max_length=100)
    is_active: bool = True

class User(UserBase, table=True):
    __tablename__ = "users"
    
    id: int = Field(default=None, primary_key=True)
    hashed_password: str = Field(min_length=60)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    updated_at: Optional[datetime] = Field(default=None)
    
    # Pydantic v2 config para modelos SQLModel
    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "user@example.com",
                "full_name": "John Doe",
                "is_active": True
            }
        }
    }


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True

## 🐳 Dockerización y Despliegue (2026)

### `docker-compose.yml`
Orquestación optimizada para desarrollo con hot reload.

```yaml
version: '3.8'

services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: app_backend
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
      - db_data:/app/data
    environment:
      - SQLITE_DB_PATH=/app/data/app.db
      - ENVIRONMENT=development
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: app_frontend
    ports:
      - "5173:5173"
    volumes:
      - ./frontend:/app
      - /app/node_modules
    environment:
      - VITE_API_URL=http://localhost:8000
    command: npm run dev -- --host
    depends_on:
      - backend

volumes:
  db_data:
```

### `backend/Dockerfile` (Multi-stage con uv)

```dockerfile
# Stage 1: Builder
FROM python:3.13-slim as builder

WORKDIR /app
RUN pip install uv
COPY pyproject.toml uv.lock* ./
RUN uv pip install --system --no-cache -r requirements.txt

# Stage 2: Runtime minimal
FROM python:3.13-slim

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .

RUN adduser --disabled-password --gecos '' appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### `frontend/Dockerfile` (Multi-stage con Node 22)

```dockerfile
# Stage 1: Builder
FROM node:22-alpine as builder

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Stage 2: Nginx Alpine
FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

RUN adduser -D -g '' nginxuser && chown -R nginxuser:nginxuser /usr/share/nginx/html
USER nginxuser

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### `frontend/nginx.conf`

```nginx
server {
    listen 80;
    server_name localhost;
    root /usr/share/nginx/html;
    index index.html;

    # Gzip compression
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml;

    # Cache static assets
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg|woff2)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # SPA routing
    location / {
        try_files $uri $uri/ /index.html;
    }

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
}
```

---

## 📜 Scripts y Comandos Esenciales (2026)

### `Makefile` (Raíz)
Unifica comandos para no recordar rutas complejas. Optimizado para `uv`.

```makefile
.PHONY: install-dev run-dev build test lint clean type-check security-check

# Instalación de dependencias con uv (10-100x más rápido)
install-dev:
	cd backend && uv pip install -e . -r requirements.txt
	cd frontend && npm install

# Ejecutar en desarrollo con Docker Compose
run-dev:
	docker compose up --build

# Ejecutar solo backend (sin Docker)
run-backend:
	cd backend && uvicorn app.main:app --reload

# Ejecutar solo frontend (sin Docker)
run-frontend:
	cd frontend && npm run dev

# Construir para producción
build:
	docker compose build

# Testing con coverage
test:
	cd backend && pytest --cov=app --cov-report=html
	cd frontend && npm run test -- --coverage

# Linting con Ruff
lint:
	cd backend && ruff check . --fix

# Type checking
type-check:
	cd frontend && npx tsc --noEmit

# Security audit
security-check:
	cd backend && pip-audit
	cd frontend && npm audit

# Formateo automático
format:
	cd backend && ruff format .

# Limpieza profunda
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "node_modules" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf coverage-html/
	docker compose down -v

# Reset completo (útil para CI/CD)
reset: clean
	docker system prune -f
```

---

## 📘 Guía de Desarrollo

### 1. Inicialización
```bash
# Clonar o copiar estructura
mkdir my-project && cd my-project
# Copiar este stack.md y seguir instrucciones

# Crear entorno virtual
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate

# Instalar deps
make install-dev
```

### 2. Flujo de Trabajo Típico
1.  **Definir Modelo:** Crear clase en `backend/app/models/`.
2.  **Crear Schema:** Definir DTOs en `backend/app/schemas/`.
3.  **Implementar Endpoint:** Agregar ruta en `backend/app/api/`.
4.  **Consumir en Frontend:** Crear hook/service en `frontend/src/services/`.
5.  **Construir UI:** Desarrollar componente en `frontend/src/components/`.

### 3. Migraciones (Alembic)
```bash
cd backend
alembic revision --autogenerate -m "Descripción del cambio"
alembic upgrade head
```

---

## ✅ Checklist de Producción

Antes de desplegar, verificar:

### Configuración General
- [ ] **Secrets:** `.env` no commiteado, variables sensibles en gestor de secretos (AWS Secrets Manager, HashiCorp Vault, etc.).
- [ ] **Debug:** `DEBUG=False`, `PYDEVD_DISABLE_FILE_VALIDATION=1`.
- [ ] **Logs:** Nivel de log cambiado a `WARNING` o `ERROR`. Logs estructurados en formato JSON habilitados.
- [ ] **HTTPS:** Certificado SSL válido (Let's Encrypt o proveedor comercial). HSTS habilitado.

### Base de Datos
- [ ] **SQLite (MVP/Edge):** Backup strategy definida (cron job con `sqlite3 .backup` o volume snapshot). WAL mode verificado.
- [ ] **PostgreSQL (Escalado):** 
  - Pool de conexiones configurado (`pool_size`, `max_overflow`)
  - Backups automáticos programados (pg_dump diario + WAL archiving)
  - Monitoreo de conexiones activas y slow queries
  - Índices analizados con `EXPLAIN ANALYZE`
- [ ] **Migraciones:** Alembic migrations aplicadas y verificadas en staging.

### Frontend
- [ ] **Build:** Source maps deshabilitados, console.logs eliminados.
- [ ] **Cache:** Headers de cache configurados para assets estáticos (inmutable por 1 año).
- [ ] **Security:** CSP (Content Security Policy) configurado según necesidades.

### Monitorización
- [ ] **Health Checks:** Endpoints `/health` activos y monitoreados.
- [ ] **Alertas:** Configurar alertas para errores 5xx, latencia > 500ms, uso de DB > 80%.
- [ ] **Tests:** Suite de tests pasando al 100% con coverage > 80%.

### Performance
- [ ] **Backend:** Response time p95 < 200ms para endpoints críticos.
- [ ] **Frontend:** Bundle size < 30KB (gzipped), Lighthouse score > 90.

---

## 🤝 Contribución y Mantenimiento

Este boilerplate está diseñado para ser **copiado y adaptado**. No es una librería a importar, sino una plantilla base.

**Actualización de dependencias:**
Revisar mensualmente:
```bash
pip list --outdated
npm outdated
```

**Seguridad:**
Ejecutar regularmente:
```bash
pip-audit
npm audit
```

---

*Generado con estándares modernos de desarrollo Full-Stack 2026. Optimizado para eficiencia de recursos, velocidad de desarrollo y escalabilidad.*
