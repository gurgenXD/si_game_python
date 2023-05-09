from collections.abc import Callable
from contextlib import AbstractContextManager, asynccontextmanager

from sqlalchemy import orm
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine


class DatabaseProvider:
    """Database provider."""

    def __init__(
        self,
        db_url: str,
        db_schema: str,
        pool_size: int,
        max_overflow: int,
        pool_timeout: int,
        *,
        echo: bool,
    ) -> None:
        self._engine = create_async_engine(
            url=db_url,
            pool_size=pool_size,
            max_overflow=max_overflow,
            pool_timeout=pool_timeout,
            echo=echo,
            connect_args={"server_settings": {"search_path": db_schema}},
        )
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                bind=self._engine,
                class_=AsyncSession,
                autocommit=False,
                autoflush=False,
                expire_on_commit=True,
            )
        )

    def get_engine(self) -> "AsyncEngine":
        """Get engine."""
        return self._engine

    @asynccontextmanager
    async def session(self) -> Callable[[], AbstractContextManager["AsyncSession"]]:
        """Scoped session context manager."""
        session: "AsyncSession" = self._session_factory()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
