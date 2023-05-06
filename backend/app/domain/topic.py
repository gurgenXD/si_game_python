from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.domain.question import Question


class Topic(BaseModel):
    """Topic."""

    title: str
    questions: list["Question"]
