from fastapi import FastAPI

from app.api.v1 import factory as v1_factory
from app.container import CONTAINER


def create_app():
    """Create FastAPI application."""

    settings = CONTAINER.app_settings()

    app = FastAPI(title=settings.title, version=settings.version, docs_url=None, redoc_url=None)

    api_v1 = v1_factory.create_app(settings.title, settings.version)
    app.mount("/api/v1", api_v1)

    return app
