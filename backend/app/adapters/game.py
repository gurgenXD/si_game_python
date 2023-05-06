from contextlib import AbstractAsyncContextManager
from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable

from app.models import GameModel
from app.services.interfaces.game import GameStorageInterface

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class GameAdapter(GameStorageInterface):
    _session_factory = Callable[[], AbstractAsyncContextManager["AsyncSession"]]

    _game_model = GameModel

    def create(self, hashed_password: str, players_max_count: int, pack: int) -> None:
        """Create new game."""
        game = self._game_model(
            hashed_password=hashed_password,
            players_max_count=players_max_count,
            showman=None,
            pack=pack,
            is_active=False,
            is_paused=False,
            is_finished=False,
        )

        with self._session_factory() as session:
            session.add(game)
