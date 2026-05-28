from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import LoginSchema, TokenResponse
from app.services.auth_service import AuthService
from app.api.deps import get_auth_service, role_required
from app.utils.response import success_response

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=dict)
async def login(payload: LoginSchema, service: AuthService = Depends(get_auth_service)):
    try:
        token = await service.login(payload.email, payload.password)
        return success_response("Login successful", token)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.get("/admin-only", dependencies=[Depends(role_required(["Admin"]))])
async def admin_route():
    return success_response("Welcome Admin")
