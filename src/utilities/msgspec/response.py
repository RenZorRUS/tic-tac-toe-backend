"""Contains msgspec response for FastAPI application."""

from fastapi.responses import JSONResponse
from msgspec.json import encode as msgspec_encode
from typing import Any


class MsgSpecJSONResponse(JSONResponse):
    """Response using the high-performance `msgspec` library to serialize data to JSON."""

    def render(self: 'MsgSpecJSONResponse', content: Any) -> bytes:
        """Convert arbitrary Python data to binary JSON using the `msgspec` library."""
        return msgspec_encode(content)
