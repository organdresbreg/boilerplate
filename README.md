# 🚀 Modern Full-Stack Boilerplate 2026

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI 0.115+](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
[![Preact 11+](https://img.shields.io/badge/Preact-11+-black.svg)](https://preactjs.com/)
[![Vite 6+](https://img.shields.io/badge/Vite-6+-purple.svg)](https://vitejs.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Una base profesional, ligera y tipada para aplicaciones web modernas. Construida con **FastAPI**, **Pydantic v2**, **SQLite**, **Preact** y **Vite**.

## ⚡ Quick Start

```bash
# Clonar el repositorio
git clone <tu-repo> && cd <tu-proyecto>

# Instalar dependencias (backend + frontend)
make install-dev

# Iniciar en modo desarrollo con Docker
make run-dev

# Acceder a:
# Backend: http://localhost:8000/docs
# Frontend: http://localhost:5173
```

## 🎯 ¿Por qué este boilerplate?

| Característica | Beneficio |
|----------------|-----------|
| **Type-Safety End-to-End** | Tipado estático desde la BD hasta el componente UI |
| **Bundle < 30KB** | Performance first, carga instantánea |
| **Hot Reload Instantáneo** | DX optimizado con Vite 6 y Uvicorn |
| **Zero-Config** | Configuraciones optimizadas por defecto |
| **Edge-Ready** | Preparado para despliegue en edge computing |
| **Minimalista** | Solo dependencias estrictamente necesarias |

## 🛠️ Stack Tecnológico

### Backend
- **Python 3.13+** - Últimas features y mejor rendimiento
- **FastAPI 0.115+** - Framework moderno y rápido
- **Pydantic v2** - Validación ultrarrápida
- **SQLModel** - ORM type-safe con SQLAlchemy 2.0
- **SQLite (WAL)** - Serverless, ACID compliant
- **uv** - Package manager 10-100x más rápido

### Frontend
- **Preact 11+** - 2.8KB, compatible con React 19
- **Vite 6+** - Build tool con Rolldown nativo (Rust)
- **TypeScript 5.0+** - Inferencia mejorada
- **TanStack Query 5.5+** - Offline-first, optimistic updates
- **Zustand 5.0+** - Estado minimalista sin re-renders

### DevOps
- **Docker + Compose** - Contenedores multi-stage optimizados
- **Ruff + Biome** - Linting y formateo ultrarrápidos
- **Pytest + Vitest** - Testing integrado backend/frontend
- **GitHub Actions** - CI/CD con deploy preview

## 📂 Estructura del Proyecto

```
.
├── backend/           # API FastAPI
│   ├── app/
│   │   ├── api/       # Endpoints
│   │   ├── core/      # Config, security
│   │   ├── db/        # DB session, CRUD
│   │   ├── models/    # SQLModel definitions
│   │   ├── schemas/   # Pydantic schemas
│   │   └── services/  # Business logic
│   └── tests/
├── frontend/          # App Preact + Vite
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── services/
│       └── store/
├── docker-compose.yml
├── Makefile
└── stack.md           # Documentación técnica completa
```

## 🚀 Comandos Esenciales

```bash
# Desarrollo
make install-dev      # Instalar dependencias
make run-dev          # Docker compose up
make run-backend      # Solo backend (sin Docker)
make run-frontend     # Solo frontend (sin Docker)

# Base de datos
make migrate          # Ejecutar migraciones Alembic
make seed             # Precargar datos de ejemplo (admin@example.com / admin123)
make backup-db        # Backup de SQLite con timestamp

# Calidad
make lint             # Ruff + Biome
make format           # Formateo automático
make test             # Tests con coverage
make type-check       # Type checking

# Producción
make build            # Construir contenedores
make clean            # Limpieza profunda
```

## 📖 Documentación

- **[📘 Ver especificación técnica completa](./stack.md)** - Detalles de configuración, ejemplos de código, migraciones, Dockerfiles y checklist de producción.

## 🔧 Configuración Rápida

### Variables de Entorno

Crear `.env` en la raíz basado en `.env.example`:

```bash
cp .env.example .env
```

Principales variables:
- `SECRET_KEY` - Clave secreta para JWT (dejar vacío para generación automática)
- `DATABASE_URL` - URL de conexión a SQLite
- `BACKEND_CORS_ORIGINS_RAW` - Orígenes permitidos para CORS (formato JSON o comma-separated)
- `DISABLE_DOCS` - Deshabilitar `/docs`, `/redoc` y `/openapi.json` en producción (default: `False`)
- `ENABLE_OTEL` - Habilitar OpenTelemetry para tracing (default: `True`)
- `OTEL_EXPORTER_OTLP_ENDPOINT` - Endpoint del colector OTLP (Jaeger/Tempo)

### Base de Datos

Las migraciones se gestionan con Alembic:

```bash
# Crear nueva migración
cd backend
alembic revision --autogenerate -m "Descripción"

# Aplicar migraciones
make migrate

# Precargar datos de ejemplo
make seed
# Usuario por defecto: admin@example.com / admin123
```

### Observabilidad (OpenTelemetry)

El proyecto incluye soporte nativo para tracing distribuido:

```bash
# Iniciar con Jaeger (tracing)
docker compose --profile monitoring up

# Acceder a UI de Jaeger
http://localhost:16686
```

Los traces se exportan automáticamente cuando `ENABLE_OTEL=True`.

## 🐳 Docker

El proyecto incluye configuración Docker optimizada:

- **Multi-stage builds** - Imágenes mínimas (~150MB backend, ~20MB frontend)
- **Hot reload** - Volúmenes montados para desarrollo
- **Health checks** - Monitoreo automático de servicios
- **Non-root users** - Seguridad por defecto

```bash
# Iniciar todos los servicios
docker compose up --build

# Solo producción
docker compose -f docker-compose.prod.yml up
```

## ✅ Checklist de Producción

Antes de desplegar:

- [ ] Secrets en gestor seguro (no en `.env`)
- [ ] `DEBUG=False` y logs en nivel `WARNING`
- [ ] Backup strategy para SQLite definida
- [ ] HTTPS con certificado válido
- [ ] Source maps deshabilitados en frontend
- [ ] Tests pasando al 100%

## 🤝 Contribución

Este boilerplate está diseñado para ser **copiado y adaptado**. No es una librería, sino una plantilla base para tus proyectos.

**Recomendaciones:**
1. Actualizar dependencias mensualmente (`pip list --outdated`, `npm outdated`)
2. Ejecutar auditorías de seguridad regularmente (`pip-audit`, `npm audit`)
3. Personalizar según las necesidades de tu proyecto

## 📄 Licencia

MIT License - ver [LICENSE](LICENSE) para más detalles.

---

*Construido con estándares modernos de desarrollo Full-Stack 2026. Optimizado para eficiencia, velocidad y escalabilidad.*
