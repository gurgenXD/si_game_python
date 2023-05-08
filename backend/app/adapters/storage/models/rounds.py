from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.adapters.storage.database.base_model import BaseModel


class RoundModel(BaseModel):
    """Round model."""

    __tablename__ = "rounds"

    uuid: Mapped[UUID] = mapped_column(sa.Uuid, primary_key=True)
    order: Mapped[int]
    type: Mapped[str] = mapped_column(sa.String(16))

    game_uuid: Mapped[UUID] = mapped_column(sa.Uuid, sa.ForeignKey("games.uuid"))
