from typing import Union

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel

from app.routes import users
from app.routes.auth import token

from app.models.user import User
from app.models.token import Token, TokenData


app = FastAPI()


# @app.get("/users/me/", response_model=User)
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#    return current_user
app.include_router(
    users.router,
    tags=["Users"],
    prefix="/users"
)


app.include_router(
    token.router,
    tags=["Token"],
    prefix=""
)
