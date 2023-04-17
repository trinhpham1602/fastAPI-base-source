from fastapi import Depends, FastAPI, Request
from sqlalchemy.orm import Session
from database.db_config import engine, get_db
from controllers.auth_controller import auth_router
from repository.abstract_repository import AbstractRepository

import database.tables as tables

# create all tables



app = FastAPI()
@app.on_event("startup")
async def startup():
    tables.Base.metadata.create_all(bind=engine)

def get_abstract_repository(db: Session = Depends(get_db)):
    return AbstractRepository(db)

# dependencies
app.dependency_overrides[get_abstract_repository] = get_abstract_repository

# middleware

# include route
app.include_router(auth_router, prefix='/api/v1/auth')
