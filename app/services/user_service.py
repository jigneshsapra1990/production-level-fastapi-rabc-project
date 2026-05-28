from fastapi import HTTPException
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password
from app.schemas.user import UserCreate


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def register(self, payload: UserCreate):
        if await self.repo.get_by_email(payload.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        return await self.repo.create(
            username=payload.username,
            email=payload.email,
            password=hash_password(payload.password),
            role_id=payload.role_id,
        )
