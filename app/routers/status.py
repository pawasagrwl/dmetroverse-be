"""Service status and line information."""
from fastapi import APIRouter, Query
from app.models import Lang
from app.proxy import proxy

router = APIRouter(tags=["Service Status"])


@router.get("/lines")
async def get_lines(lang: Lang = Query(Lang.en)):
    """Get all metro lines with current service status."""
    return await proxy(f"{lang.value}/line_list")


@router.get("/service-info")
async def get_service_info(lang: Lang = Query(Lang.en)):
    """Get current service alerts and information."""
    return await proxy(f"{lang.value}/service_information")
