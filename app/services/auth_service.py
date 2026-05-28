from fastapi import HTTPException
from app.repositories.user_repository import UserRepository
from app.core.security import verify_password
from app.auth.jwt import create_access_token


class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def login(self, email: str, password: str) -> dict:
        user = await self.repo.get_by_email(email)
        if not user or not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Invalid email or password")
        token = create_access_token(data={"sub": str(user.id), "role_id": str(user.role_id)})
        return {"access_token": token, "token_type": "bearer"}
