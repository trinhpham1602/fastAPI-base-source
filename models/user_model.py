from pydantic import BaseModel
from typing import ClassVar

from models.enum_model import ESex, ERole
from models.auth_model import MConfirmPassword
import datetime
import uuid

class MUser(BaseModel):
    id: ClassVar[uuid.UUID] = None
    name: str
    fullname: str
    email: str
    password: str
    role: ERole
    sex: ESex
    birthday: datetime.date
    is_active: bool

class MRegisterUser(MUser, MConfirmPassword):
    pass