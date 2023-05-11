from fastapi import APIRouter
from models.auth_model import MLogin

router = APIRouter()


@router.post("/me")
def get_current_user(payload: MLogin):
    pass
