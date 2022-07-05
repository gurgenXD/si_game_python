from typing import TYPE_CHECKING

from utils.settings.base import BaseSettings

if TYPE_CHECKING:
    from utils.pyproject import PyProjectData


class AppSettings(BaseSettings):
    """Application settings."""

    # Environment.
    env: str
    # App title.
    title: str
    # App version.
    version: str

    class Config:
        env_prefix = "app_"

    def __init__(self, pyproject_data: "PyProjectData", *args, **kwargs):
        """Set pyproject data to variables."""

        if not kwargs.get("title"):
            kwargs["title"] = pyproject_data.get_app_name()

        if not kwargs.get("version"):
            kwargs["version"] = pyproject_data.get_app_version()

        super().__init__(*args, **kwargs)
