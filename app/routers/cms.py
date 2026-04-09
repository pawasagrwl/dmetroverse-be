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


@router.get("/reddit-posts", include_in_schema=False)
async def get_reddit_posts():
    """Proxy reddit posts for the old frontend."""
    # We'll use the existing proxy infrastructure if possible, or direct httpx
    import httpx
    async with httpx.AsyncClient() as client:
        # standard reddit hot feed for /r/delhi
        url = "https://www.reddit.com/r/delhi/hot.json"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        res = await client.get(url, headers=headers)
        return res.json()

