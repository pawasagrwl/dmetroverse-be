"""CMS pages and Navigation Menus."""
from fastapi import APIRouter, Path, Query
from app.models import Lang
from app.proxy import proxy

router = APIRouter(tags=["CMS"])


@router.get("/menus")
async def get_menus(lang: Lang = Query(Lang.en)):
    """Get the full navigation menu tree."""
    return await proxy(f"{lang.value}/menus")


@router.get("/page/{slug:path}")
async def get_page(
    slug: str = Path(..., description="CMS page slug (supports nested paths)"),
    lang: Lang = Query(Lang.en),
):
    """Get a generic CMS page by its slug."""
    return await proxy(f"{lang.value}/{slug}")
