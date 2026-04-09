"""
Access-control middleware.

Validates the Origin / Referer header on every request.
Only origins listed in config.ALLOWED_ORIGINS are allowed through.
"""
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from app.config import ALLOWED_ORIGINS, RESTRICT_ACCESS


class AccessControlMiddleware(BaseHTTPMiddleware):
    """Block requests that don't come from an allowed origin."""

    async def dispatch(self, request: Request, call_next) -> Response:
        if not RESTRICT_ACCESS:
            return await call_next(request)

        # Always let through: docs, openapi schema, health, root redirect
        path = request.url.path
        if path in ("/", "/help", "/openapi.json", "/docs", "/redoc"):
            return await call_next(request)

        origin = request.headers.get("origin") or request.headers.get("referer") or ""

        # Allow if origin is completely empty (direct browser navigation or cURL)
        if not origin:
            return await call_next(request)

        if not _is_allowed(origin):
            return JSONResponse(
                status_code=403,
                content={"detail": "Access denied. This API is private."},
            )

        return await call_next(request)


def _is_allowed(origin: str) -> bool:
    """Check if the origin matches any allowed origin."""
    origin = origin.rstrip("/")
    for allowed in ALLOWED_ORIGINS:
        allowed = allowed.rstrip("/")
        if origin == allowed or origin.startswith(allowed):
            return True
    return False
