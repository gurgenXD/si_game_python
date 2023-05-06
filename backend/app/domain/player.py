from pydantic import BaseModel

from app.domain.user import User


class Player(BaseModel):
    """Player."""

    user: User
    score: int
