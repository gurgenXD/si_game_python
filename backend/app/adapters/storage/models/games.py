from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.adapters.storage.database import BaseModel
from app.services.types.game_status import GameStatusType


class GameModel(BaseModel):
    """Game model."""

    __tablename__ = "games"

    uuid: Mapped[UUID] = mapped_column(sa.Uuid, primary_key=True)
    capacity: Mapped[int]
    status: Mapped[GameStatusType] = mapped_column(sa.Enum(GameStatusType))
    is_deleted: Mapped[bool]

    presenter_uuid: Mapped[UUID] = mapped_column(sa.Uuid, sa.ForeignKey("users.uuid"))
    package_uuid: Mapped[UUID] = mapped_column(sa.Uuid, sa.ForeignKey("packages.uuid"))
