from pydantic import BaseModel


class UserSchema(BaseModel):
    """User's schema."""

    id: int
    nick_name: str
    avatar: str
    password_hash:
    email:
