
from typing import List
from sqlalchemy.orm import Session
from model.team import Team, TeamSchema
from model.event import Event, EventSchema
from utils.error import ResourceNouFoundException


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