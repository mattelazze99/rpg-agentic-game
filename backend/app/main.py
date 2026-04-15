"""FastAPI application entrypoint."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from .api.root import router as root_router
from .api.session import router as session_router
from .api.world import router as world_router
from .core.config import settings
from .core.database import engine
from .models import Base


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title=settings.app_name, version="0.1.0", lifespan=lifespan)
Base.metadata.create_all(bind=engine)
app.include_router(root_router)
app.include_router(session_router)
app.include_router(world_router)
