from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routes import auth, user
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth.router, prefix="/api/v1")
    app.include_router(user.router, prefix="/api/v1")

    return app


app = create_app()


@app.get("/health", tags=["Health"])
async def health():
    return {"status": "ok", "app": settings.APP_NAME}
