from abc import ABC
from sqlalchemy.orm import Session
class AbstractRepository(ABC):
    def __init__(self, db: Session) -> None:
        super().__init__()
        self.db = db