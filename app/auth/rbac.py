from fastapi import Depends, HTTPException


def role_required(roles: list):

    async def checker(current_user=Depends()):

        if current_user.role.name not in roles:
            raise HTTPException(403, "Permission Denied")

        return current_user

    return checker