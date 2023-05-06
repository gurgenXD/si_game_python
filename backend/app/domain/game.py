from enum import StrEnum
from uuid import UUID

from pydantic import BaseModel

from app.domain.package import Package
from app.domain.player import Player
from app.domain.user import User


class GameStatus(StrEnum):
    """Game status."""

    CREATED = "CREATED"
    STARTED = "STARTED"
    PAUSED = "PAUSED"
    FINISHED = "FINISHED"


class Game(BaseModel):
    """Game."""

    uuid: UUID
    capacity: int
    status: GameStatus
    presenter: User
    package: Package
    is_deleted: bool

    players: list[Player]
    viewers: list[User]
