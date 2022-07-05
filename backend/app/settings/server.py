from utils.settings.base import BaseSettings


class ServerSettings(BaseSettings):
    """Server settings."""

    # The ASGI application to run, in the format "<module>:<attribute>".
    app: str = "app.api.factory:create_app"
    # Treat APP as an application factory, i.e. a () -> <ASGI app> callable.
    factory: bool = True
    # Worker processes count.
    workers: int = 1
    # Development mode.
    debug: bool = False
    # Logging level.
    log_level: str = "info"
    # Event loop.
    loop: str = "auto"
    # Application host.
    host: str
    # Application port.
    port: int

    class Config:
        env_prefix = "server_"
