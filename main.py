from fastapi import FastAPI

from app.api.v1.routes.user import router as user_router
from app.api.v1.routes.auth import router as auth_router

app = FastAPI(title="FastAPI RBAC")

app.include_router(user_router)
app.include_router(auth_router)