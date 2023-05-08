from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.adapters.storage.database.base_model import BaseModel


class UserModel(BaseModel):
    """User model."""

    __tablename__ = "users"

    uuid: Mapped[UUID] = mapped_column(sa.Uuid, primary_key=True)
