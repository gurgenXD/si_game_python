from pydantic import BaseModel


class ViewerSchema(BaseModel):
    """Viewer's schema."""

    user:
