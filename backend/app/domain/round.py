from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.domain.topic import Topic


class Round(BaseModel):
    """Round."""

    order: int

    topics: list["Topic"]
