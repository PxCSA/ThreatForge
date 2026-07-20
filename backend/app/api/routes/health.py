from fastapi import APIRouter
from backend.app.core.config import settings

router = APIRouter()


@router.get("/health", tags=["Health"])
def health():
    return {
        "status": "healthy",
        "debug": settings.DEBUG,
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }