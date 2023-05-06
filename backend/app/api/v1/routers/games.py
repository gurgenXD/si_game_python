from uuid import UUID, uuid4

from fastapi import APIRouter

from app.domain.game import Game

router = APIRouter(prefix="/games", tags=["GAMES"])


@router.get("", summary="Get games")
async def get_games() -> list["Game"]:
    """Get games."""
    return [
        Game(
            uuid=uuid4(),
            players_max_count=3,
            members=[],
            pack="pack1",
            is_active=True,
            is_paused=False,
            is_finished=False,
        )
    ]


@router.get("/{uuid}", summary="Get game by UUID")
async def get_game_by_uuid(uuid: UUID) -> "Game":
    """Get game by UUID."""
    return Game(
        uuid=uuid,
        players_max_count=3,
        members=[],
        pack="pack1",
        is_active=True,
        is_paused=False,
        is_finished=False,
    )
