from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from database.db_config import engine
from controllers.auth_controller import router as auth_router
from controllers.user_controller import router as user_router
from controllers.file_controller import router as file_router

import database.tables as tables

# create all tables
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/sign-in")

# middleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    tables.Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix='/api/v1/auth')
app.include_router(user_router, prefix='/api/v1/users',
                   dependencies=[Depends(oauth2_scheme)])
app.include_router(file_router, prefix='/api/v1/files')
