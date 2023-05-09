from uuid import UUID

from fastapi import APIRouter, status

from app.container import CONTAINER
from app.services.schemas.package import PackageCreateSchema, PackageSchema

router = APIRouter(prefix="/packages", tags=["PACKAGES"])


@router.post("", summary="Create package", status_code=status.HTTP_201_CREATED)
async def create_package(package: PackageCreateSchema) -> None:
    """Create package."""
    service = CONTAINER.package_service()
    await service.create(package=package)


@router.get("/{uuid}", summary="Get package by UUID")
async def get_package_by_uuid(uuid: UUID) -> PackageSchema:
    """Get package by UUID."""
    service = CONTAINER.package_service()
    return await service.get(uuid=uuid)
