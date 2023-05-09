from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.storage.database.base_model import BaseModel


if TYPE_CHECKING:
    from app.adapters.storage.models.games import GameModel
    from app.adapters.storage.models.rounds import RoundModel
    from app.adapters.storage.models.users import UserModel


class PackageModel(BaseModel):
    """Package model."""

    __tablename__ = "packages"

    title: Mapped[str] = mapped_column(sa.String(64))
    difficult: Mapped[int]
    rating: Mapped[int]
    counter: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True))

    author_uuid: Mapped[UUID] = mapped_column(sa.Uuid, sa.ForeignKey("users.uuid"))

    games: Mapped[list["GameModel"]] = relationship("GameModel", back_populates="package")
    rounds: Mapped[list["RoundModel"]] = relationship("RoundModel", back_populates="package")
    author: Mapped["UserModel"] = relationship("UserModel", back_populates="packages")
