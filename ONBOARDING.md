# 🚀 ONBOARDING - Guía de Implementación

> ⚠️ Este repositorio es una **Plantilla Maestra (Boilerplate)**. No lo uses directamente como proyecto de producción sin antes seguir los pasos de inicialización.

## 1. 📦 Inicialización del Proyecto

Clonar esta plantilla y limpiar su historial para comenzar un nuevo proyecto desde cero.

### 1.1. Clonar y Limpiar Historial

Ejecutá estos comandos en tu terminal:

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

### 1.2. 🔗 Configurar Repositorio Remoto

Vincular el nuevo proyecto con su repositorio remoto en GitHub:

```bash
git remote add origin <URL_DEL_NUEVO_REPOSITORIO>
git branch -M main
git push -u origin main
```

## 2. 🎨 Personalización Esencial

Antes de empezar a desarrollar, adaptá los metadatos y la configuración base a las necesidades de tu proyecto.

### 2.1. 📝 Actualización de Metadatos

Revisar y editar los siguientes archivos:

- **`README.md`**: Actualizá título, descripción, badges y enlaces específicos de tu proyecto.
- **`package.json`** (Frontend) y **`pyproject.toml`** (Backend): Modificá `name`, `version`, `description` y `author`.
- **`LICENSE`**: Confirmá que el año y el titular del copyright sean correctos.
- **`.env.example`**: Ajustá las variables de entorno si tu proyecto requiere servicios adicionales.

### 2.2. 📋 Definición de Especificaciones (`specs.md`)

Editar el archivo `specs.md` en la raíz del proyecto. Este documento será la fuente única de verdad para los requisitos particulares, diferenciándolos de la arquitectura base del boilerplate.

## 3. 🔄 Flujo de Trabajo Recomendado

Para mantener la integridad del código y la eficiencia en el desarrollo:

1. **📖 Análisis**: Leé `stack.md` (arquitectura base) y `specs.md` (requisitos del proyecto).
2. **⚙️ Configuración**: Copiá `.env.example` a `.env` y ajustá las credenciales locales.
3. **💻 Desarrollo**: Usá ramas temáticas (`feature/nombre-funcionalidad`) para cada nueva capacidad.
4. **✅ Validación**: Ejecutá `make test` o los scripts de testing definidos antes de cada commit.
5. **🚀 Despliegue**: Usá los contenedores Docker configurados para simular el entorno de producción localmente.

## 4. 🛠️ Mantenimiento y Actualizaciones

Si la Plantilla Maestra recibe actualizaciones críticas (parches de seguridad, mejoras de rendimiento), podés integrarlas en tu proyecto derivado.

**Procedimiento de sincronización:**

```bash
# Agregar la plantilla como un repositorio remoto llamado 'upstream'
git remote add upstream <URL_DEL_REPOSITORIO_PLANTILLA>

# Obtener los cambios
git fetch upstream

# Intentar fusionar los cambios (puede requerir resolución de conflictos)
git merge upstream/main --allow-unrelated-histories
```

> **💡 Tip**: Resolvé los conflictos priorizando la lógica de negocio específica de tu proyecto sobre las configuraciones genéricas de la plantilla.

## 5. ✅ Checklist de Verificación Pre-Inicio

Completá esta lista antes de iniciar el desarrollo activo:

- [ ] Historial de Git original eliminado y nuevo repositorio inicializado
- [ ] Repositorio remoto configurado correctamente
- [ ] Archivo `specs.md` editado con los requisitos del proyecto
- [ ] Metadatos en `README`, `package.json` y `pyproject.toml` actualizados
- [ ] Archivo `.env` generado y configurado con valores locales
- [ ] Contenedores Docker iniciados correctamente (`make dev` o `docker-compose up`)
- [ ] Tests básicos ejecutados sin errores

## 6. 📚 Referencias Técnicas

- **`stack.md`**: Especificación técnica detallada de la arquitectura, dependencias y estructura de directorios.
- **`README.md`**: Documentación pública del proyecto, instrucciones de instalación y uso.
