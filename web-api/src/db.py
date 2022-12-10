from random import random
import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import db_config
import utils.logger as logger

if (db_config.get('DB') == 'sqlite'):
    SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite3"
elif(db_config.get('DB') == 'mysql'):
    SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://{user}:{password}@{host}:{port}/{database}".format(
        user=db_config.get("DB_USER"),
        password=db_config.get("DB_PASSWORD"),
        host=db_config.get("DB_HOST"),
        port=db_config.get("DB_PORT"),
        database=db_config.get("DB_DATABASE")
    )
else:
    logger.warn(f"invalid db settings: DB={db_config.get('DB')}")
    exit(-1)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def idgen() -> str:
    current = int(time.time() * 1000)
    return f"{current - 1654319790000}{int(random() * 1000)}"
