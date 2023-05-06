from pydantic import BaseModel

from app.domain.question import Question


class Topic(BaseModel):
    """Topic."""

    title: str
    questions: list[Question]
