from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.adapters.storage.database import BaseModel


class PackageModel(BaseModel):
    """Package model."""

    __tablename__ = "packages"

    uuid: Mapped[UUID] = mapped_column(sa.Uuid, primary_key=True)
