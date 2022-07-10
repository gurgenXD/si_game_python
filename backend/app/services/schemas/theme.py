from pydantic import BaseModel


class ThemeSchema(BaseModel):
    """Theme's schema."""

    title: str
    questions: []
