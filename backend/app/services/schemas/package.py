from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.services.schemas.round import RoundCreateSchema, RoundSchema


class PackageSchema(BaseModel):
    """Package schema."""

    uuid: UUID
    title: str
    author_uuid: UUID
    difficult: int
    rating: int
    counter: int
    created_at: datetime

    rounds: list[RoundSchema]

    class Config:
        orm_mode = True


class PackageCreateSchema(BaseModel):
    """Package create schema."""

    title: str
    author_uuid: UUID

    rounds: list[RoundCreateSchema]
