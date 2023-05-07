from unittest.mock import MagicMock
from uuid import UUID, uuid4

from fastapi import APIRouter

from app.container import CONTAINER
from app.domain.game import Game, GameStatus
from app.domain.package import Package
from app.domain.user import User
from app.services.schemas.game import GameCreateSchema

router = APIRouter(prefix="/games", tags=["GAMES"])


@router.post("", summary="Create game")
async def create_game(game: GameCreateSchema) -> None:
    """Create game."""
    service = CONTAINER.game_service()
    await service.create(game=game)


@router.get("", summary="Get games")
async def get_games(
    status: GameStatus | None = None,
    presenter_uuid: UUID | None = None,
    package_uuid: UUID | None = None,
) -> list[Game]:
    """Get games."""
    service = CONTAINER.game_service()
    games = await service.get_all(
        status=status, presenter_uuid=presenter_uuid, package_uuid=package_uuid
    )

    return [
        Game(
            uuid=uuid4(),
            capacity=3,
            status=GameStatus.FINISHED,
            is_deleted=False,
            package=MagicMock(Package),
            presenter=MagicMock(User),
            players=[],
            viewers=[],
        )
    ]


@router.get("/{uuid}", summary="Get game by UUID")
async def get_game_by_uuid(uuid: UUID) -> Game:
    """Get game by UUID."""
    service = CONTAINER.game_service()
    game = await service.get(uuid=uuid)

    return Game(
        uuid=uuid,
        capacity=3,
        status=GameStatus.FINISHED,
        is_deleted=False,
        package=MagicMock(Package),
        presenter=MagicMock(User),
        players=[],
        viewers=[],
    )
