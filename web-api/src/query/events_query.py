
from typing import List, Union
from sqlalchemy.orm import Session
from model.team import Team, TeamSchema
from model.event import Event, EventSchema
from utils.error import ResourceNouFoundException, InvalidParameterException


def get_event(db: Session, event_id: int):
    event: EventSchema = db.get(Event, event_id)

    if(event is None):
        raise ResourceNouFoundException("event")

    return event


def check_event_exists(db: Session, event_id: int):
    event: EventSchema = db.get(Event, event_id)

    if(event is None):
        raise ResourceNouFoundException("event")


def get_teams(db: Session, event_id: int):
    check_event_exists(db, event_id)
    teams: List[TeamSchema] = db.query(Team).filter(
        Team.event_id == event_id).all()
    return teams


def get_team(db: Session, event_id: int, team_id: int):
    check_event_exists(db, event_id)
    try:
        team: TeamSchema = db.query(Team).filter(Team.id == team_id,
                                                 Team.event_id == event_id).one()
    except:
        raise ResourceNouFoundException("team")
    return team


def update_team(db: Session, event_id: int, team_id: int, name: Union[str, None], progress: Union[int, None]):
    if(name is None and progress is None):
        raise InvalidParameterException
    team = get_team(db, event_id, team_id)
    if(name is not None):
        team.name = name
    if(progress is not None):
        team.progress = progress
    db.commit()

    return team


def update_team_progress(db: Session, event_id: int, team_id: int, new_progress: int):
    team = get_team(db, event_id, team_id)
    team.progress = new_progress
    db.commit()
    return team


def update_team_name(db: Session, event_id: int, team_id: int, new_name: str):
    team = get_team(db, event_id, team_id)
    team.name = new_name
    db.commit()
    return team


def create_event(db: Session, event: EventSchema):
    e = event.to_model()
    db.add(e)
    db.commit()


def create_teams(db: Session, teams: List[TeamSchema]):
    ts = [team.to_model() for team in teams]
    db.add_all(ts)
    db.commit()


def create_team(db: Session, team: TeamSchema):
    t = team.to_model()
    db.add(t)
    db.commit()


def update_event(db: Session, event_id: int, name: Union[str, None], description: Union[str, None]):
    if(name is None and description is None):
        raise InvalidParameterException
    event = get_event(db, event_id)
    if(name is not None):
        event.name = name
    if(description is not None):
        event.description = description
    db.commit()

    return event


def delete_team(db: Session, event_id: int, team_id: int):
    team = get_team(db, event_id, team_id)
    db.delete(team)
    db.commit()


def delete_event(db: Session, event_id: int):
    event = get_event(db, event_id)
    teams = get_teams(db, event_id)
    for t in teams:
        db.delete(t)
    db.delete(event)
    db.commit()
