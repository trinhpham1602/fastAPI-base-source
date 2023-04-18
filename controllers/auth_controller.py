from fastapi import APIRouter, Depends, Request
from models.auth_model import MLogin, MConfirmPassword
from models.user_model import MRegisterUser
from services.user_service import UserService
from repository.user_repository import UserRepository
from .base_controller import BaseController


class AuthController(BaseController):

    def __init__(self, router: APIRouter, service: UserService):
        super().__init__(router, service)
        self.service = service

    def configure_routes(self):
        @self.router.post("/sign-in")
        def login(payload: MLogin):
            pass

        @self.router.post("/sign-up")
        def sign_up(register_user: MRegisterUser):
            self.service.create_user(register_user)

        @self.router.post("/change-password")
        def change_password(payload: MConfirmPassword):
            pass
