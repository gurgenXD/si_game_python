from fastapi import APIRouter
from app.domain.game import Game
from uuid import uuid4, UUID


router = APIRouter(prefix="/users", tags=["USERS"])


@router.get("", summary="Get users")
async def get_users() -> list[dict]:
    """Get users."""
    return []
