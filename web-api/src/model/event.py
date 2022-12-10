from db import Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import String, BigInteger


class Event(Base):
    __tablename__ = 'events'
    id = Column('id', BigInteger, primary_key=True, index=True)
    name = Column('name', String, nullable=False)
    description = Column('description', String, nullable=False)
    passwd = Column('passwd', String, nullable=False)
