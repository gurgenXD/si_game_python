from abc import abstractmethod
from typing import Protocol


class GameStorageInterface(Protocol):
    """Game storage interface."""

    @abstractmethod
    def create(self, hashed_password: str, players_max_count: int, pack: int) -> None:
        """Create new game."""
