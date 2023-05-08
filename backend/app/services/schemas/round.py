from pydantic import BaseModel

from app.services.schemas.topic import TopicSchema


class RoundSchema(BaseModel):
    """Round schema."""

    order: int
    type: str

    topics: list[TopicSchema]

    class Config:
        orm_mode = True
