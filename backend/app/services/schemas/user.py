from uuid import UUID

from pydantic import BaseModel


class UserSchema(BaseModel):
    """User schema."""

    uuid: UUID
    nickname: str
    password_hash: str
    email: str
    avatar: str | None
