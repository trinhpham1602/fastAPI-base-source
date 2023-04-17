from fastapi import APIRouter
from models.user_model import MUser
import uuid
user_router = APIRouter()

@user_router.post("/users")
def create_user(payload: MUser):
    return None

@user_router.get("/users")
def get_user_list():
    return None

@user_router.get("/me")
def get_me():
    return None

@user_router.post("/users/{user_id}")
def get_user_info(user_id: uuid.UUID):
    return None
