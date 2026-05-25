from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role_id: Optional[UUID]

class UserResponse(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    role_id: Optional[UUID]

    class Config:
        from_attributes = True
