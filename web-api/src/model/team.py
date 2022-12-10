from pydantic import BaseModel
from db import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, BigInteger, Integer


class Team(Base):
    __tablename__ = 'teams'
    id = Column('id', BigInteger, primary_key=True,
                index=True, autoincrement=False)
    name = Column('name', String(45), nullable=False)
    progress = Column('progress', Integer, nullable=False)
    event_id = Column('event_id', BigInteger, ForeignKey(
        "events.id", onupdate='CASCADE', ondelete='CASCADE'), index=True, nullable=False)


class TeamSchema(BaseModel):
    id: int
    name: str
    progress: int
    event_id: int

    class Config:
        orm_mode = True

    def to_model(self):
        return Team(id = self.id, name = self.name, progress = self.progress, event_id = self.event_id)
