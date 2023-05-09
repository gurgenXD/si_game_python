from datetime import datetime, timezone
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from app.services.schemas.package import PackageSchema
from app.services.schemas.question import QuestionSchema
from app.services.schemas.round import RoundSchema
from app.services.schemas.topic import TopicSchema

if TYPE_CHECKING:
    from app.adapters.storage.package import PackageAdapter
    from app.services.schemas.package import PackageCreateSchema


class PackageService:
    """Package service."""

    def __init__(self, packages: "PackageAdapter") -> None:
        self._packages = packages

    async def create(self, package: "PackageCreateSchema") -> None:
        """Create new package."""
        package_creation = PackageSchema(
            uuid=uuid4(),
            title=package.title,
            author_uuid=package.author_uuid,
            difficult=0,
            rating=0,
            counter=0,
            created_at=datetime.now(tz=timezone.utc),
            rounds=[
                RoundSchema(
                    uuid=uuid4(),
                    order=index,
                    type=round_.type,
                    topics=[
                        TopicSchema(
                            uuid=uuid4(),
                            title=topic.title,
                            questions=[
                                QuestionSchema(
                                    uuid=uuid4(),
                                    text=question.text,
                                    answer=question.answer,
                                    cost=question.cost,
                                    type=question.type,
                                    file_path=question.file_path,
                                )
                                for question in topic.questions
                            ],
                        )
                        for topic in round_.topics
                    ],
                )
                for index, round_ in enumerate(package.rounds)
            ],
        )

        await self._packages.create(package=package_creation)

    async def get(self, uuid: UUID) -> "PackageSchema":
        """Get package."""
        return await self._packages.get(uuid=uuid)
