from typing import TYPE_CHECKING

from fastapi import status
from fastapi.responses import JSONResponse

from app.services.exceptions import NotFoundError

if TYPE_CHECKING:
    from fastapi import FastAPI, Request


def add_all(app: "FastAPI") -> None:
    """Add handlers to app."""
    app.add_exception_handler(NotFoundError, _not_found_error_handler)
    app.add_exception_handler(Exception, _internal_server_error_handler)


async def _not_found_error_handler(_request: "Request", exception: "Exception") -> "JSONResponse":
    """Handler for 404 errors."""
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": str(exception)})


async def _internal_server_error_handler(
    _request: "Request", exception: "Exception"
) -> "JSONResponse":
    """Handler for 500 errors."""
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": str(exception)}
    )
