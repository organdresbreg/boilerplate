# Especificaciones Técnicas: Módulo de Corresponsales IA (Frontend + Backend)

## 1. Contexto del Proyecto

Este documento define los requisitos para desarrollar la sección **Corresponsales** de la aplicación **Corresponsales IA**. El objetivo es permitir la gestión completa (CRUD) y la ejecución de agentes de IA que actúan como corresponsales de prensa digitales.

### 1.1 Objetivo

- Permitir crear, editar, listar, eliminar y ejecutar correspondents desde el frontend.
- Asegurar que la UI consuma de forma consistente los endpoints del backend.
- Garantizar una experiencia sin modales, con componentes inline y un flujo claro.

### 1.2 Criterios de aceptación

- El usuario puede ver la lista de correspondents y crear uno nuevo desde la misma pantalla.
- El usuario puede editar un correspondent y volver a la lista sin abrir modales.
- El usuario puede ejecutar un correspondent activo y ver el resultado del reporte inmediatamente.
- Los datos enviados y recibidos coinciden con las interfaces TypeScript definidas.
- Las validaciones del backend se muestran junto a los campos correspondientes.

### 1.3 Restricciones críticas

- **Sin modales:** toda la interacción debe ocurrir dentro del mismo contenedor principal de la sección.
- **Nomenclatura unificada:** la entidad debe llamarse siempre **Correspondent** en el código.
- **Alineación con el backend:** usar únicamente los endpoints y esquemas definidos aquí.
- **UI responsiva:** el componente debe funcionar correctamente en escritorio y móvil.

### 1.4 Estructura base del proyecto

Este primer módulo debe levantarse como una aplicación full-stack pequeña con frontend y backend separados, pero dentro del mismo repositorio.

Propuesta de estructura:

- `frontend/`
  - `src/`
  - `public/`
  - `package.json`
  - `vite.config.ts`
  - `tsconfig.json`
  - `tailwind.config.js`
  - `postcss.config.js`
  - `.env`
- `backend/`
  - `app/`
    - `main.py`
    - `api.py`
    - `models.py`
    - `schemas.py`
    - `crud.py`
    - `database.py`
  - `requirements.txt` o `pyproject.toml`
  - `.env`
- `.gitignore`
- `README.md`

### 1.5 Dependencias iniciales y configuración

#### Frontend

Dependencias principales:

- `react`
- `react-dom`
- `typescript`
- `vite`
- `@vitejs/plugin-react`
- `axios`
- `tailwindcss`
- `postcss`
- `autoprefixer`
- `lucide-react`

Dependencias de desarrollo:

- `@types/react`
- `@types/react-dom`
- `@types/node`

Variables de entorno:

- `VITE_API_URL=http://localhost:8000/api/v1`

#### Backend

Dependencias principales:

- `fastapi`
- `uvicorn[standard]`
- `pydantic`
- `sqlalchemy`
- `databases` o `sqlmodel` (opcional)

Dependencias de desarrollo:

- `python-dotenv`

Variables de entorno:

- `DATABASE_URL=sqlite:///./database.db`
- `API_PREFIX=/api/v1`

### 1.6 Archivos de arranque sugeridos

#### `frontend/package.json`

```json
{
  "name": "correspondent-frontend",
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
    "lucide-react": "^0.476.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1"
  },
  "devDependencies": {
    "@types/node": "^20.14.0",
    "@types/react": "^18.4.0",
    "@types/react-dom": "^18.4.0",
    "@vitejs/plugin-react": "^4.4.0",
    "autoprefixer": "^10.4.20",
    "postcss": "^8.4.36",
    "tailwindcss": "^3.4.5",
    "typescript": "^5.7.4",
    "vite": "^5.4.1"
  }
}
```

#### `frontend/vite.config.ts`

```ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
  },
});
```

#### `frontend/tailwind.config.js`

```js
export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {},
  },
  plugins: [],
};
```

#### `frontend/postcss.config.js`

```js
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

#### `frontend/tsconfig.json`

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["DOM", "DOM.Iterable", "ES2020"],
    "allowJs": false,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

#### `frontend/.env`

```env
VITE_API_URL=http://localhost:8000/api/v1
```

#### `backend/requirements.txt`

```
fastapi>=0.111.0
uvicorn[standard]>=0.23.0
sqlalchemy>=2.0.0
pydantic>=2.10.0
python-dotenv>=1.0.0
```

#### `backend/app/main.py`

```py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router

app = FastAPI(title='Correspondents IA API')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(router, prefix='/api/v1')
```

#### `backend/app/database.py`

```py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./database.db')
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

#### `backend/app/models.py`

```py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.types import JSON
from app.database import Base
import datetime

class Correspondent(Base):
    __tablename__ = 'correspondents'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=False)
    keywords = Column(JSON, nullable=False)
    sources = Column(JSON, nullable=False)
    active = Column(Boolean, default=True)
    last_execution = Column(DateTime, nullable=True)
```

#### `backend/app/schemas.py`

```py
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class CorrespondentBase(BaseModel):
    name: str = Field(..., min_length=3)
    description: str
    category: str
    keywords: List[str]
    sources: List[str]
    active: bool = True

class CorrespondentCreate(CorrespondentBase):
    pass

class CorrespondentUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    category: Optional[str]
    keywords: Optional[List[str]]
    sources: Optional[List[str]]
    active: Optional[bool]

class Correspondent(CorrespondentBase):
    id: int
    last_execution: Optional[datetime]

    class Config:
        orm_mode = True

class ExecutionRequest(BaseModel):
    correspondent_id: int

class ExecutionResponse(BaseModel):
    result: str
    metrics: dict
```

#### `backend/app/api.py`

```py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/correspondents/', response_model=list[schemas.Correspondent])
def read_correspondents(db: Session = Depends(get_db)):
    return crud.get_correspondents(db)

@router.get('/correspondents/{id}', response_model=schemas.Correspondent)
def read_correspondent(id: int, db: Session = Depends(get_db)):
    correspondent = crud.get_correspondent(db, id)
    if not correspondent:
        raise HTTPException(status_code=404, detail='Correspondent not found')
    return correspondent

@router.post('/correspondents/', response_model=schemas.Correspondent)
def create_correspondent(payload: schemas.CorrespondentCreate, db: Session = Depends(get_db)):
    return crud.create_correspondent(db, payload)

@router.put('/correspondents/{id}', response_model=schemas.Correspondent)
def update_correspondent(id: int, payload: schemas.CorrespondentUpdate, db: Session = Depends(get_db)):
    correspondent = crud.update_correspondent(db, id, payload)
    if not correspondent:
        raise HTTPException(status_code=404, detail='Correspondent not found')
    return correspondent

@router.delete('/correspondents/{id}', status_code=204)
def delete_correspondent(id: int, db: Session = Depends(get_db)):
    success = crud.delete_correspondent(db, id)
    if not success:
        raise HTTPException(status_code=404, detail='Correspondent not found')

@router.post('/agents/execute', response_model=schemas.ExecutionResponse)
def execute_agent(payload: schemas.ExecutionRequest, db: Session = Depends(get_db)):
    correspondent = crud.get_correspondent(db, payload.correspondent_id)
    if not correspondent or not correspondent.active:
        raise HTTPException(status_code=404, detail='Correspondent not found or inactive')
    result = crud.execute_correspondent(db, correspondent)
    return result
```

#### `backend/app/crud.py`

```py
from sqlalchemy.orm import Session
from datetime import datetime
from app import models, schemas

CATEGORY_OPTIONS = ['digital_media', 'social_accounts', 'institutions', 'specific_topics']

def get_correspondents(db: Session):
    return db.query(models.Correspondent).all()

def get_correspondent(db: Session, id: int):
    return db.query(models.Correspondent).filter(models.Correspondent.id == id).first()

def create_correspondent(db: Session, payload: schemas.CorrespondentCreate):
    if payload.category not in CATEGORY_OPTIONS:
        raise ValueError('Invalid category')
    model = models.Correspondent(
        name=payload.name,
        description=payload.description,
        category=payload.category,
        keywords=payload.keywords,
        sources=payload.sources,
        active=payload.active,
    )
    db.add(model)
    db.commit()
    db.refresh(model)
    return model

def update_correspondent(db: Session, id: int, payload: schemas.CorrespondentUpdate):
    correspondent = get_correspondent(db, id)
    if not correspondent:
        return None
    for field, value in payload.dict(exclude_unset=True).items():
        setattr(correspondent, field, value)
    db.commit()
    db.refresh(correspondent)
    return correspondent

def delete_correspondent(db: Session, id: int):
    correspondent = get_correspondent(db, id)
    if not correspondent:
        return False
    db.delete(correspondent)
    db.commit()
    return True

def execute_correspondent(db: Session, correspondent: models.Correspondent):
    correspondent.last_execution = datetime.utcnow()
    db.commit()
    db.refresh(correspondent)
    return {
        'result': 'Reporte simulado generado por el agente.',
        'metrics': {
            'elapsed_time': 1200,
            'tokens_used': 450,
        },
    }
```

#### `backend/.env`

```env
DATABASE_URL=sqlite:///./database.db
```

### 1.7 Flujo de arranque inicial

1. Clonar el repositorio.
2. Frontend:
   - `cd frontend`
   - `npm install`
   - `npm run dev`
3. Backend:
   - `cd backend`
   - `python -m venv .venv`
   - `source .venv/bin/activate`
   - `pip install -r requirements.txt`
   - `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

### 1.8 Notas sobre configuración de despliegue

- La API debe exponerse en `http://localhost:8000/api/v1` en desarrollo.
- El frontend debe leer `VITE_API_URL` para todas las llamadas.
- En producción se puede usar un proxy inverso o deploy separado, pero el contrato de API se mantiene.

---

## 2. Especificaciones del Backend (Fuente de Verdad)

El backend está construido en **Python (FastAPI)** con base de datos **SQLite**. El frontend debe adaptarse exactamente a este modelo de datos y contratos de API.

### 2.1 Modelo de datos

Un objeto `Correspondent` tiene la siguiente estructura. Todos los campos son obligatorios salvo indicación contraria.

| Campo | Tipo (TS) | Obligatorio | Valor por defecto | Descripción |
| --- | --- | :---: | :---: | --- |
| `id` | `number` | No | - | Identificador único generado por la base de datos. |
| `name` | `string` | Sí | - | Nombre del correspondent (ej: "Political Monitor"). |
| `description` | `string` | Sí | - | Descripción de su función o foco. |
| `category` | `string` | Sí | - | Enum: `"digital_media"`, `"social_accounts"`, `"institutions"`, `"specific_topics"`. |
| `keywords` | `string[]` | Sí | - | Lista de términos para buscar. |
| `sources` | `string[]` | Sí | - | Lista de URLs o nombres de cuentas a monitorear. |
| `active` | `boolean` | No | `true` | Estado de ejecución del correspondent. |
| `last_execution` | `string` (ISO) | No | - | Fecha/hora de la última ejecución exitosa. |

#### Reglas de validación

- `name` debe tener al menos 3 caracteres.
- `description` no puede estar vacío.
- `category` debe ser uno de los valores permitidos.
- `keywords` debe contener al menos un término válido.
- `sources` debe contener al menos una URL o cuenta. No se permiten strings vacíos.
- Si `active` es `false`, el botón `Execute` debe quedar deshabilitado.

### 2.2 Endpoints API

Base URL: `/api/v1`.

El frontend debe configurar su cliente HTTP (Axios) apuntando a `VITE_API_URL` (por ejemplo, `http://localhost:8000`).

#### A. Gestión de correspondents (CRUD)

- **List all:** `GET /correspondents/`
  - Response: `Correspondent[]`

- **Get one:** `GET /correspondents/{id}`
  - Response: `Correspondent`

- **Create:** `POST /correspondents/`
  - Body: `Omit<Correspondent, 'id' | 'last_execution'>`
  - Response: `Correspondent`
  - Ejemplo:
    ```json
    {
      "name": "Political Monitor",
      "description": "Monitors news and social posts about politics",
      "category": "digital_media",
      "keywords": ["election", "vote"],
      "sources": ["https://example.com", "@politics"],
      "active": true
    }
    ```

- **Update:** `PUT /correspondents/{id}`
  - Body: `Partial<Correspondent>`
  - Response: `Correspondent`
  - Ejemplo:
    ```json
    {
      "description": "Monitors news and social media publications",
      "active": false
    }
    ```

- **Delete:** `DELETE /correspondents/{id}`
  - Response: `204 No Content`

##### Errores esperados

- `400 Bad Request` para payload inválido.
- `404 Not Found` si el correspondent no existe.
- `422 Unprocessable Entity` con errores de validación:
  ```json
  {
    "detail": [
      {"loc": ["body", "name"], "msg": "field required", "type": "value_error.missing"}
    ]
  }
  ```

#### B. Endpoint de ejecución

- **Execute task:** `POST /agents/execute`
  - Nota: este endpoint está en `/agents`, no en `/correspondents`.
  - Body request:
    ```json
    {
      "correspondent_id": 123
    }
    ```
  - Response success:
    ```json
    {
      "result": "Text or markdown report generated by the agent.",
      "metrics": {
        "elapsed_time": 1350,
        "tokens_used": 524
      }
    }
    ```
  - Response error:
    ```json
    {
      "detail": "Correspondent not found or inactive"
    }
    ```

##### Lógica del backend

- Valida que el correspondent exista y esté `active`.
- Ejecuta el agent planner.
- Busca datos externos (DuckDuckGo) y genera un resumen con LLM.
- Actualiza `last_execution` en el correspondent.

---

## 3. Planificación de implementación frontend

El desarrollador debe seguir este orden de archivos y esta lógica.

### Paso 1: Definición de tipos (`src/types/index.ts`)

Definir tipos que reflejen exactamente el esquema del backend:

- `interface Correspondent`
- `type CorrespondentCreate = Omit<Correspondent, 'id' | 'last_execution'>`
- `type CorrespondentUpdate = Partial<Correspondent>`
- `interface ExecutionResponse`

Ejemplo de tipos:

```ts
export interface Correspondent {
  id: number;
  name: string;
  description: string;
  category: 'digital_media' | 'social_accounts' | 'institutions' | 'specific_topics';
  keywords: string[];
  sources: string[];
  active: boolean;
  last_execution?: string;
}

export type CorrespondentCreate = Omit<Correspondent, 'id' | 'last_execution'>;
export type CorrespondentUpdate = Partial<Correspondent>;

export interface ExecutionResponse {
  result: string;
  metrics: {
    elapsed_time: number;
    tokens_used: number;
  };
}
```

### Paso 2: Servicio API (`src/services/api.ts`)

Configurar Axios con la base URL dinámica desde `.env`.

Implementar `correspondentsApi` con métodos:

- `getAll()` → `GET /correspondents/`
- `getById(id)` → `GET /correspondents/{id}`
- `create(payload)` → `POST /correspondents/`
- `update(id, payload)` → `PUT /correspondents/{id}`
- `remove(id)` → `DELETE /correspondents/{id}`
- `execute(correspondentId)` → `POST /agents/execute`

Incluir manejo de errores para `422` y `404`, y mapear los mensajes de validación para mostrarlos en la UI.

### Paso 3: Componente principal (`src/components/features/CorrespondentsManager.tsx`)

Debe ser un componente autónomo con el siguiente comportamiento:

#### Estado principal

- `list`: `Correspondent[]`
- `form`: `CorrespondentCreate | CorrespondentUpdate`
- `editMode`: `null` | `-1` | `number`
- `loadingList`: boolean
- `saving`: boolean
- `executingId`: number | null
- `validationErrors`: `Record<string, string>`
- `executionResult`: `string | null`
- `message`: `string | null`

#### Flujo UI

- Cuando `editMode === null`, mostrar la lista completa.
- Cuando `editMode === -1`, mostrar el formulario en modo creación.
- Cuando `editMode >= 0`, mostrar el formulario con datos cargados para edición.
- El formulario ocupa el contenido principal y reemplaza la tabla; no se usa modal.
- `Cancel` vuelve a la lista y limpia el formulario.

#### Vista de listado

- Columnas: `Name`, `Category`, `Status`, `Last execution`, `Actions`.
- `Status`: badge verde para `active`, rojo para `inactive`.
- Acciones:
  - `Edit` → carga `form` y activa el modo de edición.
  - `Delete` → elimina el correspondent y refresca la lista.
  - `Execute` → solo habilitado si `active === true`.
- Mostrar `New Correspondent` arriba de la lista.
- Mostrar `executionResult` o mensaje de error debajo de la tabla en un panel.

#### Vista de formulario

Campos:

- `Name` (texto)
- `Description` (textarea)
- `Category` (select)
- `Keywords` (tags dinámicos)
- `Sources` (tags dinámicos o inputs de lista)
- `Active` (checkbox)

Botones:

- `Save` → crea o actualiza según `editMode`.
- `Cancel` → vuelve a la lista.

Comportamiento:

- Agregar y eliminar tags debe actualizar `keywords` y `sources`.
- `Save` deshabilitado mientras la petición está en curso.
- Mostrar errores de validación debajo de cada campo.

#### Resultados de ejecución

- Al ejecutar un correspondent, mostrar un spinner en el botón.
- Al completarse, mostrar el texto del reporte en un panel debajo de la lista o junto a ella.
- Si la ejecución falla, mostrar un mensaje claro con el motivo.

### Paso 4: Enrutamiento (`src/App.tsx`)

- Definir la ruta `/correspondents`.
- Renderizar `<CorrespondentsManager />` en esa ruta.
- Eliminar referencias antiguas a `/agents` si están obsoletas.

### Paso 5: Navegación (`src/components/layout/Sidebar.tsx`)

- Actualizar el item del menú:
  - Label: **Correspondents**
  - Icono: `Bot` o `Newspaper`
  - Path: `/correspondents`

---

## 4. Instrucciones para el desarrollador

Cuando inicies en un nuevo entorno:

1. Leer este archivo y revisar las interfaces en `src/types`.
2. Verificar si existe `src/services/api.ts` y ajustar el cliente Axios.
3. Implementar el componente `CorrespondentsManager` antes de tocar rutas o sidebar.
4. Probar create/edit/delete/execute en orden.
5. Asegurar que no haya errores `404`, `422` o validaciones sin manejar.

---

## 5. Notas adicionales

- Manejo de errores: los errores `422` deben mapearse a campos del formulario.
- Estilos: usar **Tailwind CSS** para mantener una UI limpia y responsiva.
- Iconos: usar `lucide-react`.
- Estados de carga: mostrar botones deshabilitados y spinners durante las peticiones.

---

## 6. Qué puede mejorar para ser documentación definitiva

Este documento ya es una base sólida, pero para que funcione como documentación definitiva se recomienda agregar:

- Índice navegable con enlaces internos a los apartados principales.
- Diagrama de arquitectura simple que muestre frontend, backend y la base de datos.
- Ejemplos de payload completos para cada endpoint, incluidos casos de error y respuestas de validación.
- Convenciones de naming y estilo de código para frontend y backend.
- Instrucciones de testing unitario y de integración, con comandos y herramientas propuestas.
- Guía de deploy mínima para staging y producción.
- Checklist de revisión antes de merge: lint, tests, validaciones, e2e básicas.
- Notas de seguridad básicas: CORS, validación de entrada, manejo de secretos.
- Definición de la API contract en OpenAPI/Swagger o un archivo `openapi.json` si se desea documentar programáticamente.
- Referencias a recursos adicionales: estilos de componente, librerías usadas, URLs de documentación.
