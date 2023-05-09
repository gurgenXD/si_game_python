from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from app.services.types.game_status import GameStatusType


if TYPE_CHECKING:
    from app.adapters.storage.game import GameAdapter
    from app.services.schemas.game import GameCreateSchema, GameSchema


class GameService:
    """Game service."""

    def __init__(self, games: "GameAdapter") -> None:
        self._games = games

    async def create(self, game: "GameCreateSchema") -> None:
        """Create new game."""
        await self._games.create(
            uuid=uuid4(),
            presenter_uuid=game.presenter_uuid,
            package_uuid=game.package_uuid,
            capacity=game.capacity,
            status=GameStatusType.CREATED,
            is_deleted=False,
        )

    async def get_all(
        self, status: GameStatusType | None, presenter_uuid: UUID | None, package_uuid: UUID | None
    ) -> list["GameSchema"]:
        """Get games."""
        await self._games.get_all(
            status=status, presenter_uuid=presenter_uuid, package_uuid=package_uuid
        )

    async def get(self, uuid: UUID) -> "GameSchema":
        """Get game."""
        return await self._games.get(uuid=uuid)
