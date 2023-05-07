from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from app.domain.game import Game, GameStatus

if TYPE_CHECKING:
    from app.adapters.storage.game import GameAdapter
    from app.services.schemas.game import GameCreateSchema


class GameService:
    """Game Service."""

    def __init__(self, games: "GameAdapter") -> None:
        self._games = games

    async def create(self, game: "GameCreateSchema") -> None:
        """Create new game."""
        await self._games.create(
            uuid=uuid4(),
            presenter_uuid=game.presenter_uuid,
            package_uuid=game.package_uuid,
            capacity=game.capacity,
            status=GameStatus.CREATED,
            is_deleted=False,
        )

    async def get_all(
        self, status: GameStatus | None, presenter_uuid: UUID | None, package_uuid: UUID | None
    ) -> list["Game"]:
        """Get games."""
        await self._games.get_all(
            status=status, presenter_uuid=presenter_uuid, package_uuid=package_uuid
        )

    async def get(self, uuid: UUID) -> "Game":
        """Get game."""
        await self._games.get(uuid=uuid)
