from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    """User."""

    uuid: UUID
    nickname: str
    password_hash: str
    email: str
    avatar: str | None
