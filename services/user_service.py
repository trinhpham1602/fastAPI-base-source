from fastapi import HTTPException, status
from models.user_model import MRegisterUser
from validations.user_validation import is_valid_date, is_valid_email
from error_messages import DONT_MATCH_PASSWORD, INVALID_BIRTHDAY, INVALID_EMAIL_ADDRESS
from .base_service import BaseService
from repository.user_repository import UserRepository
from sqlalchemy.orm import Session


class UserService(BaseService):
    def __init__(self, user_repo: UserRepository):
        super().__init__(user_repo)
        self.user_repo = user_repo

    def create_user(self, register_user: MRegisterUser):

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
        
        self.user_repo.create_user(register_user)
