from uuid import UUID

from pydantic import BaseModel

from app.services.schemas.question import QuestionCreateSchema, QuestionSchema


class TopicSchema(BaseModel):
    """Topic schema."""

    uuid: UUID
    title: str

    questions: list[QuestionSchema]

    class Config:
        orm_mode = True


class TopicCreateSchema(BaseModel):
    """Topic create schema."""

    title: str

    questions: list[QuestionCreateSchema]
