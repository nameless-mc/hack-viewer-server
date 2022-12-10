from db import Base, engine
from .event import Event
from .team import Team

__all__ = [
    "Event",
    "Team"
]

Base.metadata.create_all(engine)
