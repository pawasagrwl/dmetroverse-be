"""
DMetroverse Backend — DMRC API Proxy
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.routers import journey, status, station, cms, corporate, tenders, tourism
from app.middleware import AccessControlMiddleware
from app.proxy import shutdown_client
from app.config import FRONTEND_URL

app = FastAPI(
    title="DMetroverse API",
    description="Complete proxy wrapper for Delhi Metro Rail Corporation backend APIs.",
    version="1.0.0",
)

# --- Middleware ---
# 1. Custom Access Control (Blocks non-allowed Origins)
app.add_middleware(AccessControlMiddleware)

# 2. CORS (Allows browser to access if Origin is allowed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Fine because AccessControlMiddleware restricts origins first
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Register routers ---
app.include_router(journey.router)
app.include_router(status.router)
app.include_router(station.router)
app.include_router(cms.router)
app.include_router(corporate.router)
app.include_router(tenders.router)
app.include_router(tourism.router)

# --- Lifecycle Events ---
@app.on_event("shutdown")
async def shutdown_event():
    await shutdown_client()


# --- Root & Help Routes ---
@app.get("/", tags=["Root"])
async def root():
    return {
        "service": "DMetroverse API",
        "description": "Proxy for DMRC routing and information.",
        "docs": "/docs",
        "frontend": FRONTEND_URL
    }

@app.get("/help", tags=["Root"])
async def help_page():
    """Redirects to the Swagger UI docs which provides a visual guide to the API."""
    return RedirectResponse(url="/docs")
