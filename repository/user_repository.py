from fastapi import Depends
from database.db_config import get_db
from sqlalchemy.orm import Session
from models.user_model import MRegisterUser
from database.tables import User
from .abstract_repository import AbstractRepository

class UserRepository(AbstractRepository):
    def __init__(self) -> None:
        pass
    def create_user(self, user: MRegisterUser):
        user: User = User(name=user.name,
fullname=user.fullname,
email=user.email,
password=user.password,
role=user.role,
sex=user.sex,
birthday=user.birthday,
is_active=user.is_active)
        self.db.add(user)
        self.db.commit()
        self.db.close()