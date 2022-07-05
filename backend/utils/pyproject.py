import tomli
from pydantic import BaseModel

from utils.constants import BASE_DIR

_PYPROJECT_PATH = BASE_DIR / "pyproject.toml"


class PoetryToolData(BaseModel):
    """Data from pyproject.tool.poetry."""

    name: str
    version: str
    description: str
    authors: list[str]


class ToolsData(BaseModel):
    """Data from pyproject.tool."""

    poetry: PoetryToolData


class PyProjectData(BaseModel):
    """Data from pyproject.toml."""

    def __init__(self) -> None:
        super().__init__(**tomli.load(_PYPROJECT_PATH.open(mode="rb")))

    tool: ToolsData

    def get_app_name(self) -> str:
        """Get app name."""
        return self.tool.poetry.name

    def get_app_version(self) -> str:
        """Get app version."""
        return self.tool.poetry.version
