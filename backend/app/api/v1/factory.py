from fastapi import FastAPI

from app.api.v1.routers import games, packages, users


def create_app(title: str, version: str) -> "FastAPI":
    """Create FastAPI application."""
    app = FastAPI(title=title, version=version)

    app.include_router(games.router)
    app.include_router(users.router)
    app.include_router(packages.router)

    return app
