from fastapi import FastAPI

from app.api import handlers
from app.api.v1 import factory as v1_factory
from app.container import CONTAINER


def create_app():
    """Create FastAPI application."""

    settings = CONTAINER.api_settings()

    app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

    # Mount sub-applications.
    api_v1 = v1_factory.create_app(settings.title, settings.version_v1)
    handlers.add_all(api_v1)
    app.mount("/api/v1", api_v1)

    return app
