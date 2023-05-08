from typing import TYPE_CHECKING
from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.storage.database.base_model import BaseModel

if TYPE_CHECKING:
    from app.adapters.storage.models.topics import TopicModel


class QuestionModel(BaseModel):
    """Question model."""

    __tablename__ = "questions"

    uuid: Mapped[UUID] = mapped_column(sa.Uuid, primary_key=True)
    text: Mapped[str] = mapped_column(sa.String(1024))
    answer: Mapped[str] = mapped_column(sa.String(128))
    cost: Mapped[int]
    type: Mapped[str] = mapped_column(sa.String(16))
    file_path: Mapped[str | None] = mapped_column(sa.String(128))

    topic_uuid: Mapped[UUID] = mapped_column(sa.Uuid, sa.ForeignKey("topics.uuid"))

    topic: Mapped["TopicModel"] = relationship(
        "TopicModel", back_populates="questions", uselist=True
    )
