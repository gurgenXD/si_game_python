from contextlib import AbstractAsyncContextManager
from typing import TYPE_CHECKING, Callable
from uuid import UUID

from sqlalchemy import exc, select

from app.adapters.storage.models import GameModel
from app.services.exceptions import NotFoundError
from app.services.types.game_status import GameStatusType

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
        status: GameStatusType,
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

    async def get_all(
        self, status: GameStatusType | None, presenter_uuid: UUID | None, package_uuid: UUID | None
    ) -> list[dict]:
        """Get games."""
        query = select(GameModel)

        if status:
            query = query.where(GameModel.status == status)

        if presenter_uuid:
            query = query.where(GameModel.presenter_uuid == presenter_uuid)

        if package_uuid:
            query = query.where(GameModel.package_uuid == package_uuid)

        async with self._session_factory() as session:
            games = (await session.execute(query)).all()

            print(games)

            await session.commit()

    async def get(self, uuid: UUID) -> dict:
        """Get game."""
        query = select(GameModel).where(GameModel.uuid == uuid)

        async with self._session_factory() as session:
            game = (await session.execute(query)).first()

            if not game:
                raise NotFoundError("Object not found.")

            await session.commit()