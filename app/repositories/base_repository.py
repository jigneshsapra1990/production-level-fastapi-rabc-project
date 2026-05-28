from typing import Generic, TypeVar, Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.base import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db: AsyncSession):
        self.model = model
        self.db = db

    async def get_by_id(self, id) -> ModelType | None:
        result = await self.db.execute(select(self.model).where(self.model.id == id))
        return result.scalars().one_or_none()

    async def get_all(self, offset: int = 0, limit: int = 10) -> list[ModelType]:
        result = await self.db.execute(select(self.model).offset(offset).limit(limit))
        return result.scalars().all()

    async def save(self, instance: ModelType) -> ModelType:
        self.db.add(instance)
        await self.db.commit()
        await self.db.refresh(instance)
        return instance

    async def delete(self, instance: ModelType) -> None:
        await self.db.delete(instance)
        await self.db.commit()
