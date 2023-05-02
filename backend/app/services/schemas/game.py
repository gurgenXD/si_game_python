from pydantic import BaseModel
from uuid import UUID


class GameSchema(BaseModel):
    """Game's schema."""

    id: UUID
    players_max_count: int
    members: list[int]
    pack: str
    is_active: bool
    is_paused: bool
    is_finished: bool
