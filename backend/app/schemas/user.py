from pydantic import BaseModel, EmailStr, Field
from sqlmodel import SQLModel
from datetime import datetime
from typing import Optional


class UserBase(SQLModel):
    email: str = Field(unique=True, index=True, min_length=5, max_length=255)
    full_name: Optional[str] = Field(default=None, max_length=100)
    is_active: bool = True


class UserCreate(SQLModel):
    """Schema para crear un usuario"""
    
    email: EmailStr = Field(..., min_length=5, max_length=255)
    password: str = Field(..., min_length=8, max_length=100)
    full_name: Optional[str] = Field(default=None, max_length=100)


class UserUpdate(SQLModel):
    """Schema para actualizar un usuario"""
    
    email: Optional[EmailStr] = Field(default=None, min_length=5, max_length=255)
    full_name: Optional[str] = Field(default=None, max_length=100)
    is_active: Optional[bool] = None
    password: Optional[str] = Field(default=None, min_length=8, max_length=100)


class UserResponse(UserBase):
    """Schema de respuesta para usuario"""
    
    id: int
    created_at: datetime
    
    model_config = {"from_attributes": True}


class Token(SQLModel):
    """Schema para token de acceso"""
    
    access_token: str
    token_type: str = "bearer"


class TokenData(SQLModel):
    """Datos del token decodificado"""
    
    email: Optional[str] = None
