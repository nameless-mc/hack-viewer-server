from db import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import String, BigInteger, Integer


class Team(Base):
    __tablename__ = 'teams'
    id = Column('id', BigInteger, primary_key=True, index=True)
    name = Column('name', String, nullable=False)
    progress = Column('progress', Integer, nullable=False)
    event_id = Column('event_id', BigInteger, ForeignKey(
        "events.id", onupdate='CASCADE', ondelete='CASCADE'), index=True)
