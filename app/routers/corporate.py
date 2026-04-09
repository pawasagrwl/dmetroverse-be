"""Corporate information: careers, press releases, and news."""
from typing import Optional
from fastapi import APIRouter, Path, Query
from app.models import Lang
from app.proxy import proxy

router = APIRouter(tags=["Corporate"])


@router.get("/career")
async def get_career(
    page: int = Query(1, ge=1, description="Page number (10 per page)"),
    lang: Lang = Query(Lang.en),
):
    """Get current job vacancies (paginated)."""
    return await proxy(f"{lang.value}/career/?page={page}")


@router.get("/archived-career")
async def get_archived_career(
    page: int = Query(1, ge=1, description="Page number"),
    lang: Lang = Query(Lang.en),
):
    """Get archived/past job vacancies (paginated)."""
    return await proxy(f"{lang.value}/archived_career/?page={page}")


@router.get("/press-releases")
async def get_press_releases(lang: Lang = Query(Lang.en)):
    """Get list of press releases."""
    return await proxy(f"{lang.value}/pressrelease")


@router.get("/press-releases/{slug}")
async def get_press_release_detail(
    slug: str = Path(..., description="Press release page slug"),
    lang: Lang = Query(Lang.en),
):
    """Get a single press release by slug."""
    return await proxy(f"{lang.value}/pressrelease_details/{slug}")


@router.get("/news")
async def get_news(
    month: Optional[int] = Query(None, ge=1, le=12, description="Filter by month (1-12)"),
    year: Optional[int] = Query(None, ge=2000, description="Filter by year"),
    lang: Lang = Query(Lang.en),
):
    """Get news articles, optionally filtered by month and year."""
    params = []
    if month is not None:
        params.append(f"month={month}")
    if year is not None:
        params.append(f"year={year}")
    qs = f"?{'&'.join(params)}" if params else ""
    return await proxy(f"{lang.value}/news/{qs}")


@router.get("/news/{news_id}")
async def get_news_detail(
    news_id: int = Path(..., description="News article ID"),
    lang: Lang = Query(Lang.en),
):
    """Get a single news article by ID."""
    return await proxy(f"{lang.value}/news_details/{news_id}")
