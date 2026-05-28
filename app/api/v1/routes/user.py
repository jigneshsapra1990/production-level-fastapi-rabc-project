from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserResponse, UserCreate
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.db.database import get_db

router = APIRouter(prefix="/users", tags=["users"])


def get_user_service(db: AsyncSession = Depends(get_db)) -> UserService:
    return UserService(UserRepository(db))


@router.post("/", response_model=UserResponse)
async def create_user(payload: UserCreate, service: UserService = Depends(get_user_service)):
    return await service.register(payload)
