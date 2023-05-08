from datetime import datetime
from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.adapters.storage.database.base_model import BaseModel
from app.services.types.game_status import GameStatusType


class GameModel(BaseModel):
    """Game model."""

    __tablename__ = "games"

    uuid: Mapped[UUID] = mapped_column(sa.Uuid, primary_key=True)
    capacity: Mapped[int]
    status: Mapped[GameStatusType] = mapped_column(sa.Enum(GameStatusType))
    is_deleted: Mapped[bool]

    created_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True))
    started_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True))
    finished_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True))

    presenter_uuid: Mapped[UUID] = mapped_column(sa.Uuid, sa.ForeignKey("users.uuid"))
    package_uuid: Mapped[UUID] = mapped_column(sa.Uuid, sa.ForeignKey("packages.uuid"))
