from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.domain.round import Round
    from app.domain.user import User


class Package(BaseModel):
    """Package."""

    uuid: UUID
    title: str
    author: "User"
    difficult: int
    rating: int

    rounds: list["Round"]
