"""Contains application routers."""

from fastapi import APIRouter, FastAPI


def add_app_routes(app: FastAPI) -> None:
    """Add all API routes to the FastAPI application."""
    router = APIRouter()

    @router.get('/status')
    async def get_health_status_async() -> dict[str, str]:
        return {'status': 'ok'}

    app.include_router(router)
