from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    """User schema."""

    uuid: UUID
    nickname: str
    password_hash: str
    email: EmailStr
    file_path: str | None
