from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.core.security import verify_password
from app.auth.jwt import create_access_token
from app.db import get_db
from pydantic import BaseModel
from app.core.security import role_required

router = APIRouter(prefix="/auth", tags=["auth"])

class LoginSchema(BaseModel):
        email: str
        password: str

router.get("/login")
async def login(payload: LoginSchema, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == payload.email))
    user = result.scalars().one_or_none()
    if not user or not verify_password(payload.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token(data={"sub": str(user.id),"role_id": str(user.role_id)})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/admin-only")
async def admin_route(user=Depends(role_required(["Admin"]))):
    return {"message": "Welcome Admin"}


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


@router.get("/search")
async def search_users(
    search: str,
    db: AsyncSession = Depends(get_db)
):

    query = select(User).where(User.name.ilike(f"%{search}%"))

    result = await db.execute(query)

    return result.scalars().all()

