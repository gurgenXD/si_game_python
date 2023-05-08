from typing import TYPE_CHECKING
from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.storage.database.base_model import BaseModel

if TYPE_CHECKING:
    from app.adapters.storage.models.questions import QuestionModel
    from app.adapters.storage.models.rounds import RoundModel


class TopicModel(BaseModel):
    """Topic model."""

    __tablename__ = "topics"

    uuid: Mapped[UUID] = mapped_column(sa.Uuid, primary_key=True)
    title: Mapped[str] = mapped_column(sa.String(64))

    round_uuid: Mapped[UUID] = mapped_column(sa.Uuid, sa.ForeignKey("rounds.uuid"))

    round: Mapped["RoundModel"] = relationship("RoundModel", back_populates="topics")
    questions: Mapped["QuestionModel"] = relationship(
        "QuestionModel", back_populates="topic", uselist=True
    )
