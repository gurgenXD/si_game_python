from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.domain.package import Package
    from app.domain.player import Player
    from app.domain.user import User


class Game(BaseModel):
    """Game."""

    uuid: UUID
    capacity: int
    package: "Package"
    is_active: bool
    is_paused: bool
    is_finished: bool

    presenter: "User"
    players: list["Player"]
    viewers: list["User"]
