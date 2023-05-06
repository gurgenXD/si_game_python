from utils.settings.base import BaseSettings


class APISettings(BaseSettings):
    """API settings."""

    # Environment.
    env: str
    # API title.
    title: str = "si_game"
    # API v1 version.
    version_v1: str

    class Config:
        env_prefix = "api_"
