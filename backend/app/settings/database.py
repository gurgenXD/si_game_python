from utils.settings.base import BaseSettings


class DatabaseSettings(BaseSettings):
    """Database settings."""

    # Database user.
    user: str
    # Database password.
    password: str
    # Database host.
    host: str
    # Database port.
    port: int
    # Database name.
    name: str
    # Database app schema.
    schema_: str

    # Database url schema.
    url_schema: str = "postgresql"
    # Async driver for connection to database.
    async_driver: str = "asyncpg"

    # Min size of database connections.
    pool_size: int = 1
    # Max size of database connections.
    max_overflow: int = 5
    # Database connections lifetime in seconds after usage.
    pool_timeout: int = 5
    # Log engine messages.
    echo: bool = False

    class Config:
        env_prefix = "database_"

    @property
    def url(self) -> str:
        """Database url with anync driver."""
        schema = f"{self.url_schema}+{self.async_driver}"
        connection = f"{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
        return f"{schema}://{connection}"
