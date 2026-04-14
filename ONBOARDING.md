# ONBOARDING - Guía de Implementación

> **Nota Importante**: Este repositorio funciona como una **Plantilla Maestra (Boilerplate)**. No debe utilizarse directamente como un proyecto de producción sin antes realizar los pasos de inicialización descritos a continuación.

## 1. Inicialización del Proyecto

El primer paso consiste en clonar esta plantilla y limpiar su historial de versiones para comenzar un nuevo proyecto desde cero.

### 1.1. Clonar y Limpiar Historial
Ejecutar los siguientes comandos en la terminal:

```bash
# 1. Clonar la plantilla en una nueva carpeta con el nombre de tu proyecto
git clone <URL_DEL_REPOSITORIO_PLANTILLA> <nombre-del-nuevo-proyecto>

# 2. Ingresar al directorio
cd <nombre-del-nuevo-proyecto>

# 3. Eliminar la referencia al repositorio original (.git)
rm -rf .git

# 4. Inicializar un nuevo repositorio Git
git init

# 5. Realizar el commit inicial
git add .
git commit -m "feat: initial project setup based on master boilerplate"
```

### 1.2. Configurar Repositorio Remoto
Vincular el nuevo proyecto con su repositorio remoto en GitHub, GitLab o similar:

```bash
git remote add origin <URL_DEL_NUEVO_REPOSITORIO>
git branch -M main
git push -u origin main
```

## 2. Personalización Esencial

Antes de comenzar el desarrollo, es necesario adaptar los metadatos y la configuración base a las necesidades específicas del nuevo proyecto.

### 2.1. Actualización de Metadatos
Revise y edite los siguientes archivos:
- **`README.md`**: Actualice título, descripción, badges y enlaces específicos del proyecto.
- **`package.json`** (Frontend) y **`pyproject.toml`** (Backend): Modifique `name`, `version`, `description` y `author`.
- **`LICENSE`**: Confirme que el año y el titular del copyright sean correctos.
- **`.env.example`**: Ajuste las variables de entorno si el nuevo proyecto requiere servicios adicionales.

### 2.2. Definición de Especificaciones (`specs.md`)
Se recomienda crear un archivo `specs.md` en la raíz del proyecto. Este documento servirá como la fuente única de verdad para los requisitos particulares, diferenciándolos de la arquitectura base del boilerplate.

**Contenido sugerido para `specs.md`:**
- Objetivos del negocio.
- Reglas de validación y lógica específica.
- Integraciones de terceros requeridas.
- Decisiones técnicas que desvíen del stack estándar.

## 3. Flujo de Trabajo Recomendado

Para mantener la integridad del código y la eficiencia en el desarrollo:

1.  **Análisis**: Lea `stack.md` (arquitectura base) y `specs.md` (requisitos del proyecto).
2.  **Configuración**: Copie `.env.example` a `.env` y ajuste las credenciales locales.
3.  **Desarrollo**: Utilice ramas temáticas (`feature/nombre-funcionalidad`) para cada nueva capacidad.
4.  **Validación**: Ejecute `make test` o los scripts de testing definidos antes de cada commit.
5.  **Despliegue**: Utilice los contenedores Docker configurados para simular el entorno de producción localmente.

## 4. Mantenimiento y Actualizaciones

Si la Plantilla Maestra recibe actualizaciones críticas (parches de seguridad, mejoras de rendimiento), es posible integrarlas en el proyecto derivado.

**Procedimiento de sincronización:**
```bash
# Agregar la plantilla como un repositorio remoto llamado 'upstream'
git remote add upstream <URL_DEL_REPOSITORIO_PLANTILLA>

# Obtener los cambios
git fetch upstream

# Intentar fusionar los cambios (puede requerir resolución de conflictos)
git merge upstream/main --allow-unrelated-histories
```
*Nota: Resuelva los conflictos priorizando la lógica de negocio específica de su proyecto sobre las configuraciones genéricas de la plantilla.*

## 5. Checklist de Verificación Pre-Inicio

Asegúrese de completar esta lista antes de iniciar el desarrollo activo:

- [ ] Historial de Git original eliminado y nuevo repositorio inicializado.
- [ ] Repositorio remoto configurado correctamente.
- [ ] Archivo `specs.md` creado con los requisitos del proyecto.
- [ ] Metadatos en `README`, `package.json` y `pyproject.toml` actualizados.
- [ ] Archivo `.env` generado y configurado con valores locales.
- [ ] Contenedores Docker iniciados correctamente (`make dev` o `docker-compose up`).
- [ ] Tests básicos ejecutados sin errores.

## 6. Referencias Técnicas

- **`stack.md`**: Especificación técnica detallada de la arquitectura, dependencias y estructura de directorios.
- **`README.md`**: Documentación pública del proyecto, instrucciones de instalación y uso.
- **`CONTRIBUTING.md`**: Normas y estándares de código para contribuciones futuras.

---

*Versión del documento: 1.0 | Basado en Arquitectura Full-Stack Moderna (2026)* ✨
