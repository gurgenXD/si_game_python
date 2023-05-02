from pydantic import BaseModel
from uuid import UUID


class Game(BaseModel):
    """Game."""

    uuid: UUID
    players_max_count: int
    members: list[int]
    pack: str
    is_active: bool
    is_paused: bool
    is_finished: bool
