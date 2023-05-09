from typing import TYPE_CHECKING
from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.storage.database.base_model import BaseModel


if TYPE_CHECKING:
    from app.adapters.storage.models.packages import PackageModel
    from app.adapters.storage.models.topics import TopicModel


class RoundModel(BaseModel):
    """Round model."""

    __tablename__ = "rounds"

    order: Mapped[int]
    type_: Mapped[str] = mapped_column(sa.String(16))

    package_uuid: Mapped[UUID] = mapped_column(sa.Uuid, sa.ForeignKey("packages.uuid"))

    package: Mapped["PackageModel"] = relationship("PackageModel", back_populates="rounds")
    topics: Mapped[list["TopicModel"]] = relationship("TopicModel", back_populates="round")
