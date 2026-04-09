"""Tourism and Places to Visit."""
from fastapi import APIRouter, Query
from app.models import Lang
from app.proxy import proxy

router = APIRouter(tags=["Tourism"])

@router.get("/tour")
async def get_tour(lang: Lang = Query(Lang.en)):
    """Get tourist places and nearest metro stations."""
    # Note: Currently returns 404 from DMRC API in production.
    return await proxy(f"{lang.value}/tour")
