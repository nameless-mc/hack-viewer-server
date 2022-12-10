from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from model.team import Team, TeamSchema
from model.event import Event, EventSchema
from utils.error import ResourceNouFoundException
from db import get_db

router = APIRouter()


@router.get("/api/events/{event_id}")
async def get_event(event_id: int, db: Session = Depends(get_db)):
    event: EventSchema = db.get(Event, event_id)

    if(event is None):
        raise ResourceNouFoundException("event")

    return {
        "name": event.name,
        "description": event.description
    }


@router.get("/api/events/{event_id}/teams")
async def get_teams(event_id: int, db: Session = Depends(get_db)):
    event: EventSchema = db.get(Event, event_id)

    if(event is None):
        raise ResourceNouFoundException("event")

    teams: List[TeamSchema] = db.query(Team).filter(
        Team.event_id == event_id).all()

    return {
        "teams": [{"name": t.name, "progress": t.progress} for t in teams]
    }


@router.get("/api/events/{event_id}/teams/{team_id}")
async def get_team(event_id: int, team_id: int, db: Session = Depends(get_db)):
    event: EventSchema = db.get(Event, event_id)

    if(event is None):
        raise ResourceNouFoundException("event")

    try:
        team: TeamSchema = db.query(Team).filter(Team.id == team_id,
                                                 Team.event_id == event_id).one()
    except:
        raise ResourceNouFoundException("team")

    return {"name": team.name, "progress": team.progress}


class PutTeamProgressRequestBody(BaseModel):
    progress: int


@router.put("/api/events/{event_id}/teams/{team_id}/progress")
async def put_team_progress(event_id: int, team_id: int, body: PutTeamProgressRequestBody, db: Session = Depends(get_db)):
    event: EventSchema = db.get(Event, event_id)

    if(event is None):
        raise ResourceNouFoundException("event")

    try:
        team: TeamSchema = db.query(Team).filter(Team.id == team_id,
                                                 Team.event_id == event_id).one()
    except:
        raise ResourceNouFoundException("team")

    team.progress = body.progress

    db.commit()

    return {"name": team.name, "progress": team.progress}


class PutTeamNameRequestBody(BaseModel):
    name: str


@router.put("/api/events/{event_id}/teams/{team_id}/name")
async def put_team_name(event_id: int, team_id: int, body: PutTeamNameRequestBody, db: Session = Depends(get_db)):
    event: EventSchema = db.get(Event, event_id)

    if(event is None):
        raise ResourceNouFoundException("event")

    try:
        team: TeamSchema = db.query(Team).filter(Team.id == team_id,
                                                 Team.event_id == event_id).one()
    except:
        raise ResourceNouFoundException("team")

    team.name = body.name

    db.commit()

    return {"name": team.name, "progress": team.progress}
