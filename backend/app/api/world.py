"""World API endpoints.

Provides endpoints for retrieving the generated world or setting data.  In V1
this is a placeholder returning an uninitialised world summary.
"""

from fastapi import APIRouter

from ..schemas.world_schema import WorldResponse


router = APIRouter()


@router.get("/", response_model=WorldResponse)
def get_world() -> WorldResponse:
    """Retrieve the current world summary.

    Returns
    -------
    WorldResponse
        A placeholder summary until world generation is implemented.
    """
    return WorldResponse(summary="World has not been generated yet.")