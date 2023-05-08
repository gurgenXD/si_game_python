from pydantic import BaseModel

from app.services.schemas.question import QuestionSchema


class TopicSchema(BaseModel):
    """Topic schema."""

    title: str
    questions: list[QuestionSchema]

    class Config:
        orm_mode = True
