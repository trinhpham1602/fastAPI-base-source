from fastapi import APIRouter, Depends, Request
from models.auth_model import MLogin, MConfirmPassword
from models.user_model import MRegisterUser
from services.user_service import UserService
from repository.user_repository import UserRepository
auth_router = APIRouter()
user_repo = UserRepository()
user_service = UserService(user_repo)

@auth_router.post("/sign-in")
def login(payload: MLogin):
    pass

@auth_router.post("/sign-up")
def sign_up(payload: MRegisterUser):
    user_service.create_user(payload)

@auth_router.post("/change-password")
def change_password(payload: MConfirmPassword):
    pass
