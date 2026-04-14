# 🚀 ONBOARDING: Tu Nuevo Proyecto Empieza Aquí

> **⚠️ ALTO:** Este repo es una **Plantilla Maestra**. No codes aquí directamente.
> Sigue estos pasos para clonarlo, limpiarlo y lanzar tu próximo proyecto en < 5 minutos.

---

## 1. El "Ritual" de Inicio (Copiar y Limpiar)

No necesitas herramientas complejas. Solo terminal.

### Paso 1: Clona y entra
```bash
git clone <URL_DE_ESTA_PLANTILLA> mi-nuevo-proyecto
cd mi-nuevo-proyecto
```

### Paso 2: Borra el pasado (Limpia el .git)
Queremos un historial limpio, solo tuyo.
```bash
rm -rf .git
git init
```

### Paso 3: Conecta tu propio remoto
Crea tu repo vacío en GitHub/GitLab y conéctalo:
```bash
git remote add origin git@github.com:tu-usuario/mi-nuevo-proyecto.git
git branch -M main
git add .
git commit -m "✨ Initial commit: Boilerplate listo para volar"
git push -u origin main
```

✅ **¡Listo!** Ahora eres el único dueño de este código.

---

## 2. Personalización Express (5 Minutos)

Antes de escribir lógica de negocio, ajusta lo básico para que sea *tuyo*.

### A. Define las reglas del juego (`specs.md`)
Crea un archivo `specs.md` en la raíz. No tiene que ser formal. Escribe:
- ¿Qué problema resuelve esto?
- ¿Qué funcionalidades sí o sí necesita el MVP?
- ¿Algún requisito técnico raro? (Ej: "El cliente quiere MySQL en vez de SQLite").
> *Tip: Usa este archivo como brújula cuando te pierdas en el código.*

### B. Limpia la identidad
- [ ] **README.md**: Cambia el título, descripción y badges. Borra lo que no sirva.
- [ ] **package.json / pyproject.toml**: Actualiza `name`, `version` (ponla en 0.0.1) y `author`.
- [ ] **.env.example**: Revisa si necesitas cambiar puertos o secretos por defecto.

---

## 3. Tu Flujo de Trabajo (Sin Fricción)

Esta plantilla ya trae todo configurado. Úsala así:

1.  **Levanta el entorno:**
    ```bash
    make dev  # O docker-compose up --build
    ```
    *(Backend en localhost:8000, Frontend en localhost:5173)*

2.  **Codifica:**
    - Backend: `/backend/app`
    - Frontend: `/frontend/src`
    - La estructura ya es escalable, no la sobrepienses.

3.  **Commit & Push:**
    Usa mensajes simples. Ej: `feat: login de usuarios`, `fix: error en css`.

---

## 4. ¿Cómo actualizo la Plantilla en el futuro?

Si saco una nueva versión de esta plantilla con mejoras (ej: nuevo Dockerfile, mejor config de Vite) y quieres traerla a tu proyecto:

```bash
# Agrega la plantilla como un remoto lejano (solo se hace una vez)
git remote add template <URL_DE_ESTA_PLANTILLA>

# Trae los cambios
git fetch template
git merge template/main --allow-unrelated-histories
```
> **Ojo:** Revisa los conflictos con calma. Generalmente querrás mantener tus configs (`.env`, `specs.md`) pero aceptar las mejoras en archivos de sistema (`Dockerfile`, `Makefile`).

---

## 5. Checklist de Despegue 🛫

Antes de empezar a tirar líneas de lógica de negocio:

- [ ] ¿Borraste el `.git` original e iniciaste uno nuevo?
- [ ] ¿Hiciste push a TU repositorio remoto?
- [ ] ¿Creaste tu `specs.md` con las ideas claras?
- [ ] ¿Actualizaste el `README.md` para que no diga "Boilerplate"?
- [ ] ¿Corriste `make dev` y ves la app funcionando?

Si marcaste todo, **estás en el negocio**. ¡A codear! 💻🔥

---

### ¿Dudas rápidas?
- **Stack Técnico:** Lee `stack.md` (la biblia técnica).
- **Comandos:** Mira el `Makefile` o `docker-compose.yml`.
- **Estructura:** Explora las carpetas `/backend` y `/frontend`.

*Hecho con ❤️ para desarrolladores que quieren construir, no configurar.*
