from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserResponse, UserCreate
from app.services.user_service import UserService
from app.api.deps import get_user_service
from app.utils.response import success_response

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=dict, status_code=201)
async def create_user(payload: UserCreate, service: UserService = Depends(get_user_service)):
    try:
        user = await service.register(payload)
        return success_response("User created successfully", UserResponse.model_validate(user).model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=dict)
async def list_users(page: int = 1, limit: int = 10, service: UserService = Depends(get_user_service)):
    users = await service.list_users(page=page, limit=limit)
    return success_response("Users fetched successfully", [UserResponse.model_validate(u).model_dump() for u in users])


@router.get("/{user_id}", response_model=dict)
async def get_user(user_id: str, service: UserService = Depends(get_user_service)):
    try:
        user = await service.get_by_id(user_id)
        return success_response("User fetched successfully", UserResponse.model_validate(user).model_dump())
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
