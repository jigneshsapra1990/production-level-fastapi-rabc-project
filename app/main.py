from fastapi import FastAPI
from app.api.v1.routes import auth, user

app = FastAPI(title="FastAPI RBAC")

app.include_router(auth.router, prefix="/api/v1")
app.include_router(user.router, prefix="/api/v1")


@app.get("/health")
async def health():
    return {"status": "ok"}
