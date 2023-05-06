from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.domain.user import User


class Player(BaseModel):
    """Player."""

    user: "User"
    score: int
