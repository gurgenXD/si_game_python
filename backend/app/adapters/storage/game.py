from contextlib import AbstractAsyncContextManager
from typing import TYPE_CHECKING, Callable
from uuid import UUID

from sqlalchemy import exc

from app.adapters.storage.models import GameModel
from app.domain.game import GameStatus
from app.services.exceptions import NotFoundError

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class GameAdapter:
    """Game adapter."""

    def __init__(
        self, session_factory: Callable[[], AbstractAsyncContextManager["AsyncSession"]]
    ) -> None:
        self._session_factory = session_factory

    async def create(
        self,
        uuid: UUID,
        presenter_uuid: UUID,
        package_uuid: UUID,
        capacity: int,
        status: GameStatus,
        is_deleted: bool,
    ) -> None:
        """Create new game."""
        game = GameModel(
            uuid=uuid,
            presenter_uuid=presenter_uuid,
            package_uuid=package_uuid,
            capacity=capacity,
            status=status,
            is_deleted=is_deleted,
        )

        async with self._session_factory() as session:
            session.add(game)

            try:
                await session.commit()
            except exc.IntegrityError as ex:
                raise NotFoundError("Object not found.") from ex
