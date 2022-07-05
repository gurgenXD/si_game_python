from fastapi import FastAPI

from app.container import CONTAINER


def create_app():
    """Create FastAPI application."""

    settings = CONTAINER.app_settings()

    app = FastAPI(
        title=settings.title, version=settings.version, docs_url="/", redoc_url=None
    )

    return app
