from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from uuid import UUID


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role_id: Optional[UUID] = None


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    username: str
    email: EmailStr
    role_id: Optional[UUID] = None
    is_active: bool


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
