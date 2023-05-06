from typing import TYPE_CHECKING
from uuid import uuid4

from app.domain.game import GameStatus

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
