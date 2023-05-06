from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton

from app.adapters.storage.database import Database
from app.settings import APISettings, DatabaseSettings, ServerSettings


class Container(DeclarativeContainer):
    """Container with dependencies."""

    api_settings = Singleton(APISettings)
    db_settings = Singleton(DatabaseSettings)
    server_settings = Singleton(ServerSettings)

    db = Singleton(
        Database,
        db_url=db_settings.provided.url,
        db_schema=db_settings.provided.schema_,
        echo=db_settings.provided.echo,
        pool_size=db_settings.provided.pool_size,
        max_overflow=db_settings.provided.max_overflow,
        pool_timeout=db_settings.provided.pool_timeout,
    )


CONTAINER = Container()
