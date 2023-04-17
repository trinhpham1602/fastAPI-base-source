from pydantic import BaseModel
from constants import EMPTY_STR
class Message(BaseModel):
    message: str = EMPTY_STR
    success: bool = True
    error: bool = False