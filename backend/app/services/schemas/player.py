from pydantic import BaseModel

from app.services.schemas.user import UserSchema


class PlayerSchema(BaseModel):
    """Player schema."""

    user: UserSchema
    score: int
