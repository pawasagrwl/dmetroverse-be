"""
Async DMRC backend proxy client.
"""
import httpx
from fastapi import HTTPException
from app.config import API_URL, DMRC_HEADERS

# Reusable async client — keeps connections alive across requests.
_client: httpx.AsyncClient | None = None


def _get_client() -> httpx.AsyncClient:
    global _client
    if _client is None or _client.is_closed:
        _client = httpx.AsyncClient(headers=DMRC_HEADERS, timeout=15.0)
    return _client


async def proxy(path: str) -> dict | list | str:
    """Proxy a GET request to the DMRC backend API."""
    url = f"{API_URL}/{path}"
    client = _get_client()
    try:
        resp = await client.get(url)
    except httpx.RequestError as exc:
        raise HTTPException(status_code=502, detail=f"Failed to reach DMRC backend: {exc}")

    if resp.status_code != 200:
        raise HTTPException(
            status_code=resp.status_code,
            detail=f"DMRC API returned {resp.status_code}",
        )

    try:
        return resp.json()
    except ValueError:
        raise HTTPException(status_code=502, detail="DMRC API returned non-JSON response")


async def shutdown_client():
    """Close the shared HTTP client (called on app shutdown)."""
    global _client
    if _client and not _client.is_closed:
        await _client.aclose()
        _client = None
