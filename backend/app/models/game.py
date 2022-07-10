from sys import maxsize

from sqlalchemy import Boolean, Column, Integer, String

from app.models.base import BaseModel


class GameModel(BaseModel):
    """Game model."""

    __tablename__ = "games"

    id = Column(Integer, primary_key=True, autoincrement=True)
    hashed_password = Column(String)
    players_max_count = Column(Integer)
    showman = Column(Integer, nullable=True)
    pack = Column(Integer)
    is_active = Column(Boolean)
    is_paused = Column(Boolean)
    is_finished = Column(Boolean)
