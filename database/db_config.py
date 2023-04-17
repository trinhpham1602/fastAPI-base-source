from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os
load_dotenv()

NAME = os.getenv('NAME')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DB = os.getenv('DB')

engine = create_engine(f'postgresql://{NAME}:{PASSWORD}@{HOST}:{PORT}/{DB}')
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db() -> Session:
    db = session_local()
    try:
        yield db
    finally:
        db.close()