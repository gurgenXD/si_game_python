from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton

from app.settings import AppSettings, DatabaseSettings, ServerSettings
from utils.pyproject import PyProjectData


class Container(DeclarativeContainer):
    """Container with dependencies."""

    pyproject_data: Singleton["PyProjectData"] = Singleton(PyProjectData)

    app_settings: Singleton["AppSettings"] = Singleton(AppSettings, pyproject_data.provided)
    db_settings: Singleton["DatabaseSettings"] = Singleton(DatabaseSettings)
    server_settings: Singleton["ServerSettings"] = Singleton(ServerSettings)


CONTAINER = Container()
