from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db import get_db, Transactional
import query.events_query as query

router = APIRouter()


@router.get("/api/events/{event_id}")
async def get_event(event_id: int, db: Session = Depends(get_db)):
    event = query.get_event(db, event_id)
    return {
        "name": event.name,
        "description": event.description
    }


@router.get("/api/events/{event_id}/teams")
async def get_teams(event_id: int, db: Session = Depends(get_db)):
    teams = query.get_teams(db, event_id)
    return {
        "teams": [{"name": t.name, "progress": t.progress} for t in teams]
    }


@router.get("/api/events/{event_id}/teams/{team_id}")
async def get_team(event_id: int, team_id: int, db: Session = Depends(get_db)):
    team = query.get_team(db, event_id, team_id)
    return {"name": team.name, "progress": team.progress}


class PutTeamProgressRequestBody(BaseModel):
    progress: int


@router.put("/api/events/{event_id}/teams/{team_id}/progress")
async def put_team_progress(event_id: int, team_id: int, body: PutTeamProgressRequestBody, db: Session = Depends(get_db)):
    with Transactional(db):
        team = query.update_team_progress(db, event_id, team_id, body.progress)
        return {"name": team.name, "progress": team.progress}


class PutTeamNameRequestBody(BaseModel):
    name: str


@router.put("/api/events/{event_id}/teams/{team_id}/name")
async def put_team_name(event_id: int, team_id: int, body: PutTeamNameRequestBody, db: Session = Depends(get_db)):
    with Transactional(db):
        team = query.update_team_name(db, event_id, team_id, body.name)
        return {"name": team.name, "progress": team.progress}
