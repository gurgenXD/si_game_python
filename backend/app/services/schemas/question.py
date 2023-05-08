from pydantic import BaseModel


class QuestionSchema(BaseModel):
    """Question schema."""

    text: str
    answer: str
    cost: int
    type: str
    file_path: str | None
