import datetime
from database.db_config import get_db
from models.user_model import MUser
from database.tables import User
from logs.log_config import logging
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session


async def create_user(user: MUser, db_session: Session):
    try:
        target: User = User()
        target.name = user.name
        target.fullname = user.fullname
        target.email = user.email
        target.password = user.password
        target.role = user.role
        target.sex = user.sex
        target.birthday = user.birthday
        target.is_active = user.is_active
        target.joined_at = datetime.date.today()
        target.hash_password()
        db_session.add(target)
        db_session.commit()
        db_session.close()
        return user
    except SQLAlchemyError as e:
        time = datetime.datetime().now()
        logging.exception(f'ERROR occur {time}: {e}')


async def get_user_by_email(email: str):
    try:
        user: User = db_session.query(
            User).filter(User.email == email)
        return user
    except SQLAlchemyError as e:
        time = datetime.datetime().now()
        logging.exception(f'ERROR occur {time}: {e}')
