from pydantic import BaseModel

from app.domain.topic import Topic


class Round(BaseModel):
    """Round."""

    order: int

    topics: list[Topic]
