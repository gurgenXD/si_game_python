from fastapi import APIRouter


router = APIRouter(prefix="/users", tags=["USERS"])


@router.get("", summary="Get users")
async def get_users() -> list[dict]:
    """Get users."""
    return []
