from pydantic import BaseModel

from app.services.schemas.round import RoundSchema


class PackageSchema(BaseModel):
    """Package schema."""

    title: str
    author_uuid: int
    difficult: int
    rating: int

    rounds: list[RoundSchema]

    class Config:
        orm_mode = True
