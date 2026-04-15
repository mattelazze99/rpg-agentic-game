"""Root and health endpoints."""

from fastapi import APIRouter

router = APIRouter(tags=["meta"])


@router.get("/")
def root() -> dict:
    return {
        "name": "Multi-Agent RPG V1",
        "status": "ok",
        "message": "Backend is running.",
        "docs": "/docs",
        "health": "/health",
    }


@router.get("/health")
def health() -> dict:
    return {"status": "ok"}
