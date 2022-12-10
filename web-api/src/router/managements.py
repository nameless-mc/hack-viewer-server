from typing import List, Optional, Union
from fastapi import APIRouter, Cookie, Depends, Request, Response
from pydantic import BaseModel
from sqlalchemy.orm import Session
from model.event import Event, EventSchema
from model.team import Team, TeamSchema
from utils.auth import SESSION_KEY, hash_passwd, check_password, create_session, check_signin
from utils.error import UnauthorizedException
from db import get_db, idgen, Transactional
import query.events_query as query

router = APIRouter()


class PostCreateEventBody(BaseModel):
    class Team(BaseModel):
        name: str

    name: str
    description: str
    password: str
    teams: List[Team]


@router.post("/api/managements/events")
def create_event(body: PostCreateEventBody, response: Response, db: Session = Depends(get_db)):
    with Transactional(db):
        event = EventSchema(
            id=idgen(),
            name=body.name,
            description=body.description,
            passwd=hash_passwd(body.password))
        query.create_event(db, event)
        teams = [
            TeamSchema(
                id=idgen(),
                name=t.name,
                progress=0,
                event_id=event.id
            )for t in body.teams]
        query.create_teams(db, teams)
        response.set_cookie(
            key=SESSION_KEY, value=create_session(event.id, event.passwd))

        return{
            "event_id": event.id,
            "name": event.name,
            "description": event.description,
            "teams": [{"team_id": t.id, "name": t.name} for t in teams]
        }


class PostSigninEventBody(BaseModel):
    password: str


@router.post("/api/managements/events/{event_id}/signin")
def signin_event(event_id: int, body: PostSigninEventBody, response: Response, db: Session = Depends(get_db)):
    event = query.get_event(db, event_id)
    if(not check_password(body.password, event)):
        raise UnauthorizedException
    response.set_cookie(
        key=SESSION_KEY, value=create_session(event.id, event.passwd))


@router.get("/api/managements/events/{event_id}")
def get_event(event_id: int, request: Request, db: Session = Depends(get_db)):
    session = request.cookies.get(SESSION_KEY)
    check_signin(db, event_id, session)
    event = query.get_event(db, event_id)
    teams = query.get_teams(db, event_id)

    return{
        "event_id": event.id,
        "name": event.name,
        "description": event.description,
        "teams": [{"team_id": t.id, "name": t.name} for t in teams]
    }


class PostUpdateEventBody(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None


@router.put("/api/managements/events/{event_id}")
def update_event(event_id: int, body: PostUpdateEventBody, request: Request, db: Session = Depends(get_db)):
    with Transactional(db):
        session = request.cookies.get(SESSION_KEY)
        check_signin(db, event_id, session)
        event = query.update_event(db, event_id, body.name, body.description)
        return {
            "name": event.name,
            "description": event.description
        }


class PutUpdateTeamBody(BaseModel):
    name: Union[str, None] = None
    progress: Union[int, None] = None


@router.put("/api/managements/events/{event_id}/teams/{team_id}")
def update_team(event_id: int, team_id: int, body: PutUpdateTeamBody, request: Request, db: Session = Depends(get_db)):
    with Transactional(db):
        session = request.cookies.get(SESSION_KEY)
        check_signin(db, event_id, session)

        team = query.update_team(
            db, event_id, team_id, body.name, body.progress)
        return {"name": team.name, "progress": team.progress}


class PostCreateTeamBody(BaseModel):
    name: str


@router.post("/api/managements/events/{event_id}/teams")
def create_team(event_id: int, body: PostCreateTeamBody, request: Request, db: Session = Depends(get_db)):
    with Transactional(db):
        session = request.cookies.get(SESSION_KEY)
        check_signin(db, event_id, session)
        team = TeamSchema(
            id=idgen(),
            name=body.name,
            progress=0,
            event_id=event_id
        )
        query.create_team(db, team)
        return {"name": team.name, "progress": team.progress}


@router.delete("/api/managements/events/{event_id}/teams/{team_id}")
def delete_team(event_id: int, team_id: int, request: Request, db: Session = Depends(get_db)):
    with Transactional(db):
        session = request.cookies.get(SESSION_KEY)
        check_signin(db, event_id, session)

        query.delete_team(db, event_id, team_id)
        return Response(status_code=204)


@router.delete("/api/managements/events/{event_id}")
def delete_event(event_id: int, request: Request, db: Session = Depends(get_db)):
    with Transactional(db):
        session = request.cookies.get(SESSION_KEY)
        check_signin(db, event_id, session)

        query.delete_event(db, event_id)
        return Response(status_code=204)
