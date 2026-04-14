"""Application entrypoint.

Defines a factory for creating the FastAPI application and registers API routers.
In development you can run the app via `uvicorn app.main:app --reload`.
"""

from fastapi import FastAPI

from .api.session import router as session_router
from .api.world import router as world_router


def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance.

    Returns
    -------
    FastAPI
        The configured FastAPI application with all routers registered.
    """
    app = FastAPI(title="Multi‑Agent RPG API", version="0.1.0")
    # Session management endpoints
    app.include_router(session_router, prefix="/session", tags=["session"])
    # World/setting endpoints
    app.include_router(world_router, prefix="/world", tags=["world"])
    return app


# Create a default app instance for ASGI servers
app = create_app()