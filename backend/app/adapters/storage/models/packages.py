from datetime import datetime
from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.adapters.storage.database.base_model import BaseModel


class PackageModel(BaseModel):
    """Package model."""

    __tablename__ = "packages"

    uuid: Mapped[UUID] = mapped_column(sa.Uuid, primary_key=True)
    title: Mapped[str] = mapped_column(sa.String(64))
    difficult: Mapped[int]
    rating: Mapped[int]
    counter: Mapped[int]

    created_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True))

    author_uuid: Mapped[UUID] = mapped_column(sa.Uuid, sa.ForeignKey("users.uuid"))
