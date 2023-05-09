from uuid import UUID

from fastapi import APIRouter, status

from app.container import CONTAINER
from app.services.schemas.game import GameCreateSchema, GameSchema
from app.services.types.game_status import GameStatusType

router = APIRouter(prefix="/games", tags=["GAMES"])


@router.post("", summary="Create game", status_code=status.HTTP_201_CREATED)
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

    return []


@router.get("/{uuid}", summary="Get game by UUID")
async def get_game_by_uuid(uuid: UUID) -> GameSchema:
    """Get game by UUID."""
    service = CONTAINER.game_service()
    return await service.get(uuid=uuid)
