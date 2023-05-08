from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.adapters.storage.database.base_model import BaseModel


class PlayerModel(BaseModel):
    """Player model."""

    __tablename__ = "players"

    user_uuid: Mapped[UUID] = mapped_column(sa.Uuid, sa.ForeignKey("users.uuid"), primary_key=True)
    game_uuid: Mapped[UUID] = mapped_column(sa.Uuid, sa.ForeignKey("games.uuid"), primary_key=True)
    score: Mapped[int]
