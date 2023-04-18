import datetime
from sqlalchemy.orm import Session
from models.user_model import MUser
from database.tables import User
from .base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, db_session: Session):
        super().__init__(db_session)

    def create_user(self, user: MUser):
        user: User = User(**user.dict())
        user.hash_password()
        user.joined_at = datetime.date()
        self.db_session.add(user)
        self.db_session.commit()
        self.db_session.close()
