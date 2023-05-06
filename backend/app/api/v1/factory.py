from fastapi import FastAPI

from app.api.v1.routers import games, users


def create_app(title: str, version: str):
    """Create FastAPI application."""

    app = FastAPI(title=title, version=version)

    app.include_router(games.router)
    app.include_router(users.router)

    return app
