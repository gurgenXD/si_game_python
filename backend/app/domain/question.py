from pydantic import BaseModel


class Question(BaseModel):
    """Question."""

    text: str
    answer: str
    cost: int
    type: str
    file_path: str
