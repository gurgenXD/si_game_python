from uuid import UUID

from pydantic import BaseModel

from app.services.schemas.package import PackageSchema
from app.services.schemas.player import PlayerSchema
from app.services.schemas.user import UserSchema
from app.services.types.game_status import GameStatusType


class GameCreateSchema(BaseModel):
    """Game create schema."""

    presenter_uuid: UUID
    package_uuid: UUID
    capacity: int


class GameSchema(BaseModel):
    """Game schema."""

    uuid: UUID
    capacity: int
    status: GameStatusType
    presenter: UserSchema
    package: PackageSchema
    is_deleted: bool

    players: list[PlayerSchema] = []
    viewers: list[UserSchema] = []

    class Config:
        orm_mode = True
