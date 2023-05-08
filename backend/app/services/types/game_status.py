from enum import StrEnum


class GameStatusType(StrEnum):
    """Game status."""

    CREATED = "CREATED"
    STARTED = "STARTED"
    PAUSED = "PAUSED"
    FINISHED = "FINISHED"
