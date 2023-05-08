from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.storage.database.base_model import BaseModel
from app.services.types.game_status import GameStatusType

if TYPE_CHECKING:
    from app.adapters.storage.models.packages import PackageModel
    from app.adapters.storage.models.users import UserModel


class GameModel(BaseModel):
    """Game model."""

    __tablename__ = "games"

    capacity: Mapped[int]
    status: Mapped[GameStatusType] = mapped_column(sa.Enum(GameStatusType))
    is_deleted: Mapped[bool]

    created_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True))
    started_at: Mapped[datetime | None] = mapped_column(sa.DateTime(timezone=True))
    finished_at: Mapped[datetime | None] = mapped_column(sa.DateTime(timezone=True))

    presenter_uuid: Mapped[UUID] = mapped_column(sa.Uuid, sa.ForeignKey("users.uuid"))
    package_uuid: Mapped[UUID] = mapped_column(sa.Uuid, sa.ForeignKey("packages.uuid"))

    presenter: Mapped["UserModel"] = relationship("UserModel", back_populates="games")
    package: Mapped["PackageModel"] = relationship("PackageModel", back_populates="games")
