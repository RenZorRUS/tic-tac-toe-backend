"""Contains server configurations."""

from dataclasses import dataclass
from dotenv import dotenv_values
from functools import lru_cache
from utilities.common import get_env_file_name


@dataclass(frozen=True, slots=True)
class ServerConfig:
    """Contain server configurations."""

    host: str
    port: int
    api_prefix: str
    title: str
    summary: str
    description: str
    version: str


@lru_cache(maxsize=1)
def get_server_config(*, is_production: bool = False) -> ServerConfig:
    """Return server configurations."""
    env_file_name = get_env_file_name(is_production=is_production)
    env_config = dotenv_values(env_file_name, encoding='utf-8')

    return ServerConfig(
        host=env_config.get('APP_HOST', 'localhost'),
        port=int(env_config.get('APP_PORT', 8081)),
        api_prefix=env_config.get('API_PREFIX', '/api'),
        title=env_config.get('APP_TITLE', 'Tic-tac-toe Backend API'),
        summary=env_config.get('APP_SUMMARY', 'A backend API for a Tic-tac-toe game.'),
        description=env_config.get('APP_DESCRIPTION', ''),
        version=env_config.get('APP_VERSION', '0.0.1'),
    )
