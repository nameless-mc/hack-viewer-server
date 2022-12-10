from pydantic import BaseModel
from db import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String, BigInteger


class Event(Base):
    __tablename__ = 'events'
    id = Column('id', BigInteger, primary_key=True,
                index=True, autoincrement=False)
    name = Column('name', String(45), nullable=False)
    description = Column('description', String(200), nullable=False)
    passwd = Column('passwd', String(45), nullable=False)


class EventSchema(BaseModel):
    id: int
    name: str
    description: str
    passwd: str

    class Config:
        orm_mode = True
