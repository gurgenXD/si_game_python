from contextlib import AbstractAsyncContextManager
from typing import TYPE_CHECKING, Callable

from app.adapters.storage.models import PackageModel, QuestionModel, RoundModel, TopicModel
from app.services.schemas.package import PackageSchema

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class PackageAdapter:
    """Package adapter."""

    def __init__(
        self, session_factory: Callable[[], AbstractAsyncContextManager["AsyncSession"]]
    ) -> None:
        self._session_factory = session_factory

    async def create(self, package: "PackageSchema") -> None:
        """Create package."""
        async with self._session_factory() as session:
            package_model = PackageModel(
                uuid=package.uuid,
                title=package.title,
                difficult=package.difficult,
                rating=package.rating,
                counter=package.counter,
                created_at=package.created_at,
                author_uuid=package.author_uuid,
            )
            session.add(package_model)

            for round_ in package.rounds:
                round_model = RoundModel(
                    uuid=round_.uuid,
                    order=round_.order,
                    type=round_.type,
                    package_uuid=package.uuid,
                )
                session.add(round_model)

                for topic in round_.topics:
                    topic_model = TopicModel(
                        uuid=topic.uuid, title=topic.title, round_uuid=round_.uuid
                    )
                    session.add(topic_model)

                    for question in topic.questions:
                        question_model = QuestionModel(
                            uuid=question.uuid,
                            text=question.text,
                            answer=question.answer,
                            cost=question.cost,
                            type=question.type,
                            file_path=question.file_path,
                            topic_uuid=topic.uuid,
                        )
                        session.add(question_model)

            await session.commit()
