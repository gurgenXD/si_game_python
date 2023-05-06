import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.adapters.storage.database.base_model import BaseModel


class GameModel(BaseModel):
    """Game model."""

    __tablename__ = "games"

    uuid: Mapped[str] = mapped_column(sa.String(36), primary_key=True)
    capacity: Mapped[int]
    is_active: Mapped[bool]
    is_paused: Mapped[bool]
    is_finished: Mapped[bool]

    presenter_uuid: Mapped[str] = mapped_column(sa.String(36), sa.ForeignKey("users.uuid"))
    package_uuid: Mapped[str] = mapped_column(sa.String(36), sa.ForeignKey("packages.uuid"))
