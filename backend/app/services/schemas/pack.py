from pydantic import BaseModel


class PackSchema(BaseModel):
    """Pack's schema."""

    id: int
    title: str
    author:
    rounds:
    difficult: int
    rating: int
