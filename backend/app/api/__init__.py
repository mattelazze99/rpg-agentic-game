"""API routing package.

Defines a root APIRouter that can be used to include all subrouters if desired.
Individual modules such as `session` and `world` also expose their own routers.
"""

from fastapi import APIRouter

# Root router can be used to aggregate sub‑routers
router = APIRouter()