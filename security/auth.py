from dotenv import load_dotenv
import os
from fastapi import Depends
import jwt
from sqlalchemy.orm import Session, query

from database.tables import User

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

def get_current_user(token: str):
    return jwt.decode(token, SECRET_KEY)

def is_email_exist(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    if user:
        return True
    return False

