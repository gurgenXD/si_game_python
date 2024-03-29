from uuid import UUID

from pydantic import BaseModel

from app.services.schemas.topic import TopicCreateSchema, TopicSchema


class RoundSchema(BaseModel):
    """Round schema."""

    uuid: UUID
    order: int
    type_: str

    topics: list[TopicSchema]

    class Config:
        orm_mode = True


class RoundCreateSchema(BaseModel):
    """Round create schema."""

    type_: str

    topics: list[TopicCreateSchema]
