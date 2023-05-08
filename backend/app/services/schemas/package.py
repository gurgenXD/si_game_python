from uuid import UUID

from pydantic import BaseModel

from app.services.schemas.round import RoundSchema
from app.services.schemas.user import UserSchema


class PackageSchema(BaseModel):
    """Package schema."""

    uuid: UUID
    title: str
    author: UserSchema
    difficult: int
    rating: int

    rounds: list[RoundSchema]
