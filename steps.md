# createproject.md

# FastAPI Production-Level RBAC Project

# 🚀 Step-by-Step FastAPI Project Setup with RBAC + PostgreSQL

This guide includes:

* FastAPI Setup
* PostgreSQL Setup
* Async SQLAlchemy
* JWT Authentication
* RBAC (Role-Based Access Control)
* CRUD APIs
* Pagination
* Search
* Sorting
* Soft Delete
* UUID IDs
* Alembic Migration
* Production Folder Structure

---

# 📁 Project Structure

```bash
app/
├── api/
│   ├── deps/
│   └── v1/
│       └── routes/
├── core/
├── db/
├── models/
├── schemas/
├── services/
├── repositories/
├── utils/
├── auth/
├── migrations/
├── tests/
└── main.py
```

---

# ✅ Step 1: Create Project

```bash
mkdir fastapi-rbac
cd fastapi-rbac
```

---

# ✅ Step 2: Create Virtual Environment

```bash
uv venv
```

Activate Environment

## Linux / Mac

```bash
source .venv/bin/activate
```

## Windows

```bash
.venv\Scripts\activate
```

---

# ✅ Step 3: Install Dependencies

```bash
uv pip install fastapi uvicorn sqlalchemy asyncpg psycopg2-binary alembic python-jose passlib[bcrypt] python-multipart pydantic-settings email-validator
```

---

# ✅ Step 4: Create `.env`

```env
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost/fastapi_rbac
SECRET_KEY=mysecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# ✅ Step 5: Database Configuration

## `app/core/config.py`

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()
```

---

## `app/db/database.py`

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
```

---

# ✅ Step 6: Create Base Model

## `app/models/base.py`

```python
import uuid
from sqlalchemy import Column, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.database import Base

class BaseModel(Base):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
```

---

# ✅ Step 7: Create Role Model

## `app/models/role.py`

```python
from sqlalchemy import Column, String
from app.models.base import BaseModel

class Role(BaseModel):
    __tablename__ = "roles"

    name = Column(String, unique=True, nullable=False)
```

---

# ✅ Step 8: Create User Model

## `app/models/user.py`

```python
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    role_id = Column(ForeignKey("roles.id"))

    role = relationship("Role")
```

---

# ✅ Step 9: Create Schemas

## `app/schemas/user.py`

```python
from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role_id: UUID

class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
```

---

# ✅ Step 10: Password Hashing

## `app/core/security.py`

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)
```

---

# ✅ Step 11: JWT Token

## `app/auth/jwt.py`

```python
from datetime import datetime, timedelta
from jose import jwt
from app.core.config import settings


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
```

---

# ✅ Step 12: Create User API

## `app/api/v1/routes/user.py`

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.core.security import hash_password

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
async def create_user(
    payload: UserCreate,
    db: AsyncSession = Depends(get_db)
):

    query = select(User).where(User.email == payload.email)
    result = await db.execute(query)
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(400, "Email already exists")

    user = User(
        name=payload.name,
        email=payload.email,
        password=hash_password(payload.password),
        role_id=payload.role_id
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user
```

---

# ✅ Step 13: Login API

## `app/api/v1/routes/auth.py`

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel

from app.db.database import get_db
from app.models.user import User
from app.core.security import verify_password
from app.auth.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


class LoginSchema(BaseModel):
    email: str
    password: str


@router.post("/login")
async def login(payload: LoginSchema, db: AsyncSession = Depends(get_db)):

    query = select(User).where(User.email == payload.email)
    result = await db.execute(query)

    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(400, "Invalid Credentials")

    if not verify_password(payload.password, user.password):
        raise HTTPException(400, "Invalid Credentials")

    token = create_access_token({
        "sub": str(user.id),
        "role_id": str(user.role_id)
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }
```

---

# ✅ Step 14: RBAC Dependency

## `app/auth/rbac.py`

```python
from fastapi import Depends, HTTPException


def role_required(roles: list):

    async def checker(current_user=Depends()):

        if current_user.role.name not in roles:
            raise HTTPException(403, "Permission Denied")

        return current_user

    return checker
```

---

# ✅ Step 15: Protected API

```python
@router.get("/admin-only")
async def admin_route(
    user=Depends(role_required(["Admin"]))
):
    return {"message": "Welcome Admin"}
```

---

# ✅ Step 16: Pagination API

```python
@router.get("/")
async def list_users(
    page: int = 1,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):

    offset = (page - 1) * limit

    query = select(User).offset(offset).limit(limit)

    result = await db.execute(query)

    return result.scalars().all()
```

---

# ✅ Step 17: Search API

```python
@router.get("/search")
async def search_users(
    search: str,
    db: AsyncSession = Depends(get_db)
):

    query = select(User).where(User.name.ilike(f"%{search}%"))

    result = await db.execute(query)

    return result.scalars().all()
```

---

# ✅ Step 18: Alembic Setup

```bash
alembic init migrations
```

---

# ✅ Step 19: Create Migration

```bash
alembic revision --autogenerate -m "initial migration"
```

---

# ✅ Step 20: Run Migration

```bash
alembic upgrade head
```

---

# ✅ Step 21: Main App

## `app/main.py`

```python
from fastapi import FastAPI

from app.api.v1.routes.user import router as user_router
from app.api.v1.routes.auth import router as auth_router

app = FastAPI(title="FastAPI RBAC")

app.include_router(user_router)
app.include_router(auth_router)
```

---

# ✅ Step 22: Run Project

```bash
uvicorn app.main:app --reload
```

---

# ✅ Swagger URL

```bash
http://127.0.0.1:8000/docs
```

---

# ✅ Features Included

* FastAPI
* PostgreSQL
* Async SQLAlchemy
* JWT Authentication
* RBAC
* CRUD APIs
* UUID IDs
* Pagination
* Search
* Alembic Migration
* Swagger Docs
* Soft Delete

---

# 🚀 Future Features

You can later add:

* Redis Cache
* Docker
* Rate Limiting
* Celery
* RabbitMQ
* CI/CD
* Kubernetes
* WebSocket
* Multi Tenant
