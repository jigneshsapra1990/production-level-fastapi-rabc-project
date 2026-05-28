from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.auth_service import AuthService
from app.repositories.user_repository import UserRepository
from app.db.database import get_db
from app.api.deps import role_required
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["auth"])


class LoginSchema(BaseModel):
    email: str
    password: str


def get_auth_service(db: AsyncSession = Depends(get_db)) -> AuthService:
    return AuthService(UserRepository(db))


@router.post("/login")
async def login(payload: LoginSchema, service: AuthService = Depends(get_auth_service)):
    return await service.login(payload.email, payload.password)


@router.get("/admin-only")
async def admin_route(user=Depends(role_required(["Admin"]))):
    return {"message": "Welcome Admin"}
