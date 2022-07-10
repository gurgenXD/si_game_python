from pydantic import BaseModel


class PlayerSchema(BaseModel):
    """Player's schema."""

    user:
    points: int
