from fastapi import FastAPI

from backend.app.api.router import api_router
from backend.app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(api_router)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME} "
    }