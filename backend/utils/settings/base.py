from pydantic import BaseSettings as PydanticBaseSettings

_ENV_FILE = ".env"
_ENV_FILE_ENCODING = "utf-8"


class BaseSettings(PydanticBaseSettings):
    """Base class for reading configs from the environment and file."""

    class Config:
        """Class for static configurations."""

        env_file = _ENV_FILE
        env_file_encoding = _ENV_FILE_ENCODING
