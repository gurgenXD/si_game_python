import sqlalchemy as sa
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID


@as_declarative()
class BaseModel:
    """Base model."""

    uuid: Mapped[UUID] = mapped_column(sa.Uuid, primary_key=True, index=True)
