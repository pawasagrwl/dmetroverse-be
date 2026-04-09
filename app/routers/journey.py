"""Station search & route planning."""
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Path, Query
from app.models import Lang, RouteType
from app.proxy import proxy

router = APIRouter(tags=["Journey"])


@router.get("/search/{keyword}")
async def search_station(
    keyword: str = Path(..., description="Station name or partial keyword"),
    lang: Lang = Query(Lang.en),
):
    """Search for metro stations by keyword."""
    return await proxy(f"{lang.value}/station_by_keyword/all/{keyword}")


@router.get("/route/{from_code}/{to_code}")
async def get_route(
    from_code: str = Path(..., description="Source station code (e.g. KG)"),
    to_code: str = Path(..., description="Destination station code (e.g. RCK)"),
    route_type: RouteType = Query(RouteType.least_distance, description="Routing strategy"),
    time: Optional[str] = Query(None, description="ISO datetime; defaults to now"),
    lang: Lang = Query(Lang.en),
):
    """Get route, fare, and timing between two stations."""
    dt = time or datetime.now().isoformat()
    return await proxy(
        f"{lang.value}/station_route/{from_code}/{to_code}/{route_type.value}/{dt}"
    )


@router.get("/{from_code}/{to_code}/{route_type}", include_in_schema=False)
async def get_route_legacy(
    from_code: str = Path(...),
    to_code: str = Path(...),
    route_type: str = Path(...),
    lang: Lang = Query(Lang.en),
):
    """Legacy compatibility route for old frontend."""
    dt = datetime.now().isoformat()
    return await proxy(
        f"{lang.value}/station_route/{from_code}/{to_code}/{route_type}/{dt}"
    )
