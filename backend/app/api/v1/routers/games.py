from unittest.mock import MagicMock
from uuid import UUID, uuid4

from fastapi import APIRouter

from app.domain.game import Game
from app.domain.package import Package
from app.domain.user import User

router = APIRouter(prefix="/games", tags=["GAMES"])


@router.get("", summary="Get games")
async def get_games() -> list[Game]:
    """Get games."""
    return [
        Game(
            uuid=uuid4(),
            capacity=3,
            is_active=True,
            is_paused=False,
            is_finished=False,
            package=MagicMock(Package),
            presenter=MagicMock(User),
            players=[],
            viewers=[],
        )
    ]


@router.get("/{uuid}", summary="Get game by UUID")
async def get_game_by_uuid(uuid: UUID) -> Game:
    """Get game by UUID."""
    return Game(
        uuid=uuid,
        capacity=3,
        is_active=True,
        is_paused=False,
        is_finished=False,
        package=MagicMock(Package),
        presenter=MagicMock(User),
        players=[],
        viewers=[],
    )
