# 🚀 Onboarding Guide: Boilerplate Full-Stack 2026

Bienvenido al **Boilerplate Oficial**. Este documento es tu guía maestra para iniciar, configurar y escalar nuevos proyectos basados en nuestra arquitectura estándar.

> **⚠️ Importante:** Este repositorio es una **Plantilla Maestra (Golden Master)**. No desarrolles features directamente aquí. Úsalo como base para crear nuevos proyectos.

---

## 📋 Índice

1. [Propósito del Repositorio](#-propósito-del-repositorio)
2. [Inicio Rápido: Crear un Nuevo Proyecto](#-inicio-rápido-crear-un-nuevo-proyecto)
3. [Definición del Proyecto (`specs.md`)](#-definición-del-proyecto-specsmd)
4. [Flujo de Trabajo Estándar](#-flujo-de-trabajo-estándar)
5. [Mantenimiento y Actualizaciones](#-mantenimiento-y-actualizaciones)
6. [Checklist de Verificación](#-checklist-de-verificación)
7. [Soporte y Recursos](#-soporte-y-recursos)

---

## 🎯 Propósito del Repositorio

Este repositorio contiene la **arquitectura de referencia** para todos nuestros proyectos Full-Stack. Su objetivo es:

*   **Estandarizar:** Garantizar que todos los proyectos compartan la misma estructura, calidad de código y herramientas.
*   **Acelerar:** Reducir el tiempo de setup inicial de días a minutos.
*   **Calidad:** Incorporar las mejores prácticas de 2026 (Tipado estático, Docker, CI/CD ready, Seguridad).
*   **Escalabilidad:** Proveer una base sólida preparada para crecer sin deuda técnica inicial.

**Stack Tecnológico Base:**
*   **Backend:** FastAPI (Python 3.12+) + SQLite (Dev) / PostgreSQL (Prod-ready).
*   **Frontend:** Preact + TypeScript + Vite.
*   **Infraestructura:** Docker & Docker Compose.
*   **Calidad:** Ruff, Pytest, ESLint, Vitest.

---

## ⚡ Inicio Rápido: Crear un Nuevo Proyecto

Sigue estos pasos **exactos** para instanciar un nuevo proyecto sin arrastrar el historial de git de la plantilla.

### Paso 1: Clonar y Limpiar

```bash
# 1. Clona el boilerplate en una nueva carpeta con el nombre de tu proyecto
git clone <URL_DESTE_REPOSITORIO> mi-nuevo-proyecto
cd mi-nuevo-proyecto

# 2. Elimina el historial de git de la plantilla (¡Crucial!)
rm -rf .git

# 3. Inicializa un nuevo repositorio limpio
git init

# 4. Crea la rama principal
git checkout -b main

# 5. Commit inicial limpio
git add .
git commit -m "feat: initial commit from boilerplate"
```

### Paso 2: Personalización Básica

Antes de escribir código, actualiza los metadatos del proyecto:

1.  **`README.md`**: Cambia el título, descripción y badges para reflejar tu nuevo proyecto.
2.  **`pyproject.toml`** (Backend): Actualiza `name`, `version` y `description`.
3.  **`package.json`** (Frontend): Actualiza `name`, `version` y `description`.
4.  **`.env.example`**: Ajusta las variables si tu proyecto requiere configuraciones específicas iniciales.

---

## 📝 Definición del Proyecto (`specs.md`)

Una vez clonado, el **primer archivo que debes crear** es `specs.md` en la raíz.

### ¿Qué es `specs.md`?
Es el documento de **Especificaciones Técnicas y de Negocio** único para *este* proyecto específico. Mientras que el boilerplate define el "cómo" genérico, `specs.md` define el "qué" particular.

### Estructura Recomendada para `specs.md`

```markdown
# Especificaciones de [Nombre del Proyecto]

## 1. Visión General
Breve descripción del problema que resuelve el proyecto.

## 2. Requerimientos Específicos
- **Base de Datos:** ¿Se mantiene SQLite o se migra a PostgreSQL/MySQL?
- **Autenticación:** ¿JWT, OAuth, Session-based?
- **Servicios Externos:** Stripe, SendGrid, AWS S3, etc.

## 3. Reglas de Negocio Clave
Listado de las lógicas críticas que el sistema debe cumplir.

## 4. Configuraciones Personalizadas
- Puertos no estándar.
- Variables de entorno adicionales necesarias.
- Librerías extra a instalar.

## 5. Roadmap Inicial
Fases de desarrollo planificadas.
```

> **💡 Tip:** Usa este archivo como contexto para IA (Copilot, Cursor, etc.) para que genere código alineado a tus reglas de negocio desde el día 1.

---

## 🔄 Flujo de Trabajo Estándar

Una vez tengas tu repo limpio y tu `specs.md`:

1.  **Analiza `specs.md`**: Identifica qué partes del boilerplate necesitas modificar (ej. cambiar DB, agregar Redis).
2.  **Ajusta la Infraestructura**:
    *   Edita `docker-compose.yml` si agregas servicios.
    *   Actualiza `.env.example` con nuevas variables.
3.  **Desarrollo de Features**:
    *   Crea ramas feature: `git checkout -b feat/nombre-feature`.
    *   Sigue la estructura de carpetas existente (`backend/app`, `frontend/src`).
    *   Escribe tests antes o durante el desarrollo.
4.  **Validación Local**:
    *   Ejecuta `make dev` para levantar todo el stack.
    *   Ejecuta `make test` para asegurar que no hay regresiones.
5.  **Commit y Push**: Sigue las convenciones de commits (Conventional Commits).

---

## 🛠️ Mantenimiento y Actualizaciones

El boilerplate evoluciona. Para traer mejoras desde la plantilla original a tus proyectos existentes:

### Estrategia de Remote Upstream

1.  **Agrega el remoto original** (solo se hace una vez por proyecto):
    ```bash
    git remote add boilerplate <URL_DESTE_REPOSITORIO>
    ```

2.  **Trae los cambios**:
    ```bash
    git fetch boilerplate
    ```

3.  **Revisa los cambios** antes de mergear:
    ```bash
    git diff boilerplate/main
    ```

4.  **Mergea con cuidado**:
    ```bash
    git merge boilerplate/main
    ```
    *Resuelve los conflictos prestando atención a no sobreescribir tus configuraciones específicas (`specs.md`, `.env`, configs de negocio).*

> **Nota:** Las actualizaciones mayores de versión (ej. Python 3.12 -> 3.13) deben probarse primero en un entorno de staging.

---

## ✅ Checklist de Verificación

Antes de considerar el setup del nuevo proyecto como "Completo", verifica:

- [ ] **Git Limpio**: El historial de commits comienza desde "initial commit from boilerplate".
- [ ] **Documentación**: `README.md` refleja el nuevo proyecto (no dice "Boilerplate").
- [ ] **Especificaciones**: Archivo `specs.md` creado y detallado.
- [ ] **Entorno**: Archivo `.env` creado desde `.env.example` con valores válidos.
- [ ] **Docker**: `docker compose up` levanta todos los servicios sin errores.
- [ ] **Tests**: `make test` ejecuta correctamente la suite de pruebas base.
- [ ] **Build**: `make build` genera las imágenes de Docker sin fallos.
- [ ] **Seguridad**: Se han cambiado las contraseñas por defecto y secretos en `.env`.

---

## 🆘 Soporte y Recursos

Si encuentras problemas o tienes dudas sobre la arquitectura:

1.  **Revisa `stack.md`**: Contiene la documentación técnica profunda de cada componente.
2.  **Issues del Repositorio**: Busca si tu duda ya fue reportada en el boilerplate original.
3.  **Canal de Ingeniería**: Consulta con el equipo de arquitectura antes de desviarte significativamente del estándar.

---

**¡Listo!** Ahora tienes una base sólida, estandarizada y profesional para construir software de alta calidad. ¡A codificar! 🚀
