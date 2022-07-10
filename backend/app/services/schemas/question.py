from pydantic import BaseModel


class QuestionSchema(BaseModel):
    """Question's schema."""

    text: str
    answer: str
    cost: int
    type:
    file_path: str
