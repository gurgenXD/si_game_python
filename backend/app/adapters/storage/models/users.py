import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.adapters.storage.database import BaseModel


class UserModel(BaseModel):
    """User model."""

    __tablename__ = "users"

    uuid: Mapped[str] = mapped_column(sa.String(36), primary_key=True)
