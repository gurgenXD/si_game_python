from uuid import UUID

from pydantic import BaseModel


class QuestionSchema(BaseModel):
    """Question schema."""

    uuid: UUID
    text: str
    answer: str
    cost: int
    type: str
    file_path: str | None

    class Config:
        orm_mode = True


class QuestionCreateSchema(BaseModel):
    """Question create schema."""

    text: str
    answer: str
    cost: int
    type: str
    file_path: str | None
