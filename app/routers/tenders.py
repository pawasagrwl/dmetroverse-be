"""Tender details and categories."""
from fastapi import APIRouter, Path, Query
from app.models import Lang
from app.proxy import proxy

router = APIRouter(tags=["Tenders"])


@router.get("/tender-categories")
async def get_tender_categories(lang: Lang = Query(Lang.en)):
    """Get list of tender categories."""
    return await proxy(f"{lang.value}/tenderscategory")


@router.get("/tenders/{category_id}")
async def get_tenders(
    category_id: int = Path(..., description="Tender category ID"),
    page: int = Query(1, ge=1, description="Page number (10 per page)"),
    lang: Lang = Query(Lang.en),
):
    """Get tenders for a specific category (paginated)."""
    return await proxy(f"{lang.value}/tenders_by_category/{category_id}/?page={page}")
