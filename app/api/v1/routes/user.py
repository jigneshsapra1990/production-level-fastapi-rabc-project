from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserResponse, UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.core.security import hash_password
from app.db import get_db

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse)
async def create_user(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == payload.email))
    if result.scalars().one_or_none():
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        username=payload.username,
        email=payload.email,
        password=hash_password(payload.password),
        role_id=payload.role_id,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
