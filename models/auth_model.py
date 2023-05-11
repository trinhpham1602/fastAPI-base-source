from pydantic import BaseModel

class MLogin(BaseModel):
    username: str
    password: str

class MConfirmPassword(MLogin):
    confirm_password: str


class MAuth(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = 'bearer'
