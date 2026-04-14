# Especificaciones Técnicas: [NOMBRE DEL MÓDULO/PROYECTO]

<!-- 
╔══════════════════════════════════════════════════════════════════════════╗
║  PLANTILLA DE ESPECIFICACIONES TÉCNICAS - BOILERPLATE 2026              ║
║                                                                          ║
║  INSTRUCCIONES DE USO:                                                   ║
║  1. Reemplaza todos los textos entre [CORCHETES] con tu información     ║
║  2. Los ejemplos comentados sirven como guía de formato y detalle       ║
║  3. Elimina los comentarios <!-- --> una vez completada la edición      ║
║  4. Mantén la estructura de secciones para consistencia                 ║
║                                                                          ║
║  SECCIONES PRINCIPALES:                                                  ║
║  - Sección 1: Contexto del Proyecto (EDITAR COMPLETAMENTE)              ║
║  - Sección 2: Especificaciones del Backend (FUENTE DE VERDAD)           ║
║  - Sección 3: Planificación de Implementación Frontend                  ║
║  - Sección 4: Instrucciones para el Desarrollador                       ║
║  - Sección 5: Notas Adicionales                                          ║
║  - Sección 6: Checklist de Calidad                                       ║
╚══════════════════════════════════════════════════════════════════════════╝
-->

## 1. Contexto del Proyecto

<!-- [EDITAR] Describe aquí el propósito general del módulo o proyecto -->

Este documento define los requisitos para desarrollar la sección **[NOMBRE DE LA SECCIÓN]** de la aplicación **[NOMBRE DE LA APLICACIÓN]**. El objetivo es [DESCRIBIR OBJETIVO PRINCIPAL].

### 1.1 Objetivo

<!-- [EDITAR] Lista los objetivos específicos del módulo. Ejemplos comentados abajo: -->

- [OBJETIVO 1: ej. Permitir crear, editar, listar, eliminar y ejecutar X desde el frontend]
- [OBJETIVO 2: ej. Asegurar que la UI consuma de forma consistente los endpoints del backend]
- [OBJETIVO 3: ej. Garantizar una experiencia sin modales, con componentes inline y un flujo claro]

<!-- 
EJEMPLO DE OBJETIVOS (COMENTADO, SOLO COMO REFERENCIA):
- Permitir crear, editar, listar, eliminar y ejecutar correspondents desde el frontend.
- Asegurar que la UI consuma de forma consistente los endpoints del backend.
- Garantizar una experiencia sin modales, con componentes inline y un flujo claro.
-->

### 1.2 Criterios de aceptación

<!-- [EDITAR] Define los criterios que deben cumplirse para considerar el módulo completo -->

- [CRITERIO 1: ej. El usuario puede ver la lista de X y crear uno nuevo desde la misma pantalla]
- [CRITERIO 2: ej. El usuario puede editar un X y volver a la lista sin abrir modales]
- [CRITERIO 3: ej. El usuario puede ejecutar un X activo y ver el resultado inmediatamente]
- [CRITERIO 4: ej. Los datos enviados y recibidos coinciden con las interfaces TypeScript definidas]
- [CRITERIO 5: ej. Las validaciones del backend se muestran junto a los campos correspondientes]

### 1.3 Restricciones críticas

<!-- [EDITAR] Lista las restricciones técnicas o de diseño que deben respetarse -->

- **[RESTRICCIÓN 1]:** [DESCRIPCIÓN: ej. Sin modales: toda la interacción debe ocurrir dentro del mismo contenedor principal de la sección]
- **[RESTRICCIÓN 2]:** [DESCRIPCIÓN: ej. Nomenclatura unificada: la entidad debe llamarse siempre [NOMBRE] en el código]
- **[RESTRICCIÓN 3]:** [DESCRIPCIÓN: ej. Alineación con el backend: usar únicamente los endpoints y esquemas definidos aquí]
- **[RESTRICCIÓN 4]:** [DESCRIPCIÓN: ej. UI responsiva: el componente debe funcionar correctamente en escritorio y móvil]

### 1.4 Estructura base del proyecto

<!-- 
[EDITAR] Adapta esta estructura según las necesidades de tu proyecto.
El boilerplate ya incluye una estructura base, pero puedes modificarla si necesitas algo diferente.
Si tu proyecto usa la estructura estándar del boilerplate, puedes simplificar esta sección.
-->

Este primer módulo debe levantarse como una aplicación full-stack pequeña con frontend y backend separados, pero dentro del mismo repositorio.

Propuesta de estructura:

```
- frontend/
  - src/
    - components/
    - services/
    - types/
    - hooks/
    - utils/
  - public/
  - package.json
  - vite.config.ts
  - tsconfig.json
  - tailwind.config.js
  - postcss.config.js
  - .env
- backend/
  - app/
    - main.py
    - api.py
    - models.py
    - schemas.py
    - crud.py
    - database.py
  - requirements.txt o pyproject.toml
  - .env
- .gitignore
- README.md
- specs.md (este archivo)
```

### 1.5 Dependencias iniciales y configuración

<!-- 
[EDITAR] Ajusta las dependencias según lo que necesite tu proyecto.
El boilerplate ya incluye las dependencias base, pero puedes agregar librerías específicas.
Los ejemplos comentados muestran formatos comunes.
-->

#### Frontend

Dependencias principales:

<!-- [EDITAR] Lista las dependencias específicas de tu proyecto -->
- [DEPENDENCIA 1: ej. react]
- [DEPENDENCIA 2: ej. typescript]
- [DEPENDENCIA 3: ej. axios para llamadas HTTP]
- [DEPENDENCIA 4: ej. tailwindcss para estilos]
- [DEPENDENCIA 5: ej. lucide-react para iconos]

Variables de entorno:

<!-- [EDITAR] Define las variables de entorno que necesita el frontend -->
- `[NOMBRE_VARIABLE]=[VALOR POR DEFECTO]` (ej: `VITE_API_URL=http://localhost:8000/api/v1`)

#### Backend

Dependencias principales:

<!-- [EDITAR] Lista las dependencias específicas de tu proyecto -->
- [DEPENDENCIA 1: ej. fastapi]
- [DEPENDENCIA 2: ej. uvicorn[standard]]
- [DEPENDENCIA 3: ej. pydantic]
- [DEPENDENCIA 4: ej. sqlalchemy o sqlmodel]

Variables de entorno:

<!-- [EDITAR] Define las variables de entorno que necesita el backend -->
- `[NOMBRE_VARIABLE]=[VALOR POR DEFECTO]` (ej: `DATABASE_URL=sqlite:///./database.db`)
- `[NOMBRE_VARIABLE]=[VALOR POR DEFECTO]` (ej: `API_PREFIX=/api/v1`)

### 1.6 Archivos de arranque sugeridos

<!-- 
[NOTA] El boilerplate ya incluye configuraciones base funcionales.
Esta sección muestra ejemplos de configuración que puedes adaptar si necesitas modificaciones.
Puedes eliminar los ejemplos que no uses o dejarlos como referencia.
-->

<!-- 
EJEMPLO: frontend/package.json (COMENTADO, SOLO COMO REFERENCIA)
{
  "name": "[nombre-del-proyecto]-frontend",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "axios": "^1.6.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  }
}
-->

<!-- 
EJEMPLO: backend/requirements.txt (COMENTADO, SOLO COMO REFERENCIA)
fastapi>=0.111.0
uvicorn[standard]>=0.23.0
sqlalchemy>=2.0.0
pydantic>=2.10.0
python-dotenv>=1.0.0
-->

### 1.7 Flujo de arranque inicial

<!-- [EDITAR] Ajusta los comandos según tu configuración específica -->

1. Clonar el repositorio.
2. Frontend:
   - `cd frontend`
   - `npm install` (o `pnpm install`, `yarn install`)
   - `npm run dev`
3. Backend:
   - `cd backend`
   - `python -m venv .venv`
   - `source .venv/bin/activate` (Linux/Mac) o `.venv\Scripts\activate` (Windows)
   - `pip install -r requirements.txt`
   - `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

### 1.8 Notas sobre configuración de despliegue

<!-- [EDITAR] Agrega notas específicas sobre cómo desplegar este módulo -->

- La API debe exponerse en `[URL_DESARROLLO]` en desarrollo.
- El frontend debe leer `[VARIABLE_DE_ENTORNO]` para todas las llamadas.
- En producción se puede usar un proxy inverso o deploy separado, pero el contrato de API se mantiene.

---

## 2. Especificaciones del Backend (Fuente de Verdad)

<!-- 
[IMPORTANTE] Esta sección es CRÍTICA. El frontend debe adaptarse EXACTAMENTE a lo definido aquí.
[EDITAR] Completa el modelo de datos y endpoints según tu implementación real en el backend.
-->

El backend está construido en **Python (FastAPI)** con base de datos **[TIPO_DE_BD]**. El frontend debe adaptarse exactamente a este modelo de datos y contratos de API.

### 2.1 Modelo de datos

<!-- 
[EDITAR] Define la entidad principal del módulo.
Reemplaza [NOMBRE_ENTIDAD] con el nombre de tu entidad (ej: Correspondent, User, Product, etc.)
Todos los campos son obligatorios salvo indicación contraria.
-->

Un objeto `[NOMBRE_ENTIDAD]` tiene la siguiente estructura. Todos los campos son obligatorios salvo indicación contraria.

| Campo | Tipo (TS) | Obligatorio | Valor por defecto | Descripción |
| --- | --- | :---: | :---: | --- |
| `id` | `number` | No | - | Identificador único generado por la base de datos. |
| `[campo_1]` | `[tipo]` | Sí/No | - | [Descripción del campo] |
| `[campo_2]` | `[tipo]` | Sí/No | - | [Descripción del campo] |
| `[campo_3]` | `[tipo_enum]` | Sí | - | Enum: `[valor1]`, `[valor2]`, `[valor3]`. |
| `[campo_4]` | `[tipo][]` | Sí | - | Lista de [descripción]. |
| `[campo_5]` | `boolean` | No | `true` | [Descripción del campo]. |
| `[campo_6]` | `string` (ISO) | No | - | Fecha/hora de [evento]. |

<!-- 
EJEMPLO DE MODELO (COMENTADO, SOLO COMO REFERENCIA):
| Campo | Tipo (TS) | Obligatorio | Valor por defecto | Descripción |
| --- | --- | :---: | :---: | --- |
| `id` | `number` | No | - | Identificador único generado por la base de datos. |
| `name` | `string` | Sí | - | Nombre de la entidad (ej: "Political Monitor"). |
| `description` | `string` | Sí | - | Descripción de su función o foco. |
| `category` | `string` | Sí | - | Enum: `"digital_media"`, `"social_accounts"`, `"institutions"`, `"specific_topics"`. |
| `keywords` | `string[]` | Sí | - | Lista de términos para buscar. |
| `sources` | `string[]` | Sí | - | Lista de URLs o nombres de cuentas a monitorear. |
| `active` | `boolean` | No | `true` | Estado de ejecución de la entidad. |
| `last_execution` | `string` (ISO) | No | - | Fecha/hora de la última ejecución exitosa. |
-->

#### Reglas de validación

<!-- [EDITAR] Define las reglas de validación específicas para cada campo -->

- `[campo_1]` debe tener al menos [X] caracteres.
- `[campo_2]` no puede estar vacío.
- `[campo_3]` debe ser uno de los valores permitidos.
- `[campo_4]` debe contener al menos un elemento válido.
- `[campo_5]` debe contener al menos una URL o cuenta. No se permiten strings vacíos.
- Si `[campo_booleano]` es `false`, el botón `[ACCIÓN]` debe quedar deshabilitado.

### 2.2 Endpoints API

<!-- [EDITAR] Define todos los endpoints que expone el backend -->

Base URL: `[RUTA_BASE]` (ej: `/api/v1`).

El frontend debe configurar su cliente HTTP (Axios) apuntando a `[VARIABLE_DE_ENTORNO]` (por ejemplo, `http://localhost:8000`).

#### A. Gestión de [ENTIDADES] (CRUD)

<!-- [EDITAR] Detalla los endpoints CRUD para tu entidad principal -->

- **List all:** `GET /[ruta_entidades]/`
  - Response: `[NombreEntidad][]`

- **Get one:** `GET /[ruta_entidades]/{id}`
  - Response: `[NombreEntidad]`

- **Create:** `POST /[ruta_entidades]/`
  - Body: `Omit<[NombreEntidad], 'id' | '[campo_autogenerado]'>`
  - Response: `[NombreEntidad]`
  - Ejemplo:
    ```json
    {
      "[campo_1]": "[valor_ejemplo]",
      "[campo_2]": "[valor_ejemplo]",
      "[campo_3]": "[valor_ejemplo]"
    }
    ```

- **Update:** `PUT /[ruta_entidades]/{id}`
  - Body: `Partial<[NombreEntidad]>`
  - Response: `[NombreEntidad]`
  - Ejemplo:
    ```json
    {
      "[campo_a_actualizar]": "[nuevo_valor]"
    }
    ```

- **Delete:** `DELETE /[ruta_entidades]/{id}`
  - Response: `204 No Content`

##### Errores esperados

<!-- [NOTA] Estos son errores estándar de FastAPI, normalmente no requieren edición -->

- `400 Bad Request` para payload inválido.
- `404 Not Found` si la entidad no existe.
- `422 Unprocessable Entity` con errores de validación:
  ```json
  {
    "detail": [
      {"loc": ["body", "[campo]"], "msg": "field required", "type": "value_error.missing"}
    ]
  }
  ```

#### B. Endpoint de [ACCIÓN_ESPECIAL]

<!-- [EDITAR] Si tu módulo tiene endpoints especiales además del CRUD, defínelos aquí. Si no, elimina esta subsección. -->

- **[Nombre de la acción:** `POST /[ruta_accion]`
  - Nota: este endpoint está en `[ruta]`, no en `[ruta_entidades]`.
  - Body request:
    ```json
    {
      "[campo_id]": 123
    }
    ```
  - Response success:
    ```json
    {
      "result": "[descripción_del_resultado]",
      "metrics": {
        "[metrica_1]": 1350,
        "[metrica_2]": 524
      }
    }
    ```
  - Response error:
    ```json
    {
      "detail": "[mensaje_de_error]"
    }
    ```

##### Lógica del backend

<!-- [EDITAR] Describe brevemente qué hace el backend cuando se llama a este endpoint -->

- Valida que [condiciones].
- Ejecuta [proceso].
- [Acciones adicionales].
- Actualiza [campos] en la entidad.

---

## 3. Planificación de implementación frontend

<!-- 
[NOTA] Esta sección guía al desarrollador frontend sobre el orden y estructura de implementación.
[EDITAR] Adapta los nombres de archivos, tipos y componentes según tu proyecto.
-->

El desarrollador debe seguir este orden de archivos y esta lógica.

### Paso 1: Definición de tipos (`src/types/index.ts`)

<!-- [EDITAR] Define los tipos TypeScript que reflejen exactamente el esquema del backend -->

Definir tipos que reflejen exactamente el esquema del backend:

- `interface [NombreEntidad]`
- `type [NombreEntidad]Create = Omit<[NombreEntidad], 'id' | '[campo_autogenerado]'>`
- `type [NombreEntidad]Update = Partial<[NombreEntidad]>`
- `interface [NombreRespuestaEspecial]`

Ejemplo de tipos:

```ts
export interface [NombreEntidad] {
  id: number;
  [campo_1]: string;
  [campo_2]: string;
  [campo_3]: '[valor1]' | '[valor2]' | '[valor3]';
  [campo_4]: string[];
  [campo_5]: boolean;
  [campo_6]?: string;
}

export type [NombreEntidad]Create = Omit<[NombreEntidad], 'id' | '[campo_autogenerado]'>;
export type [NombreEntidad]Update = Partial<[NombreEntidad]>;

export interface [NombreRespuestaEspecial] {
  result: string;
  metrics: {
    [metrica_1]: number;
    [metrica_2]: number;
  };
}
```

### Paso 2: Servicio API (`src/services/api.ts`)

<!-- [EDITAR] Define los métodos del servicio API según tus endpoints -->

Configurar Axios con la base URL dinámica desde `.env`.

Implementar `[nombreEntidad]Api` con métodos:

- `getAll()` → `GET /[ruta_entidades]/`
- `getById(id)` → `GET /[ruta_entidades]/{id}`
- `create(payload)` → `POST /[ruta_entidades]/`
- `update(id, payload)` → `PUT /[ruta_entidades]/{id}`
- `remove(id)` → `DELETE /[ruta_entidades]/{id}`
- `[metodo_especial](param)` → `[VERBO] /[ruta_especial]`

Incluir manejo de errores para `422` y `404`, y mapear los mensajes de validación para mostrarlos en la UI.

### Paso 3: Componente principal (`src/components/features/[NombreComponente].tsx`)

<!-- 
[EDITAR] Describe el componente principal del módulo.
Ajusta el estado, flujo UI y comportamiento según las necesidades de tu proyecto.
-->

Debe ser un componente autónomo con el siguiente comportamiento:

#### Estado principal

<!-- [EDITAR] Define el estado que necesita tu componente -->

- `list`: `[NombreEntidad][]`
- `form`: `[NombreEntidad]Create | [NombreEntidad]Update`
- `editMode`: `null` | `-1` | `number`
- `loadingList`: boolean
- `saving`: boolean
- `[estado_especial]`: [tipo] | null
- `validationErrors`: `Record<string, string>`
- `[resultado_especial]`: `string | null`
- `message`: `string | null`

#### Flujo UI

<!-- [EDITAR] Describe cómo debe comportarse la UI en diferentes estados -->

- Cuando `editMode === null`, mostrar la lista completa.
- Cuando `editMode === -1`, mostrar el formulario en modo creación.
- Cuando `editMode >= 0`, mostrar el formulario con datos cargados para edición.
- El formulario ocupa el contenido principal y reemplaza la tabla; no se usa modal.
- `Cancel` vuelve a la lista y limpia el formulario.

#### Vista de listado

<!-- [EDITAR] Define las columnas y acciones de la vista de listado -->

- Columnas: `[Campo 1]`, `[Campo 2]`, `[Campo 3]`, `[Campo 4]`, `Actions`.
- `[Campo_estado]`: badge verde para `active`, rojo para `inactive`.
- Acciones:
  - `Edit` → carga `form` y activa el modo de edición.
  - `Delete` → elimina la entidad y refresca la lista.
  - `[Acción especial]` → solo habilitado si `[condición]`.
- Mostrar `New [Entidad]` arriba de la lista.
- Mostrar `[resultado_especial]` o mensaje de error debajo de la tabla en un panel.

#### Vista de formulario

<!-- [EDITAR] Define los campos del formulario -->

Campos:

- `[Campo 1]` (texto)
- `[Campo 2]` (textarea)
- `[Campo 3]` (select)
- `[Campo 4]` (tags dinámicos)
- `[Campo 5]` (tags dinámicos o inputs de lista)
- `[Campo 6]` (checkbox)

Botones:

- `Save` → crea o actualiza según `editMode`.
- `Cancel` → vuelve a la lista.

Comportamiento:

- Agregar y eliminar tags debe actualizar `[campo_lista]`.
- `Save` deshabilitado mientras la petición está en curso.
- Mostrar errores de validación debajo de cada campo.

#### Resultados de [acción especial]

<!-- [EDITAR] Si hay una acción especial, describe cómo mostrar sus resultados -->

- Al ejecutar [acción], mostrar un spinner en el botón.
- Al completarse, mostrar el texto del reporte en un panel debajo de la lista o junto a ella.
- Si la ejecución falla, mostrar un mensaje claro con el motivo.

### Paso 4: Enrutamiento (`src/App.tsx`)

<!-- [EDITAR] Define la ruta para tu componente -->

- Definir la ruta `/[ruta]`.
- Renderizar `<[NombreComponente] />` en esa ruta.
- Eliminar referencias antiguas a `/[ruta_antigua]` si están obsoletas.

### Paso 5: Navegación (`src/components/layout/Sidebar.tsx`)

<!-- [EDITAR] Define cómo aparece el módulo en la navegación -->

- Actualizar el item del menú:
  - Label: **[Nombre visible]**
  - Icono: `[NombreIcono]` (de lucide-react)
  - Path: `/[ruta]`

---

## 4. Instrucciones para el desarrollador

<!-- 
[NOTA] Esta sección proporciona una checklist rápida para comenzar a trabajar en el módulo.
[EDITAR] Ajusta los pasos según tu flujo de trabajo específico.
-->

Cuando inicies en un nuevo entorno:

1. Leer este archivo y revisar las interfaces en `src/types`.
2. Verificar si existe `src/services/api.ts` y ajustar el cliente Axios.
3. Implementar el componente `[NombreComponente]` antes de tocar rutas o sidebar.
4. Probar create/edit/delete/[acción_especial] en orden.
5. Asegurar que no haya errores `404`, `422` o validaciones sin manejar.

---

## 5. Notas adicionales

<!-- 
[NOTA] Agrega aquí consideraciones específicas de tu proyecto.
Las siguientes son recomendaciones generales del boilerplate.
-->

- Manejo de errores: los errores `422` deben mapearse a campos del formulario.
- Estilos: usar **Tailwind CSS** para mantener una UI limpia y responsiva.
- Iconos: usar `lucide-react`.
- Estados de carga: mostrar botones deshabilitados y spinners durante las peticiones.
- [NOTA ESPECÍFICA DEL PROYECTO: agregar aquí cualquier consideración especial]

---

## 6. Checklist de Calidad

<!-- 
[RECOMENDADO] Usa esta checklist antes de considerar el módulo completo.
Puedes agregar o quitar items según las necesidades de tu proyecto.
-->

### Antes de marcar como completado:

- [ ] El CRUD completo funciona (crear, leer, actualizar, eliminar)
- [ ] Las validaciones del backend se muestran correctamente en la UI
- [ ] No hay errores de consola en desarrollo
- [ ] Los tipos TypeScript coinciden exactamente con los schemas del backend
- [ ] La UI es responsiva (móvil y escritorio)
- [ ] Los estados de carga (loading) están implementados
- [ ] Los mensajes de error son claros y útiles
- [ ] El código pasa linting (`make lint`)
- [ ] Los tests pasan (`make test`)
- [ ] La documentación de este archivo está completa y actualizada

### Recomendaciones para documentación definitiva:

<!-- [OPCIONAL] Elementos que podrías agregar para mejorar la documentación -->

- [ ] Índice navegable con enlaces internos a los apartados principales
- [ ] Diagrama de arquitectura simple que muestre frontend, backend y la base de datos
- [ ] Ejemplos de payload completos para cada endpoint, incluidos casos de error
- [ ] Convenciones de naming y estilo de código específicas del módulo
- [ ] Instrucciones de testing unitario y de integración
- [ ] Guía de deploy mínima para staging y producción
- [ ] Notas de seguridad básicas: CORS, validación de entrada, manejo de secretos
- [ ] Referencias a recursos adicionales: estilos de componente, librerías usadas

---

<!-- 
╔══════════════════════════════════════════════════════════════════════════╗
║  FIN DE LA PLANTILLA                                                     ║
║                                                                          ║
║  Recuerda:                                                               ║
║  1. Reemplazar todos los [CORCHETES] con información real               ║
║  2. Eliminar estos comentarios una vez completada la edición            ║
║  3. Mantener actualizado este archivo si cambian las especificaciones   ║
╚══════════════════════════════════════════════════════════════════════════╝
-->
