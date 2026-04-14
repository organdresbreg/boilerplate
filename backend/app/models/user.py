from sqlmodel import Field, SQLModel
from datetime import datetime
from typing import Optional


class UserBase(SQLModel):
    email: str = Field(unique=True, index=True, min_length=5, max_length=255)
    full_name: Optional[str] = Field(default=None, max_length=100)
    is_active: bool = True


class User(UserBase, table=True):
    __tablename__ = "users"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str = Field(min_length=60)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    updated_at: Optional[datetime] = Field(default=None)
    
    # Pydantic V3 config para modelos SQLModel
    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "user@example.com",
                "full_name": "John Doe",
                "is_active": True
            }
        }
    }
