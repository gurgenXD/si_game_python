import click
import uvicorn

from app.container import CONTAINER


@click.group()
def start() -> None:
    """Run service."""


@start.command()
def api() -> None:
    """Run API service."""
    uvicorn.run(**CONTAINER.server_settings().dict())
