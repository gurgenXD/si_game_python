from pydantic import BaseModel

from app.services.schemas.topic import TopicSchema


class RoundSchema(BaseModel):
    """Round schema."""

    order: int

    topics: list[TopicSchema]
