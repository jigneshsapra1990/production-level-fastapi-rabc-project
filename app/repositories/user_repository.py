from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_email(self, email: str) -> User | None:
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalars().one_or_none()

    async def create(self, username: str, email: str, password: str, role_id) -> User:
        user = User(username=username, email=email, password=password, role_id=role_id)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
