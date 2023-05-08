from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.adapters.storage.database.base_model import BaseModel


class TopicModel(BaseModel):
    """Topic model."""

    __tablename__ = "topics"

    uuid: Mapped[UUID] = mapped_column(sa.Uuid, primary_key=True)
    title: Mapped[str] = mapped_column(sa.String(64))

    round_uuid: Mapped[UUID] = mapped_column(sa.Uuid, sa.ForeignKey("rounds.uuid"))
