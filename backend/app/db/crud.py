from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel, select
from typing import TypeVar, Generic, Type, Optional, List

T = TypeVar("T", bound=SQLModel)


class CRUDBase(Generic[T]):
    """Clase base para operaciones CRUD"""
    
    def __init__(self, model: Type[T]):
        self.model = model
    
    async def get(self, db: AsyncSession, id: int) -> Optional[T]:
        """Obtener un registro por ID"""
        result = await db.execute(select(self.model).where(self.model.id == id))  # type: ignore[attr-defined]
        return result.scalar_one_or_none()
    
    async def get_multi(
        self, db: AsyncSession, *, skip: int = 0, limit: int = 100
    ) -> List[T]:
        """Obtener múltiples registros con paginación"""
        result = await db.execute(select(self.model).offset(skip).limit(limit))
        return list(result.scalars().all())
    
    async def create(self, db: AsyncSession, *, obj_in: SQLModel) -> T:
        """Crear un nuevo registro"""
        obj_in_data = obj_in.model_dump()
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        await db.flush()
        await db.refresh(db_obj)
        return db_obj
    
    async def update(
        self, db: AsyncSession, *, db_obj: T, obj_in: SQLModel
    ) -> T:
        """Actualizar un registro existente"""
        obj_data = obj_in.model_dump(exclude_unset=True)
        for field, value in obj_data.items():
            setattr(db_obj, field, value)
        db.add(db_obj)
        await db.flush()
        await db.refresh(db_obj)
        return db_obj
    
    async def delete(self, db: AsyncSession, *, id: int) -> Optional[T]:
        """Eliminar un registro por ID"""
        obj = await self.get(db, id=id)
        if not obj:
            return None
        await db.delete(obj)
        await db.flush()
        return obj
