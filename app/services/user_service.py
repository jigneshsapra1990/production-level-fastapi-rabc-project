from app.repositories.user_repository import UserRepository
from app.core.security import hash_password
from app.schemas.user import UserCreate
from app.models.user import User


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def register(self, payload: UserCreate) -> User:
        if await self.repo.get_by_email(payload.email):
            raise ValueError("Email already registered")
        if await self.repo.get_by_username(payload.username):
            raise ValueError("Username already taken")
        user = User(
            username=payload.username,
            email=payload.email,
            password=hash_password(payload.password),
            role_id=payload.role_id,
        )
        return await self.repo.save(user)

    async def get_by_id(self, user_id) -> User:
        user = await self.repo.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    async def list_users(self, page: int = 1, limit: int = 10) -> list[User]:
        return await self.repo.get_all(offset=(page - 1) * limit, limit=limit)
