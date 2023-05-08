from datetime import datetime
from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.storage.database.base_model import BaseModel

if TYPE_CHECKING:
    from app.adapters.storage.models.games import GameModel
    from app.adapters.storage.models.packages import PackageModel


class UserModel(BaseModel):
    """User model."""

    __tablename__ = "users"

    nickname: Mapped[str] = mapped_column(sa.String(32))
    password_hash: Mapped[str] = mapped_column(sa.String(128))
    email: Mapped[str] = mapped_column(sa.String(128))
    file_path: Mapped[str | None] = mapped_column(sa.String(128))

    created_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True))
    updated_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True))

    games: Mapped[list["GameModel"]] = relationship("GameModel", back_populates="presenter")
    packages: Mapped[list["PackageModel"]] = relationship("PackageModel", back_populates="author")
