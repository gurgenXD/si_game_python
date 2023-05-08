from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton

from app.adapters.storage.database.provider import DatabaseProvider
from app.adapters.storage.game import GameAdapter
from app.adapters.storage.models import packages
from app.adapters.storage.package import PackageAdapter
from app.services.game import GameService
from app.services.package import PackageService
from app.settings import APISettings, DatabaseSettings, ServerSettings


class Container(DeclarativeContainer):
    """Container with dependencies."""

    api_settings = Singleton(APISettings)
    db_settings = Singleton(DatabaseSettings)
    server_settings = Singleton(ServerSettings)

    db = Singleton(
        DatabaseProvider,
        db_url=db_settings.provided.url,
        db_schema=db_settings.provided.schema_,
        echo=db_settings.provided.echo,
        pool_size=db_settings.provided.pool_size,
        max_overflow=db_settings.provided.max_overflow,
        pool_timeout=db_settings.provided.pool_timeout,
    )

    game_adapter = Singleton(GameAdapter, session_factory=db.provided.session)
    package_adapter = Singleton(PackageAdapter, session_factory=db.provided.session)

    game_service = Singleton(GameService, games=game_adapter.provided)
    package_service = Singleton(PackageService, packages=package_adapter.provided)


CONTAINER = Container()
