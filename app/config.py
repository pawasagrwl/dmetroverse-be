"""
Configuration and constants.
"""
import os

# --- DMRC Backend ---
API_BASE = "https://backend.delhimetrorail.com"
API_URL = f"{API_BASE}/api/v2"

DMRC_HEADERS = {
    "Referer": "https://delhimetrorail.com/",
    "Origin": "https://delhimetrorail.com",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/135.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
}

# Origins allowed to call this API.
# Set ALLOWED_ORIGINS env var as comma-separated list to override.
_default_origins = [
    "http://pawasagrwl.github.io",
    "https://pawasagrwl.github.io",
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:8000",
]

ALLOWED_ORIGINS: list[str] = [
    o.strip()
    for o in os.getenv("ALLOWED_ORIGINS", ",".join(_default_origins)).split(",")
    if o.strip()
]

# When True, the access-control middleware is active.
# Set RESTRICT_ACCESS=false to disable (e.g. for local dev).
RESTRICT_ACCESS: bool = os.getenv("RESTRICT_ACCESS", "true").lower() == "true"

# --- GitHub Pages frontend ---
FRONTEND_URL = os.getenv("FRONTEND_URL", "https://pawasagrwl.github.io/dmetroverse")
