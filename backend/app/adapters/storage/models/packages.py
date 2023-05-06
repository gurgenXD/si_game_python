import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.adapters.storage.database import BaseModel


class PackageModel(BaseModel):
    """Package model."""

    __tablename__ = "packages"

    uuid: Mapped[str] = mapped_column(sa.String(36), primary_key=True)
