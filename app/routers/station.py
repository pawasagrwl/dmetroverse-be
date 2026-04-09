"""Station detailed information."""
from fastapi import APIRouter, Path, Query
from app.models import Lang
from app.proxy import proxy

router = APIRouter(tags=["Station Info"])


@router.get("/station/{slug}")
async def get_station(
    slug: str = Path(..., description="Station slug (from search results or menus)"),
    lang: Lang = Query(Lang.en),
):
    """Get full station details: facilities, gates, lifts, parking, timing, feeder bus."""
    return await proxy(f"{lang.value}/{slug}")


@router.get("/v2/en/station/{code}", include_in_schema=False)
async def get_station_legacy(
    code: str = Path(..., description="Station code"),
):
    """Legacy compatibility proxy for direct DMRC station calls."""
    return await proxy(f"en/{code}")

