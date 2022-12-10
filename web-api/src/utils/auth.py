import hashlib
from typing import Optional, Union

from utils.error import UnauthorizedException, ForbiddenException
import config
from model.event import EventSchema
from sqlalchemy.orm import Session
import query.events_query as query


def hash_passwd(passwd: str):
    return hashlib.sha256(bytes(passwd, 'utf-8') + bytes(config.solt, 'utf-8')).hexdigest()


def create_session(event_id: int, hashed_passwd: str):
    return hashlib.sha256(bytes(str(event_id), 'utf-8') + bytes(hashed_passwd, 'utf-8') + bytes(config.solt, 'utf-8')).hexdigest()


def check_password(passwd: str, event: EventSchema):
    return hash_passwd(passwd) == event.passwd


def check_session(session: str, event: EventSchema):
    return session == create_session(event.id, event.passwd)


def check_signin(db: Session, event_id: int, session: Union[str, None]):
    if(session is None):
        raise ForbiddenException
    event = query.get_event(db, event_id)
    if(not check_session(session, event)):
        raise ForbiddenException


SESSION_KEY = "JSESSION"
