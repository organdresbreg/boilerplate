# 🚀 Modern Full-Stack Boilerplate 2026

[![Python 3.13.2](https://img.shields.io/badge/python-3.13.2-blue.svg)](https://www.python.org/downloads/)
[![FastAPI 0.122.0](https://img.shields.io/badge/FastAPI-0.122.0-green.svg)](https://fastapi.tiangolo.com/)
[![Preact 10.26.2](https://img.shields.io/badge/Preact-10.26.2-black.svg)](https://preactjs.com/)
[![Vite 8.0.4](https://img.shields.io/badge/Vite-8.0.4-purple.svg)](https://vitejs.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Una base profesional, ligera y tipada para aplicaciones web modernas. Construida con **FastAPI 0.122**, **Pydantic 2.11**, **SQLite**, **Preact 10** y **Vite 8**.

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
| **Hot Reload Instantáneo** | DX optimizado con Vite 8 y Uvicorn |
| **Zero-Config** | Configuraciones optimizadas por defecto. Sin tiempo perdido en setup. |
| **Edge-Ready** | Preparado para despliegue en edge computing |
| **Minimalista** | Solo dependencias estrictamente necesarias. Cada librería debe justificar su existencia. |
| **SQLite → PostgreSQL** | Desarrollo simple (SQLite), producción escalable (PostgreSQL). Cambia solo `DATABASE_URL`. |

## 🛠️ Stack Tecnológico

### Backend
- **Python 3.13.2** - JIT experimental, mejoras en GC y rendimiento
- **FastAPI 0.122.0** - Framework moderno y rápido, integrado con Pydantic 2.11
- **Pydantic 2.11.0** - Validación ultrarrápida con núcleo en Rust
- **pydantic-settings 2.8.1** - Gestión de variables de entorno tipadas
- **SQLModel 0.0.24** - ORM type-safe con SQLAlchemy 2.0.38
- **SQLite (WAL) - Ideal para desarrollo modular** - Serverless, ACID compliant
- **uv** - Package manager 10-100x más rápido que pip
- **bcrypt 4.2.1** - Hashing seguro y moderno

### Frontend
- **Preact 10.26.2** - ~3KB, compatible con React, misma API
- **Vite 8.0.4** - Build tool rápido y maduro, HMR instantáneo
- **TypeScript 5.7.3** - Inferencia mejorada
- **TanStack Query 5.66.0** - Offline-first, optimistic updates, caché inteligente
- **Preact Router 4.1.2** - Lazy loading nativo, transiciones integradas

### DevOps
- **Docker + Compose** - Contenedores multi-stage optimizados
- **Ruff 0.9.4** - Linting y formateo ultrarrápidos (Python), unificado
- **Pytest 8.3.4 + pytest-asyncio 0.25.3 (Backend), Vitest 3.0.5 (Frontend)** - Testing integrado backend/frontend
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
make lint             # Ruff (Python)
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
- `DATABASE_URL` - URL de conexión a la base de datos. **SQLite por defecto** (desarrollo), configurable a **PostgreSQL** para producción.
  - Desarrollo: `sqlite+aiosqlite:///./app.db`
  - Producción: `postgresql+asyncpg://user:password@host:5432/dbname`
- `BACKEND_CORS_ORIGINS_RAW` - Orígenes permitidos para CORS (formato JSON o comma-separated)
- `DISABLE_DOCS` - Deshabilitar `/docs`, `/redoc` y `/openapi.json` en producción (default: `False`)

> **💡 Nota sobre SQLite:** La elección de SQLite es estratégica para desarrollo modular: cero configuración, portable y ideal para módulos independientes. El stack está diseñado para escalar a PostgreSQL en producción simplemente cambiando `DATABASE_URL`, sin modificar código. Ver [stack.md](./stack.md) para guía completa de migración.

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

## 🚀 Quick Start (Un solo comando)

Para iniciar el proyecto desde cero con un solo comando:

```bash
make dev
```

Esto ejecutará automáticamente:
1. Instalación de dependencias (backend + frontend)
2. Migraciones de base de datos
3. Inicio de servicios con Docker Compose

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

### Configuración General
- [ ] **Secrets:** Variables sensibles en gestor seguro (AWS Secrets Manager, HashiCorp Vault, etc.)
- [ ] **Debug:** `DEBUG=False` y logs en nivel `WARNING`
- [ ] **HTTPS:** Certificado SSL válido configurado

### Base de Datos
- [ ] **SQLite (MVP/Edge):** Backup strategy definida (cron job o volume snapshot)
- [ ] **PostgreSQL (Escalado):** Pool de conexiones configurado, backups automáticos programados
- [ ] **Migraciones:** Alembic migrations aplicadas y verificadas

### Frontend & Testing
- [ ] **Build:** Source maps deshabilitados en frontend
- [ ] **Tests:** Suite de tests pasando al 100%

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
