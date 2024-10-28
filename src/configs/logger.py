"""Contains logger configurations.

Docs: https://docs.python.org/3/library/logging.config.html#dictionary-schema-details
"""

from logging import INFO, NOTSET
from typing import Any, Literal


def get_default_logging_handlers() -> dict[Literal['console', 'error'], Any]:
    """Return default logging handlers."""
    return {
        'console': {
            'formatter': 'default',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        'error': {
            'formatter': 'default',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
        },
    }


def get_default_formatter(*, is_production: bool = False) -> dict[str, Any]:
    """Return default logging formatter."""
    file_path = '[{module}.py:{lineno}]' if is_production else '[{pathname}:{lineno}]'

    return {
        'style': '{',
        'datefmt': '%Y-%m-%d %H:%M:%S',
        'format': (
            '{asctime} [{processName}: {process}] [{threadName}: {thread}] '  # noqa: UP031
            '[{taskName}] [{levelname}] %s {message}' % file_path
        ),
    }


def get_logger_config(*, is_production: bool = False) -> dict[str, Any]:
    """Return logger configuration."""
    default_formatter = get_default_formatter(is_production=is_production)
    default_handlers = get_default_logging_handlers()
    log_level = INFO if is_production else NOTSET

    return {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'default': default_formatter,
        },
        'handlers': default_handlers,
        'root': {
            'handlers': ('console',),
            'propagate': False,
            'level': log_level,
        },
    }


def get_uvicorn_logger_config(*, is_production: bool = False) -> dict[str, Any]:
    """Return `uvicorn` logger configuration."""
    default_formatter = get_default_formatter(is_production=is_production)
    default_handlers = get_default_logging_handlers()
    log_level = 'INFO' if is_production else 'TRACE'

    return {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'default': default_formatter,
            'access': {
                # `()` - checks if a custom instantiation is required
                '()': 'uvicorn.logging.AccessFormatter',
                'use_colors': not is_production,
                'fmt': (
                    '%(levelprefix)s %(client_addr)s - '
                    '"%(request_line)s" %(status_code)s'
                ),
            },
        },
        'handlers': {
            **default_handlers,
            'access': {
                'formatter': 'access',
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout',
            },
        },
        'loggers': {
            'uvicorn': {
                'handlers': ('console',),
                'level': log_level,
                'propagate': False,
            },
            'uvicorn.access': {
                'handlers': ('access',),
                'level': log_level,
                'propagate': False,
            },
            'uvicorn.error': {
                'handlers': ('error',),
                'level': log_level,
                'propagate': False,
            },
            'uvicorn.asgi': {
                'handlers': ('console',),
                'level': log_level,
                'propagate': False,
            },
        },
    }
