from fastapi import Depends, FastAPI, Request, APIRouter
from sqlalchemy.orm import Session
from database.db_config import engine, get_db
from repository.user_repository import UserRepository
from services.user_service import UserService
from controllers.auth_controller import AuthController

import database.tables as tables

# create all tables
app = FastAPI()


@app.on_event("startup")
async def startup():
    tables.Base.metadata.create_all(bind=engine)

# initialize database session
db_session: Session = next(get_db())
 
# initialize repositories
user_repo = UserRepository(db_session)

# initialize services
user_service = UserService(user_repo)

# initialize routers
auth_router = APIRouter()

# initialize controllers
auth_controller = AuthController(auth_router, user_service)




# middleware

# include route
app.include_router(auth_router, prefix='/api/v1/auth')
