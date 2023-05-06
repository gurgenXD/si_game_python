from uuid import UUID

from pydantic import BaseModel


class GameCreateSchema(BaseModel):
    """Game create schema."""

    presenter_uuid: UUID
    package_uuid: UUID
    capacity: int
