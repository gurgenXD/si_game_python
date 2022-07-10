from pydantic import BaseModel


class GameSchema(BaseModel):
    """Game's schema."""

    id: int
    players_max_count: int
    members: list[int]
    pack: str
    is_active: bool
    is_paused: bool
    is_finished: bool
