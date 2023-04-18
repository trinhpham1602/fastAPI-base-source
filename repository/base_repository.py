from sqlalchemy.orm import Session
from abc import ABC, abstractmethod


class BaseRepository(ABC):
    def __init__(self, db_session: Session):
        self.db_session = db_session
