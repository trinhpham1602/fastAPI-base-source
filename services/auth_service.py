from fastapi import HTTPException, status
from models.auth_model import MAuth, MLogin
from models.user_model import MRegisterUser, MUser
from error_messages import DONT_MATCH_PASSWORD, INCORRECT_USERNAME_PASSWORD, INTERNAL_ERROR, INVALID_BIRTHDAY, INVALID_EMAIL_ADDRESS
from validations.user_validation import is_valid_date, is_valid_email
from fastapi.responses import JSONResponse
import jwt
from dotenv import load_dotenv
import os
import repository.user_repository as user_repo
from sqlalchemy.orm import Session
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')


async def login(user: MLogin):
    email = user.username
    password = user.password
    user_db = await user_repo.get_user_by_email(email)
    if not user_db or not user_db.is_match_password(password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=INCORRECT_USERNAME_PASSWORD)
    user_info = MUser(user_db.__dict__)
    auth = generate_token(user_info)
    return JSONResponse(content=auth, status_code=status.HTTP_200_OK)


def generate_token(user: MUser):
    access_expired = 1
    refresh_expired = 30
    payload: dict = {}
    payload['userInfo'] = user
    payload['expired'] = access_expired
    access_token = jwt.encode(payload, key=SECRET_KEY)
    payload['expired'] = refresh_expired
    refresh_token = jwt.encode(payload, key=SECRET_KEY)
    auth: MAuth = MAuth(access_token, refresh_token)
    return auth


async def create_user(register_user: MRegisterUser, db_session: Session):
    email = register_user.email
    if not is_valid_email(email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=INVALID_EMAIL_ADDRESS)

    password = register_user.password
    confirm_password = register_user.confirm_password
    if password != confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=DONT_MATCH_PASSWORD)

    date_string = register_user.birthday
    if not is_valid_date(date_string):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=INVALID_BIRTHDAY)
    try:
        user = await user_repo.create_user(register_user, db_session)
        return JSONResponse(content=user, status_code=status.HTTP_201_CREATED)
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=INTERNAL_ERROR)
