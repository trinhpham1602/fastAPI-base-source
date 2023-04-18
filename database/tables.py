import os
from sqlalchemy import Boolean, Column, String, Date
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database.db_config import Base
import bcrypt
from dotenv import load_dotenv

load_dotenv()

SALF = os.getenv('SALF')

class User(Base):
    __tablename__ = "user_table"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String)
    fullname = Column(String)
    email = Column(String, index=True, unique=True)
    password = Column(String)
    role = Column(String)
    sex = Column(String)
    birthday = Column(Date) 
    is_active = Column(Boolean, default=True)
    joined_at = Column(Date)

    def is_match_password(self, password):
        if bcrypt.checkpw(password, self.hashed_password):
            return True
        return False

    def hash_password(self):
        self.password = bcrypt.hashpw(self.password, SALF)
