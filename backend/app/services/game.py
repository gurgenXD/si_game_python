from dataclasses import dataclass

from services.interfaces.game import GameStorageInterface


@dataclass
class GameService:
    """Game Service."""

    _storage: "GameStorageInterface"

    def create(self, password: str, players_max_count: int, pack: int) -> None:
        """Create new game."""
        self._storage.create(password, players_max_count, pack)
