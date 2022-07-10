from pydantic import BaseModel


class MemberSchema(BaseModel):
    """Member's schema."""

    user:
    role:
