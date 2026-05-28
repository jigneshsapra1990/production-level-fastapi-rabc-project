from fastapi import Depends, HTTPException
from app.auth.jwt import get_current_user


def role_required(roles: list):
    async def checker(current_user: dict = Depends(get_current_user)):
        if current_user.get("role_id") not in roles:
            raise HTTPException(status_code=403, detail="Forbidden")
        return current_user
    return checker
