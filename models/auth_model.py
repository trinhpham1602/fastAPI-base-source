from pydantic import BaseModel

class MLogin(BaseModel):
    email: str
    password: str

class MConfirmPassword(MLogin):
    confirm_password: str

