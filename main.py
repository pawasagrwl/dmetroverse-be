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
# Permissive CORS - Accessible from anywhere
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
    """Redirects the base API URL directly to the Frontend."""
    return RedirectResponse(url=FRONTEND_URL)

@app.get("/help", tags=["Root"])
async def help_page():
    """Redirects to the Swagger UI docs which provides a visual guide to the API."""
    return RedirectResponse(url="/docs")
