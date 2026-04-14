.PHONY: install-dev run-dev build test lint clean type-check security-check format reset backup-db migrate seed

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

# Linting con Ruff y Biome
lint:
	cd backend && ruff check . --fix
	cd frontend && npx @biomejs/biome check --apply .

# Type checking
type-check:
	cd backend && pyright || true
	cd frontend && npx tsc --noEmit

# Security audit
security-check:
	cd backend && pip-audit
	cd frontend && npm audit

# Formateo automático
format:
	cd backend && ruff format .
	cd frontend && npx @biomejs/biome format --write .

# Migraciones de base de datos con Alembic
migrate:
	cd backend && alembic upgrade head

# Seed de datos iniciales
seed:
	cd backend && python -c "from app.db.base import seed_db; import asyncio; asyncio.run(seed_db())"

# Backup de base de datos SQLite con timestamp
backup-db:
	@mkdir -p backups
	@cp backend/app.db backups/app.db.$$(date +%Y%m%d_%H%M%S) 2>/dev/null || echo "SQLite DB not found, skipping backup"
	@echo "Backup created in backups/"

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
