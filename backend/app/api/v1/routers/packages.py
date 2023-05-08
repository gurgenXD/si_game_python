from fastapi import APIRouter

from app.container import CONTAINER
from app.services.schemas.package import PackageCreateSchema

router = APIRouter(prefix="/packages", tags=["PACKAGES"])


@router.post("", summary="Create package")
async def create_package(package: PackageCreateSchema) -> None:
    """Create package."""
    service = CONTAINER.package_service()
    await service.create(package=package)
