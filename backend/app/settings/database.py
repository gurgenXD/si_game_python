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
    url_schema: str
    # Async driver for connection to database.
    async_driver: str

    # Min size of database connections.
    min_pool_size: int
    # Max size of database connections.
    max_pool_size: int
    # Database connections lifetime in seconds after usage.
    connection_timeout_seconds: int

    class Config:
        env_prefix = "database_"

    @property
    def url(self) -> str:
        """Database url with anync driver."""
        schema = f"{self.url_schema}+{self.async_driver}"
        connection = f"{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
        return f"{schema}://{connection}"
