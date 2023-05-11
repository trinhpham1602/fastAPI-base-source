from http.client import HTTPException
from fastapi import APIRouter, Depends, status
from database.db_config import get_db
from models.auth_model import MConfirmPassword, MLogin
from models.user_model import MRegisterUser
import services.auth_service as auth_service
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/sign-in")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    loginPayload = MLogin(username, password)
    auth = await auth_service.login(loginPayload)
    return auth


@router.post("/sign-up")
async def sign_up(register_user: MRegisterUser, db_session: Session = Depends(get_db)):
    await auth_service.create_user(register_user, db_session)


@router.post("/change-password")
def change_password(payload: MConfirmPassword):
    pass
