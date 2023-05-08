from unittest.mock import MagicMock
from uuid import UUID, uuid4

from fastapi import APIRouter

from app.container import CONTAINER
from app.services.schemas.game import GameCreateSchema, GameSchema
from app.services.schemas.package import PackageSchema
from app.services.schemas.user import UserSchema
from app.services.types.game_status import GameStatusType

router = APIRouter(prefix="/games", tags=["GAMES"])


@router.post("", summary="Create game")
async def create_game(game: GameCreateSchema) -> None:
    """Create game."""
    service = CONTAINER.game_service()
    await service.create(game=game)


@router.get("", summary="Get games")
async def get_games(
    status: GameStatusType | None = None,
    presenter_uuid: UUID | None = None,
    package_uuid: UUID | None = None,
) -> list[GameSchema]:
    """Get games."""
    service = CONTAINER.game_service()
    games = await service.get_all(
        status=status, presenter_uuid=presenter_uuid, package_uuid=package_uuid
    )

    return [
        GameSchema(
            uuid=uuid4(),
            capacity=3,
            status=GameStatusType.FINISHED,
            is_deleted=False,
            package=MagicMock(PackageSchema),
            presenter=MagicMock(UserSchema),
            players=[],
            viewers=[],
        )
    ]


@router.get("/{uuid}", summary="Get game by UUID")
async def get_game_by_uuid(uuid: UUID) -> GameSchema:
    """Get game by UUID."""
    service = CONTAINER.game_service()
    game = await service.get(uuid=uuid)

    return GameSchema(
        uuid=uuid,
        capacity=3,
        status=GameStatusType.FINISHED,
        is_deleted=False,
        package=MagicMock(PackageSchema),
        presenter=MagicMock(UserSchema),
        players=[],
        viewers=[],
    )
