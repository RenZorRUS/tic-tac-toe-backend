"""Application entry point."""

from collections.abc import AsyncIterator
from configs.logger import get_logger_config, get_uvicorn_logger_config
from configs.server import ServerConfig, get_server_config
from contextlib import asynccontextmanager as async_context_manager
from fastapi import FastAPI
from logging import getLogger
from logging.config import dictConfig
from routers.router import add_app_routes
from sys import argv as sys_argv
from utilities.msgspec.response import MsgSpecJSONResponse
from uvicorn import run as run_asgi_server


@async_context_manager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """FastAPI application lifespan."""
    logger = getLogger(__name__)

    add_app_routes(app)

    logger.info('Application initialized, starting...')
    yield
    logger.info('Shutting down application...')


def create_app(server_config: ServerConfig, /, *, is_production: bool = False) -> FastAPI:
    """Create FastAPI application."""
    return FastAPI(
        debug=not is_production,
        title=server_config.title,
        summary=server_config.summary,
        description=server_config.description,
        version=server_config.version,
        root_path=server_config.api_prefix,
        lifespan=lifespan,
        default_response_class=MsgSpecJSONResponse,
        openapi_url='/openapi.json' if not is_production else None,
        docs_url='/docs' if not is_production else None,
        redoc_url='/redoc' if not is_production else None,
        swagger_ui_oauth2_redirect_url='/docs/oauth2-redirect'
        if not is_production
        else None,
    )


if __name__ == '__main__':
    is_production = '--prod' in sys_argv

    server_config = get_server_config(is_production=is_production)
    uvicorn_logger_config = get_uvicorn_logger_config(is_production=is_production)
    logger_config = get_logger_config(is_production=is_production)

    app = create_app(server_config, is_production=is_production)

    # NOTE: We must configure the logger before running the server.
    dictConfig(logger_config)

    # NOTE: We must pass the app as an import string to enable 'reload' or 'workers'.
    run_asgi_server(
        app,
        host=server_config.host,
        port=server_config.port,
        loop='uvloop',
        http='httptools',
        use_colors=not is_production,
        log_config=uvicorn_logger_config,
    )
