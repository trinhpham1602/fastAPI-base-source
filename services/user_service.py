from fastapi import Depends, HTTPException, status, Request
from repository.user_repository import UserRepository
from models.user_model import MRegisterUser
from validations.user_validaiton import is_valid_email
from error_messages import INVALID_EMAIL_ADDRESS
class UserService:
    def __init__(self, user_repo: UserRepository) -> None:
        self.user_repo = user_repo
    def create_user(self, user: MRegisterUser):
        if is_valid_email(user.email):
            self.user_repo.create_user(user)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=INVALID_EMAIL_ADDRESS)
        
