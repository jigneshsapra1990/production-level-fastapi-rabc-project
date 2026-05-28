from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.core.security import verify_password
from app.auth.jwt import create_access_token
from app.db.database import get_db
from app.api.deps import role_required
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["auth"])


class LoginSchema(BaseModel):
    email: str
    password: str


@router.post("/login")
async def login(payload: LoginSchema, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == payload.email))
    user = result.scalars().one_or_none()
    if not user or not verify_password(payload.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token(data={"sub": str(user.id), "role_id": str(user.role_id)})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/admin-only")
async def admin_route(user=Depends(role_required(["Admin"]))):
    return {"message": "Welcome Admin"}
