import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
LOCAL_SQLITE_URL = f"sqlite:///{DATA_DIR / 'festival_local.db'}"


def get_database_url() -> str:
    mysql_url = os.getenv("MYSQL_URL")
    if mysql_url and mysql_url.strip():
        return mysql_url.strip()
    return LOCAL_SQLITE_URL


def get_engine():
    return create_engine(get_database_url(), echo=False, future=True)


SessionLocal = sessionmaker(bind=get_engine(), autocommit=False, autoflush=False, future=True)


def init_db() -> None:
    from src.models import Base

    Base.metadata.create_all(bind=get_engine())


def get_session():
    return SessionLocal()
