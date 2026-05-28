from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.auth.jwt import get_current_user
from app.db.database import get_db
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.services.auth_service import AuthService


def get_user_service(db: AsyncSession = Depends(get_db)) -> UserService:
    return UserService(UserRepository(db))


def get_auth_service(db: AsyncSession = Depends(get_db)) -> AuthService:
    return AuthService(UserRepository(db))


def role_required(roles: list[str]):
    async def checker(current_user: dict = Depends(get_current_user)):
        if current_user.get("role_id") not in roles:
            raise HTTPException(status_code=403, detail="Forbidden")
        return current_user
    return checker
